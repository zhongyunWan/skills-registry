# Agent Skills 定义库 — 项目规格说明（SPEC）

## 1. 项目目标

本仓库构建一个可复用、可组合、可执行的 Agent Skills 定义层。

核心目标：将不稳定的一次性 LLM Agent 行为，沉淀为结构化、可复用、可组合、可验证的 Skill 工作单元，并稳定应用在真实开发者工作流中。

本仓库不是：
- Prompt 集合
- 通用 Tool 封装库
- 单一厂商绑定的 Agent 实现

本仓库是：
- Agent Skill 定义层 / 协议层
- 官方 Skills / Tools 的兼容与增强层
- 面向 Workflow 的能力沉淀库
- 可长期演进的 AI 辅助工作方法论载体

## 2. 核心问题

1. Agent 结果不稳定、不可控
2. 工作流难表达、难组合、难复用
3. 官方技能偏原子化，隐含逻辑多
4. 团队缺少 AI 工作经验沉淀机制

## 3. 设计原则

### 3.1 Skill 粒度原则

- 每个 Skill 表示可感知、可验收任务
- 对应 10-30 分钟人类工作量
- 人类能快速判断成功与否

### 3.2 执行模型

Skill 默认由 LLM Agent 执行，且必须受约束、可引导。稳定性与可控性优先。

每个 Skill 必须显式定义：
- Inputs
- Outputs（结构固定）
- Workflow
- Success criteria
- Failure modes & fallback

### 3.3 官方生态对齐

- 尽可能 1:1 对齐官方 Skills / Tools
- 不发明新工具
- 价值在于固化不稳定行为、显式隐含流程、提升可预测性

每个 Skill 必须声明 Official skill mapping。

### 3.4 可组合性

- Skill 必须可组合为 Workflow Skill
- 组合后的 Workflow 仍是 Skill
- 组合必须声明式、步骤化、可读

## 4. Skill 协议

### 4.1 基本形态

每个 Skill 以目录存在，最小必需文件：

```text
SKILL.md
```

推荐文件：
- `skill.yaml`（机器可校验契约）
- `evals/`（稳定性评测样例）
- `workflow.yaml`（组合型 Skill）

### 4.2 SKILL.md 必需章节

每个 `SKILL.md` 必须包含以下 10 个二级标题（标题文本精确匹配）：

1. Intent
2. When to use
3. When NOT to use
4. Inputs
5. Outputs
6. Workflow
7. Success criteria
8. Failure modes & fallback
9. Official skill mapping
10. Stability notes

该文档目标是约束 Agent 行为，而不是激发创意。

### 4.3 双轨约束

- 人类轨：`SKILL.md`
- 机器轨：`skill.yaml` + `spec/*.schema.json`

CI 必须阻止不满足协议约束的变更。

## 5. 仓库结构

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

目录按能力域组织，而非技术分层。

## 6. Phase 1 范围

基础 Skills：
1. `repo/explore-repository`
2. `code-review/review-pull-request`
3. `docs/generate-release-notes`

组合 Workflow：
- `workflows/onboard-review-release`

## 7. 稳定性与评测要求

- 每个 Skill 建议包含 `evals/`
- 必须明确失败场景与兜底策略
- Agent 禁止：
  - 编造事实
  - 编造命令
  - 编造指标或性能数据

## 8. 非目标

本仓库不试图：
- 替代 Agent 框架
- 定义执行引擎或运行时
- 提供 UI 或最终用户产品
- 做模型特定 prompt trick 优化

## 9. 成功标准

- Skill 目录可直接复制使用
- Skills 可组合且无需重写逻辑
- 输出更可预测、可复核
- 团队可持续沉淀 AI 工作流
- Skills 可跨厂商迁移

## 10. 与 AI 工具协作约束

本文件是项目单一事实源。

所有 AI 生成目录、文件、内容都必须严格遵循本规格。
