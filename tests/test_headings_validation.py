from pathlib import Path

from tools.check_skill_headings import (
    check_repository,
    check_skill_file,
    load_required_headings,
)

ROOT = Path(__file__).resolve().parents[1]


def test_all_skill_markdown_have_required_headings() -> None:
    assert check_repository(ROOT) == []


def test_missing_heading_fails(tmp_path: Path) -> None:
    required = load_required_headings(ROOT / "spec" / "required-skill-headings.json")
    bad_file = tmp_path / "SKILL.md"
    bad_file.write_text(
        "\n".join(
            [
                "## Intent",
                "## When to use",
                "## Inputs",
            ]
        ),
        encoding="utf-8",
    )

    errors = check_skill_file(bad_file, required)
    assert any("Missing heading" in err for err in errors)
