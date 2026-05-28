import sys

sys.stdout.reconfigure(encoding='utf-8')
file_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\products\breezy-brain\Product-Spec.md"
with open(file_path, "r", encoding="utf-8", errors="replace") as f:
    lines = f.readlines()

start_idx = -1
for idx, line in enumerate(lines):
    if "### 3.5" in line or "3.5 BreezyBrain" in line:
        start_idx = idx
        break

if start_idx != -1:
    print(f"Found section 3.5 at Line {start_idx+1}")
    for idx in range(start_idx, len(lines)):
        print(f"Line {idx+1:03d}: {lines[idx].rstrip()}")
else:
    print("Section 3.5 not found")
