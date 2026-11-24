# Airdrop Address Lookup

<span translate="no">AiBTC</span> ecosystem genesis incentives: <span translate="no">ORDI</span> &amp; <span translate="no">DOG</span> community airdrop

Conditions:

- Address holds <span translate="no">ORDI</span> or <span translate="no">DOG•GO•TO•THE•MOON</span>
- Log in with it at aibtc.bot from November 25, 2026 to January 25, 2027 (UTC)

30M <span translate="no">AiBTC</span>, split equally per address.

No forms. No DMs. Log in = registered.

## Look up your address

<form id="airdrop-lookup">
  <input id="airdrop-address" type="text" placeholder="Enter a Bitcoin address" aria-label="Enter a Bitcoin address" aria-describedby="airdrop-result" maxlength="100" autocomplete="off" autocapitalize="none" spellcheck="false">
  <button type="submit" class="md-button">Look up</button>
</form>
<div id="airdrop-result" role="status" aria-live="polite" aria-atomic="true"></div>

<div hidden>
<template id="airdrop-invalid"><p>Enter a Bitcoin mainnet address.</p></template>
<template id="airdrop-loading"><p>Looking up…</p></template>
<template id="airdrop-not-found"><p>This address is not on the list. Enter the address that holds your <span translate="no">ORDI</span> or <span translate="no">DOG</span>; some wallets show two addresses per account.</p></template>
<template id="airdrop-load-error"><p>The list could not be loaded. Please try again.</p></template>
<template id="airdrop-found">
  <strong>Eligible</strong>
  <p data-token="ordi">This address is on the <span translate="no">ORDI</span> holder list.</p>
  <p data-token="dog">This address is on the <span translate="no">DOG•GO•TO•THE•MOON</span> holder list.</p>
  <p>Log in at aibtc.bot with this address from November 25, 2026 to January 25, 2027 (UTC) to register.</p>
</template>
</div>

## About the list

- <span translate="no">ORDI</span>: all holder addresses at Bitcoin block 977366 — 28,940 addresses.
- <span translate="no">DOG•GO•TO•THE•MOON</span>: 82,114 holder addresses, taken at Bitcoin blocks 977366–977370.
- Source: <span translate="no">UniSat</span> Open API.
- The full lists and their SHA-256 are published in this repository. Anyone, and any Agent, can check them.
- The lookup runs in your browser.
