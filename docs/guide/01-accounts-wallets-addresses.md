# 01 Accounts, Wallets & Addresses

### Self-custodial Signing & Non-custodial Wallet Access

AiBTC is built on user-held authorization and self-sovereign design. Wallets connect non-custodially: AiBTC never obtains or stores the private keys of your external wallet. Sign-in establishes your account and its permissions; any on-chain action involving your wallet is confirmed and signed by you in that wallet.

Sign in with a Bitcoin wallet, email or a social account. Once connected, you can check your assets, trade, and use Launch and Liquidity at any time.

## 1.1 Sign-in Methods & Self-authorization {#c1-s1}

### Bitcoin Wallet Sign-in

Connect your wallet and prove address ownership with a BIP-322 message signature to enter your AiBTC account. Your keys stay in your wallet and are never handed to the platform.

### Email Sign-in

Enter your email, receive a code and verify. AiBTC uses Privy, identity and wallet infrastructure for Web3 apps. It brings a familiar email sign-in to on-chain apps and lowers the barrier for new users. [Privy](https://privy.io)

### Social Sign-in

Verify with Google, Telegram, GitHub or X; the options shown in the sign-in window apply.

Email and social sign-in are verified by Privy, and AiBTC opens the matching account session. You never give AiBTC a wallet private key to sign in.

Wallet sign-in: your wallet → BIP-322 signature → AiBTC account

Email / social sign-in: email or social account → Privy verification → AiBTC account

## 1.2 Supported Wallets {#c1-s2}

AiBTC supports the following Bitcoin wallets, currently marked Preview in the interface:

- UniSat
- OKX Wallet
- Xverse
- Bitget Wallet
- Phantom

Connection, sign-in and transaction signing use each wallet's standard capabilities. UniSat and OKX Bitcoin wallets can detect and deposit AIBRC assets directly, and you can see your wallet holdings on the Assets page.

## 1.3 Address Types & Account Model {#c1-s3}

AIBRC identifies asset accounts by the scriptPubKey of a Bitcoin address and supports these mainnet address types:

- Taproot (P2TR): mainnet addresses start with bc1p.
- Native SegWit (P2WPKH): mainnet addresses start with bc1q and use the matching single-key script. bc1q can also stand for other script types; the scriptPubKey decides.

```text
Bitcoin address
    ↓ scriptPubKey (account identity)
AIBRC protocol account
    ↓
Balances & transfer history
```

AIBRC assets are recorded as address-level balances; your external wallet manages keys and signs. Asset operations from your wallet are authorized by you and verified under the protocol rules.

## 1.4 Linking Email Accounts & Bitcoin Wallets {#c1-s4}

Email and social accounts make sign-in easy; a Bitcoin wallet proves address ownership and signs on-chain transactions.

After signing in with email or a social account, follow the on-page steps to link a Bitcoin wallet address and use features that need wallet signatures. Privy only verifies identity on this path; AiBTC does not create embedded Ethereum or Solana wallets because of it.

```text
Email / social sign-in → AiBTC account → link Bitcoin address
                                                  ↓
                                  Wallet authorization & on-chain actions
```

A familiar sign-in, connected to a Bitcoin wallet you control.

## 1.5 Sign-in Signatures & Transaction Signatures {#c1-s5}

### Sign-in Signature · BIP-322

Proves you own the address. No on-chain transfer and no network fee.

### Transaction Signature · PSBT (Partially Signed Bitcoin Transaction)

Used for Block Swap, AIBRC protocol deposits, withdrawals and similar actions. Review the transaction in your wallet and sign; the system then completes co-signing, broadcast and confirmation.

Sign-in: confirms who you are.

Transaction: confirms what you authorize.

Open-source reference: [GitHub · aibtcbot/aibtcbot](https://github.com/aibtcbot/aibtcbot)

## 1.6 Assets {#c1-s6}

The Assets page brings your assets and activity together, linked to verifiable on-chain transactions and public proofs:

- BTC and AIBRC balances
- AIBRC assets detected in your wallet
- Liquidity positions and fee earnings
- Assets you created
- Trades, deposits and withdrawals

From holdings to history, all in one place.

## 1.7 Sessions & Authorization Management {#c1-s7}

After sign-in, AiBTC keeps your session with secure cookies. You can sign out, disconnect your wallet and manage trading authorization. After switching wallet account or network, re-confirm your identity as prompted.

Easy sign-in, self-authorization: your wallet is your gateway to the Bitcoin ecosystem.
