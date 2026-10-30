"""Validate source-backed historical records and examples.

This checks structure and cross-references, not historical truth or causality.
"""
from __future__ import annotations

import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
EXAMPLE_SCHEMAS = {
    "measure.example.yml": "measure.schema.json",
    "legal_lineage.example.yml": "legal_lineage.schema.json",
}
COLLECTIONS = {
    "legislation": "legal_lineage.schema.json",
    "governments": "government.schema.json",
}


def validate_yaml(path: Path, schema_path: Path) -> list[str]:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [
        f"{path.relative_to(ROOT)}: {error.message}"
        for error in sorted(validator.iter_errors(data), key=str)
    ]


def main() -> int:
    errors: list[str] = []
    all_records: list[tuple[Path, dict]] = []
    seen_ids: set[str] = set()

    for filename, schema_filename in EXAMPLE_SCHEMAS.items():
        errors.extend(
            validate_yaml(ROOT / "data" / "examples" / filename,
                          ROOT / "schemas" / schema_filename)
        )

    for dirname, schema_filename in COLLECTIONS.items():
        for path in sorted((ROOT / "data" / dirname).glob("*.yml")):
            errors.extend(validate_yaml(path, ROOT / "schemas" / schema_filename))
            record = yaml.safe_load(path.read_text(encoding="utf-8"))
            if not isinstance(record, dict):
                errors.append(f"{path.relative_to(ROOT)}: not an object")
                continue
            identifier = record.get("id")
            if identifier in seen_ids:
                errors.append(f"{path.relative_to(ROOT)}: duplicate id {identifier}")
            seen_ids.add(identifier)
            all_records.append((path, record))

    sources_data = yaml.safe_load(
        (ROOT / "data" / "sources" / "sources.yml").read_text(encoding="utf-8")
    ) or {}
    sources = sources_data.get("sources", [])
    source_ids = [s.get("id") for s in sources]
    if len(source_ids) != len(set(source_ids)):
        errors.append("data/sources/sources.yml: duplicate source ids")
    defined_sources = set(source_ids)

    governments = {
        item.get("id") for path, item in all_records
        if path.parent.name == "governments"
    }
    for path, record in all_records:
        references = list(record.get("sources", []))
        for article in record.get("constitutional_comparison", {}).get("articles", []):
            references += article.get("sources", [])
        for phase in record.get("government_phases", []):
            references += phase.get("sources", [])
            if phase.get("government_id") not in governments:
                errors.append(f"{path.relative_to(ROOT)}: unknown government phase {phase.get('government_id')}")
        gov = record.get("approved_under_government_id")
        if gov is not None and gov not in governments:
            errors.append(f"{path.relative_to(ROOT)}: unknown approving government {gov}")
        for sid in references:
            if sid not in defined_sources:
                errors.append(f"{path.relative_to(ROOT)}: unknown source id {sid}")

    for folder in ["legislatures", "parties"]:
        for path in sorted((ROOT / "data" / folder).glob("*.yml")):
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
            if not isinstance(data, dict) or not data.get("id"):
                errors.append(f"{path.relative_to(ROOT)}: missing id")
                continue
            for source_id in data.get("sources", []):
                if source_id not in defined_sources:
                    errors.append(f"{path.relative_to(ROOT)}: unknown source id {source_id}")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validation OK: {len(all_records)} laws/government records checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
