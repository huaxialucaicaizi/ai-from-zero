# #18 error: externally-managed-environment（pip 安装时）

| 字段 | 内容 |
| --- | --- |
| 报错原文 / 现象 | error: externally-managed-environment（pip 安装时） |
| 平台 | Mac |
| 人话解释 | 系统自带的 Python 不让直接装包，要用虚拟环境。 |
| 出处 | https://packaging.python.org/en/latest/specifications/externally-managed-environments/ |
| 实测记录 | 待 Mac 实测 |

## Mac 修复步骤

1. 创建 venv 后再 pip install
2. 不要强行破坏系统 Python

## 备注

地区/账号限制类问题只给官方支持名单与条款，不提供任何绕过方法。
