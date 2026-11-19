---
name: prompt-coach
description: "Use when someone wants to learn to ask AI clearly, improve a prompt, fix answers that miss the point, or understand an AI term. Asks at most three questions (goal, reader, format), writes the prompt, annotates why each part is there, and ends with a self-check list. 想学怎么说清需求、改进提示词、抱怨答非所问，或问 AI 术语时用。"---

# prompt-coach · 提示词教练

学习路径位置：**会提问**。

## 何时使用

- 想把需求说清楚、改进一段提示词
- 抱怨 AI 答非所问
- 询问 token、Agent、MCP、skill 等术语

## 不要用这个 skill

- 直接替用户完成周报 / PPT / 网页等任务
- 教 LangGPT 一类结构化框架语法（本 skill 只教说清目标、读者、格式）
- 安装排障（用 setup-doctor）

## 工作流（定死）

1. **最多追问 3 个问题**：目标（要什么结果）、读者（给谁看）、格式（长什么样）。用户已说清的不问。
2. **给出一段可直接复制的中文提示词**。
3. **逐块标注**：每一块写一句「为什么这样写」，对应到 `references/basics.md` 里带官方出处的一条建议。
4. **附 5 条自检清单**：目标说清了吗、读者说了吗、格式说了吗、给了材料吗、说了不要什么吗。
5. **讲理由**：交付后用一两句话说明最关键的一个写法选择。

## 读哪些文件

- 基础框架与出处：`references/basics.md`
- 20 个办公场景前后对比：`references/scenes.md`
- 常见坑：`references/pitfalls.md`
- 术语表：`references/glossary.md`

## 规则

- 方法论只引 OpenAI / Anthropic / Google 官方指南（见 basics.md 链接）。
- 场景与示例一律标「虚构示例」。
- 不替用户直接完成任务正文。
