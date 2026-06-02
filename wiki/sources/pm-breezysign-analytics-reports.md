---
title: "PM BreezySign 分析報表 (2025.10 - 2026.06)"
type: source
source_file: "raw/BZSdata/PMBreezySign分析報表/"
date_ingested: 2026-05-22
date_updated: 2026-06-02
tags: [PM, Dashboard, 營收, Leads, 月報]
author: "BreezySign PM Team"
original_date: "2025-10 to 2026-06"
language: "zh-tw"
summary: "產品經理 (PM) 的每月營運儀表板，包含公司整體數據、營收狀況、付費客戶名單及進件量 (Contact Us Leads) 追蹤。"
---

# PM BreezySign 分析報表 (2025.10 - 2026.06)

> 本來源彙整了從 2025 年 10 月至 2026 年 6 月初（包含最新 2026.06.02 報表），由產品經理定期輸出的各項營運儀表板 (Dashboard)。此系列報表以視覺化圖表與 PDF 附件為主，為管理層提供定期的數據快照。

## 報表結構與核心指標

這批系列報表每個月均維持一致的架構，追蹤以下四大板塊：

1. **Dashboard-Company (公司整體儀表板)**
   - 包含公司整體的註冊、活躍度等核心產品指標的快照。
2. **Dashboard-Income (營收儀表板)**
   - 追蹤當月營收、MRR 變動。附帶詳細的 `Dashboard-Income.pdf` 報表。
3. **Paid Company (付費客戶追蹤)**
   - 當月新增或續約的付費企業名單快照。附帶 `Paid Company.pdf`。
4. **Contact Us Leads (業務進件與潛在客戶)**
   - 詳細追蹤透過官網或產品端提交「聯絡我們」的高意圖名單。附帶 `Contact Us Leads.pdf`。

## 知識庫聯動與應用價值

- **視覺化輔助**：這些報表提供了我們在 [SaaS 漏斗綜合分析報告](../analyses/bzs/bzs-saas-funnel-ltv-cac-report.md) 中計算出的 CAC 與 MRR 數據的視覺化左證。
- **詳細標準定價**：參考 [好好簽價格方案](../sources/breezysign-pricing.md)、[2026 銷售日報分析](../sources/bzs-sales-reports-2026.md)。

## 📊 2026.06.02 最新報表數據快照 (對應 5 月底營運實績)

最新於 2026 年 6 月 2 日產出之營運動態報表，揭示了截至 5 月底的關鍵財務與獲客漏斗數據：

### 1. 財務營收與付費客戶結構 (Dashboard-Income / Paid Company)
* **實收總營收**：本月實收總營收高達 **NT$ 365,202**（SaaS 訂閱實收為 **NT$ 84,080**，專案與 API 實收為 **NT$ 281,122**）。
* **SaaS 新購業績 (New Booking)**：達 **NT$ 73,200**。
  - 包含點點簽轉單大客 **太平洋旅行社** (40人年約) 電匯入帳 **NT$ 60,000**。
  - 其他 9 家新客新購訂閱（含 6 家專業方案、3 家企業方案）共計 **NT$ 13,200**。
* **舊客自動續訂金流 (ARR)**：達 **NT$ 10,880**，維持健康的 Recurring Revenue 基礎。
* **營收歷史趨勢**：SaaS 實收因太平洋大單（6/1生效）扣款時間差出現技術性 MoM 衰退（-56.83%），但若併計專案實收，本月總體營收 MoM 其實為 **+87.49%**。2026 年前五個月累計實收營收已達 **NT$ 728,700**，具備高度增長動能。

### 2. 新增註冊與獲客漏斗 (Dashboard-Company / Contact Us Leads)
* **新增註冊公司數**：當月新增註冊公司數達 **312 家**，註冊基底持續擴大。
* **電話開發開發品質**：業務電訪 30 家註冊 Leads，其中 **15 家有興趣**（占比 50%），高達 **9 家名列高意願名單**。
* **技術輔導中客戶**：共計 **19 家**（SaaS 體驗版 7 家，API/SI 方案 12 家）。

### 3. 競爭態勢與重大決策分析
* **點點簽 (DottedSign) 漲價轉單潮**：點點簽自 2026-04-21 改採 Envelope Tasks（按發送件數計費，單份 NT$45~50）模式，導致大簽署量客戶（如福安 2萬份/年、太平洋旅行社 2000份/年）面臨數倍的續約報價，促使客戶大舉轉向好好簽吃到飽年租方案。
* **聖美麗 (St. Mary) 憑證限制婉拒**：由於聖美麗健檢文件多為大於 10MB 的超大 PDF，好好簽嵌入 AATL 憑證時易因伺服器負載超時。CSM 與技術團隊於本月正式予以婉拒年約（客戶選擇於 8/1 續約點點簽），確立了我方針對單檔 10MB 憑證限制的防禦邊界。

## 🔗 相關連結
- [SaaS 歷年四大維度與成長漏斗綜合分析報告 (2024-2026)](../analyses/bzs/bzs-saas-funnel-ltv-cac-report.md)
- [BZS 業務日報與週報彙整 (2026)](bzs-sales-reports-2026.md)
- [太平洋旅行社 Onboarding 專案](../projects/pacific-travel-onboarding.md)
- [鼎新電腦 API 對接專案](../projects/ding-xin-api-integration.md)
- [福安健康與職安 API 專案](../projects/fuan-api-integration.md)
- [聯合線上 API 對接與公開表單專案](../projects/udn-api-integration.md)
