from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

from tools.validate_skills import load_schema, validate_repository

ROOT = Path(__file__).resolve().parents[1]


def test_all_skill_files_pass_schema() -> None:
    assert validate_repository(ROOT) == []


def test_invalid_official_mapping_rejected() -> None:
    schema = load_schema(ROOT / "spec" / "skill.schema.json")
    validator = Draft202012Validator(schema)

    sample = yaml.safe_load(
        (ROOT / "skills" / "repo" / "explore-repository" / "skill.yaml").read_text(
            encoding="utf-8"
        )
    )
    sample["official_mapping"] = "invalid"

    errors = list(validator.iter_errors(sample))
    assert errors
