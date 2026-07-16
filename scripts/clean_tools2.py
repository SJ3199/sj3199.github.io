import re, os

BASE = r"D:\portfolio"
# Process files already in src/pages/tools/ (from earlier restore)
files = ["convert.astro", "resize.astro"]

for f in files:
    path = os.path.join(BASE, "src", "pages", "tools", f)
    if not os.path.exists(path):
        print(f"SKIP {f}: not found")
        continue
    with open(path, "r", encoding="utf-8") as fh:
        c = fh.read()
    
    # Strip __t() calls
    c = re.sub(r"__t\('[^']*'\)", lambda m: m.group(0)[4:], c)
    # Strip data-i18n attributes
    c = re.sub(r'\s*data-i18n="[^"]*"', "", c)
    
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(c)
    print(f"{f}: {len(c)} bytes")
    
print("Done")
