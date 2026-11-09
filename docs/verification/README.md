# Verify a trade and its pool reserves / 核对成交与池子储备

Start with [AiBTC Verification Method v2](METHOD_v2.en.md) and the [website's public Explorer](https://aibtc.bot/explorer/events). Give the method, [AI prompt](PROMPT.en.md), and the complete material copied from a record to your AI for independent computation.

**One trade, with the pool's reserve change, leaves a verifiable proof. Hand it to your AI to recompute independently.**

The proof connects a record's original bytes, its place in the public log, a batch manifest, and a Bitcoin anchor. For supported AMM records, the method also gives the integer calculations for output amounts, fees and reserve changes.

```text
Original record bytes
  → Event fingerprint
  → Merkle inclusion in a stated log head
  → Canonical batch manifest and digest
  → OTS operations and a Bitcoin block
  → Recompute the covered trade and reserve changes
```

Bitcoin authenticates the commitment reached by that chain. The full trade JSON is read from the public log; it is not inserted verbatim into a Bitcoin block by this verification method.

## Read in this order

| Read | What it provides |
| --- | --- |
| [Method v2](METHOD_v2.en.md) | Exact byte operations, Merkle checks, Bitcoin anchoring and covered trade formulas |
| [AI prompt](PROMPT.en.md) | The questions to ask alongside a complete copied proof |
| [Public endpoints](PUBLIC_ENDPOINTS.md) | Read-only paths, identifiers, market scope, time fields and reference downloads |
| [What an AI can check](WHAT_AN_AI_CAN_CHECK.md) | What each kind of evidence can establish, and which inputs are still needed |
| [Reference script](../reference-proof.md) | Existing Python verifier, its checksum and local usage |
| [Code examples](../code-examples.md) | Existing public API, MCP and wallet examples |

## Use a complete proof

1. Open a record in the Explorer and copy its complete verification material. Keep `canonical_payload` and `canonical_manifest` exactly as copied.
2. Supply the method and prompt together with that material. Ask for computed results, not an opinion based on the project's description.
3. Run the [existing reference script](../reference-proof.md). It checks fingerprints and Merkle relations; complete the method's OTS-to-Bitcoin check separately.
4. For the formula version covered by the method, recompute the amounts, rounding, fees and pool reserve changes using integer arithmetic.
5. Report each check as **matches**, **does not match**, **material missing**, or **not actually run**. A successful fingerprint check does not automatically complete the other checks.

## Pool reserves and comparable data

**Liquidity-pool reserves (from the proof log)** describe the BTC and tokens recorded in a market's pool. Virtual reserves are pricing parameters. The LP fee vault is a separate accounting field, not part of the market's trading reserve.

A record describes a particular execution state; the public market API returns a cached snapshot. Keep `as_of` and `stale`, the market identity, and the record's log context with the comparison. A later API snapshot need not equal an earlier trade's after-values. Compare the same state before concluding that values disagree.

The public market API and MCP cover the **top 250 markets by market cap**. That scope alone does not establish a complete all-market total. BTC reserves can be added when the dataset and observation context are complete; token reserves remain identified by asset and must not be combined as if different tokens were the same unit.

## Version and record identity

These documents use **AiBTC Verification Method v2**. The Merkle V3 manifest and the `aibrc-merkle-reference-v3.py` filename identify different components, not a conflicting method version.

The original method and prompt are copied without rewriting. The November 2026 documentation addition appends **step 7, Pool reserves**, and adds **question 5** to the prompt. Synchronizing those additions into the website's copied text is a separate web update. Preserve the method included in your copied material when comparing versions; do not silently replace its algorithms.

Identify a record by its **network, log epoch, sequence and event hash**. A sequence number alone can refer to a different record after an epoch change. This directory deliberately pins no pre-launch trade: a worked example will use the launch epoch so that its identifiers remain meaningful.

The website supplies the record's current copyable method; this repository preserves the corresponding documentation and explicitly identified additions. Changes to the website's method should be reflected here without rewriting existing proof bytes.

## 中文入口

从[验证方法 v2](METHOD_v2.en.md)和[网站存证页](https://aibtc.bot/explorer/events)开始，把[提示词](PROMPT.en.md)与某条记录复制出的完整材料一起交给 AI。

**一笔交易，连同池子储备的变化，一起留下可验证的证明，交给你的 AI 独立复算。**

先核原始字节和记录指纹，再核 Merkle 关系、批次清单及 Bitcoin 锚定；方法覆盖的成交，还可以用整数公式重算成交数量、手续费与储备变化。Bitcoin 锚定的是摘要承诺，完整成交 JSON 从公开日志取得。

- [方法原文](METHOD_v2.en.md)和[提示词原文](PROMPT.en.md)保持英文，避免翻译改变计算规则。
- [能核对什么](WHAT_AN_AI_CAN_CHECK.md)用中英说明证据范围；[公开接口](PUBLIC_ENDPOINTS.md)给出读取入口。
- [参考脚本说明](../reference-proof.md)提供已有下载与运行方法；它的成功结果仍须与 OTS、Bitcoin 和业务公式检查分开。
- 池子账面储备、虚拟定价参数、LP 费用和链上资金位置分别解释。不能把其中一种检查的通过当成全部检查通过。
- 比较当前 API 时保留时间、市场和日志身份。公开快照仅覆盖市值前 250 个市场，不能仅凭它宣称已汇总所有市场。
- 本目录不固定上线前的成交序号。正式实例将在新一期取材，避免清空换期后旧序号指向另一条记录。

本次只补公开说明，不改变交易规则、存证内容或网站功能。
