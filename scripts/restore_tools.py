import re, os

BASE = r"D:\portfolio"
# Process ALL files: temp_backup -> src/pages/tools/
files = ["compress.astro", "convert.astro", "resize.astro"]

for f in files:
    src = os.path.join(BASE, "temp_backup", f)
    if not os.path.exists(src):
        print(f"SKIP {f}: not found")
        continue
    with open(src, "r", encoding="utf-8") as fh:
        c = fh.read()
    
    # FIX: capture the inner string and reconstruct correctly
    # __t('xxx') -> 'xxx'
    c = re.sub(r"__t\('([^']*)'\)", r"'\1'", c)
    # Strip data-i18n attributes
    c = re.sub(r'\s*data-i18n="[^"]*"', "", c)
    
    out = os.path.join(BASE, "src", "pages", "tools", f)
    with open(out, "w", encoding="utf-8", newline="") as fh:
        fh.write(c)
    print(f"{f}: {len(c)} bytes written")

print("Done")
