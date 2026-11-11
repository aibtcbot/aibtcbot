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

## Read in this order

| Read | What it provides |
| --- | --- |
| [Method v2](METHOD_v2.en.md) | Exact byte operations, Merkle checks, Bitcoin anchoring and covered trade formulas |
| [AI prompt](PROMPT.en.md) | The questions to ask alongside a complete copied proof |
| [Public endpoints](PUBLIC_ENDPOINTS.md) | Read-only paths, identifiers, market scope, time fields and reference downloads |
| [What an AI can check](WHAT_AN_AI_CAN_CHECK.md) | What to calculate from a copied trade proof |
| [Reference script](../reference-proof.md) | Existing Python verifier, its checksum and local usage |
| [Code examples](../code-examples.md) | Existing public API, MCP and wallet examples |

## Use a complete proof

1. Open a record in the Explorer and copy its complete verification material. Keep `canonical_payload` and `canonical_manifest` exactly as copied.
2. Supply the method and prompt together with that material. Ask for the computed value of each check.
3. Use the [reference script](../reference-proof.md) for fingerprints and Merkle relations, then follow Method v2 to verify the Bitcoin anchor.
4. For the formula version covered by the method, recompute the amounts, rounding, fees and pool reserve changes using integer arithmetic.
5. Report each check as **matches**, **does not match**, **material missing**, or **not actually run**.

## Pool reserves and comparable data

**Liquidity-pool reserves (from the proof log)** describe the BTC and tokens recorded in a market's pool. Virtual reserves are pricing parameters. The LP fee vault records liquidity providers' fees separately.

Compare the market's latest recorded reserves with its public API snapshot. Keep the market identity, log context, `as_of` and `stale` together to align the observation times. For an earlier record, report the reserve change across that trade.

The public market API and MCP provide the market-reserve fields used in this comparison. For a complete dataset at the same observation time, sum BTC reserves across markets and report token reserves by asset.

## Version and record identity

These examples use **AiBTC Verification Method v2**. Identify a record by its **network, log epoch, sequence and event hash**, and keep the original proof and rule version together.

## 中文入口

从[验证方法 v2](METHOD_v2.en.md)和[网站存证页](https://aibtc.bot/explorer/events)开始，把[提示词](PROMPT.en.md)与某条记录复制出的完整材料一起交给 AI。

**一笔交易，连同池子储备的变化，一起留下可验证的证明，交给你的 AI 独立复算。**

先核原始字节和记录指纹，再核 Merkle 关系、批次清单及 Bitcoin 锚定；方法覆盖的成交，还可以用整数公式重算成交数量、手续费与储备变化。Bitcoin 锚定的是摘要承诺，完整成交 JSON 从公开日志取得。

用[参考脚本](../reference-proof.md)核指纹和 Merkle 关系，再按[核验步骤](WHAT_AN_AI_CAN_CHECK.md)核对 Bitcoin 锚定与成交公式。对比当前储备时，取该市场最新一笔记录的期末数值，用[公开接口](PUBLIC_ENDPOINTS.md)返回的 `as_of` 和 `stale` 对齐观察时点。
