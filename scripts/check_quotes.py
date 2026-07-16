import re
c = open(r"D:\portfolio\temp_backup\convert.astro", encoding="utf-8").read()
script = re.search(r"<script>(.*?)</script>", c, re.DOTALL).group(1)

sq = script.count("'")
dq = script.count('"')
bt = script.count("`")
print(f"Single quotes: {sq} ({"even" if sq % 2 == 0 else "ODD!"})")
print(f"Double quotes: {dq} ({"even" if dq % 2 == 0 else "ODD!"})")
print(f"Backticks: {bt} ({"even" if bt % 2 == 0 else "ODD!"})")

# Find lines with odd quote counts
for i, line in enumerate(script.split("\n"), 1):
    sq_line = line.count("'")
    if sq_line % 2 != 0:
        print(f"L{i}: odd singles ({sq_line}): {line.strip()[:120]}")
    dq_line = line.count('"')
    if dq_line % 2 != 0:
        print(f"L{i}: odd doubles ({dq_line}): {line.strip()[:120]}")
    bt_line = line.count("`")
    if bt_line % 2 != 0:
        print(f"L{i}: odd backticks ({bt_line}): {line.strip()[:120]}")
