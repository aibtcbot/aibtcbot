# Reference proof script

Use the existing reference script with the complete proof copied from an Explorer record.

- [Download the Python script](../proofs/aibrc-merkle-reference-v3.py)
- [Download its SHA-256 file](../proofs/aibrc-merkle-reference-v3.py.sha256)
- [Read the Explorer & Agents guide](guide/06-explorer-agents.md)
- [Read the signing and proof notes](wallet-signatures.md#8-reference-verification-script)

The script uses the Python 3 standard library. It reads a local file and makes no network requests. No wallet connection, private key, platform login or database access is required.

Save the complete copied proof as `copied-proof.txt`, then run this command from the repository root:

```sh
python3 proofs/aibrc-merkle-reference-v3.py copied-proof.txt
```

For a complete copied proof, a successful result is:

```text
FINGERPRINTS_AND_MERKLE_MATCHED_OTS_BITCOIN_NOT_VERIFIED
```

This checks the record and manifest fingerprints, inclusion proof and any supplied consistency proof. Complete the OTS-to-Bitcoin check and supported business-formula recomputation separately, using the verification method included with the copied proof.

The GitHub script includes compatibility for LF and CRLF input files. Its checksum belongs to this file; no change to the trading website is required to use this copy.

For the complete method, AI prompt, public endpoints and evidence scope, start with [Verify a trade and its pool reserves](verification/README.md).
