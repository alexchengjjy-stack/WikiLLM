import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

script_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch\generate_competitor_snapshot_pptx.py"

if os.path.exists(script_path):
    with open(script_path, 'rb') as f:
        data = f.read()
    content = data.decode('utf-8', errors='ignore')
    print("--- generate_competitor_snapshot_pptx.py CODE ---")
    print(content)
else:
    print("腳本不存在！")
