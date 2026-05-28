import sys

sys.stdout.reconfigure(encoding='utf-8')
file_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\products\breezy-brain\Product-Spec.md"

with open(file_path, "r", encoding="utf-8", errors="replace") as f:
    content = f.read()

content = content.replace("\r\n", "\n")
lines = content.split("\n")

def dump_section(header, num_lines):
    idx = -1
    for i, line in enumerate(lines):
        if header in line:
            idx = i
            break
    if idx != -1:
        print(f"=== FOUND {header} ===")
        section_lines = lines[idx:idx+num_lines]
        print(repr("\n".join(section_lines)))
    else:
        print(f"=== NOT FOUND {header} ===")

dump_section("#### 3.5.1", 6)
dump_section("#### 3.5.5", 5)
