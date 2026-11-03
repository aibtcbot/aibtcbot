# Terminology

Names and interface labels follow the platform documentation and the current public website. These distinctions help you move between the app, the documentation and the protocol site.

| Term | Meaning in these docs |
| --- | --- |
| **AiBTC** | The platform: asset launches, trading, liquidity, developer tools and the user interface. |
| **AIBRC** | The Bitcoin asset and account protocol. Read its specifications at [aibrc.io](https://aibrc.io). |
| **Covenant Inscription** | The established English name for AIBRC's native protocol expression and assets. |
| **AIBTC CORE** | The platform's execution and accounting system. Its public records can be checked using the disclosed rules and proof material. |
| **Smart Covenant** | Versioned asset and execution rules, including the R1 and X1 concepts explained in the [covenant guide](guide/04-smart-covenant-liquidity.md). |
| **Instant** | Trading through platform account balances, without a separate Bitcoin transaction for each fill. |
| **Block Swap** | The wallet-based route combining BTC payment and an AIBRC transfer instruction in one Bitcoin transaction. The guide explains its current direction and confirmation stages. |
| **Trade Session** | A platform authorization with specific in-app permission scopes and an expiry. It is not a Bitcoin transaction signature. |
| **PSBT** | Partially Signed Bitcoin Transaction: transaction data passed between the parties that construct and sign a Bitcoin transaction. |
| **Co-signing** | Each participant signs the inputs it is responsible for in the same transaction. The handshake is not a generic 2-of-2 script covering every input. |
| **Deposit / withdrawal** | The conventional English terms used for moving assets into or out of the platform account, through the supported flow. |
| **Miner fee** | The Bitcoin network fee. Amounts are in sats; the fee rate is in sat/vB. |
| **Explorer** | The public-record interface, including record details, checkpoints and proof-copy actions. |
| **Merkle proof v2** | The user-facing proof-method name. [Format and script version identifiers](reference-proof.md) belong to their respective layers. |
| **Agent** | A client acting within the interfaces and permissions provided to it. Connecting the public MCP only grants read-only market access. |

For the exact bytes or fields used in a signature, use the [wallet signing notes](wallet-signatures.md); product names do not replace those rules.
