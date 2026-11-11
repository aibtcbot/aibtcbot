# Code examples

These are selected examples from the platform's public interfaces and the wallet-signature notes already published in this repository. They explain the interaction; they are not a trading SDK.

## Read public markets

No API key or wallet credential is needed for the public market API.

```javascript
const response = await fetch(
  'https://aibtc.bot/api/v1/public/markets?page=1',
  { credentials: 'omit' }
);

if (!response.ok) {
  throw new Error(`HTTP ${response.status}`);
}

const result = await response.json();
console.log(result.data, result.as_of, result.stale);
```

Keep the snapshot time and `stale` flag with the data. Follow the [API usage rules](build-tools.md#build-s2) for scope, rate limits and errors.

## Connect an Agent through MCP

The hosted MCP endpoint is:

```text
https://aibtc.bot/api/v1/public/mcp
```

For a client that supports local stdio MCP:

```json
{
  "mcpServers": {
    "aibtc": {
      "command": "npx",
      "args": ["-y", "@aibtcbot/mcp@0.2.0"]
    }
  }
}
```

The four market tools are read-only. See the [complete MCP and npm documentation](build-tools.md#build-s3).

## Ask the wallet to sign a message

The existing UniSat adapter uses the wallet's message-signing API:

```typescript
const signature = await provider.signMessage(
  input.message,
  "bip322-simple"
);
```

The message determines the purpose. Read the actual [sign-in and authorization messages](wallet-signatures.md#2-signing-in) before treating a signature as permission for an action.

## Specify the PSBT inputs to sign

The handshake adapter takes the signing instructions from the preview:

```typescript
const toSignInputs = preview.wallet_sign_inputs.map(s => ({
  index: s.index,
  address: s.address,
  sighashTypes: [...s.sighash_types]
}));
```

The adapter also checks the allowed signature modes and the selected wallet identity. See [what your wallet signs](wallet-signatures.md#4-on-chain-transactions-what-your-wallet-signs) for the full explanation and implementation excerpts.

## Check copied proof material

Run the [Python reference script](reference-proof.md) on a copied proof. Use the [verification guide](verification/README.md) to check the Bitcoin anchor and recalculate trade amounts and reserves.
