# onboard-review-release

## Intent

将仓库上手、PR 评审、发布说明生成串联为单一可复用工作流 Skill。

## When to use

- 新成员接手项目并需要完成一次完整交付前检查
- 需要在一次流程中产出仓库理解、风险评审、发布说明
- 希望减少跨步骤信息丢失

## When NOT to use

- 仅需执行单个基础 Skill
- 缺少 PR 或 commits 范围，无法完成完整链路
- 需要自动执行代码修复与发布操作

## Inputs

- `repository_path`：仓库绝对路径
- `pull_request_ref`：PR 引用
- `commits_range`：发布说明提交范围

## Outputs

输出 `workflow_report`（Markdown），固定包含：
- repository_report 摘要
- review_report 摘要
- release_notes
- 全流程风险与阻塞

## Workflow

1. 执行 `repo/explore-repository`
2. 基于仓库上下文执行 `code-review/review-pull-request`
3. 基于评审结果执行 `docs/generate-release-notes`
4. 汇总为 workflow_report

## Success criteria

- 三个子 Skill 按顺序执行并产出结果
- workflow_report 含完整链路摘要与阻塞信息
- 任一步失败时触发声明式 fallback

## Failure modes & fallback

- 前置 Skill 失败：停止后续步骤并返回部分结果
- 输入不完整：指出缺失字段并请求补充
- 子结果冲突：在汇总中标记冲突并建议人工确认

## Official skill mapping

- OpenAI：映射到多步工具调用与结构化汇总能力
- GitHub Copilot：映射到仓库上下文串联与阶段化输出能力
- Anthropic Claude：映射到顺序执行多任务并聚合报告能力

## Stability notes

- 严格固定执行顺序，禁止跳步
- 子 Skill 输出必须保留来源信息
- 任何不确定项都需显式传递到最终报告
