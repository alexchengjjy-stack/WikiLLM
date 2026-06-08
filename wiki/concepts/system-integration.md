---
title: "系統整合 (System Integration)"
type: concept
category: methodology
tags: [好好簽, 系統整合, API串接, 數位轉型]
date_created: 2026-06-08
date_updated: 2026-06-08
source_count: 1
sources: ["wiki/sources/system-integration-welly-seo.md"]
summary: "將企業內部原本分散的軟硬體系統、資料庫與作業流程，透過規劃與串接，建立能協同運作的整體架構。"
---

# 系統整合 (System Integration)

> 系統整合（簡稱 SI）是指將企業內部原本分散運作的軟體系統、硬體設備、網路架構與資料庫，透過標準的接口（如 API、Webhook 或 Middleware）進行重新規劃與串接，建立能協同運作、即時交換資料並自動化執行業務邏輯的整體資訊架構。

## 核心要點
- **消除資訊孤島**：透過資料與系統功能的串接，防止各部門資料重複輸入與流程中斷。
- **5 大整合維度**：資料整合、UI 介面整合、流程整合、雲端整合、軟體系統整合。
- **電子簽章的 SI 核心價值**：在不改變企業既有 ERP 或 BPM 操作習慣的前提下，將「身分驗證、電子簽署、安全憑證與文件歸檔」自動化嵌入現有業務流程中。

## 詳細內容

### 1. 系統整合在好好簽電子簽章的實作模式
企業在導入電子簽章時，通常有以下幾種系統整合架構：
- **標準 API 串接**：
  * 好好簽提供完善的 RESTful API 與 Sandbox 測試環境。
  * 企業的 ERP（如報價、採購系統）或 BPM（流程管理平台）可直接發起簽署請求，自動產生專屬傳簽連結或派發通知。
- **Webhook 動態事件回流**：
  * 當簽署者完成簽署、拒絕簽署或合約逾期時，系統即時拋送 Webhook 訊號回企業伺服器。
  * 系統接獲 Webhook 後，自動下載完簽 PDF（含 AATL 憑證及 SHA-256 雜湊值防竄改保護）並回存至企業地端或雲端檔案管理系統。
- **硬體與平板整合（現場臨櫃簽署）**：
  * 結合實體「蒙恬電子簽名板」與平板系統，進行面對面無紙化申辦。字跡即時呈現在合約中，並與 eKYC/CDD 身分驗證機制整合。

### 2. 代表性企業系統整合案例
- **太平洋旅行社（BPM 與電子簽約）**：
  * 利用 Webhook/API 產生簽名連結，並透過簡訊與 Line 傳簽，使旅客可在坐捷運或公車等空檔完成定型化契約手寫簽名，合約回收率從 60% 飆升至 98%。
- **鼎新電腦（ISV 生態合作）**：
  * 將電子簽章服務深度嵌入 ISV ERP 流程中，優化連結時效與批次傳簽機制。

## 相關連結
- [太平洋旅行社實體](../entities/pacific-travel.md)
- [鼎新電腦 API 對接專案](../projects/ding-xin-api-integration.md)
- [系統整合部落格完稿文章](../analyses/bzs/system-integration-blog-post-20260608.md)

## 來源引用
- [系統整合 Welly SEO 審核稿](../sources/system-integration-welly-seo.md) — 系統整合定義與情境來源
