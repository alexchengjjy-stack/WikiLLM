# -*- coding: utf-8 -*-
import os

def main():
    log_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\log.md"
    if not os.path.exists(log_path):
        print(f"[ERROR] {log_path} not found.")
        return

    with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # 移除 BOM
    has_bom = content.startswith('\ufeff')
    if has_bom:
        content = content.lstrip('\ufeff')

    # 清理重複 \r，統一為 \n
    content = content.replace("\r", "")

    new_log_entry = """## [2026-06-02 16:40] ingest | BreezySign分析報表 2026.06.02
- **操作人**: LLM Agent (Antigravity)
- **變更與修改**:
  - **修改來源摘要**:
    - [pm-breezysign-analytics-reports.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/sources/pm-breezysign-analytics-reports.md) ── 增量寫入 2026.06.02 最新報表之財務營收、獲客漏斗與競品轉單指標數據。
  - **修改分析報告**:
    - [bzs-saas-funnel-ltv-cac-report.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/analyses/bzs/bzs-saas-funnel-ltv-cac-report.md) ── 增量更新 2026 年 5 月底財務與 Leads 漏斗實績，並加入聖美麗憑證大檔案限制之防禦決策分析。
  - **新創專案**:
    - [fuan-api-integration.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/projects/fuan-api-integration.md) ── 福安健康與職安 API 專案 (12 萬報價簽約中)。
    - [udn-api-integration.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/projects/udn-api-integration.md) ── 聯合線上 API 對接與公開表單專案 (3 萬成交測試中)。
  - **修改專案**:
    - [ding-xin-api-integration.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/projects/ding-xin-api-integration.md) ── 更新 API 串接完成與連結時效優化里程碑。
    - [pacific-travel-onboarding.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/projects/pacific-travel-onboarding.md) ── 更新 40 人企業正式版方案於 6/1 順利開通啟用。
  - **修改目錄**:
    - [index.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/index.md) ── 註冊新專案並修正 PM 分析報表之標題。
- **關鍵發現**:
  - **實收總營收**: 5 月實收達 NT$365,202（SaaS $84,080 + 專案 $281,122）。新購業績達 $73,200（含太平洋旅行社大單 $60K）。前五個月累計實收已達 NT$728,700。
  - **獲客漏斗**: 當月新增註冊公司數 312 家。電訪 30 家，其中 15 家有興趣（高意願 9 家）。技術輔導中客戶達 19 家。
  - **競品轉單效應**: 點點簽（DottedSign）漲價及份數計費效應發酵，推動福安與太平洋旅行社等大戶轉單至我方吃到飽方案。
  - **聖美麗防線**: 因單檔 10MB 與 AATL 數位憑證效能限制，本月正式婉拒其年約，完成售後成本防線劃定。"""

    # 尋找 frontmatter 結束的 --- (從第 3 個字元後開始尋找第一個 ---)
    end_fm_idx = content.find("---", 3)
    if end_fm_idx != -1:
        insert_pos = end_fm_idx + 3
        before = content[:insert_pos]
        after = content[insert_pos:]

        # 重塑乾淨的 before 避免 frontmatter 殘留過多空行
        fm_lines = [line.strip() for line in before.split("\n") if line.strip()]
        new_fm_lines = []
        for line in fm_lines:
            if line.startswith("date_updated:"):
                new_fm_lines.append("date_updated: 2026-06-02")
            else:
                new_fm_lines.append(line)
        
        new_before = "\n".join(new_fm_lines)

        # 拼接並確保 spacing
        new_content = new_before + "\n\n" + new_log_entry + "\n\n" + after.lstrip("\n")
        
        if has_bom:
            new_content = '\ufeff' + new_content

        with open(log_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("[SUCCESS] Log prepended successfully via index slice insertion.")
    else:
        print("[ERROR] Could not find closing frontmatter --- in log.md.")

if __name__ == "__main__":
    main()
