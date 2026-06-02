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
## [2026-06-02 13:43] update | 修正 6 月普查快照排除內部非公開資訊並同步 Playbook 規則
- **操作人**: LLM Agent (Antigravity)
- **變更與修改**:
  - **修訂檔案**: 
    - [esign-competitor-monitoring-mechanism.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/playbooks/esign-competitor-monitoring-mechanism.md) (新增限制規範)
    - [esign-monitoring-snapshot-202606.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/analyses/esign/esign-monitoring-snapshot-202606.md) (修正好好簽產品動態)
  - **重新生成檔案**: 
    - [bzs-esign-monitoring-snapshot-202606-20260602-1343-v1.html](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/outputs/bzs/bzs-esign-monitoring-snapshot-202606-20260602-1343-v1.html)
    - [bzs-esign-monitoring-snapshot-202606-20260602-1343-v1.pdf](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/outputs/bzs/bzs-esign-monitoring-snapshot-202606-20260602-1343-v1.pdf)
    - [bzs-esign-monitoring-snapshot-202606-20260602-1343-v1.pptx](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/outputs/bzs/bzs-esign-monitoring-snapshot-202606-20260602-1343-v1.pptx)
  - **說明**: 
    1. 於 `esign-competitor-monitoring-mechanism.md` SOP 中，明確寫入「核心普查原則與限制規範」，規定普查報告只以公開正式站（Production）各頁面發布的正式資訊為唯一比較基準。
    2. 修剪 6 月普查快照、PDF 腳本與 PPTX 腳本中關於我方的資訊，剔除未在官網正式上線公開的「持續優化與鼎新 ERP 整合」工作報告與產品規劃項目。
    3. 重新編譯輸出全套 HTML, PDF 與 PPTX 快照檔案。
"""
        new_content = f"---{frontmatter}---{new_log}{body}"
        
        with open(file_path, 'w', encoding='utf-8') as f_out:
            f_out.write(new_content)
        print("成功追加日誌！")
    else:
        print("無法解析 frontmatter 結構")
else:
    print("log.md 不存在！")
