# 06 Explorer & Agents

### Make everyone's Agent an independent verifier of the Bitcoin ecosystem

Don’t Trust. Verify. With Your Own Agent.

Bitcoin lets people verify instead of trusting blindly. Agents give that ability a chance to leave the developer's terminal and enter everyone's daily life.

Copy a trade's raw record, batch manifest, OTS proof and block height from the Explorer. Your Agent can recompute the fingerprints, check the Merkle path and trace the OTS proof to the Bitcoin block.

## How it works: how a trade becomes a fingerprint on Bitcoin {#c6-s1}

```text
A trade
  │  canonical_payload (raw bytes, never reordered)
  ▼
Event hash  event_hash = SHA256(TAG‖TAG‖prev_hash‖seq‖len‖payload)
  │  Each record wraps the previous record's hash → a linked hash chain
  ▼
Global Merkle tree  RFC 9162, leaves from event_hash, through record N
  │  Inclusion proof: this record → treeRoot
  ▼
Batch manifest  manifest { logEpoch, treeSize, treeRoot, chainTip, prevCheckpoint, ... }
  │  checkpoint_digest = SHA256("AIBRC-CHECKPOINT-V1"‖manifest)
  ▼
OTS proof  Submitted to ≥2 independent calendars (e.g. alice.btc.calendar / finney.eternitywall)
  │  Calendars aggregate digests into a Merkle tree; the root goes into a Bitcoin transaction
  ▼
Bitcoin block H  Merkle root = the same block's Merkle root on an independent explorer
```

Four layers of fingerprints, each recomputable with public formulas:

| Layer | What it fixes | What a change does |
| --- | --- | --- |
| event_hash | Every field of this record + the record before it | Change any field and the hash changes; every later record breaks from the chain |
| treeRoot | Ordered records through N | Changing a leaf, position or historical prefix breaks the proof |
| checkpoint_digest | Manifest (log epoch, size, root, previous batch) | Batches chain too; changing a past batch means changing every later batch |
| Bitcoin Merkle root | This digest existed before block H | Can't be changed without rewriting Bitcoin |

## 1. Look up transactions: hash search & record details {#c6-s2}

```text
Search
    ├─ Event hash / command hash → single execution record
    ├─ Sequence number           → position in the global event stream
    ├─ Bitcoin txid              → root deploy / deposit / withdrawal / Block Swap
    ├─ Asset ID                  → asset page: root tx, rule identity, supply, liquidity
    └─ Account reference         → account page: trade history under the public reference
```

The record detail page has three areas:

| Area | Contents | Purpose |
| --- | --- | --- |
| Display layer · display | Direction, amount, fee, stage before / after, hashes | For people |
| Record layer · record | canonical_payload raw bytes, event_hash, previous_event_hash | For machines ① |
| Proof layer · inclusion + checkpoint + ots + bitcoin | Batch manifest, digest, OTS file, block height & hash | For machines ②③④ |

**Copy proof** gives you all three layers. Use the original `canonical_payload` bytes to recompute the event hash.

Public records contain no deposit/withdrawal addresses, txids or internal IDs — only command hashes, account-reference hashes and rule-version hashes.

## 2. On-chain status: batches, blocks & confirmation {#c6-s3}

Each record shows how far it has got:

| Status | Meaning | How to read it |
| --- | --- | --- |
| PUBLISHED | Record is in the hash chain, not yet in a batch | Committed by the platform, not yet on Bitcoin |
| CHECKPOINTED | In a batch; OTS awaiting confirmation | Digest submitted to calendars, waiting for a block |
| ANCHORED | OTS traced back to Bitcoin block H | Ready for independent verification |
| MISMATCH | Local record doesn't match the chain | Needs attention |

## 3. Copy records: raw data & full proofs {#c6-s4}

Click "Copy proof" to get a JSON pack (schema AIBRC_EXPLORER_PROOF_COPY_V2):

```text
{
  material_integrity   ← page check before copying
  record               ← canonical_payload + event_hash + previous_event_hash
  inclusion            ← this record's Merkle inclusion proof
  display              ← human-readable fields
  checkpoint           ← canonical_manifest + checkpoint_digest
  ots                  ← OTS file, base64
  bitcoin              ← block height / hash / time
}
```

Save the proof pack and method together to run the checks later. Open-source reference: [GitHub · aibtcbot/aibtcbot](https://github.com/aibtcbot/aibtcbot)

## 4. Verify a trade with your Agent {#c6-s5}

This is the explorer's core use. You don't need to understand hashes — just copy and paste.

### Steps

```text
① Click "Copy proof" on the record page
② Open any AI (Claude / ChatGPT / Gemini / a local model)
③ Paste "AiBTC Verification Method v2" + the proof pack
④ Ask your Agent to compute and report the result of each check
```

### What the AI does

```text
① Record fingerprint   Recompute event_hash from the raw payload bytes  → correct?
② Inclusion proof     Verify the RFC 9162 position and path → matches manifest treeRoot?
③ Batch fingerprint    Recompute checkpoint_digest  → was the manifest changed?
④ Bitcoin              Parse the OTS → get height H and the Merkle root
                       Check block H on mempool.space yourself  → same Merkle root?
⑤ Trade recompute      amountOut & fee by the public formula (x·y=k, round down; fee rounds up)
```

Report each result from the material actually copied

| Check | Result |
| --- | --- |
| Record fingerprint | Compute: match / mismatch |
| Inclusion proof | Check the position, tree size and root |
| Manifest fingerprint | Compute and compare checkpoint_digest |
| OTS and Bitcoin | Check the digest, attestation and independent block |
| Append-only history | Check consistency when two authenticated heads are supplied |
| Trade recomputation | Apply Method v2 to its matching AMM event and formula version |

Use the [Python reference script](../reference-proof.md) to start with fingerprints and Merkle checks. The [verification guide](../verification/README.md) walks through the Bitcoin anchor, trade calculations and comparison with current pool reserves.

## 5. Agent interaction: state intent, preview the trade, authorize in your wallet {#c6-s6}

Beyond verification, Agents can also trade on your behalf, but the path is fixed and signing always stays with you.

```text
"Buy this asset with 50,000 sats for me"
         ▼
Agent reads the rules: rule-version hash, fee rate, graduated or not, current virtual reserves
         ▼
Calls the deterministic Preview → expected fill, fee breakdown, unfilled refund
         ▼
Shows you the preview
         ▼
You sign in your local wallet / session authorization   ← the Agent never touches private keys
         ▼
CORE executes idempotently → event written to the hash chain
         ▼
Agent recomputes the fill afterwards and confirms it matches the preview
```

Interfaces are designed for Agents: machine-readable specs, idempotent request IDs, deterministic preview and per-identity rate limits. Agents can preview, compare, remind and pre-fill; they can't decide whether a trade is valid, change balances or broadcast funds automatically.

## 6. Ecosystem direction: open interfaces, user-level execution & a verification network {#c6-s7}

```text
Today ────────────────────────────────────────────────────────────────────────────────► Further
─────────────                   ─────────────                     ─────────────
Explorer + proof copy           Reference verifier + MCP / CLI    User-level witness network
Any AI recomputes (method v2)   Agents replay from a snapshot     N independent Agent witnesses
Single-record verification      Full JSONL export + state hash    Auto alert / HALT on mismatch
```

Witnessing, not consensus. Your Agent runs the reference verifier to compute the state hash at height H, signs a witness "state at H = X" with your wallet and sends it back to the platform; the page shows "N independent Agents witnessed a match". No leader, no staking, no slashing.

### The explorer is for people to read, Agents for machines to compute, and wallets for you to decide

Don’t Trust. Verify. With Your Own Agent.
