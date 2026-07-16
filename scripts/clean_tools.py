import re, os

BASE = r"D:\portfolio"
files = ["compress.astro", "convert.astro", "resize.astro"]

for f in files:
    path = os.path.join(BASE, "temp_backup", f)
    with open(path, "r", encoding="utf-8") as fh:
        c = fh.read()
    
    # Strip __t() calls
    c = re.sub(r"__t\('[^']*'\)", lambda m: m.group(0)[4:], c)
    # Strip data-i18n attributes
    c = re.sub(r'\s*data-i18n="[^"]*"', "", c)
    
    out = os.path.join(BASE, "src", "pages", "tools", f)
    with open(out, "w", encoding="utf-8", newline="") as fh:
        fh.write(c)
    print(f"{f}: {len(c)} bytes")
    
print("Done")
