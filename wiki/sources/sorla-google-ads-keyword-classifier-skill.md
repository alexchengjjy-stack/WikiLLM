---
title: "geniushub-seo/google-ads-keyword-classifier: Google Ads 關鍵字研究分類 Skill"
type: source
source_file: "raw/marketing/geniushub-seogoogle-ads-keyword-classifier Google Ads 關鍵字研究分類 Skill：將 Keyword Planner 匯出清單分類為排除競品品牌品類痛點決策資訊詞，並透過 SERP 抽樣驗證，輸出結構化分類 Excel 供廣告群組規劃使用。.md"
date_ingested: 2026-06-10
tags: [Google-Ads, 關鍵字研究, Claude, 廣告投放, 技能包]
author: "Sorla - 超簡單行銷"
original_date: "2026-06-10"
language: "繁體中文"
summary: "GitHub 開源的 Google Ads 關鍵字分類 Claude Skill 配置檔，提供結構化的關鍵字意圖分類邏輯、同義變體合併、強制升降級規則與 SERP 抽樣驗證 SOP。"
---

# Google Ads 關鍵字研究分類 Skill (SKILL.md)

> 本文為 GitHub 開源項目 `geniushub-seo/google-ads-keyword-classifier` 中的 `SKILL.md` 摘要。這是一個供 Claude 使用的 Skill 說明文件，旨在將 Google Keyword Planner 匯出的關鍵字清單，自動進行高精確度的意圖分類，並在 Chrome 瀏覽器中主動調用 SERP 抽樣驗證，最終輸出結構化的四個工作表 Excel 檔案。

## 核心要點
- **必填收集**：開始前必須向用戶確認：關鍵字清單、目標國家/地區（決定 Google 地區版本）、品牌名稱、主要商品/服務。
- **前置篩選下限**：低於 10 的搜尋量直接剔除（台灣市場屬統計誤差），並排除無關語言。
- **7大意圖分類優先級**：排除 → 競品 → 品牌 → 比較決策 → 通用品類 → 功能痛點 → 資訊。
- **強制升降級輔助規則**：包含特定字詞的關鍵字會被強制更改分類或狀態（例如：含「ptt/dcard/論壇」一律強制降為備用）。
- **主力與備用判定公式**：根據搜尋量四分位數（高、中、低層）與意圖進行雙向判定，控制每個類別主力字以 10-20 個為上限。
- **SERP 抽樣驗證 SOP**：主動調用瀏覽器工具，對各類別抽取 10-15%（最少3個），依據前三名搜尋結果調整分類。

## 分類與判定詳細規則

### 一、 7大分類定義與特徵

| 類別 | 意圖 | 常見字詞特徵 |
|---|---|---|
| **1. 排除 (Negative)** | 負面詞、免費、求職或明顯無關 | 黑店、詐騙、免費、破解、招聘、徵才 |
| **2. 競品詞 (Competitor)** | 競爭對手品牌或產品名稱 | IKEA系統櫃、歐德系統櫃 |
| **3. 品牌詞 (Branded)** | 客戶自身品牌/產品名稱 | 超簡單系統櫃、Super Simple |
| **4. 比較決策 (Comparison)** | 做最終決策，意圖極明確 | 推薦、費用、價格、評價、vs、哪家好、報價 |
| **5. 通用品類 (Generic)** | 描述產品/服務品類，不含品牌 | 台北系統櫃、系統家具、系統櫃設計 |
| **6. 功能痛點 (Feature)** | 描述問題或解決方案，尚未指定品類 | 怎麼選、如何解決、小坪數衣櫃解決方案 |
| **7. 資訊詞 (Informational)** | 獲取知識，無購買意圖 | 什麼是、介紹、原理、歷史 |

### 二、 字詞結構強制升降級規則
1. **強制升為比較決策（主力）**：含「費用/價格/報價/收費」、「推薦/評價/怎麼選」、「代操/代理/外包/找公司」等。
2. **強制歸入資訊詞（備用）**：含「教學/課程/自學」、「什麼是/介紹/原理」等。
3. **強制降為備用（論壇討論）**：含「ptt/dcard/mobile01/論壇/討論/開箱」等。
4. **地名過濾**：不符目標投放地區之地名詞降為備用或剔除。

### 三、 主力與備用判定公式

- **排除**：全數標記「排除」。
- **競品**：預設「備用」（若要打防守/進攻廣告可手動升主力）。
- **品牌**：全數「主力」。
- **比較決策**：搜尋量 ≥ 10 全數「主力」（例外：高競爭 + 後25% 搜尋量降備用）。
- **通用品類**：
  - 高/中層搜尋量預設「備用」（避免高預算燒錢）。
  - 低層搜尋量預設「主力」（長尾字競爭低，值得投放）。
  - 單一品類字（如「google ads」）一律「備用」。
- **功能痛點**：高/中層搜尋量預設「主力」，低層預設「備用」。
- **資訊**：全數預設「備用」。

### 四、 SERP 抽樣驗證 SOP
- 對各分類抽取 **10-15% (最少 3 個)**。
- 前往目標 Google（如 `google.com.tw`）搜尋 `?q={keyword}&gl=tw&hl=zh-TW`。
- 讀取 SERP 前三名結果類型：
  - 若皆為電商/報價頁 → 移至決策/品類詞。
  - 若皆為部落格/教學文 → 移至資訊詞。
- 若某類別有 **30% 以上需修正**，則該類別重新全檢。

## 相關連結
- [關鍵字意圖分類概念](../concepts/keyword-categorization.md)
- [Sorla 關鍵字研究來源摘要](../sources/sorla-google-ads-keyword-research-claude.md)
- [SEO 搜尋引擎優化技能](../skills/seo-optimization.md)
- [Sorla - 超簡單行銷實體](../entities/sorla.md)

## 來源引用
- [GitHub 項目 (SKILL.md)](https://github.com/geniushub-seo/google-ads-keyword-classifier/blob/main/SKILL.md) — google-ads-keyword-classifier
