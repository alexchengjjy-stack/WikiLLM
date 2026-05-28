# -*- coding: utf-8 -*-
import re

with open('c:/Users/alexc/OneDrive/文件/WikiLLM/scratch/log_extracted_decoded.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 我們要尋找模型 (MODEL) 對報表圖片讀取的回覆。
# 通常模型回覆會在 "## Step X (MODEL)" 或類似的段落中。
# 我們可以把含有 "Step" 且後面有 "MODEL" 的區塊提取出來，或者尋找包含各個分析報表日期的段落。

# 尋找 "BreezySign分析報表 2025.10.02", "2025.11.03", "2025.12.02", "2026.01.05", "2026.02.02", "2026.03.03", "2026.04.02", "2026.05.05" 的內容
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

out = []
# 我們來用正則表達式切分步驟，或者直接尋找這些日期所在的 Step
# 歷史日誌格式看起來是 "## Step X (MODEL)"開頭，直到下一個 "## Step"
steps = re.split(r'## Step \d+', text)
for step in steps:
    # 檢查這個 step 裡面有沒有提到任何一個報表日期，且有數據內容
    found_dates = [d for d in dates if d in step]
    if found_dates and "MODEL" in step:
        # 這是一個模型的回答
        out.append("="*50)
        out.append(f"Found Step containing: {', '.join(found_dates)}")
        out.append("="*50)
        out.append(step.strip())

with open('c:/Users/alexc/OneDrive/文件/WikiLLM/scratch/report_data_extracted.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))

print("Extraction completed!")
