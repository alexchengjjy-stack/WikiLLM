import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs\bzs\bzs-esign-monitoring-snapshot-202606-20260602-1306-v1.html"

if os.path.exists(html_path):
    with open(html_path, 'rb') as f:
        data = f.read()
    content = data.decode('utf-8', errors='ignore')
    
    print("--- HTML 快照核心內容大綱 ---")
    
    headings = re.findall(r'<(h[1-4])[^>]*>(.*?)</\1>', content, re.DOTALL | re.IGNORECASE)
    for tag, text in headings:
        clean_text = re.sub(r'<[^>]+>', '', text).strip()
        indent = "  " * (int(tag[1]) - 1)
        print(f"{indent}- {tag.upper()}: {clean_text}")
        
    print("\n--- 檢查是否有表格 ---")
    tables = re.findall(r'<table[^>]*>(.*?)</table>', content, re.DOTALL | re.IGNORECASE)
    print(f"找到 {len(tables)} 個表格")
else:
    print("HTML 檔案不存在！")
