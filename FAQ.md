AiBTC Product FAQ

Bitcoin Hybrid DEX · One Fair Launch · One Pool, Two Swaps · An Asset Interface for Agents

AiBTC is a Bitcoin Hybrid DEX and fair-launch trading platform, powered by the AIBRC protocol. @ is both identity and address. Through @, AiBTC lets AI understand Bitcoin and makes every Bitcoin asset programmable. AIBRC, BRC-20, Runes and EVM assets all live in 1 address, with 1 fair launch. 1 liquidity pool powers 2 Swaps: 0-gas Instant Swap and Bitcoin Block Swap. AiBTC brings public-chain-grade trading and fair launches to Bitcoin.

This FAQ explains how those ideas connect: a unified asset standard for the Bitcoin ecosystem, identity and address through @, shared-root issuance through one fair launch, two trading routes powered by one pool, and a common language that lets Agents understand assets and work with their rules.

1. Understanding AiBTC

1. What is AiBTC?

AiBTC is a Bitcoin Hybrid DEX and fair-launch trading platform powered by AIBRC. It brings asset creation, continuous trading, liquidity and Agent interaction into one Bitcoin-based product experience.

A project can launch an asset, enter bonding-curve trading, graduate into a V2 liquidity pool and build services around its asset and community. One pool supports both 0-gas Instant Swap and Bitcoin Block Swap, connecting continuous account trading with direct wallet-based exchange.

AIBRC supplies the common asset and account language. Smart Covenant connects assets with public rules. AIBTC CORE executes application logic and maintains the account ledger. Public interfaces and execution records let people and Agents read markets, calculate outcomes and check results.

The product connects the asset's whole journey: creation, participation, trading, liquidity and continued use. Its core ideas are one identity and address interface, one fair launch, one pool with two Swaps, and assets that Agents can understand and interact with. Source: AiBTC overview

2. Why does Bitcoin need this kind of infrastructure?

Bitcoin keeps producing new protocols, assets and applications. Each adds something valuable, while projects often repeat the same work across ecosystems: issuing assets, integrating wallets, finding market infrastructure and organizing the community around another interface.

AiBTC and AIBRC address that repeated work through a unified asset standard and account foundation. Asset identity, balances, rules and operations gain a common language. Individual protocols retain their native mechanics, while applications reuse shared ways to discover assets and organize interactions.

For users, this means a more consistent way to participate. For developers, it means reusable account, market and integration tools. For Agents, it means asking the same clear questions about an asset: what it is, where its balance belongs, which rules apply and how to prepare an operation.

Projects can connect new capabilities to an existing asset family, market and community. Innovation in one protocol can become another useful part of the same project's experience. Sources: AiBTC overview, cross-protocol foundations

3. How do AiBTC and AIBRC work together?

AIBRC provides the unified asset standard and account foundation. AiBTC turns that foundation into a fair-launch platform, Hybrid DEX, liquidity system and interface for Agents.

AIBRC defines native asset creation, account identity, transfer authorization and deterministic asset-state calculation. Wallets, indexers, markets and Agents can implement the same public rules. External protocols connect through their own adapters, preserving their native identities and validity rules.

AiBTC adds the application experience: shared-root launches, bonding curves, V2 markets, Instant Swap, Block Swap and execution records. AIBTC CORE handles the corresponding application calculations and account changes.

A useful architectural comparison is the way ERC standards and execution infrastructure support reusable applications in other ecosystems. AIBRC supplies common asset and account definitions, while Smart Covenant and CORE connect rule identity with execution.

The protocol is openly implementable, so other wallets, applications and services can build on the same foundation. AiBTC brings those pieces together in its first application infrastructure. Sources: AIBRC overview, AIBTC CORE

2. @ as Identity and Address: Helping Agents Understand Assets

4. Why is @ both identity and address?

@ brings two closely related needs into one product expression: recognizing an identity and knowing how to interact with it. A person, asset or community needs an identity people can understand; an operation needs an address and account context that software can use.

AiBTC connects those ideas so people and Agents can follow one relationship from identity to asset information, rules and prepared actions.

For an Agent, an address becomes a starting point for understanding Bitcoin-native assets. It can identify the account, read its AIBRC holdings and amounts, resolve each asset's identity, and follow its deployment, market and rule information. Native AIBRC balances are organized by account, removing the need to identify an individual asset-carrying UTXO for each part of a balance.

The underlying account is derived from the Bitcoin scriptPubKey, and each asset has its own identifier. Related BRC-20, Runes and EVM applications connect through their own protocol data and references. The result is a clearer path from “who or what is this?” to “what can I do with it?” Sources: AIBRC accounts, shared application foundations

5. What does it mean for AIBRC assets to live in an address?

Native AIBRC assets are recorded as balances on accounts derived from Bitcoin address scripts. One supported address can hold multiple AIBRC assets.

For example, an account holding 100,000 tokens can send 25,000 by specifying the asset, amount and recipient. The protocol checks the designated authorization input and updates the sender's and receiver's balances. The remaining 75,000 stays in the original account.

This separates asset accounting from Bitcoin coin selection. The AIBRC balance belongs to the script account rather than to a specific satoshi or dedicated carrier UTXO. Ordinary BTC spending follows Bitcoin's transaction rules, while AIBRC balance changes follow valid asset instructions.

Wallets and Agents can therefore work with accounts, assets, amounts and recipients directly. Indexers read Bitcoin transactions, apply AIBRC rules and calculate the resulting balances. That indexing foundation gives applications a reusable account view while simplifying the asset-carrier management that users and Agents would otherwise perform. Source: AIBRC account model

6. What practical advantages does this account model provide?

It creates a balance-oriented experience. Hold 10,000 tokens, send 5,000, and the remaining 5,000 stays at the same account. Token accounting becomes separate from the Bitcoin inputs, change outputs and miner fees used to construct the transaction.

It also supports clear multi-recipient distributions. The current Transfer instruction can allocate one asset to 1–25 receiver outputs within the protocol's payload limits. Community distributions, group payments and contribution rewards can be prepared from a list of recipients and amounts.

An Agent can turn “send 2,000 to B and 3,000 to C” into a structured operation: check the account balance, calculate allocations and transaction costs, then prepare the wallet interaction. The same workflow can serve many assets and applications.

An account's AIBRC holdings also remain recorded when its BTC balance is zero. When a transfer is needed, the transaction supplies the inputs and outputs required for authorization, receiving and network fees. Asset ownership and transaction funding each have a clear role. Sources: AiBTC overview, AIBRC quickstart

7. How does one address connect AIBRC, BRC-20, Runes and EVM assets?

“One address” expresses a unified identity, account and interaction entry point. A project and community can organize AIBRC, BRC-20, Runes and EVM-related asset or application relationships around that shared experience.

The components connect through defined mechanisms. Native AIBRC balances belong to script accounts. Shared-root BRC-20 and Runes branches trace their origin to the same Bitcoin root transaction. R1 references public EVM calculation rules, while X1 records an external network and contract address.

Each protocol supplies its own asset state and operations. EVM contracts execute on their respective networks, and application integrations define any exchange, redemption or service relationship between assets.

AiBTC organizes these relationships into a common product foundation: asset discovery, account views, market access, rule information and interaction preparation. The supported native AIBRC account types are P2TR and single-key P2WPKH, identified by their actual scripts.

For users and Agents, the benefit is less repeated discovery and identity matching. For developers, it is a reusable interface for connecting assets while preserving their native rules. Sources: accounts and wallets, AIBRC account model, cross-protocol connections

3. One Fair Launch Across Multiple Protocols

8. How does one fair launch connect with shared-root issuance?

One fair launch organizes issuance, creator participation, public trading and graduation into a continuous process. Supply allocation, bonding-curve calculations and graduation conditions are defined in advance. The creator's optional first buy is a paid purchase calculated through the same curve mechanism.

Shared-root issuance gives that launch a common origin across protocols. The AIBRC root asset supports the platform's core trading and liquidity. BRC-20 and Runes branches establish related starting points in their own ecosystems, while covenant references connect rules and external applications.

A project can explain where its related assets came from and how they connect to one community. Wallets and Agents can follow that provenance through transaction relationships.

This makes launch infrastructure reusable across a project's lifecycle. The project begins with one recognizable origin and market process, then uses its asset relationships to connect applications and community activity. Source: creation and shared-root issuance

9. How does shared-root issuance establish a common origin?

AiBTC connects protocol issuance paths through one Bitcoin root transaction.

The AIBRC Deploy instruction is recorded in the root transaction. BRC-20 and Runes use commitment outputs in that transaction, followed by their respective reveal and issuance processes. These transaction relationships establish traceable common ancestry.

Each branch progresses under its own protocol rules and confirmation process. Applications can display those branches together as one project's asset family, while showing each branch's deployment identity and status.

This shared origin gives developers a concrete basis for asset discovery, community dashboards and related-asset views. Additional application rules can define how membership, distribution, exchange or redemption relationships work between the branches.

The provenance remains useful across interfaces: a wallet, market page or Agent can follow the same root and recognize the relationship using the corresponding protocol data. Sources: root deployment, cross-protocol interaction

10. How can shared-root assets help a project connect more applications?

A shared-root branch gives a project an identifiable presence in another protocol's ecosystem. That presence can connect the community to wallets, markets, games and other services built around that protocol.

Application designs can use these relationships for participation credentials, membership, distributions, rights mapping or redemption. A community can define the role of each branch, then implement the rules that connect its use to the AIBRC root asset and the wider project.

For Agents, common provenance makes related-asset discovery easier. An Agent can resolve the family, collect each branch's data and explain how a particular application uses it.

The advantage is continuity. A new application can build on an existing project identity, market and community. The asset family gives that integration a recognizable starting point, while the application's own rules define the resulting experience. Source: shared-root assets and ecosystem use

11. How does a fair launch move from creation to public trading?

The creator enters the asset name, ticker, description, image and project links, chooses Standard, R1 or X1 mode, and decides whether to set an optional first buy. Images and metadata receive IPFS references, while the deployment transaction records the asset's protocol origin.

The launch then progresses through root deployment and the corresponding protocol branches. Once opening conditions are met, public bonding-curve trading begins. Reaching the graduation threshold moves the same asset into its V2 liquidity stage.

The current AiBTC launch template uses a total supply of 1 billion tokens with 8 display decimals: 800 million for bonding-curve allocation and 200 million reserved for graduation liquidity. Graduation occurs when the current real BTC reserve reaches 0.1 BTC. AIBRC's underlying deployment model supports fixed-supply assets as a general protocol capability.

New launches currently have zero platform creation fee. Bitcoin network fees follow the creation quote, and the creator's optional first buy is a separate purchase.

The result is one connected process for presentation, provenance, initial trading and ongoing liquidity. Sources: creation, curve and graduation, AIBRC assets

12. What is the creator's first buy?

The creator's first buy is an optional purchase before the public market opens. It follows the bonding-curve quote and records creator participation through explicit purchase, fee and accounting rules.

The current range is 2,000–10,000,000 sats, up to 0.1 BTC. Setting the amount to zero skips the option. After the launch reaches its first-buy stage, the creator confirms the purchase manually; execution deducts BTC and credits the purchased AIBRC.

The first buy follows the pre-graduation base trading fee of 0.5%. Its net principal contributes to the real BTC reserve and therefore to graduation progress.

Public trading opens when the launch satisfies its opening conditions. At that point, the creator and other participants trade under the market's applicable rules.

This makes the creator's early participation part of the same market process that carries the asset into public trading and graduation. Source: creator first buy

13. What do the bonding curve and graduation each accomplish?

The bonding curve gives a new asset a defined process for developing its initial market. Virtual reserves establish the opening pricing model, while actual buys and sells change the real BTC reserve.

Graduation progress follows that current real reserve. Buy principal increases it, sell settlement reduces it, and trading fees follow their separate accounting paths.

At 0.1 BTC in real reserve, graduation connects the asset to the V2 liquidity stage. Actual BTC and the remaining AIBRC form the pool reserves, and LP shares are initialized. Existing holdings continue to represent the same asset throughout the transition.

During the curve stage, users buy and sell through their platform accounts. After graduation, V2 trading, Block Swap, liquidity participation and AIBRC protocol withdrawals become available under their respective conditions.

This creates a continuous market lifecycle: an asset starts with an accessible issuance mechanism, builds real reserves through participation, then moves into a liquidity pool that supports ongoing trading. Source: bonding curve and graduation

4. Programmable Bitcoin Assets and Smart Covenant

14. How does AiBTC help AI understand Bitcoin and make its assets programmable?

An Agent needs a clear description of an asset: its identity, account balance, rules and the effect of an operation. AIBRC organizes those questions into consistent asset identifiers, address-based accounts, amount units and authorization rules.

That lets an Agent begin with an address and understand its native AIBRC holdings directly. It can prepare actions around assets, amounts and recipients, leaving Bitcoin transaction construction to the corresponding tooling.

Smart Covenant adds a computable rule identity. An asset can reference a rule version and parameters; CORE applies the relevant rules to trading, fee distribution and block buybacks; public records provide inputs for result checks.

This is the programming model behind the product's “every Bitcoin asset” ambition: shared asset interfaces combined with explicit application rules. Native AIBRC accounts and R1 provide concrete foundations, protocol-specific adapters connect other asset standards, and X1 identifies related EVM applications.

Developers can reuse account and rule tooling. Agents can translate intent into structured actions. Projects can organize services and community interactions around assets people already recognize. Sources: AIBRC Smart Covenant, AiBTC rules and execution

15. What is Smart Covenant, and why do assets benefit from a rule layer?

Smart Covenant connects an asset's identity with rules that applications can read and calculate.

An asset's name, supply and holders describe what it is. Rules describe how it participates in applications: how fees are calculated, how proceeds are distributed, what triggers a buyback and how results can be checked.

Bitcoin records the asset and its selected rule identity. A public reference expresses the calculations. The application executes the corresponding operations and records the outcome.

For creators, this gives economic activity a defined distribution mechanism. For developers, it provides reusable calculations. For Agents, it turns asset behavior into explicit inputs, conditions and results.

R1 supplies a fixed template for fees, fee destinations and buyback plans. Application designers can apply the same approach to community budgets, contribution distributions, service payments, governance or liquidity mechanisms through their corresponding templates and implementations. An asset retains the rule version selected at creation. Sources: Smart Covenant and liquidity, AIBRC Smart Covenant

16. What rules does R1 provide?

R1 is the first fixed Smart Covenant template. It publishes calculations for trading fees, rule-fee distribution and buyback plans.

At creation, an asset selects its R1 version, reference address, extra rule-fee rate and destination. These parameters connect to the root deployment and provide the basis for execution and recomputation.

In the current AiBTC product, the extra R1 fee applies after graduation. Its range is 0–5% in 0.1% increments, with the selected destination directing it to creator earnings or system block buybacks. The 0.5% base trading fee is calculated separately. The curve trade that reaches graduation uses its pre-graduation starting state for fee calculation.

The result is an asset with a readable economic rule identity. A user can understand its selected fee mechanism, while an Agent can calculate the applicable amounts from the same inputs used by an application. Sources: R1 product rules, R1 calculations

17. Why use EVM contracts to express rules for Bitcoin assets?

Bitcoin provides the asset record, transaction ordering and settlement foundation. The EVM ecosystem provides mature contract languages, ABIs, RPC interfaces and developer tools. Smart Covenant connects those strengths.

For R1, the public EVM contract serves as a read-only calculation reference. CORE reads the asset's bound version and parameters, performs the same calculations locally and updates the relevant account and market state.

Each fill therefore reuses the public standard without requiring a separate EVM transaction. Developers, wallets and Agents can implement and compare the same formulas using familiar tools.

This gives EVM expertise a direct role in Bitcoin applications. A public calculation standard can serve many Bitcoin assets, each with its own selected parameters, while adapters connect additional services through precise references.

“EVM as Bitcoin's extension layer” describes this combination: mature rule-expression and application tooling working around Bitcoin asset identities and their associated execution paths. Source: EVM as rule infrastructure

18. How does R1 connect trading, creator earnings and block buybacks?

An eligible trade produces swap principal, a base trading fee and the asset's selected R1 rule fee. Each follows its own accounting path, linking market activity with liquidity and the asset's chosen distribution mechanism.

For a 100,000-sat buy of an already-graduated asset with a 2% R1 fee, 500 sats goes to the base trading fee, 2,000 sats to the R1 fee and 97,500 sats becomes swap principal. A Block Swap also includes its Bitcoin network fee and transaction-output requirements.

With creator earnings selected, the rule fee accrues in the creator earnings account and can be claimed to the platform BTC account.

With block buybacks selected, the rule fee accrues in the buyback account. At new Bitcoin block heights, CORE checks the balance and execution conditions. The current balance threshold is 1,000 sats. An eligible buyback purchases AIBRC from the market and places it in a one-way system lock account.

Locked balances accumulate while total supply stays constant. Public parameters connect each step: trading activity, fee allocation, buyback execution and asset locking. Sources: rule execution and distribution, CORE block buybacks

19. What is X1, and how does it connect external applications?

X1 records an external application's EVM chain ID and contract address. Together, they provide a precise coordinate that wallets, developers and Agents can follow.

With the relevant ABI and RPC tools, an application can read the contract's exposed interfaces, rules and state, then build a service view or prepare an interaction around that relationship.

For example, a community can associate its Bitcoin asset with a game's membership contract. A wallet can show the service entry, an Agent can explain membership terms, and an adapter can prepare the relevant action. Stablecoin payments and stock-related asset services can use similar application relationships with their own asset interfaces, settlement and product terms.

R1 provides a fixed calculation template; X1 provides an external application reference. The referenced contract runs on its own network, while the adapter defines how users encounter and interact with that service through the shared asset experience. Sources: X1 application connections, external application relationships

5. One Liquidity Pool, Two Swaps

20. What is AIBTC CORE, and how does it connect the system?

AIBTC CORE is AiBTC's application execution and accounting layer. It uses AIBRC asset identities, address accounts and bound rules to execute trading, fee distribution and block buybacks, recording the resulting account and market changes.

Three components work together. Bitcoin records asset deployment, rule identity and parameters, along with relevant on-chain transactions. Public EVM reference contracts express R1 fee, distribution and buyback-plan calculations. CORE applies those calculations locally and completes the application operations. It also handles bonding-curve and V2 AMM trading under their respective market rules.

This division supports continuous interaction. Account trades use CORE for quotes, balances and distributions. On-chain operations progress through Bitcoin confirmation and the applicable asset-protocol checks.

Determinism gives the system a consistent calculation model: the same rule version, starting state and event order produce the same result. Bitcoin consensus validates and orders Bitcoin transactions; CORE computes and records application state. Public rules and execution data connect those layers for recomputation. Sources: AIBTC CORE, Smart Covenant execution

21. What does deterministic execution offer users and Agents?

It gives each operation a structured, repeatable workflow: read state, generate a preview, obtain authorization, execute the account changes and record the result.

The preview explains amounts, fees and the expected outcome. Execution applies the current balance, market stage, rules and selected trade conditions, then processes debit, exchange, credit, fee distribution and accounting together.

Each request has an identifier. Repeated use of the same identifier refers to the same operation and result, giving applications a consistent way to submit and track work.

For an Agent, this creates clear stages to automate around: gather inputs, calculate the preview, prepare the user's action, follow the original order and inspect the execution record. For a user, it keeps the operation understandable from intent through completion.

The recorded state changes also provide material for later replay with the same rules, making the interaction useful both to execute and to explain. Sources: CORE execution flow, trading integration

22. Why offer both 0-gas Instant Swap and Bitcoin Block Swap?

Users may want continuous account trading for one action and direct delivery to an external wallet for another. AiBTC connects both experiences to the same market.

0-gas Instant Swap uses available AiBTC account balances. CORE executes buys and sells and updates the account immediately through the application flow. Each fill avoids a separate Bitcoin transaction and its network fee. Market trading fees and applicable R1 fees follow the asset's rules.

Bitcoin Block Swap supports BTC-to-AIBRC purchases in graduated markets directly from an external wallet. The user's wallet and protocol vault sign their respective transaction inputs, combining the BTC payment and AIBRC transfer instruction in one Bitcoin transaction. The purchased AIBRC is delivered to the linked external wallet.

Instant makes repeated interaction convenient; Block Swap makes direct wallet participation convenient. AIBRC held externally can enter the platform's deposit flow for subsequent Instant selling. Both routes draw on the same market and liquidity foundation. Source: AIBTC Swap

23. How does PSBT co-signing combine payment and asset delivery in Block Swap?

Block Swap uses BTC directly from the user's external wallet, bringing payment and the AIBRC transfer instruction into the same Bitcoin transaction. This removes the intermediate deposit, account purchase and asset-withdrawal sequence for that exchange.

After the amount, quote, receiving address and fees are established, the transaction is constructed in PSBT format. The user's wallet signs its BTC inputs, and the protocol vault signs the asset-authorization inputs it controls. Co-signing means each participant signs its own inputs in the shared transaction.

The signer rebuilds each transaction according to the order record and execution rules, checking inputs, receiving addresses, amounts, fees and change. After confirming the user's signature, it completes the protocol vault's signature and broadcasts the transaction. The user keeps the wallet private key, while an isolated signer handles protocol-vault signing.

This PSBT co-signing mechanism covers AIBRC protocol withdrawals and Block Swap. BTC withdrawals use their own separate flow.

For Block Swap, asset delivery is recognized at one confirmation after AIBRC validation. At two confirmations, the corresponding funds and fees enter the AMM's confirmed accounting. Instant uses account balances for immediate trading, and both routes share the market's liquidity. Source: Block Swap signing and settlement

24. How does one liquidity pool power both Swaps?

One AIBRC market's pool supplies the liquidity for Instant and Block Swap. Trading demand connects to the same depth, so the project builds one market across both account-based and wallet-based participation.

The two routes share a reserve and pricing foundation while operating at different speeds. Instant executes through the account state machine; Block Swap progresses with Bitcoin confirmations.

Pending-aware pricing connects those rhythms. AiBTC tracks confirmed reserves alongside the effects of eligible pending swaps, then calculates effective reserves for subsequent quotes. The pending swap's net BTC effect and corresponding AIBRC quantity are reflected in that calculation.

When the swap reaches formal pool-entry conditions, its effect moves from pending accounting into confirmed reserves. Later quotes therefore incorporate the market changes already accepted into the relevant pending state.

The result is a continuous market experience: both routes use the same liquidity base, and each quote reflects the effective reserves and conditions at that point in the market. Source: pending-aware pricing

25. What role does liquidity play in the platform?

Liquidity connects initial issuance with a continuing market. At graduation, actual BTC and remaining AIBRC establish V2 reserves and initial LP shares. Additional liquidity participation supports ongoing trading depth.

In the graduated market, base trading fees follow the LP fee path and are distributed by effective share. User-held and protocol-held shares participate according to the same applicable rules. The R1 rule fee follows its selected creator-earnings or buyback path.

A trade therefore connects several roles: the trader receives the exchange result, liquidity providers contribute depth and participate in fee distribution, and the creator or rule account receives the asset's selected allocation.

This is why AiBTC organizes launch, bonding curve, graduation and liquidity as one product journey. The initial market leads into a structure that supports continued participation and connects trading activity to the asset's economic rules. Source: Smart Covenant and liquidity

6. Agents, Public Interfaces and Recomputable Results

26. Why are Explorer and public proofs part of the product?

An Agent that understands asset rules also benefits from structured execution results. AiBTC Explorer brings human-readable information together with raw records, batch information and proof material that tools can calculate against.

The public verification method covers record fingerprints, Merkle inclusion, batch fingerprints and the relationship between OTS commitments and Bitcoin time anchors. Matching trade and pool-reserve records can also be recomputed under the method's applicable formulas.

Copy proof packages the material for a specific record. A user can pass that package to an Agent or local tool and obtain the results of the checks actually performed.

This turns market history into something people can understand through calculations. Developers gain common inputs for verification tools; users gain a practical way to ask their own Agent to explain the relationship between an operation, its recorded outcome and the rules used to calculate it. Sources: Explorer and Agents, verification documentation

27. What can an Agent do with the public AiBTC MCP?

The public MCP provides four read-only market tools: find_market, list_markets, get_market and get_recent_trades.

An Agent can find an asset by name, ticker or official market link, read its price, market capitalization, reserves and market phase, and organize recent trading activity into an explanation or watchlist. When a query has several matches, it can present the candidates and continue with the selected market.

The hosted connection is https://aibtc.bot/api/v1/public/mcp. The npm package @aibtcbot/mcp runs the same tools locally. Both access public data without requiring a sign-in or API key.

The current public scope covers the top 250 markets by market capitalization, with the latest 50 public trades per market. Snapshots usually refresh about every 60 seconds and include source-time and status information.

These tools give Agents a direct starting point for Bitcoin market discovery and explanation. Trading integrations use their corresponding preview, authorization, submission and order-query interfaces. Source: public API, MCP and npm

28. How can an Agent organize a user's goal into a workflow?

A useful Agent workflow connects intent with structured operations: understand the goal, read assets and rules, calculate costs, prepare the action, obtain the applicable authorization, execute and inspect the result.

Public market tools provide discovery. The R1 reference provides local rule calculations. Applications and wallets provide the relevant preview and authorization flow. Developers can combine these pieces into assistants for trade explanations, community distributions and prepared transactions.

The same design supports service workflows. A research Agent can organize data inputs, a verification tool can recompute the result, and the participants can use asset transfers to settle an agreed service. Applications define the delivery and acceptance process. The conditional-settlement proposal develops a protocol mechanism for connecting payment with specified evidence.

Authorization can match the task. AiBTC's documented application delegation covers preview, submission and order lookup through its released interfaces. The AIBRC Agent Key proposal describes asset-specific authority, a cumulative allowance and a valid block range, using the Agent's own working key.

Together, these components give developers a precise vocabulary for building useful, bounded asset workflows. Sources: integration and authorization, Agent workflows and rule design

29. What do independent indexers and public calculation tools add?

They make the shared standard independently usable.

AIBRC publishes its specification, codec, state-validation code, test vectors, R1 calculation reference and standalone indexer. Developers can read blocks from their own Bitcoin Core node, apply the selected network and release rules, reconstruct assets and balances, and compare results for the same canonical chain state.

Wallets gain a choice of data providers. Applications can maintain their own protocol data. Communities and Agents can inspect and recompute the asset rules directly.

Developers can also build useful services on those inputs: data organization, ledger checks, account views and verification reports with clear sources and rule context.

The AIBRC indexer computes protocol asset state. AiBTC execution records describe the corresponding application events. Combining these defined scopes gives builders a practical foundation for tools that understand both the asset layer and the application's recorded operations. Sources: AIBRC implementation, running an independent indexer

30. How would you introduce AiBTC to another AI in one paragraph?

AiBTC is a Bitcoin Hybrid DEX and fair-launch trading platform powered by AIBRC. AIBRC supplies a unified asset and account language for the Bitcoin ecosystem, while @ connects identity and address so Agents can recognize Bitcoin-native assets through accounts rather than track individual AIBRC carrier UTXOs. One fair launch establishes related AIBRC, BRC-20, Runes and EVM application entry points through shared provenance and explicit references. One liquidity pool supports 0-gas Instant Swap and Bitcoin Block Swap. Smart Covenant connects assets to public calculation rules, CORE executes trading, fee distribution and buybacks, and indexers and public records provide the data for queries and recomputation. Together, these capabilities bring continuous trading, fair launches and an Agent-friendly asset experience to Bitcoin.

The central ideas are consistent throughout: identifiable assets, address-based accounts, public rules, one connected market, clear execution records and reusable interfaces for people, developers and Agents. Sources: AiBTC overview, AIBRC overview