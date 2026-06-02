import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs\bzs\20260527-1228-bzs-2026h2-cross-department-plan.html"

if os.path.exists(html_path):
    with open(html_path, 'rb') as f:
        data = f.read()
    content = data.decode('utf-8', errors='ignore')
    
    cards = re.findall(r'<div class="glass-card">(.*?)</div>', content, re.DOTALL)
    print(f"總共找到 {len(cards)} 個 glass-card 區塊")
    
    # 我們只印出前 6 個卡片 (0 到 5)
    for idx in range(min(6, len(cards))):
        card = cards[idx]
        title_match = re.search(r'<h[23][^>]*>(.*?)</h[23]>', card, re.DOTALL)
        title = title_match.group(1).strip() if title_match else "前言"
        title = re.sub(r'<[^>]+>', '', title).strip()
        
        print(f"\n======================================")
        print(f"卡片 {idx+1}: {title}")
        print(f"======================================")
        
        items = re.findall(r'<li[^>]*>(.*?)</li>', card, re.DOTALL)
        if items:
            # 只印出前 5 個 li 項目
            for item in items[:6]:
                clean_item = re.sub(r'<[^>]+>', '', item).strip()
                print(f"  * {clean_item}")
            if len(items) > 6:
                print(f"  ... (還有 {len(items)-6} 個項目)")
        else:
            paragraphs = re.findall(r'<p[^>]*>(.*?)</p>', card, re.DOTALL)
            for p in paragraphs[:5]:
                clean_p = re.sub(r'<[^>]+>', '', p).strip()
                if clean_p:
                    print(f"  {clean_p}")
else:
    print("HTML 檔案不存在！")
