import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

file_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\analyses\breezybrain-mvp-roadmap.md"
try:
    print("Starting to read file...")
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()
    print(f"Total lines: {len(lines)}")
    for idx, line in enumerate(lines):
        if line.startswith("#"):
            print(f"Line {idx+1:03d}: {line.strip()}")
except Exception as e:
    print(f"Error occurred: {e}", file=sys.stderr)
