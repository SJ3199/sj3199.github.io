# Portfolio 作品集网站

> 个人设计作品展示 + AI 工具集，基于 [Astro](https://astro.build) 构建，部署于 GitHub Pages。

## 技术栈

| 类别 | 技术 |
|------|------|
| 框架 | [Astro 5](https://astro.build) (SSG 静态生成) |
| 样式 | Tailwind CSS v3 + 自定义 CSS |
| 动画 | AOS (Animate on Scroll) |
| 图标 | Lucide Astro (内联 SVG) |
| 字体 | 系统字体栈 (无外部字体加载) |
| 部署 | GitHub Pages (`sj3199.github.io`) |
| 包管理 | npm |

## 快速启动

```bash
cd D:\portfolio
npm run dev          # 开发模式 → http://localhost:5200
npm run build        # 生产构建 → dist/
```

## 目录结构

```
portfolio/
├── public/                    # 静态资源 (直接复制到 dist/)
│   └── assets/
│       ├── js/
│       │   ├── i18n.js       # ⚠️ 运行时 i18n — 修改后必须同步 src/assets/js/
│       │   └── main.js       # AOS 初始化 + 暗色模式
│       ├── social/           # 社交图标 (SVG 优先)
│       ├── tools/            # 工具页静态资源
│       └── ...
├── src/
│   ├── assets/
│   │   └── js/
│   │       └── i18n.js       # i18n 源文件 — 修改后需复制到 public/assets/js/
│   ├── components/
│   │   ├── cards/            # 卡片组件 (BlogCard, WorkCard, SocialCard)
│   │   ├── elements/         # 通用元素 (SectionHeader, PageHeader)
│   │   ├── home/             # 首页专属组件
│   │   ├── sections/         # 页面级区块
│   │   │   ├── Footer.astro  # 全站底栏
│   │   │   ├── Header.astro  # 全站顶栏 + 语言/暗色切换
│   │   │   └── ...
│   │   ├── ui/               # 基础 UI (Button, Logo, TopBg)
│   │   └── widgets/          # 独立小组件 (TrackGa, OptimizedImage)
│   ├── collections/          # JSON 数据文件 (菜单、作品、画廊)
│   ├── config/
│   │   └── site.js           # 网站配置 (SEO、社交链接)
│   ├── layouts/
│   │   ├── Layout.astro      # ⭐ 全局布局 (body, Header, Footer, i18n 加载)
│   │   └── Meta.astro        # SEO meta 标签
│   ├── pages/                # 路由页面 (文件即路由)
│   │   ├── index.astro       # 首页
│   │   ├── about.astro       # AI 工具卡片列表页
│   │   ├── works.astro       # 作品列表
│   │   ├── work/             # 作品详情页
│   │   ├── intro/            # 个人介绍
│   │   └── tools/            # ⭐ AI 工具页
│   │       ├── compress.astro   # 图片压缩
│   │       ├── convert.astro    # 格式转换
│   │       └── resize.astro     # 尺寸调整
│   └── styles/               # 全局样式
├── .gitignore
├── astro.config.mjs
├── package.json
├── tailwind.config.mjs
└── tsconfig.json
```

## ⚠️ 关键约定 (必读)

### i18n 文件同步规则

```
src/assets/js/i18n.js    ← 源文件 (修改这个)
public/assets/js/i18n.js  ← 运行时加载 (必须从源文件复制过来!)
```

**每次修改 `src/assets/js/i18n.js` 后必须执行：**
```bash
Copy-Item src/assets/js/i18n.js public/assets/js/i18n.js -Force
# 或在 build 前执行
```

> 忘记同步 = `ReferenceError: __t is not defined` → 所有页面 JS 崩溃。

### 暗色模式

- 默认暗色模式，用户切换后存入 `localStorage('dark_mode')`
- CSS 使用 `dark:` 前缀响应暗色模式
- Layout.astro 在 `<head>` 中内联脚本防止页面闪烁

### 中英切换

- 切换按钮在右下角浮动面板 (`#langToggle`)
- 静态文本：`data-i18n="key"` 属性
- 动态文本 (JS 生成)：`__t('key', { vars })` 函数 + `window.addEventListener('langchange', ...)`
- 翻译文件：`i18n.js` 中 `zh` / `en` 两个对象

### 布局结构约定

- `<body>` 使用 `min-h-screen flex flex-col`
- 内容区包裹在 `<main class="flex-1">` 中
- Footer 使用 `mt-auto` 自动贴底
- Header 使用 `position: fixed`

### 工具页架构

所有工具页 (`tools/*.astro`) 遵循统一结构：
1. **Hero** — 标题 + 描述
2. **Control Bar** — 各工具专属的核心控件（quality/formats/size inputs）
3. **Upload Zone** — 拖拽上传 + 粘贴
4. **Preview** — 缩略图网格
5. **Progress** — 进度条 + 状态文字
6. **Results** — `max-w-7xl` 容器内 `grid-template-columns: repeat(auto-fill, minmax(200px, 1fr))`
7. **Features** — 4 项功能亮点
8. **FAQ** — 3 个常见问题

### 图片处理

- 全部浏览器端 Canvas API，不上传服务器
- JSZip CDN 用于批量下载
- 灯箱用 `fixed overlay + Escape` 关闭

## 部署

推送 `master` 分支到 GitHub，GitHub Pages 自动构建部署：

```bash
git add -A
git commit -m "描述改动"
git push
```

构建预览：
```bash
npm run build && npx serve dist
```

访问地址：https://sj3199.github.io

## AI 工具页

| 路径 | 标题 | 核心控件 |
|------|------|----------|
| `/tools/compress` | 在线图片智能压缩 | 画质滑块 (80% 默认) |
| `/tools/convert` | 在线图片格式转换 | 格式切换按钮 (JPG/PNG/WebP/BMP) |
| `/tools/resize` | 在线图片尺寸调整 | 宽高输入 + 快捷预设 (4K/2K/1080p) |

### 添加新工具

1. 在 `src/pages/tools/` 创建 `your-tool.astro`
2. 使用 `<Layout>` 包裹，参考现有工具页结构
3. 添加 `data-i18n` 属性支持中英切换
4. 在 `about.astro` 添加工具卡片
5. 在 `i18n.js` 添加翻译条目
6. `npm run build` 验证
7. 同步 i18n.js 并推送

## 常见陷阱

- **修改 tool 页面 `<script>` 块后 build 失败**：检查模板字符串中是否有未转义的反引号或 `${}`
- **`__t is not defined`**：忘记同步 `i18n.js` 到 `public/assets/js/`
- **底栏不贴底**：Footer 的 `mt-auto` 不能在响应式断点中被覆盖（如 `md:mt-48`）
- **Git 漏提交**：`.gitignore` 中 `/tools/` 只匹配根目录，`tools/` 会匹配所有 `tools` 目录
- **社交图标加载慢**：优先使用内联 SVG (`fill="currentColor"`)，避免大体积 PNG
