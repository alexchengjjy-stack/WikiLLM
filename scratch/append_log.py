import os

file_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\log.md"

if os.path.exists(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    
    # 嘗試用 utf-8 解碼
    content = raw_data.decode('utf-8', errors='ignore')
    
    # 尋找 frontmatter 的結束點 "---"
    parts = content.split('---', 2)
    if len(parts) >= 3:
        frontmatter = parts[1]
        body = parts[2]
        
        # 準備要插入的新日誌內容
        new_log = """
## [2026-06-02 12:36] update | 移除好好簽定價 FAQ 中的競爭對手提及
- **操作人**: LLM Agent (Antigravity)
- **變更與修改**:
  - **修改來源**: [breezysign-pricing.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/sources/breezysign-pricing.md) — 移除 FAQ 第 A3 題中提及的所有競品（點點簽、律果簽、捷鵬國際、FastSIGN）資訊，改為通用且合規的國家級背書與法律效力描述，以避免 FAQ 內容涉及競品敏感資訊。
"""
        # 重組內容
        # 保留 frontmatter
        new_content = f"---{frontmatter}---{new_log}{body}"
        
        # 寫回檔案 (使用 utf-8，因為 log.md 主要內容是 utf-8)
        with open(file_path, 'w', encoding='utf-8') as f_out:
            f_out.write(new_content)
        print("成功將日誌寫入 log.md！")
    else:
        print("無法解析 log.md 的 frontmatter 結構")
else:
    print("log.md 不存在！")
