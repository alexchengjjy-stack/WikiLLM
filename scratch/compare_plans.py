import csv
import re
from io import StringIO
import collections

pipedrive_file = r"C:\Users\alexc\.gemini\antigravity-ide\brain\49388b83-c002-4a3d-b958-4b5448c94f44\.system_generated\steps\263\content.md"
orders_file = r"C:\Users\alexc\.gemini\antigravity-ide\brain\49388b83-c002-4a3d-b958-4b5448c94f44\.system_generated\steps\53\content.md"

def parse_pipedrive():
    with open(pipedrive_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    csv_start = content.find("日期,免費版註冊數")
    csv_text = content[csv_start:]
    reader = csv.reader(StringIO(csv_text))
    headers = next(reader)
    
    col_date = headers.index("日期")
    
    # Try to find columns for plans. In the sheet preview: 
    # ...,專業版,商務版,企業版,"簡訊點數",...
    col_pro, col_biz, col_ent = -1, -1, -1
    for i, h in enumerate(headers):
        if "專業版" in h: col_pro = i
        if "商務版" in h: col_biz = i
        if "企業版" in h: col_ent = i
        
    print(f"Pipedrive Cols: Pro={col_pro}, Biz={col_biz}, Ent={col_ent}")
    
    counts = {"Pro": 0, "Biz": 0, "Ent": 0}
    
    for row in reader:
        if not row or len(row) <= max(col_pro, col_biz, col_ent):
            continue
            
        date_val = row[col_date].strip()
        # Only parse daily rows or total rows. Actually if we just sum total rows, it might be easier.
        if date_val.startswith("總計"):
            try:
                p = int(row[col_pro]) if row[col_pro].strip().isdigit() else 0
                b = int(row[col_biz]) if row[col_biz].strip().isdigit() else 0
                e = int(row[col_ent]) if row[col_ent].strip().isdigit() else 0
                counts["Pro"] += p
                counts["Biz"] += b
                counts["Ent"] += e
            except Exception as ex:
                pass
                
    return counts

def parse_orders():
    with open(orders_file, 'r', encoding='utf-8') as f:
        text = f.read()
        
    blocks = text.split("訂單編號:")
    
    counts = {"Pro": 0, "Biz": 0, "Ent": 0}
    
    for block in blocks[1:]:
        # Find exactly which plan it is.
        if "專業方案" in block or "Professional" in block:
            counts["Pro"] += 1
        elif "商務方案" in block or "Business" in block:
            counts["Biz"] += 1
        elif "企業方案" in block or "Enterprise" in block:
            counts["Ent"] += 1
            
    return counts

if __name__ == "__main__":
    try:
        pipe_counts = parse_pipedrive()
        print("=== PIPEDRIVE COUNTS (July 2024 - May 2026) ===")
        print(f"Professional: {pipe_counts['Pro']}")
        print(f"Business: {pipe_counts['Biz']}")
        print(f"Enterprise: {pipe_counts['Ent']}")
        total_pipe = pipe_counts['Pro'] + pipe_counts['Biz'] + pipe_counts['Ent']
        print(f"Total Plans Sold: {total_pipe}")
    except Exception as e:
        print("Error parsing Pipedrive:", e)
        
    print("\n")
    
    try:
        order_counts = parse_orders()
        print("=== ORDERS COUNTS (from raw transactions 2023-2026) ===")
        print(f"Professional: {order_counts['Pro']}")
        print(f"Business: {order_counts['Biz']}")
        print(f"Enterprise: {order_counts['Ent']}")
        total_order = order_counts['Pro'] + order_counts['Biz'] + order_counts['Ent']
        print(f"Total Plans Sold: {total_order}")
    except Exception as e:
        print("Error parsing Orders:", e)
