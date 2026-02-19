# Agent Skills Registry

一个面向开发者工作流的 Agent Skills 定义库。

本仓库聚焦于把一次性、不稳定的 Agent 行为沉淀为可复用、可组合、可验证的 Skill 协议与样例实现。

## 快速开始

1. 阅读 `/Users/wanzhongyun/github/skills-registry/SPEC.md`（协议与约束）
2. 阅读 `/Users/wanzhongyun/github/skills-registry/PROJECT.md`（范围与路线图）
3. 执行校验：

```bash
python tools/validate_skills.py
python tools/check_skill_headings.py
pytest
```

## 目录结构

```text
skills/
  repo/
  code-review/
  docs/
  workflows/
docs/
spec/
tools/
tests/
```

## Phase 1 已包含

- `repo/explore-repository`
- `code-review/review-pull-request`
- `docs/generate-release-notes`
- `workflows/onboard-review-release`
