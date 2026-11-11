# 03 AIBTC Swap

Hybrid DEX Engine

### AIBTC Swap, two tracks · Instant execution & on-chain swaps

Dual-track Swap · Instant & Block Swap

Instant trades don't wait for a block each time; Block Swap settles the BTC payment and the AIBRC delivery in one Bitcoin transaction.

AiBTC connects in-account instant execution and wallet-based on-chain swaps to the same AIBRC market. You can trade continuously from your account balance, or pay with BTC from an external wallet and receive the swapped asset at your own on-chain address.

Instant and Block Swap serve different needs. They share the market and its pricing base, but differ in source of funds, authorization, where the asset lands and how confirmation works. Pending-aware pricing, layered confirmation and dynamic limits let the two routes work together at their different speeds.

```text
                 AIBRC market
                       │
      ┌────────────────┴────────────────┐
      ▼                                 ▼
 Instant                           Block Swap
      │                                 │
 aibtc account balance             BTC from an external wallet
 Account trading authorization     Handshake · PSBT co-signing
 Buy / Sell                        BTC → AIBRC
      │                                 │
 Executed by AIBTC CORE            One Bitcoin transaction
 Account balances updated          BTC payment + AIBRC delivery
      │                                 │
 No per-trade block wait           Delivered at 1 confirmation
                                   Pooled at 2 confirmations
      │                                 │
      └────────────────┬────────────────┘
                       ▼
         Same market · shared pricing
        Continuous trading & liquidity
```

AIBTC's dual-track Swap is more than two buttons: it fully connects the speed of account trading, wallet authorization and on-chain delivery on Bitcoin.

## 3.1 Choose Your Route {#c3-s1}

### Instant · Buy & sell inside your account

For users who already hold BTC or AIBRC on AiBTC and want to trade continuously or rebalance.

- Funds: available balance in your AiBTC account
- Direction: buy and sell
- Result: BTC and AIBRC balances in your account are updated
- Execution: by AIBTC CORE, with no block wait per trade
- Network fee: no Bitcoin network fee per instant fill

### Block Swap · Your wallet takes part directly

For users who want to pay with BTC from an external wallet and keep the AIBRC they receive in their linked wallet.

- Funds: BTC in your external wallet
- Direction now: BTC → AIBRC
- Available for: graduated AIBRC markets
- Authorization: wallet handshake, PSBT construction and co-signing by both sides
- Asset goes to: your linked external wallet
- Network fee: your wallet pays the network fee for that Bitcoin transaction

During the bonding-curve stage, trade with Instant under curve rules; un-graduated AIBRC can't be withdrawn. After graduation the market moves to the V2 liquidity pool, and Block Swap and protocol withdrawal open.

Block Swap does not yet support the reverse AIBRC → BTC route. To sell AIBRC from your wallet with Instant, first deposit it into your account through the AIBRC deposit flow.

## 3.2 Instant Trading & Deterministic Execution {#c3-s2}

With Instant, AIBTC CORE handles quoting, execution and account updates. You don't build, sign and broadcast a Bitcoin transaction for every trade, so you can keep trading from one account.

### Buy

Choose an asset, enter the BTC to spend, check the estimated amount, trading fee and price protection, then confirm and submit.

```text
Available BTC
    │ Get quote · check fees & minimum received
    ▼
Submit trade
    │ AIBTC CORE verifies & executes
    ▼
BTC deducted → AIBRC credited to your account
```

### Sell

Enter the AIBRC amount to sell, check the estimated BTC, fees and price protection, then confirm and submit.

```text
Available AIBRC
    │ Get quote · check fees & minimum received
    ▼
Submit trade
    │ AIBTC CORE verifies & executes
    ▼
AIBRC deducted → net BTC credited to your account
```

### Minimum Trade Size

- Standard buy: at least 1,000 sats in total (0.00001 BTC)
- Standard sell: BTC output before fees of at least 1,000 sats
- Minimum sell amount: varies with the current quote, not a fixed token count
- Creator first buy: separate rule, minimum 2,000 sats

Execution in Seconds

Instant separates trade execution from Bitcoin confirmation, giving trading in seconds without waiting for a block on each trade.

"Instant" here means execution of account trades, not instant confirmation on Bitcoin mainnet. Actual response depends on the network, service load and order state; the order result and balance update are what count.

Deterministic Execution

Quotes and fills are computed from explicit reserves, fee rates and your constraints, with amounts handled as integers in each asset's smallest unit. After you submit, the system re-checks balance, market stage, trading authorization and price protection, and applies the account changes once all are met.

```text
In-account trades
    └─ Quote & authorization → execution checks → balances updated
On-chain deposits, withdrawals & Block Swap
    └─ Bitcoin transaction → block confirmation → protocol checks & delivery
```

Execution and on-chain confirmation each do their own job, so frequent trading doesn't pay the repeated wait and network cost of going on-chain every time.

## 3.3 Wallet Handshake & Single-transaction Atomic Swap · Block Swap {#c3-s3}

In a step-by-step flow, buying with BTC from an external wallet and taking the asset back to that wallet usually means:

Deposit BTC → wait for confirmation → buy on the platform → request withdrawal → wait for confirmation again

Block Swap combines the BTC payment and the AIBRC transfer instruction in one Bitcoin mainnet transaction — no deposit, buy and withdrawal in turn. Once the transaction confirms and passes protocol checks, the asset is delivered straight to your linked wallet.

```text
Your external wallet                    Protocol execution node
    │                                       │
BTC payment & network-fee inputs        Inventory & protocol authorization inputs
    │                                       │
Wallet handshake · check the quote      Checks rules, limits & price protection
Sign the PSBT locally                   Co-signs
    │                                       │
    └───────────────────┬───────────────────┘
                        ▼
           One Bitcoin L1 transaction
             ├─ User BTC & node authorization inputs
             ├─ BTC payment & fee outputs
             ├─ AIBRC Transfer protocol instruction
             └─ Linked-wallet receive output · address-level delivery
                        │
                        ▼
         Broadcast · await confirmation
```

### Core Mechanisms

### Handshake

The system quotes from the current effective reserves and checks the swap amount, estimated tokens, receive address and fee breakdown. Once the request is admitted, it locks the matching Atomic Swap Unit and asset inventory, so signing and execution proceed on consistent terms.

### PSBT · Partially Signed Bitcoin Transaction

The transaction is built together using the standard PSBT format. You check the payment, fees and receive details in your wallet's transaction preview and sign locally; your private key never goes to the platform.

### Co-signing

Your wallet signs the BTC inputs you provide; after its checks pass, the protocol execution node automatically signs the authorization inputs it is responsible for — no manual approval per trade.

Co-signing here means each side signs its own inputs in the same transaction. It is not one 2-of-2 multisig script holding all inputs.

### Atomic Exchange

The BTC payment and the AIBRC transfer instruction go into the same transaction, instead of payment and token delivery as two separate transactions. Delivery must still satisfy AIBRC protocol rules; being signed or broadcast alone does not make it complete.

### Requirements & Where Assets Go

Connect and confirm your linked wallet → enter the BTC amount → check quote & fees → sign in wallet → node co-signs & broadcasts → delivered on-chain

- Minimum swap: 10,000 sats (0.0001 BTC)
- Wallet funds: besides the swap amount, keep BTC for the network fee and the transaction outputs
- Receiving: AIBRC is delivered straight to your linked external wallet address
- Account view: your on-platform AIBRC balance does not increase as well

AIBRC uses an address-level balance model. Transaction outputs take part in protocol receiving and authorization; tokens are not bound to a particular "carrier sat".

## 3.4 Layered Settlement {#c3-s4}

### Delivered at 1 confirmation · Pooled at 2

Block Swap splits asset delivery to you and AMM reserve accounting into two confirmation stages, drawing a clear line between delivery and pool settlement.

```text
Transaction co-signed & broadcast
    │ Propagating or in the mempool
    ▼
1st Bitcoin block confirmation · 1-Conf
    ├─ Transaction in a block
    ├─ AIBRC protocol index confirms validity
    └─ Asset delivery to your linked wallet confirmed
    │
    │ The BTC may still be pending pool entry
    ▼
2nd Bitcoin block confirmation · 2-Conf
    ├─ AMM reserves & fees recorded
    └─ Moves from pending to confirmed reserve
```

### Why two stages?

Valid asset delivery is recognized at 1 confirmation, so you get the on-chain asset promptly. The corresponding BTC formally enters the AMM reserves at 2 confirmations, adding a confirmation buffer to pool accounting against short reorgs.

This does not mean 2 confirmations rule out every reorg risk, and "the wallet has received the asset" is not the same moment as "the BTC is formally in the pool".

Bitcoin block intervals vary naturally. Congestion, fee rates, chain reorgs and index sync can all affect waiting time. The system tracks status by the original transaction hash; don't pay again just because the page hasn't refreshed yet.

## 3.5 Pending-aware Pricing {#c3-s5}

When Instant and Block Swap share one market, a key problem arises: some swaps are already validly pending settlement, but their BTC isn't yet formally in the AMM. If later trades still quoted only from the old reserves, they would ignore the market change those swaps cause.

With pending-aware pricing, AiBTC records confirmed reserves and valid pending effects separately and uses both to compute later quotes.

```text
Confirmed Reserve
    │
    ├─ Plus net BTC effect of valid pending swaps
    └─ Minus the AIBRC amount of those swaps
    │
    ▼
Effective Reserve
    │
    ├─ Used for later Instant quotes
    └─ Used for later Block Swap quotes
When a swap meets the pool-entry conditions
    │
    ▼
Its pending effect is removed and the confirmed reserve updated
No swap is counted twice
```

### Linking the Two Tracks

Swaps that qualify for pending accounting enter the effective reserve, so later trades reflect swaps already accepted instead of a price that ignores them.

Counting toward quotes does not mean the funds have settled on-chain; a request that only reached the preview stage does not change the effective reserve either.

This mechanism links the different speeds of instant execution and block confirmation. Sharing one market doesn't mean different times or routes always get identical quotes; the current valid quote is what counts.

## 3.6 Atomic Swap Units & Dynamic Limits {#c3-s6}

Block Swap manages concurrent execution and unconfirmed exposure with three indicators: Atomic Swap Units, the dynamic limit and pending BTC. Each answers a different question; none replaces another.

### ① Atomic Swap Unit

Each asset starts with a target of 25 Atomic Swap Units. A unit manages a renewable protocol authorization resource: submission occupies it, and confirmation checks restore it. The target can be adjusted through the admin console based on market cap, liquidity and demand, by preparing and approving an expansion plan. This does not mean a market-cap-driven automatic expansion strategy is already enabled.

The main figure shows pending resource usage as total units minus available units, without a denominator. The current target limit is shown in the information tooltip:

- 0: no units shown in use
- 1: one unit shown in use
- 2: two units shown in use

This figure reuses resource availability: maintenance, disabled units and units not yet ready can also contribute to the difference. It is not an independent count of on-chain orders. When the target changes from 25 to 50, the figure still uses total minus available, and the tooltip limit changes to 50. A higher target does not mean the new units are already confirmed and available. Admission still depends on unit availability, the dynamic limit, inventory and your own order status.

### Atomic Swap Unit Recovery

After the matching transaction confirms and the successor authorization input passes validity and unspent checks, the Atomic Swap Unit can take orders again. Atomic Swap Units don't all reset with every new block, and recovery does not mean every resource of the original order has been finally released.

Each user is also limited per asset by orders in progress. If a swap is already processing, check that order first; a free Atomic Swap Unit elsewhere is no reason to submit again.

### ② Dynamic Swap Limit

The system takes 20% of the current confirmed BTC reserve as the base for swaps not yet in a block, minus the total of swaps not yet first seen in a block, to get the limit left for new requests.

```text
Limit left now
    = Confirmed BTC reserve × 20%
    − Total of swaps not yet first seen in a block
```

### Example

Confirmed BTC reserve: 1.00 BTC

Limit base: 0.20 BTC

Currently not yet in a block: 0.08 BTC

Left for new requests: 0.12 BTC

Usage counts the gross swap amount, not net principal after fees. What you can actually submit is still bounded by Atomic Swap Units, inventory, your order status and the latest quote.

### When is the limit released?

Once a swap is first seen in a block, it leaves the not-yet-in-block usage, freeing limit for later requests.

### ③ Pending BTC

BTC already counted as pending pool entry but not yet formally recorded in the AMM; shown to track settlement progress.

### Why do pending BTC and limit usage differ?

```text
The same transaction
    │
    ├─ First seen in a block
    │    └─ Leaves not-yet-in-block limit usage
    │
    └─ Reaches 2 confirmations & is recorded
         └─ Moves from pending to confirmed reserve
```

So a swap may already have freed limit for new requests while still showing in pending BTC.

Before ordering, check all three: is an Atomic Swap Unit available, is the swap limit enough, and do you already have an order in progress? No single indicator guarantees a fill.

## 3.7 Trading Fees {#c3-s7}

Swap fees consist of the base trading fee, the covenant rule fee and the Bitcoin network fee. BTC needed for transaction outputs is shown separately, not lumped into platform fees.

### Base Fee

- Base rate: 0.5% (50 bps)
- Buy or BTC → AIBRC swap: the fee comes out of the gross input; the net principal sets the swap amount
- Instant sell: BTC output before fees is computed first, then the fee is deducted to settle net BTC

### Covenant Fee

If the asset chose the R1 Tax Covenant at launch, an extra rule fee applies after graduation at the parameters fixed at creation; no extra fee during the bonding-curve stage.

- Rate range: 0–5%
- Step: 0.1%
- Active from: after graduation
- Fee goes to: system block buyback or creator earnings, per the asset's rules

For example, a 0.5% base fee plus a 2% R1 rule fee makes a 2.5% total trading fee. This excludes Block Swap network fees and BTC needed for transaction outputs.

### Network Fee

Instant runs in the account state machine and does not broadcast a Bitcoin transaction per fill, so there's no on-chain network fee per trade.

Block Swap broadcasts a Bitcoin mainnet transaction, and your external wallet pays the network fee.

- Default suggested rate: recommended fast rate +1 sat/vB
- Minimum rate: 2 sat/vB
- Estimated network fee: estimated transaction size in vB × confirmed rate

"+1" adds 1 sat per virtual byte to the rate; it is not a flat extra 1 sat per transaction.

Once you confirm a custom rate, the system won't raise it automatically if the recommended rate goes up later. A rate that is too low may mean a longer wait or fail submission checks; the result of that attempt is what counts.

```text
Block Swap wallet spend
    ├─ Gross swap amount
    │    ├─ Net swap principal
    │    ├─ 0.5% base trading fee
    │    └─ Applicable R1 covenant fee
    ├─ Bitcoin network fee
    └─ BTC needed for transaction outputs
```

Before signing, check the payment, each fee, receive details and change. Change is an output returned to your wallet, not a platform charge.

## 3.8 Quotes, Price Impact & Slippage {#c3-s8}

### Estimated Received

The amount you're expected to receive, computed from the current effective reserves, trade size and fees. It is not an unconditional promise; execution must still meet this quote's and authorization's conditions.

### Price Impact

How far your order's own size moves the average execution price from the pre-trade reserve price. The larger the trade relative to pool reserves, the larger the impact usually is.

Price impact comes from the trade itself changing reserves. It is not a fee, and not the slippage caused by other trades while you wait.

### Slippage

The gap between the quote you saw and the actual result, caused by other trades, reserve changes or pending-state changes between viewing the quote and execution.

### Minimum Received

With price protection on and a tolerance set, the system computes the minimum receive from the quote as a constraint on this trade. Amounts are integers in each asset's smallest unit.

Estimated receive: 10,000 tokens

```text
Price protection: 1%
Minimum receive: 9,900 tokens
    │
    ├─ Actual amount ≥ 9,900 tokens
    │    └─ Protection met; other fill conditions still checked
    │
    └─ Actual amount < 9,900 tokens
         └─ No fill below that floor
```

Price protection constrains this fill's result; it does not protect your principal or future market prices.

### Turning Price Protection Off

With it off, the system sets no non-zero minimum receive floor. The estimate can no longer be read as a guaranteed minimum; balance, limits, authorization and other conditions still apply.

### Re-quoting

When a quote expires or conditions change, review the updated quote. A refreshed quote on the page does not create a new order, and never loosens the original order's minimum receive.

## 3.9 Market Data & Holdings {#c3-s9}

### Price

Shows the last trade price in sats per token, convertible to USD at the BTC reference price. A USD display does not mean a separate USD pool exists.

The last price is a market reference; actual buys and sells follow the quote generated after you enter an amount. It doesn't mean any size can fill at that price.

### Market Cap

```text
Market cap = Last price × Fixed total supply
```

For an asset with a 1 billion supply, it's computed on that 1 billion. Market cap is a valuation metric — not the BTC in the pool, and not what all holders would get by selling at once.

### Volume

Trading size counted into market data over the period. Volume shows activity; it is not net inflow and not current liquidity.

### Candlestick

Open, high, low, close and volume summarized per time interval, for viewing trading history.

Intervals: 1m / 5m / 15m / 1h / 4h / 1d.

Historical candles don't predict future prices and are not a quote for the next trade.

### My Holdings

```text
Total holdings in your AiBTC account
    ├─ Available balance
    │    └─ For actions allowed by the current stage & conditions
    │       Un-graduated AIBRC can't be withdrawn
    │
    └─ Locked balance
         └─ Until the related action completes or the rules release it
Holdings in your linked external wallet
    └─ AIBRC and other on-chain assets delivered by Block Swap
         └─ To sell with Instant, deposit the AIBRC first
```

Holding value is quantity × market price, not the net proceeds of selling everything. Real sell results are also bounded by price impact, fees and available reserves.

LP shares and their lock status are shown separately under liquidity rules, not mixed with ordinary token balance locks.

### Market Change & Your P&L

24h change reflects the market price move, not your holding's return. Your P&L needs your buy cost, trading fees, sell history and current holdings.

### Data Updates

Market data updates as new data arrives, and you can refresh manually. On-chain confirmation, protocol indexing, market aggregation and account balances are separate stages, so not every metric changes at the same moment.

When data is delayed or unavailable, read the page status; missing data is never a zero price, zero volume or zero assets.

## 3.10 Order Status & Recovery {#c3-s10}

### Instant Status Flow

```text
Submit order
    │
    ▼
Waiting → AIBTC CORE executing
                │
                ├─ Filled → balances updated
                ├─ Clearly not filled → handled per actual charge & lock
                └─ Result pending → check the original order
```

### Block Swap Status Flow

```text
Quote & handshake
    │
    ▼
Wallet signs → node co-signs → broadcast to the network
                                           │
                                           ▼
                              Awaiting block confirmation
                                           │
                                           ▼
                                1 conf: asset delivered
                                           │
                                           ▼
                              2 conf: recorded in the AMM
```

### Signing, Broadcast & Confirmation

Signed is not broadcast, and broadcast is not in a block. A transaction gets on-chain confirmation only once it's in a block, and delivery still needs the protocol validity check.

Use the original order and transaction hash to track progress, including after a page timeout. Check the original payment's status before sending another.

### Idempotent Recovery

The system checks results against the original request ID, keeping retried queries tied to the original order instead of creating a new trade after a single network timeout.

Recovery keeps the original trade constraints: it never raises the charge, and never lowers the minimum receive.

### Exceptions

- Quote expired: get a new quote, check it, then confirm.
- Too many pending block swaps. Try again shortly.
- The pending total is over 20% of pool liquidity. Try again shortly.
- Order already in progress: handle or check the original order first.
- Wallet signing failed: check the wallet and the original request to see whether a transaction was created.
- Broadcast but unconfirmed: track the original transaction; don't pay again.
- Result unknown: check the original order first; don't resubmit as if it failed.

An order that was never charged needs no "refund"; any lock or charge that did happen is handled from the original order's facts and the recovery rules.

## 3.11 A Bitcoin L1 Trading Base for People & Agents {#c3-s11}

Dual-track Swap isn't just two trade buttons on one page; it lets different ways of using assets work together under one market and public rules.

For traders: one route for speed, one for wallet delivery

To trade continuously and rebalance, use Instant and skip the per-trade on-chain wait and network fees.

To pay straight from your wallet's BTC and receive the asset at your linked address, use Block Swap: one wallet handshake joins one atomic swap.

You don't have to pick speed or on-chain delivery once and for all; choose the route by what each action is for.

For the ecosystem: one core market that keeps connecting apps

The AIBRC root asset carries core trading and liquidity, while same-root protocols and external apps keep room to grow. We want new ecosystem exploration to connect with the existing market and community, instead of scattering assets and depth with every new direction.

Pending-aware pricing links the two trading routes, and covenant rules tie fee distribution to asset rules. Trading fees follow the relevant stage and covenant, supporting liquidity providers, creator earnings and community building.

For future Agents: from understanding intent to independent verification

Structured quotes, explicit fee rates, dynamic limits and minimum receive give Agents computable terms for understanding a trade.

In the future, you'll state a trading goal; your personal Agent helps check the route and fees and prepares a preview, and you give the authorization. After execution, the Agent can use the full execution record, Bitcoin on-chain data and timestamp proofs to check that the result follows the public rules.

```text
Your trading intent
"Use 0.05 BTC, 1% price protection, deliver to my wallet"
    │
    ▼
Personal Agent · Claude / Codex / OpenClaw
    ├─ Reads the open market & limit data
    ├─ Checks quote, price impact & fees
    └─ Computes minimum receive, prepares the preview
    │
    ▼
You keep final authorization
Check the terms → sign the PSBT in your local wallet
    │
    ▼
Protocol execution & on-chain delivery
Co-sign & broadcast → delivered at 1 conf → pooled at 2
    │
    ▼
Result verification
Execution record + protocol rules + Bitcoin data
Checked against timestamp proofs
```

Timestamp proofs help show that data existed at a point in time; they don't by themselves prove each fill correct. A full recomputation still needs the records and rules.

Agent interaction and independent verification are evolving directions; they don't mean every interface or automatic trading permission is open to any third-party Agent today. Your authorization remains the boundary of execution.

Connect account trading to on-chain value, connect wallet authorization to a shared market, and let people and Agents take part in the Bitcoin ecosystem in one asset language
