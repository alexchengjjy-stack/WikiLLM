# -*- coding: utf-8 -*-
import os
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

wiki_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM"
index_path = os.path.join(wiki_dir, "wiki", "index.md")
log_path = os.path.join(wiki_dir, "wiki", "log.md")
result_txt = os.path.join(wiki_dir, "outputs", "arch_breezysign_generation_result.txt")

if not os.path.exists(result_txt):
    print(f"[ERROR] Result file {result_txt} not found. Task might still be running.")
    sys.exit(1)

# 讀取檔案名稱
with open(result_txt, "r", encoding="utf-8") as f:
    lines = f.readlines()

html_file = ""
pdf_file = ""
png_file = ""

for line in lines:
    if line.startswith("HTML:"):
        html_file = line.replace("HTML:", "").strip().replace("\\", "/")
    elif line.startswith("PDF:"):
        pdf_file = line.replace("PDF:", "").strip().replace("\\", "/")
    elif line.startswith("PNG:"):
        png_file = line.replace("PNG:", "").strip().replace("\\", "/")

# 從 html 檔名中擷取 timestamp 還有檔名
# 格式為 outputs/YYYYMMDD-HHMM-breezysign-architecture.html
html_basename = os.path.basename(html_file)
timestamp_match = re.match(r"(\d{8}-\d{4})", html_basename)
if timestamp_match:
    timestamp = timestamp_match.group(1)
else:
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M")

print(f"Detected timestamp: {timestamp}")
html_url = f"file:///c:/Users/alexc/OneDrive/文件/WikiLLM/outputs/{timestamp}-breezysign-architecture.html"
pdf_url = f"file:///c:/Users/alexc/OneDrive/文件/WikiLLM/outputs/{timestamp}-breezysign-architecture.pdf"
png_url = f"file:///c:/Users/alexc/OneDrive/文件/WikiLLM/outputs/{timestamp}-breezysign-architecture.png"

# 1. 刪除 10:47 產生的 breezy-brain-architecture_eraser 系列
eraser_old_files = [
    os.path.join(wiki_dir, "outputs", "20260529-1047-breezy-brain-architecture_eraser.html"),
    os.path.join(wiki_dir, "outputs", "20260529-1047-breezy-brain-architecture_eraser.pdf"),
    os.path.join(wiki_dir, "outputs", "20260529-1047-breezy-brain-architecture_eraser.png"),
    os.path.join(wiki_dir, "outputs", "arch_eraser_generation_result.txt")
]
for fpath in eraser_old_files:
    if os.path.exists(fpath):
        try:
            os.remove(fpath)
            print(f"Removed old temporary file: {fpath}")
        except Exception as e:
            print(f"Failed to remove {fpath}: {e}")

# 2. 更新 wiki/index.md 中的 Eraser.io 關係圖資訊
if os.path.exists(index_path):
    print("Reading wiki/index.md...")
    with open(index_path, "r", encoding="utf-8", errors="replace") as f:
        index_content = f.read()
    
    index_lines = index_content.splitlines()
    new_index_lines = []
    
    for line in index_lines:
        # 如果是原先 eraser.html 的行
        if "breezy-brain-architecture_eraser.html" in line or "breezysign-architecture.html" in line:
            line = f"* [BreezySign 產品核心關係圖 (Eraser.io 霓虹風格 HTML 版)]({html_url}) & [PDF 版本]({pdf_url}) ── 完美還原 V2 英文簡潔字體、發光 SVG 連接線條與高對比霓虹關係藍圖。"
            print(f"Updated index HTML line: {line}")
        # 如果是原先 eraser.png 的行
        elif "breezy-brain-architecture_eraser.png" in line or "breezysign-architecture.png" in line:
            line = f"* [BreezySign 產品核心關係圖 (Eraser.io 霓虹風格 PNG 圖檔)]({png_url}) ── 精確 16:9 (1920x1080) 無損截圖之高對比極簡英文版架構關係圖。"
            print(f"Updated index PNG line: {line}")
            
        new_index_lines.append(line)
        
    with open(index_path, "w", encoding="utf-8") as f:
        f.write("\n".join(new_index_lines) + "\n")
    print("[SUCCESS] wiki/index.md updated.")
else:
    print(f"[ERROR] index.md not found at {index_path}")

# 3. 更新 wiki/log.md
if os.path.exists(log_path):
    print("Reading wiki/log.md...")
    with open(log_path, "r", encoding="utf-8", errors="replace") as f:
        log_content = f.read()
        
    log_blocks = log_content.split("## [")
    new_blocks = []
    new_blocks.append(log_blocks[0])
    
    # 移除剛才 10:50 寫入的舊日誌 block
    for block in log_blocks[1:]:
        if "2026-05-29 10:50] update | BreezyBrain 霓虹架構關係圖更新" in block:
            print("Removing old 10:50 log entry...")
            continue
        new_blocks.append("## [" + block)
        
    log_content_cleaned = "".join(new_blocks)
    log_lines = log_content_cleaned.splitlines()
    
    insert_log_idx = -1
    for idx, line in enumerate(log_lines):
        if line.strip().startswith("## ["):
            insert_log_idx = idx
            break
            
    if insert_log_idx != -1:
        print(f"Inserting new log entry at line {insert_log_idx+1}...")
        log_entry = [
            f"## [2026-05-29 10:55] update | BreezySign 霓虹關係圖更新（高對比、大字體、純英文極簡描述版）",
            "- **操作人員**: LLM Agent (Antigravity)",
            "- **產出與變更**:",
            f"  - **新生成 HTML**: [{html_file}](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/{html_file})",
            f"  - **新生成 PDF**: [{pdf_file}](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/{pdf_file})",
            f"  - **新生成 PNG**: [{png_file}](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/{png_file})",
            "  - **更新索引**: [wiki/index.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/index.md)",
            "  - **清理暫存**: 刪除多餘的舊架構關係圖暫存檔案與舊日誌。",
            "- **關鍵發現與改善**:",
            "  - **大字體與高對比優化**: 遵照用戶反饋，將卡片字體與高度全面放大（卡片標題 15px、描述 11.5px、大標題 38px），並將背景調為極深黑，邊框粗度與霓虹連接線粗度加強，文字描述顏色改為高對比度的白色的 72% 透明度，大幅增強了深色底色與文字的視覺對比。",
            "  - **全英文與標題修正**: 將大標題正式正名為 **BreezySign Architecture**，且卡片內部所有描述改為簡潔的純英文，完美還原了 V2 PNG 藍圖的最美細節。",
            "" # 空行
        ]
        new_log_lines = log_lines[:insert_log_idx] + log_entry + log_lines[insert_log_idx:]
        with open(log_path, "w", encoding="utf-8") as f:
            f.write("\n".join(new_log_lines) + "\n")
        print("[SUCCESS] wiki/log.md updated.")
    else:
        print("[ERROR] Could not find header line starting with '## [' in log.md.")
else:
    print(f"[ERROR] log.md not found at {log_path}")
