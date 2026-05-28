---
title: "Harness Engineering 完全解析"
type: source
source_file: "raw/AI_knowhow/Harness Engineering 完全解析：當 AI Agent 的護城河不再是模型，而是環境.md"
date_ingested: 2026-04-18
tags: [Harness-Engineering, AI-Agent, Guides-Sensors, 企業案例, OpenAI, Anthropic, Stripe]
author: "BASHCAT (HackMD)"
original_date: ""
language: "繁體中文"
summary: "最全面的 Harness Engineering 綜述，含 Guides×Sensors 矩陣、五大企業案例、五級實作路徑"
---

# Harness Engineering 完全解析

> HackMD 上最全面的 Harness Engineering 中文綜述文章。從三代範式演進到 Guides×Sensors 技術框架，涵蓋五家企業實戰案例，並提供從 Level 1 到 Level 5 的漸進式實作路徑。

## Guides × Sensors 框架（Birgitta Böckeler / Martin Fowler）

|  | Computational（確定性） | Inferential（推理性） |
|---|---|---|
| **Guide（前饋）** | LSP、TypeScript 型別系統、架構文檔 | AGENTS.md、AI 生成規劃、Skills |
| **Sensor（回饋）** | ESLint、semgrep、coverage 檢查 | AI Code Review、Architecture Review |

**成熟的 Harness 需要四個象限都有覆蓋。**

## 五大企業案例

| 企業 | 核心做法 | 關鍵洞察 |
|------|---------|---------|
| **OpenAI Codex** | 3人/5個月/100萬行零手寫 | Linter 錯誤訊息內嵌修復指令；Garbage Collection Agent |
| **Anthropic Claude Code** | Planner-Generator-Evaluator 三代理架構 | Initializer Agent 設定工作環境；模型無法可靠評估自己的工作 |
| **Stripe Minions** | 每週數千個 AI PR | 明確退出條件；最大迭代 3-5 次 |
| **Datadog** | Harness-first + 可觀測性閉環 | Production telemetry 回饋修正 Harness 本身 |
| **Manus** | 同一模型重寫 5 次 Harness | 每次重寫方向都是**簡化**；護城河在 Harness 不在模型 |

## 五級實作路徑

| Level | 做什麼 |
|-------|--------|
| 1 | 建立 AGENTS.md（第一個 Guide） |
| 2 | 添加 Computational Sensor（自定義 ESLint） |
| 3 | CI Pipeline 整合 |
| 4 | 引入 Inferential Sensor（AI Code Review） |
| 5 | 建立可觀測性追蹤指標 |

## 五個陷阱

1. 過度約束扼殺 Agent 創造力
2. Harness 本身的 bug（Who watches the watchmen?）
3. 只有回饋沒有前饋
4. 忽略推理型感測器
5. 把 Harness 當一次性工作

## 相關連結
- [Harness Engineering](../topics/harness-engineering.md)（主題頁）

## 來源引用
- 擷取自：https://hackmd.io/@BASHCAT/SkQEW0F2bg
