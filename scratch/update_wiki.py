# -*- coding: utf-8 -*-
import os
import sys

# 強制 UTF-8 輸出
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

wiki_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM"
index_path = os.path.join(wiki_dir, "wiki", "index.md")
log_path = os.path.join(wiki_dir, "wiki", "log.md")

# 1. 更新 wiki/index.md (因為剛才已經成功更新過了，我們先重新檢查一下，以防重複插入)
if os.path.exists(index_path):
    print("Reading wiki/index.md...")
    with open(index_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
        
    if "breezy-brain-architecture_v6.html" not in content:
        # 如果還沒插入，重新讀取行並插入
        with open(index_path, "r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()
        
        insert_idx = -1
        for idx, line in enumerate(lines):
            if "breezy-brain-architecture_v5.html" in line:
                insert_idx = idx
                break
                
        if insert_idx != -1:
            print(f"Found V5 reference at line {insert_idx+1}. Inserting V6 above it...")
            v6_lines = [
                "* [BreezyBrain 產品核心分層架構 v6 (HTML 版本)](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/outputs/20260529-1033-breezy-brain-architecture_v6.html) & [PDF 版本](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/outputs/20260529-1033-breezy-brain-architecture_v6.pdf) ── 完美還原 V3 比例與彈性佈局（移除寫死尺寸以消除滾動條），並找回 BPM 與垂直數據流箭頭 (workflow-arrow)，同時保留 V5 SVG 發光小圖示與 hover 懸停動效的旗艦版本。\n",
                "* [BreezyBrain 產品核心分層架構 v6 (PNG 橫幅圖檔)](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/outputs/20260529-1033-breezy-brain-architecture_v6.png) ── 精確 16:9 (1920x1080) 無損截圖之 V6 旗艦版架構藍圖。\n"
            ]
            new_lines = lines[:insert_idx] + v6_lines + lines[insert_idx:]
            with open(index_path, "w", encoding="utf-8") as f:
                f.writelines(new_lines)
            print("[SUCCESS] wiki/index.md updated.")
    else:
        print("[NOTE] V6 reference already exists in index.md. Skipping.")
else:
    print(f"[ERROR] index.md not found at {index_path}")

# 2. 更新 wiki/log.md (加上 errors="replace")
if os.path.exists(log_path):
    print("Reading wiki/log.md...")
    with open(log_path, "r", encoding="utf-8", errors="replace") as f:
        log_content = f.read()
    
    # 尋找第一個 "## [" 作為日誌插入點，將 v6 插入至最頂部
    log_lines = log_content.splitlines()
    insert_log_idx = -1
    for idx, line in enumerate(log_lines):
        if line.strip().startswith("## ["):
            insert_log_idx = idx
            break
            
    if insert_log_idx != -1:
        print(f"Inserting V6 log entry at line {insert_log_idx+1}...")
        v6_log_entry = [
            "## [2026-05-29 10:35] update | BreezyBrain 旗艦版 V6 產品核心分層架構圖產生與發布",
            "- **操作人員**: LLM Agent (Antigravity)",
            "- **產出與變更**:",
            "  - **新生成 HTML**: [outputs/20260529-1033-breezy-brain-architecture_v6.html](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/outputs/20260529-1033-breezy-brain-architecture_v6.html)",
            "  - **新生成 PDF**: [outputs/20260529-1033-breezy-brain-architecture_v6.pdf](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/outputs/20260529-1033-breezy-brain-architecture_v6.pdf)",
            "  - **新生成 PNG**: [outputs/20260529-1033-breezy-brain-architecture_v6.png](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/outputs/20260529-1033-breezy-brain-architecture_v6.png)",
            "  - **更新索引**: [wiki/index.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/index.md)",
            "- **關鍵發現與改善**:",
            "  - **還原精緻比例**: 捨棄了 V5 中將 body 寬高寫死為 `1920x1080` 的冗餘限制，改用 V3 的彈性自適應設計搭配 `min-height: 100vh` 居中佈局，既能在一般瀏覽器上完美自適應呈現（無滾動條），亦能在 Edge Headless 視窗中精準輸出 1920x1080 的 16:9 無損截圖。",
            "  - **補回核心數據流**: 補回了 V5 中缺失的 BPM 引擎卡片，並重新引入各卡片之間的垂直箭頭指示器 (`.workflow-arrow`)，完整呈現 BCR ➡️ CRM ➡️ BPM ➡️ CLM ➡️ KM 的數據閉環。",
            "  - **整合發光與動效**: 保留了 V5 精美的 SVG 圖示與發光效果，並保留了 CSS hover 懸停動效，在科技感與閱讀舒適性上皆超越先前所有版本。",
            "" # 空行
        ]
        
        new_log_lines = log_lines[:insert_log_idx] + v6_log_entry + log_lines[insert_log_idx:]
        with open(log_path, "w", encoding="utf-8") as f:
            f.write("\n".join(new_log_lines) + "\n")
        print("[SUCCESS] wiki/log.md updated.")
    else:
        print("[ERROR] Could not find header line starting with '## [' in log.md.")
else:
    print(f"[ERROR] log.md not found at {log_path}")
