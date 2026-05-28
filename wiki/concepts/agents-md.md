---
title: "AGENTS.md 標準"
type: concept
category: AI-Engineering
tags: [AGENTS-md, Harness-Engineering, 標準化, 開放格式]
date_created: 2026-04-18
date_updated: 2026-04-18
source_count: 6
summary: "給 AI Agent 的 README——代碼倉庫根目錄的 Markdown 文件，編碼 Agent 工作約定與架構約束"
---

# AGENTS.md 標準

> AGENTS.md 是一個新興的開放約定——本質上是給 AI Agent 的 README。放在代碼倉庫根目錄，Agent 在每次會話開始時自動讀取。它不是靜態文檔，而是一個**活的回饋循環**：每當 Agent 犯錯就更新。

---

## 核心特性

- **不是**一次性編寫後遺忘的靜態文檔
- 每當 Agent 犯錯時都要更新——**文檔變成回饋循環而非靜態制品**
- 簡單的錯誤透過更新 AGENTS.md 解決
- 複雜的問題需要工具層面的解決方案

## 設計原則

### 地圖而非手冊
AGENTS.md 應該是**目錄頁**（約 100 行），指向更深層的文檔，而非百科全書。

巨型指令文件的三個死因：
1. 擠占上下文窗口
2. 無法維護（快速腐壞）
3. 無法機械驗證

### 分層結構

OpenAI 的最佳實踐：

```markdown
# AGENTS.md（約 100 行）

## 架構原則
- 分層架構：Types → Config → Repo → Service → API → UI
- 詳見 [docs/architecture/layering.md]

## 禁止事項
- 不可直接操作生產資料庫
- 不可刪除或重建 infrastructure

## 風險分級
- 見 [risk-tiers.json]

## 測試要求
- 見 [docs/testing/guide.md]
```

### Codex 支援的指令鏈

- 全域 → 專案路徑 → 合併順序
- 預設 32KiB 上限
- 可用 symlink 讓 `CLAUDE.md` 指向 `AGENTS.md`（一份文件維護）

## 各工具的對應

| 工具 | 對應檔案 |
|------|---------|
| OpenAI Codex | `AGENTS.md` |
| Claude Code | `CLAUDE.md` |
| Cursor | `.cursor/rules/` |
| 通用 | `docs/` 目錄 |

## 標準化趨勢

- **2025 年 12 月**：Linux Foundation 成立 Agentic AI Foundation（AAIF）
- OpenAI 捐出 AGENTS.md、Anthropic 捐出 MCP、Block 捐出 goose
- 「讓 agent 可靠取得上下文與工具」開始走向跨廠互通的公共基礎建設
- 官方站點：[agents.md](https://agents.md/)

## Hashimoto 的實踐

> 「Ghostty 專案 AGENTS.md 的**每一行**都對應著一個過去的 Agent 失敗案例。」 — Mitchell Hashimoto

## 相關連結
- [Harness Engineering](../concepts/harness-engineering.md)（概念）
- [Harness Engineering](../topics/harness-engineering.md)（主題頁）
