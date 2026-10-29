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


def validate_yaml(path: Path, schema_path: Path) -> list[str]:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [f"{path}: {error.message}" for error in sorted(validator.iter_errors(data), key=str)]


def main() -> int:
    errors: list[str] = []
    for filename, schema_filename in EXAMPLE_SCHEMAS.items():
        path = ROOT / "data" / "examples" / filename
        schema_path = ROOT / "schemas" / schema_filename
        errors.extend(validate_yaml(path, schema_path))

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
