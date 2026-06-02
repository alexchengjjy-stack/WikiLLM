# -*- coding: utf-8 -*-
import os

index_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\index.md"
log_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\log.md"

# 1. Update index.md
if os.path.exists(index_path):
    with open(index_path, "r", encoding="utf-8") as f:
        index_content = f.read()
    
    old_line = "  * [BZS 客戶畫像特徵](analyses/bzs/bzs-customer-personas.md)"
    new_line = "  * [好好簽 (BZS) 企業客戶畫像分析](analyses/bzs/bzs-customer-personas.md) ── 重構醫療HIS/PACS整合、競品漲價流失轉單大客及大檔案防禦邊界之客戶畫像分析。"
    
    if old_line in index_content:
        index_content = index_content.replace(old_line, new_line)
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(index_content)
        print("index.md updated successfully.")
    else:
        print("Target line not found in index.md (or already updated).")
else:
    print("index.md not found.")

# 2. Update log.md
new_log_entry = """## [2026-06-02 17:15] analyze | 好好簽 (BZS) 企業客戶畫像分析
- **操作人**: LLM Agent (Antigravity)
- **變更與修改**:
  - **修改分析報告**:
    - [bzs-customer-personas.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/analyses/bzs/bzs-customer-personas.md) ── 重構企業客戶畫像結構，增量整合醫療 HIS/PACS 系統 API 對接、混合雲離線時間戳記合規、競品調漲轉單大客（如太平洋旅行社、福安管理顧問等）以及大檔案憑證限制防禦邊界（如聖美麗）等最新實戰案例與技術特徵。
  - **修改目錄**:
    - [index.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/index.md) ── 更新客戶畫像分析之標題與詳細描述。
- **關鍵發現**:
  - **醫療 API 整合合規**: 整合座標 API、Dicom 自動轉存，並設計診所地端中繼程式離線暫存與 NTP 校時（3 天內校正），滿足電子病歷與電子簽章法規要求。
  - **大戶轉單抗性**: 點點簽按件計費導致大量簽署客群成本倍增，我方以「吃到飽方案」與 UNIFY 共享範本權限管理精準攔截。
  - **技術防禦邊界**: 確立 10MB 單檔憑證限制防禦邊界，主動婉拒大檔案客戶（如聖美麗），降低高維護成本案件侵蝕利潤。

"""

if os.path.exists(log_path):
    with open(log_path, "r", encoding="utf-8") as f:
        log_content = f.read()
    
    # Insert right below "---" metadata block or before the first "## ["
    marker = "## ["
    pos = log_content.find(marker)
    if pos != -1:
        updated_log_content = log_content[:pos] + new_log_entry + log_content[pos:]
        with open(log_path, "w", encoding="utf-8") as f:
            f.write(updated_log_content)
        print("log.md updated successfully.")
    else:
        print("Marker not found in log.md.")
else:
    print("log.md not found.")
