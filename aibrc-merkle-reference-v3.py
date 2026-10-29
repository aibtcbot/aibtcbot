"""AIBRC V3 record/manifest fingerprints and RFC9162 relations.
CLI: python3 aibrc-merkle-reference-v3.py copied.txt (or bundle.json).
OTS header binding is checked; independently verify OTS/Bitcoin by Method v2.
"""
import base64, hashlib, json, re, sys
H = lambda b: hashlib.sha256(b).digest()
L = lambda b: H(b'\x00' + b)
P = lambda a, b: H(b'\x01' + a + b)
MAX = (1 << 63) - 1

def integer(v):
    if not isinstance(v, str) or not re.fullmatch(r'0|[1-9][0-9]{0,18}', v): raise ValueError('INTEGER')
    n = int(v)
    if n > MAX: raise ValueError('INTEGER_RANGE')
    return n

def digest(v):
    if not isinstance(v, str) or not re.fullmatch('[0-9a-f]{64}', v): raise ValueError('HASH')
    return bytes.fromhex(v)

def path(v):
    if not isinstance(v, list) or len(v) > 64: raise ValueError('PATH_SIZE')
    return [digest(x) for x in v]

def inclusion(leaf, i, n, proof, root):
    if not 0 <= i < n <= MAX or len(proof) > 63 or len(leaf) != 32 or len(root) != 32: return False
    fn, sn, r = i, n - 1, leaf
    for p in proof:
        if sn == 0 or len(p) != 32: return False
        if fn & 1 or fn == sn:
            r = P(p, r)
            while fn and not fn & 1: fn >>= 1; sn >>= 1
        else: r = P(r, p)
        fn >>= 1; sn >>= 1
    return sn == 0 and r == root

def consistency(m, n, old, new, proof):
    if not 0 <= m <= n <= MAX or len(proof) > 64 or len(old) != 32 or len(new) != 32: return False
    if m == 0: return old == H(b'') and not proof and (n > 0 or new == H(b''))
    if m == n: return old == new and not proof
    if not proof: return False
    fn, sn = m - 1, n - 1
    while fn & 1: fn >>= 1; sn >>= 1
    nodes = ([old] if m & (m - 1) == 0 else []) + list(proof)
    fr = sr = nodes[0]
    for c in nodes[1:]:
        if sn == 0 or len(c) != 32: return False
        if fn & 1 or fn == sn:
            fr, sr = P(c, fr), P(c, sr)
            while fn and not fn & 1: fn >>= 1; sn >>= 1
        else: sr = P(sr, c)
        fn >>= 1; sn >>= 1
    return sn == 0 and fr == old and sr == new

def context(a, b):
    return all(a.get(k) == b.get(k) for k in ('networkId', 'logEpoch'))

def head(m):
    if m.get('version') != 'AIBRC_CHECKPOINT_MANIFEST_V3': raise ValueError('VERSION')
    if m.get('treeAlgorithm') != 'RFC9162_SHA256' or m.get('leafEncoding') != 'EVENT_HASH_BYTES_V1': raise ValueError('ALGORITHM')
    if m.get('networkId') not in ('mainnet', 'signet', 'testnet', 'regtest'): raise ValueError('NETWORK')
    if not re.fullmatch(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', m.get('logEpoch', '')): raise ValueError('EPOCH')
    return integer(m['treeSize']), digest(m['treeRoot'])

def verify(bundle):
    m, p = bundle['manifest'], bundle['proof']; n, root = head(m)
    if not context(m, p): return False
    if bundle['kind'] == 'inclusion':
        r = bundle['record']; seq = integer(r['sequence']); i = integer(p['leafIndex'])
        return (p.get('version') == 'AIBRC_MERKLE_INCLUSION_V1' and r['network_id'] == m['networkId']
            and p['eventHash'] == r['event_hash'] and integer(p['sequence']) == seq and i == seq - 1
            and integer(p['treeSize']) == n and digest(p['treeRoot']) == root
            and inclusion(L(digest(r['event_hash'])), i, n, path(p['auditPath']), root))
    if bundle['kind'] != 'consistency': return False
    a = bundle['oldManifest']; size, old = head(a)
    return (p.get('version') == 'AIBRC_MERKLE_CONSISTENCY_V1' and context(a, m)
        and integer(p['oldTreeSize']) == size and integer(p['newTreeSize']) == n
        and digest(p['oldRoot']) == old and digest(p['newRoot']) == root
        and consistency(size, n, old, root, path(p['consistencyPath'])))

def checkpoint(c, ots):
    text = c['canonical_manifest']; m = json.loads(text); raw = text.encode('utf-8')
    keys = 'version networkId logEpoch epoch triggerBlock eventSeqRange treeAlgorithm leafEncoding treeSize treeRoot chainTip prevCheckpoint rulesetHash codeVersion'.split()
    if set(m) != set(keys) or json.dumps(m, sort_keys=True, ensure_ascii=False, separators=(',', ':')) != text: raise ValueError('MANIFEST')
    if H(raw).hex() != c['manifest_content_hash'] or H(b'AIBRC-CHECKPOINT-V1' + raw).hex() != c['checkpoint_digest']: raise ValueError('MANIFEST_HASH')
    head(m); n = integer(m['treeSize']); start = integer(m['eventSeqRange']['start'])
    if not 1 <= start <= n or integer(m['eventSeqRange']['end']) != n: raise ValueError('RANGE')
    proof = base64.b64decode(ots['original_file_base64'], validate=True)
    magic = b'\0OpenTimestamps\0\0Proof\0' + bytes.fromhex('bf89e2e884e89294')
    if len(proof) > 1048576 or H(proof).hex() != ots['proof_content_hash']: raise ValueError('OTS_HASH')
    if proof[:len(magic)+2] != magic + b'\x01\x08' or proof[len(magic)+2:len(magic)+34] != digest(c['checkpoint_digest']): raise ValueError('OTS_BINDING')
    return m

def verify_copy(b):
    m = checkpoint(b['checkpoint'], b['ots']); r = b['record']; p = b['inclusion']; seq = integer(r['sequence'])
    payload = r['canonical_payload'].encode('utf-8'); tag = H(b'AIBRC/NetworkEvent/v0.1')
    if len(payload) > 16384 or H(tag + tag + digest(r['previous_event_hash']) + seq.to_bytes(8,'big') + len(payload).to_bytes(4,'big') + payload).hex() != r['event_hash']: return False
    data = json.loads(payload)
    for outer, inner in [('network_id','networkId'),('event_type','eventType'),('epoch','epoch'),('ruleset_hash','rulesetHash'),('source_revision','sourceRevision'),('version','schemaVersion')]:
        if r[outer] != data[inner]: return False
    if p['checkpointDigest'] != b['checkpoint']['checkpoint_digest'] or not verify({'kind':'inclusion','manifest':m,'record':r,'proof':p}): return False
    if b.get('append_only') is None: return True
    a = b['append_only']; old = checkpoint(a['previous_checkpoint'], a['previous_ots']); c = a['consistency']
    return (c['oldCheckpointDigest'] == a['previous_checkpoint']['checkpoint_digest'] and c['newCheckpointDigest'] == b['checkpoint']['checkpoint_digest']
        and verify({'kind':'consistency','manifest':m,'oldManifest':old,'proof':c}))

if __name__ == '__main__':
    try:
        with open(sys.argv[1], 'rb') as f: data = f.read(4 * 1024 * 1024 + 1)
        if len(data) > 4 * 1024 * 1024: raise ValueError('INPUT_SIZE')
        text = data.decode('utf-8').replace('\r\n', '\n')
        try: bundle = json.loads(text)
        except json.JSONDecodeError: bundle = json.loads(text[text.rindex('\n\n{')+2:])
        is_copy = bundle.get('schema_version') == 'AIBRC_EXPLORER_PROOF_COPY_V2'
        ok = verify_copy(bundle) if is_copy else verify(bundle)
        print(('FINGERPRINTS_AND_MERKLE_MATCHED_OTS_BITCOIN_NOT_VERIFIED' if is_copy else 'MERKLE_MATCHED_ONLY') if ok else 'MERKLE_MISMATCH')
        sys.exit(0 if ok else 1)
    except (ValueError, KeyError, TypeError, IndexError, OSError, RecursionError):
        print('INVALID_MERKLE_MATERIAL'); sys.exit(2)
