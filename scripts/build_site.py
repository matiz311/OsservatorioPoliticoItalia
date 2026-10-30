"""Generate the public, reproducible site catalog from reviewed repository data."""
from __future__ import annotations

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "site" / "data" / "catalog.json"


def records(folder: str):
    items = []
    base = ROOT / "data" / folder
    if not base.exists():
        return items
    for path in sorted(base.glob("*.yml")):
        if ".example." in path.name:
            continue
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(value, dict):
            if "id" in value:
                items.append(value)
            elif isinstance(value.get("records"), list):
                items.extend(value["records"])
    return items


def main():
    references = yaml.safe_load((ROOT / "data/reference/contexts.yml").read_text(encoding="utf-8")) or {}
    sources = yaml.safe_load((ROOT / "data/sources/sources.yml").read_text(encoding="utf-8")) or {}
    catalog = {
        "measures": records("measures"),
        "acts": records("legislation"),
        "governments": records("governments"),
        "legislatures": records("legislatures"),
        "parties": records("parties"),
        "contexts": references.get("contexts", []),
        "sources": sources.get("sources", []),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(catalog, ensure_ascii=False, indent=2, default=str) + "\n", encoding="utf-8")
    print(f"Built {OUT}: " + ", ".join(f"{k}={len(v)}" for k, v in catalog.items()))


if __name__ == "__main__":
    main()
