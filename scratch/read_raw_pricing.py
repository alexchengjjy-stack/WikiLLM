import os
import sys
import glob

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM\raw\BZSdata\eSign"
files = glob.glob(os.path.join(base_dir, "*BreezySign*"))

if files:
    file_path = files[0]
    print(f"讀取檔案: {file_path}")
    with open(file_path, 'rb') as f:
        data = f.read()
    content = data.decode('utf-8', errors='ignore')
    print("--- RAW FILE 1 CONTENT (300 to 600 lines) ---")
    lines = content.split('\n')
    for i in range(300, min(600, len(lines))):
        print(f"{i+1:3d}: {lines[i]}")
else:
    print("找不到原始檔案！")
