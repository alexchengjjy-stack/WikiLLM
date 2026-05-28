---
title: "電子簽章能量登錄競品週期性觀測機制 (Playbook)"
type: playbook
category: competitive-intelligence
status: active
frequency: monthly
date_created: 2026-05-14
date_updated: 2026-05-15
tags: [競品觀測, 能量登錄, 點點簽, 律果簽, 好好簽, 市場情報, SOP]
summary: "針對已通過數位發展部電子簽章解決方案服務能量登錄之核心競品，建立跨越七大情報通道的固定週期性情報採集與戰略反饋機制，以數據化指標監控市場動態。"
---

# 電子簽章能量登錄競品週期性觀測機制 (Playbook)

> **執行週期**：每月出版一份月度快照，並允許在當月內針對重點廠商多次執行滾動式觀測與更新。
> **觀測目標**：數位發展部「電子簽章服務能量登錄」核心廠商（重點鎖定：點點簽、律果簽、好好簽、全景軟體等）  
> **輸出標的**：單一月份的所有查詢與參考資料統一彙整於該月的快照檔案中（例如：`wiki/analyses/esign-monitoring-snapshot-YYYYMM.md`）。

---

## 🎯 觀測目的與戰略意圖

隨著電子簽章法修法與數位發展部推動「服務能量登錄」，合規資格已成為企業與公部門採購的硬性門檻。透過對已登錄競品進行七大維度的常態性監控，能及早識破對手的产品迭代方向、定價策略調整、技術佈局（透過招募職缺反推）與獲客重心，進而動態校準 BreezySign 好好簽的銷售論述與 GEO 攻防策略。

---

## 🔍 七大觀測通道與採集指標 (7-Dimensional Observation Channels)

本機制核心在於將「碎片化資訊」轉化為「可度量情報」。每個通道需針對其 **觀測指標 (Metrics)** 進行評分，並推導其 **戰略意圖 (Strategic Intent)**。

### 1. 官網與定價動向 (Digital Storefront & Pricing)
*   **觀測對象**：Pricing Page, Feature Matrix, Schema.org 標註。
*   **關鍵採集指標 (KPIs)**：
    *   [ ] **方案門檻變動**：Free Tier 限制（例如：從 3 份/月縮減至 1 份/月，代表其正強迫用戶轉為付費）。
    *   [ ] **API 計費透明度**：是否公開 Webhook 或 API 單價（代表其正加強與企業系統整合之佈局）。
    *   [ ] **SEO/GEO 結構優化**：檢查 FAQ 區塊是否使用 `JSON-LD` 標註（這是 AI 抓取答案的關鍵）。
*   **戰略推論**：定價下調 + FAQ 增加 = 準備在大眾市場 (PLG) 發動價格戰；定價隱藏 + 主打 API = 轉向大企業 (Enterprise) 訂製市場。

### 2. 內容文章的策略方向 (Content Strategy)
*   **觀測對象**：Blog, Case Studies, Whitepapers。
*   **關鍵採集指標 (KPIs)**：
    *   [ ] **垂直行業覆蓋率**：新文章標籤（例如：#醫療電子簽名, #不動產經紀法），觀測其試圖攻佔的新領域。
    *   [ ] **內容產出頻率**：每月發布的深度文章數量，推測其資源投入程度。
*   **戰略推論**：大量發布教學文 (How-to) = 吸引初階用戶；發布合規/法律深度解析 = 吸引法務與金融決策者。

### 3. 廣告策略與關鍵字清單 (Ads & Keyword Strategy)
*   **觀測對象**：Google Ads 投放字詞, 搜尋結果排名, Perplexity/Gemini 引用。
*   **關鍵採集指標 (KPIs)**：
    *   [ ] **付費關鍵字與廣告花費費用 (Paid Keywords & Ad Budget)**：估算競品每月的 SEM 廣告費用與精確購買字組，費用呈現必須**同時包含預估日均廣告預算與月均廣告預算大約總金額 (Est. Daily & Monthly Ad Budget)**。
    *   [ ] **AI 引用滲透率 (AI Citation Rate)**：在 AI 搜尋引擎中，針對「台灣電子簽章推薦」等詞，品牌被提及並帶連結的頻率（目標 > 50%）。
    *   [ ] **SEO Share of Voice (SoV)**：核心字組（電子簽章、電子契約）在搜尋結果前 3 頁的佔有量。
*   **工具與查找 SOP (How to track Keywords & Costs)**：
    *   1. **精確用字與費用估算 (SEMrush / Ahrefs)**：輸入競品網域 (如 `dottedsign.com`)，於 *Organic/Paid Research* 功能中查找其 **Paid Keywords List** (付費關鍵字清單、排名與搜尋量) 以及 **Est. Ad Budget** (預估每月廣告預算與 CPC 費用)。**日均廣告預算之計算公式為：月度廣告預算 / 30，並四捨五入至整數百位，以直觀評估其每日買量飽和度。**
    *   2. **單字競價費用查找 (Google Keyword Planner)**：將採集到的關鍵字輸入官方關鍵字規劃工具，取得「頁首出價 (Top of page bid) 低價與高價區間」，即可精確得知如 `電子簽名`、`線上合約` 每次點擊的真實競價費用 (CPC)。
    *   3. **100% 精準當前廣告實體抓取 (Google 廣告透明度中心)**：造訪官方 [Google Ads Transparency Center](https://adstransparency.google.com/)，輸入競品營運主體名稱（如「凱鈿行動科技」、「律果科技」），即可直接抓取競品**當前正在投放的所有 Google 搜尋廣告文案、多媒體 Banner 與 YouTube 影片廣告用字**。
    *   4. **社群廣告追蹤 (Meta Ad Library)**：於 Meta 廣告檔案庫搜尋競品粉絲專頁，監控其 Facebook / Instagram 的廣告投放文案與素材用字。
    *   5. **數據整理與對比表列產出**：依據採集結果，於月報快照中產出「各家廣告費用與關鍵字比較表列」，其標準 Markdown 格式模板如下：
        
        | 品牌 | 營運主體 | 預估日均廣告預算 (NT$) | 預估月度廣告預算 (NT$) | 核心付費關鍵字 (SEM) 與 CPC 區間 | 廣告透明度中心實證狀態 | AI 引用率 (台灣推薦電簽) | GEO 定位與攔截戰略 |
        | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
        | **競品A** | 營運公司 | $X - Y / 日 | $A - B / 月 | `關鍵字` (CPC $X) | 運行中 (N 個文案) / 無廣告 | X% | 說明我方如何攔截 |
        
*   **戰略推論**：購買大量長尾關鍵字 = 全面佈局 GEO/SEO；投放高預算品牌對打廣告 = 具備強烈搶客企圖心。廣告預算高且持續 = 該關鍵字轉換效果好，我方應重點跟進。日/月預算之落差能直接揭露其行銷戰役的集火程度。

### 4. 人才招募與戰略重心 (Talent & Recruitment)
*   **觀測對象**：104, Yourator, LinkedIn Jobs.
*   **關鍵採集指標 (KPIs)**：
    *   [ ] **職缺結構權重**：AI/LLM 工程師佔比（預示產品智能化方向）、資安專才（預示進攻金融/政府標案）。
    *   [ ] **業務拓展 (BD) 焦點**：招募「政府標案專員」或「製造業轉型顧問」，直接揭露其下季度開發重點。
    *   [ ] **擴編速率**：近 30 天新開職缺總數（代表資金充裕度與擴張野心）。
*   **戰略推論**：招募大量 CSM（客戶成功） = 現有客戶流失率高；招募 AI 組 = 即將發布 AI 合約審查功能。

### 5. 能量登錄與合規認證 (Compliance & Accreditation)
*   **觀測對象**：數位發展部公告、ISO 證書查詢、Adobe AATL 清單。
*   **關鍵採集指標 (KPIs)**：
    *   [ ] **能量登錄效期**：是否在有效期內更新（失去登錄資格將失去政府標案投標門檻）。
    *   [ ] **身分驗證整合度**：是否新增 TWFidO、金融 FIDO、或特定的 eIDAS 兼容認證。
    *   [ ] **資安標章更新**：ISO 27001/27701 續證動態。
*   **戰略推論**：獲得高階資安認證 = 鎖定極高標準的金融或關鍵基礎設施 (CI) 客戶。

### 6. 公關新聞與政府標案 (PR & Public Sector)
*   **觀測對象**：政府電子採購網、Google News, 數位產業署新聞。
*   **關鍵採集指標 (KPIs)**：
    *   [ ] **指標性標案獲取**：得標金額與採購單位（例如：拿下縣市政府數位平台，具備極強的信譽背書）。
    *   [ ] **策略結盟公告**：與 ERP 廠商（如鼎新、SAP）或電信商（中華電信、遠傳）的深度整合。
*   **戰略推論**：拿下政府標案 = 建立該領域的「標準操作範本」，增加我方進入該領域的說服難度。

### 7. 技術 SEO 與 GEO 能見度監控 (Technical SEO & GEO Drift)
*   **觀測對象**：官網 CWV 技術指標、DOM H 標籤語意、JSON-LD 結構化資料、AI 搜尋引擎 (GEO/AEO) 引用率與提及漂移。
*   **關鍵採集指標 (KPIs)**：
    *   [ ] **INP 與載入延遲 (INP & LCP)**：監控競品是否加載過多第三方代碼導致 Core Web Vitals 衰退，從中識別體驗弱點（如點點簽的 INP 差值）。
    *   [ ] **SPA 爬蟲盲區評估 (SPA Shell Detect)**：檢查競品官網（如律果簽）是否缺乏 SSR 導致 thin content 誤判。
    *   [ ] **大模型 Feature Matrix 抓取率**：測試 ChatGPT Search、Gemini、Perplexity 在回答對比問題時，是否能準確提取競品與我方方案。
    *   [ ] **AI 引用負面漂移監控 (AEO Citation Drift)**：監控 AI 引用中是否出現競品負面聲音（如價格上漲、卡頓），作為搶客切入點。
*   **工具與查找 SOP (依據 Claude SEO)**：
    *   1. **全站技術與 DOM 審計 (`/seo audit <url>`)**：每月對 4 大官網執行此命令，剖析 LCP、CLS、INP 指標，並產出 Title/Meta Tag 的 H標籤語意重構建議。
    *   2. **競品比較與 Matrix 生成 (`/seo competitor-pages <competitor_url>`)**：抓取並拆解競品定價與 Feature，產出 BreezySign vs 競品的高轉化對比著陸頁，並自動配置 `Product` 與 `AggregateRating` 的 JSON-LD 程式碼。
    *   3. **SEO 狀態漂移監控 (`/seo drift <url>`)**：每雙週對 4 大官網執行此監控，建立 baseline，追蹤技術迭代引起的 SEO 與 AI 引用提及率衰退。

---

## 📋 常態性觀測目標名單與快速通道

| 廠商與品牌                | 官網快速通道                                   | 部落格 / 資源頁                                      | 人力銀行招募頁                                               | 備註與重點觀察維度                       |
| -------------------- | ---------------------------------------- | ---------------------------------------------- | ----------------------------------------------------- | ------------------------------- |
| **點點簽 (DottedSign)** | [首頁](https://www.dottedsign.com/zh-tw/)  | [官方部落格](https://www.dottedsign.com/zh-tw/blog) | [104 凱鈿專頁](https://www.104.com.tw/company/1a2x6biz7d) | 鎖定其企業方案定價微調與 AI 顧問化轉型。          |
| **律果簽 (LegalSign)**  | [首頁](https://legalsign.ai/)              | [律果學院](https://legalsign.ai/blog)              | [104 律果專頁](https://www.104.com.tw/company/1a2x6bks12) | 重點追蹤其法遵合約模組與法律 LLM 研發。          |
| **全景軟體 (CHANGING)**  | [FastSIGN](https://www.fastsign.com.tw/) | [最新消息](https://www.changingtec.com/news.html)  | [104 全景專頁](https://www.104.com.tw/company/748g2f4)    | 老牌上櫃資安廠，觀察其政府標案與地端整合動向。         |
| **好好簽 (BreezySign)** | [首頁](https://www.breezysign.com/)        | [官方部落格](https://www.breezysign.com/blog)          | [104 蒙恬專頁](https://www.104.com.tw/company/12n4h0hs)   | **我方本體觀測**：即時驗證官網修復進度與 GEO 能見度。 |

---

## 📝 月報情報記錄表 (Data Recording Template)

每次執行完畢後，請於下方表格（或專用追蹤頁）建立或更新該月的觀測快照連結。

### [2026-05] 月度觀測報告
- **詳細報告**：[2026-05 競品情報月度快照](../analyses/esign-monitoring-snapshot-202605.md)
- **核心情報摘要**：
    - **凱鈿 (DottedSign)**：招募通路轉向 Yourator，擴張 AI 團隊，從工具轉向 AI 顧問。
    - **律果簽 (LegalSign)**：確立「法律垂直 AI」定位，強化法律專屬 LLM 研發。
    - **我方 (BreezySign)**：AI 引用能見度受益於 Schema 優化，上升至約 40%。
    - **技術審計**：完成國內四家電簽官網 [[esign-competitor-seo-geo-analysis|Claude SEO 競品技術普查]]，指出點點簽 INP 與 AEO 漂移缺陷、律果 SPA 盲區，並為我方設計 Product JSON-LD 比較頁。
- **動作建議**：強化「ERP 生態系整合」優勢，並啟動 BreezySign 競品對比著陸頁部署，包抄競品流失流量。

---

## 🔗 關聯指引與情報庫

- [國內電子簽章服務競品比較](../analyses/domestic-e-signature-comparison.md)
- [官網技術 SEO 普查](../analyses/esign-competitor-seo-geo-analysis.md)
- [能量登錄官方許可名單](../sources/esign-solution-approved-list.md)
- [實際 AI 搜尋測試 SOP](../topics/ai-search-testing.md)
