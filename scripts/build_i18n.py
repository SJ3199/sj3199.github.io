# Build comprehensive i18n.js with text-node walk for full-page translation
import json, os

BASE = r"D:\portfolio"
I18N_PATH = os.path.join(BASE, "public/assets/js/i18n.js")

# Comprehensive translations: {chinese_text: english_text}
T = {
    # Nav / Common
    "视觉作品": "Portfolio",
    "个人介绍": "About Me",
    "AI项目": "AI Projects",
    "简历": "Resume",
    "返回首页": "Back to Home",
    "浅色": "Light",
    "深色": "Dark",
    "主题": "Theme",
    "中": "EN",
    "EN": "\u4e2d",

    # Compress hero
    "在线图片": "Online Image",
    "智能压缩": "Smart Compression",
    "纯浏览器端处理，图片不会上传到任何服务器。\n      支持 JPG / PNG / WebP，批量拖拽，一键下载。":
        "Client-side only. Images never leave your device.\n      Supports JPG / PNG / WebP, batch drag-and-drop, one-click download.",
    "纯浏览器端处理，图片不会上传到任何服务器。\n      支持 JPG / PNG / WebP，\n      批量拖拽，一键下载。":
        "Client-side only. Images never leave your device.\n      Supports JPG / PNG / WebP,\n      batch drag-and-drop, one-click download.",

    # Compress controls
    "格式转换": "Format",
    "不修改格式": "Keep Original",
    "转为 JPEG": "Convert to JPEG",
    "转为 WebP": "Convert to WebP",
    "转为 PNG": "Convert to PNG",
    "压缩画质": "Quality",
    "最大宽度": "Max Width",
    "原始尺寸": "Original",
    "4K": "4K",
    "2K": "2K",
    "1080p": "1080p",
    "720p": "720p",
    "800px": "800px",

    # Compress features
    "100% 免费 · 全场景图片压缩": "100% Free · Universal Image Compression",
    "纯浏览器端处理，图片不会离开你的设备，绝不上传服务器。":
        "Client-side processing. Images never leave your device, never uploaded.",
    "Canvas 引擎本地运算，毫秒级响应，不受网络速度影响。":
        "Canvas engine for local processing. Millisecond response, no network dependency.",
    "支持拖拽多图、Ctrl+V 粘贴，一次处理最多 50 张图片。":
        "Drag multiple images, Ctrl+V paste, process up to 50 at once.",
    "支持 JPG、PNG、WebP 格式互转，自定义画质和尺寸。":
        "Convert between JPG, PNG, WebP with custom quality and dimensions.",

    # Compress FAQ
    "如何实现高画质低体积的压缩？": "How to achieve high quality with small file size?",
    "使用 Canvas API 进行智能重采样，通过调节画质参数（推荐 75-85%）在视觉效果和文件大小间取得最佳平衡。WebP 格式通常能在相同画质下比 JPEG 减小 25-35% 的体积。":
        "Uses Canvas API for intelligent resampling. Adjust quality (75-85% recommended) for optimal visual-to-size balance. WebP typically reduces file size by 25-35% vs JPEG.",
    "使用 Canvas API 进行智能重采样，通过调节画质参数（推荐 75-85%）在视觉效果和文件大小间取得最佳平衡。":
        "Uses Canvas API for intelligent resampling. Adjust quality (75-85% recommended) for optimal visual-to-size balance.",
    "图片会被上传到服务器吗？": "Are my images uploaded to a server?",
    "不会。所有压缩操作都在你的浏览器中通过 Canvas API 完成，图片数据从未离开你的设备。":
        "No. All compression runs in your browser via Canvas API. Your images never leave your device.",
    "支持哪些图片格式？": "Which formats are supported?",
    "输入支持 JPG、PNG、WebP 格式。输出可选择不修改、JPEG、WebP 或 PNG。推荐照片使用 WebP 格式，图标/透明图使用 PNG 格式。":
        "Input: JPG, PNG, WebP. Output: original, JPEG, WebP or PNG. WebP recommended for photos, PNG for icons/transparent images.",
    "输入支持 JPG、PNG、WebP 格式。推荐照片使用 WebP，图标/透明图使用 PNG。":
        "Input: JPG, PNG, WebP. Use WebP for photos, PNG for transparent images.",

    # Convert
    "格式转换": "Format Conversion",
    "批量将 PNG、WEBP、BMP、TIFF 等格式转换为 JPG 格式。纯浏览器端处理，安全快速。":
        "Batch convert PNG, WebP, BMP, TIFF and more to JPG. Client-side processing, safe and fast.",
    "转换为": "Convert to",
    "画质": "Quality",
    "全格式覆盖 · 一键转换": "All Formats · One-Click Convert",
    "多格式输入": "Multi-Format Input",
    "支持 JPG、PNG、WebP、BMP、TIFF 等常见格式。": "Supports JPG, PNG, WebP, BMP, TIFF and more.",
    "批量转换": "Batch Convert",
    "一次拖入多张图片，批量完成格式转换。": "Drop multiple images and convert them all at once.",
    "质量可控": "Quality Control",
    "自由调节输出画质，平衡文件大小和视觉效果。":
        "Freely adjust output quality to balance file size and visual fidelity.",
    "可以将 PNG 透明图转为 JPG 吗？": "Can I convert transparent PNG to JPG?",
    "可以。转换时透明区域会自动填充为白色背景。":
        "Yes. Transparent areas will be filled with white background.",
    "支持哪些输入格式？": "What input formats are supported?",
    "输入支持 JPG、PNG、GIF、WebP、BMP、TIFF 等浏览器可识别的图片格式。":
        "Input supports JPG, PNG, GIF, WebP, BMP, TIFF and other browser-recognized formats.",
    "支持 JPG、PNG、WebP、BMP、TIFF 等常见图片格式。":
        "JPG, PNG, WebP, BMP, TIFF and other common formats.",
    "支持 JPG、PNG、GIF、WebP、BMP、TIFF 等浏览器可识别的图片格式。":
        "JPG, PNG, GIF, WebP, BMP, TIFF and other browser-recognized formats.",

    # Resize
    "改尺寸": "Resize",
    "免费在线图片尺寸调整工具，批量修改图片宽高像素，纯浏览器端处理。":
        "Free online image resizer. Batch resize image dimensions. Client-side processing.",
    "宽度": "Width",
    "高度": "Height",
    "保持比例": "Keep Ratio",
    "100% 免费 · 灵活调整尺寸": "100% Free · Flexible Resizing",
    "灵活适配": "Flexible Sizing",
    "支持像素级精确调整，可锁定宽高比例，满足各种尺寸需求。":
        "Pixel-precise adjustment with aspect ratio lock for any dimension requirement.",
    "调整尺寸会影响画质吗？": "Does resizing affect quality?",
    "缩小图片不会显著降低画质，但放大图片可能会导致模糊。":
        "Downscaling does not significantly affect quality, but upscaling may cause blurriness.",
    "可以批量处理吗？": "Can I batch process?",
    "可以。上传多张图片后，设置目标尺寸，一键批量处理所有图片。":
        "Yes. Upload multiple images, set target dimensions, and process all in one click.",

    # Compress-to-size
    "将图片压缩到你设定的目标文件大小，自动二分查找最佳压缩率。纯浏览器端处理。":
        "Compress images to your target file size. Automatic binary search for optimal compression. Client-side only.",
    "目标大小": "Target Size",
    "100% 免费 · 指定大小压缩": "100% Free · Target Size Compression",
    "智能算法": "Smart Algorithm",
    "二分查找自动逼近目标大小，无需手动调参，效率极高。":
        "Binary search automatically approaches target size. No manual tuning needed.",
    "格式保持": "Format Preserved",
    "保持原始格式不变，仅优化压缩参数，确保兼容性。":
        "Original format preserved. Only compression parameters optimized for compatibility.",
    "压缩后的文件大小能完全精确吗？": "Is the output file size perfectly accurate?",
    "我们会尽力逼近目标大小，使用二分查找自动调整压缩率。受图片内容复杂度影响，结果可能会有轻微偏差。":
        "We approximate the target using binary search. Results may vary slightly depending on image complexity.",
    "如果图片本身很小，无法压到目标怎么办？":
        "What if the image is already smaller than target?",
    "如果原始文件已小于目标大小，我们会保持原图质量不做额外压缩，避免画质损失。":
        "If the original is already smaller, we preserve quality without additional compression.",

    # Shared upload zone
    "拖拽图片到此处，或点击上传": "Drag images here, or click to upload",
    "拖拽图片到此处，或": "Drag images here, or",
    "点击上传": "click to upload",
    "Ctrl+V 粘贴图片 ｜ 支持 JPG / PNG / WebP ｜ 一次最多 50 张":
        "Ctrl+V to paste | JPG / PNG / WebP | Up to 50 files",
    "Ctrl+V 粘贴图片 ｜ 支持 JPG / PNG / WebP / BMP / TIFF ｜ 一次最多 50 张":
        "Ctrl+V to paste | JPG / PNG / WebP / BMP / TIFF | Up to 50 files",
    "清空全部": "Clear All",
    "准备中...": "Preparing...",
    "\U0001f4e6 批量下载": "\U0001f4e6 Download All",

    # Progress, download
    "预览": "Preview",
    "下载": "Download",
    "一次最多处理 50 张图片": "Maximum 50 images per batch",

    # Features shared
    "隐私安全": "Privacy First",
    "纯浏览器端处理，图片不会上传到任何服务器。":
        "Client-side processing. Images never leave your device.",
    "闪电速度": "Lightning Fast",
    "批量处理": "Batch Processing",
    "多格式支持": "Multi-Format",
}

# Build zh: key=text, value=text; en: key=text, value=translation
zh = {}
en = {}
for cn_text, eng_text in T.items():
    # Use the Chinese text as the key
    key = cn_text
    zh[key] = cn_text
    en[key] = eng_text

def format_section(d):
    lines = []
    for k, v in d.items():
        k_esc = k.replace("\\", "\\\\").replace("'", "\\'").replace("\n", "\\n")
        v_esc = v.replace("\\", "\\\\").replace("'", "\\'").replace("\n", "\\n")
        lines.append(f"    '{k_esc}': '{v_esc}'")
    return "{\n" + ",\n".join(lines) + "\n  }"

zh_str = format_section(zh)
en_str = format_section(en)

i18n_js = f"""// i18n v4 — text-content-based global + data-i18n for overrides
const i18n = {{
  zh: {zh_str},
  en: {en_str}
}};

function getLang() {{
  try {{ return localStorage.getItem('lang') || 'zh'; }} catch(e) {{ return 'zh'; }}
}}

function setLang(lang) {{
  localStorage.setItem('lang', lang);
  applyLang(lang);
}}

window.__t = function(key) {{
  var t = i18n[getLang()] || i18n.zh;
  return t[key] || i18n.zh[key] || key;
}};

// Store original text on first load
function markOrigText() {{
  if (document.body.hasAttribute('data-i18n-scanned')) return;
  document.body.setAttribute('data-i18n-scanned', '1');

  var walker = document.createTreeWalker(
    document.body,
    NodeFilter.SHOW_TEXT,
    null
  );
  var nodes = [];
  while (walker.nextNode()) {{
    nodes.push(walker.currentNode);
  }}

  nodes.forEach(function(node) {{
    var text = node.textContent;
    // Skip empty/whitespace-only nodes
    if (!text || !text.trim()) return;
    // Skip script/style
    var parent = node.parentElement;
    if (!parent || parent.tagName === 'SCRIPT' || parent.tagName === 'STYLE') return;
    // Only handle leaf text (parent has this as only child, or parent is <option>)
    var cn = 0;
    for (var i = 0; i < parent.childNodes.length; i++) {{
      if (parent.childNodes[i].nodeType === 3 && parent.childNodes[i].textContent.trim()) cn++;
    }}
    if (cn !== 1 && parent.tagName !== 'OPTION') return;
    // Skip nodes inside elements that already have data-i18n
    if (parent.hasAttribute('data-i18n') || parent.hasAttribute('data-i18n-html')) return;
    // Check if text is in our zh dictionary
    var t = text.trim();
    if (i18n.zh[t]) {{
      parent.setAttribute('data-i18n-auto', '1');
      parent.setAttribute('data-i18n-key', t);
    }}
  }});
}}

function applyLang(lang) {{
  var t = i18n[lang] || i18n.zh;

  // 1. Explicit data-i18n
  document.querySelectorAll('[data-i18n]').forEach(function(el) {{
    var key = el.getAttribute('data-i18n');
    if (t[key]) el.textContent = t[key];
  }});

  // 2. data-i18n-html
  document.querySelectorAll('[data-i18n-html]').forEach(function(el) {{
    var key = el.getAttribute('data-i18n-html');
    if (t[key]) el.innerHTML = t[key];
  }});

  // 3. Auto-translate (text-content matching)
  document.querySelectorAll('[data-i18n-auto]').forEach(function(el) {{
    var key = el.getAttribute('data-i18n-key');
    if (key && t[key] && t[key] !== el.textContent.trim()) {{
      el.textContent = t[key];
    }}
  }});

  // 4. Menu text (legacy)
  function updateMenuText() {{
    var isMobile = window.innerWidth < 640;
    document.querySelectorAll('[data-i18n-menu]').forEach(function(el) {{
      var zh = isMobile ? (el.getAttribute('data-i18n-zh-short') || el.getAttribute('data-i18n-zh')) : el.getAttribute('data-i18n-zh');
      var en = isMobile ? (el.getAttribute('data-i18n-en-short') || el.getAttribute('data-i18n-en')) : el.getAttribute('data-i18n-en');
      if (zh && en) el.textContent = lang === 'en' ? en : zh;
    }});
  }}
  updateMenuText();

  var menuResizeHandler = null;
  window.addEventListener('resize', function() {{
    if (menuResizeHandler) clearTimeout(menuResizeHandler);
    menuResizeHandler = setTimeout(updateMenuText, 100);
  }});

  // 5. Category/title attributes
  document.querySelectorAll('[data-i18n-cat]').forEach(function(el) {{
    var catKey = el.getAttribute('data-i18n-cat');
    el.textContent = t['cat-' + catKey] || catKey;
  }});
  document.querySelectorAll('[data-i18n-title]').forEach(function(el) {{
    var key = el.getAttribute('data-i18n-title');
    if (t[key]) el.setAttribute('title', t[key]);
  }});

  document.documentElement.classList.add('i18n-ready');
  var langBtn = document.getElementById('langToggle');
  if (langBtn) langBtn.textContent = lang === 'en' ? '\\u4e2d' : 'EN';
  document.documentElement.setAttribute('lang', lang === 'en' ? 'en' : 'zh-CN');
}}

// Init
if (document.readyState === 'loading') {{
  document.addEventListener('DOMContentLoaded', initI18n);
}} else {{
  initI18n();
}}

function initI18n() {{
  var lang = getLang();
  markOrigText();
  applyLang(lang);

  var langToggle = document.getElementById('langToggle');
  if (langToggle) {{
    langToggle.addEventListener('click', function() {{
      setLang(getLang() === 'zh' ? 'en' : 'zh');
    }});
  }}
  var langToggleMobile = document.getElementById('langToggleMobile');
  if (langToggleMobile) {{
    langToggleMobile.addEventListener('click', function() {{
      setLang(getLang() === 'zh' ? 'en' : 'zh');
    }});
  }}
}}
"""

with open(I18N_PATH, "w", encoding="utf-8") as f:
    f.write(i18n_js)

print(f"✓ i18n.js v4 written with {len(zh)} translations ({len(i18n_js)} bytes)")

# Also copy to dist if exists
dist_path = os.path.join(BASE, "dist", "assets", "js", "i18n.js")
os.makedirs(os.path.dirname(dist_path), exist_ok=True)
with open(dist_path, "w", encoding="utf-8") as f:
    f.write(i18n_js)
print(f"✓ Also copied to dist/")
