import re, os

BASE = r"D:\portfolio"

for fname in ["convert.astro", "resize.astro", "compress-to-size.astro"]:
    path = os.path.join(BASE, "src", "pages", "tools", fname)
    with open(path, encoding="utf-8") as f:
        content = f.read()
    
    try:
        idx = content.index("<script>")
    except ValueError:
        print(f"{fname}: no <script>")
        continue
    
    script = content[idx:]
    
    # Find lines with Chinese text in strings
    has_chinese = re.compile(r'[\u4e00-\u9fff]')
    
    for i, line in enumerate(script.split('\n')):
        if has_chinese.search(line) and ('"' in line or "'" in line):
            # Extract quoted strings
            for m in re.finditer(r"'([^']*)'", line):
                s = m.group(1)
                if has_chinese.search(s) and '__t(' not in s:
                    print(f"{fname}:{idx + i}: '{s[:60]}'")
    
    # Check for __t usage
    t_count = script.count("__t(")
    print(f"  __t() calls: {t_count}")
    print()
