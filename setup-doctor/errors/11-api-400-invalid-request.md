# #11 400 invalid_request_error（即常说的 api 400）

| 字段 | 内容 |
| --- | --- |
| 报错原文 / 现象 | 400 invalid_request_error（即常说的 api 400） |
| 平台 | 通用 |
| 人话解释 | 请求格式或内容有问题；达到自设花费上限也会返回 400。 |
| 出处 | https://platform.claude.com/docs/en/api/errors |
| 实测记录 | 待 Mac 实测 |

## Mac 修复步骤

1. 对照官方 API errors 页检查请求
2. 检查是否触发花费上限

## 备注

地区/账号限制类问题只给官方支持名单与条款，不提供任何绕过方法。
