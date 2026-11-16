# Atom Unit Protocol

AIBTC CORE records balances and executes Swaps. Atom Unit supports deposits, verifies transactions and handles protocol signing.

## Reserves

Users and their Agents can verify their own on-chain reserves. Atomic unit model: no unified reserve address, no fund consolidation.

Verifiable: the account's deposit address, each deposit and withdrawal, and the TxID of each Block Swap; liquidity reserves are recomputed with the public method.

Each account has a fixed deposit address. Assets belong to the account of the sign-in address, and balances follow the AIBTC CORE ledger. Each asset has one protocol address that holds its Atomic Swap Units.

Use the [public verification method](verification/METHOD_v2.en.md) to recompute market liquidity reserves from the trade proofs.

## From your wallet to a Swap

Instant Swap: uses the available balance of the AiBTC account; deposit first if it is not enough.

Block Swap: pays with BTC straight from the wallet, with no deposit to AiBTC first; the AIBRC received goes straight to the linked wallet.

```text
Deposit if needed → AiBTC account balance → Instant Swap → Optional withdrawal
Wallet BTC        → Block Swap PSBT      → AIBRC in your linked wallet
```

See [AIBTC Swap](guide/03-swap.md#c3-s1) and [deposit instructions](support.md#support-s6).

## Withdrawals and signing

BTC withdrawal (mutual signing): the receiving address is authorized by the user's signature, and withdrawals pay only to that address; Atom Unit verifies, then signs.

AIBRC withdrawal and Block Swap (co-signing): the user's wallet and Atom Unit each sign their own inputs in the same Bitcoin transaction.

Both use the same Atom Unit. AIBRC withdrawal opens after graduation.

Broadcast: outside Atom Unit, by the local Bitcoin Core node.

Check the original record and its TxID to follow confirmations. See [withdrawal instructions](support.md#support-s7).
