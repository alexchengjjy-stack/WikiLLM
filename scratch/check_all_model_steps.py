# -*- coding: utf-8 -*-
import re

with open('c:/Users/alexc/OneDrive/文件/WikiLLM/scratch/log_extracted_decoded.md', 'r', encoding='utf-8') as f:
    text = f.read()

steps = re.split(r'## Step \d+', text)
out = []

# 我們想看每個含有 "MODEL" 且含有數據、圖表描述的 step 的概要
for idx, step in enumerate(steps):
    if "MODEL" in step:
        # 計算一下這個 step 裡面有多少個中文字或數據
        # 如果有 "Dashboard" 或是 "漏斗" 或是 "營收"
        keywords = ["Dashboard", "漏斗", "營收", "Paid Company", "Contact Us", "Leads", "Company"]
        found = [k for k in keywords if k.lower() in step.lower()]
        if len(found) >= 2:
            out.append(f"\n==================================================")
            out.append(f"Step {idx} - Found keywords: {found}")
            out.append(f"==================================================")
            # 擷取前500個字元和後500個字元，或者如果總長度小於3000就全寫
            if len(step) < 4000:
                out.append(step.strip())
            else:
                out.append(step[:2000].strip())
                out.append("\n... [TRUNCATED] ...\n")
                out.append(step[-2000:].strip())

with open('c:/Users/alexc/OneDrive/文件/WikiLLM/scratch/model_steps_summary.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))

print("Completed checking model steps!")
