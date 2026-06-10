---
title: "SEO / AEO / GEO 優化評分標準"
type: concept
category: marketing
date_created: 2026-05-14
date_updated: 2026-06-10
tags: [SEO, AEO, GEO, 搜尋引擎優化, 問答引擎優化, 生成式引擎優化, AI搜尋, 行銷]
summary: "SEO（地基：排名）、AEO（牆壁：回答）與 GEO（房子：引用與推薦）的評分框架、核心優化策略與三者搭配協同關係。"
related_skills: [seo-optimization, geo-optimization]
related_analyses: [bzs-website-seo-geo-analysis]
---

# SEO / AEO / GEO 優化評分標準

> 在生成式 AI 時代，搜尋的遊戲規則已從傳統「連結排名」演進為「意圖回答與品牌引用」。我們必須協同搭配三大優化手段，構建完整的流量保護體系：
> 1. **SEO (Search Engine Optimization)** 是 **地基**：讓 Google、Bing 找到並排名網頁連結（比排名）。
> 2. **AEO (Answer Engine Optimization)** 是 **牆壁**：讓網頁內容成為 Google 精選摘要與 AI Overview 的直接解答來源（比回答）。
> 3. **GEO (Generative Engine Optimization)** 是 **房子**：讓 ChatGPT、Gemini 等 AI 平台在回答時引用你的連結或推薦你的品牌（比引用）。

---

## 一、 SEO 評分框架 (地基)

### 評分維度（共 5 大類）

#### 1. 基礎 Meta 標籤（10 分）
- **Title Tag**：中文 15~30 字，關鍵字在前半段，吸睛度高。
- **Meta Description**：120~160 字元，包含差異化描述與 CTA 行動呼籲。
- **OG 標籤**：社群分享時顯示正確的圖片與描述。

#### 2. 頁面結構（20 分）
- **H1 唯一性**：每頁僅有一個 H1，且必須包含主要關鍵字。
- **H2/H3 層級順序**：遵循樹狀嵌套架構（如 H1 $\rightarrow$ H2 $\rightarrow$ H3），不可越級或亂序，避免 DOM 解析混亂。
- **語意標籤**：使用 `<article>`、`<section>`、`<nav>` 等 HTML5 語意標籤。

#### 3. 內容深度與資訊增益（25 分）
- **正文字數**：商業頁 300 字以上，長文章 1,000 字以上。
- **資訊增益 (Information Gain)**：提供 Google 偏好的獨特洞見或量化數據指標（如 96% 節省時間），拒絕平庸文案。
- **排除薄內容**：消滅只有標題與按鈕的 Thin Content 頁面。

#### 4. 關鍵字與攔截布局（20 分）
- **首屏布局**：前 100 字內自然融入主要關鍵字。
- **競品攔截頁**：佈局與主要競爭對手（如 DocuSign/Adobe Sign）的橫向對照頁，精準攔截高轉移意圖的企業潛客。
- **URL 結構**：語意化目錄（如 `/esign-service` 優於 `/page?id=123`）。

#### 5. 技術 SEO（25 分）
- **網站速度**：Core Web Vitals 指標達標（LCP < 2.5s）。
- **Sitemap & robots.txt**：正確配置並提交，引導爬蟲精準抓取。
- **HTTPS 安全性**：具備有效的 SSL 加密憑證。

---

## 二、 AEO 評分框架 (牆壁)

AEO 旨在使網頁內容最優化地被「問答引擎」擷取，特別是 Google AI Overview、精選摘要及 People Also Ask。

### 核心優化策略

#### 1. 結構化資料 (Schema Markup) (30 分)
- **JSON-LD 格式**：推薦使用 Google 官方首選的 JSON-LD 程式碼。
- **常見 Schema 類型**：
  - `FAQPage`：問答頁面專用，是最直接被 AI 提取的格式。
  - `HowTo`：逐步操作教學頁面。
  - `Organization`：公司實體基本資訊（名稱、地址、Logo、聯絡方式）。
  - `Product`：產品售價、功能與評分，方便 AI 提取表格。

#### 2. 直接回答型段落設計 (35 分)
- **40-60 字直接回答**：在文章的關鍵章節開頭，添加一個 40-60 字的直接答案。
- **三句架構**：
  - *第一句*：開門見山給出核心定義或結論（不鋪陳、不說廢話）。
  - *第二、三句*：提供具體事實、論據或**量化數據佐證**（AI 對數據敏感度高，能大幅增加採信度）。
- **實例**：
  - *不佳寫法*：「在本篇文章中，我們將會為您詳細介紹何謂 AEO，並說明如何...」
  - *佳寫法*：「AEO (問答引擎優化) 是一種優化網頁內容以利 AI 搜尋引擎直接提取作為精選解答的技術。研究指出，在關鍵段落添加 40-60 字的直接答案，能提升 AI 引用率達 11% 以上。」

#### 3. 語音與口語化搜尋優化 (20 分)
- **口語問句標題**：將 H2/H3 小標題直接設為口語化的完整問句（例如：「系統櫃費用一般怎麼算？」）。
- **對話式回答**：小標題下方的第一段答案應簡短、直接、語氣自然，模擬口頭問答的真實情境。

#### 4. 內容新鮮度與維護 (15 分)
- **定期更新標記**：在頁面顯眼處標明 `date_updated`。AI 偏好引用最新、維護良好的即時內容。

---

## 三、 GEO 評分框架 (房子)

GEO 旨在提升網站在 ChatGPT、Gemini、Perplexity 等大語言模型 (LLM) 合成回答時的品牌提及率 (Citation) 與推薦機率。

### 核心優化策略

#### 1. 答案優先的內容結構（25 分）
- **首百字結論**：在網頁開頭 100 字內直接交付核心答案。
- **獨立段落**：每個段落應能獨立表達一個完整思想，便於 LLM 爬取後拆分組合。
- **豐富的統計數據**：內容中大量使用統計數據（如「減少 80% 簽約時間」），論文證實此舉能提升 AI 引用率 **+40%**。

#### 2. 第三方高信任平台佈局（25 分）
- **AI 資訊源分佈**：LLM 合成答案時，高度參考第三方高權威平台。
- **重點佈局渠道**：
  - **論壇與社群**：Reddit、LinkedIn、YouTube。
  - **行業評論**：G2、Google 商家評論。
  - **百科與新聞**：維基百科、主流媒體新聞報導。

#### 3. E-E-A-T 雙軌權威布局（25 分）
- **在地老牌背書**：將數發部能量登錄、ISO 27001 認證、上市公司背景等權威訊號，以易被 AI 爬取的純文字形式呈現在首頁。
- **國際技術合規**：中華電信 AATL 憑證機構、歐盟 eIDAS 合規宣告。
- **專業作者證明**：文章標明作者姓名、專業證照與背景，強化專業度。

#### 4. 品牌向量一致性 (Entity Alignment)（25 分）
- **實體命名規範**：LLM 使用向量嵌入（Vector Embedding）理解實體。若品牌名混用（如「BreezySign」、「好好簽」、「蒙恬好好簽」），會分散品牌的語意強度。
- **最佳實踐**：全網統一使用特定官方實體名（如「BreezySign 好好簽」），在外部論壇、YouTube 影片說明欄中亦保持一致，增強實體關聯強度。

---

## 四、 SEO vs AEO vs GEO 差異對照

| 面向 | SEO (傳統搜尋優化) | AEO (問答引擎優化) | GEO (生成式引擎優化) |
|---|---|---|---|
| **目標引擎** | Google, Bing 傳統搜尋 | Google 精選摘要, AI Overview | ChatGPT, Gemini, Perplexity |
| **核心機制** | 傳統 PageRank 排名 | 問答相關性與微格式匹配 | 實體關聯強度與向量嵌入 |
| **重點格式** | 長文章、頁面 Meta 標籤 | FAQ、口語化問答、JSON-LD | 答案優先段落、數據、第三方提及 |
| **關鍵指標** | 反向連結、關鍵字自然密度 | Schema 標記完整度、段落長度 | 品牌提及率 (Citation Rate) |
| **房子比喻** | 🧱 **地基**：讓網頁被收錄 | 🧱 **牆壁**：讓內容被直接回答 | 🏡 **房子**：讓 AI 平台主動推薦 |

---

## 相關連結

- [關鍵字意圖分類與 Claude Skill 自動化](keyword-categorization.md)
- [Google 官方：生成式 AI 搜尋優化指南](../sources/google-ai-optimization-guide.md)
- [AI Overviews 優化怎麼做？（數位時代整理版）](../sources/google-ai-overviews-bnext-guide.md)
- [好好簽官網 SEO/GEO 分析](../analyses/bzs/bzs-website-seo-geo-analysis.md)
- [SEO 優化技能](../skills/seo-optimization.md)
- [GEO 優化技能](../skills/geo-optimization.md)
