# -*- coding: utf-8 -*-
import re

def main():
    input_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch\parsed_report_data.txt"
    output_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch\report_summaries_clean.txt"
    
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # 我們要尋找的 8 個報表日期
    dates = [
        "2025.10.02",
        "2025.11.03",
        "2025.12.02",
        "2026.01.05",
        "2026.02.02",
        "2026.03.03",
        "2026.04.02",
        "2026.05.05"
    ]
    
    # 我們在 parsed_report_data.txt 中尋找包含 "REPORT SEARCH: <date>" 之後的 MODEL 回覆
    # 或是直接搜尋 "Found Step containing: <date>" 之後的內容
    # 因為這個檔案是由 check_extracted.py 產生的，我們來看一下它是怎麼切分的。
    # check_extracted.py 的邏輯是：在 parsed_report_data.txt 中寫入 "=================== REPORT SEARCH: <date> ===================" 之後的部分。
    # 讓我們用正則表達式切分。
    
    pattern = r"=================== REPORT SEARCH: (\d{4}\.\d{2}\.\d{2}) ==================="
    parts = re.split(pattern, content)
    
    results = {}
    # re.split 會回傳 [前導文字, 日期1, 內容1, 日期2, 內容2, ...]
    for i in range(1, len(parts), 2):
        date = parts[i]
        body = parts[i+1]
        
        # 在 body 中，尋找 AI 解析的內容。AI 解析通常在 "MODEL" 或 "是的，我能看到" 或 "### 一、" 開始的區塊。
        # 我們把 body 的前 3000 字提取出來，過濾掉一些 meta 資訊。
        # 尋找 "是的，我能看到" 或是 "### " 之後的內容
        model_index = body.find("(MODEL)")
        if model_index != -1:
            body_from_model = body[model_index:]
        else:
            body_from_model = body
            
        results[date] = body_from_model[:4000] # 限制長度，只看前 4000 字
        
    with open(output_path, "w", encoding="utf-8") as out:
        for date in dates:
            out.write(f"\n=================== REPORT DATE: {date} ===================\n")
            if date in results:
                out.write(results[date])
            else:
                out.write("No data found.\n")
            out.write("\n" + "="*50 + "\n")
            
    print("Extraction complete. Output written to:", output_path)

if __name__ == "__main__":
    main()
