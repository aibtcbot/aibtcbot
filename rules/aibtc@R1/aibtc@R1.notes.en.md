# aibtc@R1 rule notes: why it is written this way

The R1 rule text is on chain: `inscriptionText()` on contract `0xed976e7b95d099c60318ef848c73d584ee5eb08a` returns the full text, and `INSCRIPTION_TEXT_SHA256` returns its SHA-256. The contract has no write interface for changing rules or parameters.

The text itself holds only parameters and mathematics. This page explains why, so that people and AI can read the text with its purpose in mind. This page can be adjusted; where it differs from the rule text, the rule text prevails.

## 1. Open programming and covenants

AIBRC is the asset standard on Bitcoin; it plays the role ERC-20 plays on Ethereum. AiBTC is an application built with Smart Covenants.

A smart contract is everyone on one chain running together: the application lives inside the chain, every node executes the same code, and those nodes jointly decide the result. In the AI era, smart contracts are challenged by AI every day and can meet a backdoor or a vulnerability at any time.

A Smart Covenant is like a delivery order: it states what is delivered, where, and what counts as delivered, and different applications can each deliver in their own way. Its rules are fixed and published at creation, they are pure mathematics, and they do not belong to any one application. Who executes, and how, is open. This is open programming: other applications, users, and a user's own AI can all execute and check against the same covenant.

## 2. Why EVM becomes the rule base for Bitcoin

Bitcoin has deep, widely recognized value and a public ledger; EVM has a mature smart-contract language and developer ecosystem. AiBTC connects the two, so smart-contract rules serve Bitcoin L1 assets.

Not moving BTC to another chain first, but bringing EVM's capabilities back to Bitcoin.

Bitcoin answers "where do assets and rules come from", EVM defines "how to calculate", AIBTC CORE handles "how to execute", and verifiers check "does the result follow the rules".

How is this different from other Bitcoin programmability routes? Some routes put a virtual machine inside Bitcoin transactions, so every action runs on-chain; others first bridge BTC to another chain and use that chain's contracts. R1 takes a third path: the asset and its rule identity are recorded on Bitcoin, the rules are pure math in an immutable public contract, and instant trades apply that same math in the unified account — no on-chain transaction per trade, yet every step is written to a replayable event hash chain.

## 3. What AI does here

Explicit parameters, triggers, formulas and result records give Agents a basis to understand and check trades. People state the goal, tools understand the rules, and execution leaves evidence.

Public rules answer "how it should be calculated"; execution records answer "what actually happened". Verification puts the two together and checks that they match. Large models are good at logical reasoning and weakest where things are ambiguous. Determinism removes the ambiguity, so for an AI, checking one R1 trade is like running a unit test.

## 4. What this explores for AI and Bitcoin

The direction is open programming and covenants: the covenant is public, execution is open, and a user with their own AI can complete something peer to peer. It is also the starting point for exploring on-chain agents. We take three steps, each built on the one before.

- **Step 1 (now): a distributed verification network for Smart Covenants.** After every pack, many people's AIs recompute the AiBTC Smart Covenant ledger. This is AI Verification. Agent authorization follows the idea of the AIBRC Agent Key proposal (AIP-0001); when Agent Key is implemented it replaces the current authorization and connects to Agent market making.
- **Step 2 (exploration): distributed indexing at the AIBRC protocol layer.** Many independent indexers compute under the same rules, publish their results and compare them. L1 assets are decentralized only when indexing is distributed. Bitcoin privacy for L1 assets, and the proposals in the AIBRC protocol repository (Agent Key, checkpoints, conditional settlement and others), all build on it.
- **Step 3 (exploration): Bitcoin privacy for L1 assets.** Distributed indexing is the foundation for privacy: it has to exist before privacy for L1 assets can be attempted.
- **After that (none of this is built):** a user and their own AI executing and checking the same covenant peer to peer; a multi-node Agent execution network; autonomous execution by a deterministic state machine and AI models inside trusted hardware.

Starting from R1, the covenant system can keep exploring more applications through new rule versions, reference addresses and parameter designs, together with matching execution and verification.

## 5. Why R1 is written this way

- **Only parameters and pure math (articles 02 to 06).** Given the trade amount, market stage and rule parameters, there is an explicit method for how fees are computed and how rule fees are split. So every step has one correct result, and any person or AI can recompute it.
- **The rule identity is written into Bitcoin (article 01).** The parameter line `aibtc@R1:<reference contract address>:T<tax>:C<destination>` is written to the genesis root transaction, in the same transaction as the AIBRC deployment. So which rule an asset uses can be read from Bitcoin, and it cannot change after creation.
- **The contract is immutable and has no write interface (articles 09 and 11).** Future extensions require a new version, a new address and new assets with explicit new parameters; existing assets keep their versions and parameters. So an existing commitment is not altered by a later upgrade.
- **The contract gives the method; it does not custody or execute (article 10).** An executor applies the same mathematics to fixed parameters without requiring per-trade EVM calls. So R1 needs no wrapped-BTC bridging and no extra EVM gas per trade.
- **The rules belong to no single application (article 10).** Any application infrastructure can reuse the same rules to execute and account for an asset's fixed parameters; AiBTC is the first application infrastructure built on them. So execution is open, which is what open programming means.
- **The rule fee takes effect only after graduation (article 02).** Before graduation only the 0.5% platform fee applies, and the graduation-triggering trade still uses the pre-graduation rule. So during launch everyone faces the same base fee.
- **The rule fee has only two destinations (article 06).** All of it goes to buyback, or all of it goes to the creator, chosen at creation. So where each rule fee went can be checked against the parameters.
- **A reserved directory of 15 entries (article 08).** These names state only possible future topics, not implemented functions. They are in the text so that the direction is public and the boundary is clear.

## 6. Check it yourself

- Full rule text: `inscriptionText()` on contract `0xed976e7b95d099c60318ef848c73d584ee5eb08a`; its fingerprint: `INSCRIPTION_TEXT_SHA256`.
- The same address is deployed on Ethereum, BNB Chain and Base: [Etherscan](https://etherscan.io/address/0xed976e7b95d099c60318ef848c73d584ee5eb08a#code) · [Basescan](https://basescan.org/address/0xed976e7b95d099c60318ef848c73d584ee5eb08a#code) · [BscScan](https://bscscan.com/address/0xed976e7b95d099c60318ef848c73d584ee5eb08a#code).
- Which rule an asset uses: read the parameter line in its genesis root transaction.
- Any single trade: in the AiBTC explorer, click "Copy proof" on that record and give it to your AI.
