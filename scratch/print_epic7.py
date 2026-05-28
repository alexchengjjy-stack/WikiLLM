import sys

sys.stdout.reconfigure(encoding='utf-8')
file_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\products\breezy-brain\Product-Spec.md"
with open(file_path, "r", encoding="utf-8", errors="replace") as f:
    lines = f.readlines()

for i in range(179, min(202, len(lines))):
    print(f"Line {i+1:04d}: {lines[i].rstrip()}")
