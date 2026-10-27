# AI 项目页维护

入口为 `/about/`，页面结构：AI-Galaxy 网站项目、Codex Skills、实用工具。

- `src/collections/ai-projects.ts` 保存 Skill 名称、介绍、功能、流程、示范图和仓库地址。
- `src/pages/about.astro` 渲染项目卡片与原生 dialog 示例窗口。
- `src/components/home/ProjectTools.astro` 保留原来的四项工具。
- 中英文文案位于 `src/assets/js/i18n.js`，修改后同步到 `public/assets/js/i18n.js`。

## 仓库状态

直播场景设计链接到真实的 `SJ3199/livestream-scene-skill` 仓库与最新版 Release。安装依赖宿主的生图、读图与本地文件能力，不能只下载技能就独立生图。

拾纹仍为本地 Skill，`repo` 与 `release` 为 `null`，仅展示功能与示范。公开仓库后补充真实 URL，并更新 `local` 与中英文状态说明。不要填写猜测的仓库地址。

## 示范图来源

- AI-Galaxy：复用本站原有的 `public/assets/ai-galaxy-preview.png` 静态封面。
- 直播场景：公开仓库 `docs/assets/crab.jpg`、`fashion.jpg`、`handbag.jpg` 的历史生成示例。
- 拾纹：用户本地 `texture-skill-validation-v15-jpg/rendered-jpg-set` 中已生成的锁屏、密码页、纯壁纸，来自同一组输出。

网站使用压缩后的 WebP 副本（`public/assets/projects/`），不修改示范原文件。示例与功能介绍应同步维护，勿把历史示例写成当前版本的验收结果。

两项 Skill 的示范区共用 `--sample-surface` 背景色，不按项目设置不同底色。图片记录真实宽高，使用按原比例裁切圆角的容器；主卡片保留紧凑介绍，完整工作流程放在示范弹窗中。AI-Galaxy 使用连续背景与渐隐星图，避免左右区域硬分割。

## 本地预览

运行中的作品管理页点击“手动网站预览”后，访问 `http://127.0.0.1:43821/about/`。构建不会发布网站。也可在此仓库运行 `npm run dev`。
