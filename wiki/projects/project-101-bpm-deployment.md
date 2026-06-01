---
title: "101 客戶 BPM 系統建置專案"
type: project
status: active
priority: medium
tags: [101, BPM, 地端部署, HiCloud, 系統建置]
date_started: 2026-03-01
date_updated: 2026-06-01
related_entities: []
related_skills: ["../skills/electronic-signature-consulting.md"]
summary: "BZS 替客戶「101」進行 BPM 系統整合建置，包含電子簽章串接與 HiCloud+DMZ 地端部署架構，已完成安裝文件與 source code 交付及異常 Email 提案。"
---

# 101 客戶 BPM 系統建置專案

> 這是一個**技術實作型專案**：BZS 為終端客戶「101」建置含電子簽章功能的 BPM（企業流程管理）系統，搭配地端部署架構（HiCloud + DMZ 隔離區）。與「101plus BPM 通路合作」不同——101plus 是 SI 合作夥伴，「101」是 101plus 引薦進來的**終端客戶**。

## 專案概覽

| 項目 | 內容 |
|------|------|
| **終端客戶** | 101（透過 101plus 引薦）|
| **專案性質** | 系統建置 + 地端部署（非 SaaS 訂閱）|
| **核心整合** | 好好簽電子簽章 + BPM 流程 + 地端部署 |
| **技術窗口** | Neil（負責設定與測試；5/13 帳號已加入 101 組織管理）|

## 目前狀態（截至 2026-06-01）

### ✅ 已完成
- [x] 初版系統部署完成（已可連線，Teamviewer 遠端設定就緒）
- [x] 與 101 就架構細節確認並持續討論
- [x] 垃圾桶留存天數調整：14 天 → **10 天**（配合 101 需求）
- [x] Neil 帳號加入 101 組織管理（5/13 完成，利於後續設定）
- [x] 確認合約與軌跡紀錄維持**分開提供**，以避免合併檔案破壞 AATL 數位簽章效力（5/28）
- [x] 規劃合約與軌跡紀錄的關聯性檔名命名（例如：合約為 `123`，軌跡檔為 `123_軌跡`）（5/28）
- [x] 交付 Hi-Cloud 和 DMZ 的安裝文件與 Source Code (5/29)
- [x] 為 101 技術窗口 (`steven.yu@tfc101.com.tw`) 開通支援 10 份雲端憑證 (5/29)

### 🔄 進行中
- [ ] **BPM 存取系統**：剩餘 BPM 功能開發中
- [ ] **佈署環境架構調整**：HiCloud 與 DMZ 間轉介 Server 安裝調整中
- [ ] **寫回機制異常邏輯**：規劃寫回成功與失敗的系統容錯與重試邏輯（預計 6 月初完成）
- [ ] **異常通知與檢測討論**：方針對系統異常時自動發送 Email 通報進行討論，Hank 提案兩方案：
  - *方案1*：HiCloud 與 DMZ 互相偵測，若異常由 101 端發送 Email（我方發送有困難）。
  - *方案2*：我方提供 `isHealth API`，由 101 端定期偵測服務狀態。

### 📅 即將執行
- [ ] 完成 HiCloud + DMZ 轉介 Server 設置
- [ ] 完整 BPM 功能驗收與異常寫回及偵測機制測試
- [ ] 系統正式驗收與上線

## 技術架構

```
HiCloud（公有雲）
    ↓ 轉介 Server（新增中）
DMZ（隔離區）
    ↓
BPM 系統（101Form BPM）
    ↓ API
好好簽（BZS）電子簽章服務
```

### 關鍵設定
- 垃圾桶留存天數：**10 天**（已調整，配合 101 資安需求）
- 轉介 Server：解決 HiCloud 與 DMZ 間的網路隔離問題
- 檔案提供方式：合約檔與軌跡紀錄檔維持獨立，使用關聯檔名
- 技術窗口帳號：[steven.yu@tfc101.com.tw](mailto:steven.yu@tfc101.com.tw)（配置 10 份雲端憑證）

## 里程碑記錄

| 日期 | 里程碑 |
|------|--------|
| 2026-04-29 | 初版系統完成，Teamviewer 遠端協作設定好，開始與 101 討論細節 |
| 2026-05-12 | 確認 HiCloud+DMZ 需新增轉介 Server，程式碼需重新拆分 |
| 2026-05-13 | 垃圾桶留存 10 天；Neil 帳號加入 101 組織管理 |
| 2026-05-28 | 確定合約與軌跡紀錄分開以保護 AATL 簽章，並使用關聯檔名；提供寫回機制異常處理架構，預計 6 月初完成 |
| 2026-05-29 | 交付 Hi-Cloud 和 DMZ 的安裝文檔與原始碼；開通 steven 帳號 10 份雲端憑證；提案兩種異常通知與 isHealth 檢測機制 |

## 相關文件

- [BZS 業務日報摘要](../sources/bzs-sales-reports-2026.md)
- [2026-05-28 專案與 API 業務日報](../sources/20260528-projects-daily.md) — 合約與軌跡決策來源
- [2026-05-29 專案與 API 業務日報](../sources/20260529-projects-daily.md) — 安裝與異常方案來源
- [百加 BPM 通路合作](pai-plus-bpm-partnership.md)
- [電子簽章顧問技能](../skills/electronic-signature-consulting.md)

