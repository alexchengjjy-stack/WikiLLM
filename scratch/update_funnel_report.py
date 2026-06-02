# -*- coding: utf-8 -*-
import os

def main():
    report_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\analyses\bzs\bzs-saas-funnel-ltv-cac-report.md"
    if not os.path.exists(report_path):
        print(f"[ERROR] {report_path} not found.")
        return

    with open(report_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # 移除 BOM 與 \r 噪音
    has_bom = content.startswith('\ufeff')
    if has_bom:
        content = content.lstrip('\ufeff')
    content = content.replace("\r", "")

    # 1. 更新 Frontmatter
    old_fm = """title: "SaaS 歷年四大維度與成長漏斗綜合分析報告 (2024-2026)"
type: analysis
analysis_type: deep_dive
tags: [SaaS, MRR, CAC, LTV, 漏斗分析, 歷年趨勢]
date_created: 2026-05-22
date_updated: 2026-05-22
source_count: 5
sources: ["bzs-sales-reports-2026.md", "bzs-marketing-ads-2026.md"]"""

    new_fm = """title: "SaaS 歷年四大維度與成長漏斗綜合分析報告 (2024-2026)"
type: analysis
analysis_type: deep_dive
tags: [SaaS, MRR, CAC, LTV, 漏斗分析, 歷年趨勢]
date_created: 2026-05-22
date_updated: 2026-06-02
source_count: 6
sources: ["bzs-sales-reports-2026.md", "bzs-marketing-ads-2026.md", "pm-breezysign-analytics-reports.md"]"""

    if old_fm in content:
        content = content.replace(old_fm, new_fm)
        print("[SUCCESS] Frontmatter updated.")
    else:
        # Fallback loose line endings for old_fm
        old_fm_norm = old_fm.replace("\n", "").replace(" ", "").replace('"', "")
        content_norm = content.replace("\n", "").replace(" ", "").replace('"', "")
        if old_fm_norm in content_norm:
            print("[INFO] Frontmatter found with spacing differences, manually parsing YAML...")
            # We will just split by --- and replace frontmatter
            parts = content.split("---", 2)
            if len(parts) >= 3:
                parts[1] = "\n" + new_fm + "\n"
                content = "---".join(parts)
                print("[SUCCESS] Frontmatter parsed and updated.")
            else:
                print("[ERROR] Split by --- failed.")
        else:
            print("[ERROR] Frontmatter old block not found.")

    # 2. 更新營收維度 (Revenue) 內容
    old_revenue = "* **2026 年 (上半年)**：迎來**點點簽漲價跳槽潮**，大量中大型企業（如太平洋旅行社，年費 6 萬）轉入好好簽企業方案，短短五個月實際入帳金額已達 **728,700 NTD**。預估目前的每帳戶平均營收 (ARPU) 已攀升至 **6,000 NTD/年** 以上。"
    
    new_revenue = "* **2026 年 (上半年)**：迎來**點點簽漲價跳槽潮**，大量中大型企業（如太平洋旅行社，年費 6 萬）轉入好好簽企業方案，短短五個月實際入帳金額已達 **728,700 NTD**。預估目前的每帳戶平均營收 (ARPU) 已攀升至 **6,000 NTD/年** 以上。根據最新的 [2026.06.02 PM分析報表](../../sources/pm-breezysign-analytics-reports.md)，5 月單月實收總營收達 **365,202 NTD**（SaaS $84,080 + 專案/API $281,122），證明了 SaaS 與專案/API 雙引擎對營收的強力貢獻。其中新購業績達 $73,200（含太平洋年費 $60,000 與 9 家新客 $13,200），證明舊客ARR與大單轉移的雙重雪球效應。"

    if old_revenue in content:
        content = content.replace(old_revenue, new_revenue)
        print("[SUCCESS] Revenue section updated.")
    else:
        print("[ERROR] Revenue old block not found.")

    # 3. 更新留存維度 (Retention) 內容
    old_retention = "* **PLG Cold Start 痛點與客成介入**：後台數據顯示，公司在註冊後**「從未發起任務/簽署」的比例高達 50%~60%**，是流失的最大痛點（Cold Start 瓶頸）。CSM 主動 onboarding 介入（電訪 + 線上操作導覽 + 範本製作）是打破 Cold Start 的關鍵，例如 **豐盛富足資產** (註冊後電訪輔導，5/7 訂閱企業方案月約)、**自強工業科學基金會** (線上 Demo 組織權限，5/15 訂閱企業方案 2 個月)、**富友旅行社** (協助優化簽署流程，5/8 訂閱專業年約)，均證實客成主動關懷對 PLG 漏斗轉化率的巨大提升。"

    new_retention = """* **PLG Cold Start 痛點與客成介入**：後台數據顯示，公司在註冊後**「從未發起任務/簽署」的比例高達 50%~60%**，是流失的最大痛點（Cold Start 瓶頸）。在 5 月底最新數據中，當月新增註冊公司達 **312 家**，CSM 團隊積極介入，電訪跟進 30 家 Leads，其中 **15 家有興趣**（含 9 家高意願），且當期技術輔導中客戶達 **19 家**（SaaS 體驗版 7 家，API/SI 方案 12 家）。此前的客成介入案例，如 **豐盛富足資產** (註冊後電訪輔導，5/7 訂閱企業方案月約)、**自強工業科學基金會** (線上 Demo 組織權限，5/15 訂閱企業方案 2 個月)、**富友旅行社** (協助優化簽署流程，5/8 訂閱專業年約)，均證實客成主動關懷對 PLG 漏斗轉化率的巨大提升。
* **技術防守與邊界決策 (聖美麗案例)**：客成介入除了推動轉換，也具備「篩選與防守服務邊界」的戰略功能。5 月連鎖醫美/健檢聖美麗（St. Mary）因其文件多大於 10MB，容易因 AATL 數位憑證限制而在簽署時失敗。為了規避無限售後成本，客成與技術團隊於本月正式予以婉拒年約（客戶選擇於 8/1 續約點點簽），確立了我方針對單檔 10MB 憑證限制的防禦邊界，避免高維護成本稀釋利潤。"""

    if old_retention in content:
        content = content.replace(old_retention, new_retention)
        print("[SUCCESS] Retention section updated.")
    else:
        print("[ERROR] Retention old block not found.")

    # 4. 更新相關連結
    old_links = """## 相關連結
- [BZS 2026 行銷廣告報表 (Google Ads & Pmax)](../sources/bzs-marketing-ads-2026.md)
- [BZS SaaS 客戶提取清單](bzs-saas-customer-list.md)"""

    new_links = """## 相關連結
- [BZS 2026 行銷廣告報表 (Google Ads & Pmax)](../sources/bzs-marketing-ads-2026.md)
- [BZS SaaS 客戶提取清單](bzs-saas-customer-list.md)
- [PM BreezySign 分析報表 (2025.10 - 2026.06)](../../sources/pm-breezysign-analytics-reports.md)"""

    if old_links in content:
        content = content.replace(old_links, new_links)
        print("[SUCCESS] Links section updated.")
    else:
        print("[ERROR] Links old block not found.")

    # 回寫
    if has_bom:
        content = '\ufeff' + content

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[INFO] Funnel report update completed.")

if __name__ == "__main__":
    main()
