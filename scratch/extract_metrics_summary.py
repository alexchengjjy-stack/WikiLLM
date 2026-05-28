import re

with open("c:/Users/alexc/OneDrive/文件/WikiLLM/scratch/metrics_summary.txt", "r", encoding="utf-8") as f:
    content = f.read()

# 我們要找包含 Dashboard-Company 或 Dashboard-Income，以及對應內容的段落
# 由於這是一個日誌彙整檔案，我們可以按 Step 切分或抓取含有重要指標的區段

steps = re.split(r"## Step \d+", content)
relevant_steps = []

for idx, step in enumerate(steps):
    if "Dashboard-Company" in step or "Dashboard-Income" in step or "營運數據分析" in step or "新增公司" in step:
        relevant_steps.append((idx, step.strip()))

with open("c:/Users/alexc/OneDrive/文件/WikiLLM/scratch/metrics_analysis.txt", "w", encoding="utf-8") as out:
    out.write(f"共找到 {len(relevant_steps)} 個與指標相關的 Step 記錄。\n\n")
    for idx, step_content in relevant_steps:
        # 只保留前 2000 字
        preview = step_content if len(step_content) <= 3000 else step_content[:3000] + "\n... (已截斷)"
        out.write(f"=== Step {idx} ===\n")
        out.write(preview + "\n")
        out.write("="*80 + "\n\n")

print("Successfully generated metrics_analysis.txt")
