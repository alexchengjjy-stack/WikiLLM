# -*- coding: utf-8 -*-
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

wiki_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM"
log_path = os.path.join(wiki_dir, "wiki", "log.md")

if os.path.exists(log_path):
    print("Reading wiki/log.md...")
    with open(log_path, "r", encoding="utf-8", errors="replace") as f:
        log_content = f.read()
        
    log_lines = log_content.splitlines()
    insert_log_idx = -1
    for idx, line in enumerate(log_lines):
        if line.strip().startswith("## ["):
            insert_log_idx = idx
            break
            
    if insert_log_idx != -1:
        print(f"Inserting SPEC update log entry at line {insert_log_idx+1}...")
        log_entry = [
            "## [2026-05-29 11:06] update | BreezyBrain SPEC 嵌入兩款旗艦架構圖並重新編譯發布",
            "- **操作人員**: LLM Agent (Antigravity)",
            "- **產出與變更**:",
            "  - **修改規格書**: [wiki/products/breezy-brain/Product-Spec.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/products/breezy-brain/Product-Spec.md) ── 更新 Section 1.5 嵌入兩款旗艦級架構圖與連結。",
            "  - **新生成 HTML**: [outputs/BreezyBrain-Product-Spec.html](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/outputs/BreezyBrain-Product-Spec.html) ── 重新編譯生成包含高對比大圖的 SPEC 網頁版。",
            "  - **新生成 PDF**: [outputs/BreezyBrain-Product-Spec.pdf](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/outputs/BreezyBrain-Product-Spec.pdf) ── 重新編譯生成包含高對比大圖的規格書 PDF 旗艦版。",
            "- **關鍵發現與改善**:",
            "  - **完美嵌入架構圖**: 將 V6「產品核心分層架構藍圖（中文玻璃卡片版）」與 BreezySign「系統拓撲關係圖（英文霓虹發光連接線版）」的 PNG 圖片，利用絕對路徑無損嵌入規格書 Section 1.5 中，並提供線上自適應預覽與 PDF 下載超連結。",
            "  - **全書自動編譯**: 透過 `convert_spec_to_pdf.py` 調用 Edge Headless 完成 PDF 與 HTML 轉換，確保圖片及排版在規格書中皆能清晰大器、無損呈現。",
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
