# #20 Claude 桌面版：上传了 zip 但 Skills 里不出现 / 无法识别

| 字段 | 内容 |
| --- | --- |
| 报错原文 / 现象 | 上传自定义 skill 的 zip 后，Customize > Skills 里看不到，或提示结构不对 |
| 平台 | Claude 桌面版 / claude.ai |
| 人话解释 | zip 里必须是「技能文件夹/SKILL.md」，不能把 SKILL.md 直接放在压缩包根目录。 |
| 出处 | https://claude.com/docs/skills/how-to |
| 实测记录 | 待 Mac 实测 |

## Mac 修复步骤

1. 确认文件夹名与 `SKILL.md` 里的 `name` 一致。
2. 在父目录打包：`zip -r <name>.zip <name>/`（压缩的是文件夹，不是里面的零散文件）。
3. 用 `unzip -l <name>.zip` 检查：每条路径应以 `<name>/` 开头。
4. 重新在 Customize > Skills 里上传，并打开开关。

## 备注

地区/账号限制类问题只给官方支持名单与条款，不提供任何绕过方法。
