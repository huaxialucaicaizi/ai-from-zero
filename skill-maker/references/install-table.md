# 四个工具安装路径摘要（与仓库 README 一致）

| 工具 | skill 放哪（Mac） | 说明 |
| --- | --- | --- |
| Claude Code | 个人 `~/.claude/skills/<name>/SKILL.md`；项目 `.claude/skills/<name>/SKILL.md` | [Skills 文档](https://code.claude.com/docs/en/skills) |
| Codex | 用户 `$HOME/.agents/skills`；仓库 `.agents/skills` | [Build skills](https://learn.chatgpt.com/docs/build-skills) |
| WorkBuddy | 项目级：工作区 `.codebuddy/skills/<name>/` | 官方已写明项目级路径；用户级精确路径 **待核实**，确认前 README 不写死 |
| DeepSeek Harness | 项目 `<git-root>/.dsh/skills/` 或 `.agents/skills/`；用户 `~/.dsh/skills/` 或 `~/.agents/skills/` | 不递归深嵌套；[skills 子系统](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/subsystems/skills.md) |

无脚本 skill 也可粘贴 CI 生成的 `dist/single-file/<skill>.md`。
