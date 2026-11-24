---
name: skill-maker
description: "Use when someone wants to turn a prompt they reuse into an installable skill. Guides the name and description, generates SKILL.md, and explains how to install it in Claude Desktop (zip upload) or other agents and test that it triggers. Uses a weekly-report skill as the worked example. 想把常用提示词变成可安装 skill 时用。"
---

# skill-maker · 做自己的 skill

学习路径位置：**做自己的 skill**。

## 何时使用

- 把常用提示词 / 工作流变成可安装 skill
- 问 SKILL.md、description 怎么写才会被触发

## 不要用这个 skill

- 代写周报正文、排障「skill 不生效」（后者用 setup-doctor）
- 上架到某商店的运营流程

## 工作流

1. 问清什么时候该触发。
2. 起 `name`（小写加连字符）→ 写 `description`（触发场景写清，不超过 1024 字符）。
3. 整理成 `SKILL.md` 正文。
4. **默认安装（Claude 桌面版）**：把文件夹打成 zip（顶层是 `<name>/SKILL.md`），在 Customize > Skills 上传并打开开关。详见 `references/install-table.md` 与 [官方 how-to](https://claude.com/docs/skills/how-to)。
5. 可选：Claude Code / Codex / DeepSeek Harness 的目录安装方式见同表。
6. 让用户写 5 句该触发、5 句不该触发自测。
7. 讲理由：为什么 description 要比正文更「会触发」。

规范要点见 `references/spec-checklist.md`。示例：`examples/weekly-report-skill/`（虚构示例）。
