# AIBTC Wallet Signatures & Public Proofs

**Know what you sign and what it authorizes.**

This repository explains how AIBTC connects to Bitcoin wallets, verifies sign-in messages, authorizes trading, and handles transaction signing and withdrawals. It includes selected implementation excerpts and the existing Merkle reference script.

AIBTC uses your wallet's connection and signing APIs. It does not ask you to enter or upload your seed phrase or private keys. Your wallet signs locally; the application receives public account information, message signatures, or signed transaction data.

```text
Connect a wallet   → Read public account information
Sign in           → Verify identity and start a session
Authorize trading → Grant specific in-app permissions
Sign a transaction → Approve a specific on-chain transaction
```

Values in `{braces}` are filled in for each request. Code excerpts show the relevant parts of the implementation, with unrelated context omitted.

## 1. Connecting your wallet

The application reads your Bitcoin address and network from the wallet you select. It checks that subsequent signing requests still belong to the same account. Some transactions also require a public key to verify the address or prepare a PSBT. A public key is not a private key.

New wallet registrations and supported withdrawal destinations use:

- **Taproot (P2TR):** Bitcoin mainnet addresses beginning with `bc1p`.
- **Native SegWit (P2WPKH):** Bitcoin mainnet addresses beginning with `bc1q`, identified by their actual script. Not every `bc1q` address is P2WPKH.

Connecting a wallet and signing a transaction are separate steps. A connection does not replace the approval required for a later signing request.

For example, the UniSat adapter requests a message signature through the wallet's existing API:

```ts
const signature = await provider.signMessage(
  input.message,
  "bip322-simple"
);
```

The call passes a message to the wallet and receives a signature. It does not read or export the user's private key.

Implementation reference: `apps/web/lib/wallet-adapters.ts`.

## 2. Signing in

Wallet sign-in uses **[BIP-322 message signing](https://bips.dev/322/)**. The platform creates a one-time challenge, your wallet signs the message, and the server verifies the signature against the address and challenge.

```text
Select your wallet and address
    ↓
Receive a one-time sign-in message
    ↓
Sign the message in your wallet
    ↓
The server verifies and marks the challenge as used
    ↓
Your platform session begins
```

The current sign-in message has this format:

```text
AIBRC Wallet Login

Domain: {domain}
Purpose: Sign in to AIBRC V1. This signature is not a transaction and does not authorize spending.
Address: {address}
Network: {network}
Wallet Type: {wallet_type}
Nonce: {nonce}
Expires At: {expires_at}
```

`Domain` identifies the site. `Address` and `Network` identify the account. `Nonce` is the random value for this challenge, and `Expires At` is the submission deadline. Sign-in challenges currently expire after **five minutes** and cannot be used again after a successful sign-in.

The server verifies the address, network, message, and signature:

```ts
const verification = await this.signatureVerifier.verifyMessage({
  address: wallet.address,
  network: wallet.network,
  walletType: wallet.walletType,
  message: input.message,
  signature: input.signature
});

if (!verification.valid) {
  throw new UnauthorizedException(verification.reason);
}
```

It also requires an exact match with the original challenge, checks that the challenge is unexpired and unused, and marks it as used within a database transaction.

**This message is not a Bitcoin payment transaction.** A successful signature establishes a platform session. Trading requires the relevant authorization described below. When an account is first registered through a wallet, that address is also recorded as its withdrawal destination. Binding a destination to an existing account uses a separate account-security confirmation.

Implementation references: `buildWalletLoginMessage()` and `verifyWalletLogin()` in `wallet-auth.service.ts`, and `btc-wallet-signature-verifier.ts`.

## 3. Trading permissions and trade confirmations

### Trade Session authorization

A Trade Session signature grants specific **in-app asset permissions**, such as creating a market, buying, selling, adding or removing liquidity, and claiming LP fees. It is not a Bitcoin payment signature, but it does authorize actions affecting your platform balances.

The current authorization message has this format:

```text
AIBRC Trade Session

Domain: {domain}
Purpose: AIBRC internal trade session authorization
Account Reference: {account_reference}
Wallet Address: {address}
Wallet Network: {network}
Wallet Type: {wallet_type}
Scopes: {scopes}
Nonce: {nonce}
Issued At: {issued_at}
Expires At: {expires_at}
This signature authorizes an AIBRC internal trade session.
It is not a Bitcoin transaction and cannot spend on-chain BTC.
```

`Scopes` lists the permissions requested for that session. The implementation supports:

```text
AMM_BUY / AMM_SELL
LAUNCH_BUY / LAUNCH_SELL / LAUNCH_CREATE
LIQUIDITY_ADD / LIQUIDITY_REMOVE
LP_FEE_CLAIM
```

The platform verifies the signature and the account's wallet binding. Protected requests check the session's permissions, expiry, and revocation status.

The message's `Expires At` field is the deadline for submitting that challenge. The issued Trade Session has its own expiry, returned in the session response. These are separate deadlines.

### Confirming an individual trade

The web application also asks your wallet to confirm individual buys and sells. The message identifies the market, side, input amount, minimum output, and relevant fee information. It begins with:

```text
AIBRC — confirm this web trade
Market name: {market_name}
Purpose: browser confirmation only; not authorization renewal or an on-chain transaction.
```

This signature is a browser confirmation. **It is not submitted as a per-order signature proof to the server, and it does not renew the Trade Session.** After confirmation, the page rechecks the active account and session, then submits the order with the selected protections. The server accepts the request based on its authorization and business rules.

Implementation references: `trade-session.service.ts`, `trade-session.types.ts`, `trade-session-authorization.ts`, and `trade-confirmation.ts`.

## 4. On-chain transactions: what your wallet signs

Deposits, Block Swaps, and AIBRC withdrawals involve real on-chain transactions. A **PSBT**—Partially Signed Bitcoin Transaction—contains transaction data for a wallet to inspect and sign. It does not contain the user's private keys.

| Action | Current signing flow |
| --- | --- |
| BTC deposit from a wallet | The wallet's transfer API handles payment confirmation, signing, and broadcast. |
| AIBRC deposit from a wallet | The wallet signs designated user inputs: DEFAULT for P2TR, ALL for P2WPKH. |
| Block Swap buy | User inputs use SINGLE. The platform checks the complete transaction, then signs its own authorization input with DEFAULT. |
| AIBRC withdrawal | User inputs use DEFAULT or ALL. The platform checks the complete transaction, then signs its own authorization input with DEFAULT. |

These signature modes mean:

- **ALL (`0x01`):** commits to every output in the transaction, including its amount and destination script.
- **DEFAULT (`0x00`):** the default Taproot signature mode, which also commits to every output.
- **SINGLE (`0x03`):** commits to the output at the same index as the signed input. Block Swap buys currently use this mode without `ANYONECANPAY`.

**“ALL” refers to the outputs of this transaction, not all the assets in your wallet.** These are existing Bitcoin signature rules; see [BIP-341](https://bips.dev/341/).

The handshake adapter reads the input indices, addresses, and signature modes from the preview:

```ts
const toSignInputs = preview.wallet_sign_inputs.map(s => ({
  index: s.index,
  address: s.address,
  sighashTypes: [...s.sighash_types]
}));
```

It then calls the wallet's PSBT signing API:

```ts
result = await waitForWalletOperation(
  p.signPsbt!.call(selected, unsignedHex, {
    autoFinalized: false,
    toSignInputs
  }),
  local.signal
);
```

For a Block Swap buy, the user's SINGLE signature does not, by itself, commit to every asset-delivery output. The platform also checks the complete transaction—including the asset instruction, inputs, amounts, destination scripts, and fees—before signing its own authorization input. Each party signs its own inputs in the same transaction.

The output checks include:

```ts
transaction.outs.forEach((actual, i) => {
  const expected = template.outs[i]!;
  if (actual.value !== expected.value || !actual.script.equals(expected.script))
    fail("TRANSACTION_TEMPLATE_MISMATCH");
});
```

Implementation references: `handshake-wallet-psbt-adapter.ts`, `handshake-wallet-psbt.ts`, and `handshake-core.ts`.

## 5. Withdrawals: browser confirmation and PSBT co-signing

### Confirming a BTC withdrawal

The BTC withdrawal page displays the destination, total balance debit, estimated amount received, fee rate, and maximum miner fee. If a wallet is connected, it signs a message confirming these details before the page submits the withdrawal request.

The existing English confirmation message has this format:

```text
aibtc — confirm withdrawal
Browser confirmation only; not an on-chain transaction or authorization renewal.
Site: {origin}
Network: {network}
Wallet: {wallet_address}
Asset: {asset_label}
Destination: {destination}
Amount (total BTC balance debit, sats): {amount_sats}
Estimated received BTC: {estimated_received_sats} sats
Service fee: {platform_fee_sats} sats (included in total debit)
Miner fee rate: {fee_rate} sat/vB
Maximum miner fee (not the estimate): {maximum_miner_fee_sats} sats
The received amount is an estimate; the actual miner fee stays within the confirmed maximum.
Nothing is submitted before you confirm. The confirmed fee rate is retained while you wait.
```

This message signature stays in the browser. It confirms the request; it is not the user's on-chain signature on the final BTC payout transaction. The withdrawal flow handles the payout and records the transaction identity and outcome.

Implementation references: `withdrawal-confirmation.ts` and `withdrawal-confirmation-copy.ts`.

### Withdrawing AIBRC through the PSBT handshake

AIBRC withdrawals use the transaction-signing flow described above:

```text
Review the asset amount, destination, and fees
    ↓
Your wallet signs the designated user inputs
    ↓
The platform checks the transaction and signs its input
    ↓
The transaction is broadcast and its txid recorded
    ↓
Chain confirmations and protocol results are tracked
```

Your wallet signs the payment inputs you provide. The platform signs its authorization input. Before co-signing, it checks the submitted transaction and signatures against the original request and preview, including the recipient.

## 6. From authorization to execution and public proofs

**Your signature authorizes an action. Smart Covenant rules govern execution. The public ledger records the result.**

| Layer | What it does |
| --- | --- |
| Wallet signatures and session authorization | Establish identity, grant specific permissions, or approve an on-chain transaction. |
| Smart Covenant rules and execution code | Check amounts, fees, recipients, and state changes against the applicable rule version, parameters, and current state. |
| Public records and Merkle proofs | Commit to the published records and their order, with inclusion proofs and consistency material between checkpoints. |
| OTS and Bitcoin | Link a batch digest to a proof that it existed by a particular Bitcoin block. |

### How an action becomes a public proof

```text
The user authorizes an action
    ↓
AIBTC CORE executes the applicable rules
    ↓
The business result and pending event are saved
    ↓
A public record and event_hash are produced
    ↓
The record enters the global Merkle tree
    ↓
OTS anchors the checkpoint digest to Bitcoin
    ↓
Users and Agents can obtain the record and proof
```

For an AMM trade, the implementation captures the event in the same business transaction as the reserve update and fee handling. Published records include rule identifiers and disclosed execution data, such as:

- `rulesetHash` and `sourceRevision`: the rule-set and source-version identifiers.
- `formulaVersion` and `feePolicyVersion`: the formula and fee policy used for that record.
- `amountIn`, `amountOut`, and `feeBtcSats`: input, output, and fee amounts.
- `btcReserveSatsBefore` / `btcReserveSatsAfter` and `tokenReserveAmountBefore` / `tokenReserveAmountAfter`: the corresponding reserve changes.

These fields connect a record to the rules used to interpret it. Where the disclosed data is sufficient, a user or Agent can recompute the result using the same formula.

For example, the current AMM buy rules include this integer calculation:

```ts
const expectedOut = price.token * amountIn / (price.btc + amountIn);
```

`price` is the pricing state used for that trade. If pending Block Swap buys affected the quote, the record's additional pricing parameters must also be used. Fees and rounding follow the policy version recorded for that trade.

### Merkle proof v2

Public records are linked by hash and added to an RFC 9162 global Merkle tree. Each checkpoint commits to the tree size, root, log epoch, previous checkpoint digest, and other batch metadata. OTS then anchors the checkpoint digest to Bitcoin.

```text
Record → event_hash → inclusion path → treeRoot
                                         ↓
                         Checkpoint digest → OTS → Bitcoin
```

The explorer's **Copy proof** action provides the original record, inclusion path, checkpoint manifest, OTS file, and Bitcoin block information. When material for both an earlier and a later checkpoint is supplied, the corresponding append-only relationship can also be checked.

**Record integrity and trade calculations are separate checks.** Merkle proofs check inclusion in a committed history. Trade results are recomputed under the applicable rules. OTS and Bitcoin establish the digest's anchor. Bitcoin does not execute the platform's internal ledger code.

Digests are anchored in batches. Each in-app trade does not require its own Bitcoin transaction.

## 7. Cancellation, sign-out, and unknown outcomes

If you cancel before submission, the page stops that attempt and checks that any late signing response still belongs to the active account and request.

Once a request has been submitted or a transaction broadcast, its outcome must be checked using the original request or transaction ID. Closing the page, signing out, or reaching a timeout does not establish that nothing happened. An unknown outcome is recovered through the original request, not treated as a reason to create another payment.

## 8. Reference verification script

This repository includes the existing reference script linked from the explorer:

[`proofs/aibrc-merkle-reference-v3.py`](proofs/aibrc-merkle-reference-v3.py)

It uses the Python 3 standard library. No wallet connection, platform login, private key, or database access is required. It reads the local proof file you specify and makes no network requests.

### Usage

Use **Copy proof** on a record's detail page and save the complete text as `copied-proof.txt`. Then run:

```sh
python3 proofs/aibrc-merkle-reference-v3.py copied-proof.txt
```

You can keep the instructions preceding the JSON in the copied text. The script also accepts the corresponding JSON proof material directly.

### What it checks

- The record's fields and event fingerprint.
- The checkpoint manifest fingerprint and `checkpoint_digest`.
- The record's inclusion path against the checkpoint's Merkle root.
- The append-only relationship when both checkpoints and the consistency material are supplied.
- The OTS file's content fingerprint and the digest committed in its header.

For a complete proof copy that passes the applicable checks, the script prints:

```text
FINGERPRINTS_AND_MERKLE_MATCHED_OTS_BITCOIN_NOT_VERIFIED
```

This means the record and manifest fingerprints and the Merkle relations match. **The script has not completed the OTS-to-Bitcoin verification.** Follow **AiBTC Verification Method v2**, included in the copied proof, to check the OTS operations, the actual Bitcoin block, and the supported trade formulas separately. The script does not mark those steps as verified.

When checking a standalone inclusion or consistency bundle, success is reported as `MERKLE_MATCHED_ONLY`. Mismatched or invalid material produces an error result and a nonzero exit code.

### Version names

The user-facing documentation calls this **Merkle proof v2** and **AiBTC Verification Method v2**. The underlying checkpoint manifest is `AIBRC_CHECKPOINT_MANIFEST_V3`, while the complete copied-proof format is `AIBRC_EXPLORER_PROOF_COPY_V2`. The reference script retains its existing `v3` filename to keep these separate version identifiers accurate.

The original SHA-256 checksum file is included alongside the script. Both files match the web application's public source files byte for byte.

## Source version

This document is based on source revision:

```text
7ec073658d77507851d05516024a6261ce390d05
```

Signing-message examples preserve the implementation's wording. Code excerpts are taken from the relevant functions, with minor line wrapping for readability. This repository documents wallet interactions, signing rules, and the existing Merkle reference script. It contains no private keys, session credentials, production configuration, or real users' signing data.
