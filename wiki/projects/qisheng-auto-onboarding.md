---
title: "棋勝汽車電子合約 Onboarding 專案"
type: project
status: active
priority: medium
tags: [棋勝汽車, 中古車, 電子合約, Onboarding, AATL]
date_started: 2026-06-08
date_updated: 2026-06-10
related_entities: ["qisheng-auto.md", "breezysign.md"]
related_skills: ["../skills/electronic-signature-consulting.md", "../skills/saas-sales-development.md"]
summary: "為中古車龍頭「棋勝汽車」導入好好簽電子合約方案（年用量 2000 份），目前與其自研 CRM 系統進行 API 串接規格規劃與轉單談判中。"
---

# 棋勝汽車電子合約 Onboarding 專案

> 本專案為**電子合約 API 串接與客群 Onboarding 專案**：為知名中古車集團「棋勝汽車」將電子合約無縫介接至其自研的 CRM 系統中。未來客戶規劃將該 CRM + 電簽系統打包為獨立產品販售給其他中古車同業。目前專案重點在於與競品點點簽進行談判，並提供對接技術文件。

## 專案概覽

| 項目 | 內容 |
|------|------|
| **終端客戶** | 棋勝汽車 |
| **年約用量** | 約 2,000 份/年 |
| **技術方案** | 好好簽 (BZS) API 串接、AATL 憑證、OCR 辨識 |
| **當前階段** | 評估與技術展示 (轉單爭奪中，點點簽競品攔截) |

## 目前狀態（截至 2026-06-10）

### ✅ 已完成
- [x] 初步洽談與需求釐清：確立年用量 2,000 份，提供 AATL $30/份報價。 (6/05)
- [x] 關鍵痛點分析：釐清點點簽因「日期無法設為民國年格式」及「業務對技術細節不熟」引發其執行層抗性，我方以此切入。 (6/05)
- [x] **整合測試帳號開通**：帳號 `cw_robot@cwgroup.com.tw` 已開通整合測試兩個月（6/08）；目前仍在拉框規劃，範本建立完成後將以操作員帳號進行測試。
- [x] OCR 識別展示：向客戶介紹好好簽 OCR 身分證、行照等車籍證件識別方案，客戶目前自行測試 Google OCR 效果良好。 (6/05)

### 🔄 進行中
- [ ] 業務跟進：引導客戶端進行好好簽 Sandbox 測試環境開通與 API 試用。
- [ ] 協調技術團隊支援：若客戶端有 CRM 對接民國年格式的疑慮，隨時提供規格諮詢。
- [ ] 轉單合約攻防：針對其老闆與點點簽高層之交情，由商務端 Kelly 進一步跟進中。

### 📅 即將執行
- [ ] 確立棋勝汽車 API 開通時程。
- [ ] 進行 CRM 與好好簽地端/雲端 API 聯調測試。

## 里程碑記錄

| 日期 | 里程碑 |
|------|--------|
| 2026-06-05 | 業務進件，確立 2,000 份需求與 AATL 報價；分析點點簽痛點並介紹 OCR 身分證與行照識別方案 |
| 2026-06-08 | 整合測試帳號 `cw_robot@cwgroup.com.tw` 開通兩個月；目前拉框規劃中，等待範本建立完成後開始操作員測試 |

## 相關文件
- [棋勝汽車實體](../entities/qisheng-auto.md) — 實體資訊
- [點點簽轉單潮深度分析報告](../analyses/esign/esign-dottedsign-price-hike-churn-analysis.md)
- [好好簽 2026-06-05 業務與專案日報](../sources/20260605-projects-daily.md) — 來源日報
- [好好簽 2026-06-08 業務與專案日報](../sources/20260608-projects-daily.md) — 整合測試帳號開通來源
