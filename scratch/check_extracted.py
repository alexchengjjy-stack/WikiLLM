import re

with open("c:/Users/alexc/OneDrive/文件/WikiLLM/scratch/parsed_report_data.txt", "r", encoding="utf-8") as f:
    content = f.read()

# 找出所有類似 REPORT SEARCH 或日期區段的標記
matches = re.finditer(r"={10,}\s*(REPORT SEARCH:.*?|Found Step.*?)\s*={10,}", content)
titles = [m.group(0) for m in matches]

blocks = re.split(r"={10,}\s*(?:REPORT SEARCH:.*?|Found Step.*?)\s*={10,}", content)

with open("c:/Users/alexc/OneDrive/文件/WikiLLM/scratch/check_extracted_utf8.txt", "w", encoding="utf-8") as out:
    out.write("=== 提取報表區塊大綱 ===\n")
    for t in titles:
        out.write(t + "\n")
        
    out.write("\n=== 各區段長度與前300字預覽 ===\n")
    for i in range(1, len(blocks), 2):
        title = blocks[i].strip()
        body = blocks[i+1].strip() if i+1 < len(blocks) else ""
        out.write(f"【{title}】(字數: {len(body)})\n")
        out.write(body[:300] + "\n")
        out.write("-" * 50 + "\n")
        
print("Successfully generated check_extracted_utf8.txt")
