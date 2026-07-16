import re, os

BASE = r"D:\portfolio"
files = ["compress.astro", "convert.astro", "resize.astro"]

# FAQ corruption fixes (U+FFFD = replacement character)
faq_fixes = {
    "convert.astro": [
        ("\ufffd", ""),  # Remove all replacement chars first
        # Restore correct FAQ text
        ("可以将PNG 透明图转为JPG 吗", "可以将 PNG 透明图转为 JPG 吗？"),
        ("会自动填充为白色背景。", "会自动填充为白色背景。"),
        ("支持哪些输入格式", "支持哪些输入格式？"),
        ("等浏览器可识别的图片格式。", "等浏览器可识别的图片格式。"),
    ],
    "resize.astro": [
        ("\ufffd", ""),
    ],
    "compress.astro": [
        ("\ufffd", ""),
    ],
}

for f in files:
    src = os.path.join(BASE, "temp_backup", f)
    if not os.path.exists(src):
        print(f"SKIP {f}: not found")
        continue
    with open(src, "r", encoding="utf-8") as fh:
        c = fh.read()
    
    # Fix FAQ corruptions
    for old, new in faq_fixes.get(f, []):
        c = c.replace(old, new)
    
    # Strip __t() calls
    c = re.sub(r"__t\('([^']*)'\)", r"'\1'", c)
    # Strip data-i18n attributes
    c = re.sub(r'\s*data-i18n="[^"]*"', "", c)
    
    out = os.path.join(BASE, "src", "pages", "tools", f)
    with open(out, "w", encoding="utf-8", newline="") as fh:
        fh.write(c)
    print(f"{f}: {len(c)} bytes written")

print("Done")
