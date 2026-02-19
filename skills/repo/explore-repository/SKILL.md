# explore-repository

## Intent

在只读前提下快速建立仓库结构与架构理解，输出可复核的仓库概览报告。

## When to use

- 新接手项目，需要快速上手目录、模块与依赖关系
- 进入代码评审前，需要先建立上下文
- 需要为后续 Skill 提供结构化仓库背景输入

## When NOT to use

- 需要修改代码或执行迁移
- 需要性能压测、基准测试等运行时结论
- 仓库不存在或路径不可访问

## Inputs

- `repository_path`：仓库绝对路径
- `focus_areas`：可选，关注模块列表
- `constraints`：可选，时间或深度限制

## Outputs

输出 `repository_report`（Markdown），固定包含：
- 仓库概览
- 关键目录职责
- 核心依赖与构建入口
- 风险与未知项
- 下一步建议

## Workflow

1. 读取仓库目录树与关键配置文件
2. 识别构建入口、测试入口、主要模块边界
3. 汇总高风险区域与信息缺口
4. 生成结构化报告并标注不确定项

## Success criteria

- 产出包含固定章节的 `repository_report`
- 每个关键判断有可追溯文件依据
- 明确列出未知项，不做无依据推断

## Failure modes & fallback

- 仓库过大导致扫描超时：聚焦顶层目录与核心配置，声明覆盖范围
- 缺少关键配置文件：输出已发现结构并列出缺失项
- 路径不可访问：返回阻塞原因与重试建议

## Official skill mapping

- OpenAI：映射到文件读取与终端只读探索能力
- GitHub Copilot：映射到工作区上下文读取与变更前分析能力
- Anthropic Claude：映射到代码库浏览与只读 shell 分析能力

## Stability notes

- 只输出可验证信息，禁止编造事实
- 不推断未读取文件内容
- 命令示例必须可执行且来自常见工具
