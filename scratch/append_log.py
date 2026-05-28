# -*- coding: utf-8 -*-
import os
from datetime import datetime

log_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\log.md"
if not os.path.exists(log_path):
    print("log.md not found")
    exit(1)

with open(log_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找出 Frontmatter 的結束位置（第二個 --- 行）
fm_count = 0
insert_index = 0
for idx, line in enumerate(lines):
    if line.strip() == "---":
        fm_count += 1
        if fm_count == 2:
            insert_index = idx + 1
            break

# 取得目前時間並組裝日誌內容
current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
new_log_entry = f"""
## [{current_time}] update | 於 BreezyBrain 規格書中加入雙旗艦級架構展示圖 (形式三與形式四)
- **操作人員**: LLM Agent (Antigravity)
- **產出與變更**:
  - **修改規格書**: [Product-Spec.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/products/breezy-brain/Product-Spec.md) ── 更新 Section 1.5 將架構圖形式擴充為四種，新增嵌入「BreezyBrain 智慧工作流操作系統架構圖 (breezy_brain_framework.png)」與「WikiLLM Agent 系統架構編排藍圖 (wikillm_agent_framework.png)」，同步 frontmatter `date_updated` 為 2026-05-29。
  - **修改輔助腳本**: [edit_spec_architecture.py](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/scratch/edit_spec_architecture.py) ── 同步更新規格更新輔助腳本以與主規格書同步。
  - **修改目錄**: [index.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/index.md) ── 註冊並微調規格書簡介，標註包含四種形式的架構圖。
  - **新編譯 HTML**: [BreezyBrain-Product-Spec.html](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/outputs/BreezyBrain-Product-Spec.html) ── 包含四種架構圖的新規格書網頁。
  - **新編譯 PDF**: [BreezyBrain-Product-Spec.pdf](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/outputs/BreezyBrain-Product-Spec.pdf) ── 包含四種架構圖的新規格書 PDF 文件。
- **關鍵發現與改善**:
  - **豐富視覺縱深**: 導入地端 RAG 大腦推理與 RAG 數據流向的兩大旗艦級深藍色霓虹發光風格架構圖，使得產品在說明大腦算力與 Agent Pipeline 時具備更完善的科技視覺美感與專業度。
"""

# 在 Frontmatter 結束後插入日誌
lines.insert(insert_index, new_log_entry)

with open(log_path, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("[SUCCESS] log.md successfully updated with UTF-8 encoding.")
