# -*- coding: utf-8 -*-
import re

def search_blocks():
    filepath = "scratch/parsed_report_data.txt"
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading: {e}")
        return

    # 我們用 REPORT SEARCH 來切分
    pattern = r"=================== REPORT SEARCH: (\d{4}\.\d{2}\.\d{2}) ==================="
    parts = re.split(pattern, content)
    
    print(f"Split parts count: {len(parts)}")
    
    # 儲存非重複的部分
    out_lines = []
    
    for i in range(1, len(parts), 2):
        date = parts[i]
        body = parts[i+1].strip()
        
        # 看看這個 body 裡是否包含 "是的"、"Dashboard"、"Never signing" 等
        # 我們檢查它的前 1000 字
        preview = body[:200].replace("\n", " ")
        print(f"Date: {date}, Body length: {len(body)}, Preview: {preview}")
        
        # 如果裡面包含了 2025.10.02 且跟 2025.10.02.md 的內容完全一樣，那就是重複的
        # 我們只想要真的屬於該月份的數據
        out_lines.append(f"\n=================== {date} ===================\n")
        out_lines.append(body)
        out_lines.append("\n" + "="*80 + "\n")
        
    with open("scratch/filtered_report_data.txt", "w", encoding="utf-8") as f_out:
        f_out.write("\n".join(out_lines))
    print("Filtered data written to scratch/filtered_report_data.txt")

if __name__ == "__main__":
    search_blocks()
