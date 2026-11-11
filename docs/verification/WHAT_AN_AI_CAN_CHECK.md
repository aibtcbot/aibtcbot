# Verify a trade with your Agent

Open a trade in the [Explorer](https://aibtc.bot/explorer/events) and select **Copy proof**. Give the proof, [Method v2](METHOD_v2.en.md) and the [AI prompt](PROMPT.en.md) to your Agent.

| Check | What to compute |
| --- | --- |
| Record fingerprint | Recompute `event_hash` from the original record bytes and compare it with the recorded hash. |
| Merkle inclusion | Check the record's path and position against the batch's tree root. With two authenticated heads from the same network and log epoch, also check their append-only consistency. |
| Bitcoin anchor | Recompute the batch digest and match it to the OTS commitment. Run the OTS proof and compare the result with the Bitcoin block's Merkle root from an independent source. |
| Trade amounts and fees | For the AMM formula version in Method v2, recalculate the fill, fees and ending reserves from the recorded starting reserves using integer arithmetic. |
| Current pool reserves | Compare the latest record's ending reserves with the same market's [public snapshot](PUBLIC_ENDPOINTS.md#market-snapshots). Use `as_of` and `stale` to check the snapshot's timing and freshness. |

Start locally with the [Python reference script](../reference-proof.md) for record fingerprints and Merkle checks.
