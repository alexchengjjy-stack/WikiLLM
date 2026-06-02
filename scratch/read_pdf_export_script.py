import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

script_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch\export_2026h2_plan_to_pdf.py"

if os.path.exists(script_path):
    with open(script_path, 'rb') as f:
        data = f.read()
    content = data.decode('utf-8', errors='ignore')
    print("--- export_2026h2_plan_to_pdf.py CODE ---")
    print(content)
else:
    print("腳本不存在！")
