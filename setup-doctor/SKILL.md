---
name: setup-doctor
description: "Use on Mac when installing or running Claude Desktop, Claude Code, Codex, or DeepSeek Harness fails: command not found, skills not loading, API 400/401/403/429, zip skill not recognized, or an environment check. Runs a read-only self-check, then matches the error library for a plain-language cause and Mac fixes. Region and account limits cite official terms only. 在 Mac 上安装或使用上述工具报错、命令找不到、skill 不生效时用。"
---

# setup-doctor · 安装排障

学习路径位置：**装上工具**。  
**目前仅支持 Mac**（第一版不做 Windows）。

## 何时使用

- 安装/使用 Claude 桌面版、Claude Code、Codex、DeepSeek Harness 失败
- command not found、skill 不生效、上传 zip 认不出来、API 400/401/403/429
- 「帮我检查电脑环境」

## 不要用这个 skill

- 教绕过地区或账号限制
- 直接写业务文案、做网页、剪视频

## 工作流

1. **收下报错**：文字或截图。截图识别依赖用户自己的 AI 能读图；脚本做不到——请尽量贴文字。
2. **自检**：在仓库内运行：

```bash
bash setup-doctor/scripts/doctor.sh --tool all
# 或按要装的工具：claude-desktop | claude-code | codex | deepseek-harness | hyperframes
```

脚本只读不改。Node 版本按工具分别判断：Claude Code（npm）22+、HyperFrames 22+、DeepSeek Harness 以官方文档为准（当前升级说明写 24.9+）。人话报告会写清是哪个工具的要求。

3. **对报错库**：用关键句匹配 `errors/`；匹配不上就说「库里没有」，引导用 issue 模板投稿，不猜。
4. **输出**：人话解释 + Mac 步骤 + 出处链接。
5. **讲理由**：说明为什么先跑自检或为什么不能提供绕过方法。

## 官方最低要求（摘录）

- Claude Code：macOS 13.0+、4 GB 内存 — [setup](https://code.claude.com/docs/en/setup)
- Claude 桌面版 Skills：上传 zip 时顶层必须是技能文件夹 — [how-to](https://claude.com/docs/skills/how-to)
- DeepSeek Harness：Node.js 以官方 engines / 升级说明为准（当前文档写 24.9+）— [Node 24 升级说明](https://raw.githubusercontent.com/deepseek-ai/deepseek-harness/master/docs/upgrade-guide/v0.2.1-rc.2/node-24/guide.md)

## 待 Mac 实测

- 报错库各条在本机的复现记录（见各 `errors/*.md` 的「实测记录」字段）
- Claude 桌面版上传本仓库 skill zip 后的触发情况

## 读哪些文件

- `errors/*.md`：报错库
- `references/update-flow.md`：更新流程
