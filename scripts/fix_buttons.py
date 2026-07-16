import re, os

BASE = r"D:\portfolio"
TOOLS = os.path.join(BASE, "src", "pages", "tools")

config = {
    "compress.astro":         {"ready": "开始压缩", "progress": "压缩中...", "done": "开始压缩"},
    "convert.astro":          {"ready": "开始转换", "progress": "转换中...", "done": "开始转换"},
    "resize.astro":           {"ready": "开始调整", "progress": "调整中...", "done": "开始调整"},
    "compress-to-size.astro": {"ready": "开始压缩", "progress": "压缩中...", "done": "开始压缩"},
}

for fname, labels in config.items():
    path = os.path.join(TOOLS, fname)
    if not os.path.exists(path):
        print(f"SKIP {fname}: not found")
        continue
    
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()
    
    original = c
    
    # 1. compressBtn text - processing state
    # Pattern: compressBtn.textContent = ''; (after setAttribute disabled)
    c = re.sub(
        r"(compressBtn\.setAttribute\('disabled',\s*'true'\);\s*\n\s*)compressBtn\.textContent\s*=\s*'';",
        r"\1compressBtn.textContent = '" + labels["progress"] + "';",
        c
    )
    
    # 2. compressBtn text - reset after completion
    # Pattern: compressBtn.removeAttribute... compressBtn.textContent = '';
    c = re.sub(
        r"(compressBtn\.removeAttribute\('disabled'\);\s*\n\s*)compressBtn\.textContent\s*=\s*'';",
        r"\1compressBtn.textContent = '" + labels["done"] + "';",
        c
    )
    
    # 3. downloadAllBtn text - two occurrences
    c = re.sub(
        r"downloadAllBtn\.textContent\s*=\s*'';",
        "downloadAllBtn.textContent = '📦 批量下载';",
        c
    )
    
    # 4. Preview count: ${''} ${state.files.length} ${''}
    c = re.sub(
        r"\$\{''\} \$\{state\.files\.length\} \$\{''\}",
        r"${'已选择'} ${state.files.length} ${'张图片'}",
        c
    )
    
    # 5. Progress text initial: progressText.textContent = '';
    c = re.sub(
        r"progressText\.textContent\s*=\s*'';",
        "progressText.textContent = '" + labels["progress"] + "';",
        c
    )
    
    # 6. Progress text in template: ${''}+space
    c = re.sub(
        r"\$\{''\} ",
        "${'" + labels["progress"] + "'} ",
        c
    )
    
    # 7. Fold icons (they show '?' - should show chevron)
    c = c.replace("foldIcon.textContent = '?';", "foldIcon.textContent = '\u25bc';")
    
    if c != original:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(c)
        print(f"FIXED {fname}")
    else:
        print(f"NO CHANGE {fname}")

print("Done")
