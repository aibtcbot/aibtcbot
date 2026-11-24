const BECH32 = 'qpzry9x8gf2tvdw0s3jn54khce6mua7l';
const BECH32_GENERATORS = [0x3b6a57b2, 0x26508e6d, 0x1ea119fa, 0x3d4233dd, 0x2a1462b3];
const BASE58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz';
const utf8 = new TextEncoder();

export function normalizeAddress(value) {
  const address = value.trim();
  return /^bc1/i.test(address) ? address.toLowerCase() : address;
}

function validSegwitAddress(address) {
  if (!address.startsWith('bc1') || address.length < 14 || address.length > 74) return false;
  const words = [...address.slice(3)].map(char => BECH32.indexOf(char));
  if (words.includes(-1)) return false;
  const [version] = words;
  if (version > 16) return false;

  // BIP 173 / 350 polymod, with the expanded mainnet HRP "bc".
  let checksum = 1;
  for (const word of [3, 3, 0, 2, 3, ...words]) {
    const top = checksum >>> 25;
    checksum = ((checksum & 0x1ffffff) << 5) ^ word;
    for (const [index, generator] of BECH32_GENERATORS.entries()) {
      if ((top >>> index) & 1) checksum ^= generator;
    }
  }
  if (checksum !== (version === 0 ? 1 : 0x2bc830a3)) return false;

  const program = words.slice(1, -6);
  const bitCount = program.length * 5;
  const length = Math.floor(bitCount / 8);
  const padding = bitCount % 8;
  if (padding >= 5 || (program.at(-1) & ((1 << padding) - 1))) return false;
  return version === 0 ? length === 20 || length === 32 : length >= 2 && length <= 40;
}

async function validBase58Address(address) {
  if (!/^[13][1-9A-HJ-NP-Za-km-z]{25,34}$/.test(address)) return false;
  let value = 0n;
  for (const char of address) value = value * 58n + BigInt(BASE58.indexOf(char));
  const bytes = new Uint8Array(25);
  let first = bytes.length;
  while (value > 0n && first > 0) {
    bytes[--first] = Number(value & 255n);
    value >>= 8n;
  }
  const leadingZeros = address.match(/^1*/)[0].length;
  if (value !== 0n || first !== leadingZeros || (bytes[0] !== 0 && bytes[0] !== 5)) return false;
  const digest = await crypto.subtle.digest('SHA-256', bytes.subarray(0, 21));
  const checksum = new Uint8Array(await crypto.subtle.digest('SHA-256', digest));
  return bytes.subarray(21).every((byte, index) => byte === checksum[index]);
}

export function createLookup(loadShard) {
  const cache = new Map();

  function shard(token, prefix) {
    const key = token + '/' + prefix;
    if (!cache.has(key)) {
      const pending = Promise.resolve()
        .then(() => loadShard(token, prefix))
        .then(entries => {
          if (!Array.isArray(entries) || entries.some(entry => typeof entry !== 'string')) {
            throw new Error('Unexpected shard format');
          }
          return new Set(entries);
        })
        .catch(error => {
          cache.delete(key);
          throw error;
        });
      cache.set(key, pending);
    }
    return cache.get(key);
  }

  return async value => {
    const address = normalizeAddress(value);
    if (!address) return { state: 'empty' };
    const isMainnet = validSegwitAddress(address) || await validBase58Address(address);
    // The ORDI snapshot includes an OP_RETURN script as an exact entry.
    // Look up script-shaped entries against the published lists as supplied.
    if (!isMainnet && !/^6a(?:[0-9a-f]{2}){1,44}$/.test(address)) return { state: 'invalid' };

    const digest = await crypto.subtle.digest('SHA-256', utf8.encode(address));
    const prefix = new Uint8Array(digest, 0, 1)[0].toString(16).padStart(2, '0');
    const [ordi, dog] = await Promise.all([shard('ordi', prefix), shard('dog', prefix)]);
    const onOrdi = ordi.has(address);
    const onDog = dog.has(address);
    if (onOrdi || onDog) return { state: 'found', ordi: onOrdi, dog: onDog };
    return { state: isMainnet ? 'not-found' : 'invalid' };
  };
}
