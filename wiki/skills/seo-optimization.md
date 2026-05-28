---
title: "SEO 搜尋引擎優化"
type: skill
category: marketing
proficiency: intermediate
tags: [SEO, 搜尋引擎優化, 行銷, Google, 關鍵字, 技術SEO]
date_created: 2026-05-14
date_updated: 2026-05-26
related_projects: []
related_concepts: [seo-geo-optimization]
summary: "掌握傳統搜尋引擎優化（SEO）的技術、內容與結構評估能力，能對網站進行基礎 SEO 審核並提出改善建議。"
---

# SEO 搜尋引擎優化

> 讓 Google、Bing 等傳統搜尋引擎能找到、理解並排名你的內容，最終帶來免費的自然流量。

---

## 核心能力

### 技術層面
- **頁面結構與樹狀大綱語意審核**：熟練運用 **HTML5 Outliner** 進行 DOM 標題層級驗證。能精準區分線性扁平遍歷與標準「樹狀大綱演算法 (HTML5 Outlining Algorithm)」之語意從屬關係，防禦前端開發團隊進行無謂的 DOM 標籤重構與潛在樣式崩潰風險。
- **頁面結構檢核**：薄內容頁識別、重複 footer 等 DOM 問題
- **Meta 標籤評估**：Title Tag 長度與關鍵字位置、Meta Description 品質
- **技術 SEO 基礎**：404 錯誤、HTTPS、Sitemap、robots.txt、Core Web Vitals
- **Schema Markup**：FAQPage、Organization、Product、HowTo 結構化資料設計
- **實際 AI 搜尋測試**：設計 Prompt 矩陣檢核搜尋能見度與資訊精確度（[ai-search-testing.md](../topics/ai-search-testing.md)）
- **/seo competitor-pages 競品對比頁生成**：自動產生轉換率優化的比較表、Feature Matrices 與 `Product` / `AggregateRating` 結構化資料，提升比較意圖檢索覆蓋。
- **/seo programmatic 程式化 SEO 的品質閘門 (Quality Gates)**：實施大規模數據頁面自動化構建，配置安全防護網（100+ 頁發出 Warning，500+ 頁強制 hard stop 限制，薄內容檢測，門道頁 Doorway Page 防範）。
- **/seo drift 網站 SEO 狀態漂移監控**：建立 SEO baseline，定期對比歷史數據，防止功能迭代引入 Technical/SEO 退化。

### 內容與評估層面 (SEO & AEO/GEO 進階合流)
- **搜尋意圖深剖與競品攔截 (Search Intent & Competitor Hijack)**：
  - 將意圖分為「產品核心高轉換（精準企業/臨櫃手寫板）」與「外圍導流（數位轉型）」。
  - 掌握點點簽式的高明 **「競品攔截策略」**：在網站結構中佈局與 competitors（如 DocuSign/Adobe Sign）的橫向對照頁，精準攔截高轉移意圖的企業潛客。
- **資訊增益與數據化文案檢核 (Information Gain & Data-driven Heading)**：
  - 拒絕平鋪直敘的功能說明，實踐 Google 偏好的 **「資訊增益 (Information Gain)」**，在 H 標籤與首屏正文中嵌入大量量化數據指標（如 96% 節省時間、80% 當日完成）。
- **E-E-A-T 雙軌信任度布局 (E-E-A-T Dual Trust Strategy)**：
  - 針對 YMYL（金融、法律、簽章）等高資安要求產業，實施雙軌權威布局：
    * **在地老牌背書**：上市公司背景 (5211)、數發部能量登錄、ISO 27001 認證（適合文字化呈現在首頁以利 AI 與 Google 提取）。
    * **國際技術合規**：中華電信 AATL 憑證機構、國際 ISO 標準、OTP 隱私。
- **薄內容識別（Thin Content）**：只有標題和按鈕的頁面對 SEO 的負面影響。

---

## 評分框架（傳統與生成式搜尋雙軌評估）

| 維度 | 滿分 | 傳統 SEO 重點 | AEO/GEO 延伸重點 (不衝突且完美協同) |
|------|------|---------------|----------------------------------|
| Title / Meta 標籤 | 10 | 長度、關鍵字位置、OG 標籤 | 關鍵字嵌入與 Google/AI 搜尋摘要提取 |
| H 標籤結構 | 20 | 層級順序、H1 唯一性 | H1 唯一防分散，次級標題嵌入數據化指標 |
| 內容深度與資訊增益 | 25 | 字數、意圖匹配、無薄內容 | 實踐 **資訊增益 (Information Gain)**，嵌入量化數據 |
| 關鍵字與攔截布局 | 20 | 關鍵字布局與 URL 結構 | **競品攔截頁面** (DocuSign/Adobe Sign 對照) |
| 技術 SEO 與 EEAT | 25 | 速度、行動友善、Schema 標記 | 部署 **Organization/Product Schema** 與純文字 EEAT 宣告 |

詳細評分標準 → [SEO/GEO 優化評分標準](../concepts/seo-geo-optimization.md)

---

## 實務應用

### 已執行的 SEO 分析

- **好好簽官網（2026/05/14）**：發現 H 標籤層級錯亂（H3 在 H2 前）、定價頁 FAQ 無內容、品牌名稱三種混用、功能頁薄內容
  → 完整報告：[bzs-website-seo-geo-analysis.md](../analyses/bzs-website-seo-geo-analysis.md)

---

## 常用工具

| 工具 | 用途 | 費用 |
|------|------|------|
| **Google Search Console** | 搜尋流量、索引狀況、Core Web Vitals | 免費 |
| **Claude SEO (Universal Skill)** | **自動化技術審計、競品對比頁與 programmatic 質量控制**，提供 drift 狀態漂移警報。 | 開源 / 免費（需 Claude Code） |
| **Google Lighthouse** | 技術 SEO、頁面速度 | 免費 |
| **HTML5 Outliner** | 驗證 DOM 標題嵌套與樹狀從屬層級，防禦線性遍歷誤判與多餘重構 | 免費 |
| **Ahrefs** | 關鍵字研究、競品反向連結 | 付費 |
| **Schema Markup Validator** | 驗證結構化資料正確性 | 免費 |
| **Screaming Frog** | 網站爬蟲、批次找 404/重複 title | 免費（500頁以內）|

---

## 學習資源

- [Google Search Central 官方文件](https://developers.google.com/search/docs)
- [Moz SEO Learning Center](https://moz.com/learn/seo)
- [Ahrefs Blog](https://ahrefs.com/blog)

---

## 相關連結

- [[geo-optimization|GEO 生成式引擎優化技能]]
- [[seo-geo-optimization|SEO/GEO 概念與評分標準]]
- [好好簽 SEO/GEO 分析](../analyses/bzs-website-seo-geo-analysis.md)
- [[claude-seo-universal-tool|Claude SEO 系統架構與實施指南]]
