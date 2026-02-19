# review-pull-request

## Intent

对 Pull Request 进行结构化风险评审，输出可执行、可追踪的审查结论。

## When to use

- 需要在合并前识别行为回归与潜在风险
- 需要快速形成按严重级别排序的问题列表
- 需要为发布说明提供风险上下文

## When NOT to use

- 变更内容不可访问或 diff 不完整
- 需要直接修复代码（本 Skill 只做评审）
- 需要安全审计或合规审计级别的深度检查

## Inputs

- `repository_path`：仓库绝对路径
- `pull_request_ref`：PR 编号或 diff 范围
- `review_focus`：可选，业务或模块重点

## Outputs

输出 `review_report`（Markdown），固定包含：
- 变更概览
- 按严重级别排序的发现
- 证据与影响说明
- 待确认问题
- 建议动作

## Workflow

1. 读取 PR diff 与相关上下文文件
2. 识别行为变化、回归风险、缺失测试
3. 以严重级别排序列出 findings
4. 输出结构化评审报告

## Success criteria

- finding 按严重级别排序且给出文件证据
- 对不确定结论明确标注“待确认”
- 给出可执行后续动作

## Failure modes & fallback

- diff 获取失败：返回阻塞原因并要求补充 PR 上下文
- 变更范围过大：先输出高风险区域审查结果并声明覆盖边界
- 缺少测试信息：记录测试盲区并建议补充验证

## Official skill mapping

- OpenAI：映射到代码阅读、终端 diff 分析与结构化输出能力
- GitHub Copilot：映射到 PR 上下文理解与代码审查建议能力
- Anthropic Claude：映射到代码库 diff 审查与风险总结能力

## Stability notes

- 不给出无证据结论
- 不编造未执行测试结果
- 输出优先级和影响说明必须一致
