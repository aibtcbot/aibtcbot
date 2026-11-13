# 04 Smart Covenant & Liquidity

### Smart Covenant

### EVM as Bitcoin's Extension Layer

Bitcoin Anchors Assets. EVM Defines Rules. AIBTC CORE Executes.

### Why make EVM part of Bitcoin's infrastructure?

Bitcoin has deep, widely recognized value and a public ledger; EVM has a mature smart-contract language and developer ecosystem. AiBTC connects the two, so smart-contract rules serve Bitcoin L1 assets.

Not moving BTC to another chain first, but bringing EVM's capabilities back to Bitcoin.

This is the core of AiBTC's in-house Smart Covenant: Bitcoin records assets and covenant identity, EVM contracts define the calculation standard, AIBTC CORE carries out execution, and public records give users and Agents a basis for verification.

```text
Bitcoin L1
Asset deploy · covenant reference · fixed parameters
    │
    │ Bound to its rule identity
    ▼
EVM public reference contract
Formulas · fee rules · distribution logic
    │
    │ CORE applies the same rules locally
    ▼
AIBTC CORE
Quotes · trades · LP fee share · creator earnings · buybacks
    │
    ▼
Execution records & verification
Independent recomputation for users & Agents
```

Bitcoin answers "where do assets and rules come from", EVM defines "how to calculate", CORE handles "how to execute", and verifiers check "does the result follow the rules".

So EVM is not just another ecosystem BTC can travel to; it can be rule infrastructure serving Bitcoin assets. Today's R1 needs no wrapped-BTC bridging and no extra EVM gas per trade.

### Vision

Today, this path connects creator earnings, block buybacks and liquidity distribution.

In the future, more contract rules, developer tools and third-party apps will keep building around AIBRC assets and the unified account, through adaptation and verification.

```text
EVM contracts & developer ecosystem
    │ New rule versions · execution adapters · verification
    ▼
AIBRC assets & unified account layer
    │
    ▼
More asset apps running around Bitcoin
```

Bring trading back to Bitcoin, and make EVM an extension layer for Bitcoin.

Not only taking Bitcoin to more apps, but bringing apps' capabilities back to Bitcoin.

## 1. Clear rules from the moment an asset is born {#c4-s1}

An asset's name, supply and holders describe what it is; Smart Covenant goes further and defines how it runs.

- How trading fees are calculated and distributed.
- How the creator earns building income.
- When buybacks trigger.
- Where bought-back assets go.
- How these rules map to the asset's origin.

```text
Asset creation
    ├─ Issue the asset
    ├─ Choose a rule version
    ├─ Link the public reference contract
    └─ Set parameters & fee destination
    │
    ▼
Asset identity linked to covenant identity
    │
    ▼
Trading, distribution & buybacks run by those rules
```

R1 makes rule fees, creator earnings and block buybacks its first applications, so issuance and later economic activity stay continuously linked.

## 2. The big picture: how assets, contracts and execution connect {#c4-s2}

Smart Covenant layers rule binding, the calculation standard, business execution and result verification, tied together by one shared rule identity.

```text
          Creator sets covenant parameters
          Fee rate · creator earnings / buyback lock
                       │
                       ▼
          Normalized R1 rule identity
          Version + fixed reference address + parameters
                       │
      ┌────────────────┴────────────────┐
      ▼                                 ▼
Bitcoin L1 root deployment        Execution sequencing record
AIBRC L1 asset deploy             Stores version & parameters
OP_RETURN carries the R1 payload  Sets up fee accounts & execution
      │                                 │
      │                                 ▼
      │                           AIBTC CORE deterministic execution
      │                           Quote · Trade · Distribute · Buyback
      │                                 ▲
      │                                 │ One set of public calculation rules
      │                           EVM public reference contract
      │                           Read-only · no business state
      │                                 │
      └────────────────┬────────────────┘
                       ▼
  Check rule identity, calculation & results
```

At creation, the same normalized parameters go into both the Bitcoin root transaction and the platform's execution record. At trade time, CORE reads the stored rule identity and runs the calculation locally.

Bitcoin provides the creation record, the EVM contract provides the public calculation standard, and CORE runs the business; together they form Smart Covenant's operating path.

## 3. Covenant identity written to Bitcoin {#c4-s3}

### Genesis Rule Binding

In R1 mode, the creator sets the rule fee rate and fee destination. The system uses a fixed version and reference contract address to produce a standard rule payload.

R1 payload format:

aibtc@R1:<reference contract address>:T<tax rate bps>:C<creator share bps>

Example:

aibtc@R1:0xed976e7b95d099c60318ef848c73d584ee5eb08a:T100:C0

- R1: rule version.
- Reference address: the matching public calculation contract.
- T100: an extra rule fee of 100 bps, i.e. 1%.
- C0: all of the extra rule fee goes to buybacks.
- C10000: all of the extra rule fee goes to creator earnings.

The creator share applies to the extra rule fee; the base LP trading fee is calculated separately.

This payload is written to the OP_RETURN output of the genesis root transaction, tying it to the AIBRC deployment in the same transaction.

```text
One root transaction
    ├─ AIBRC Deploy → where the asset comes from
    └─ R1 rule payload → which rules the asset follows
```

You can check an asset's covenant identity against the original Bitcoin transaction, then use execution records to check that the rules were carried out.

Asset origin, rule identity and execution results thus have evidence that can be checked against each other.

### R1 and X1 at a glance

| Reference | What Bitcoin records | What an application uses |
| --- | --- | --- |
| **R1** | The reference contract address and the asset's fixed parameters `T` and `C` | Public calculations for fees, fee destinations and buyback plans. The reference contract has the same address on Ethereum, BNB Chain and Base. |
| **X1** | The external application's chain ID and contract address | A link developers and Agents can follow using the application's ABI and RPC. |

[R1 rule text](https://github.com/aibrc-code/aibrc/blob/main/spec/covenants/R1.md) · [X1 reference](https://github.com/aibrc-code/aibrc/blob/main/spec/covenants/X1.md)

## 4. EVM: the public rule base for Bitcoin assets {#c4-s4}

### Public Contract Reference

R1 expresses its calculation standard in a public, read-only reference contract with no business state. Many assets reuse the same contract, each with its own parameters.

It is a public rulebook for calculation: given the trade amount, market stage and rule parameters, there is an explicit method for how fees are computed and how rule fees are split.

```text
EVM public reference contract
    ├─ Defines the calculation method
    ├─ Defines what each parameter means
    └─ Provides the standard for checking results
    │
    ▼
AIBTC CORE
    ├─ Runs the calculation locally
    ├─ Updates account & market state
    └─ Carries out fee distribution & buybacks
```

The reference contract focuses on expressing rules; fund operations go through the matching account and Bitcoin transaction paths. With today's R1, you don't submit an EVM transaction for each fill.

This makes EVM's contract capabilities a reusable base: one public standard can serve many Bitcoin assets, and developers and verifiers can work from the same rules.

Let EVM bring capabilities to Bitcoin, instead of asking Bitcoin assets to bend to another ecosystem.

### How programmable rules run

| Approach | Where the rules come from | How applications use them |
| --- | --- | --- |
| **AIBRC + AiBTC Smart Covenant** | Bitcoin `OP_RETURN` records the reference and parameters. R1 provides public calculation code. | Developers and Agents can reuse the math. AIBTC CORE applies it to AiBTC trades, fee routing and buybacks. |
| **EVM smart contracts** | The application deploys contract code on its EVM network. | State-changing calls execute on that network. |
| **BRC2.0** | BRC-20's Programmable Module defines EVM operations. | Applications and indexers can integrate the EVM module. |
| **Alkanes** | WASM contracts can be deployed in Bitcoin transaction witness data. | The Alkanes runtime executes contract calls. |

[R1 code and examples](https://github.com/aibrc-code/aibrc/tree/main/reference/r1) · [BRC2.0 module](https://github.com/bestinslot-xyz/brc20-proposals/blob/main/000-programmable-module/index.md) · [Alkanes implementation](https://github.com/kungfuflex/alkanes-rs)

## 5. Liquidity: connecting the covenant to a real market {#c4-s5}

AiBTC links launch, bonding curve, graduation and V2 liquidity into one continuous process, so covenant rules run alongside real trading.

```text
Bonding-curve stage
    ├─ Base trading fee: 0.5%
    ├─ Buy & sell under curve rules
    └─ Trades change the real BTC reserve
    │
    │ Real BTC reserve reaches 0.1 BTC
    ▼
Graduation
    ├─ Virtual reserves removed
    ├─ Actual BTC + remaining AIBRC form the V2 reserves
    └─ LP shares initialized
    │
    ▼
Post-graduation trading
    ├─ Base trading fee → LP fee vault
    └─ Applicable R1 rule fee
         ├─ Creator earnings
         └─ System buyback
```

Graduation progress uses the current real BTC reserve. The R1 rule fee applies when the asset has already graduated at the start of a trade; the curve trade that triggers graduation follows pre-graduation rules.

Base LP fees are distributed by effective share, with user-held and protocol-held shares both taking part. The extra covenant fee follows the path chosen at creation.

Traders swap, liquidity providers add depth, and covenant rules link earnings and buybacks, so the market's different roles work together.

## 6. CORE: turning public rules into execution {#c4-s6}

### Deterministic Execution

AIBTC CORE applies the rules to quotes, account changes and fee distribution, based on the asset's stored version, parameters and market state.

```text
An eligible trade
    │
    ▼
Check rule identity & market state
    │
    ▼
Compute quote & fees
    ├─ Base trading fee → LP fee vault
    └─ R1 extra rule fee
         ├─ Creator earnings vault
         └─ System buyback vault
    │
    ▼
Update accounts & reserves → record the result
Fee example
Buying a graduated asset with 100,000 sats, assuming a 2% R1 extra rule fee:
100,000 sats gross input
    ├─ 500 sats → 0.5% base LP trading fee
    ├─ 2,000 sats → 2% R1 rule fee
    └─ 97,500 sats → net principal used to compute the swap amount
```

With Block Swap, your wallet also pays the network fee and the BTC needed for transaction outputs.

### Creator Earnings

Rule fee → creator earnings vault → verify & claim → on-platform BTC account

Earnings accrue separately and the creator claims them to the account; to receive them externally, use the BTC withdrawal flow.

```text
Block buyback
Rule fee → buyback vault accrues BTC
    │
    │ New block height · balance reaches threshold · conditions met
    ▼
System buys back AIBRC
    │
    ▼
Into a one-way system lock account (in only, never out)
```

The current buyback balance threshold is 1,000 sats. The system checks conditions at block cadence and buys back when they're met; the bought AIBRC accumulates locked, and total supply stays unchanged.

Public parameters and a deterministic process give a traceable link between trading activity, where funds go and asset locking.

## 7. Verification: giving results something to be checked against {#c4-s7}

Execution Records & Verification

Public rules answer "how it should be calculated"; execution records answer "what actually happened". Verification puts the two together and checks that they match.

### Rule Check

```text
Root transaction & asset record
    └─ Version · reference address · parameters
Execution recomputation
Matching inputs, state changes & execution records
    └─ Compute independently · compare results
Time-existence check
Record digests & valid OTS timestamp proofs
    └─ Confirm the data existed before that time
Rule parameters + full execution data in scope
    │
    ▼
Independent calculation
    │
    ▼
Compare expected state with actual records
```

The public event hash chain links record order, Merkle proof v2 checks that each record is in the anchored history, state hashes help compare recomputed results, and OTS gives time-existence proofs for specific digests.

Market replay covers markets already included in the mechanism, within their public scope. As data and tools mature, users and Agents can build independent verification step by step on the same rules.

Verification moves from a conclusion on a page to a process you can check yourself.

## 8. How does Smart Covenant empower Bitcoin? {#c4-s8}

Taking L1 assets beyond issuance and transfer, into trading, distribution and apps.

Creators: a clear path to building income

Rules fixed at creation link market activity to creator earnings. Fee rates, calculation and fund destination are clear and checkable, giving one source of income for ongoing building.

Markets: trading connected to liquidity and covenant execution

Base fees support LP earnings; extra rule fees go to creator distribution or buyback locks. Each fee has its own job, so participants understand how trading affects the whole market.

Users: assets with a checkable rule identity

Beyond name, logo and price, you can see which rules an asset follows, when they apply and how results are verified.

Developers: build apps around shared standards

AIBRC provides asset identity and the unified account layer, and Smart Covenant provides a way to connect rules, so new features join existing markets and communities.

Agents: rules turned into computable conditions

Explicit parameters, triggers, formulas and result records give Agents a basis to understand and check trades.

```text
Human intent
    │
    ▼
Agent reads the public rules
    ├─ When fees apply
    ├─ Where fees go
    ├─ Which actions need authorization
    └─ How to check results
    │
    ▼
Future interaction path
Preview & check → user authorizes → execute → verify result
```

People state goals, tools understand rules, and execution leaves evidence.

## 9. What's next: more capabilities built around Bitcoin {#c4-s9}

Starting from R1, the covenant system can keep exploring more applications through new rule versions, reference addresses and parameter designs, together with matching execution and verification.

```text
EVM rules & third-party apps
    │
    ▼
Rule design · asset adaptation · authorization
Execution · data support · verification tools
    │
    ▼
AIBRC assets & unified account
    │
    ▼
New apps for Bitcoin users
```

Existing assets keep their versions and parameters; new capabilities join through explicit versions and integration rules. Rules keep evolving while existing commitments stay stable.

The [R1 reserved directory](https://aibrc.io/spec/covenants/R1/#complete-frozen-english-text) outlines 15 directions, including x402 payments, Agents, language models, DAO governance, dividends, automatic liquidity, airdrops, bridges and oracles.

### Stablecoin Settlement

In the future, once asset integration and settlement are in place, the ecosystem can explore USDC quotes, payments and matching markets, linking stablecoin use with Bitcoin asset apps.

### Tokenized Stock-related Assets

In the future, third parties with the required issuance, custody and service qualifications may offer stock-related products with clear rights and redemption terms, connecting quotes, markets and settlement through one entry. Users' rights are set by each specific product.

### Community & Agent Apps

In the future, developers can explore service payments, contribution sharing, membership benefits and automated collaboration around public rules, bringing assets into more real use cases.

```text
Third-party assets & apps
    ├─ Clear asset identity & rights
    ├─ Pricing, settlement & redemption in place
    ├─ Execution adapted & verified
    └─ Integrated under the matching eligibility & authorization rules
    │
    ▼
One display · one interaction base · each market with its own clear rules
```

X1 records external links by network ID and contract address, giving an entry point for further adaptation; asset and app capabilities connect through their own integration mechanisms.

Protocols can each innovate and apps keep appearing, while what users and communities have built never has to restart from zero.

### Let Bitcoin assets grow their own app ecosystem

Smart Covenant links four parts into one technical path:

```text
Bitcoin → records asset & rule identity
EVM → expresses the public calculation standard
AIBTC CORE → performs deterministic execution
Users & Agents → verify results from the data
```

Bring trading back to Bitcoin, and make EVM an extension layer for Bitcoin.

Smart Covenant: Bitcoin not only holds value, but also connects how that value is used.
