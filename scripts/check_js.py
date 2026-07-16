# Check JS syntax
with open(r"D:\portfolio\public\assets\js\i18n.js", encoding="utf-8") as f:
    c = f.read()
open_braces = c.count("{")
close_braces = c.count("}")
print(f"Braces: open={open_braces}, close={close_braces}")
if open_braces != close_braces:
    print("BRACE MISMATCH!")

# Check each line for odd quote counts
for i, line in enumerate(c.split("\n")):
    if line.count("'") % 2 != 0:
        print(f"Line {i+1} has odd quotes: {line[:80]}")
    # Check for JSON-like syntax that might fail in JS
    if i < 10:
        print(f"Line {i+1}: {line[:80]}")
