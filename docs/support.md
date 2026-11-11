# Support Center

## Community channels & contact {#support-s2}

**Security first: hold your BTC and AIBRC in your own cold wallet. Leave only what you trade.**

| Type | Entry |
| --- | --- |
| Main platform domain | [aibtc.bot](https://aibtc.bot) |
| Documentation | [aibtc.io](https://aibtc.io) |
| Platform backup entry | [aibrc.fun](https://aibrc.fun) |
| AIBRC protocol site | [aibrc.io](https://aibrc.io) |
| Telegram · community | [t.me/aibtc](https://t.me/aibtc) |
| X · announcements & news | [x.com/aibtc_bot](https://x.com/aibtc_bot) |
| GitHub · wallet signatures & public proofs | [github.com/aibtcbot/aibtcbot](https://github.com/aibtcbot/aibtcbot) |
| Support email | [aibtc.bot@aibtc.bot](mailto:aibtc.bot@aibtc.bot) |

Use the main domain first; if you have trouble reaching it, check the platform announcements or a backup entry. The protocol site is for the AIBRC specification and developer resources; do not confuse it with platform account pages.

Telegram and X are for community chat and announcements. Send account issue details to the support email. Keep sensitive information out of public group chats.

## Read first | Before you email support {#support-s1}

This support guide helps with common connection, sign-in, signing, deposit and withdrawal issues on AiBTC. Before emailing support, look up the matching notes and try the suggested fixes. The official docs cover trading, confirmation and account rules.

For an action you have already submitted, check its progress in the original record. A page timeout does not mean the transaction failed; do not pay again to test whether it has recovered.

Keep your original email and reply in the same thread with any new information.

1. 1. Look up your issue in this support guide and complete the checks that match your situation.
2. 2. Search the official docs and check the assets, addresses, fees and confirmation conditions involved.
3. 3. If it is still unresolved, send the details to the support email listed on this page.

If you suspect your wallet or account has been stolen, take the security steps in section 5 immediately.

### Submit by email

Support email: [aibtc.bot@aibtc.bot](mailto:aibtc.bot@aibtc.bot)

Write the issue, original order ID, transaction hash and error message directly in the email body. Use plain text and leave out images, attachments, archives, full log exports and signature files.

Use a subject such as “Issue type | original order ID or txid”. The original order follows the applicable execution rules and Bitcoin confirmation conditions.

## Important security reminders {#support-s3}

**No one, including people claiming to be AiBTC support, community volunteers or wallet staff, should ever ask for your seed phrase, private key, password, verification code or cookie.** Never enter these into so-called “verify”, “fix”, “sync” or “unfreeze” pages.

Wallet addresses and txids are public on-chain identifiers. You can give them to the community volunteers and the platform Agent when really needed, but consider the privacy impact once they are linked to your identity. They are not the same kind of information as the private keys and seed phrases that control assets.

Check the full domain even when your browser shows a secure HTTPS connection. Watch for extra characters, look-alike letters and different suffixes. In aibtc.bot.example.com, the domain is example.com.

Treat any stranger who contacts you first and asks you to move funds, download tools, allow remote control or sign as a potential scam, and verify independently through the channels listed on this page.

## 1. Wallet connection & signing {#support-s4}

### 1.1 The wallet won't connect, keeps asking to connect, or doesn't respond

Check these in order:

1. 1. Update your wallet and browser; make sure the wallet is unlocked and the extension is enabled.
2. 2. Make sure you are on Bitcoin mainnet and the wallet address matches the address you intend to use.
3. 3. Check the wallet window or app and handle any pending connection, authorization or signing prompt.
4. 4. Disconnect the current connection in both the wallet and AiBTC, then connect again.
5. 5. Hard-refresh the page: usually Ctrl + Shift + R on Windows and Command + Shift + R on Mac.
6. 6. If you have several wallet extensions, check that you connected the wallet you intended; temporarily disable a conflicting extension if needed.

On a phone, open aibtc.bot in your wallet's built-in browser first. An ordinary mobile browser may not have the connection and signing abilities that wallet needs.

A failed sign-in or connection can simply be retried. Once you have signed or submitted, or a transaction hash has appeared, check the original record first. Do not keep confirming repeated requests, and do not clear site storage before checking.

### 1.2 How do I use Binance Wallet? Why are there several pop-ups?

Open aibtc.bot in **the wallet's built-in browser in the Binance app**. Connecting Binance Wallet from an ordinary web browser to sign in to AiBTC is not supported at the moment.

Connection confirmation, account-action authorization and transaction signing are separate steps. When the connection was not kept or has expired, you need to reconnect and confirm the address before authorizing and signing, so several pop-ups may appear.

```text
Open AiBTC in the Binance app's built-in browser
    ↓
Connect the wallet and confirm the current address
    ↓
Authorize the account or sign the transaction for the action
    ↓
Check the result in the original record
```

The number of pop-ups is not the number of payments. A connection prompt itself makes no on-chain transfer; for a real transaction, check the amount, address, fees and original transaction hash.

If the same prompt keeps looping, the address changes, or the content has nothing to do with this action, stop confirming and check the connection again.

### 1.3 What is the difference between a sign-in signature and a transaction signature?

A sign-in signature proves that you own the address; it makes no on-chain transfer and needs no network fee. A transaction signature authorizes a specific action; check the asset, amount, address and fees before you sign. Open-source reference: [GitHub · aibtcbot/aibtcbot](https://github.com/aibtcbot/aibtcbot)

```text
Sign-in signature → proves “I control this address”
Transaction signature → confirms “I authorize this action”
```

A signature is not a broadcast, and a broadcast is not yet in a block. The result follows the original record and its on-chain confirmations.

### 1.4 Which Bitcoin addresses are supported?

Two mainnet address types are supported:

| Address type | Usually looks like |
| --- | --- |
| Taproot · P2TR | Starts with bc1p |
| Native SegWit · P2WPKH | A single-key address starting with bc1q |

Not every bc1q address is P2WPKH. The system identifies the actual script, not just the address prefix.

Two supported address types does not mean only two supported wallets. Connecting, signing in and signing transactions also depend on what the wallet offers on your current device; if the page says it is not compatible, follow the prompt.

## 2. Email sign-in & address linking {#support-s5}

### 2.1 I don't receive the sign-in code

AiBTC uses Privy for email and social sign-in verification. Please check:

- Whether the email address is correct, with no spaces or typos.
- Your spam, promotions, updates and other category folders.
- Whether the mailbox is full, or has auto-delete or blocking rules.
- Whether a company or school mailbox applies organization-level filtering or quarantine.

If you once marked the code email as spam, restore it and add the verified sender to your safe senders list. Request a new code as the sign-in window instructs; do not keep clicking send.

If it still doesn't arrive, report the request time, time zone, device and email provider through the channels listed in the [Privy Help Center](https://www.privy.io/user-help-center). Never send the code.

### 2.2 Why do I still need to link a Bitcoin address after email sign-in?

Email and social accounts are for sign-in; the Bitcoin wallet is for proving address ownership and for actions that need a wallet signature.

```text
Sign in with email or a social account
    ↓
Link a Bitcoin address you control
    ↓
Use the features that need wallet authorization
```

Before linking, check the address type and make sure you can keep using that wallet. Email sign-in cannot replace transaction signing, and it never gives the platform your external wallet's private key.

### 2.3 I don't see my earlier assets after signing in

First confirm you are using your original sign-in method, account and linked address. Do not deposit again or link another address just because the display looks different.

If you still have questions after checking, keep the original records and report as described in section 5. Switching wallet software or addresses does not automatically move your platform account or its linked address.

## 3. Deposits & crediting {#support-s6}

### 3.1 My deposit hasn't arrived. Where do I look first?

Open the original deposit record under “Assets” and check the address it was sent to, the amount, the broadcast, the confirmation progress and the exact status.

An ordinary BTC deposit is usually credited after 1 Bitcoin block confirmation and system verification. There may still be processing time between reaching the confirmations and the balance updating on the page; go by the conditions shown in the original record.

```text
Deposit
    ↓
Send BTC to your account's fixed deposit address
    ↓
The Bitcoin L1 transfer enters a block · usually 1 confirmation
    ↓
The system verifies the transaction, amount and current main chain
    ↓
The AIBTC CORE ledger records it and the account balance updates
```

Each account has its own fixed BTC deposit address. Copy and check it from your own deposit page; never use a “dedicated address” from a DM, a group chat or a stranger.

Bitcoin block times vary, so arrival cannot be guaranteed within a fixed number of minutes. A deposit below the minimum, or one that does not meet the asset requirements, is handled by the reason shown in its record; do not keep waiting for it as an ordinary confirmation.

### 3.2 How do I deposit AIBRC?

On your Assets page, choose a supported AIBRC asset, check the amount, address and fees in its deposit flow, then complete the wallet signature and the broadcast that follows.

Bitcoin transaction confirmation and AIBRC instruction effect are verified separately. A BTC transaction being in a block does not mean any token instruction in it automatically takes effect.

Do not send other protocols' assets the same way just because their names look similar; follow the asset the page identifies and its supported flow.

### 3.3 A block rollback, reorg or conflicting transaction happened

A reorg can lower the confirmation count or put the original transaction back into waiting. This does not necessarily mean the assets were stolen, and it does not by itself mean the transaction failed.

```text
The original transaction's confirmation status changes
    ↓
Re-verify against the current valid main chain
    ├─ Back in a block: keep confirming per the original record
    ├─ Not found yet: keep the pending status and the original txid
    └─ Conflict found: goes to exception review
```

Keep the original transaction hash and check the deposit record and announcements. Do not pay again to “top up” the deposit, and never pay a “recovery fee” or an “unfreeze fee” to resolve an exception.

Whether recovery has finished follows the original transaction and the page status; a growing block height alone does not mean an exception has cleared.

## 4. Withdrawals, Block Swap & transaction progress {#support-s7}

### 4.1 How do withdrawals work?

Normal withdrawals are processed automatically by the rules, without manual approval of each one. First check the asset, receiving address, amount and fees, complete any required authorization or signature on the page, then track it through the original withdrawal record.

How deposits and withdrawals fit together:

```text
Deposit
    ↓
Bitcoin L1 transfer and protocol verification
    ↓
AIBTC CORE ledger record
    ↓
On-chain withdrawal · L1 Settlement / Handshake Exit
    ├─ Authorization: verify and sign for the asset
    ├─ Verification: processed automatically by the rules
    ├─ Fees: check the service fee and network fee before submitting
    └─ Tracking: original record, transaction hash and confirmations
    ↓
Delivered on-chain to the receiving address · look up by txid
```

The BTC and AIBRC withdrawal steps are described separately below.

### 4.2 BTC withdrawal

```text
Choose BTC withdrawal
    ↓
Check the receiving address, amount and fees
    ↓
Complete the required authorization and submit
    ↓
The system processes the queue, signs and broadcasts
    ↓
Check the original record and the Bitcoin transaction hash
    ↓
Wait for the receiving wallet to show it and for on-chain confirmation
```

Queued is not failed. Inventory availability, earlier requests and network conditions can affect how fast it moves. If a request is already in progress, check that original request first; do not submit again.

### 4.3 AIBRC protocol withdrawal

```text
Start a protocol withdrawal · Handshake Exit
    ↓
Check the asset, amount, address and fees
    ↓
Your wallet signs the inputs you are responsible for
    ↓
The execution node verifies the rules and completes co-signing
    ├─ Method: both sides sign · Co-signing
    ├─ Processing: normally no manual approval of each one
    ├─ Verification: checked by the rules · Code-Enforced
    └─ Fees: as in the preview you confirmed
    ↓
The system broadcasts the fully signed transaction
    ↓
Bitcoin confirmation + AIBRC delivery verification
    ↓
The asset arrives at the receiving address · look up by txid
```

Co-signing means each side signs the inputs it is responsible for in the same transaction; it does not mean every input uses the same 2-of-2 multisig script. The wallet makes the user's signature; the broadcast is done by the wallet or system that the flow designates, so signing and broadcasting are not one step.

AIBRC that has not graduated cannot be withdrawn yet; after graduation, use the protocol withdrawal flow the page provides. If the page says the address is not linked, the wallet's signing ability is not compatible, or a request is already in progress, handle that prompt first.

### 4.4 I have a txid but can't find it on-chain

A transaction hash can be generated before broadcast, and network propagation and explorer syncing can lag. First check whether the original record is waiting for a signature, waiting for broadcast, broadcast and awaiting confirmation, or awaiting verification of its result.

A signature is not a broadcast, and a broadcast is not a confirmation. When the result is unknown, keep the original record; do not pay again or build another transaction. If the original page offers a recovery or resend entry, use that entry.

### 4.5 Why does Block Swap have two confirmation stages?

| Stage | Meaning |
| --- | --- |
| 1st confirmation | The transaction is in a block; once AIBRC verification passes, the asset delivery is recognized |
| 2nd confirmation | The matching pool reserves and fees are recorded |

The change in your wallet's assets and the pool accounting don't necessarily finish at the same time. A stage that is still waiting does not mean you need to pay again.

If you see “Too many pending block swaps. Try again shortly.” or “The pending total is over 20% of pool liquidity. Try again shortly.”, wait for conditions to change before checking again. For an expired quote, review a new quote; if an order already exists, recover the original order first.

### 4.6 A launch creation is stuck, or the page shows an unknown result

Go back to the original creation record and check the actual progress of each protocol branch. A page timeout does not mean no branch ran; do not pay the creation fee again to test. If you're paying from your wallet and haven't signed yet, go back to the create page and continue signing; nothing is broadcast until you sign.

For any action already submitted, check the original request, original order and original txid first; handle “not submitted” and “result unknown” separately.

## 5. Scammed or hacked? Security & reporting {#support-s8}

### 5.1 I found an unauthorized transaction, or my assets seem to be missing

If you see a transaction, withdrawal or unfamiliar authorization that you did not start, stop signing anything further, save the suspicious records, and check your wallet, email and sign-in sessions.

Signatures in an external wallet are controlled by that wallet; AiBTC never obtains your external wallet's private key. An incident may come from a leaked seed phrase or private key, or involve a malicious signature or a stolen account session or authorization; a single incident cannot pin down one cause.

If only the displayed balance looks different, first check the account, address, orders in progress, locked amounts and on-chain records; a display difference does not mean anything was transferred out. If you already see an unfamiliar transaction, do not wait to learn the cause before protecting your account.

### 5.2 Take these steps now

1. 1. Stop connecting and signing on the suspicious page, and do not install any “fix tool” someone recommends.
2. 2. Use a trusted device to check your account, and revoke the suspicious sessions and transaction authorizations you can identify.
3. 3. Protect the linked email and social accounts: change their passwords, check for unusual sign-ins, and turn on the multi-factor verification they support.
4. 4. If you confirm your seed phrase or private key has leaked, treat every wallet it controls as permanently unsafe and stop using it.
5. 5. Create a new, independent wallet backup with a trusted wallet and keep it safe, then handle the remaining external assets according to the control you actually have. Importing the same leaked seed phrase into another app does not make it a new wallet.
6. 6. Save the original addresses, orders, transaction hashes, times and suspicious links, and report through the support email.

A leaked seed phrase does not become safe again by changing the wallet's unlock password. Check the other accounts and apps controlled by the same seed phrase too.

Switching external wallets or addresses does not automatically move your AiBTC account, balance or linked address. For issues with access to the original account, signed requests or address linking, report with the original records for review; never hand wallet secrets to anyone to “prove your identity”.

If you suspect the device is infected, stop using it for sensitive actions and investigate with a trusted device and the software's official channels. Do not rush to reset the wallet or delete all records before you have preserved the records and confirmed your wallet backup.

If fraud or theft is involved, keep the relevant evidence and seek help from the law enforcement or reporting channels that apply where you live. Do not keep providing information or sending funds because someone promises a “100% recovery”.

### 5.3 Support services

Support is provided jointly by community volunteers and the platform Agent, who help investigate server faults, service anomalies and technical issues whose cause is not yet confirmed.

AiBTC: 1 Pool, 2 Swaps. Instant for speed, Block Swap for self-custody. Instant is driven by AIBRC programmable rules (R1) and executed at the application layer by AiBTC CORE (currently a single node). Block Swap settles atomically on Bitcoin L1 via PSBT, delivering assets directly to your wallet without custody. AiBTC never holds your private keys. Both swaps share one liquidity pool.

Community support does not manually reorder trades, rewrite execution results, or modify, cancel or restore orders. Server anomalies are handled through the system's established procedures, never by manually rewriting the transaction history.

If you run into a suspected server fault or an unknown technical anomaly, email support or ask in the community. Send account or order details privately by email. Never provide your private key, seed phrase, password or access token.

### 5.4 Protect your wallet and signatures

- Never enter your seed phrase, private key or wallet backup into a website, chat box, email or unknown app, and never send them to any “customer service”.
- Don't photograph your seed phrase into chats, email or ordinary cloud storage. Keep the backup offline as your wallet officially recommends.
- Before every signature, check the website, transaction type, amount, receiving address and fees; if the information is incomplete or you don't understand it, stop signing.
- Don't sign “security verification”, “asset recovery” or unclear messages from strangers; signing a message can also grant permissions.
- A hardware wallet reduces how often the private key is exposed to everyday browsing, but it does not replace reading what you sign, and it cannot stop you from giving away your seed phrase.
- You can look into hardware wallets such as Ledger, Trezor and Keystone. First confirm that the specific device and its wallet software support the Bitcoin address types, message signing and PSBT operations you need; listing a brand is not a certification of full compatibility with AiBTC.

### 5.5 Guard against fake sites, DMs and malicious files

- Bookmark the platform domains listed on this page and open them from your bookmarks; don't judge authenticity from search results or ads alone.
- Check the full URL and where it actually redirects; watch for look-alike spellings, extra characters and fake suffixes. A change in letter case alone is not how you spot a fake site.
- Check X and Telegram through the links on this page. Use third-party directories and market data sites as secondary references.
- Verify unsolicited DMs through the official channels on this page, even if the profile, voice or video looks familiar.
- Don't click links of unknown origin, and don't install apps, extensions, browser configurations or remote-control tools from unverified sources.
- Don't open PDFs, archives or executables sent by strangers, even if the name looks like a report, a verification result or a technical fix.
- Get updates for wallets, browsers and hardware devices only from their own official channels; keep them up to date and remove extensions that are no longer maintained or used.
- Never pay so-called unfreeze fees, deposits, wallet sync fees or security verification payments, and never move assets to a “safe address” someone gives you.

### 5.6 Third-party projects and external links

Asset names, descriptions, websites and community links are provided by the project creators. An asset appearing on the platform or in the public API does not mean AiBTC vouches for its team, its promises of returns or the safety of its external services.

Before entering an external website or using a third-party swap, wallet or Agent tool, re-check the provider and the scope of authorization. Do not skip signature checks or hand over wallet secrets just because a link comes from a token's profile page.

For account, delivery or service problems with a third-party product, also contact that product's official support; for the part that involves an original AiBTC order, report to this platform with the original record.

### 5.7 What should I include when I report an issue?

Include the following details in one support email so support staff can locate the issue.

| Information | Notes |
| --- | --- |
| Where it happened | Sign-in, deposit, withdrawal, Block Swap, creation, etc. |
| Original order ID or txid | Copied from the original record |
| When it happened | Date, time and time zone |
| Wallet and device | Wallet name and version, browser or app |
| Page message | The exact error text |
| What you have tried | Reconnecting, refreshing, checking the original record, etc. |

Use plain text in your first email, with no attachments. Do not provide complete signature files, raw cookies, session tokens, verification codes or logs that contain them.

Do not post your email or other personal information in public group chats. A public address or txid helps lookups, but it also reveals links between on-chain activity and your account; share them only as needed.

Keep replying in the same email thread for follow-ups. Treat unsolicited DMs that claim to be support replies as suspicious.

### 5.8 Terms & privacy

[Terms of Use](https://aibtc.bot/terms) · [Privacy Policy](https://aibtc.bot/privacy)

## White-hat program {#support-s9}

**Keeping AIBTC secure together**

We welcome security researchers who report potential vulnerabilities responsibly, helping protect users' assets, privacy and the platform's services.

### Scope

Account authentication, wallet connection, signing and permission control; deposits, withdrawals, trading and ledger consistency; the platform's website, APIs and user data protection; security issues in the protocol implementation, public verification materials and key dependencies.

### Research boundaries

This program accepts vulnerability reports; it does not grant permission to attack or test the production environment. Before any active testing, contact the team to agree on the scope and method.

Do not run stress tests, denial-of-service, phishing or social-engineering attacks; do not access, download or modify other people's data, and do not move or hold other people's funds. Third-party wallets' and service providers' systems are outside the scope this program authorizes.

If you come across sensitive data or an issue that could affect real funds by accident, stop further verification immediately, keep only the minimum necessary evidence and report it privately.

### Submitting a report

Send the report to the support email listed on this page. Where possible, include the affected page or feature, when you found it, a description, the possible impact and the steps to reproduce the issue. Include redacted text excerpts when relevant.

Never send private keys, seed phrases, passwords, access tokens or complete user data.

### Responsible disclosure

Report privately first, and agree with the team on the timing and content of any public disclosure, so exploitable details are not made public before a fix. Public acknowledgment by name requires the reporter's consent.

### Contributions & rewards

The Bitcoin ecosystem grows because every builder and security researcher looks after it together. We value every good-faith discovery and responsible disclosure, and thank you for the time and expertise you give to the safety of users' assets, the reliability of the protocol and the growth of the ecosystem.

For verified, valid vulnerabilities within the scope of this program, we will assess a reward and form of acknowledgment based on severity, real impact and report quality. Rewards are decided case by case; public acknowledgment respects the contributor's wishes about attribution.

Join us in making the Bitcoin ecosystem safer and more trustworthy.
