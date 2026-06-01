---
title: "WikiLLM 工作項目分類與打標指南"
type: playbook
playbook_type: sop
category: operations
tags: [工作分類, 標籤規範, BreezySign, BreezyBrain, SOP]
date_created: 2026-06-01
date_updated: 2026-06-01
summary: "定義 WikiLLM 現有現役業務 BreezySign (第一大項) 與下一代自研產品 BreezyBrain (第二大項) 的分類範疇與標籤打標規範，防止交叉文件混淆。"
---

# WikiLLM 工作項目分類與打標指南

> **核心目的**：本指南旨在對 WikiLLM 知識庫中的所有來源（Sources）、專案（Projects）、分析（Analyses）與實體（Entities）建立清晰的工作類別劃分。當未來有新文件攝入或新指示加入時，必須自動依此框架進行區分、打標與歸檔，防範交錯文件與進度產生混淆。

---

## 🗂️ 工作分類對照架構

知識庫中的所有項目應嚴格區分為**現役業務（第一大項）**與**下一代自研產品（第二大項）**：

### 🟩 第一大項：BreezySign 好好簽現役業務 (Current Business & Ops)

此大項聚焦於「好好簽 BreezySign」現行電子簽章業務之運營、行銷與專案落地：

| 子分類 | 包含範疇 | 建議標籤 (Tags) |
| :--- | :--- | :--- |
| **1. BreezySign Business** | 整體營收與營運、跨部門協調與財務核對。 | `[好好簽, 營運, bzs-business]` |
| **2. SaaS CSM & Projects** | SaaS 營運數字（MRR/ARR/LTV/CAC）、專案與 API 串接、SI 系統整合（如得勝者、太平洋旅行社、鼎新、聖洋等專案進展與項目收入）。 | `[SaaS營運, 客戶成功, 專案, bzs-saas-csm, bzs-projects]` |
| **3. BreezySign Marketing** | 官網 SEO/GEO 分析、行銷推廣文章（如 Blog 推廣文案）、行銷漏斗優化與廣告報表。 | `[SEO, GEO, 行銷, bzs-marketing]` |
| **4. BreezySign PM** | 好好簽現行產品功能定義（如 AATL 憑證、10MB大檔案防線、座標完簽 API 參數定義等）。 | `[產品管理, 功能定義, bzs-pm]` |
| **5. Competitor & Compliance** | 數發部能量登錄與合規檢核、SaaS 競品（如點點簽、律果簽、FastSIGN 等）價格、計費與轉單潮定期觀測。 | `[電子簽章法, 競品分析, 合規, bzs-competitors]` |

---

### 🟦 第二大項：BreezyBrain 好好腦下一代產品 (Next-Gen AI Product)

此大項聚焦於自研下一代 AI 大腦中樞「BreezyBrain」的全生命週期研發、行銷與營運：

| 範疇領域 | 包含內容 | 建議標籤 (Tags) |
| :--- | :--- | :--- |
| **需求與設計 (Spec & Design)** | BreezyBrain 產品需求文件 (Product Spec)、架構圖（分層架構、Eraser 關係圖）、UI 提示詞與變更紀錄。 | `[BreezyBrain, 需求規格, 架構設計, bb-spec]` |
| **開發與測試 (Dev & Test)** | 程式碼開發（如 Docker 容器化、KMS 金鑰管理、RLS 權限控制）、地端一鍵部署 CLI、資料備份與系統測試。 | `[程式開發, 系統測試, 容器化, bb-dev]` |
| **行銷與文案 (Marketing & Copy)** | 行銷包裝、推廣文案、大腦官網與自定義白牌化推廣策略。 | `[行銷推廣, 官網文案, 白牌化, bb-marketing]` |
| **運營與跨部門 (Ops & Business)** | 大腦專案業務開發、客戶成功（如 LoftLoRA 腦培養引導）、大腦整體營運與跨部門協調。 | `[整體營運, 客戶成功, 專案業務, bb-ops]` |

---

## ⚙️ Ingest 與更新執行 SOP

1. **新文件攝入 (Ingest)**：
   - 讀取 raw 來源時，首先判斷該文件屬於「BreezySign 業務」還是「BreezyBrain 產品」。
   - 在來源摘要頁的 frontmatter `tags` 中，必須寫入對應的分類標籤（例如 `#bzs-projects` 或 `#bb-spec`），並在 `summary` 中註明分類歸屬。
2. **專案與實體更新 (Update)**：
   - 修改專案或實體時，檢查相關標籤是否與本指南的定義一致。
   - 若遇到交錯文件（例如會議紀錄中同時提到好好簽現行專案與未來大腦的對接），必須在 Wiki 的 **「相關連結」** 中進行清晰的跨大項交叉引用，但專案本身的 status 與 tags 應保持核心聚焦。
3. **時序日誌 (Log)**：
   - 在 `wiki/log.md` 紀錄操作時，於變更說明中明確標記：`[BreezySign - SaaS/Project]` 或 `[BreezyBrain - Dev/Spec]` 以利快速篩選。
