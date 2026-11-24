# #22 DeepSeek Harness / `npx @deepseek-ai/dsh`：Node 版本过旧装不上或起不来

| 字段 | 内容 |
| --- | --- |
| 报错原文 / 现象 | DeepSeek Harness / `npx @deepseek-ai/dsh`：Node 版本过旧装不上或起不来 |
| 平台 | DeepSeek Harness |
| 人话解释 | 官方升级说明要求 Node.js 24.9+（以当时文档为准）；先 `node --version` 再装。 |
| 出处 | https://raw.githubusercontent.com/deepseek-ai/deepseek-harness/master/docs/upgrade-guide/v0.2.1-rc.2/node-24/guide.md |
| 实测记录 | 待 Mac 实测 |

## Mac 修复步骤

1. `node --version`
2. 升级到文档要求的版本后再 `npx @deepseek-ai/dsh`
3. 以官方 upgrade guide 为准

## 备注

地区/账号限制类问题只给官方支持名单与条款，不提供任何绕过方法。
