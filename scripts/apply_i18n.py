"""Add data-i18n to all Chinese text in tool pages and rebuild i18n.js"""
import re, os, json

BASE = r"D:\portfolio"
PAGES = [
    "src/pages/tools/compress.astro",
    "src/pages/tools/convert.astro",
    "src/pages/tools/resize.astro",
    "src/pages/tools/compress-to-size.astro",
]
I18N_PATH = os.path.join(BASE, "public/assets/js/i18n.js")

# ---- 1. Build comprehensive translations ----
# Key: page_tag (prefix), Value: {zh_text: en_text}
TRANSLATIONS = {
    "compress": {
        # Hero
        "在线图片": "Online Image",
        "智能压缩": "Smart Compression",
        "纯浏览器端处理，图片不会上传到任何服务器。\n      支持 JPG / PNG / WebP，批量拖拽，一键下载。": "Client-side only. Images never leave your device.\n      Supports JPG / PNG / WebP, batch drag-and-drop, one-click download.",
        # Controls
        "格式转换": "Format",
        "不修改格式": "Keep Original",
        "转为 JPEG": "Convert to JPEG",
        "转为 WebP": "Convert to WebP",
        "转为 PNG": "Convert to PNG",
        "压缩画质": "Quality",
        "最大宽度": "Max Width",
        "原始尺寸": "Original",
        "开始压缩": "Compress",
        "清空": "Clear",
        # Upload zone
        "拖拽图片到此处，或": "Drag images here, or ",
        "点击上传": "click to upload",
        "Ctrl+V 粘贴图片 ｜ 支持 JPG / PNG / WebP ｜ 一次最多 50 张": "Ctrl+V to paste | Supports JPG / PNG / WebP | Up to 50 files",
        "清空全部": "Clear All",
        "准备中...": "Preparing...",
        "📦 批量下载": "📦 Download All",
        # Features
        "100% 免费 · 全场景图片压缩": "100% Free · Universal Image Compression",
        "隐私安全": "Privacy First",
        "纯浏览器端处理，图片不会离开你的设备，绝不上传服务器。": "Client-side processing. Images never leave your device, never uploaded.",
        "闪电速度": "Lightning Fast",
        "Canvas 引擎本地运算，毫秒级响应，不受网络速度影响。": "Canvas engine for local processing. Millisecond response, no network dependency.",
        "批量处理": "Batch Processing",
        "支持拖拽多图、Ctrl+V 粘贴，一次处理最多 50 张图片。": "Drag multiple images, Ctrl+V paste, process up to 50 at once.",
        "多格式支持": "Multi-Format",
        "支持 JPG、PNG、WebP 格式互转，自定义画质和尺寸。": "Convert between JPG, PNG, WebP with custom quality and dimensions.",
        # FAQ
        "常见问题": "FAQ",
        "如何实现高画质低体积的压缩？": "How to achieve high quality with small file size?",
        "使用 Canvas API 进行智能重采样，通过调节画质参数（推荐 75-85%）在视觉效果和文件大小间取得最佳平衡。": "Uses Canvas API for intelligent resampling. Adjust quality (75-85% recommended) for optimal visual-to-size balance.",
        "图片会被上传到服务器吗？": "Are my images uploaded to a server?",
        "不会。所有压缩操作都在你的浏览器中通过 Canvas API 完成，图片数据从未离开你的设备。": "No. All compression runs in your browser via Canvas API. Your images never leave your device.",
        "支持哪些图片格式？": "Which formats are supported?",
        "输入支持 JPG、PNG、WebP 格式。输出可选择不修改、JPEG、WebP 或 PNG。推荐照片使用 WebP 格式，图标/透明图使用 PNG 格式。": "Input: JPG, PNG, WebP. Output: original, JPEG, WebP or PNG. WebP recommended for photos, PNG for icons/transparent images.",
        # JS dynamic
        "已选择": "Selected",
        "张图片": "images",
        "压缩中…": "Compressing...",
        "完成！": "Done!",
        "正在压缩": "Compressing",
        "批量下载失败，请尝试逐个下载": "Batch download failed. Please try individual download.",
        "一次最多处理 50 张图片": "Maximum 50 images per batch",
        "⏳ 打包中...": "⏳ Packing...",
        "预览": "Preview",
        "下载": "Download",
        # Summary
        "共压缩": "Compressed",
        "节省": "saved",
        "共转换": "Converted",
        "体积变化": "size change",
        "共调整": "Resized",
        "下载 (": "Download (",
        ")": ")"
    },
    "convert": {
        "图片": "Image",
        "格式转换": "Format Conversion",
        "批量将 PNG、WEBP、BMP、TIFF 等格式转换为 JPG 格式。纯浏览器端处理，安全快速。": "Batch convert PNG, WebP, BMP, TIFF and more to JPG. Client-side processing, safe and fast.",
        # Controls
        "转换为": "Convert to",
        "画质": "Quality",
        "开始转换": "Convert",
        "清空": "Clear",
        # Upload
        "拖拽图片到此处，或": "Drag images here, or",
        "点击上传": "click to upload",
        "Ctrl+V 粘贴图片 ｜ 支持 JPG / PNG / WebP / BMP / TIFF ｜ 一次最多 50 张": "Ctrl+V to paste | Supports JPG / PNG / WebP / BMP / TIFF | Up to 50 files",
        "清空全部": "Clear All",
        "准备中...": "Preparing...",
        "📦 批量下载": "📦 Download All",
        # Features
        "全格式覆盖 · 一键转换": "All Formats · One-Click Convert",
        "多格式输入": "Multi-Format Input",
        "支持 JPG、PNG、WebP、BMP、TIFF 等常见格式。": "Supports JPG, PNG, WebP, BMP, TIFF and more.",
        "批量转换": "Batch Convert",
        "一次拖入多张图片，批量完成格式转换。": "Drop multiple images and convert them all at once.",
        "隐私安全": "Privacy First",
        "纯浏览器端处理，图片不会上传到任何服务器。": "Client-side processing. Images never leave your device.",
        "质量可控": "Quality Control",
        "自由调节输出画质，平衡文件大小和视觉效果。": "Freely adjust output quality to balance file size and visual fidelity.",
        # FAQ
        "常见问题": "FAQ",
        "可以将 PNG 透明图转为 JPG 吗？": "Can I convert transparent PNG to JPG?",
        "可以。转换时透明区域会自动填充为白色背景。": "Yes. Transparent areas will be filled with white background.",
        "支持哪些输入格式？": "What input formats are supported?",
        "支持 JPG、PNG、WebP、BMP、TIFF 等常见图片格式。": "JPG, PNG, WebP, BMP, TIFF and other browser-supported formats.",
        # JS
        "已选择": "Selected",
        "张图片": "images",
        "转换中…": "Converting...",
        "完成！": "Done!",
        "正在转换": "Converting",
        "批量下载失败，请尝试逐个下载": "Batch download failed. Please try individual download.",
        "一次最多处理 50 张图片": "Maximum 50 images per batch",
        "⏳ 打包中...": "⏳ Packing...",
        "预览": "Preview",
        "下载": "Download",
        "共转换": "Converted",
        "下载 (": "Download (",
        ")": ")"
    },
    "resize": {
        "图片": "Image",
        "改尺寸": "Resize",
        "免费在线图片尺寸调整工具，批量修改图片宽高像素，纯浏览器端处理。": "Free online image resizer. Batch resize image dimensions. Client-side processing.",
        # Controls
        "宽度": "Width",
        "高度": "Height",
        "保持比例": "Keep Aspect Ratio",
        "开始调整": "Resize",
        "清空": "Clear",
        # Upload
        "拖拽图片到此处，或": "Drag images here, or",
        "点击上传": "click to upload",
        "Ctrl+V 粘贴图片 ｜ 支持 JPG / PNG / WebP ｜ 一次最多 50 张": "Ctrl+V to paste | Supports JPG / PNG / WebP | Up to 50 files",
        "清空全部": "Clear All",
        "准备中...": "Preparing...",
        "📦 批量下载": "📦 Download All",
        # Features
        "100% 免费 · 灵活调整尺寸": "100% Free · Flexible Resizing",
        "隐私安全": "Privacy First",
        "纯浏览器端处理，图片不会离开你的设备，绝不上传服务器。": "Client-side processing. Images never leave your device, never uploaded.",
        "闪电速度": "Lightning Fast",
        "Canvas 引擎本地运算，毫秒级响应，不受网络速度影响。": "Canvas engine for local processing. Millisecond response, no network dependency.",
        "批量处理": "Batch Processing",
        "支持拖拽多图、Ctrl+V 粘贴，一次处理最多 50 张图片。": "Drag multiple images, Ctrl+V paste, process up to 50 at once.",
        "灵活适配": "Flexible Sizing",
        "支持像素级精确调整，可锁定宽高比例，满足各种尺寸需求。": "Pixel-precise adjustment with aspect ratio lock for any dimension requirement.",
        # FAQ
        "常见问题": "FAQ",
        "调整尺寸会影响画质吗？": "Does resizing affect quality?",
        "缩小图片不会显著降低画质，但放大图片可能会导致模糊。": "Downscaling does not significantly affect quality, but upscaling may cause blurriness.",
        "可以批量处理吗？": "Can I batch process?",
        "可以。上传多张图片后，设置目标尺寸，一键批量处理所有图片。": "Yes. Upload multiple images, set target dimensions, and process all in one click.",
        # JS
        "已选择": "Selected",
        "张图片": "images",
        "调整中…": "Resizing...",
        "完成！": "Done!",
        "正在调整": "Resizing",
        "批量下载失败，请尝试逐个下载": "Batch download failed. Please try individual download.",
        "一次最多处理 50 张图片": "Maximum 50 images per batch",
        "⏳ 打包中...": "⏳ Packing...",
        "预览": "Preview",
        "下载": "Download",
        "共调整": "Resized",
        "下载 (": "Download (",
        ")": ")"
    },
    "cs": {
        "图片": "Image",
        "压缩到指定大小": "Compress to Target",
        "将图片压缩到你设定的目标文件大小，自动二分查找最佳压缩率。纯浏览器端处理。": "Compress images to your target file size. Automatic binary search for optimal compression. Client-side only.",
        # Controls
        "目标大小": "Target Size",
        "开始压缩": "Compress",
        "清空": "Clear",
        # Upload
        "拖拽图片到此处，或": "Drag images here, or",
        "点击上传": "click to upload",
        "Ctrl+V 粘贴图片 ｜ 支持 JPG / PNG / WebP ｜ 一次最多 50 张": "Ctrl+V to paste | Supports JPG / PNG / WebP | Up to 50 files",
        "清空全部": "Clear All",
        "准备中...": "Preparing...",
        "📦 批量下载": "📦 Download All",
        # Features
        "100% 免费 · 指定大小压缩": "100% Free · Target Size Compression",
        "隐私安全": "Privacy First",
        "纯浏览器端处理，图片不会离开你的设备，绝不上传服务器。": "Client-side processing. Images never leave your device, never uploaded.",
        "智能算法": "Smart Algorithm",
        "二分查找自动逼近目标大小，无需手动调参，效率极高。": "Binary search automatically approaches target size. No manual tuning needed.",
        "批量处理": "Batch Processing",
        "支持拖拽多图、Ctrl+V 粘贴，一次处理最多 50 张图片。": "Drag multiple images, Ctrl+V paste, process up to 50 at once.",
        "格式保持": "Format Preserved",
        "保持原始格式不变，仅优化压缩参数，确保兼容性。": "Original format preserved. Only compression parameters optimized for compatibility.",
        # FAQ
        "常见问题": "FAQ",
        "压缩后的文件大小能完全精确吗？": "Is the output file size perfectly accurate?",
        "我们会尽力逼近目标大小，使用二分查找自动调整压缩率。受图片内容复杂度影响，结果可能会有轻微偏差。": "We approximate the target using binary search. Results may vary slightly depending on image complexity.",
        "如果图片本身很小，无法压到目标怎么办？": "What if the image is already smaller than target?",
        "如果原始文件已小于目标大小，我们会保持原图质量不做额外压缩，避免画质损失。": "If the original is already smaller, we preserve quality without additional compression.",
        # JS
        "已选择": "Selected",
        "张图片": "images",
        "压缩中…": "Compressing...",
        "完成！": "Done!",
        "正在压缩": "Compressing",
        "批量下载失败，请尝试逐个下载": "Batch download failed. Please try individual download.",
        "一次最多处理 50 张图片": "Maximum 50 images per batch",
        "⏳ 打包中...": "⏳ Packing...",
        "预览": "Preview",
        "下载": "Download",
        "共压缩": "Compressed",
        "下载 (": "Download (",
        ")": ")"
    }
}

# ---- 2. Add data-i18n to each page ----
for page_rel in PAGES:
    page_path = os.path.join(BASE, page_rel)
    tag = page_rel.split("/")[-1].replace(".astro", "")
    if tag == "compress-to-size":
        tag = "cs"
    
    with open(page_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    trans = TRANSLATIONS.get(tag, {})
    
    # Counters
    added = 0
    skipped = 0
    
    # For each translation, find Chinese text in the page and add data-i18n
    for zh, en in trans.items():
        # Skip very short strings that might match inside longer strings
        if len(zh) < 3:
            continue
        # Only add if zh text is actually in the page
        if zh not in content:
            skipped += 1
            continue
        
        # Generate a unique i18n key
        key = f"{tag}-{added:03d}"
        
        # Find the text in an HTML element (not already inside data-i18n)
        # Replace: >TEXT< → data-i18n="KEY">TEXT<
        pattern = re.compile(
            r'(<(h[1-6]|p|span|button|option|a|div)\b[^>]*?)(?<!data-i18n=")(?<!data-i18n-)>\s*'
            + re.escape(zh)
            + r'\s*</',
            re.DOTALL
        )
        
        # Try without looking for specific tag
        pattern2 = re.compile(
            r'(<(\w+)\b[^>]*?)(?<!data-i18n)>\s*'
            + re.escape(zh)
            + r'\s*</',
            re.DOTALL
        )
        
        def replacer(m):
            tag_open = m.group(1)
            if 'data-i18n=' in tag_open:
                return m.group(0)  # already has data-i18n
            inner_text = m.group(0)[len(tag_open)+1:-2]  # between > and <
            return f'{tag_open} data-i18n="{key}">{inner_text}</'
        
        new_content = pattern2.sub(replacer, content)
        if new_content != content:
            content = new_content
            added += 1
    
    with open(page_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"{tag}: added {added} data-i18n attributes, skipped {skipped}")


# ---- 3. Build new i18n.js ----
# Build zh and en sections
zh_section = {}
en_section = {}

for tag, trans in TRANSLATIONS.items():
    for zh, en in trans.items():
        key = f"{tag}-{zh}"  # use text as key for simplicity
        zh_section[key] = zh
        en_section[key] = en

# Also add legacy keys if present
legacy_keys = {
    "resume": ("简历", "Resume"),
    "light": ("浅色", "Light"),
    "dark": ("深色", "Dark"),
    "theme": ("主题", "Theme"),
}

new_i18n = """// i18n translations v3 - Portfolio Site
const i18n = {
  zh: ZH_PLACEHOLDER,
  en: EN_PLACEHOLDER
};

function getLang() {
  try { return localStorage.getItem('lang') || 'zh'; } catch(e) { return 'zh'; }
}

function setLang(lang) {
  localStorage.setItem('lang', lang);
  applyLang(lang);
}

// Global translation helper for dynamic JS text
window.__t = function(key) {
  return (i18n[getLang()] || i18n.zh)[key] || i18n.zh[key] || key;
};

function applyLang(lang) {
  const t = i18n[lang] || i18n.zh;

  document.querySelectorAll('[data-i18n]').forEach(function(el) {
    const key = el.getAttribute('data-i18n');
    if (t[key]) el.textContent = t[key];
  });

  document.querySelectorAll('[data-i18n-html]').forEach(function(el) {
    const key = el.getAttribute('data-i18n-html');
    if (t[key]) el.innerHTML = t[key];
  });

  function updateMenuText() {
    var isMobile = window.innerWidth < 640;
    document.querySelectorAll('[data-i18n-menu]').forEach(function(el) {
      var zh = isMobile ? (el.getAttribute('data-i18n-zh-short') || el.getAttribute('data-i18n-zh')) : el.getAttribute('data-i18n-zh');
      var en = isMobile ? (el.getAttribute('data-i18n-en-short') || el.getAttribute('data-i18n-en')) : el.getAttribute('data-i18n-en');
      if (zh && en) el.textContent = lang === 'en' ? en : zh;
    });
  }

  document.querySelectorAll('[data-i18n-menu]').forEach(function(el) {
    updateMenuText();
  });

  var menuResizeHandler = null;
  window.addEventListener('resize', function() {
    if (menuResizeHandler) clearTimeout(menuResizeHandler);
    menuResizeHandler = setTimeout(updateMenuText, 100);
  });

  document.querySelectorAll('[data-i18n-cat]').forEach(function(el) {
    var catKey = el.getAttribute('data-i18n-cat');
    var catName = t['cat-' + catKey] || catKey;
    el.textContent = catName;
  });

  document.querySelectorAll('[data-i18n-title]').forEach(function(el) {
    var key = el.getAttribute('data-i18n-title');
    if (t[key]) el.setAttribute('title', t[key]);
  });

  document.documentElement.classList.add('i18n-ready');

  var langBtn = document.getElementById('langToggle');
  if (langBtn) langBtn.textContent = lang === 'en' ? '\\u4e2d' : 'EN';

  document.documentElement.setAttribute('lang', lang === 'en' ? 'en' : 'zh-CN');
}

document.addEventListener('DOMContentLoaded', function() {
  var lang = getLang();
  applyLang(lang);

  var langToggle = document.getElementById('langToggle');
  if (langToggle) {
    langToggle.addEventListener('click', function() {
      setLang(getLang() === 'zh' ? 'en' : 'zh');
    });
  }

  var langToggleMobile = document.getElementById('langToggleMobile');
  if (langToggleMobile) {
    langToggleMobile.addEventListener('click', function() {
      setLang(getLang() === 'zh' ? 'en' : 'zh');
    });
  }
});
"""

# Format zh/en sections as JS objects
def format_section(d):
    lines = []
    for k, v in d.items():
        # Escape single quotes in keys and values
        k_esc = k.replace("'", "\\'").replace("\n", "\\n")
        v_esc = v.replace("'", "\\'").replace("\n", "\\n")
        lines.append(f"    '{k_esc}': '{v_esc}'")
    return "{\n" + ",\n".join(lines) + "\n  }"

zh_str = format_section(zh_section)
en_str = format_section(en_section)

new_i18n = new_i18n.replace("ZH_PLACEHOLDER", zh_str).replace("EN_PLACEHOLDER", en_str)

# Write to public/
with open(I18N_PATH, "w", encoding="utf-8") as f:
    f.write(new_i18n)

print(f"\n✓ i18n.js written with {len(zh_section)} translations")
