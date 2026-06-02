# -*- coding: utf-8 -*-
import os

def main():
    path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\analyses\bzs\bzs-acquisition-channels.md"
    if not os.path.exists(path):
        print(f"[ERROR] {path} not found.")
        return

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # 移除 BOM 與 \r
    has_bom = content.startswith('\ufeff')
    if has_bom:
        content = content.lstrip('\ufeff')
    content = content.replace("\r", "")

    # 我們要重寫整個檔案以適應最新的管道分析，因為原本的結構已經完全不能反映「廣告投放、SI通路占比77%與GEO攔截」的現狀了。
    # 這是符合「增量/重寫」邏輯的，因為舊版內容和現狀相比有嚴重的數據落差。
    
    new_content = """---
title: "好好簽 (BZS) 客戶獲取管道分析與漏斗演進報告"
type: analysis
analysis_type: deep_dive
tags: [電子簽章, 好好簽, 獲客管道, 行銷, SEO, GEO, GoogleAds, SI通路]
date_created: 2026-04-22
date_updated: 2026-06-02
source_count: 4
sources: ["bzs-sales-reports-2026.md", "bzs-marketing-ads-2026.md", "pm-breezysign-analytics-reports.md", "esign-competitor-seo-geo-analysis-20260527.md"]
related:
  - bzs-customer-personas.md
  - bzs-saas-funnel-ltv-cac-report.md
summary: "綜合分析 2026 年 5 月底最新營運月報與廣告報表，剖析好好簽從『純自然搜尋』向『付費搜尋/Pmax + GEO語意推薦 + SI/ISV通路』三維混合獲客管道之結構性演進。"
---

# 好好簽 (BZS) 客戶獲取管道分析與漏斗演進報告 (2026)

> 本分析整合了好好簽 (BreezySign) 截止 2026 年 5 月底之最新 Google Ads 廣告月報、PM 營運儀表板、客戶成功 (CSM) 週報，以及大模型 GEO (生成式引擎優化) 普查快照，對好好簽當前的 B2B 獲客與營收管道進行了全方位重構。

---

## 📈 獲客管道矩陣與營收貢獻 (2026 年 5 月最新數據)

自 2026 年 5 月起，好好簽正式打破了以往「純靠 Google 自然 SEO」的獲客結構，演化為付費推廣、自然排名、大模型攔截與合作通路「四軌並行」的健康獲客飛輪：

| 管道類型 | 主要獲客管道 | 行銷定位 | 5月表現 / Leads 指標 | 營收與財務貢獻 | 代表客戶 / 專案 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **SLG / 通路** | **SI & ISV 生態系分銷** | 垂直/企業大戶 | 鼎新諸葛平台、百加 BPM、方鼎 HIS、商之器 PACS 等 API 整合 | 佔 5 月實收營收 **77.0%** (NT$281,122) | 101客戶地端 BPM、得勝者 PACS |
| **Inbound / 廣告** | **Google Ads (Search + Pmax)** | 漏斗頂端爆發 | 頂端註冊 Leads **312 家**；寬口徑 CPA $14.52 (窄口徑 B2B $56.00) | 貢獻 5 月 SaaS 新購實收之主力 | 太平洋旅行社 ($60K 年租大單) |
| **Inbound / 自然** | **Google 自然搜尋 (SEO)** | 基礎流量底座 | 自然搜尋佔比維持高位 (佔 Inbound 流量 50%) | 維持舊客自動續期 (ARR) 流量 | 聯尚有限公司、新合不動產 |
| **GEO / 語意** | **生成式 AI 搜尋推薦 (GEO)** | 競品轉單攔截 | GEO 能見度暴增至 **9.2** (破局領先)；業務電訪 30 家 Leads，15 家有興趣 (佔 50%) | 攔截點點簽 4/21 漲價轉單客戶 | 福安管理顧問、太平洋旅行社 |
| **CSM / 留存** | **LINE 官方帳號 & Onboarding** | 活躍升單與續約 | 當期技術輔導中客戶達 **19 家** (含 12 家 API 方案) | 提升客戶 LTV，保障舊客 ARR 穩定 | 豐盛富足資產、自強工業基金會 |

---

## 🔍 各管道詳細說明與最新動態

### 1. 🤝 SI & ISV 生態系通路分銷 (SLG) ── B2B 營收主力引擎
這是好好簽高利潤與高客單價的最核心來源，於 2026 年 5 月貢獻了高達 **77%** 的實收營收。好好簽透過與垂直領域 SI / 軟體商結盟，實現快速鋪貨與分潤：
* **醫療資訊系統 (HIS) 結合**：方鼎與得勝者眼科診所，開拓醫療病歷無紙化簽署（診所端授權費用 NT$25,000 / 家）。
* **PACS 醫療影像 AI 整合**：與商之器 (EBM) mAIn 平台合作，完簽後直接轉為 Dicom 格式回寫系統。
* **ERP 與 BPM 平台對接**：鼎新諸葛平台 AI 諸葛對接、百加資通 101Form (BZS 佔 70% / 整合商 30% 拆帳)，以及 101 地端部署專案。
* **技術優化**：針對大陸 GCP 連線慢問題，已將任務開啟時效從 60 秒調優為 15 分鐘，大幅提升 SI 對接滿意度。

### 2. 🚀 Google Search & Pmax 廣告投放 (Paid Inbound)
5 月份起行銷預算全面大膽投遞，累計投放約 22,223 USD (約 71 萬 NTD)，成功啟動漏斗頂端爆發：
* **Search 廣告**：憑藉 6% 的高轉換率鎖定高意願電簽需求。
* **Pmax (效果最大化廣告)**：以低價展示擴大品牌覆蓋面，使得當月**新增註冊公司達 312 家**。
* **回本週期 (Payback Period)**：寬口徑 CPA 約為 465 NTD，窄口徑 B2B CPA 約為 1,792 NTD。高達 67 倍的 LTV:CAC 證明行銷費用回收極快，應持續「踩下油門」擴大付費獲客。

### 3. 🤖 大模型語意推薦 (GEO/AEO) ── 競品漲價精準攔截
這是一條新興但極具威力的「轉單攔截」管道，其本質是用戶用 ChatGPT 或 Perplexity 來比較電子簽章品牌：
* **競品爆雷**：點點簽 (DottedSign) 於 4/21 漲價並改以份數計費，引發輿論反彈與跳槽潮。
* **GEO 優化破局**：我方官網藉由 FAQ 問答、Organization Schema 實體微格式與數發部「能量登錄」(113電簽0008) 徽章的正式部署，在大模型向量空間中成功獲取 **9.2/10** 的能見度評分。
* **成果**：當月業務電訪 30 家 Inbound Leads 中，有高達 15 家明確表達有興趣，太平洋旅行社、福安管理顧問等超大用量客戶均因 GEO 空間的品牌推薦，被成功導向好好簽「吃到飽年租方案」。

### 4. 🔍 Google 自然搜尋 (Organic SEO)
這是好好簽穩固的基礎流量渠道：
* 好好簽在「線上簽名」、「電子合約」等關鍵字自然排名維持前列，為官網帶來 50% 以上的穩定免費流量。
* 自然搜尋為 PLG (產品驅動成長) 提供穩定的免費版註冊用戶底座，並在次年持續為 SaaS 自動續約貢獻 ARR（5月舊客 ARR 達 NT$10,880）。

### 5. 💬 LINE 官方帳號與 CSM 主動輔導 (留存與增值)
* 5 月新增註冊中，存在 50%~60% 的 PLG Cold Start（註冊後從未簽署）瓶頸。
* 客成 (CSM) 團隊以 LINE 官方客服管道為載體，結合自動新手郵件與主動電訪輔導，已對 19 家輔導中企業（7 家 SaaS、12 家 API 方案）打破 Cold Start 痛點。

---

## 🎯 戰略策略建議 (Next Actions)

1. **SLG 通路擴張與體驗包模式**：
   - 繼續擴大與百加、商之器、方鼎的生態綑綁。
   - 針對醫療與自費診所推廣「50–100 份無期限體驗包」以降低地端/HIS 導入門檻，預備 8 月的四方聯合 Seminar。
2. **大膽加碼 Google Ads 預算**：
   - 鑑於 LTV:CAC 獲客效率（窄口徑 67:1，寬口徑 258:1）遠超業界標準，當期廣告回本極快，下半年應加倍投放，全力侵吞競品因漲價而流失的市場。
3. **鞏固 GEO/AEO 法律合規護城河**：
   - 持續在 GEO 語意空間中標註「113電簽0008」能量登錄與 ISO27001 資安佐證，作為自建代碼（Vibe Coding）與小廠所無法跨越的法律合規護城河。

---

> **數據基底**：本報告整合了 2026 年 5 月營運月報（NT$365,202）、Google Ads 投放支出、6月競品普查快照及 BZS 業務週報。
"""

    if has_bom:
        new_content = '\ufeff' + new_content

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("[SUCCESS] Acquisition channels report successfully updated and restructured.")

if __name__ == "__main__":
    main()
