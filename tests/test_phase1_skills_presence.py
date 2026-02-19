from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_phase1_required_files_exist() -> None:
    required = [
        ROOT / "skills/repo/explore-repository/SKILL.md",
        ROOT / "skills/repo/explore-repository/skill.yaml",
        ROOT / "skills/repo/explore-repository/evals/basic-case.yaml",
        ROOT / "skills/code-review/review-pull-request/SKILL.md",
        ROOT / "skills/code-review/review-pull-request/skill.yaml",
        ROOT / "skills/code-review/review-pull-request/evals/basic-case.yaml",
        ROOT / "skills/docs/generate-release-notes/SKILL.md",
        ROOT / "skills/docs/generate-release-notes/skill.yaml",
        ROOT / "skills/docs/generate-release-notes/evals/basic-case.yaml",
        ROOT / "skills/workflows/onboard-review-release/SKILL.md",
        ROOT / "skills/workflows/onboard-review-release/skill.yaml",
        ROOT / "skills/workflows/onboard-review-release/workflow.yaml",
        ROOT / "skills/workflows/onboard-review-release/evals/basic-case.yaml",
    ]
    missing = [str(p) for p in required if not p.exists()]
    assert not missing


def test_workflow_order_is_fixed() -> None:
    workflow_data = yaml.safe_load(
        (ROOT / "skills/workflows/onboard-review-release/workflow.yaml").read_text(
            encoding="utf-8"
        )
    )
    uses = [step["uses_skill"] for step in workflow_data["steps"]]
    assert uses == [
        "repo/explore-repository",
        "code-review/review-pull-request",
        "docs/generate-release-notes",
    ]


def test_eval_must_not_contains_anti_hallucination_rules() -> None:
    expected = {"编造事实", "编造命令", "编造指标或性能数据"}
    eval_files = list((ROOT / "skills").rglob("evals/basic-case.yaml"))

    assert eval_files
    for eval_file in eval_files:
        data = yaml.safe_load(eval_file.read_text(encoding="utf-8"))
        rules = set(data.get("must_not", []))
        assert expected.issubset(rules), f"Missing rules in {eval_file}"
