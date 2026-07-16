import os, re

BASE = r"D:\portfolio"
TOOLS = os.path.join(BASE, "src", "pages", "tools")

# Read base JS from current compress.astro
with open(os.path.join(TOOLS, "compress.astro"), "r", encoding="utf-8") as f:
    compress_raw = f.read()
BASE_SCRIPT = re.search(r"<script>(.*?)</script>", compress_raw, re.DOTALL).group(1)

# Extract the outer Layout wrapper from compress template
compress_template = compress_raw.split("<script>")[0]

# Common page shell (header/footer of the template)
# Find the page content area - after the hero title section, before the script
hero_end = compress_template.find('</p>\n    </div>\n\n    <!-- Controls')
if hero_end < 0:
    hero_end = compress_template.find('</p>\n    </div>\n\n    <!--')
after_controls = compress_template.find('<!-- Upload Area -->')
if after_controls < 0:
    after_controls = compress_template.find('<!-- Drop Zone -->')

page_head = compress_template[:hero_end]
drop_zone_and_below = compress_template[after_controls:]
# Extract everything between hero and drop zone as the controls area
controls_area = compress_template[hero_end:after_controls]

# Find Layout closing
layout_end_marker = '</Layout>'

# ================================================
# 1. COMPRESS.ASTRO - Quality-focused
# ================================================
compress_controls = '''    <!-- Controls -->
    <div class="flex flex-wrap items-center gap-x-5 gap-y-2.5">
      <!-- Quality slider - PROMINENT -->
      <span class="whitespace-nowrap text-xs font-medium text-neutral-500 dark:text-neutral-400">压缩画质</span>
      <div class="flex items-center gap-2">
        <input id="qualitySlider" type="range" min="10" max="100" value="80" class="h-2 w-28 accent-primary" />
        <span id="qualityLabel" class="w-9 text-sm font-bold text-primary dark:text-primary-light">80%</span>
      </div>

      <span class="hidden h-5 w-px bg-neutral-200 dark:bg-neutral-700 sm:block"></span>

      <!-- Format -->
      <span class="whitespace-nowrap text-xs font-medium text-neutral-500 dark:text-neutral-400">输出格式</span>
      <select id="formatSelect" class="rounded-lg border border-neutral-200 bg-white px-2.5 py-1.5 text-xs font-medium text-neutral-700 dark:border-neutral-600 dark:bg-neutral-800 dark:text-neutral-200">
        <option value="auto" selected>保持原格式</option>
        <option value="image/jpeg">JPEG</option>
        <option value="image/webp">WebP</option>
        <option value="image/png">PNG</option>
      </select>

      <span class="hidden h-5 w-px bg-neutral-200 dark:bg-neutral-700 sm:block"></span>

      <!-- Size -->
      <span class="whitespace-nowrap text-xs font-medium text-neutral-500 dark:text-neutral-400">输出尺寸</span>
      <select id="maxWidthSelect" class="rounded-lg border border-neutral-200 bg-white px-2.5 py-1.5 text-xs font-medium text-neutral-700 dark:border-neutral-600 dark:bg-neutral-800 dark:text-neutral-200">
        <option value="0" selected>原始尺寸</option>
        <option value="3840">4K</option>
        <option value="2560">2K</option>
        <option value="1920">1080p</option>
        <option value="1280">720p</option>
        <option value="800">800px</option>
      </select>
    </div>
'''

# Fix title
compress_page = page_head + compress_controls + drop_zone_and_below
compress_page = compress_page.replace(
    'title="图片智能压缩 | AI 项目 | Portfolio"',
    'title="在线图片智能压缩 | AI 项目 | Portfolio"'
)
compress_page = compress_page.replace(
    'description="免费的在线图片压缩工具，支持 JPG、PNG、WebP 格式，批量压缩，本地处理保护隐私。"',
    'description="在线图片智能压缩工具，支持 JPG、PNG、WebP 格式，批量压缩，本地处理保护隐私。"'
)

compress_full = compress_page + "<script>\n" + BASE_SCRIPT + "\n</script>\n</Layout>\n"
compress_full = compress_full.replace(
    "compressBtn.textContent = '压缩中...';", 
    "compressBtn.textContent = '压缩中...';"
)

with open(os.path.join(TOOLS, "compress.astro"), "w", encoding="utf-8", newline="") as f:
    f.write(compress_full)
print("compress.astro rebuilt")

# ================================================
# 2. CONVERT.ASTRO - Format buttons
# ================================================
convert_controls = '''    <!-- Controls -->
    <div class="space-y-3">
      <!-- Format selection - PRIMARY -->
      <div class="flex flex-wrap items-center gap-x-3 gap-y-2">
        <span class="whitespace-nowrap text-xs font-semibold text-neutral-700 dark:text-neutral-200">转换为：</span>
        <div class="flex gap-1.5" id="formatBtns">
          <button data-format="image/jpeg" class="fmt-btn active rounded-lg border-2 border-primary bg-primary/10 px-3.5 py-1.5 text-sm font-semibold text-primary dark:text-primary-light dark:border-primary-light dark:bg-primary/15 transition-all">JPG</button>
          <button data-format="image/png" class="fmt-btn rounded-lg border-2 border-neutral-200 px-3.5 py-1.5 text-sm font-medium text-neutral-600 hover:border-primary/40 hover:text-primary dark:border-neutral-600 dark:text-neutral-400 dark:hover:border-primary/40 dark:hover:text-primary-light transition-all">PNG</button>
          <button data-format="image/webp" class="fmt-btn rounded-lg border-2 border-neutral-200 px-3.5 py-1.5 text-sm font-medium text-neutral-600 hover:border-primary/40 hover:text-primary dark:border-neutral-600 dark:text-neutral-400 dark:hover:border-primary/40 dark:hover:text-primary-light transition-all">WebP</button>
          <button data-format="image/bmp" class="fmt-btn rounded-lg border-2 border-neutral-200 px-3.5 py-1.5 text-sm font-medium text-neutral-600 hover:border-primary/40 hover:text-primary dark:border-neutral-600 dark:text-neutral-400 dark:hover:border-primary/40 dark:hover:text-primary-light transition-all">BMP</button>
        </div>
        <span class="hidden h-5 w-px bg-neutral-200 dark:bg-neutral-700 sm:block"></span>
        <!-- Quality -->
        <span class="whitespace-nowrap text-xs font-medium text-neutral-500 dark:text-neutral-400">画质</span>
        <input id="qualitySlider" type="range" min="10" max="100" value="92" class="h-1.5 w-20 accent-primary" />
        <span id="qualityLabel" class="w-8 text-xs font-semibold text-neutral-700 dark:text-neutral-200">92%</span>
      </div>
    </div>

<style>
  .fmt-btn.active { border-color: var(--color-primary, #2d6dc3) !important; }
  :root.dark .fmt-btn.active { border-color: var(--color-primary-light, #8fb9ff) !important; }
</style>
'''

# Build convert page - reuse the page shell but change controls and title
convert_head = page_head.replace(
    '在线图片<span class="text-primary dark:text-primary-light">智能压缩</span>',
    '在线图片<span class="text-primary dark:text-primary-light">格式转换</span>'
)
convert_head = convert_head.replace(
    'title="在线图片智能压缩 | AI 项目 | Portfolio"',
    'title="在线图片格式转换 | AI 项目 | Portfolio"'
)
convert_head = convert_head.replace(
    'description="在线图片智能压缩工具，支持 JPG、PNG、WebP 格式，批量压缩，本地处理保护隐私。"',
    'description="在线图片格式转换工具，支持 JPG、PNG、WebP、BMP 格式互转，纯浏览器端处理。"'
)
convert_head = convert_head.replace(
    'keywords="图片压缩, 在线压缩, AI压缩, WebP, JPEG压缩, PNG压缩, 批量压缩"',
    'keywords="图片格式转换, PNG转JPG, WebP转JPG, 批量转换"'
)
# Fix feature text
convert_head = convert_head.replace(
    '智能压缩引擎，自动优化图片体积',
    '全格式覆盖，一键转换输出格式'
)
# FAQ fixes
convert_head = convert_head.replace(
    '如何实现高画质低体积的压缩？',
    '可以将 PNG 透明图转为 JPG 吗？'
)
convert_head = convert_head.replace(
    '使用 Canvas API 进行智能重采样，通过调节画质参数（推荐 75-85%）在视觉效果和文件大小间取得最佳平衡。WebP 格式通常能在相同画质下比 JPEG 减小 25-35% 的体积。',
    '可以。转换时透明区域会自动填充为白色背景。'
)
convert_head = convert_head.replace(
    '图片会被上传到服务器吗？',
    '支持哪些输入格式？'
)
convert_head = convert_head.replace(
    '不会。所有压缩操作均在您的浏览器本地完成，图片不会离开您的设备，确保隐私安全。',
    '输入支持 JPG、PNG、GIF、WebP、BMP、TIFF 等浏览器可识别的图片格式。'
)
convert_head = convert_head.replace(
    '会影响原始图片吗？',
    '转换会降低画质吗？'
)
convert_head = convert_head.replace(
    '输入支持 JPG、PNG、WebP 格式。输出可选择不修改、JPEG、WebP 或 PNG。推荐照片使用 WebP 格式，图标/透明图使用 PNG 格式。',
    '转换过程会重新编码图片。使用高画质设置（85%+）可保持视觉效果几乎不变。'
)
convert_head = convert_head.replace(
    '开始压缩', '开始转换'
)
convert_head = convert_head.replace(
    'compress-faq', 'convert-faq'
)

# Modify drop zone area button
convert_body = drop_zone_and_below.replace('开始压缩', '开始转换')

convert_full = convert_head + convert_controls + convert_body + "<script>\n" + BASE_SCRIPT + "\n</script>\n</Layout>\n"

# Adjust JS for convert: default format=jpeg, quality=92
convert_full = convert_full.replace(
    "compressBtn.textContent = '压缩中...';",
    "compressBtn.textContent = '转换中...';"
)
convert_full = convert_full.replace(
    "compressBtn.textContent = '开始压缩';",
    "compressBtn.textContent = '开始转换';"
)
convert_full = convert_full.replace(
    "compressBtn.setAttribute('disabled', 'true');",
    "compressBtn.setAttribute('disabled', 'true');"
)
# Fix downloadAllBtn text too
convert_full = convert_full.replace(
    "downloadAllBtn.textContent = '📦 批量下载';",
    "downloadAllBtn.textContent = '📦 批量下载';"
)

with open(os.path.join(TOOLS, "convert.astro"), "w", encoding="utf-8", newline="") as f:
    f.write(convert_full)
print("convert.astro rebuilt")

# ================================================
# 3. RESIZE.ASTRO - Dimension inputs
# ================================================
resize_controls = '''    <!-- Controls -->
    <div class="flex flex-wrap items-center gap-x-5 gap-y-2.5">
      <!-- Width/Height inputs - PRIMARY -->
      <span class="whitespace-nowrap text-xs font-semibold text-neutral-700 dark:text-neutral-200">目标尺寸</span>
      <div class="flex items-center gap-1">
        <span class="text-xs text-neutral-500 dark:text-neutral-400">宽</span>
        <input id="resizeWidth" type="number" min="1" max="7680" placeholder="自动" class="w-20 rounded-lg border border-neutral-200 bg-white px-2 py-1.5 text-xs font-medium text-neutral-700 dark:border-neutral-600 dark:bg-neutral-800 dark:text-neutral-200 focus:border-primary focus:ring-1 focus:ring-primary" />
        <span class="text-xs text-neutral-500 dark:text-neutral-400">px</span>
        <button id="lockRatio" class="ml-1 flex items-center justify-center rounded p-1 text-neutral-400 hover:text-primary dark:hover:text-primary-light transition-colors" title="锁定宽高比">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
        </button>
        <span class="text-xs text-neutral-500 dark:text-neutral-400 ml-1">高</span>
        <input id="resizeHeight" type="number" min="1" max="7680" placeholder="自动" class="w-20 rounded-lg border border-neutral-200 bg-white px-2 py-1.5 text-xs font-medium text-neutral-700 dark:border-neutral-600 dark:bg-neutral-800 dark:text-neutral-200 focus:border-primary focus:ring-1 focus:ring-primary" />
        <span class="text-xs text-neutral-500 dark:text-neutral-400">px</span>
      </div>

      <span class="hidden h-5 w-px bg-neutral-200 dark:bg-neutral-700 sm:block"></span>

      <!-- Quick presets -->
      <span class="whitespace-nowrap text-xs font-medium text-neutral-500 dark:text-neutral-400">快捷尺寸</span>
      <div class="flex gap-1">
        <button class="size-btn rounded border border-neutral-200 px-2 py-1 text-[11px] font-medium text-neutral-600 hover:border-primary/40 hover:text-primary dark:border-neutral-600 dark:text-neutral-400 dark:hover:text-primary-light transition-colors" data-w="3840" data-h="2160">4K</button>
        <button class="size-btn rounded border border-neutral-200 px-2 py-1 text-[11px] font-medium text-neutral-600 hover:border-primary/40 hover:text-primary dark:border-neutral-600 dark:text-neutral-400 dark:hover:text-primary-light transition-colors" data-w="2560" data-h="1440">2K</button>
        <button class="size-btn rounded border border-neutral-200 px-2 py-1 text-[11px] font-medium text-neutral-600 hover:border-primary/40 hover:text-primary dark:border-neutral-600 dark:text-neutral-400 dark:hover:text-primary-light transition-colors" data-w="1920" data-h="1080">1080p</button>
        <button class="size-btn rounded border border-neutral-200 px-2 py-1 text-[11px] font-medium text-neutral-600 hover:border-primary/40 hover:text-primary dark:border-neutral-600 dark:text-neutral-400 dark:hover:text-primary-light transition-colors" data-w="1280" data-h="720">720p</button>
        <button class="size-btn rounded border border-neutral-200 px-2 py-1 text-[11px] font-medium text-neutral-600 hover:border-primary/40 hover:text-primary dark:border-neutral-600 dark:text-neutral-400 dark:hover:text-primary-light transition-colors" data-w="800" data-h="0">800px</button>
      </div>

      <span class="hidden h-5 w-px bg-neutral-200 dark:bg-neutral-700 sm:block"></span>

      <!-- Format + Quality secondary -->
      <span class="whitespace-nowrap text-xs font-medium text-neutral-500 dark:text-neutral-400">输出格式</span>
      <select id="formatSelect" class="rounded-lg border border-neutral-200 bg-white px-2.5 py-1.5 text-xs font-medium text-neutral-700 dark:border-neutral-600 dark:bg-neutral-800 dark:text-neutral-200">
        <option value="auto" selected>保持原格式</option>
        <option value="image/jpeg">JPEG</option>
        <option value="image/webp">WebP</option>
        <option value="image/png">PNG</option>
      </select>

      <span class="whitespace-nowrap text-xs font-medium text-neutral-500 dark:text-neutral-400">画质</span>
      <input id="qualitySlider" type="range" min="10" max="100" value="90" class="h-1.5 w-20 accent-primary" />
      <span id="qualityLabel" class="w-8 text-xs font-semibold text-neutral-700 dark:text-neutral-200">90%</span>
    </div>
'''

resize_head = page_head.replace(
    '在线图片<span class="text-primary dark:text-primary-light">智能压缩</span>',
    '在线图片<span class="text-primary dark:text-primary-light">尺寸调整</span>'
)
resize_head = resize_head.replace(
    'title="在线图片智能压缩 | AI 项目 | Portfolio"',
    'title="在线图片尺寸调整 | AI 项目 | Portfolio"'
)
resize_head = resize_head.replace(
    'description="在线图片智能压缩工具，支持 JPG、PNG、WebP 格式，批量压缩，本地处理保护隐私。"',
    'description="在线图片尺寸调整工具，支持自定义宽高、锁定比例、批量缩放，纯浏览器端处理。"'
)
resize_head = resize_head.replace(
    'keywords="图片压缩, 在线压缩, AI压缩, WebP, JPEG压缩, PNG压缩, 批量压缩"',
    'keywords="图片尺寸调整, 图片缩放, 在线改尺寸, 批量缩放"'
)
resize_head = resize_head.replace(
    '智能压缩引擎，自动优化图片体积',
    '精准尺寸控制，支持自定义宽高与锁定比例'
)
# FAQ
resize_head = resize_head.replace(
    '如何实现高画质低体积的压缩？',
    '调整尺寸会改变画质吗？'
)
resize_head = resize_head.replace(
    '使用 Canvas API 进行智能重采样，通过调节画质参数（推荐 75-85%）在视觉效果和文件大小间取得最佳平衡。WebP 格式通常能在相同画质下比 JPEG 减小 25-35% 的体积。',
    '缩小尺寸不会降低原始画质。放大可能产生轻微模糊，建议使用原始尺寸作为上限。'
)
resize_head = resize_head.replace(
    '图片会被上传到服务器吗？',
    '会保持原始比例吗？'
)
resize_head = resize_head.replace(
    '不会。所有压缩操作均在您的浏览器本地完成，图片不会离开您的设备，确保隐私安全。',
    '输入任意一边，另一边会自动计算保持原始宽高比。取消锁定后可自由设置。'
)
resize_head = resize_head.replace(
    '会影响原始图片吗？',
    '支持哪些尺寸？'
)
resize_head = resize_head.replace(
    '输入支持 JPG、PNG、WebP 格式。输出可选择不修改、JPEG、WebP 或 PNG。推荐照片使用 WebP 格式，图标/透明图使用 PNG 格式。',
    '支持 1-7680px 范围，常见尺寸（4K、2K、1080p、720p）一键切换，也可自定义输入。'
)
resize_head = resize_head.replace(
    '开始压缩', '开始调整'
)
resize_head = resize_head.replace(
    'compress-faq', 'resize-faq'
)

resize_body = drop_zone_and_below.replace('开始压缩', '开始调整')

resize_full = resize_head + resize_controls + resize_body + "<script>\n" + BASE_SCRIPT + "\n</script>\n</Layout>\n"

# Adjust JS labels
resize_full = resize_full.replace(
    "compressBtn.textContent = '压缩中...';",
    "compressBtn.textContent = '调整中...';"
)
resize_full = resize_full.replace(
    "compressBtn.textContent = '开始压缩';",
    "compressBtn.textContent = '开始调整';"
)

with open(os.path.join(TOOLS, "resize.astro"), "w", encoding="utf-8", newline="") as f:
    f.write(resize_full)
print("resize.astro rebuilt")

print("All done")
