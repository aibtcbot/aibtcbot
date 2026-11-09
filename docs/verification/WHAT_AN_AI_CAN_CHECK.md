# What your AI can check / 你的 AI 能核对什么

Give an AI the original proof material and the [method](METHOD_v2.en.md), then ask it to show the calculation for each conclusion. A named hash or a confident explanation is not the calculation itself.

## Checks supported by the relevant material

| Check | How to check it | Evidence and scope |
| --- | --- | --- |
| Reproduce recorded pool-reserve changes | Start from an identified state and apply the published calculation for each covered transition | Keep original before/after fields, rule versions and complete input coverage. Method v2's numerical trade formulas cover the specified AMM event/formula combination |
| Recompute a trade's amounts and fees | Calculate output, fee rounding and after-values using integer arithmetic; include the pending-buy pricing variant when present | Match the record's formula and fee-policy versions. A version not covered by this method is reported as not covered |
| Detect missing or changed records within an authenticated log range | Verify event fingerprints and inclusion; authenticate both heads before checking append-only consistency | Same network and epoch, with exact sizes and roots. This detects inconsistency in that committed range; it does not prove every possible business action was originally recorded |
| Establish the Bitcoin commitment for the supplied material | Verify the manifest fingerprint, then execute the OTS operations and compare the claimed Bitcoin block root independently | Keep the canonical bytes and the exact block height/root. An announced anchor or pending OTS attestation is not a completed check |
| Check token conservation when the complete state is available | Compare all relevant token-state categories with the published supply in the same units and context | Follow holder pagination and check `truncated`; include system/pool categories. A partial holder view alone cannot establish the total |
| Recompute the recorded fee and LP-fee-vault movement | Compare `feeBtcSats` and the before/after fee-vault values with the named fee rule | The LP-vault delta is not automatically the platform's total income; the method identifies fee components recorded elsewhere |
| Reproduce a published ranking with a fixed rule and complete inputs | Apply the stated scoring window, prices, weights and rounding | Requires the actual published scoring rule and full sample set. A current snapshot alone is not a complete contest dataset |

## What this material does not establish on its own

| Question | Additional evidence needed |
| --- | --- |
| Are the BTC recorded in the pool matched by particular chain outputs under the required control? | Wallet/UTXO identity, control and balance evidence tied to the same observation context; a committed pool number alone does not provide that mapping |
| Does a trade proof expose a complete customer funding, withdrawal or account-history dataset? | The relevant complete dataset. Some public account views include balance fields, but a trade bundle or selected public snapshot is not every customer's full history |
| Can the platform meet all of its obligations? | A complete, comparable view of assets and obligations. Record integrity and correct pool arithmetic do not supply that entire dataset |

**Read the result at the level actually checked:** bytes, log relation, Bitcoin anchor, covered trade formula and reserve comparison are separate checks. If an input is missing or a step was not run, say which one; do not turn that gap into either an automatic endorsement or an automatic accusation.

## 中文

把原始证明材料与[方法](METHOD_v2.en.md)一起交给 AI，让它逐项给出实际计算，而不是只评价项目介绍。

| 能核对的项目 | 怎么核对 | 证据范围 |
| --- | --- | --- |
| 池子储备的记录变化能否复算 | 从明确的初始状态出发，按公开计算规则重算覆盖范围内的状态变化 | 保留原始前后值、规则版本与完整输入；方法 v2 的成交公式只覆盖指定的 AMM 事件和公式版本 |
| 每笔成交数量和手续费是否符合规则 | 用整数计算数量、向上或向下取整、费用及成交后储备；存在在途买单定价变体时按对应字段计算 | 必须匹配公式和费用策略版本；方法没有覆盖的版本不能假装已经验算 |
| 已认证日志范围内有没有缺失或改动 | 核记录指纹、包含关系，并在独立认证新旧两个日志头后核追加一致性 | 网络和日志期次相同，大小和根精确匹配；不把这一点扩大成从未漏记过任何业务 |
| 这些材料对应哪一个 Bitcoin 摘要承诺 | 核批次指纹，执行 OTS 运算，并独立比对对应 Bitcoin 区块根 | 使用原始字节及准确区块高度；仅有锚定说明或待完成的 OTS 材料不等于已经核验 |
| 完整状态下代币总量是否守恒 | 将同一范围、同一单位下的相关余额、池子和系统类别与公开供应量核对 | 先检查持有人分页、快照与截断标记；不完整的持有人列表不能证明完整总量 |
| 记录的手续费及 LP 费用账变化是否正确 | 按费用规则核对手续费和费用账前后值 | LP 费用账增量不能直接当成平台全部收入；其他费用分量按方法所列范围另看 |
| 固定规则、完整数据下的公开榜单能否复算 | 按实际公布的评分窗口、价格、权重和取整重算 | 需要完整评分规则和样本；当前快照不能替代完整比赛数据 |

| 仅凭这些材料不能确定的项目 | 还需要什么 |
| --- | --- |
| 池子记下的 BTC 是否对应特定链上输出并满足控制要求 | 同一观察时点的钱包、UTXO、控制权和余额证据；池子账面数字本身不提供完整对应关系 |
| 某条成交证明是否揭示全部客户的存提和账户历史 | 对应的完整数据集；公开账户视图虽可包含部分余额字段，但一条成交或部分快照并不等于所有账户的完整历史 |
| 平台是否足以履行全部资金义务 | 完整且时点可比的资产与义务数据；记录完整、池子算数正确不能代替整套数据 |

原始字节、日志关系、Bitcoin 锚定、方法覆盖的成交公式与储备对比，分别报告实际核对结果。材料缺失或没有执行，就说明是哪一项，不自动判成全部通过或全部有问题。
