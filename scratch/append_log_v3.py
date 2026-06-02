import os

file_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\log.md"

if os.path.exists(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    
    content = data.decode('utf-8', errors='ignore')
    
    parts = content.split('---', 2)
    if len(parts) >= 3:
        frontmatter = parts[1]
        body = parts[2]
        
        new_log = """
## [2026-06-02 13:06] update | 修復 2026 年 6 月情報普查快照中 logo 缺失之問題
- **操作人**: LLM Agent (Antigravity)
- **變更與修改**:
  - **修復檔案**: outputs/assets/bzs-logo-green.png, outputs/assets/bzs-logo-white.png
  - **重新生成檔案**: 
    - [bzs-esign-monitoring-snapshot-202606-20260602-1306-v1.html](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/outputs/bzs/bzs-esign-monitoring-snapshot-202606-20260602-1306-v1.html)
    - [bzs-esign-monitoring-snapshot-202606-20260602-1306-v1.pdf](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/outputs/bzs/bzs-esign-monitoring-snapshot-202606-20260602-1306-v1.pdf)
  - **說明**: 修正了 `process_logo.py` 輸出路徑（`outputs/`）與 `generate_competitor_snapshot_pdf.py` 讀取路徑（`outputs/assets/`）不一致的問題。在 `outputs/assets/` 目錄下補齊綠色與白色 logo，並重新渲染 2026 年 6 月普查快照報告，使 BreezySign 好好簽的圖片 logo 能夠正確內嵌並顯示於 HTML 和 PDF 中。
"""
        new_content = f"---{frontmatter}---{new_log}{body}"
        
        with open(file_path, 'w', encoding='utf-8') as f_out:
            f_out.write(new_content)
        print("成功追加日誌！")
    else:
        print("無法解析 frontmatter 結構")
else:
    print("log.md 不存在！")
