from __future__ import annotations

import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]


def validate_yaml(path: Path, schema_path: Path) -> list[str]:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [f"{path}: {error.message}" for error in sorted(validator.iter_errors(data), key=str)]


def main() -> int:
    errors: list[str] = []
    measure_schema = ROOT / "schemas" / "measure.schema.json"
    for path in (ROOT / "data" / "examples").glob("*.yml"):
        if "measure" in path.name:
            errors.extend(validate_yaml(path, measure_schema))

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Validation OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
