# Contributing / 参与贡献

感谢你愿意改进 **ai-from-zero**。

## 怎么改

1. Fork 并新建分支。
2. 只改一个明确主题（一个 skill、一条报错、一个信息源等）。
3. 示例必须标注「虚构示例」，不写真实个人经历。
4. 引用须附官方链接；查不到写「待核实」，不要编造。
5. 本地跑轻量检查：

```bash
pip install pyyaml
python3 scripts/validate_repo.py
python3 scripts/build_single_file.py
```

6. 开 PR，说明改了什么、如何自测。

## 投稿模板

- 报错库：用 Issue 模板「报错库投稿」
- 信息源：用 Issue 模板「信息源投稿」

## 红线

- 不写个人履历/案例（作者介绍仅保留 README 固定一句）
- 不加第三方推广徽章或引流链接
- 正文不提禁用产品名（CI 会检查）；路径白名单仅允许 `.codebuddy/` 这种官方目录写法
