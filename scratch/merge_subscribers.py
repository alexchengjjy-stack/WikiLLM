import csv
import re
import sys
import codecs
from io import StringIO
from collections import defaultdict

file_path = r"C:\Users\alexc\.gemini\antigravity-ide\brain\49388b83-c002-4a3d-b958-4b5448c94f44\.system_generated\steps\352\content.md"
output_path = r"C:\Users\alexc\OneDrive\文件\WikiLLM\scratch\merged_list.md"

def extract_customers():
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find("收入,,客戶,,金額,Note")
    if start_idx == -1:
        print("Could not find start of customer data")
        return

    csv_data = content[start_idx:]
    reader = csv.reader(StringIO(csv_data))
    
    customers = []
    
    current_year = ""
    current_month = ""
    current_plan = ""

    for row in reader:
        if not row: continue
        if row[0].startswith("202") and not "SaaS" in row[1]:
            current_year = row[0][:4]
            continue
            
        if "月" in row[0] and "方案" in row[1]:
            current_month = row[0]
            current_plan = row[1]
            continue
            
        if "專業方案" in row[0] or "專業方案" in row[1]:
             current_plan = "專業版"
        elif "企業方案" in row[0] or "企業方案" in row[1]:
             current_plan = "企業版"
             
        if len(row) > 8:
            company_name = row[2].strip()
            note = row[5].strip()
            email = row[8].strip()
            
            if company_name and company_name != "客戶" and company_name != "Note":
                company_name = company_name.replace(" ", "")
                plan = current_plan
                if "企業" in note:
                    plan = "企業版"
                elif "專業" in note:
                    plan = "專業版"
                elif "API" in note:
                    plan = "API整合"
                
                if not plan: plan = "專業版"
                
                customers.append({
                    "company": company_name,
                    "email": email,
                    "plan": plan,
                    "note": note
                })
                
    unique_customers = {}
    for c in customers:
        key = c["company"] if c["company"] else c["email"]
        if not key: continue
        
        if key in unique_customers:
            if c["plan"] == "企業版" or c["plan"] == "API整合":
                unique_customers[key]["plan"] = c["plan"]
        else:
            unique_customers[key] = c
            
    grouped = defaultdict(list)
    for c in unique_customers.values():
        grouped[c["plan"]].append(c)
        
    with open(output_path, 'w', encoding='utf-8') as out_f:
        def print_markdown_table(plan_name, plan_customers):
            out_f.write(f"### {plan_name} ({len(plan_customers)} 家)\n")
            out_f.write("| 企業/客戶名稱 | Email | 備註資訊 |\n")
            out_f.write("| :--- | :--- | :--- |\n")
            for c in sorted(plan_customers, key=lambda x: x["company"]):
                name = c["company"] if c["company"] else "未提供"
                email = c["email"] if c["email"] else "-"
                note = c["note"][:40] + "..." if len(c["note"]) > 40 else c["note"]
                note = note.replace("\n", " ").replace("|", " ")
                out_f.write(f"| {name} | `{email}` | {note} |\n")
            out_f.write("\n")

        print_markdown_table("企業版 (Enterprise)", grouped.get("企業版", []))
        print_markdown_table("專業版 (Professional)", grouped.get("專業版", []))
        print_markdown_table("API 整合方案", grouped.get("API整合", []))
        
    print("Successfully wrote to", output_path)
    
if __name__ == "__main__":
    extract_customers()
