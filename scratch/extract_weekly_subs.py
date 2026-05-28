import os
import re

saas_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM\raw\BZSdata\SaaS"
h1_file = r"c:\Users\alexc\OneDrive\文件\WikiLLM\raw\BZSdata\小匯整\BreezySign SaaS 2026H1.md"
output_file = r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch\csm_subscriptions_summary.txt"

transactions = []

# 1. 解析 H1.md
if os.path.exists(h1_file):
    print("正在解析 H1 彙整文件...")
    with open(h1_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    current_date = "2026H1"
    in_sub_section = False
    sub_lines = []
    
    for i, line in enumerate(lines):
        # 尋找週報日期區段
        date_match = re.search(r'當週新訂閱：\((.*?)\)', line)
        if date_match:
            current_date = date_match.group(1)
            in_sub_section = True
            sub_lines = []
            continue
            
        if in_sub_section:
            if "註冊客戶且聯絡資料的品質" in line or "二、當週客戶情況" in line or "—-------------------------------------------" in line:
                in_sub_section = False
                # 處理收集到的行
                content = "".join(sub_lines)
                transactions.append({
                    'source': 'H1_Summary',
                    'date_range': current_date,
                    'content': content.strip()
                })
            else:
                sub_lines.append(line)

# 2. 解析 SaaS/ 目錄下的週報
for filename in os.listdir(saas_dir):
    if "週報" in filename and filename.endswith(".md"):
        filepath = os.path.join(saas_dir, filename)
        # 提取日期，例如 20260410BreezySign 0410 週報.md -> 20260410
        date_match = re.search(r'\d{8}', filename)
        file_date = date_match.group(0) if date_match else filename
        
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        in_section = False
        section_lines = []
        for line in lines:
            if "當週金額" in line or "當週新訂閱" in line:
                in_section = True
                section_lines = []
                continue
            if in_section:
                if "註冊客戶且聯絡資料的品質" in line or "企業方案(體驗版)測試" in line or "當週客戶情況" in line or "常用功能" in line:
                    in_section = False
                    transactions.append({
                        'source': filename,
                        'date_range': file_date,
                        'content': "".join(section_lines).strip()
                    })
                else:
                    section_lines.append(line)

# 輸出結果
with open(output_file, 'w', encoding='utf-8') as out:
    out.write("=== CSM 訂閱交易彙整 ===\n\n")
    for tx in transactions:
        out.write(f"來源: {tx['source']} | 期間: {tx['date_range']}\n")
        out.write(f"{tx['content']}\n")
        out.write("-" * 50 + "\n\n")

print(f"提取完成！結果已儲存至 {output_file}")
