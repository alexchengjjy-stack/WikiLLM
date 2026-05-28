---
title: "鼎新電腦 API 對接專案"
type: project
status: active
priority: high
tags: [鼎新, API, ERP, 通路合作]
date_started: 2026-04-01
date_updated: 2026-05-20
related_entities: []
related_skills: ["../skills/electronic-signature-consulting.md", "../skills/saas-sales-development.md"]
summary: "好好簽與鼎新電腦的 API 技術對接，整合至諸葛 AI 平台，觸及台灣 2 萬家製造業客戶。"
---

# 鼎新電腦 API 對接專案

> 好好簽（BZS）與鼎新電腦進行 API 整合，將電子簽章功能嵌入鼎新諸葛 AI 平台。此為重要通路合作，可觸及鼎新台灣 2 萬家、大陸 4 萬家製造業客戶群。

## 專案概覽

| 項目 | 內容 |
|------|------|
| **合作夥伴** | 鼎新電腦（ERP / AI 諸葛平台） |
| **市場規模** | 台灣 2 萬家 + 大陸 4 萬家（製造業為主）|
| **合約模式** | 70%（BZS）/ 30%（鼎新）拆帳 |
| **基礎方案** | $3,000/年，含 100 份 AATL；超額 $30/份；雲端憑證 $80/份 |
| **窗口** | 鼎新 PO（API 對接）；鼎新法務（合約審核）|

## 目前狀態（截至 2026-05-13）

### ✅ 已完成
- [x] 確認 API 功能清單（雲端憑證、AATL、遠距簽、現場簽）
- [x] 5/12 API 文件更新，提供給鼎新開發端
- [x] 5/13 技術會議：提供技術簡報、新帳號 Private Key、確認 `createTaskUrl` 有效期限
- [x] 建立微信群組（鼎新技術聯繫管道）
- [x] BZS 端新增價格方案（合約條款其他部分 OK）
- [x] 建立新對接帳號 (isv.connector@gmail.com)，方案改為 SI 並提供 Private Key（5/20）

### 🔄 進行中
- [ ] **合約**：鼎新法務端審核中（BZS 新增價格方案後再次送審）
  - [ ] **API 實作對接**：Hank 持續協助鼎新技術團隊整合問題（進行中）

### 📅 即將執行
- [ ] **YT 就享知直播**（時間 TBD）：聯合行銷活動
- [ ] **6/11 直播活動**：同時訂閱加贈 2 個月免費使用
- [ ] **BZS 與諸葛平台串接**：預計 **6 月完成**

## 里程碑記錄

| 日期 | 里程碑 |
|------|--------|
| 2026-04-xx | 確認合作框架，進入合約談判 |
| 2026-05-08 | 鼎新確認 5/13 提供 API，安排 5/13~5/22 實作對接 |
| 2026-05-12 | API 文件更新（下午），API Key 提供 |
| 2026-05-13 | 技術會議完成；法務審核中；行銷活動規劃確認 |
| 2026-05-20 | 建立新對接帳號 (isv.connector@gmail.com)，改為 SI 方案並提供 Private Key；Hank 持續對接技術問題 |

## 風險與注意事項

- ⚠️ **大陸 VPN 問題**：鼎新部分客戶在大陸，需評估 VPN 連線替代方案
- ⚠️ **MCP 框架轉型**：鼎新預告轉向業務中台 + MCP，BZS API 品質要求將大幅提升
- ⚠️ **諸葛平台-鐵工廠**：報價單電子化專案，建議串接完成後引導升級加購

## 相關文件

- [BZS 業務日報摘要](../sources/bzs-sales-reports-2026.md)
- [API 方案報價 SOP](../playbooks/api-proposal-flow.md)
- [電子簽章顧問技能](../skills/electronic-signature-consulting.md)
