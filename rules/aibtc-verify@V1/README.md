# aibtc-verify@V1

The rule core of AiBTC AI Verification. AIBTC CORE opens, closes, releases, splits and credits verification rewards only as this file says.

AI 验证的规则核心。验证奖励的开放、关闭、放出、分配和到账，AIBTC CORE 只照这份文件执行。

## Why · 为什么这么做

**Open programming and covenants.** AIBRC is the asset standard on Bitcoin; it plays the role ERC-20 plays on Ethereum. AiBTC is an application built with Smart Covenants. A smart contract is everyone on one chain running the same code together. A Smart Covenant is like a delivery order: it states what is delivered and what counts as delivered, its rules are fixed and published at creation, and who executes is open. Other applications, users, and a user's own AI can execute and check against the same covenant.

**Why verify.** Trust should not rest on anyone saying "it is correct". Bitcoin provides time and finality, a Smart Covenant fixes the rules, and a deterministic state machine gives one result for the same inputs. So any person and any AI can recompute the AiBTC Smart Covenant ledger. The more open execution becomes, the more verification matters.

**Why reward it.** "Anyone can verify" is only a possibility until someone does it. The reward goes to those who actually verify each pack and leave a public record. A distributed AI network starts with verification.

**Why the rule is written this way.** It was finalized and Bitcoin-timestamped before the pool is funded, so the basis for paying exists before the money does. It holds only parameters and formulas, so every step has one correct result that any AI can recompute. The verification hash includes the login address and the anchoring Bitcoin block hash, so it differs per address and cannot be computed before the pack is on chain. Rewards are split by shares held, with no first place.

**Where it leads.** Now: a distributed verification network for Smart Covenants. Next, exploring distributed indexing at the AIBRC protocol layer, which is the foundation for Bitcoin privacy for L1 assets. After that: a user with their own AI acting peer to peer, and on-chain agents.

**开放式编程和契约。** AIBRC 是比特币上的资产标准，作用相当于以太坊上的 ERC-20。AiBTC 是用智能契约做出来的一个应用。智能合约是一条链上大家一起跑同一段代码。智能契约像一张订单：写明送什么、怎样才算送达，规则在创建时固定并公开，谁来执行是开放的。别的应用、用户、用户自己的 AI，都可以照同一份契约去执行、去核对。

**为什么要验证。** 可信不应该来自任何一方的一句「它是对的」。比特币提供时间和终局，智能契约把规则固定，确定性状态机对同样的输入只给出一个结果。所以 AiBTC 的智能契约账本，任何人、任何 AI 都可以自己重算。执行越开放，验证就越重要。

**为什么给验证奖励。** 「任何人都可以验证」只是一种可能，要有人真的去做。验证奖励给的是每一次打包都实际去验、并留下公开记录的人。分布式 AI 网络从验证开始。

**为什么规则写成这样。** 规则先定稿、先盖比特币时间戳，奖励池之后才转入，发放的依据早于资金。规则核心只有参数和公式，每一步只有一个正确结果，任何 AI 都能重算。验证哈希里有登录地址和锚定区块的哈希，所以每个地址的结果不同，打包上链之前谁也算不出。按持有的份数平分，不设第一名。

**往哪里走。** 现在是智能契约的分布式验证网络。接下来探索 AIBRC 协议层的分布式索引，它是 L1 资产比特币隐私的地基。再往后，是用户带着自己的 AI 点对点，和链上智能体。

## Files · 文件

| File | What it is |
|---|---|
| `aibtc-verify@V1.txt` | The rule core. Frozen. 3,756 bytes, 34 lines; UTF-8, LF line endings, no BOM, one trailing newline. 规则核心，已冻结。 |
| `aibtc-verify@V1.txt.ots` | OpenTimestamps proof that this exact file existed before the Bitcoin blocks listed below. 3,972 bytes. 这份文件的比特币时间证明。 |
| `aibtc-verify@V1.notes.zh.md` | Notes in Chinese: why the rule exists, then how each clause executes. The notes can be adjusted; where they differ from the rule core, the rule core prevails. 规则说明：先讲为什么这么做，再逐条讲怎么执行；可以调整，和规则核心不一致时以规则核心为准。 |

## Rule fingerprint · 规则指纹

SHA-256 over all bytes of `aibtc-verify@V1.txt`:

```text
8e5eccc1f19de8068e75e1335fa98cb41a1b3efb726387ad2a9a94d05bdf5a56
```

Frozen at 2026-11-27T17:39:47Z. Every settlement record cites this fingerprint.

冻结时间 2026-11-27T17:39:47Z。每一次结算的公开记录都写明这枚指纹。

## Check it yourself · 自己核对

**1. The fingerprint · 指纹**

```bash
sha256sum 'aibtc-verify@V1.txt'
```

The result must equal the fingerprint above. Use the file itself; text copied from a web page does not count.

结果应当和上面的指纹一致。必须用文件本身，从网页上复制出来的文字不算。

**2. The Bitcoin timestamp · 比特币时间证明**

With the two files in the same folder:

```bash
ots verify 'aibtc-verify@V1.txt.ots'
```

Or drop both files onto opentimestamps.org. The proof commits the fingerprint into three Bitcoin blocks, one per public calendar:

把两个文件放在同一个文件夹里运行上面的命令，或者把两个文件拖进 opentimestamps.org。证明把这枚指纹写进了三个比特币区块：

| Bitcoin block height · 区块高度 | Block time (UTC) · 区块时间 | Merkle root the proof arrives at · 证明算出的默克尔根 |
|---|---|---|
| 977,832 | 2026-11-27 18:32:07 | `f72cac080320426ecce3287ac4efeb65af5953225297287b06cc50b2a911df02` |
| 977,836 | 2026-11-27 18:59:49 | `a8e34accc83786509f88448b4249732b88e9668f314a30e8ee36f44c86a5c7c2` |
| 977,841 | 2026-11-27 19:48:51 | `9ebce2e9cbdb180ed1c92dbfdf88993eb5ed5204e97b40409b318f4e5c933b50` |

To check without the OpenTimestamps client: start from the fingerprint, apply each operation in the proof in order, and compare the result with the Merkle root in that block's header, taken from your own Bitcoin node or any block explorer.

不用客户端也能核对：从指纹出发，照证明里的每一步运算依次算到底，把结果和该高度区块头里的默克尔根比较。区块头可以从自己的比特币节点或任何区块浏览器取。

**3. Each settlement · 每一次结算**

Every settlement with at least one share is a public record. It carries this fingerprint, the sequences of the head and tail records, and the SHA-256 of the settlement list. Anyone can recompute the release and the split from the rule core and the public list.

有份数的每一次结算都是一条公开记录，写明这枚指纹、头尾两条记录的编号和结算名单的 SHA-256。任何人可以用规则核心和公开名单重算放出量和分配。

## Frozen · 冻结

Not one byte of `aibtc-verify@V1.txt` changes after freezing. A rule change is a new version, `aibtc-verify@V2`: a new file, a new fingerprint and a new Bitcoin timestamp, announced in advance and applied only to packs that open after the announcement.

冻结之后，`aibtc-verify@V1.txt` 一个字节都不再改。要改规则，就发布新版本 `aibtc-verify@V2`：新的文件、新的指纹、新的比特币时间证明，事先公布，只对公布之后开放的打包生效。
