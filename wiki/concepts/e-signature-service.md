---
title: "電子簽章服務"
type: concept
category: technology
tags: [電子簽章, 數位信任, SaaS]
date_created: 2026-04-18
date_updated: 2026-04-19
source_count: 0
summary: "透過密碼學與系統稽核軌跡，在數位世界賦予文件簽署法律效力的服務。"
---

# 電子簽章服務 (e-Signature Service)

> 電子簽章 (Electronic Signature) 是指依附於電子文件並與其相關連，用以辨識簽署人身分及表示簽署人同意電子文件內容的數位方法。

---

## 技術與法律效力

在 SaaS 軟體的發展中，電子簽章服務必須提供：
1. **身份驗證 (Authentication)**：透過 Email、手機簡訊 (OTP) 或更進階的自然人/工商憑證確保身分。
2. **不可否認性 (Non-repudiation)**：記錄下發送、開啟、同意簽署的 IP、時間戳等稽核軌跡 (Audit Trail)。
3. **文件防篡改 (Integrity)**：簽署完畢後將文件與各項歷程打包，透過數位憑證 (如 AATL) 加密，若被修改即立刻失效。

## 產業生態系

根據我們整理的 [國內電子簽章服務競品比較](../analyses/domestic-e-signature-comparison.md)，電子簽章廠商通常具備不同的戰略定位：
* 有些主打與國際 ERP、文件軟體無縫接軌。
* 有些主攻深度的合規與在地流程（如搭配手寫板、LINE通知）。
* 最核心的評估往往落在「計費模式（人頭 vs 任務）」以及企業需要的合約周邊服務。
