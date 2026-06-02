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
## [2026-06-02 13:14] export | 匯出 2026 年 6 月電子簽章能量登錄競品情報普查快照 PPTX 簡報
- **操作人**: LLM Agent (Antigravity)
- **變更與修改**:
  - **產出檔案**: 
    - [bzs-esign-monitoring-snapshot-202606-20260602-1314-v1.pptx](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/outputs/bzs/bzs-esign-monitoring-snapshot-202606-20260602-1314-v1.pptx)
  - **說明**: 依據包含完整 logo 圖片的六月份情報普查快照 HTML 內容，成功匯出一份具備高畫質設計的 PPTX 簡報。簡報完全保留首頁翠綠色底色與反白 logo，各內容頁右上角嵌入綠色 logo，採用左右卡片（雙欄）版型整齊呈現兩代對照、四大廠矩陣、七大情報通道解析、業務反駁小卡及行動方針等內容，滿足版次控制與專業簡報規範。
"""
        new_content = f"---{frontmatter}---{new_log}{body}"
        
        with open(file_path, 'w', encoding='utf-8') as f_out:
            f_out.write(new_content)
        print("成功追加日誌！")
    else:
        print("無法解析 frontmatter 結構")
else:
    print("log.md 不存在！")
