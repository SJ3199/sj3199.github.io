# AI Context — Portfolio 项目快速索引

> 此文件为 AI 代理（OpenClaw、Claude Code、Cursor 等）提供项目快速理解和修改指南。

## 一句话概括

基于 Astro 5 的静态作品集网站，含 3 个浏览器端 AI 图片处理工具，部署于 GitHub Pages。

## 项目路径

```
D:\portfolio\
```

## 修改任何文件前的检查清单

- [ ] `src/assets/js/i18n.js` 修改后 → 复制到 `public/assets/js/i18n.js`
- [ ] Astro 组件 `.astro` 修改后 → `npm run build` 验证
- [ ] `.gitignore` 检查 → `/tools/` 仅匹配根目录

## 核心文件索引

### 全局布局 & 配置
| 文件 | 作用 | 修改频率 |
|------|------|----------|
| `src/layouts/Layout.astro` | body/header/footer/i18n 加载 | 低 |
| `src/components/sections/Header.astro` | 导航栏 + 语言/暗色浮动按钮 | 低 |
| `src/components/sections/Footer.astro` | 底栏 + 社交图标 | 低 |
| `src/config/site.js` | SEO、社交链接配置 | 低 |
| `public/assets/js/i18n.js` | **运行时** 中英翻译字典 | 高 |
| `src/assets/js/i18n.js` | i18n 源文件 (**修改后必须同步**) | 高 |

### AI 工具页
| 文件 | 标题 | 核心 CSS 类 |
|------|------|------------|
| `src/pages/tools/compress.astro` | 图片压缩 | `#qualitySlider`, `#formatSelect`, `#maxWidthSelect` |
| `src/pages/tools/convert.astro` | 格式转换 | `#formatBtns .fmt-btn`, `#qualitySlider` |
| `src/pages/tools/resize.astro` | 尺寸调整 | `#resizeWidth`, `#resizeHeight`, `.size-btn`, `#lockRatio` |
| `src/pages/about.astro` | 工具卡片列表 | 3 张 `<a>` 卡片 |

### 工具页共享 JS 模式
```js
// i18n 辅助函数 (每个工具页都需要)
function __t(key, vars) {
  var lang = localStorage.getItem('lang') || 'zh';
  try {
    var t = i18n[lang] || i18n.zh;
    var s = t[key] || key;
    if (vars) { Object.keys(vars).forEach(function(k) { s = s.split('{'+k+'}').join(vars[k]); }); }
    return s;
  } catch(e) { return key; }
}

// 监听语言切换
window.addEventListener('langchange', function() { updatePreviewCount(); });
```

## i18n 翻译 Key 命名规范

```
<tool>-<section>-<field>
```

示例：
- `compress-btn-start` — 压缩页开始按钮
- `convert-faq1-q` — 转换页第一个 FAQ 问题
- `resize-label-quality` — 调整页画质标签
- `tool-download-all` — 通用：批量下载按钮

## 构建 & 部署命令

```bash
# 开发
cd D:\portfolio
npm run dev                # http://localhost:5200

# 构建 (执行前先同步 i18n.js!)
Copy-Item src/assets/js/i18n.js public/assets/js/i18n.js -Force
npx astro build

# 部署 (推送即部署)
git add -A
git commit -m "描述"
git push
```

## 常见错误速查

| 症状 | 原因 | 修复 |
|------|------|------|
| `__t is not defined` | i18n.js 未同步 | `Copy-Item src/assets/js/i18n.js public/assets/js/i18n.js -Force` |
| Build 报 JS 语法错误 | 模板字符串冲突 | 检查 `<script>` 中 `` `${}` `` 是否被 Astro 解析 |
| 页面底栏浮中间 | `mt-auto` 被覆盖 | Footer class 中去掉 `md:mt-48` 等断点类 |
| 工具页未出现在线上 | `.gitignore` 阻止 | `tools/` → `/tools/` |
| `AIAI` 重复文字 | i18n key 与 HTML 硬编码重复 | i18n 值去掉与 HTML 重叠的前缀 |

## 设计规范速记

- 字体：`font-sans`，标题 `text-4xl sm:text-5xl font-bold`
- 描述：`text-sm sm:text-base lg:text-lg text-neutral-700 dark:text-neutral-300`
- 容器：`site-container mx-auto`
- 卡片网格：`max-w-7xl` + `grid-template-columns: repeat(auto-fill, minmax(200px, 1fr))`
- 主色调：`primary` / `primary-light` (Tailwind 配置)
- Features 区：无边框无背景，flex 图标+文字
- FAQ 区：纯文字 `max-w-2xl`
- 社交图标：内联 SVG + `fill="currentColor"` + Tailwind 色值

## 分支策略

- 主分支：`master`（直接推送即部署）
- 还原点：`git log --oneline --grep="AUTO-SNAPSHOT\|RESTORE-POINT" -3`
- 回滚：`git reset --hard <hash>` → `npx astro build` → `git push --force`
