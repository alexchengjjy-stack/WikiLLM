---
title: "Harness Engineering — AI 工程師的第三個維度"
type: source
source_file: "raw/AI_knowhow/Harness Engineering — AI 工程師的第三個維度.md"
date_ingested: 2026-04-18
tags: [Harness-Engineering, AI-Agent, Prompt-Engineering, Context-Engineering]
author: "溫煜鈞"
original_date: "2026-04-02"
language: "繁體中文"
summary: "清楚釐清 Prompt/Context/Harness Engineering 三層關係，提出 Harness 五維度框架"
---

# Harness Engineering — AI 工程師的第三個維度

> 溫煜鈞在 WordPress 上發表的文章，清楚地釐清了 Prompt、Context、Harness Engineering 三者各自解決的問題層次，並提出 Harness 的五個維度框架。

## 三層關係

| 層次 | 核心問題 | 比喻 |
|------|---------|------|
| Prompt Engineering（訊息層） | 怎麼**說**，才能得到最好的輸出？ | — |
| Context Engineering（信息層） | 什麼信息，應該在什麼時候進入 context window？ | — |
| **Harness Engineering（系統層）** | 怎麼建立一套系統，讓模型能安全、可控地在真實世界行動？ | 馬術中的韁繩裝備 |

三者是**嵌套關係**：`Harness ⊃ Context ⊃ Prompt`。

## Harness 五維度

| 維度 | 職責 |
|------|------|
| 資源管理 | Token 預算、成本控制、熔斷機制 |
| 狀態持久化 | Memory 系統，讓 stateless 模型在有狀態世界工作 |
| 信息流控制 | Context 壓縮、雙視圖，決定模型每輪「看到什麼」 |
| 安全邊界 | 工具權限、行為約束 |
| 任務編排 | Multi-agent 協調 |

## 關於 Managed Agents 的更新（2026/4/9）

Claude Managed Agents 出現後，作者指出：
- Managed Agents 解決的是 Harness 的「管線問題」（plumbing）
- **不解決**：tools 設計、system prompt、任務拆解、domain-specific 錯誤處理
- Harness Engineering 不會消失，而是**升維**：從「怎麼讓 Agent 不掛掉」到「怎麼讓 Agent 做對的事」
- Agent 設計必須**可快速拆裝**，每一層可獨立替換

## 相關連結
- [Harness Engineering](../topics/harness-engineering.md)（主題頁）
- [Harness Engineering 概念](../concepts/harness-engineering.md)（概念頁）

## 來源引用
- 原始來源：[raw/AI_knowhow/Harness Engineering — AI 工程師的第三個維度.md](../../raw/AI_knowhow/Harness%20Engineering%20%E2%80%94%20AI%20%E5%B7%A5%E7%A8%8B%E5%B8%AB%E7%9A%84%E7%AC%AC%E4%B8%89%E5%80%8B%E7%B6%AD%E5%BA%A6.md)
- 擷取自：https://wenwender.wordpress.com/2026/04/02/harness-engineering-ai-工程師的第三個維度/
