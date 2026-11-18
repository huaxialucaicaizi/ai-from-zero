# ai-from-zero

零基础学 AI 的开源 skill 仓库：一个仓库，6 个 skill。中文场景、讲清为什么、结果可核对。

**目前仅支持 Mac**（需要装环境或跑脚本的部分）。许可证：[Apache-2.0](./LICENSE)。

作者：华夏路菜菜子：前大厂 AI 产品增长，现 AI 创业者

---

## 先这样用（首推）

不需要脚本的 skill，**优先复制 CI 生成的单文件版**，粘贴进任意 AI 对话：

| skill | 单文件版 |
| --- | --- |
| ai-sources | [`dist/single-file/ai-sources.md`](./dist/single-file/ai-sources.md) |
| ai-for-my-job | [`dist/single-file/ai-for-my-job.md`](./dist/single-file/ai-for-my-job.md) |
| prompt-coach | [`dist/single-file/prompt-coach.md`](./dist/single-file/prompt-coach.md) |
| skill-maker | [`dist/single-file/skill-maker.md`](./dist/single-file/skill-maker.md) |

本地生成：

```bash
python3 scripts/build_single_file.py
```

`setup-doctor`、`first-build` 需要本机环境或写文件能力，请按下方安装到支持的工具。

---

## 学习路径

```text
知道看什么 → 会提问 → 装上工具 → 做出作品 → 用进工作 → 做自己的 skill
   ai-sources   prompt-coach  setup-doctor  first-build  ai-for-my-job   skill-maker
```

详细说明见 [`docs/learning-path.md`](./docs/learning-path.md)。  
不知道从哪开始：先告诉 AI 你的职业，走 `ai-for-my-job`（第二入口）。

| skill | 完成度 | 一句话 |
| --- | --- | --- |
| [ai-for-my-job](./ai-for-my-job/) | 完整 | 岗位 → 3 个先试场景 + 提示词 |
| [prompt-coach](./prompt-coach/) | 完整 | 最多 3 问，写出提示词并讲为什么 |
| [ai-sources](./ai-sources/) | 完整 | 官方一手源 + 课程避坑标准 |
| [setup-doctor](./setup-doctor/) | 完整 | Mac 自检 + 报错库 |
| [first-build](./first-build/) | v0.1 骨架 | 一句话做单文件作品 |
| [skill-maker](./skill-maker/) | v0.1 骨架 | 把提示词打成 skill |

每个 skill 交付结果时，都会用一两句话说明关键选择的理由。

---

## 安装到主流 agent（Mac）

| 工具 | 安装（Mac） | skill 放哪 | 官方链接 |
| --- | --- | --- | --- |
| Claude Code | 推荐 `curl -fsSL https://claude.ai/install.sh \| bash`；或 `brew install --cask claude-code`。要求 macOS 13.0+、4 GB+ RAM | 个人：`~/.claude/skills/<name>/SKILL.md`；项目：`.claude/skills/<name>/SKILL.md` | [安装](https://code.claude.com/docs/en/setup) · [Skills](https://code.claude.com/docs/en/skills) |
| Codex | `curl -fsSL https://chatgpt.com/codex/install.sh \| sh` | 用户：`$HOME/.agents/skills`；仓库：`.agents/skills` | [CLI](https://learn.chatgpt.com/docs/codex/cli) · [Skills](https://learn.chatgpt.com/docs/build-skills) |
| WorkBuddy | 官网下载 Mac `.dmg`，拖入「应用程序」；要求 macOS 12+ | 项目级：工作区 `.codebuddy/skills/<name>/`（官方项目/Skills 文档已写明）。用户级精确路径未在本次打开的官方页写死 → **待核实**，确认前本文不写死用户级路径 | [Mac 安装](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Installation-Mac-Guide) · [技能](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills) · [IDE Skills 结构](https://www.workbuddy.ai/docs/ide/Features/Skills) |
| DeepSeek Harness | 先装 Node.js（当前升级说明要求 **Node.js 24.9+**，以仓库最新文档为准），然后 `npx @deepseek-ai/dsh web` | 项目：`<git-root>/.dsh/skills/<name>/SKILL.md` 或 `.agents/skills/`；用户：`~/.dsh/skills/` 或 `~/.agents/skills/` | [README](https://github.com/deepseek-ai/deepseek-harness/blob/HEAD/README.md) · [skills](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/subsystems/skills.md) |

各工具触发适配测试结果：见 `tests/triggers/`（当前均为 **待 Mac 实测**）。

---

## setup-doctor 快速自检

```bash
bash setup-doctor/scripts/doctor.sh --tool all
```

Node 版本按工具分别判断（人话报告会写明是哪个工具的要求）：

- Claude Code 用 npm 安装：22+
- HyperFrames：22+
- DeepSeek Harness：以官方文档为准（当前升级说明 24.9+）

报错库更新流程见 [`setup-doctor/references/update-flow.md`](./setup-doctor/references/update-flow.md)。截图识错依赖你使用的 AI 能读图；脚本本身只处理环境检查。

---

## 触发测试

每个 skill 在 [`tests/triggers/`](./tests/triggers/) 有 10 句应触发 + 10 句不应触发清单。

---

## 开发与 CI

```bash
pip install pyyaml
python3 scripts/validate_repo.py
python3 scripts/build_single_file.py
```

CI（GitHub Actions）会：校验 frontmatter / `agents/openai.yaml` / 虚构示例 / 触发清单 / 禁用词（路径写法 `.codebuddy/` 已白名单）/ 报错库「出处」字段；生成单文件版；在 **macOS** runner 上跑一遍 `doctor.sh`。

---

## 字体

若作品需要中文字体，只用免费商用字体，例如：

- [思源黑体（OFL 1.1）](https://github.com/adobe-fonts/source-han-sans)
- [霞鹜文楷（OFL 1.1）](https://github.com/lxgw/LxgwWenKai)

---

## English

**ai-from-zero** is a multi-skill repo for absolute beginners: trusted sources, prompt coaching, Mac setup help, first builds, job scenarios, and making your own skills.

- License: Apache-2.0
- Platform: **Mac only** in v1 for scripted setup
- Prefer the CI-built **single-file** Markdown under `dist/single-file/` for paste-into-any-chat skills
- Author line: 华夏路菜菜子：前大厂 AI 产品增长，现 AI 创业者

See the learning path above. Anything marked **待 Mac 实测** or **待核实** has not been claimed as verified on Mac yet.
