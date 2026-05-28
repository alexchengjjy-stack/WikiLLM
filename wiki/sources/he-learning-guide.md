---
title: "Harness Engineering 學習指南（GitHub）"
type: source
source_file: "raw/AI_knowhow/deusyuharness-engineering Harness Engineering 学习指南 — 从概念理解到独立实践的深度学习档案.md"
date_ingested: 2026-04-18
tags: [Harness-Engineering, 學習資源, Ralph-Methodology, AGENTS-md, 開源]
author: "deusyu"
original_date: ""
language: "簡體中文（已翻譯摘要）"
summary: "GitHub 開源學習指南，含六大核心概念映射、Ralph 方法論、五階段學習路線"
---

# Harness Engineering 學習指南（GitHub）

> GitHub 上的開源學習專案（deusyu/harness-engineering），從概念理解到獨立實踐，包含 6 大核心概念、Ralph 方法論映射、五階段學習路線和 18 篇資源深度摘要。

## 一句話理解

```
傳統工程：人類寫代碼 → 機器執行代碼
Harness Engineering：人類設計約束 → 智能體寫代碼 → 機器執行代碼
```

**工程師的產出從代碼變成了約束系統**。

## 六大核心概念

| 概念 | 要點 |
|------|------|
| 倉庫即記錄系統 | 不在 repo 裡的東西，對 Agent 不存在 |
| 地圖而非手冊 | AGENTS.md 是目錄頁（~100 行），不是百科全書 |
| 機械化執行 | 文檔會腐壞，lint 規則不會 |
| 智能體可讀性 | 選「無聊」技術（API 穩定、訓練集覆蓋好） |
| 吞吐量改變合併理念 | 糾錯成本低，等待成本高 |
| 熵管理 = 垃圾回收 | Agent 會複製壞模式，需定期清理 |

## Ralph 方法論

Ralph Wiggum Loop：讓 Agent 在循環中自主工作直到任務完成。

| Ralph 信條 | Harness Engineering 對應 |
|------------|------------------------|
| Fresh Context Is Reliability | 智能體可讀性 |
| Backpressure Over Prescription | 機械化執行（門控拒絕壞結果） |
| The Plan Is Disposable | 熵管理 |
| Disk Is State, Git Is Memory | 倉庫即記錄系統 |
| Steer With Signals, Not Scripts | 人類掌舵 |
| Let Ralph Ralph | 智能體執行 |

## OpenAI 關鍵數據

| 指標 | 數值 |
|------|------|
| 團隊規模 | 3 → 7 人 |
| 時間跨度 | 5 個月 |
| 代碼量 | ~100 萬行 |
| PR 數量 | ~1,500 個 |
| 人均日 PR | 3.5 個 |
| 效率估算 | 手工的 ~1/10 時間 |

## 相關連結
- [Harness Engineering](../topics/harness-engineering.md)（主題頁）
- [AGENTS.md 標準](../concepts/agents-md.md)（概念頁）

## 來源引用
- 擷取自：https://github.com/deusyu/harness-engineering
