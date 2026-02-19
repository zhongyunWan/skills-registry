# 编写规范与贡献约定

## 1. Skill 命名与目录

- 使用小写、连字符、语义化名称
- 路径格式：`skills/<domain>/<skill-name>/`
- `domain` 当前允许：`repo`、`code-review`、`docs`、`workflows`

## 2. 必需文件

每个 Skill 目录至少包含：
- `SKILL.md`
- `skill.yaml`

推荐包含：
- `evals/basic-case.yaml`

Workflow Skill 额外包含：
- `workflow.yaml`

## 3. SKILL.md 标题规则

必须包含且按顺序出现以下二级标题：
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

## 4. 输出约束

- 输出结构必须可被人类复核
- 禁止编造事实、命令、指标或性能数据
- 无法验证时必须声明不确定性并触发 fallback

## 5. 贡献流程

1. 新增或修改 Skill
2. 运行本地校验：

```bash
python tools/validate_skills.py
python tools/check_skill_headings.py
pytest
```

3. 提交 PR，等待 CI 全绿
