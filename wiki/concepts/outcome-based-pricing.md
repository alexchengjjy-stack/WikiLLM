---
title: "Outcome-Based Pricing"
type: concept
category: methodology
tags: [UBP, Outcome-Based, SaaS-Pricing, Unit-Economics]
date_created: 2026-06-02
date_updated: 2026-06-02
source_count: 2
sources: ["../sources/saaspocalypse-insight.md", "../analyses/bzs/bzs-pricing-cost-structure-analysis-20260525.md"]
summary: "結果/使用量計費模式：隨著 GenAI 帶來 Token 變動成本，軟體計費從傳統席位制轉向按成果與實際用量計費的演進趨勢。"
---

# Outcome-Based Pricing (結果導向計費) & UBP

> **結果導向計費 (Outcome-Based Pricing)** 與 **使用量計費 (Usage-Based Pricing, UBP)** 是指軟體的收費不再與「使用人數（席位）」綁定，而是與「軟體為客戶創造的具體成果、完成的任務數量或消耗的資源量」掛鉤的定價模式。

---

## 核心演進背景

在 AI 時代前，SaaS 主要採取 **Seat-based (席位制)** 計費，其前提是：
1. 新增用戶的邊際成本趨近於零，從而享有 70-80% 的高毛利率。
2. 企業的軟體支出與員工數量呈線性成長關係。

然而，GenAI 的興起從根本上顛覆了這兩大前提，推動了計費模式的重構：
*   **變動成本 (Variable Costs) 的引入**：AI 的 Token 推論、算力與存儲直接與使用量綁定，運算成本呈現明確的變動成本特性。如果繼續採用席位吃到飽，高頻使用戶將會嚴重稀釋甚至吃掉軟體公司的利潤空間。
*   **AI 替代人力導致席位流失**：AI Agent 與自動化工具能替企業完成重複性與流程性工作。當原本 3~5 人的工作量能被 1 個 AI Agent 解決時，企業採購的 SaaS 席位數將會下降，Seat-based 模式面臨失效。
*   **責任與任務轉移**：傳統 SaaS 將維運責任轉給供應商；Outcome-based 則是將「具體任務結果」轉移給供應商。彭博預測，SaaS 傳統訂閱制在 2025-2035 年的 CAGR 僅 2%，而 Outcome-based 將以 **30% 的年複合成長率** 高速膨脹。

---

## 業界實踐案例

1.  **Salesforce (Agentforce)**：採取 Flex Credit（每 10 萬點 500 美元）或 Conversations（每場對話 2 美元）計費，依 AI 客服與消費者的實際對話次數收費。
2.  **Sierra (AI Agent 客服)**：採取 100% 的 Outcome-based 計費，僅在 AI 客服成功解決客戶問題、完成特定任務時收費。
3.  **Workday**：於 2026 年初提出防範外部 AI「寄生（Parasite）」調用其 SoR 數據的防線，計劃對通過 API 讀取 Workday 數據以運行第三方 Agent 的行為收取 consumption (消耗型/流量型) 費用。

---

## BreezySeries (好好簽 & 好好腦) 的應對

### 1. BreezySign (好好簽) 的防禦與轉型
好好簽本身面臨 AATL 憑證 (NT$1.5/份) 與簡訊 (NT$0.85/則) 的通道變動成本。
*   **大戶去載安全閥**：限制個人專業方案的吃到飽額度（如 150 份/月），超額強制購買憑證加購包（每次最少 5 份，每份 NT$15 ~ $30），守住 **78%~94%** 的毛利率。
*   **混合 UBP 模型**：推動「固定基礎席位費 + 超額 UBP」的收費方案（如企業版年約內含 5,000 份凭證，超額按憑證以件加價計費）。

### 2. BreezyBrain (好好腦) 的計費優勢
好好腦作為地端工作流操作系統，其 CRM 去重、CLM 自動審約等模組均為「任務結果導向」。
*   地端部署收取軟體授權與 FDE 部署費。
*   CLM 的 AI 審約可採用 Outcome-based 定價（按審核合約份數或 API 調用次數計費），將運算負荷留在地端或安全雲端 API 中，避免毛利率受外網 Token 價格波動的影響。

---

## 相關連結
* [SaaSpocalypse 深度分析報告摘要](../sources/saaspocalypse-insight.md)
* [好好簽定價成本結構與利潤邊際分析報告](../analyses/bzs/bzs-pricing-cost-structure-analysis-20260525.md)
* [Vibe Coding 範式與實踐](vibe-coding-paradigm.md)
