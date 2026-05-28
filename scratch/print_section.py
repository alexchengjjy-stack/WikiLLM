import sys

sys.stdout.reconfigure(encoding='utf-8')
file_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\analyses\breezybrain-mvp-roadmap.md"
with open(file_path, "r", encoding="utf-8", errors="replace") as f:
    lines = f.readlines()

for idx in range(47, 62):
    print(f"Line {idx+1:03d}: {lines[idx].rstrip()}")
