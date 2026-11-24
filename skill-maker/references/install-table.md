# 安装路径摘要（与仓库 README 一致）

默认推荐：**Claude 桌面版 / claude.ai** 上传 zip。其他工具可选。

| 工具 | 怎么装 skill | 说明与出处 |
| --- | --- | --- |
| Claude 桌面版 / claude.ai（默认） | 把技能文件夹打成 zip（zip 顶层必须是 `<name>/SKILL.md`），在 **Customize > Skills** 里上传，并打开开关 | [创建自定义 skill](https://claude.com/docs/skills/how-to) · [Skills 总览](https://claude.com/docs/skills/overview) |
| Claude Code | 个人：`~/.claude/skills/<name>/SKILL.md`；项目：`.claude/skills/<name>/SKILL.md` | [Skills 文档](https://code.claude.com/docs/en/skills) |
| Codex | 用户：`$HOME/.agents/skills`；仓库：`.agents/skills` | [Build skills](https://learn.chatgpt.com/docs/build-skills) |
| DeepSeek Harness | 项目：`<git-root>/.dsh/skills/` 或 `.agents/skills/`；用户：`~/.dsh/skills/` 或 `~/.agents/skills/` | 不递归深嵌套；[skills 子系统](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/subsystems/skills.md) |

无脚本 skill 也可粘贴 CI 生成的 `dist/single-file/<skill>.md`。
