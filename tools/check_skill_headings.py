#!/usr/bin/env python3
"""Ensure every SKILL.md contains required headings in exact order."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HEADING_PATTERN = re.compile(r"^##\s+(.*\S)\s*$")


def load_required_headings(path: Path) -> list[str]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list) or not all(isinstance(x, str) for x in data):
        raise ValueError("required headings file must be a JSON string array")
    return data


def extract_h2_headings(markdown: str) -> list[str]:
    headings: list[str] = []
    for line in markdown.splitlines():
        m = HEADING_PATTERN.match(line)
        if m:
            headings.append(m.group(1).strip())
    return headings


def check_skill_file(path: Path, required_headings: list[str]) -> list[str]:
    content = path.read_text(encoding="utf-8")
    found = extract_h2_headings(content)
    errors: list[str] = []

    pos = {name: idx for idx, name in enumerate(found) if name in required_headings}

    for heading in required_headings:
        if heading not in pos:
            errors.append(f"{path}: Missing heading '{heading}'")

    if not errors:
        indexes = [pos[h] for h in required_headings]
        if indexes != sorted(indexes):
            errors.append(
                f"{path}: Required headings are out of order; expected exact order from spec"
            )

    return errors


def check_repository(repo_root: Path) -> list[str]:
    skills_root = repo_root / "skills"
    required = load_required_headings(repo_root / "spec" / "required-skill-headings.json")

    files = sorted(skills_root.rglob("SKILL.md"))
    if not files:
        return [f"{skills_root}: no SKILL.md files found"]

    errors: list[str] = []
    for file in files:
        errors.extend(check_skill_file(file, required))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate SKILL.md required headings")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root path",
    )
    args = parser.parse_args()

    errors = check_repository(args.repo_root)
    if errors:
        for err in errors:
            print(err)
        return 1

    print("Heading validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
