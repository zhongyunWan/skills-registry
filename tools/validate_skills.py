#!/usr/bin/env python3
"""Validate skill.yaml, workflow.yaml, and eval cases against schemas."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


def load_schema(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError(f"{path} is not a YAML object")
    return data


def format_errors(path: Path, errors: list) -> list[str]:
    formatted: list[str] = []
    for err in sorted(errors, key=lambda e: list(e.path)):
        loc = "/".join(str(p) for p in err.path)
        if loc:
            formatted.append(f"{path}: {loc}: {err.message}")
        else:
            formatted.append(f"{path}: {err.message}")
    return formatted


def validate_repository(repo_root: Path) -> list[str]:
    spec_dir = repo_root / "spec"
    skills_root = repo_root / "skills"

    skill_validator = Draft202012Validator(load_schema(spec_dir / "skill.schema.json"))
    workflow_validator = Draft202012Validator(load_schema(spec_dir / "workflow.schema.json"))
    eval_validator = Draft202012Validator(load_schema(spec_dir / "eval-case.schema.json"))

    problems: list[str] = []
    skill_files = sorted(skills_root.rglob("skill.yaml"))

    if not skill_files:
        return [f"{skills_root}: no skill.yaml files found"]

    for skill_file in skill_files:
        skill_dir = skill_file.parent
        try:
            skill_data = load_yaml(skill_file)
        except Exception as exc:  # noqa: BLE001
            problems.append(f"{skill_file}: cannot read YAML ({exc})")
            continue

        problems.extend(format_errors(skill_file, list(skill_validator.iter_errors(skill_data))))

        skill_id = skill_data.get("id") if isinstance(skill_data, dict) else None

        workflow_file = skill_dir / "workflow.yaml"
        if workflow_file.exists():
            try:
                workflow_data = load_yaml(workflow_file)
                problems.extend(
                    format_errors(workflow_file, list(workflow_validator.iter_errors(workflow_data)))
                )
                if skill_id and workflow_data.get("workflow_id") != skill_id:
                    problems.append(
                        f"{workflow_file}: workflow_id must match skill id ({skill_id})"
                    )
            except Exception as exc:  # noqa: BLE001
                problems.append(f"{workflow_file}: cannot read YAML ({exc})")

        eval_dir = skill_dir / "evals"
        if eval_dir.exists():
            for eval_file in sorted(eval_dir.glob("*.yaml")):
                try:
                    eval_data = load_yaml(eval_file)
                except Exception as exc:  # noqa: BLE001
                    problems.append(f"{eval_file}: cannot read YAML ({exc})")
                    continue

                problems.extend(format_errors(eval_file, list(eval_validator.iter_errors(eval_data))))
                if skill_id and eval_data.get("skill_id") != skill_id:
                    problems.append(
                        f"{eval_file}: skill_id must match parent skill id ({skill_id})"
                    )

    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate all skill contracts in repository")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root path",
    )
    args = parser.parse_args()

    problems = validate_repository(args.repo_root)
    if problems:
        for problem in problems:
            print(problem)
        return 1

    print("Skill validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
