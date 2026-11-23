# Quick Guide to AiBTC & AIBRC

From @, AI understands BTC and executes Smart Covenants, while people + Agents verify independently.

AIBRC mainnet activation height: Bitcoin block 976720.

Protocol repo: [github.com/aibrc-code/aibrc](https://github.com/aibrc-code/aibrc)

## AiBTC & AIBRC

- **AiBTC**: a Hybrid DEX built on Bitcoin and the first application of Smart Covenant programmability. One launch connects assets across multiple protocols, and unified liquidity builds the ecosystem’s finance and application layer.
- **AIBRC protocol**: a unified asset and account standard for the Bitcoin ecosystem.
    - Assets live at Bitcoin addresses, and the address is a unified account.
    - Protocols keep their native rules, while wallets, apps and Agents share one interaction language.
    - AiBTC is one of the apps built on AIBRC.
- **Smart Covenant**: Bitcoin anchors assets and EVM defines rules. It is already a distributed Agent network: execution is handed to Smart Covenants and Agents, and the right to verify returns to every person and every Agent.

Just as ERC defines asset standards and EVM provides the execution environment, AIBRC Covenant Inscription sets the asset and account standard for Bitcoin, and Smart Covenant connects its rules to applications such as AiBTC.

| Ethereum | Bitcoin (AIBRC × AiBTC) |
| --- | --- |
| **ERC asset standard**<br>Asset issuance & interaction interfaces | **AIBRC Protocol · Covenant Inscription**<br>Bitcoin L1 assets & address-level unified accounts |
| **EVM execution environment**<br>Smart-contract logic execution | **Smart Covenant + deterministic state machine (FSM)**<br>R1 parameters are fixed per asset and anchored on Bitcoin; AIBTC CORE and Agents execute on the same state machine; anyone can recompute with the R1 reference code (reference/r1). |

## Three steps: read, execute, verify

### Read

- Assets live in the address balance, and any valid BTC UTXO at the address proves control.
- One transaction can pay several addresses; send part of a balance and the rest stays where it was.
- Say “send 2,000 to B and 3,000 to C”, and tools build the transaction for your wallet to authorize.

#### Traditional UTXO-bound model

```text
Every transfer splits a carrier UTXO
    ↓
The carrier UTXO is spent whole
    ↓
Fragmented change · accidental burns · scattered UTXOs · reliance on protocol-aware exchanges & wallets · cross-protocol contamination
```

#### AIBRC model · Asset–UTXO Decoupling

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

### Execute

- One launch derives same-root AIBRC, BRC-20 and Runes.
- Instant Swap trades in seconds from your AiBTC account.
- Block Swap is signed by your own wallet and settles the BTC payment and the AIBRC delivery in one Bitcoin transaction.
- After graduation, Smart Covenants run block buybacks or creator shares under R1 rules.

### Verify

- Every step is written into a public event hash chain, and records are anchored to Bitcoin in batches with OTS.
- Copy the proof of a trade and hand it to your own AI to recompute; different AI models can replay the same deterministic state machine independently and check one another's results. **Don’t Trust. Verify. With Your Own Agent.** [Verification guide](docs/verification/README.md)

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

## In the future

- Agent Key (proposed): controlled authorization, limited by asset, amount and block, would let Agents act on their own within the rules while the master private key stays with the user.
- A multi-node Agent execution network.
- More protocols and extensions, plug-and-play.

## Start here

| Chapter | What you’ll find |
| --- | --- |
| [01 Accounts, Wallets & Addresses](docs/guide/01-accounts-wallets-addresses.md) | Sign in with a Bitcoin wallet, email or social account; wallet keys stay with you |
| [02 Create & Launch · First Buy & Bonding Curve · Graduation](docs/guide/02-create-launch.md) | One launch, many protocols growing together |
| [03 AIBTC Swap](docs/guide/03-swap.md) | 1 Pool, 2 Swaps: Instant Swap and Block Swap |
| [04 Smart Covenant & Liquidity](docs/guide/04-smart-covenant-liquidity.md) | EVM as Bitcoin’s extension layer |
| [05 AIBTC CORE](docs/guide/05-aibtc-core.md) | Bitcoin’s deterministic execution engine, every step replayable |
| [06 Explorer & Agents](docs/guide/06-explorer-agents.md) | Make everyone’s Agent an independent verifier of the Bitcoin ecosystem |
| [07 Atom Unit Protocol](docs/atom-unit.md) | Where reserves are deposited and withdrawn; users and their Agents can verify their own on-chain reserves |
| [Build tools](docs/build-tools.md) · [Support](docs/support.md) | Public API, MCP, npm and integration examples; wallet troubleshooting, deposits, withdrawals and official contacts |
| [Product FAQ](FAQ.md) · [Wallet signatures](docs/wallet-signatures.md) · [Code examples](docs/code-examples.md) · [Reference proof script](docs/reference-proof.md) | Product answers for people and Agents; signing messages, permission scopes and PSBT excerpts; selected integration examples; Python reference and downloads |
| [Audit & Open Source](docs/audit-and-open-source.md) | R1 audit report, verification method and public endpoints |

## Why we build

From digital money to smart contracts and DeFi, blockchains keep widening how value can be exchanged. With PoW hash power, a public ledger and its network consensus as “energy money”, Bitcoin became the store-of-value base for finance and blockchains.

As AI moves from assistant tools to autonomous Agents, Bitcoin’s meaning extends from “storing value” to “how machines exchange value”. Agents understand intent and interact; Bitcoin gives value exchange a verifiable ledger.

The Bitcoin ecosystem has spent 17 years exploring. From Ordinals, BRC-20 and Runes to Atomicals, RGB++, Taproot Assets, the Lightning Network and L2s, every protocol and extension brought new apps, assets, communities and culture. Some created works, some built protocols, some kept maintaining tools. Each wave left names behind, and many unfinished dreams.

### Bitcoin ecosystem in figures

| Metric | Figure |
| --- | ---: |
| Bitcoin price | $23K → $121K |
| Bitcoin address growth in the inscription year, year over year | 9.9M addresses |
| Bitcoin address growth over the next 14 months | +3.75M addresses |
| Miner earnings from inscription and Rune mints | >9,600 BTC |
| BRC-20 cumulative on-chain transactions | 103M |
| Total secondary trading volume | >$70B |

Figures from the November 13, 2026 overview, drawing on Dune and Total Secondary Trading Volume.

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

We want to bring this consensus and these unfinished dreams back to Bitcoin. We connect them through AIBRC & AiBTC: a unified account, a consistent interaction base, continuous trading and liquidity.

## About the builders

AiBTC and AIBRC are funded entirely by the AIBTC Labs team itself, with no outside venture capital (VC) or institutional money with strings attached.

We chose to build the underlying system and protocol standard from zero, free of outside capital's pressure for short-term returns, to keep the platform and protocol independent and neutral as long-term ecosystem infrastructure, with no privileges reserved for any single party. As infrastructure, we want the rules to stay pure and neutral, leaving real participation and long-term room to the community, builders and every holder.

The AIBRC protocol has no founder and no team. Docs are CC0 and code is MIT, fully open source.

We love Bitcoin. That pure love — for decentralization, monetary freedom and technological ideals — is where AiBTC began and what brings its global community together.

Math over promises, rules over individuals. This is an ecosystem experiment between BTC and AI.
