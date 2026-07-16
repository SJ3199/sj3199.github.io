import re, os

BASE = r"D:\portfolio"
TOOLS = os.path.join(BASE, "src", "pages", "tools")

config = {
    "compress.astro":         ("开始压缩", "压缩中..."),
    "convert.astro":          ("开始转换", "转换中..."),
    "resize.astro":           ("开始调整", "调整中..."),
    "compress-to-size.astro": ("开始压缩", "压缩中..."),
}

for fname, (ready, progress) in config.items():
    path = os.path.join(TOOLS, fname)
    if not os.path.exists(path):
        continue
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()
    
    original = c
    
    # Fix 1: Processing state button - setAttribute disabled then textContent = ''
    # Handle both CRLF and LF line endings
    c = re.sub(
        r"compressBtn\.setAttribute\('disabled',\s*'true'\);\s*\r?\n\s*compressBtn\.textContent\s*=\s*'[^']*';",
        "compressBtn.setAttribute('disabled', 'true');\n      compressBtn.textContent = '" + progress + "';",
        c
    )
    
    # Fix 2: Reset state button - removeAttribute disabled then textContent = ''
    c = re.sub(
        r"compressBtn\.removeAttribute\('disabled'\);\s*\r?\n\s*compressBtn\.textContent\s*=\s*'[^']*';",
        "compressBtn.removeAttribute('disabled');\n      compressBtn.textContent = '" + ready + "';",
        c
    )
    
    # Fix 3: downloadAllBtn textContent = ''
    c = re.sub(
        r"downloadAllBtn\.textContent\s*=\s*'[^']*';",
        "downloadAllBtn.textContent = '📦 批量下载';",
        c
    )
    
    # Fix 4: Preview count template literal
    c = re.sub(
        r"\$\{'已选择'\} \$\{state\.files\.length\} \$\{'张图片'\}",
        r"${'xxxselected'} ${state.files.length} ${'xxximages'}",
        c
    )
    c = c.replace("${'xxxselected'}", "${'已选择'}")
    c = c.replace("${'xxximages'}", "${'张图片'}")
    
    # Fix 5: progressText initial text (before loop)
    c = re.sub(
        r"progressText\.textContent\s*=\s*'压缩中\.\.\.';",
        "progressText.textContent = '" + progress + "';",
        c
    )
    
    # Fix 6: Progress text in for loop template literal
    c = re.sub(
        r"\$\{'压缩中\.\.\.'\} ",
        "${'" + progress + "'} ",
        c
    )
    
    # Fix 7: foldIcon question marks
    c = c.replace("foldIcon.textContent = '?';", "foldIcon.textContent = '▼';")
    
    if c != original:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(c)
        print(f"FIXED {fname}")
    else:
        print(f"NO CHANGE {fname}")

print("Done")
