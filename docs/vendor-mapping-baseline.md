# Official Skill Mapping Baseline

本文件定义 `official_mapping` 的统一语义，确保跨厂商迁移时语义稳定。

## 字段结构

```yaml
official_mapping:
  openai:
    native_tools: ["..."]
    mapping_notes: "..."
  github_copilot:
    native_tools: ["..."]
    mapping_notes: "..."
  anthropic:
    native_tools: ["..."]
    mapping_notes: "..."
```

## 约束

- `native_tools` 只列官方能力名，不写自定义工具
- `mapping_notes` 描述能力映射边界与注意事项
- 不绑定具体 SDK 版本
- 同一 Skill 的三方映射应表达等价意图，而非完全相同实现细节
