import os
import glob

raw_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM\raw"

# 我們做個遞迴搜尋，找尋所有包含 2026.06.02 或 分析報表 的檔案
files = []
for root, dirs, filenames in os.walk(raw_dir):
    for f in filenames:
        if "分析" in f or "2026.06.02" in f or "20260602" in f or "BreezySign" in f:
            files.append(os.path.join(root, f))

print("找到的可能 raw 檔案：")
for f in files:
    print(f"  - {os.path.relpath(f, raw_dir)}")
