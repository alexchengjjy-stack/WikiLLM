# -*- coding: utf-8 -*-
import re

# 讀取 merged_list.md
with open('c:/Users/alexc/OneDrive/文件/WikiLLM/scratch/merged_list.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

customers = []
current_plan = ""

for line in lines:
    line = line.strip()
    if line.startswith("###"):
        current_plan = line.replace("###", "").strip()
        continue
    if "|" in line and not line.startswith("| :---") and not line.startswith("| 企業/客戶名稱"):
        parts = [p.strip() for p in line.split("|")]
        if len(parts) >= 4:
            name = parts[1]
            email = parts[2]
            note = parts[3]
            customers.append({
                "plan_group": current_plan,
                "name": name,
                "email": email,
                "note": note
            })

ranges = [
    {"name": "1/1~1/16", "month": 1, "start_day": 1, "end_day": 16, "list": []},
    {"name": "2/1~2/15", "month": 2, "start_day": 1, "end_day": 15, "list": []},
    {"name": "3/1~3/14", "month": 3, "start_day": 1, "end_day": 14, "list": []},
    {"name": "4/1~4/18", "month": 4, "start_day": 1, "end_day": 18, "list": []}
]

date_pat = re.compile(r'(\d+)/(\d+)')

for c in customers:
    note = c["note"]
    m = date_pat.search(note)
    if m:
        month = int(m.group(1))
        day = int(m.group(2))
        
        # 比對是否在區間內
        for r in ranges:
            if month == r["month"] and r["start_day"] <= day <= r["end_day"]:
                r["list"].append(c)
                break

# 將結果寫入 UTF-8 檔案
output_path = 'c:/Users/alexc/OneDrive/文件/WikiLLM/scratch/missing_paid_companies.txt'
with open(output_path, 'w', encoding='utf-8') as f:
    for r in ranges:
        f.write(f"\n=== 區間: {r['name']} (共 {len(r['list'])} 筆) ===\n")
        for item in r["list"]:
            f.write(f"[{item['plan_group']}] {item['name']} | 備註: {item['note']}\n")

print("File written successfully!")
