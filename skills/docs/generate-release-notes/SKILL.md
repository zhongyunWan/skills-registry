# generate-release-notes

## Intent

基于提交记录与评审结论生成结构化发布说明，保证信息可追溯、可发布。

## When to use

- 需要从 commit / PR 生成版本发布说明
- 需要区分用户可见变更与内部改动
- 需要输出标准化发布文档模板

## When NOT to use

- 没有可用变更记录
- 需要市场文案级别的创意写作
- 需要自动发布到外部平台（本 Skill 只生成说明文本）

## Inputs

- `repository_path`：仓库绝对路径
- `commits_range`：提交范围
- `review_report`：可选，来自代码评审的风险结论

## Outputs

输出 `release_notes`（Markdown），固定包含：
- 版本范围与时间
- 用户可见变更
- 修复项
- 风险与注意事项
- 验证建议

## Workflow

1. 汇总 commits 与可选评审报告
2. 归类变更类型并提炼用户影响
3. 生成标准结构发布说明
4. 对不确定项进行显式标记

## Success criteria

- 发布说明章节完整且可直接复用
- 每个要点可追溯到 commit 或 review 依据
- 明确列出风险与验证建议

## Failure modes & fallback

- commits 范围无效：返回可重试的范围格式示例
- 提交信息不足：输出已知内容并列出缺失信息
- 分类歧义较高：标记待人工确认项

## Official skill mapping

- OpenAI：映射到提交信息读取与结构化文本生成能力
- GitHub Copilot：映射到 PR/commit 上下文摘要能力
- Anthropic Claude：映射到版本变更总结与文档输出能力

## Stability notes

- 不编造不存在的变更项
- 不夸大影响范围
- 无依据时使用“待确认”标记
