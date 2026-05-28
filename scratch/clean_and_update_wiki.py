# -*- coding: utf-8 -*-
import os
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

wiki_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM"
index_path = os.path.join(wiki_dir, "wiki", "index.md")
log_path = os.path.join(wiki_dir, "wiki", "log.md")

# 1. 刪除多餘的 V7 檔案
v7_files = [
    os.path.join(wiki_dir, "outputs", "20260529-1041-breezy-brain-architecture_v7.html"),
    os.path.join(wiki_dir, "outputs", "20260529-1041-breezy-brain-architecture_v7.pdf"),
    os.path.join(wiki_dir, "outputs", "20260529-1041-breezy-brain-architecture_v7.png"),
    os.path.join(wiki_dir, "outputs", "arch_v7_generation_result.txt"),
    os.path.join(wiki_dir, "scratch", "generate_breezy_brain_arch_v7.py"),
    os.path.join(wiki_dir, "scratch", "update_wiki_v7.py")
]

for fpath in v7_files:
    if os.path.exists(fpath):
        try:
            os.remove(fpath)
            print(f"Removed temporary file: {fpath}")
        except Exception as e:
            print(f"Failed to remove {fpath}: {e}")

# 2. 更新 wiki/index.md
if os.path.exists(index_path):
    print("Reading wiki/index.md...")
    with open(index_path, "r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()
    
    new_lines = []
    skip = False
    for line in lines:
        # 移除剛才插入的 V7 兩行
        if "breezy-brain-architecture_v7" in line:
            print(f"Removing V7 reference from index: {line.strip()}")
            continue
            
        # 更新 Eraser.io 相關行
        if "breezy-brain-architecture_eraser.html" in line:
            # 替換為最新 1047 版本
            line = re.sub(
                r"outputs/\d{8}-\d{4}-breezy-brain-architecture_eraser\.html",
                "outputs/20260529-1047-breezy-brain-architecture_eraser.html",
                line
            )
            line = re.sub(
                r"outputs/\d{8}-\d{4}-breezy-brain-architecture_eraser\.pdf",
                "outputs/20260529-1047-breezy-brain-architecture_eraser.pdf",
                line
            )
            print(f"Updated Eraser HTML/PDF line in index: {line.strip()}")
            
        elif "breezy-brain-architecture_eraser.png" in line:
            line = re.sub(
                r"outputs/\d{8}-\d{4}-breezy-brain-architecture_eraser\.png",
                "outputs/20260529-1047-breezy-brain-architecture_eraser.png",
                line
            )
            print(f"Updated Eraser PNG line in index: {line.strip()}")
            
        new_lines.append(line)
        
    with open(index_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print("[SUCCESS] wiki/index.md updated.")
else:
    print(f"[ERROR] index.md not found at {index_path}")

# 3. 更新 wiki/log.md
if os.path.exists(log_path):
    print("Reading wiki/log.md...")
    with open(log_path, "r", encoding="utf-8", errors="replace") as f:
        log_content = f.read()
    
    # 我們需要找出剛才插入的 V7 日誌，並將其移除。
    # 剛才插入的日誌開頭是： "## [2026-05-29 10:45] update | BreezyBrain 標準分層版 V7"
    # 直到下一個 "## ["
    log_blocks = log_content.split("## [")
    new_blocks = []
    
    # log_blocks[0] 通常是檔頭或者空字元
    new_blocks.append(log_blocks[0])
    
    removed_v7 = False
    for block in log_blocks[1:]:
        if "2026-05-29 10:45] update | BreezyBrain 標準分層版 V7" in block:
            print("Found V7 log entry. Removing it...")
            removed_v7 = True
            continue
        new_blocks.append("## [" + block)
        
    log_content_cleaned = "".join(new_blocks)
    
    # 插入新的 V8 霓虹關係圖發布日誌
    log_lines = log_content_cleaned.splitlines()
    insert_log_idx = -1
    for idx, line in enumerate(log_lines):
        if line.strip().startswith("## ["):
            insert_log_idx = idx
            break
            
    if insert_log_idx != -1:
        print(f"Inserting Eraser log entry at line {insert_log_idx+1}...")
        eraser_log_entry = [
            "## [2026-05-29 10:50] update | BreezyBrain 霓虹架構關係圖更新與需求澄清回滾",
            "- **操作人員**: LLM Agent (Antigravity)",
            "- **產出與變更**:",
            "  - **新生成 HTML**: [outputs/20260529-1047-breezy-brain-architecture_eraser.html](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/outputs/20260529-1047-breezy-brain-architecture_eraser.html)",
            "  - **新生成 PDF**: [outputs/20260529-1047-breezy-brain-architecture_eraser.pdf](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/outputs/20260529-1047-breezy-brain-architecture_eraser.pdf)",
            "  - **新生成 PNG**: [outputs/20260529-1047-breezy-brain-architecture_eraser.png](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/outputs/20260529-1047-breezy-brain-architecture_eraser.png)",
            "  - **更新索引**: [wiki/index.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/index.md)",
            "  - **清理暫存**: 刪除誤產生的 V7（無箭頭玻璃卡片版）相關檔案與日誌 entry。",
            "- **關鍵發現與改善**:",
            "  - **需求澄清**: 經與用戶比對確認，「產品核心分層架構」採用 V6（玻璃卡片流程引導版）即為唯一正確版本。而用戶希望「額外加入」的另一種型式，實為 **Eraser.io 霓虹風格關係圖**（帶有 SVG 發光連接線條與英文簡潔卡片，如圖所示）。",
            "  - **霓虹風格更新**: 執行 `generate_breezy_brain_arch_eraser.py` 生成最新 10:47 時間戳版本，完整包含名片 OCR 採集、微型 CRM、電子簽核連動 CLM 與知識智庫 KM 的 SVG 連接線發光藍圖，並更新索引。",
            "" # 空行
        ]
        new_log_lines = log_lines[:insert_log_idx] + eraser_log_entry + log_lines[insert_log_idx:]
        with open(log_path, "w", encoding="utf-8") as f:
            f.write("\n".join(new_log_lines) + "\n")
        print("[SUCCESS] wiki/log.md updated.")
    else:
        print("[ERROR] Could not find insertion point in log.md.")
else:
    print(f"[ERROR] log.md not found at {log_path}")
