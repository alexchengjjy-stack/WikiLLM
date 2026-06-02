# -*- coding: utf-8 -*-
import os

log_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\log.md"

new_log_entry = """## [2026-06-02 18:04] update | 好好簽 (BZS) 付費客戶方案結構對照分析順序調整
- **操作人**: LLM Agent (Antigravity)
- **變更與修改**:
  - **修改分析報告**:
    - [bzs-saas-paid-subscribers-by-plan.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/analyses/bzs/bzs-saas-paid-subscribers-by-plan.md) ── 依據閱讀體驗調整內容順序，將「銷售方案佔比與客戶結構對照分析」移至最前方，詳細付費客戶名單降為二級標題移至後方。
- **關鍵發現**:
  - **結構層級優化**: 讓決策者在開啟付費清單分析時，優先閱讀宏觀的銷售金額佔比與客戶數量結構分析（企業方案佔營收比重 83.2% 的核心啟示），再進入微觀明細列表，提升報告可讀性。

"""

if os.path.exists(log_path):
    with open(log_path, "r", encoding="utf-8") as f:
        log_content = f.read()
    
    marker = "## ["
    pos = log_content.find(marker)
    if pos != -1:
        updated_log_content = log_content[:pos] + new_log_entry + log_content[pos:]
        with open(log_path, "w", encoding="utf-8") as f:
            f.write(updated_log_content)
        print("log.md updated successfully with section swap entry.")
    else:
        print("Marker not found in log.md.")
else:
    print("log.md not found.")
