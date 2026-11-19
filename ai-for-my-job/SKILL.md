---
name: ai-for-my-job
description: "Use when someone names their job or role and asks what AI can do for it. Returns the three scenarios worth trying first, each with a copy-ready prompt and a pointer to the matching office skill. Does not perform the task itself. 用户说出职业或岗位、问 AI 能帮这个岗位做什么时用。"---

# ai-for-my-job · 我的岗位能用 AI 做什么

学习路径位置：**用进工作**（也是第二入口：不知道从哪开始时，先说自己的职业）。

## 何时使用

- 用户说出职业 / 岗位，问 AI 能做什么、先从哪开始
- 想按岗位拿到 3 个高频、低风险、好核对的场景和可复制提示词

## 不要用这个 skill

- 直接代写周报、改简历、分析某份 Excel、做网页等具体任务（应指向对应 skill 或直接完成任务的能力）
- 安装排障、信息源推荐、提示词方法论教学（分别用 setup-doctor / ai-sources / prompt-coach）

## 工作流

1. **收下输入**：职业（可选：每天最花时间的一件事）。
2. **对上岗位**：能对上 `references/jobs.md` 里 10 个岗位之一就直接用；对不上就追问一句「你每天最花时间的三件事」，再按事情归类。
3. **挑 3 个场景**：标准为高频、省时明显、出错风险低、结果好核对。
4. **输出**：每个场景 = 一句话说明 + 可复制提示词 + 「想做得更好，用 xx skill」。尚未上线的办公 skill 标「规划中」。
5. **讲理由**：交付后用一两句话说明为什么先推这 3 个（例如「都是高频、出错后果可控、结果肉眼能核对」）。

## 读哪些文件

- 岗位与场景表：`references/jobs.md`

## 规则

- 不编造「平均省时 X 小时」等无出处数字。
- 不写真实个人案例；示例一律虚构。
- 不替用户完成具体任务正文。
