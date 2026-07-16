import re
with open(r"D:\portfolio\src\pages\tools\convert.astro", encoding="utf-8") as f:
    c = f.read()
matches = re.findall(r"__t\('[^']*'\)", c)
with open(r"D:\portfolio\scripts\_tcheck.txt", "w", encoding="utf-8") as f:
    for m in matches:
        ascii_m = m.encode('ascii', errors='backslashreplace').decode('ascii')
        f.write(ascii_m + "\n")
print("Written _tcheck.txt")
