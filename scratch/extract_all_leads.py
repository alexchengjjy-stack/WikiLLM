# -*- coding: utf-8 -*-
import re

with open('c:/Users/alexc/OneDrive/文件/WikiLLM/scratch/log_extracted_decoded.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 搜尋所有提到 Leads, Contact Us, 喜事來, 聯尚, 恩主公醫院, 亞聯工程 等的段落
# 我們來列印出包含這些關鍵字的 Step 模型回答
steps = re.split(r'## Step \d+', text)
leads_info = []

for step in steps:
    if "MODEL" in step:
        # 如果有提到 "Contact Us Leads" 或是具體公司名
        keywords = ["Contact Us Leads", "Leads", "喜事來", "聯尚", "恩主公", "聯華", "太平洋", "富友"]
        found = [k for k in keywords if k.lower() in step.lower()]
        if found:
            # 找到包含該關鍵字的步驟，我們將這個步驟的日期與相關的行提取出來
            lines = step.strip().split('\n')
            # 提取前幾行看是哪個日期
            date_info = "Unknown Date"
            for line in lines[:10]:
                if "BreezySign分析報表" in line or "Created At" in line:
                    date_info = line.strip()
                    break
            
            leads_info.append("="*60)
            leads_info.append(f"Source: {date_info} | Found keywords: {', '.join(found)}")
            leads_info.append("="*60)
            # 篩選出包含關鍵字的行以及前後3行
            for i, line in enumerate(lines):
                if any(k.lower() in line.lower() for k in keywords):
                    start = max(0, i-3)
                    end = min(len(lines), i+4)
                    leads_info.append(f"--- Context (lines {start}-{end}) ---")
                    for j in range(start, end):
                        leads_info.append(f"  {lines[j]}")
                    leads_info.append("-" * 30)

with open('c:/Users/alexc/OneDrive/文件/WikiLLM/scratch/leads_search_result.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(leads_info))

print("Search completed!")
