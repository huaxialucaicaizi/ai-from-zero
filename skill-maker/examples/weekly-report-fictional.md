# 虚构示例：用 skill-maker 打包「写周报」

> 本页全部为虚构示例。

## 用户原话

> 把我写周报常用的那段提示词做成 skill。

## 对比前

每次把长提示词复制进对话框，容易漏约束，也不好分享给同事。

## 对比后（skill-maker）

1. name：`weekly-report-helper`
2. description：写清「给领导写周报、用户会粘贴要点」
3. 生成 `examples/weekly-report-skill/SKILL.md`
4. 打包：`zip -r weekly-report-helper.zip weekly-report-helper/`
5. 在 Claude 桌面版 Customize > Skills 上传并打开开关
6. 用 5 句该触发、5 句不该触发自测

完整 Mac 适配测试：**待 Mac 实测**。

**理由：** 把「何时用」写进 description，比把提示词塞进正文更重要，否则 skill 装了也不触发。
