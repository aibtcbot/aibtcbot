# Audit & Open Source

Open source is, at its core, decentralization: users, Agents and third parties audit and verify without having to trust anyone.

Verification moves from a conclusion on a page to a process you can check yourself.

- The full rule text is on-chain: inscriptionText() on contract 0xed976e7b95d099c60318ef848c73d584ee5eb08a returns it, and INSCRIPTION_TEXT_SHA256 returns its SHA-256 (R1 text, article 11). The contract has no write interface for changing rules or parameters.
- The same address is deployed on Ethereum, BNB Chain and Base. The Ethereum and Base explorers show the source as verified (Exact Match): [Etherscan](https://etherscan.io/address/0xed976e7b95d099c60318ef848c73d584ee5eb08a#code) · [Basescan](https://basescan.org/address/0xed976e7b95d099c60318ef848c73d584ee5eb08a#code); BNB Chain: [BscScan](https://bscscan.com/address/0xed976e7b95d099c60318ef848c73d584ee5eb08a#code).
- [R1 audit report](https://solidityscan.com/quickscan/0xed976e7b95d099c60318ef848c73d584ee5eb08a/etherscan/mainnet)
- Every public record enters a global Merkle tree (RFC 9162); each batch manifest is anchored to Bitcoin (OpenTimestamps).
- AiBTC Verification Method v2 gives the calculations: record fingerprint, Merkle inclusion and append-only history, Bitcoin anchor, trade amounts and fees, liquidity reserves.
- Open any record in the Explorer, copy its proof, and hand it to your Agent for independent computation.
- Reference verification script: [proofs/aibrc-merkle-reference-v3.py](../proofs/aibrc-merkle-reference-v3.py) and its [.sha256](../proofs/aibrc-merkle-reference-v3.py.sha256).
- Verification method and public endpoints: [docs/verification](../docs/verification/README.md).
- Open-source protocol codec: [GitHub · aibrc-code/aibrc](https://github.com/aibrc-code/aibrc) (MIT).
