---
title: "SEO / GEO 優化評分標準"
type: concept
category: marketing
date_created: 2026-05-14
date_updated: 2026-05-14
tags: [SEO, GEO, 搜尋引擎優化, 生成式引擎優化, AI搜尋, 行銷]
summary: "SEO（傳統搜尋引擎優化）與 GEO（生成式引擎優化）的評分框架、核心維度、實務評估方法，以及兩者的差異與協同關係。"
related_skills: [seo-optimization, geo-optimization]
related_analyses: [bzs-website-seo-geo-analysis]
---

# SEO / GEO 優化評分標準

> **SEO（Search Engine Optimization）** 讓 Google 等傳統搜尋引擎找到並排名你的內容。  
> **GEO（Generative Engine Optimization）** 讓 ChatGPT、Gemini、Perplexity 等 AI 引擎在回答問題時引用並推薦你的品牌。

---

## 一、SEO 評分框架

### 評分維度（共 5 大類）

#### 1. 基礎 Meta 標籤（10 分）

| 檢查項目 | 標準 | 滿分 |
|---------|------|------|
| Title Tag 長度 | 30~60 字元（英文），中文約 15~30 字 | 2 分 |
| Title Tag 包含主要關鍵字 | 關鍵字應在前半段出現 | 2 分 |
| Meta Description 長度 | 120~160 字元 | 2 分 |
| Meta Description 包含 CTA | 有行動呼籲或差異化描述 | 2 分 |
| OG / Twitter Card 標籤 | 社群分享時顯示正確圖片與描述 | 2 分 |

#### 2. 頁面結構（20 分）

| 檢查項目 | 標準 |
|---------|------|
| 每頁僅有一個 H1 | H1 包含主要關鍵字 |
| H 標籤層級正確 | H1 → H2 → H3，不可跳層（H3 不能在 H2 之前出現）|
| 關鍵字出現在 H2/H3 | 長尾關鍵字分散在次級標題 |
| 語意正確的 HTML5 標籤 | 使用 `<article>`、`<section>`、`<nav>` 等語意標籤 |

#### 3. 內容深度（25 分）

| 評估維度 | 說明 |
|---------|------|
| 正文字數 | 商業頁建議 300 字以上；長文章建議 1,000 字以上 |
| 關鍵字自然密度 | 目標關鍵字自然出現 2~4%，避免填塞 |
| 回答使用者意圖 | 內容真正回答訪客的問題（User Intent）|
| 有無薄內容頁 | 只有標題與按鈕的頁面（Thin Content）會被降分 |
| 多媒體內容 | 圖片、影片能提升停留時間信號 |

#### 4. 關鍵字布局（20 分）

| 位置 | 重要性 |
|------|-------|
| Title Tag | ⭐⭐⭐⭐⭐ 最高 |
| H1 | ⭐⭐⭐⭐⭐ |
| 前 100 字正文 | ⭐⭐⭐⭐ |
| H2/H3 | ⭐⭐⭐ |
| URL 結構 | ⭐⭐⭐（`/esign-service` 優於 `/page?id=123`）|
| 圖片 Alt 文字 | ⭐⭐ |

#### 5. 技術 SEO（25 分）

| 項目 | 說明 |
|------|------|
| 無 404 錯誤 | 所有內部連結可正常存取 |
| 網站速度 | Core Web Vitals（LCP < 2.5s, CLS < 0.1, FID < 100ms）|
| 行動裝置友善 | Mobile-First Indexing（Google 以手機版為主要索引）|
| Sitemap.xml | 提交至 Google Search Console |
| robots.txt | 正確設定，避免誤封重要頁面 |
| HTTPS | 必須有 SSL 憑證 |
| 重複內容 | 無重複標題或內容（canonical tag 正確設定）|

---

## 二、GEO 評分框架

> **理論基礎**：Princeton / Georgia Tech 2024 年論文《GEO: Generative Engine Optimization》，實驗測試了 10 種優化策略，統計各策略對 LLM 引用率的提升效果。

### GEO 核心原理

LLM（大語言模型）在回答使用者問題時，其引用決策來自：
1. **爬取時的內容品質**（是否結構清晰、可摘要）
2. **訓練資料中的品牌曝光度**（是否被多個來源提及）
3. **回答的正確性優先**（LLM 會優先引用「能直接回答問題」的來源）

### 論文確認的高效策略（有數據支撐）

| 策略 | 引用率提升 | 說明 |
|------|-----------|------|
| 加入統計數據與引用來源 | **+40%** | 有數字的內容更容易被 AI 引用（「90% 客戶表示...」）|
| 流利度優化（清晰易讀）| **+17%** | 避免長句、複雜術語；段落短、結構清晰 |
| 加入專業術語 | **+15%** | 技術詞彙讓 LLM 更準確識別你的領域 |
| Q&A 結構化格式 | **+11%** | FAQ 格式最接近使用者向 AI 提問的方式 |
| 突出品牌信息 | 定性效果 | 在顯眼位置強調品牌名稱、獨特優勢 |

### 評分維度（共 5 大類）

#### 1. 結構化內容（25 分）

| 項目 | 標準 |
|------|------|
| FAQ 區塊（有問有答）| 問題與答案都存在，非空殼 |
| 比較表格 | 功能對比表讓 LLM 可直接提取 |
| 清晰的列表 | Bullet points 優於長段落 |
| 定義框 / 摘要框 | 「[品牌] 是一款...」的開門見山段落 |

#### 2. 品牌名稱一致性（20 分）

> 這是台灣企業最常忽視的 GEO 問題！

LLM 使用**向量嵌入（Vector Embedding）** 理解實體。「BreezySign」、「好好簽」、「蒙恬好好簽」在 LLM 的語意空間中是**三個不同的向量點**，分散品牌的語意強度。

**最佳實踐**：全網統一使用「BreezySign 好好簽」，首次出現時以此完整名稱，之後可簡稱。

#### 3. 可摘要性（20 分）

| 測試方法 | 說明 |
|---------|------|
| 能否回答「XX 是什麼？」| 首頁前 200 字能否完整定義品牌 |
| 能否回答「XX 怎麼收費？」| 定價資訊是否以文字形式呈現（非動態載入）|
| 能否回答「XX 和 YY 哪個好？」| 是否有差異化比較內容 |

#### 4. Schema Markup（結構化資料）（20 分）

| 類型 | 適用場景 |
|------|---------|
| `Organization` | 公司基本資訊（名稱、地址、聯絡方式）|
| `Product` / `SoftwareApplication` | 產品功能、定價、評分 |
| `FAQPage` | FAQ 內容（最直接被 AI 摘要）|
| `HowTo` | 操作教學文章 |
| `BreadcrumbList` | 幫助 LLM 理解網站層級結構 |

#### 5. 權威性信號（15 分）

| 信號 | 說明 |
|------|------|
| 可引用的數據 | 「通過 113 年數發部能量登錄」、「ISO 27001 認證」等具體聲明 |
| 媒體報導 / 引用 | 第三方來源提及品牌（反向連結）|
| 用戶評價數量 | Google 評論、App Store 評分等 |
| 更新日期 | 明顯標示內容更新時間（LLM 偏好新鮮內容）|

---

## 三、SEO vs GEO 核心差異

| 面向 | SEO | GEO |
|------|-----|-----|
| **目標引擎** | Google、Bing | ChatGPT、Gemini、Perplexity、Claude |
| **排名方式** | 演算法排名（PageRank、相關性）| 引用決策（LLM 選擇回答時參考的內容）|
| **最重要的元素** | 反向連結、關鍵字密度 | 結構化內容、可直接摘要的文字 |
| **評估工具** | Google Search Console, Ahrefs | 直接問 AI、引用率追蹤（新興工具）|
| **內容格式** | 長文章、深度指南 | Q&A、定義框、摘要段落 |
| **標準化程度** | ✅ 有業界公認標準（15+ 年積累）| ⚠️ 仍在發展中（2023~至今）|

---

## 四、兩者共通的最佳實踐

以下策略對 SEO 和 GEO 都有效：

1. **清晰的頁面結構**（H 標籤層級正確）
2. **完整有內容的 FAQ**（不要只有問題沒有答案）
3. **在顯眼位置定義你的品牌/產品**
4. **定期更新內容**（新鮮度信號）
5. **移動端友善設計**

---

## 五、評估工具推薦

| 工具 | 用途 | 費用 |
|------|------|------|
| Google Search Console | 搜尋流量、索引狀況 | 免費 |
| Ahrefs / Semrush | 關鍵字排名、反向連結 | 付費 |
| Google Lighthouse | 技術 SEO、Core Web Vitals | 免費 |
| Schema Markup Validator | 檢查結構化資料 | 免費 |
| Perplexity AI（直接測試）| 手動測試 GEO 效果 | 免費 |
| Profound / Goodie AI | GEO 追蹤工具（新興）| 付費/Beta |

---

## 相關連結

- [Google 官方：生成式 AI 搜尋優化指南](../sources/google-ai-optimization-guide.md)
- [AI Overviews 優化怎麼做？（數位時代整理版）](../sources/google-ai-overviews-bnext-guide.md)
- [好好簽官網 SEO/GEO 分析](../analyses/bzs-website-seo-geo-analysis.md)
- [SEO 優化技能](../skills/seo-optimization.md)
- [GEO 優化技能](../skills/geo-optimization.md)
- [AI Agent Prompting 技能](../skills/ai-agent-prompting.md)
