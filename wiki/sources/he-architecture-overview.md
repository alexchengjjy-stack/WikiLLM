---
title: "Harness Engineering 架構全景"
type: source
source_file: "raw/AI_knowhow/Harness Engineering 架構全景：AI 可以寫 Code，但不能自己上 Production.md"
date_ingested: 2026-04-18
tags: [Harness-Engineering, 架構, 防禦體系, CI-CD, 安全, Amazon]
author: "Wisely Chen"
original_date: "2026-03-11"
language: "繁體中文"
summary: "七元件參考架構、三層防禦體系、五大失效模式，含大量實戰程式碼範例"
---

# Harness Engineering 架構全景

> Wisely Chen 的系列文章整合版，以「AI 可以寫 Code，但不能自己上 Production」為主題。提供最完整的參考架構，含七元件、三層防禦、五大失效模式，以及大量可直接使用的程式碼範例。

## 七元件參考架構

| # | 元件 | 關鍵能力 |
|---|------|---------|
| 1 | Context System | AGENTS.md、知識庫、MCP/RAG |
| 2 | Architecture Guardrails | 結構測試、自訂 Lint、依賴規則 |
| 3 | Eval & Test Harness | 單元/整合/E2E/LLM Eval |
| 4 | CI/PR Automation | 自動審查/修復/合併 |
| 5 | Safety & Policy | Sandbox、審批策略、Policy as Code |
| 6 | Observability | Tracing、Logs、Metrics、成本監控 |
| 7 | Feedback Loops | Doc Gardening、GC Tasks、回饋吸收 |

## 三層防禦架構

| 層級 | 名稱 | 比喻 | 職責 |
|------|------|------|------|
| 第一層（核心） | **分級審查** Risk Tiering | 紅綠燈規則 | 根據**爆炸半徑**決定審查強度 |
| 第二層 | **四層防禦** | 每個紅綠燈的判斷邏輯 | Test → Lint → CI Gate → LLM Judge |
| 第三層（最外） | **控制平面** Control Plane | 完整交通管制 | PR 生命週期八步閉環 |

**核心公式**：AI 生成代碼品質 = 80% 測試覆蓋率 + 20% Prompt 品質

## 亞馬遜禁令 vs. Harness Engineering

| | 亞馬遜禁令 | Harness Engineering |
|---|---|---|
| 護欄方式 | 人的注意力 | 系統的架構 |
| 速度 | 降速（人工瓶頸） | 加速 |
| 擴展性 | 資深工程師成瓶頸 | Peter Steinberger 一人一天 627 次提交 |

## 五大失效模式

1. **上下文腐壞**（Context Rot）— AGENTS.md 與 repo 脫節
2. **架構漂移與模式複製** — Agent 忠實複製壞模式，速度 10 倍
3. **測試 Flake 與錯誤合併策略**
4. **安全外溢** — Prompt injection、權限過大
5. **供應鏈崩壞** — Agent 更頻繁新增依賴

## 導入路線圖

| 規模 | 時程 | 年度預算 |
|------|------|---------|
| 小型（1 repo） | 4-6 月 | $100K-300K |
| 中型（3-10 repo） | 6-9 月 | $700K-1.8M |
| 企業級 | 9-12 月 | $3-10M |

## 相關連結
- [Harness Engineering](../topics/harness-engineering.md)（主題頁）

## 來源引用
- 擷取自：https://ai-coding.wiselychen.com/harness-engineering-architecture-overview-ai-code-production-guardrails/
