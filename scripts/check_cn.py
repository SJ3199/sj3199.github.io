import re, os, json

BASE = r"D:\portfolio"

for fname in ["convert.astro", "resize.astro", "compress-to-size.astro", "compress.astro"]:
    path = os.path.join(BASE, "src", "pages", "tools", fname)
    with open(path, encoding="utf-8") as f:
        content = f.read()
    try:
        idx = content.index("<script>")
    except ValueError:
        continue
    script = content[idx:]
    has_chinese = re.compile(r'[\u4e00-\u9fff]')
    t_count = script.count("__t(")
    cn_count = 0
    for line in script.split('\n'):
        if has_chinese.search(line):
            for m in re.finditer(r"'([^']*)'", line):
                s = m.group(1)
                if has_chinese.search(s) and '__t(' not in s and 'title=' not in line:
                    cn_count += 1
    out_file = f"{fname}_check.txt"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(f"__t_calls={t_count}, cn_strings_without_itt={cn_count}\n")
