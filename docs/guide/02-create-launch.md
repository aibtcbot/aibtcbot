# 02 Create & Launch · First Buy & Bonding Curve · Graduation

### No need to bet on one protocol: bring every innovation into one account and one community

### One launch, many protocols growing together

### Start from same-root assets and let the ecosystem accrue to AIBRC

The Bitcoin ecosystem keeps producing new protocols, assets and apps. BRC-20, Runes and the protocols and extensions still to come may each find their own path. Creators and holders shouldn't have to pick a new asset, build a new market and regather their community every time a new direction appears.

AiBTC uses AIBRC as the shared asset and account layer. One same-root launch connects the starting points of different protocol ecosystems and turns creation, first buy, bonding curve and graduation liquidity into one continuous market process.

You don't have to bet on which protocol wins, or fix every future use on launch day — the Agent era brings fast iteration and many possibilities. Each protocol and AI-native app can grow its own tech, tools and culture, while projects and communities stay anchored to the AIBRC root asset and one unified account, connecting to new apps and opportunities over time.

```text
One project · One community
    │
    ▼
One launch · AIBRC root deployment
    ├─ AIBRC → root asset & unified account layer
    ├─ BRC-20 → same-root inscription ecosystem
    ├─ Runes → same-root runes ecosystem
    └─ EVM → covenant rules & external app links
    │
    ▼
Creator first buy · optional, manual
    │
    ▼
Public bonding-curve trading
    │ Before graduation: trade by the rules, no AIBRC withdrawal
    │ Real BTC reserve reaches 0.1 BTC
    ▼
Graduation · V2 liquidity pool
    ├─ Instant · buy & sell instantly
    ├─ Block Swap
    ├─ Liquidity · provide liquidity
    └─ Protocol Withdrawal
```

AIBRC provides a shared asset language and account layer; AiBTC connects issuance, trading, liquidity and apps, so one launch becomes the start of long-term building.

## 2.1 Create & Launch {#c2-s1}

Open Launchpad, fill in the asset details, choose an issuance mode and decide whether to make a creator first buy. Check the fees and creation summary before you submit; after confirming, follow progress under Created assets on the Assets page.

### Asset Details

- Asset name and ticker
- Project logo
- Project description, up to 150 characters
- Project links such as website, X and Telegram

### Issuance Settings

- Standard mode, R1 Tax Covenant or X1 External Contract Reference
- Rule parameters for the chosen mode
- Creator first buy amount; enter 0 to skip
- Bitcoin network fee and creation summary

Fill in details → Set issuance mode → Set optional first buy → Check fees → Confirm

Project details help users understand the asset; protocol deployment and link records identify it. The same name and image do not mean the same asset.

## 2.2 Pinning Images & Metadata · IPFS {#c2-s2}

The project logo and asset metadata are stored on IPFS and referenced by content ID (CID). The image and the JSON metadata are pinned separately; the metadata holds the project details and references the image, so wallets, explorers and apps read the same content.

- Image formats: PNG, JPEG, WebP
- Upload size: up to 2 MB
- Processing: normalized to a square WebP, at most 1024 px per side
- Metadata: asset name, ticker, description, image reference and any project links you entered
- Reference: ipfs://CID

```text
Upload project logo
    │ Image checks & normalization
    ▼
Image CID
    │
    ▼
Project metadata JSON
Name · Ticker · Description · Image ref · Links
    │
    ▼
Metadata CID → linked to the asset creation record
```

A CID is derived from the content; changed content gets a new CID. IPFS pinning keeps the image and metadata, and the Bitcoin transaction records the protocol deployment. Together they make up the asset's display and provenance.

An upload preview is not a completed pin. After you confirm creation and the fees are charged, the system keeps pinning, and the result shows on the original creation record. IPFS does not write the image into a Bitcoin block, and content is not reachable forever without ongoing pinning.

## 2.3 Root Deployment & Same-root Issuance {#c2-s3}

One launch connects different protocols through one shared Bitcoin root transaction.

The AIBRC deploy instruction is written into the root transaction; BRC-20 and Runes proceed through their own commitment outputs and later reveal transactions. Outputs across protocols thus share a traceable provenance, not just the same name and logo.

```text
Bitcoin Genesis Commit
    │
    ├─ AIBRC Deploy
    │    └─ L1 asset deploy · address-level balances
    │
    ├─ BRC-20 Commitment
    │    └─ Inscription Reveal · inscription deploy
    │
    ├─ Runes Commitment
    │    └─ Reveal + Runestone · rune etching
    │
    └─ EVM Association
         ├─ R1 · covenant rules
         └─ X1 · chainId + Contract Address
```

The AIBRC root asset carries core trading and liquidity; same-root branches keep a starting point in other ecosystems. When a protocol later gains new apps or tools, the project can explore integrating on top of its existing provenance, instead of cutting each innovation off from its community.

Each protocol step confirms and shows its status separately; the branches don't all complete at once. The BRC-20 and Runes branches proceed on their own and may be missing (for example, due to name competition). Neither is required for the AIBRC market to open.

Same-root issuance establishes provenance. It does not merge balances across protocols, and does not open swaps or redemption automatically. Such uses must be connected later through explicit rules and implementation.

## 2.4 Creator First Buy {#c2-s4}

Before the public market opens, the creator can manually make one first buy at the bonding-curve price. It is a real purchase, not a free allocation, and entering an amount does not execute it.

### First Buy Settings

- Required: no — enter 0 to skip
- Minimum: 2,000 sats (0.00002 BTC)
- Maximum: 10,000,000 sats (0.1 BTC)
- Funded from: the creator account's available BTC
- Amount executed: the amount set at creation
- Tokens received: from the bonding-curve quote and fees, shown before you confirm

### Setting, Execution & Charging

At creation, the system checks that available BTC covers the creation fee and the first-buy amount. First-buy funds are not deducted when you enter the amount, and are not locked in advance at creation.

Once the launch reaches the stage that allows the first buy, the creator confirms the buy. At execution the system re-checks balance, trading authorization and market state; on success it deducts BTC and credits the bought AIBRC to the creator account.

```text
Set amount at creation
    │ No auto-buy, no funds locked in advance
    ▼
First-buy stage opens
    │ View quote · confirm manually
    ▼
Charged & filled
    ├─ AIBRC → creator holdings
    └─ BTC after trading fee → bonding-curve real reserve
```

### First Buy Fees

The first buy follows pre-graduation bonding-curve rules: the base trading fee is 0.5%, and the R1 extra rule fee is not active yet. The first-buy amount includes that buy's trading fee; the creation network fee is separate.

For example, a first buy of 100,000 sats:

```text
100,000 sats
    ├─ 500 sats → trading fee
    └─ 99,500 sats → curve buy principal
                              │
                              ▼
                AIBRC received per the curve
```

So setting the maximum 0.1 BTC first buy does not by itself fill the 0.1 BTC graduation reserve. Trading fees don't count toward graduation principal.

### Before the Public Market Opens

- Only the creator can use the first-buy entry.
- It can succeed only once — no split buys or top-ups.
- It is not a fixed-price allocation; the amount received follows the curve.
- To exit, sell the entire first-buy holding in one go; partial sells are not supported.
- After a full exit, the first-buy chance cannot be used again.
- Sells settle under curve and fee rules; they are not refunds.
- First-buy holdings are also bound by graduation: before the asset graduates, they can't be withdrawn to an external wallet.

```text
First buy succeeds
    │
    ├─ Keep holdings → wait for the public market
    │
    └─ Exit before the market opens
         └─ Sell entire holding at once → first-buy chance ends
```

### First Buy & Public Market

Whether the first buy is made does not affect the market opening once deployment and opening conditions are met. No first buy set, or one set but not executed, does not block the public market on its own.

When the public market opens, any unused first-buy chance closes. From then on the creator and everyone else trade under public-market rules; the pre-opening "one buy, full exit" limits no longer apply, but un-graduated assets still can't be withdrawn.

If the launch is paused or enters a name-conflict or similar handling state, an unexecuted first buy stops; existing first-buy holdings follow the allowed full-exit path.

## 2.5 Bonding Curve {#c2-s5}

After the market opens, users buy and sell AIBRC on the bonding curve. Price is computed from reserves: buys add to the real BTC reserve, sells reduce it, and graduation progress moves with it.

### Issuance Parameters

- AIBRC total supply: 1 billion
- Display precision: 8 decimals
- Bonding-curve allocation: 800 million
- Graduation liquidity reserve: 200 million
- Graduation threshold: real BTC reserve reaches 0.1 BTC
- Base trading fee: 0.5%

```text
Fixed supply · 1B
    │
    ├─ 800M → bonding curve
    │               │
    │           Buy / Sell
    │               │
    │               ▼
    │        Real BTC reserve
    │               │
    └─ 200M → graduation reserve
                    │
                    ▼
            V2 liquidity pool
```

### Virtual & Real Reserves

The bonding curve uses virtual reserves to set the initial quote, so the early market can price buys and sells. Virtual reserves are a pricing parameter — not withdrawable BTC, and not funds actually deposited.

Real reserves come from actual trades. The creator first buy's principal counts toward them, and sells settle from them.

Graduation progress tracks the current real BTC reserve — not cumulative volume, cumulative buys or market cap. Trading fees don't accrue as graduation principal.

### What Un-graduated Assets Can Do

During the bonding-curve stage, AIBRC holdings are recorded in your account and can be bought or sold under that stage's rules, but can't be withdrawn to an external wallet via Protocol Withdrawal. Protocol withdrawal opens only after graduation.

```text
Un-graduated AIBRC holdings
    ├─ View balance & holdings
    ├─ Buy / sell on the bonding curve
    └─ No withdrawal to external wallets
```

This limit applies to the AIBRC asset itself; it does not freeze BTC in your account. BTC from sells follows the BTC withdrawal rules.

### Quotes & Fills

Before you submit, the page shows estimated tokens received, trading fees and minimum received. At execution the system checks against the latest reserves; if the minimum can't be met, the trade won't fill at that quote.

When the last buy hits the graduation threshold, the system takes only the amount needed to reach it plus its fee; any excess is not charged as curve principal.

## 2.6 Graduation & Liquidity {#c2-s6}

When the bonding curve's real BTC reserve reaches 0.1 BTC, the market graduates into the V2 liquidity stage and AIBRC protocol withdrawal opens.

At graduation, virtual reserves leave pricing; actual BTC and the remaining tokens form the pool reserves and initialize LP shares. Graduation continues the same asset and market, so existing holdings need no swap.

```text
Real BTC reserve reaches 0.1 BTC
    │
    ▼
Graduation
    ├─ Virtual reserves removed
    ├─ Actual BTC + remaining AIBRC form the pool
    └─ LP shares initialized
    │
    ▼
V2 liquidity pool · BTC / AIBRC
    │
    ├─ Instant
    │    └─ Buy & sell with account balance
    │
    ├─ Block Swap
    │    └─ Wallet handshake & co-signing
    │       Delivered at 1 confirmation · pooled at 2
    │
    ├─ Liquidity
    │    └─ Add liquidity · share fees by the rules
    │
    └─ Protocol Withdrawal
         └─ Withdraw AIBRC to your linked wallet
```

### Before & After Graduation

- Before: trade on the bonding curve; AIBRC can't be withdrawn.
- After: trade on the V2 pool; Block Swap, liquidity and AIBRC protocol withdrawal open.
- Protocol withdrawal still requires available balance, a linked wallet, fees and other conditions; nothing is withdrawn automatically at graduation.

After graduation, price is set by actual pool reserves and trading. Graduation marks a change of market stage — not a price guarantee or a promise of returns.

## 2.7 Covenant Rules & EVM Association · Smart Covenant {#c2-s7}

Creators choose Standard mode, R1 Tax Covenant or X1 External Contract Reference. The parameters are linked to the asset creation record, so users can see the rules and their source.

### Standard Mode

Runs on the base trading rules, with no R1 rule fee.

### R1 · Tax Covenant

R1 binds a rule fee rate and fee destination to the asset. Parameters are fixed at creation and enforced by AiBTC under deterministic rules; the public contract serves as the calculation reference.

- Active from: after graduation
- Extra rule fee: 0–5%
- Step: 0.1%
- Fee goes to: system block buyback or the creator (pick one)
- Base trading fee: 0.5%, shown separately from the extra rule fee

```text
Rules fixed at creation
    │
    ▼
Bonding-curve stage
    └─ Base pre-graduation trading fee
    │
    ▼
Post-graduation trading
    ├─ Base trading fee
    └─ R1 extra rule fee
         ├─ System block buyback → task created → buy executed
         └─ Creator earnings → accrued by the rules
```

R1 doesn't make users pay extra EVM gas on each AiBTC trade. Buybacks run by the rules and task state — not an immediate fill after every fee — and are not a price floor.

### X1 · External Contract Reference

X1 links an EVM network ID and contract address to the asset creation record, giving external apps and contracts a queryable entry point.

```text
AIBRC root deployment
    ├─ chainId → the EVM network
    └─ Contract Address → the contract on that network
```

The target contract still runs on its EVM network. A link is not a contract audit and does not open cross-chain swaps.

## 2.8 Fees, Progress & Recovery {#c2-s8}

### Fees

- Platform creation fee: none for new launches at present
- Bitcoin network fee: paid at the quote shown on the create page
- Creator first buy: optional, separate from creation fees, charged when you execute it
- Later trading fees: per the bonding-curve or post-graduation trading rules
- Protocol withdrawal fees: after graduation, confirmed from the breakdown on the withdrawal page

```text
Creation progress
Confirm creation & fee charge
    │
    ▼
IPFS image & metadata pinning
    │
    ▼
Root deployment build & broadcast
    ├─ AIBRC deploy & confirm
    ├─ BRC-20 reveal & confirm
    └─ Runes branch proceeds on its own
    │
    ▼
Opening conditions met → Public trading → Threshold reached → Graduation
```

The creator first buy is a separate action in the allowed pre-opening stage, not a prerequisite for the public market. Each branch follows its actual progress; "submitted" is not "completed".

### Waiting & Exceptions

- Image or metadata processing: return to the original launch to check pinning progress.
- Transaction broadcast: check confirmations by the original transaction hash.
- First buy with insufficient balance, or explicitly rejected: that buy won't complete; follow the on-page prompt.
- Page timeout or unknown result: check the original request and transaction records first, then decide the next step.
- Name competition or deployment error: handled by each protocol branch's actual result; unfinished issuance is never treated as success.

Network waits are not creation failures. Don't create again, pay again or resubmit under a new request ID just because the page timed out.

## 2.9 Same-root Assets & Ecosystem Growth {#c2-s9}

### No restart for every new protocol

Taking a project to another protocol often means reissuing the asset, building a new market and gathering liquidity again. The community shares a culture, but holders, tools and apps easily scatter.

AIBRC and AiBTC aim to give exploration across protocols a shared starting point: the AIBRC root asset carries core trading, one unified account connects users and apps, and same-root branches keep the door open to other ecosystems.

Protocols can differ; projects and communities needn't lose their connection.

```text
One project
    │
    ▼
AIBRC root asset · unified account layer
    ├─ Core trading & liquidity
    ├─ Ecosystem exploration on same-root protocols
    └─ Apps & rules connected over time
    │
    ▼
Many directions grow together; what's built stays connected
```

### You don't need every use figured out at launch

A protocol may bring a better wallet experience, an app may create a new use for the asset, and a set of covenant rules may spark new economic activity. These chances may not exist yet when the project is created.

A same-root launch first establishes provenance and leaves entry points for the future, rather than fixing every branch's use on day one. As the ecosystem grows, the community, holders and Agents can discuss which apps to integrate, how to use same-root assets, and how to design open, verifiable rights.

```text
Same-root protocols keep evolving
    │ New tools · new apps · new uses
    ▼
Community · Holders · Agents
discuss uses & rules together
    │
    ├─ App integration
    ├─ Rights mapping
    ├─ Distribution plans
    └─ Redemption mechanisms
    │
    ▼
Rules defined · Implemented · Publicly verified
    │
    ▼
Connected to the AIBRC root asset & unified account
```

These are future directions; each needs its own rules and implementation. Same-root provenance does not by itself create swap or redemption rights.

### One account, so you focus on what to do

AIBRC's address-level balance model provides a shared account layer, so interactions center on accounts, assets, amounts and explicit rules. AiBTC connects trading, liquidity and apps on top of it.

In the future, users and Agents won't have to learn new tools and flows for every protocol; they express intent from one account and use the apps and asset capabilities already connected.

```text
Intent of users & Agents
    │
    ▼
AIBRC unified account layer
    ├─ Assets & holdings
    ├─ Trading & liquidity
    ├─ Covenant rules & apps
    └─ Mapping & use of future same-root assets
    │
    ▼
AiBTC connects execution & interaction
Public records let anyone verify results
```

What's unified is not every protocol's implementation but the common base for taking part. Each protocol keeps its own rules; new capabilities connect through explicit adaptation and verification.

We don't want users to have to guess which protocol leads the next cycle, or projects to lose their holders each time they explore a new direction. Our vision: let each protocol innovate, let new apps and uses connect back to AIBRC, and let assets, accounts, liquidity and community keep compounding.

We don't pick one protocol for the Bitcoin ecosystem; we let every protocol's growth serve the same project, the same community and a shared account layer.

Bring trading back to Bitcoin · Unify protocol assets, and make EVM an extension layer for Bitcoin.
