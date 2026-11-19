# Agent Skills 规范要点（摘要）

以官方规范为准：[Agent Skills specification](https://agentskills.io/specification)

- `name`：小写 + 连字符，并与文件夹同名
- `description`：写清何时用；建议简洁；规范上限 **1024** 字符（过长可能影响列表展示）
- 需要时提供 `agents/openai.yaml`（Codex 展示：display_name、short_description、default_prompt）

本仓库 CI 会检查上述字段。
