import os
import re

saas_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM\raw\BZSdata\SaaS"
output_file = r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch\march_subs_extracted.txt"

march_files = sorted([f for f in os.listdir(saas_dir) if f.startswith("202603") and f.endswith(".md")])

extracted_data = []

for filename in march_files:
    filepath = os.path.join(saas_dir, filename)
    date_str = filename[:8]
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # 尋找客戶進展部分，通常會有 4、客戶進展： 到 5、數據統計：
    # 或者是直接搜尋包含「訂閱」的行
    lines = content.split('\n')
    
    print(f"Processing {filename}...")
    
    # 1. 搜尋包含「訂閱」的行，並印出前後三行
    for i, line in enumerate(lines):
        if "訂閱" in line:
            context = []
            start = max(0, i - 2)
            end = min(len(lines), i + 3)
            for j in range(start, end):
                context.append(f"  L{j+1}: {lines[j]}")
            extracted_data.append({
                'date': date_str,
                'file': filename,
                'type': 'subscription',
                'line_num': i + 1,
                'line_content': line,
                'context': "\n".join(context)
            })
            
    # 2. 搜尋 Contact Us / Leads / 諮詢進件
    # 通常在「1、註冊進件」或「2、聯絡專人進件」或「3、Line官方」中
    # 看看是否有提到公司名稱與跟進狀況
    # 我們也印出這些段落中提及的公司
    in_progress = False
    current_company = ""
    company_lines = []
    
    for i, line in enumerate(lines):
        if line.strip().endswith("：") and not line.strip().startswith("1、") and not line.strip().startswith("2、") and not line.strip().startswith("3、") and not line.strip().startswith("4、") and not line.strip().startswith("5、"):
            # 這可能是個公司標題，例如「星辰健康顧問有限公司：」
            if len(line.strip()) > 3 and len(line.strip()) < 30:
                if current_company:
                    # 儲存上一個公司的資訊
                    extracted_data.append({
                        'date': date_str,
                        'file': filename,
                        'type': 'company_progress',
                        'company': current_company,
                        'content': "\n".join(company_lines)
                    })
                current_company = line.strip().replace("：", "")
                company_lines = []
        elif current_company:
            if "5、數據統計：" in line or line.startswith("202603") and "日報:" in line:
                # 結束了
                extracted_data.append({
                    'date': date_str,
                    'file': filename,
                    'type': 'company_progress',
                    'company': current_company,
                    'content': "\n".join(company_lines)
                })
                current_company = ""
                company_lines = []
            else:
                company_lines.append(line)
                
    if current_company:
        extracted_data.append({
            'date': date_str,
            'file': filename,
            'type': 'company_progress',
            'company': current_company,
            'content': "\n".join(company_lines)
        })

# 寫入輸出檔案
with open(output_file, 'w', encoding='utf-8') as out:
    out.write("=== 3月份 CSM 日報數據提取結果 ===\n\n")
    
    out.write("## 一、訂閱相關記錄\n")
    for item in extracted_data:
        if item['type'] == 'subscription':
            out.write(f"日期: {item['date']} | 檔案: {item['file']} | 行: {item['line_num']}\n")
            out.write(f"內容: {item['line_content']}\n")
            out.write("上下文:\n")
            out.write(f"{item['context']}\n")
            out.write("-" * 50 + "\n")
            
    out.write("\n## 二、客戶進展詳細記錄\n")
    for item in extracted_data:
        if item['type'] == 'company_progress':
            out.write(f"日期: {item['date']} | 公司: {item['company']}\n")
            out.write("進展內容:\n")
            # 過濾空白行
            clean_lines = [l for l in item['content'].split('\n') if l.strip()]
            for l in clean_lines:
                out.write(f"  {l}\n")
            out.write("-" * 50 + "\n")

print(f"3月數據提取完成，已寫入 {output_file}")
