# #10 Unable to connect to API: SSL certificate verification failed (UNABLE_TO_GET_ISSUER_CERT_LOCALLY)

| 字段 | 内容 |
| --- | --- |
| 报错原文 / 现象 | Unable to connect to API: SSL certificate verification failed (UNABLE_TO_GET_ISSUER_CERT_LOCALLY) |
| 平台 | 通用 |
| 人话解释 | 公司网络在中间换了证书，需要 IT 提供证书。 |
| 出处 | https://code.claude.com/docs/en/errors |
| 实测记录 | 待 Mac 实测 |

## Mac 修复步骤

1. 联系公司 IT 获取正确根证书
2. 不要随意关闭 TLS 验证

## 备注

地区/账号限制类问题只给官方支持名单与条款，不提供任何绕过方法。
