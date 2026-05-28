# -*- coding: utf-8 -*-
import re

def main():
    input_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch\parsed_report_data.txt"
    output_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch\report_details.txt"
    
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # 我們用正則表達式把 REPORT SEARCH 分開
    # 分割的 pattern 匹配 "=================== REPORT SEARCH: 2025.10.02 ===================" 這樣的行
    pattern = r"={10,}\s*REPORT SEARCH:\s*(\d{4}\.\d{2}\.\d{2})\s*={10,}"
    
    parts = re.split(pattern, content)
    
    # split 結果是： [前導, 日期1, 內容1, 日期2, 內容2, ...]
    
    with open(output_path, "w", encoding="utf-8") as out:
        out.write("=== 提取的報表完整細節 ===\n")
        for i in range(1, len(parts), 2):
            date = parts[i]
            body = parts[i+1].strip()
            
            out.write(f"\n\n=================== REPORT DATE: {date} ===================\n")
            # 在 body 裡面，模型解析可能會有很多重複的 steps。我們只要把最長的 MODEL 回覆抓出來，或者直接寫出整個 body
            # 如果 body 太長，我們可以只保留包含數據的部分，或是保留整個 body
            # 這裡我們保留整個 body，因為這個檔案主要就是用來做參考的。
            out.write(body)
            out.write("\n" + "="*80 + "\n")
            
    print("Successfully compiled details to:", output_path)

if __name__ == "__main__":
    main()
