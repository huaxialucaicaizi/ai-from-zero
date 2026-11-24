# #21 DeepSeek Harness：把 SKILL.md 放在多层嵌套目录里，会话里看不到

| 字段 | 内容 |
| --- | --- |
| 报错原文 / 现象 | DeepSeek Harness：把 SKILL.md 放在多层嵌套目录里，会话里看不到 |
| 平台 | DeepSeek Harness |
| 人话解释 | 本地 provider 只接受扫描根下的目录 bundle 或扁平 `.md`，不递归发现嵌套 `**/SKILL.md`。 |
| 出处 | https://raw.githubusercontent.com/deepseek-ai/deepseek-harness/master/docs/subsystems/skills.md |
| 实测记录 | 待 Mac 实测 |

## Mac 修复步骤

1. 把 skill 放到文档允许的一层目录
2. 不要深嵌套后指望自动发现

## 备注

地区/账号限制类问题只给官方支持名单与条款，不提供任何绕过方法。
