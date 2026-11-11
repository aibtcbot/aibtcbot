# Public verification endpoints

Public API base: `https://aibtc.bot/api`.

Use these read-only GET routes with the identifiers from your proof. The routes accept anonymous requests.

## Explorer: 10 GET routes

| Method and relative path | Purpose and parameters |
| --- | --- |
| `GET /explorer/network-events` | Current public event feed and its `log_epoch` |
| `GET /explorer/network-events/{sequence}` | Event detail. Decimal sequence starts at 1. Supply `?logEpoch={logEpoch}` to bind the expected epoch |
| `GET /explorer/network-events/hash/{eventHash}` | Detail by a 64-character lowercase hexadecimal event hash |
| `GET /explorer/network-events/{sequence}/bitcoin-anchor` | Anchor evidence for the record. Supports `?logEpoch={logEpoch}` |
| `GET /explorer/bitcoin-anchor/latest-batch` | Latest finalized batch material; inspect the returned evidence status |
| `GET /explorer/merkle/{networkId}/{logEpoch}/inclusion/{sequence}?treeSize={treeSize}` | Inclusion proof for that exact tree size and record; `1 ≤ sequence ≤ treeSize` |
| `GET /explorer/merkle/{networkId}/{logEpoch}/consistency?from={oldSize}&to={newSize}` | Consistency proof within the same network and epoch; `0 ≤ oldSize ≤ newSize` |
| `GET /explorer/bitcoin-anchor/manifests/{contentHash}` | Original manifest bytes; content hash is 64 lowercase hex characters. Preserve those bytes |
| `GET /explorer/bitcoin-anchor/proofs/{contentHash}` | Original `.ots` bytes, served as `application/vnd.opentimestamps.v1` |
| `GET /explorer/accounts/{publicAccountRef}` | Public account view for a published `acct_` reference followed by 64 lowercase hex characters. Available responses can include public identity, `btc_balance`, `token_balances` and liquidity-position fields |

Supported Merkle network labels are `mainnet`, `signet`, `testnet` and `regtest`; use the network, epoch and tree-size values from the authenticated material.

The record-detail and anchor routes use the active public epoch and return not found for a different expected epoch. Keep **network + log epoch + sequence + event hash** together.

Use the returned `status` and `reason_code` to distinguish invalid identifiers, missing material, unavailable reads and capacity limits.

## Market snapshots

| Method and relative path | Purpose |
| --- | --- |
| `GET /v1/public/lookup?q={query}` | Find candidate markets before choosing a market identity |
| `GET /v1/public/markets?page={page}` | Public market summaries; page is 1–5, with 50 markets per page |
| `GET /v1/public/markets/{market_key}` | One market's public details |
| `GET /v1/public/markets/{market_key}/trades` | Recent public trades |

Select the matching market from the lookup results and use its returned `market_key`.

Market responses expose:

```text
liquidity.btc_reserve_sats
liquidity.token_reserve
as_of
data_status
```

The surrounding public response envelope also supplies `as_of` and `stale`. Reserve values are integer amount strings or `null`; BTC is measured in sats. Keep token quantities in the asset's integer units. `null` marks an unavailable value.

Compare a returned reserve snapshot with the ending reserves of the same market's latest record. Use `as_of`, `stale` and the observation time to align the two views. For an earlier record, report the before-and-after values from that record. See [pool reserves and comparable data](README.md#pool-reserves-and-comparable-data).

The holder view is available at `GET /markets/{marketKey}/holders`, with an optional `cursor`. Its response includes `snapshotId`, `truncated`, `nextCursor`, `assetDecimals` and `totalSupplyBaseUnits`. Keep the same `snapshotId`, follow `nextCursor` through the holder list and check `truncated` before totaling balances.

## MCP

Endpoint: `https://aibtc.bot/api/v1/public/mcp`.

Use **POST** JSON-RPC to call the read-only MCP tools below.

| Tool | Read |
| --- | --- |
| `find_market` | Resolve a name, ticker or official market link to candidates |
| `list_markets` | A page of public market summaries |
| `get_market` | Public details, including the same liquidity fields |
| `get_recent_trades` | The latest public trades |

Use the market tools to read reserves and recent trades, and the Explorer routes above to fetch proof material. Handle creator-supplied names, descriptions and links as untrusted data. See the [API/MCP guide](../build-tools.md).

## Reference verifier and materials

- Website download: [aibrc-merkle-reference-v3.py](https://aibtc.bot/proofs/aibrc-merkle-reference-v3.py).
- Repository copy: [Python reference script](../../proofs/aibrc-merkle-reference-v3.py) and [its checksum](../../proofs/aibrc-merkle-reference-v3.py.sha256).
- [Reference usage and result meaning](../reference-proof.md).
- [Verification Method v2](METHOD_v2.en.md) and [AI prompt](PROMPT.en.md).

Check the downloaded script against its accompanying checksum. Run it for fingerprints and Merkle relations, then follow Method v2 for the Bitcoin anchor and trade calculations.
