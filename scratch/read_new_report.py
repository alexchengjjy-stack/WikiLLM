import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

raw_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM\raw"

# 尋找 2026.06.02 的營運檔案
target_file = None
for root, dirs, filenames in os.walk(raw_dir):
    for f in filenames:
        if "2026.06.02" in f and "BreezySign" in f:
            target_file = os.path.join(root, f)
            break

if target_file:
    print(f"尋找到的檔案完整路徑: {target_file}")
    with open(target_file, 'rb') as f:
        data = f.read()
    content = data.decode('utf-8', errors='ignore')
    print("--- 檔案內容 ---")
    print(content)
else:
    print("找不到 2026.06.02 營運報告！")
