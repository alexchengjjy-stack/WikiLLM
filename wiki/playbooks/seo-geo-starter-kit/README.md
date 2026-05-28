# 🚀 SEO & GEO 智慧檢測與分析專案 (Starter Kit)

> 本專案是一個專為**傳統搜尋引擎優化 (SEO)** 與**生成式引擎優化 (GEO)** 設計的自動化檢測、評估與競品分析知識庫範本。透過大語言模型 (LLM Agent) 進行結構化網頁爬取、意圖測試與量化打分，協助品牌建立搜尋能見度護城河。

---

## 📖 什麼是 SEO 與 GEO 雙軌優化？

隨著 AI 搜尋引擎（如 ChatGPT Search、Perplexity、Gemini）與傳統 Google 搜尋版面（AI Overviews）的融合，消費者獲取資訊的方式已從「點擊藍色連結」轉變為「直接獲取 AI 摘要答案（Zero-Click）」。
- **SEO (Search Engine Optimization)**：確保網頁被傳統爬蟲正確收錄、理解並在關鍵字結果頁取得高排名。
- **GEO (Generative Engine Optimization)**：投其所好設計**高易取度 (Extractability)** 內容，使生成式 AI 在聚合多方資訊回答時，優先引用並正面推薦你的品牌。

---

## 📂 專案目錄結構建議

在初始化的空白專案中，建議採取以下目錄劃分以利 Agent 維護與 Dataview 檢索：

```
my-seo-geo-project/
├── agent.md                 # 定義 LLM Agent 的核心指令、爬取規範與 SOP
├── README.md                # 專案總覽與框架說明（本文件）
├── frameworks/              # 評分標準與方法論定義
│   └── seo-geo-metrics.md   # 雙軌五大維度量化評分表
├── raw_crawls/              # 網頁原始爬取快照（供溯源與 DOM 診斷）
├── analyses/                # 產出的深度診斷報告與三強對比矩陣
└── testing_logs/            # 實際 AI 搜尋 Prompt 實證與追蹤日誌
```

---

## 📊 雙軌五大維度評分標準 (Scoring Framework)

進行任何網站檢測時，Agent 需基於以下十大維度進行客觀打分與斷點診斷：

### 傳統 SEO 評估維度 (滿分 10 分)
1. **Title / Meta 標籤**：長度合規性、核心/長尾關鍵字前置度、OG 標籤完整度。
2. **H 標籤語意階層**：`H1` 唯一性與意圖包覆、避免標籤跳級（如 H2 直接跳 H4）或誤用。
3. **內容深度與意圖**：正文字數充實度、避免純標題的「薄內容（Thin Content）」頁面。
4. **關鍵字全域布局**：URL 靜態化、首段 100 字關鍵字密度、錨點文字（Anchor text）設計。
5. **技術與結構健康度**：死鏈（404 檢測）、Schema 基礎設定、重複渲染區塊排查。

### 生成式 GEO 評估維度 (滿分 10 分)
1. **結構化內容 (Structured Content)**：是否具備文字化功能對比表、手風琴式排版。
2. **品牌實體一致性 (Entity Consistency)**：全站網域、Meta、H1 與版權聲明是否精確收束為單一稱呼，避免底層向量映射發散。
3. **單頁直出解答 (Direct Summarizability)**：核心轉換頁面（如定價方案）是否具備**完整自然語言解答的 FAQ 區塊**（切忌僅放跳轉連結）。
4. **進階 Schema 標記**：`FAQPage`、`Product`、`Organization` 等利於大模型建構圖譜的微格式。
5. **顯式權威信號 (Authority Signals)**：政府立案許可、國際級數位憑證（如 AATL）、量化減碳數據或專家/律師團隊背書的文字堆疊。

---

## 🛠️ 快速啟動與工作流程

### 第一步：設定 Agent 系統提示詞
請將 `agent.md` 的內容載入至你的 AI 助手（如 Gemini、Claude 或自訂 GPTs）的 System Prompt 或 Context 空間中。

### 第二步：發起自動化網站健檢
向 Agent 輸入以下標準指令啟動健檢：
> 💡 *「請爬取目標網站 `https://example.com/` 及其定價/功能子頁面，並依據專案定義的 SEO/GEO 五大維度標準進行量化打分，最終在 `analyses/` 產出深度診斷報告。」*

### 第三步：執行 AI 搜尋實證覆測
依據 `agent.md` 中定義的四層 Prompt 矩陣，前往 ChatGPT 或 Perplexity 實際發問，驗證品牌是否具備資訊黑洞，並將改善前後的表現記錄於 `testing_logs/`。

---
> [!TIP]
> **GEO 滿分黃金法則**：大語言模型極度偏好「有問有答的完整句子」與「權威機構背書字眼」。只要在定價頁面植入精準的文字 FAQ 並宣告官方許可，即可瞬間提升 40% 以上的 AI 引用率！
