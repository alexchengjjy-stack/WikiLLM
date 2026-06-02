import os

file_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\log.md"

if os.path.exists(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    
    content = raw_data.decode('utf-8', errors='ignore')
    
    parts = content.split('---', 2)
    if len(parts) >= 3:
        frontmatter = parts[1]
        body = parts[2]
        
        new_log = """
## [2026-06-02 12:49] update | 重構好好簽定價 FAQ 補齊 Q1~Q2 並全數去競品化
- **操作人**: LLM Agent (Antigravity)
- **變更與修改**:
  - **修改來源**: [breezysign-pricing.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/sources/breezysign-pricing.md) — 補齊原本缺失的 Q1 與 Q2 FAQ 題目與回答，將 FAQ 整理為乾淨、無重複的 Q1~Q8 完整排列。同時將 FAQ 內容中原本提及的所有競品（如點點簽、DottedSign、律果簽、FastSIGN、IDExpert、捷鵬等）全數移除，統一以「其他電子簽名系統」等合規中性詞彙帶過。
"""
        new_content = f"---{frontmatter}---{new_log}{body}"
        
        with open(file_path, 'w', encoding='utf-8') as f_out:
            f_out.write(new_content)
        print("成功追加日誌！")
    else:
        print("無法解析 frontmatter 結構")
else:
    print("log.md 不存在！")
