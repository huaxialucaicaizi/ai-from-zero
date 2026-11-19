<a id="top"></a>

<div align="center">

# AI From Zero · 零基础学 AI

**零基础学 AI 的开源 skill 仓库：从知道该关注哪些博主、科技媒体和课程，到学会写提示词、让「安装医生」帮你排除安装 AI 产品的故障，再到做出第一个作品、把 AI 用进自己的工作、做出自己的 skill，一步步带你从 0 用起 AI。**<br>
Learn AI from zero, step by step: find the right creators, tech media, and courses to follow, learn to write prompts, let the setup doctor fix problems installing AI products, build your first project, use AI in your own job, and make your own skill.

[![CI](https://github.com/huaxialucaicaizi/ai-from-zero/actions/workflows/ci.yml/badge.svg)](https://github.com/huaxialucaicaizi/ai-from-zero/actions/workflows/ci.yml)
[![Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](./LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/huaxialucaicaizi/ai-from-zero?style=social)](https://github.com/huaxialucaicaizi/ai-from-zero)

[中文](#zh) | [English](#en)

</div>

---

<a id="zh"></a>

## 中文

### 目录
- [一句话介绍](#zh-intro)
- [学习路径](#zh-path)
- [六个 skill](#zh-skills)
- [单文件版（首推）](#zh-single)
- [安装到主流工具（目前仅支持 Mac）](#zh-install)
- [setup-doctor 自检](#zh-doctor)
- [触发测试与 CI](#zh-ci)
- [目录结构](#zh-structure)
- [贡献](#zh-contrib)
- [作者](#zh-author)
- [许可](#zh-license)

<a id="zh-intro"></a>
### 一句话介绍

**零基础学 AI 的开源 skill 仓库：从知道该关注哪些博主、科技媒体和课程，到学会写提示词、让「安装医生」帮你排除安装 AI 产品的故障，再到做出第一个作品、把 AI 用进自己的工作、做出自己的 skill，一步步带你从 0 用起 AI。**

特点：一个仓库里有 6 个 skill，面向中文工作场景，输出时讲清为什么，结果尽量可核对。不需要脚本的 skill 可以先复制单文件版，粘贴进任意 AI 对话。

**痛点**
- 不知道从哪学起，也不知道哪些信息源靠谱
- 会聊天，但提示词说不清，结果对不上
- 装工具时报错看不懂，skill 放了也不触发
- 想把 AI 用进本职工作，却只有空泛建议

需要装环境或跑脚本的部分，**目前仅支持 Mac**。

<a id="zh-path"></a>
### 学习路径

```text
知道看什么 → 会提问 → 装上工具 → 做出作品 → 用进工作 → 做自己的 skill
   ai-sources   prompt-coach  setup-doctor  first-build  ai-for-my-job   skill-maker
```

更细的说明见 [`docs/learning-path.md`](./docs/learning-path.md)。  
不知道从哪开始：先说出自己的职业，走 **ai-for-my-job · 岗位场景**（第二入口）。

办公向的演示文稿、数据分析、设计、视频挂在「用进工作」之下，分仓库推进；本仓库里尚未上线的指向标「规划中」。

<a id="zh-skills"></a>
### 六个 skill

| skill | 完成度 | 对你有什么帮助 | 一句话 |
| --- | --- | --- | --- |
| [**ai-for-my-job · 岗位场景**](./ai-for-my-job/) | 完整 | 不知道 AI 能帮自己的工作做什么，它帮你找到马上能用上的场景。 | 说出职业，拿到 3 个先试场景和可复制提示词 |
| [**prompt-coach · 提问教练**](./prompt-coach/) | 完整 | AI 总答非所问，它教你把问题问清楚，拿到能用的答案。 | 最多追问 3 问，写出提示词并逐块说明为什么 |
| [**ai-sources · 信息源导航**](./ai-sources/) | 完整 | 信息太多不知道信谁，它帮你找到靠谱的一手消息，避开割韭菜的课。 | 官方一手源 + 课程避坑判断标准 |
| [**setup-doctor · 安装排障**](./setup-doctor/) | 完整 | 装 AI 产品卡住了，它帮你查出原因、按官方方法修好。 | Mac 自检 + 报错库（含官方出处） |
| [**first-build · 第一个作品**](./first-build/) | v0.1 骨架 | 没写过代码也能做出第一个自己的小网页，建立信心。 | 一句话做可双击打开的单文件网页 |
| [**skill-maker · 做自己的 skill**](./skill-maker/) | v0.1 骨架 | 常用的提示词不用每次重写，打包成自己的 skill 反复用。 | 把常用提示词打成可安装的 skill |

每个 skill 交付结果时，都会用一两句话说明关键选择的理由。示例一律标明虚构示例。

<a id="zh-single"></a>
### 单文件版（首推）

不需要脚本的 skill，**优先复制 CI 生成的单文件版**（由 `SKILL.md` 与 `references/` 合成），粘贴进任意 AI 对话：

| skill | 单文件版 |
| --- | --- |
| **ai-sources · 信息源导航** | [`dist/single-file/ai-sources.md`](./dist/single-file/ai-sources.md) |
| **ai-for-my-job · 岗位场景** | [`dist/single-file/ai-for-my-job.md`](./dist/single-file/ai-for-my-job.md) |
| **prompt-coach · 提问教练** | [`dist/single-file/prompt-coach.md`](./dist/single-file/prompt-coach.md) |
| **skill-maker · 做自己的 skill** | [`dist/single-file/skill-maker.md`](./dist/single-file/skill-maker.md) |

本地生成：

```bash
python3 scripts/build_single_file.py
```

**setup-doctor · 安装排障**、**first-build · 第一个作品** 需要本机环境或写文件能力，请按下一节安装到支持的工具。

<a id="zh-install"></a>
### 安装到主流工具（目前仅支持 Mac）

| 工具 | 安装（Mac） | skill 放哪 | 官方链接 |
| --- | --- | --- | --- |
| Claude Code | 推荐 `curl -fsSL https://claude.ai/install.sh \| bash`；或 `brew install --cask claude-code`。要求 macOS 13.0+、内存 4 GB 及以上 | 个人：`~/.claude/skills/<name>/SKILL.md`；项目：`.claude/skills/<name>/SKILL.md` | [安装](https://code.claude.com/docs/en/setup) · [Skills](https://code.claude.com/docs/en/skills) |
| Codex | `curl -fsSL https://chatgpt.com/codex/install.sh \| sh` | 用户：`$HOME/.agents/skills`；仓库：`.agents/skills` | [CLI](https://learn.chatgpt.com/docs/codex/cli) · [Skills](https://learn.chatgpt.com/docs/build-skills) |
| WorkBuddy | 官网下载 Mac 安装包，拖入「应用程序」；要求 macOS 12+ | 项目级：工作区 `.codebuddy/skills/<name>/`（官方项目文档已写明）。用户级精确路径 **待核实**，确认前本文不写死 | [Mac 安装](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Installation-Mac-Guide) · [技能](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills) · [IDE Skills 结构](https://www.workbuddy.ai/docs/ide/Features/Skills) |
| DeepSeek Harness | 先装 Node.js（当前升级说明要求 Node.js 24.9 及以上，以仓库最新文档为准），然后 `npx @deepseek-ai/dsh web` | 项目：`<git-root>/.dsh/skills/<name>/SKILL.md` 或 `.agents/skills/`；用户：`~/.dsh/skills/` 或 `~/.agents/skills/` | [说明](https://github.com/deepseek-ai/deepseek-harness/blob/HEAD/README.md) · [skills](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/subsystems/skills.md) |

各工具触发适配测试结果见 [`tests/triggers/`](./tests/triggers/)（当前均为 **待 Mac 实测**）。

<a id="zh-doctor"></a>
### setup-doctor 自检

```bash
bash setup-doctor/scripts/doctor.sh --tool all
```

脚本只读不改。Node 版本按你要装的工具分别判断，人话报告会写明是哪个工具的要求：

- Claude Code 用 npm 安装：22 及以上
- HyperFrames：22 及以上
- DeepSeek Harness：以官方文档为准（当前升级说明为 24.9 及以上）

报错库更新流程见 [`setup-doctor/references/update-flow.md`](./setup-doctor/references/update-flow.md)。用截图识别报错，依赖你使用的 AI 能读图；脚本本身只做环境检查。

<a id="zh-ci"></a>
### 触发测试与 CI

每个 skill 在 [`tests/triggers/`](./tests/triggers/) 有 10 句应触发、10 句不应触发清单。

本地轻量检查：

```bash
pip install pyyaml
python3 scripts/validate_repo.py
python3 scripts/build_single_file.py
```

CI 会校验 frontmatter、`agents/openai.yaml`、虚构示例、触发清单、禁用词（路径写法 `.codebuddy/` 已白名单）、报错库「出处」字段；生成单文件版；并在 macOS 运行器上跑一遍 `doctor.sh`。

若作品需要中文字体，只用免费商用字体，例如 [思源黑体](https://github.com/adobe-fonts/source-han-sans)、[霞鹜文楷](https://github.com/lxgw/LxgwWenKai)。

<a id="zh-structure"></a>
### 目录结构

```text
ai-from-zero/
├── README.md
├── LICENSE                          # Apache-2.0
├── docs/learning-path.md
├── dist/single-file/                # CI 生成的单文件版
├── ai-sources/
├── ai-for-my-job/
├── prompt-coach/
├── setup-doctor/
│   ├── scripts/doctor.sh
│   └── errors/                      # 报错库（每条含出处）
├── first-build/                     # v0.1 骨架
├── skill-maker/                     # v0.1 骨架
├── tests/triggers/                  # 触发测试清单
├── scripts/
│   ├── validate_repo.py
│   └── build_single_file.py
└── .github/workflows/ci.yml
```

<a id="zh-contrib"></a>
### 贡献

见 [`CONTRIBUTING.md`](./CONTRIBUTING.md)。报错库投稿、信息源投稿请用 [Issue 模板](./.github/ISSUE_TEMPLATE/)。提交前请运行上面的校验命令。

<a id="zh-author"></a>
### 作者

**华夏路菜菜子**：前大厂 AI 产品增长，现 AI 创业者。

- GitHub：[@huaxialucaicaizi](https://github.com/huaxialucaicaizi)

<a id="zh-license"></a>
### 许可

本项目采用 [Apache-2.0](./LICENSE) 许可证。

[↑ 返回顶部](#top)

---

<a id="en"></a>

## English

### Contents
- [In one sentence](#en-intro)
- [Learning path](#en-path)
- [The six skills](#en-skills)
- [Single-file edition (recommended first)](#en-single)
- [Install into common agents (Mac only for now)](#en-install)
- [setup-doctor self-check](#en-doctor)
- [Trigger tests and CI](#en-ci)
- [Directory structure](#en-structure)
- [Contributing](#en-contrib)
- [Author](#en-author)
- [License](#en-license)

<a id="en-intro"></a>
### In one sentence

**Learn AI from zero, step by step: find the right creators, tech media, and courses to follow, learn to write prompts, let the setup doctor fix problems installing AI products, build your first project, use AI in your own job, and make your own skill.**

What you get: six skills in one repo, Chinese work scenarios, plain-language reasons for key choices, and results you can check. Skills that need no scripts can start as a single pasted Markdown file in any AI chat.

**Pain points**
- Unclear where to start, or which sources to trust
- Chat works, but prompts are vague and answers miss the point
- Install errors are hard to read; skills sit unused because they never trigger
- Job use stays generic advice instead of concrete next steps

Parts that install tools or run scripts are **Mac only** in this first version.

<a id="en-path"></a>
### Learning path

```text
know what to read → ask clearly → install tools → ship a first build → use at work → make your own skill
     ai-sources      prompt-coach   setup-doctor     first-build      ai-for-my-job      skill-maker
```

Details: [`docs/learning-path.md`](./docs/learning-path.md).  
If you do not know where to start, name your job and use **ai-for-my-job · job scenarios** (second entry).

Office skills for decks, data, design, and video hang under “use at work” in other repos; pointers here say “planned” until those repos ship.

<a id="en-skills"></a>
### The six skills

| skill | Status | How it helps you | One line |
| --- | --- | --- | --- |
| [**ai-for-my-job · job scenarios**](./ai-for-my-job/) | complete | Not sure what AI can do for your job? It finds scenarios you can use right away. | Name a role; get three first scenarios and copy-ready prompts |
| [**prompt-coach · prompt coach**](./prompt-coach/) | complete | AI keeps missing the point? It teaches you to ask clearly and get answers you can use. | Ask at most three questions; write a prompt and explain each part |
| [**ai-sources · source guide**](./ai-sources/) | complete | Too much noise to know whom to trust? It points you to reliable first-hand sources and helps you avoid overhyped courses. | First-party official sources plus a course red-flag checklist |
| [**setup-doctor · setup doctor**](./setup-doctor/) | complete | Stuck installing an AI product? It finds the cause and fixes it the official way. | Mac self-check plus an error library with official sources |
| [**first-build · first build**](./first-build/) | v0.1 skeleton | Never coded? Build your first small web page anyway and gain confidence. | One sentence to a single-file page you can open locally |
| [**skill-maker · skill maker**](./skill-maker/) | v0.1 skeleton | Stop rewriting the same prompts; package them into your own reusable skill. | Turn a reused prompt into an installable skill |

Every delivery includes a short reason for the key choice. Examples are marked as fictional examples.

<a id="en-single"></a>
### Single-file edition (recommended first)

For skills without scripts, **prefer the CI-built single file** (`SKILL.md` plus `references/`), then paste it into any AI chat:

| skill | Single file |
| --- | --- |
| **ai-sources · source guide** | [`dist/single-file/ai-sources.md`](./dist/single-file/ai-sources.md) |
| **ai-for-my-job · job scenarios** | [`dist/single-file/ai-for-my-job.md`](./dist/single-file/ai-for-my-job.md) |
| **prompt-coach · prompt coach** | [`dist/single-file/prompt-coach.md`](./dist/single-file/prompt-coach.md) |
| **skill-maker · skill maker** | [`dist/single-file/skill-maker.md`](./dist/single-file/skill-maker.md) |

Generate locally:

```bash
python3 scripts/build_single_file.py
```

**setup-doctor · setup doctor** and **first-build · first build** need a local environment or file write access; install them with the table below.

<a id="en-install"></a>
### Install into common agents (Mac only for now)

| Tool | Install (Mac) | Where to put the skill | Official links |
| --- | --- | --- | --- |
| Claude Code | Preferred: `curl -fsSL https://claude.ai/install.sh \| bash`; or `brew install --cask claude-code`. Requires macOS 13.0+ and 4 GB+ RAM | User: `~/.claude/skills/<name>/SKILL.md`; project: `.claude/skills/<name>/SKILL.md` | [Setup](https://code.claude.com/docs/en/setup) · [Skills](https://code.claude.com/docs/en/skills) |
| Codex | `curl -fsSL https://chatgpt.com/codex/install.sh \| sh` | User: `$HOME/.agents/skills`; repo: `.agents/skills` | [CLI](https://learn.chatgpt.com/docs/codex/cli) · [Skills](https://learn.chatgpt.com/docs/build-skills) |
| WorkBuddy | Download the Mac installer from the official site and drag it into Applications; requires macOS 12+ | Project-level: workspace `.codebuddy/skills/<name>/` (documented). Exact user-level path is **To be verified**; this README does not invent one | [Mac install](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Installation-Mac-Guide) · [Skills](https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills) · [IDE Skills layout](https://www.workbuddy.ai/docs/ide/Features/Skills) |
| DeepSeek Harness | Install Node.js first (current upgrade guide: Node.js 24.9+; follow the latest docs), then `npx @deepseek-ai/dsh web` | Project: `<git-root>/.dsh/skills/<name>/SKILL.md` or `.agents/skills/`; user: `~/.dsh/skills/` or `~/.agents/skills/` | [README](https://github.com/deepseek-ai/deepseek-harness/blob/HEAD/README.md) · [skills](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/subsystems/skills.md) |

Trigger adaptation results live under [`tests/triggers/`](./tests/triggers/) (all currently **To be tested on Mac**).

<a id="en-doctor"></a>
### setup-doctor self-check

```bash
bash setup-doctor/scripts/doctor.sh --tool all
```

The script is read-only. Node version checks differ by tool; the plain-language report names which tool set the bar:

- Claude Code via npm: 22+
- HyperFrames: 22+
- DeepSeek Harness: follow the official docs (current upgrade guide: 24.9+)

Error-library update flow: [`setup-doctor/references/update-flow.md`](./setup-doctor/references/update-flow.md). Reading error screenshots needs an AI that can see images; the script only checks the environment.

<a id="en-ci"></a>
### Trigger tests and CI

Each skill has 10 should-trigger and 10 should-not-trigger lines under [`tests/triggers/`](./tests/triggers/).

Local light checks:

```bash
pip install pyyaml
python3 scripts/validate_repo.py
python3 scripts/build_single_file.py
```

CI validates frontmatter, `agents/openai.yaml`, fictional examples, trigger lists, banned words (with a whitelist for the `.codebuddy/` path spelling), non-empty error sources, builds single-file editions, and runs `doctor.sh` once on a macOS runner.

For Chinese fonts in builds, use free commercial fonts such as [Source Han Sans](https://github.com/adobe-fonts/source-han-sans) and [LXGW WenKai](https://github.com/lxgw/LxgwWenKai).

<a id="en-structure"></a>
### Directory structure

```text
ai-from-zero/
├── README.md
├── LICENSE                          # Apache-2.0
├── docs/learning-path.md
├── dist/single-file/                # CI-built paste editions
├── ai-sources/
├── ai-for-my-job/
├── prompt-coach/
├── setup-doctor/
│   ├── scripts/doctor.sh
│   └── errors/                      # error library (each entry has a source)
├── first-build/                     # v0.1 skeleton
├── skill-maker/                     # v0.1 skeleton
├── tests/triggers/                  # trigger checklists
├── scripts/
│   ├── validate_repo.py
│   └── build_single_file.py
└── .github/workflows/ci.yml
```

<a id="en-contrib"></a>
### Contributing

See [`CONTRIBUTING.md`](./CONTRIBUTING.md). Use the [issue templates](./.github/ISSUE_TEMPLATE/) for error-library and source submissions. Run the validation commands above before a PR.

<a id="en-author"></a>
### Author

**华夏路菜菜子 (huaxialucaicaizi)**: former AI product growth lead at major Chinese tech companies, now an AI founder.

- GitHub: [@huaxialucaicaizi](https://github.com/huaxialucaicaizi)

<a id="en-license"></a>
### License

This project is licensed under [Apache-2.0](./LICENSE).

[↑ Back to top](#top)
