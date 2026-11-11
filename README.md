# Quick Guide to AiBTC & AIBRC

## AiBTC & AIBRC at a glance

**AiBTC**: a Bitcoin L1 launchpad DEX and agent terminal, bringing together asset issuance, trading, liquidity and agent apps.

**AIBRC protocol**: a unified asset and account standard for the Bitcoin ecosystem. Its account-balance model unifies the account layer and underpins assets that work across protocols, so users and Agents can understand, track and verify assets by the rules.

Just as ERC defines asset standards and EVM provides the execution environment, AIBRC Covenant Inscription sets the asset and account standard for Bitcoin, and connects rules and apps with AiBTC through Smart Covenant.

| Ethereum ecosystem | like | Bitcoin ecosystem (AIBRC × AiBTC) |
| --- | --- | --- |
| **ERC asset standard**<br>Asset issuance & interaction interfaces | ↔ | **AIBRC Protocol**<br>Covenant Inscription<br>Bitcoin L1 assets & address-level unified accounts |
| **EVM execution environment**<br>Smart-contract logic execution | ↔ | **Smart Covenant + AiBTC execution stack**<br>Immutable on-chain covenant rules<br>AIBTC CORE execution & verification |

## The AIBRC model at a glance

### Traditional UTXO-bound model

```text
Every transfer must split a UTXO
    ↓
spent whole
    ↓
Fragmented change · accidental burns · scattered UTXOs · reliance on protocol-aware exchanges & wallets · cross-protocol contamination
```

### AIBRC model · Asset–UTXO Decoupling

```text
Unified address state (scriptPubKey): 100,000 tokens
    ↑
Authorized transfer: 25,000 tokens
    │
Any valid BTC UTXO at the address
    └─ proves control → Transferred
                       Rest untouched
```

Assets live in the address balance; there is no single "carrier UTXO" to guard. An ordinary BTC spend does not move or burn the AIBRC balance just because it consumes that UTXO.

Even with zero BTC at the address, the AIBRC balance remains. To transfer, add BTC inputs that cover source-address authorization, the receive output and the network fee.

### Multi-recipient Transfer

One set of outputs moves assets to several addresses in a single transaction. Airdrops, community distributions and group payments need no separate broadcasts; fees still depend on transaction size.

### Balance-based Transfers

Hold 10,000, send 5,000, and the rest stays at the original address. There is no separate "leftover-asset UTXO" to manage for token change; BTC change still follows Bitcoin transaction rules.

### Agent-friendly Asset Operations

Say "send 2,000 to B and 3,000 to C", and tools build the transaction around addresses, amounts and allocation rules for your wallet to authorize. Token operations no longer ask you to know which asset a UTXO carries.

## Bitcoin's value, the Agent era & ecosystem connection

From digital money to smart contracts and DeFi, blockchains keep widening how value can be exchanged. With PoW hash power, a public ledger and its network consensus as "energy money", Bitcoin became the store-of-value base for finance and blockchains.

As AI moves from assistant tools to autonomous Agents, Bitcoin's meaning extends from "storing value" to "how machines exchange value". Agents understand intent and interact; Bitcoin gives value exchange a verifiable ledger.

The Bitcoin ecosystem has been exploring for 17 years. From Ordinals, BRC-20 and Runes to Atomicals, RGB++, Taproot Assets, the Lightning Network and L2s, every protocol and extension brought new apps, assets, communities and culture.

Some created works, some built protocols, some kept maintaining tools. Each wave left names behind, and many unfinished dreams; some moved to other chains, some lost faith and left blockchain.

One project spreading across protocols is like the "A-chain dog" and "B-chain dog" of other L1s, rebuilding assets and liquidity each time. Communities can share a culture while their apps can't work together; innovation keeps coming, but what has been built gets scattered.

## The Bitcoin ecosystem today

### EVM ecosystem

```text
Projects & assets on different chains
    ↓
EVM-compatible execution
Same ERC asset standards
    ↓
Reused code, tools & frameworks
```

### The Bitcoin ecosystem today

One project & community

```text
├─ Protocol A
   Own asset rules
   Separate wallet support
   Separate markets
   Separate liquidity
├─ Protocol B
   Own asset rules
   Separate wallet support
   Separate markets
   Separate liquidity
└─ Protocol C
   Own asset rules
   Separate wallet support
   Separate markets
   Separate liquidity
```

**We connect them through AIBRC & AiBTC**

Unified account · consistent interaction base · continuous trading & liquidity

## AIBRC × AiBTC: the big picture

```text
AIBRC root deployment
Single Parent Tx · Verifiable Ancestry
    ↓
One AiBTC launch · same-root derivation
Zero Platform Creation Fee · Network Fees Paid by Users
```

```text
├─ AIBRC root asset
   Core asset on the platform
   Unified accounting
├─ Same‑root BRC‑20
   Derived from the same parent tx
   Keeps an inscription-ecosystem start
├─ Same‑root Runes
   Etched from the same parent tx
   Keeps a runes-ecosystem start
├─ EVM rules & contract extensions
   R1 tax / buyback rule reference
   X1 external contract address reference
   Intents & future contract extensions
   BOT execution & verification
└─ More quality protocols & extensions ahead
   Plug-and-Play Integration
```

```text
Human intent
What you want
    ↓
BOT execution
Done by which rules
    ↓
Agent verification
Does the result follow the rules
```

Rule parameters & intent through AIBTC CORE · public records & BTC on-chain proofs · Sequential Event Hash

```text
AIBRC as the unified account
    ↓
into trading & liquidity
    ↓
Asset launch
    ↓
Bonding curve
1B / 800M
    ↓
Graduation
    ↓
V2 liquidity pool
Block-based locks curb sudden pool exits and keep depth predictable
Permanent pool locks · freeze protection at expiry
```

```text
├─ Instant
   Trading in seconds on AIBTC CORE
   Bound to the rule version
├─ Block Swap
   Co-signing handshake
   Atomic swap in one Bitcoin transaction
   Delivered at 1 conf, pooled at 2
└─ LP market-making & covenant execution
   Block-based locks share trading fees
   Block buybacks under R1 rules
   or creator shares and other rules
```

When L1 assets and protocols break through or innovate, creating new value and economies

**Community · Holders · Agents**

Explore uses for sub-assets

```text
├─ AiBTC rule layer
   Sets asset rules
   Organizes claims, mapping or redemption
├─ AIBRC protocol index layer
   Through versioned protocol rules
   Voucher redemption & on-chain burn
└─ Open proposals
```

## Don't trust, verify.

> “Don't trust, verify.”

Verification and execution are moving from third parties to users and their agents. In the Agent era, everyone holds a PC or phone with real computing power, and uses Claude, Codex or OpenClaw to execute and verify.

```text
Early peer-to-peer
Individuals ran nodes
    ↓
Node networks
Trust in a few validators & costly hardware
    ↓
People & Agents
Bitcoin ledger + personal device + your own AI
```

— From the first peer-to-peer, toward Agents and You

## About the builders

AiBTC and AIBRC are funded entirely by the AIBTC Labs team itself, with no outside venture capital (VC) or institutional money with strings attached.

We chose to build the underlying system and protocol standard from zero, free of outside capital's pressure for short-term returns, to keep the platform and protocol independent and neutral as long-term ecosystem infrastructure, with no privileges reserved for any single party. As infrastructure, we want the rules to stay pure and neutral, leaving real participation and long-term room to the community, builders and every holder.

We all love Bitcoin this much. This pure love — for decentralization, monetary freedom and technological ideals — is where AiBTC began and what brings its global community together.

## Verify it yourself / 自己验证

Use [AiBTC Verification Method v2](docs/verification/METHOD_v2.en.md) with the [website's public Explorer](https://aibtc.bot/explorer/events) to check a record and its recorded pool-reserve changes.

**One trade, with the pool's reserve change, leaves a verifiable proof. Hand it to your AI to recompute independently.**

The [English / 中文 entry](docs/verification/README.md) connects the [AI prompt](docs/verification/PROMPT.en.md), [public endpoints](docs/verification/PUBLIC_ENDPOINTS.md), [reference script](docs/reference-proof.md) and [evidence scope](docs/verification/WHAT_AN_AI_CAN_CHECK.md). Preserve original proof bytes and report the checks actually computed. Pool-reserve figures describe the market state recorded in the public log; compare snapshots at the same state and time.

从[方法 v2](docs/verification/METHOD_v2.en.md)和[网站存证页](https://aibtc.bot/explorer/events)开始。

**一笔交易，连同池子储备的变化，一起留下可验证的证明，交给你的 AI 独立复算。**

[中英入口](docs/verification/README.md)说明如何核指纹、Merkle 关系、Bitcoin 锚定，以及方法覆盖的成交与池子储备。正式实例将取自上线后的日志期次，不固定可能被换期重用的测试序号。

## Read the full documentation

| Read | What you will find |
| --- | --- |
| [01 Accounts, Wallets & Addresses](docs/guide/01-accounts-wallets-addresses.md) | Full platform guide |
| [02 Create & Launch · First Buy & Bonding Curve · Graduation](docs/guide/02-create-launch.md) | Full platform guide |
| [03 AIBTC Swap](docs/guide/03-swap.md) | Hybrid DEX Engine |
| [04 Smart Covenant & Liquidity](docs/guide/04-smart-covenant-liquidity.md) | Full platform guide |
| [05 AIBTC CORE](docs/guide/05-aibtc-core.md) | Full platform guide |
| [06 Explorer & Agents](docs/guide/06-explorer-agents.md) | Full platform guide |
| [Build tools](docs/build-tools.md) | Public API, MCP, npm and integration examples |
| [Product FAQ](FAQ.md) · [LLMs index](llms.txt) · [Full reference](llms-full.txt) | Product answers and reference text for people and Agents |
| [Support](docs/support.md) | Wallet troubleshooting, deposits, withdrawals and official contacts |
| [Wallet signatures](docs/wallet-signatures.md) | Signing messages, permission scopes and PSBT excerpts |
| [Code examples](docs/code-examples.md) | Selected public-facing integration examples |
| [Reference proof script](docs/reference-proof.md) | Existing Python reference and downloads |
