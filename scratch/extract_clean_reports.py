# -*- coding: utf-8 -*-
import re

def main():
    input_path = "scratch/report_details.txt"
    output_path = "scratch/clean_extracted_reports.txt"
    
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    pattern = r"=================== REPORT DATE: (\d{4}\.\d{2}\.\d{2}) ==================="
    parts = re.split(pattern, content)
    
    with open(output_path, "w", encoding="utf-8") as out:
        out.write("=== 各月份營運報表 AI 解析明細 ===\n\n")
        
        for i in range(1, len(parts), 2):
            date = parts[i]
            body = parts[i+1].strip()
            
            # 切分 step
            steps = re.split(r"## Step \d+", body)
            
            # 尋找含有分析數據的 MODEL 回覆
            # 我們尋找包含 "是的"、"Dashboard"、"新增" 等，且長度最長的回覆，通常這代表完整的圖片解析結果
            best_step = ""
            for s in steps:
                if ("MODEL" in s or "是的" in s or "新增" in s) and len(s) > len(best_step):
                    best_step = s
            
            out.write(f"=================== REPORT DATE: {date} ===================\n")
            if best_step:
                # 去除一些開頭的 metadata 行，例如 Created At 等
                clean_lines = []
                in_metadata = True
                for line in best_step.strip().split("\n"):
                    if in_metadata:
                        if line.startswith("Created At:") or line.startswith("Completed At:") or line.startswith("(MODEL)") or "permission grants" in line or line.startswith("- ") or line.strip() == "":
                            continue
                        else:
                            in_metadata = False
                    clean_lines.append(line)
                
                out.write("\n".join(clean_lines).strip())
            else:
                out.write("(無模型解析數據)")
            out.write("\n\n" + "="*80 + "\n\n")
            
    print("Successfully extracted clean reports to:", output_path)

if __name__ == "__main__":
    main()
