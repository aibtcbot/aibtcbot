# 05 AIBTC CORE

**05 AIBTC CORE · Bitcoin's Deterministic Execution Engine**

**Bitcoin Settles. CORE Executes. Every Step Replayable.**

## Why does Bitcoin need an execution engine? {#c5-s1}

Bitcoin produces a block roughly every 10 minutes — its rock-solid strength, and a built-in limit for high-frequency apps. Meme launches, swaps in seconds, per-block automatic buybacks… if every step had to queue on Bitcoin mainnet and pay gas, no modern DeFi product could run.

The industry's past answers came in two kinds: bridge assets out to another virtual machine — in effect abandoning Bitcoin mainnet — or accept that Bitcoin can "only store and transfer" and give up the app layer entirely.

**AIBTC CORE offers a third way: treat Bitcoin as the final settlement layer, hand high-frequency execution to a Deterministic State Machine, and record every state change so anyone — person or Agent — can replay and verify it at any time.**

> **Speed from off-chain matching, trust from recomputing it yourself, final settlement anchored to Bitcoin.**

---

## Architecture: where CORE sits in the system {#c5-s2}

```text
  Bitcoin L1                     AIBTC CORE                     Users / Agents
  ──────────────                 ──────────────                 ──────────────
  AIBRC asset & rule records     Unified account Ledger         Wallet signs · keys stay yours
  Deposit · Withdraw · Deploy    Curve · V2 AMM · Buyback       Preview ──► Authorize ──► Execute
  PoW final confirmation         Deterministic · idempotent     Local recompute · state hash check
       │                              │                              │
       │  Deposits in · payouts out   │  Merkle proof v2 · OTS       │
       └──────────────┬───────────────┴──────────────┬───────────────┘
                      ▼                              ▼
         Indexer A (protocol state)   Public event stream (execution records)
```

> **In one line**: Bitcoin decides where assets come from and where they go; CORE decides how every entry in between is computed; the public event stream lets anyone check.

---

## 1. What CORE is {#c5-s3}

AIBTC CORE executes AiBTC's market and account rules.

| Responsibility | What CORE does |
| --- | --- |
| **Account ledger** | Maintains BTC and AIBRC balances in each user's unified account |
| **Market execution** | Runs the bonding curve, V2 AMM, R1 fee sharing and block buybacks under the published rules and root-deployment parameters |
| **Public records** | Records execution events in a hash chain and anchors batches to Bitcoin |

**The same inputs give the same outputs.** Users and Agents can recompute the published calculations using the same rule version, starting state and event order.

---

## 2. Unified account: one address, one ledger {#c5-s4}

CORE carries AIBRC's address-level balance model into the platform, keeping one clear unified-account ledger per user.

```text
Unified Ledger
    ├─ BTC balance
    │     ├─ Available  (instant trading, withdrawals)
    │     ├─ Locked     (open orders, withdrawals in progress)
    │     └─ Total
    └─ AIBRC asset balances (isolated per asset, same three fields)
```

### Four iron rules of the ledger

1. 1. **The Ledger is the only source of balances**: no second ledger, no hidden credit path around it.
2. 2. **Only Available moves**: locked funds can't be used; a failed trade unlocks at once and never over-deducts.
3. 3. **No double spending, no duplicate entries, no minting out of thin air**: every state correction is an appended event, replayable and auditable end to end.
4. 4. **Segregated Signing**: dual-input isolated control. Withdrawal and state-settlement transactions use PSBT (Partially Signed Bitcoin Transactions); the user's local wallet and the AiBTC protocol vault each independently sign the transaction inputs they control. The user's private key stays on the user's own device at all times. Without the user's local signature, the protocol vault's isolated signature is an incomplete input: the transaction cannot be broadcast or mined. **Tiered Verification**: byte-by-byte transaction rebuild. When funds trigger a withdrawal, the signing service rebuilds the standard raw transaction in full from the off-chain frozen order and compares the input sources, output addresses and change amounts byte by byte, ruling out any field tampering. **On-Chain Verification**: zero bridges, zero wrapped assets. No cross-chain bridges, sidechains or wrapped tokens. Every market order settlement and state transition is anchored into Bitcoin blocks through a Merkle root; third-party nodes, auditors or AI Agents can complete a deterministic independent replay using only the public on-chain proofs.

---

## 3. Dual-track Swap: Instant and Block Swap {#c5-s5}

CORE gives users two parallel trading routes for different preferences of speed and sovereignty.

```text
[ Track 1: Instant Swap ]
  Platform account ──► AIBTC CORE matching in seconds ──► Platform account
- Continuous quotes on the bonding curve / V2 AMM
- Deterministic execution, credited in seconds
- For high-frequency trading, swing trades and Agent strategies

[ Track 2: Block Swap ]
  Bitcoin transaction ──► on-chain confirmation ──► CORE credits per the confirmed result
- Started straight from your external wallet, signed locally
- Follows Bitcoin's block cadence, with atomic on-chain delivery
- For users who want every settlement step directly on L1
```

### Dual-track at a glance

| Dimension | Instant Swap | Block Swap |
| --- | --- | --- |
| **Speed** | Matching in seconds | 1–2 Bitcoin block confirmations |
| **Where funds sit** | AiBTC unified account balance | Your local external wallet ⇄ on-chain delivery |
| **Fees** | Platform base trading fee (no per-trade on-chain gas) | Platform base trading fee + Bitcoin network fee |
| **Authorization** | Session trading authorization | Local wallet signature for each action |

Both routes share one set of swap rules and one ledger; quote formulas, fee rates and R1 fee sharing are identical. The only difference is the on-chain rhythm of funds moving in and out.

---

## 4. Execution flow: from one request to one tamper-evident record {#c5-s6}

CORE handles every funds change through a strict deterministic transaction pipeline:

```text
① Request   ──► Idempotent request ID · rule version · inputs
       │
       ▼
② Preview   ──► Read state → quote, fees & split → expected result (no state change, deterministic)
       │
       ▼
③ Authorize ──► User / Agent confirms → wallet signature or session authorization
       │
       ▼
④ Execute   ──► Atomic: debit ➔ compute ➔ credit ➔ share fees ➔ log event; any failure rolls back
       │
       ▼
⑤ Record    ──► Appended to the hash chain → state hash updated → Merkle proof v2 → batches anchored to Bitcoin
```

### Three core execution principles

- **Idempotent**: resubmitting the same request ID executes only once; network jitter or front-end retries never cause a duplicate fill or charge.
- **Atomic**: debit, swap, fee sharing and bookkeeping either all happen or none do; no half-finished records.
- **Fail-Safe**: on anything it can't determine (such as an on-chain reorg conflict, an unexpected balance change or a rule-version mismatch), CORE pauses processing instead of guessing. Priority order: **Safety > Recoverability > Determinism > Availability > Throughput**.

---

## 5. Block buybacks: driven by Bitcoin's block cadence {#c5-s7}

The R1 covenant's system buyback path is driven by CORE on Bitcoin block height — a textbook case of on-chain cadence driving off-chain execution:

```text
New Bitcoin block height H observed
         │
         ▼
Does the buyback vault's available BTC reach the threshold?
         ├─ [No] ──► Skip this block; no borrowing, no overdraft
         └─ [Yes]
         │
         ▼
Create a buyback task (task ID bound to height H: one run per block)
         │
         ▼
Buy AIBRC on the V2 AMM pool at the live effective-reserve quote
         │
         ▼
Bought AIBRC moves at once into the one-way system lock account
         │
         ▼
BUYBACK_EXECUTED event written to the hash chain
```

> **Note**: buybacks are hard-triggered by Bitcoin block height; bought-back assets go into a one-way system lock account, **which is not the same as burning total supply**.

---

## 6. Public events: letting the records speak {#c5-s8}

Every CORE state change produces a structured event, each linked to the last in a tight hash chain:

```text
Event N-1 ──(hash)──► Event N ──(hash)──► Event N+1
   │                    │                   │
   └─ Rule version hash └─ Command hash     └─ State root hash
                               │
                               ▼
                        Merkle proof v2
                               │
                               ▼
 Distributed nodes (OpenTimestamps) anchor to a Bitcoin block
```

| Record layer | Question it answers | Who can check? |
| --- | --- | --- |
| **Event hash chain & Merkle proof v2** | What happened, and in what order? Was anything secretly altered or removed? | Anyone (via the public API and JSONL export) |
| **State root hash** | Does the global ledger at a given height match what I computed locally? | Users and Agents running the reference verifier |
| **OTS anchor proof** | Did this ledger record exist before a given Bitcoin block? | Anyone (with standard open-source OTS tools) |

*(Note: the public event stream filters out private fields such as deposit/withdrawal addresses and txids, keeping only command hashes and rule-version hashes — transparent for audit, private for users.)*

---

## 7. Agent-friendly: designed for machines from day one {#c5-s9}

The future of finance belongs to Autonomous Agents. CORE's interfaces are built not only for people to read, but for machines to read and write smoothly:

```text
┌──────────────────────────────────────┬────────────────────────────────────────────────┐
│ What an Agent needs                  │ What AIBTC CORE provides                       │
├──────────────────────────────────────┼────────────────────────────────────────────────┤
│ Machine-readable deterministic rules │ Rule version + reference contract + parameters │
│ No duplicate execution on resubmit   │ Strict idempotent Request ID                   │
│ Results known before execution       │ Stateless deterministic Preview                │
│ Protection against abuse floods      │ Rate limits by identity & credential           │
│ Replaying the ledger afterwards      │ Event-chain export API + local verifier        │
└──────────────────────────────────────┴────────────────────────────────────────────────┘
```

> **Security floor**: an Agent can preview markets, compare strategies, flag risks and draft trades for you, but **final asset signing and authorization always stay in your local wallet**. CORE never accepts blind direct calls from an AI that you haven't confirmed.

---

## 8. Execution and public verification {#c5-s10}

AIBTC Labs runs CORE as the execution node today. CORE records market events, Merkle proofs link records to batch checkpoints, and OpenTimestamps anchors each published batch digest to Bitcoin. Use the [verification guide](../verification/README.md) to check a copied record with your Agent.

Multi-node execution and independent Agent witnesses are directions for future development.

---

## Closing: giving Bitcoin its own high-speed execution layer {#c5-s11}

AIBTC CORE gives Bitcoin assets fast execution under public rules, with records that people and Agents can check.

### **Bitcoin holds final settlement, CORE carries execution, and auditing belongs to everyone.**

**Bitcoin Settles. CORE Executes. Everyone Can Verify.**
