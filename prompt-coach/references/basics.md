# 提示词基础（只引官方指南）

每条建议对应至少一家官方文档。查不到的写法不要编。

## 五块积木

| 积木 | 人话 | 为什么要有 | 出处 |
| --- | --- | --- | --- |
| 角色 | 你希望 AI 以什么身份回答 | 缩小口吻与专业边界 | [OpenAI Prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering) |
| 任务 | 要完成的具体动作 | 避免空泛「帮帮我」 | [Anthropic Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) |
| 背景 | 材料、约束、上下文 | 模型只能根据你给的信息推理 | [OpenAI GPT-4.1 prompting guide](https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide) |
| 格式 | 篇幅、结构、标题、表格等 | 降低答非所问 | [Google prompting strategies](https://aistudio.google.com/docs/prompting-strategies) |
| 示例 | 好/坏样例（可选） | 用样例对齐风格比形容词更稳 | [Anthropic interactive tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) |

办公场景可再参考：[Gemini 办公提示词指南](https://workspace.google.com/learning/content/gemini-prompt-guide)。  
企业侧设计导读：[Introduction to prompt design](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/introduction-prompt-design)。

## 和 LangGPT 的区别

[LangGPT](https://github.com/langgptai/LangGPT) 教结构化框架写法。本 skill **不教框架语法**，只帮零基础用户把目标、读者、格式说清楚。

## 教练输出模板

```text
【可复制提示词】
...

【逐块说明】
- 角色：…（对应 basics：…）
- 任务：…
- 背景：…
- 格式：…
- 示例/约束：…

【自检】
1. 目标说清了吗？
2. 读者说了吗？
3. 格式说了吗？
4. 给了材料吗？
5. 说了不要什么吗？
```
