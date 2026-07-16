"""Add __t() calls to JS dynamic text in tool pages"""
import re, os

BASE = r"D:\portfolio"
PAGES = [
    "src/pages/tools/convert.astro",
    "src/pages/tools/resize.astro",
    "src/pages/tools/compress-to-size.astro",
]

replacements = [
    # Button text
    ("'准备中...'", "__t('准备中...')"),
    ("'完成！'", "__t('完成！')"),
    ("'清空全部'", "__t('清空全部')"),
    ("'转换中…'", "__t('转换中…')"),
    ("'调整中…'", "__t('调整中…')"),
    ("'压缩中…'", "__t('压缩中…')"),
    ("'开始转换'", "__t('开始转换')"),
    ("'开始调整'", "__t('开始调整')"),
    ("'开始压缩'", "__t('开始压缩')"),
    ("'\U0001f4e6 批量下载'", "__t('\U0001f4e6 批量下载')"),
    ("'\u23f3 打包中...'", "__t('\u23f3 打包中...')"),
    ("'下载'", "__t('下载')"),
    ("'批量下载失败'", "__t('批量下载失败')"),
    ("alert('批量下载失败')", "alert(__t('批量下载失败，请尝试逐个下载'))"),
    ("alert('一次最多处理 50 张图片')", "alert(__t('一次最多处理 50 张图片'))"),
    ("'一次最多处理 50 张图片'", "__t('一次最多处理 50 张图片')"),
    # Progress text
    ("'正在转换 '", "__t('正在转换') + ' '"),
    ("'正在调整 '", "__t('正在调整') + ' '"),
    ("'正在压缩 '", "__t('正在压缩') + ' '"),
    # Summary
    ("'共转换 '", "__t('共转换') + ' '"),
    ("'共调整 '", "__t('共调整') + ' '"),
    ("' 张图片'", "' ' + __t('张图片')"),
    ("'，体积变化 '", "' ' + __t('体积变化') + ' '"),
    # Preview
    ("'已选择 '", "__t('已选择') + ' '"),
    ("' 张图片'", "' ' + __t('张图片')"),
    # Download button title
    ('title="下载"', 'title="' + "__t('下载')" + '"'),
]

for page_rel in PAGES:
    page_path = os.path.join(BASE, page_rel)
    with open(page_path, "r", encoding="utf-8") as f:
        content = f.read()

    changes = 0
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            changes += 1
    
    with open(page_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"{os.path.basename(page_rel)}: {changes} replacements")
