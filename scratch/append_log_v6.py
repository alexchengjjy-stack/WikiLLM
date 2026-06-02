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
## [2026-06-02 14:56] export | 匯出 BreezySign 好好簽 ． 2026H2 跨部門執行計畫 PPTX 簡報
- **操作人**: LLM Agent (Antigravity)
- **變更與修改**:
  - **產出檔案**: 
    - [bzs-2026h2-cross-department-plan-20260602-1456-v1.pptx](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/outputs/bzs/bzs-2026h2-cross-department-plan-20260602-1456-v1.pptx)
  - **說明**: 全新設計並編寫 `generate_2026h2_plan_pptx.py` 腳本，將最新版次《BreezySign 好好簽 ． 2026H2 跨部門執行計畫》之 HTML 內容完整轉出為科技風 PPTX 簡報。首頁保留主品牌翠綠色背景與反白白色 logo，各內容頁右上角嵌入綠色 logo，採用左右卡片（雙欄）版型呈現 PLG/SLG 雙軌定位、各部門執行指標、ToS/Privacy Policy 新法規合規與時程里程碑，完成高品質版次控制與交付。
"""
        new_content = f"---{frontmatter}---{new_log}{body}"
        
        with open(file_path, 'w', encoding='utf-8') as f_out:
            f_out.write(new_content)
        print("成功追加日誌！")
    else:
        print("無法解析 frontmatter 結構")
else:
    print("log.md 不存在！")
