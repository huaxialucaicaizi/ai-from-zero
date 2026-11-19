# #3 含 EACCES 的 npm 全局安装权限报错

| 字段 | 内容 |
| --- | --- |
| 报错原文 / 现象 | 含 EACCES 的 npm 全局安装权限报错 |
| 平台 | Mac |
| 人话解释 | 没有权限往系统目录写文件。 |
| 出处 | https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally/ |
| 实测记录 | 待 Mac 实测 |

## Mac 修复步骤

1. 按 npm 官方文档改用权限更安全的全局目录或包管理方式
2. 避免随意 `sudo npm`（除非你清楚风险）

## 备注

地区/账号限制类问题只给官方支持名单与条款，不提供任何绕过方法。
