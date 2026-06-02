# -*- coding: utf-8 -*-
import os

def main():
    log_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\log.md"
    if not os.path.exists(log_path):
        print(f"[ERROR] {log_path} not found.")
        return

    with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # 移除 BOM 與 \r
    has_bom = content.startswith('\ufeff')
    if has_bom:
        content = content.lstrip('\ufeff')
    content = content.replace("\r", "")

    # 我們要替換的變更與修改段落
    old_block = """  - **修改來源摘要**:
    - [pm-breezysign-analytics-reports.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/sources/pm-breezysign-analytics-reports.md) ── 增量寫入 2026.06.02 最新報表之財務營收、獲客漏斗與競品轉單指標數據。
  - **修改分析報告**:
    - [bzs-saas-funnel-ltv-cac-report.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/analyses/bzs/bzs-saas-funnel-ltv-cac-report.md) ── 增量更新 2026 年 5 月底財務與 Leads 漏斗實績，並加入聖美麗憑證大檔案限制之防禦決策分析。"""

    new_block = """  - **修改規範文件**:
    - [AGENTS.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/AGENTS.md) ── 於內容品質準則中新增「資料來源一致性與落差處理」工作規則。
  - **修改來源摘要**:
    - [pm-breezysign-analytics-reports.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/sources/pm-breezysign-analytics-reports.md) ── 增量寫入 2026.06.02 最新報表之財務營收、獲客漏斗與競品轉單指標數據。
  - **修改分析報告**:
    - [bzs-saas-funnel-ltv-cac-report.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/analyses/bzs/bzs-saas-funnel-ltv-cac-report.md) ── 增量更新 2026 年 5 月底財務與 Leads 漏斗實績，並加入聖美麗憑證大檔案限制之防禦決策分析。
    - [bzs-saas-paid-subscribers-by-plan.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/analyses/bzs/bzs-saas-paid-subscribers-by-plan.md) ── 企業方案中新增太平洋旅行社，並將計數更新至 142 家以對齊最新數據。
    - [bzs-saas-customer-list.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/analyses/bzs/bzs-saas-customer-list.md) ── 增量更新太平洋旅行社、自強基金會、豐盛富足、富友、耐斯、福安與聯合線上的日報引用，並新增「透明房訊」與「自強基金會」。"""

    if old_block in content:
        content = content.replace(old_block, new_block, 1)
        print("[SUCCESS] Log entry updated successfully.")
    else:
        print("[ERROR] Old block not found in log.md.")

    if has_bom:
        content = '\ufeff' + content

    with open(log_path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    main()
