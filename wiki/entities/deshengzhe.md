---
title: "得勝者"
type: entity
entity_type: company
aliases: ["得勝者", "得勝者諮詢"]
tags: [healthcare, client, integration, pacs_ai]
date_created: 2026-06-01
date_updated: 2026-06-01
source_count: 3
sources: ["20260528-projects-daily.md", "20260529-projects-daily.md", "deshengzhe-meeting-report-20260601.md"]
summary: "得勝者為醫療資訊與諮詢服務提供商，旗下包含盧森眼科與東港盧森，目前正與商之器合作串接 mAIn 醫療影像 AI 平台之電子簽章服務。"
---

# 得勝者

> 得勝者為電子簽章在醫療健康領域的關鍵落地客戶。旗下包含盧森眼科與東港盧森。目前專案包含旗下眼科診所電子簽署導入，以及與商之器（EBM Technologies）合作的 PACS（醫療影像存檔與通信系統）醫療影像 AI 整合平台 mAIn 電子簽章介接。

## 核心要點
- **旗下診所導入**：盧森眼科與東港盧森（同老闆）預計於 6 月進行測試、7 月正式上線。每一家診所收費 NT$25,000，包含加購 1,500 份 AATL 憑證，共計 NT$50,000 (含稅)。
- **PACS 醫療影像 AI 整合**：與南港「商之器」合作，針對其 mAIn 醫療影像 AI 整合平台（透過 Pass-Through 影像運算機制直接串接於醫院 PACS 後台的 AI 引擎）進行好好簽電子簽章 API 整合，預計於 6-7 月進行技術測試。

## 詳細內容

### 1. 旗下診所導入詳情
得勝者旗下主要眼科診所「盧森眼科」與「東港盧森」因應醫療文件無紙化與 AATL 數位憑證自證力需求，決定導入好好簽。
- **時程規劃**：2026 年 6 月進行功能與合約測試，7 月正式啟用上線。
- **合約財務**：兩家診所合計簽約金額為 NT$50,000（含稅），其中包括了好好簽系統授權與加購的 1,500 份 AATL 數位憑證費用。

### 2. 醫療影像 AI 平台 (PACS) 整合
得勝者近期與「商之器」洽談其 mAIn (Multi AI Nexus PACS) 平台之電子簽章合作。
- **技術背景**：mAIn 並非專門的獨立軟體，而是串接於醫院 PACS 後台的 AI 處理引擎，核心技術為「Pass-Through」影像運算機制。當 AI 引擎拋出診斷分析或醫療影像報告時，需要電子簽章來保障報告的真實性與不可篡改性。
- **串接模式**：透過 BZS API，將電子簽章機制無縫封裝於 mAIn 的 Pass-Through 工作流中。預計於 6-7 月展開系統測試。

## 相關連結
- [得勝者 PACS 醫療影像系統整合專案](../projects/deshengzhe-pacs-integration.md) — 專案進展
- [2026-05-29 專案與 API 業務日報](../sources/20260529-projects-daily.md) — 來源日報

## 來源引用
- [得勝者醫療資訊整合專案會議紀錄](../sources/deshengzhe-meeting-report-20260601.md) — 6/1 會議紀錄來源
- [20260528-projects-daily.md](../sources/20260528-projects-daily.md) — 盧森眼科與 PACS 最初提及
- [20260529-projects-daily.md](../sources/20260529-projects-daily.md) — 會議與 PACS 更新
