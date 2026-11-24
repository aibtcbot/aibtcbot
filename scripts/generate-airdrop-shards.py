"""Generate the lookup shards from the two frozen public CSV snapshots."""
import csv
import hashlib
import json
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / "site" / "assets" / "airdrop-lookup"
SNAPSHOTS = {
    "ordi": (
        "ORDI-holders-height-977366-28940.csv",
        "b9ed80c3424c06f62234912b6cfee2bc92df97f9c50250d2aee2df9c1f11c14e",
        28_940,
    ),
    "dog": (
        "DOG-holders-height-977366-977370-82114.csv",
        "1fe18af06381cd655eec22dcac966f1119f9dedcc4c3590b54be6d967a9e1c7a",
        82_114,
    ),
}


def normalize(address):
    address = address.strip()
    return address.lower() if address.lower().startswith("bc1") else address


def read_snapshot(name, digest, row_count):
    path = ASSETS / "snapshots" / name
    if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
        raise ValueError(f"Snapshot SHA-256 mismatch: {name}")
    with path.open(encoding="utf-8", newline="") as raw:
        reader = csv.DictReader(raw)
        if reader.fieldnames != ["address", "balance"]:
            raise ValueError(f"Unexpected CSV columns: {name}")
        addresses = [normalize(row["address"]) for row in reader]
    if len(addresses) != row_count or len(set(addresses)) != row_count or "" in addresses:
        raise ValueError(f"Unexpected row count or address duplication: {name}")
    return addresses


def main():
    # Verify both inputs before writing any output.
    snapshots = {token: read_snapshot(*source) for token, source in SNAPSHOTS.items()}
    for token, addresses in snapshots.items():
        buckets = {f"{number:02x}": [] for number in range(256)}
        for address in sorted(addresses):
            prefix = hashlib.sha256(address.encode("utf-8")).hexdigest()[:2]
            buckets[prefix].append(address)
        target = ASSETS / "shards" / token
        target.mkdir(parents=True, exist_ok=True)
        for key, entries in buckets.items():
            data = json.dumps(entries, separators=(",", ":"), ensure_ascii=True)
            (target / (key + ".json")).write_bytes((data + "\n").encode("ascii"))
        print(f"{token}: {len(addresses)} entries in {len(buckets)} shards")


if __name__ == "__main__":
    main()
