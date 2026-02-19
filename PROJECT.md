# Agent Skills Registry — 项目实施说明（PROJECT）

## 1. 项目定位

本文件定义实施路径、里程碑、验收标准与演进策略；具体协议以 `/Users/wanzhongyun/github/skills-registry/SPEC.md` 为准。

## 2. 当前阶段

- 当前阶段：Phase 1
- 目标：交付 3 个基础 Skill + 1 个 Workflow Skill，并建立可执行校验链路

## 3. 交付清单

1. 文档层：`SPEC.md`、`PROJECT.md`、`README.md`
2. 协议层：Schema、标题约束、Vendor mapping baseline
3. 样例层：4 个 Skill（含 `skill.yaml`、`SKILL.md`、`evals/basic-case.yaml`）
4. 校验层：`tools/validate_skills.py`、`tools/check_skill_headings.py`
5. 测试层：`tests/` 下协议、标题、Phase 1 存在性测试
6. CI 层：PR / Push 自动执行校验与测试

## 4. Definition of Done

一个变更被认为完成，必须满足：
- Skill 文档完整包含 10 个必需章节
- `skill.yaml`、`workflow.yaml`、`evals/*.yaml` 均通过 schema 校验
- `pytest` 全绿
- CI 全绿
- Official mapping 覆盖 OpenAI、GitHub Copilot、Anthropic Claude

## 5. 里程碑

1. M1: 协议与文档基线
2. M2: Phase 1 Skills 落地
3. M3: 校验与测试闭环
4. M4: CI 门禁上线

## 6. 迭代策略

- 每个 Skill 后续至少补充 2 类 eval：边界输入、失败回退
- 不引入运行时引擎，保持定义层最小闭环
- 新增域必须先补 schema 与 headings 规则，再加 Skill 实例

## 7. 风险与控制

1. 风险：Skill 文档漂移
   - 控制：heading 精确校验 + CI 门禁
2. 风险：结构字段随意扩展
   - 控制：schema `additionalProperties: false`
3. 风险：跨厂商映射语义不一致
   - 控制：统一 baseline 模板与字段解释
