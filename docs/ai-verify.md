# AI Verification

Let your AI verify every pack of the AiBTC Smart Covenant ledger, submit the verification hash, and share the verification reward by the AIBTC shares you hold.

## Open programming and covenants {#ai-verify-open}

AIBRC is the asset standard on Bitcoin; it plays the role ERC-20 plays on Ethereum. AiBTC is an application built with Smart Covenants.

A smart contract is everyone on one chain running together: the application lives inside the chain, every node executes the same code, and those nodes jointly decide the result. Both the rules and the execution environment are complex. In the AI era, smart contracts are challenged by AI every day and can meet a backdoor or a vulnerability at any time.

A Smart Covenant divides the work differently, the way food delivery and couriers do. The order states what is delivered, where, and what counts as delivered; different delivery apps and courier companies can each deliver in their own way. A Smart Covenant is that order: its rules are fixed and published at creation, they are pure mathematics, and they do not belong to any one application. Who executes, and how, is open. AiBTC is the first application to adopt these rules.

This is open programming: the covenant is public and execution is open. Other applications, users, and a user's own AI can all execute and check against the same covenant. Further along, a user with their own AI completes something peer to peer without going through any one application. It is also the starting point for exploring on-chain agents.

The more open execution becomes, the more verification matters. AI Verification is the first step on this path.

## 1. What is verified {#ai-verify-s1}

The AiBTC Smart Covenant ledger.

A Smart Covenant fixes and publishes the rules at creation, and AIBTC CORE executes those rules and keeps the ledger. That programmable ledger is what you verify.

Every trade and every liquidity change in AiBTC is a public record in this ledger. Records are chained: each one carries the fingerprint of the one before it. At intervals AIBTC CORE packs the new records, and distributed nodes write the fingerprint of the pack into a Bitcoin block. This is "Pack @N" on the explorer page.

Your AI checks three things:

1. The records in this pack are exactly what the ledger published, with nothing altered.
2. These records really are in this pack.
3. This pack really was written into Bitcoin.

The method is recomputation. The rules and the data are public. Compute it again; if the results match, it is true.

## 2. Why verify {#ai-verify-s2}

Because trust should not rest on anyone saying "it is correct".

The way of delivering may differ, but whether it was delivered must be checkable by everyone. So AiBTC is arranged like this:

- Bitcoin anchors the assets and provides time and finality that cannot be changed.
- A Smart Covenant fixes and publishes the rules at creation.
- Execution goes to a deterministic state machine: the same starting state, the same rules and the same events in the same order give exactly one result.

So anyone can replay this ledger. Large models are good at logical reasoning and weakest where things are ambiguous. Determinism removes the ambiguity: every step has one correct result. For an AI, verifying this ledger is like running a unit test.

Trust rests on records, not on endorsement or a referee.

## 3. Why verification is rewarded {#ai-verify-s3}

Because the right to verify has been handed out, and someone has to use it.

"Anyone can verify" is only a possibility. AI Verification turns it into a fact: for every pack, people and their AIs actually verify it and leave a public record.

The verification reward goes to those who do this. When the head or the tail does not match, the AI does not return a verification hash; it tells you which record is wrong. That alarm is what the reward pays for.

The larger reason: we are building a distributed AI network, and it starts with verification. Once many people's AIs verify this ledger, the network has its first nodes.

## 4. What this explores for AI and Bitcoin {#ai-verify-s4}

Bitcoin provides time and finality. A deterministic state machine provides a single result. AI provides verification that everyone can afford. Together they make every person and every Agent a verifying node.

The direction is the one stated at the top: open programming and covenants. The items below are examples of what we are exploring, not the end state. The aim is open programming and covenants: built for AI, with respect for what AI can do, and moving step by step toward more decentralization. The proposals in the AIBRC protocol repository are part of the same exploration. It starts from execution and verification: Instant Swap is execution built for Agent interaction, and AI Verification is verification that everyone's AI can take part in.

Three of them follow one another, each built on the one before.

**Step 1 (now): a distributed verification network for Smart Covenants.**

This is what AI Verification does: after every pack, many people's AIs recompute the Smart Covenant ledger. The more verifiers there are and the more spread out they are, the less this ledger depends on what any one party says.

You can submit on the web page, or use Agent authorization to let an Agent verify automatically. Agent authorization follows the idea of the AIBRC Agent Key proposal (AIP-0001): the main key stays in the wallet, and the authorization given to an Agent has a scope and an expiry. When Agent Key is implemented it replaces the current authorization and connects to Agent market making; AIBTC placed in liquidity will then count toward shares. From now on AiBTC rules follow the same order as this one: finalized first, Bitcoin-timestamped first, executed after.

**Step 2 (exploration): distributed indexing at the AIBRC protocol layer.**

The balance of an AIBRC asset on Bitcoin L1 is computed by an indexer replaying Bitcoin blocks under public rules. Today anyone can run the reference indexer. What comes next is to make this a network: many independent indexers compute under the same rules, publish their results and compare them, while wallets and personal Agents check their own balances with light proofs.

L1 assets are decentralized only when indexing is distributed. Bitcoin privacy for L1 assets, and the proposals in the AIBRC protocol repository (Agent Key, checkpoints, conditional settlement and others), all build on it.

At that point verification and payout can become protocol-layer rules executed jointly by those indexers, and the verification reward no longer passes through an AiBTC account. The proposal is in the AIBRC protocol repository: [AIP-0008](https://aibrc.io/proposals/AIP-0008-verification-reward/).

**Step 3 (exploration): Bitcoin privacy for L1 assets.**

Today every amount of an L1 asset is public, which is why anyone can compute the state. To keep amounts and holdings private, the chain can no longer carry them in the clear; it can only carry commitments and proofs. If a single indexer then decided what is valid, everyone would have to trust it. Only when many independent indexers validate and compare results can a private transfer be accepted without depending on any one party.

So distributed indexing is the foundation for privacy: it has to exist before privacy for L1 assets can be attempted.

**After that: user plus AI peer to peer, and on-chain agents**

AI is heading toward on-chain agents. The verification, authorization and indexing work being done now serves AI and lays the ground for that.

- User-level execution: a user and their own AI execute and check the same covenant peer to peer, without going through any one application.
- A multi-node Agent execution network: more than one executor, all executing the same rules and checking each other.
- Trusted hardware (TEE): the deterministic state machine and AI models execute autonomously inside trusted hardware, collecting fees and paying for their own operation, with anyone and any Agent able to check remotely which public code is running. Trusted hardware still depends on the reliability of the hardware itself and on the security of the hardware provider, so it is one step along the way.
- On-chain agents: the correctness of execution is verified directly on the Bitcoin chain and funds are released according to that verification, so no party holds custody while the rules still execute.

The goal is to join execution, verification and settlement into one, moving step by step toward more decentralization.

Speed comes from off-chain matching. Trust comes from recomputing it yourself. Finality is anchored to Bitcoin.

## 5. How to take part {#ai-verify-s5}

1. Open the AiBTC explorer and, under "My verification", click "Copy @N proof and prompt".
2. Give the copied text to your AI. It recomputes, checks, and returns a verification hash.
3. Paste the verification hash back under "My verification" and submit.

To have an Agent do it automatically: click "Agent authorization", sign once in your wallet, and give the authorization code to your AI or to the AiBTC MCP tool. For 24 hours it verifies every pack and submits. The code can only submit verifications for this address; it cannot trade or withdraw.

In each pack, the first and the last publicly visible records are verified. The verification hash is computed from those two records, the hash of the Bitcoin block that anchors the pack, and your login address. It is therefore different for every address, so submitting someone else's result does nothing, and nobody can compute it before the pack is on chain. The records in between are sealed in the same pack, and anyone can spot-check any of them at any time with "Copy proof" on a single record.

## 6. Where the reward comes from, and on what basis it is paid {#ai-verify-s6}

AiBTC is neither the payer nor the referee.

- **Source**: the ecosystem address `bc1pm0rnskm4264ulh0g4j6fxd207tu36d47dm4t8g7xknftgwzg9m9q2dk6qk` deposits AIBTC on the Bitcoin chain into its AiBTC account. That account is the reward pool and has no other use.
- **Basis**: the rule core `aibtc-verify@V1` was finalized and Bitcoin-timestamped before the deposit. By depositing after that, the ecosystem address agrees to release under this rule; it can withdraw the unreleased part at any time.
- **Execution**: AIBTC CORE executes only the rule core. Every settlement is a public record that cites the rule fingerprint, and any person or AI can recompute it.
- **Custody**: held by Atom Unit, like every user's balance. To move a credited reward to your own wallet, use AIBRC withdrawal: your wallet signs, delivery is on chain.

## 7. How it is split and credited {#ai-verify-s7}

- Each pack releases 1/10,000 of the reward pool's available balance.
- 1,000 AIBTC = 1 share, split by shares. Shares are counted from the AIBTC available in your AiBTC account at settlement.
- A pack opens when it is on chain. It closes and settles when the first pack with a larger number is on chain after it.
- At settlement the verification reward goes directly into your AiBTC account.
- A pack nobody verified is shown as settled as usual: 0 addresses, 0 shares, nothing released.
- While people keep verifying, each settlement record enters the next pack, so packing and release continue one after another at the pace of Bitcoin anchoring.

Example: this pack releases 2,000 AIBTC and 4 addresses are verified with 1, 2, 5 and 12 shares. That is 20 shares at 100 AIBTC each, so they receive 100, 200, 500 and 1,200 AIBTC.

## 8. Rule text and how to check it {#ai-verify-s8}

- Rule core: `aibtc-verify@V1.txt`, [GitHub](https://github.com/aibtcbot/aibtcbot/blob/780f56b4537a208361ca4d3da0f31ce6a0f6411b/rules/aibtc-verify%40V1/aibtc-verify%40V1.txt).
- Rule fingerprint (SHA-256 over all bytes of the file): `8e5eccc1f19de8068e75e1335fa98cb41a1b3efb726387ad2a9a94d05bdf5a56`
- Bitcoin timestamp proof: `aibtc-verify@V1.txt.ots`, in block: 977,832 (2026-11-27 18:32:07 UTC).
- Rule notes (clause-by-clause explanation): [GitHub](https://github.com/aibtcbot/aibtcbot/blob/main/rules/aibtc-verify%40V1/aibtc-verify%40V1.notes.zh.md). The notes can be adjusted; where they differ from the rule core, the rule core prevails.
- The "verification hash" section of the verification method gives the full formula and one real worked example.

## 9. Limits of the first version {#ai-verify-s9}

- The formula is public, so a program can compute the same verification hash; the model name is whatever the submitter enters.
- Until release, the coins in the reward pool are held by Atom Unit, like every user's balance; submissions go to AIBTC CORE first, and the settlement list is public.
- Shares are the available balance AIBTC CORE reads at settlement, and they appear in the public list.
- A fault interrupts nothing: a payout that was not posted is listed in the settlement record, and once the program is fixed the next pack proceeds as usual.

These limits are the reason the explorations in section 4 exist.
