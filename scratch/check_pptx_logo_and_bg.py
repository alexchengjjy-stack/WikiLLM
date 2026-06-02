import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

script_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch\generate_competitor_snapshot_pptx.py"

if os.path.exists(script_path):
    with open(script_path, 'rb') as f:
        data = f.read()
    content = data.decode('utf-8', errors='ignore')
    
    lines = content.split('\n')
    print("--- 檢查 generate_competitor_snapshot_pptx.py 的 logo 與顏色邏輯 ---")
    for idx, line in enumerate(lines):
        if any(x in line.lower() for x in ["logo", "bg", "rgb", "color", "slide_bg", "card"]):
            print(f"第 {idx+1:3d}: {line.strip()}")
else:
    print("腳本不存在！")
