---
title: "WikiLLM 新文件攝入 Runbook"
type: playbook
playbook_type: runbook
category: ai_workflow
tags: [WikiLLM, 知識庫, Ingest, Runbook, LLM]
date_created: 2026-05-14
date_updated: 2026-05-14
related_skills: ["../skills/llm-wiki-management.md", "../skills/ai-agent-prompting.md"]
summary: "使用者說「有新文件加入」時，LLM Agent 執行新文件攝入的完整標準作業程序。"
---

# WikiLLM 新文件攝入 Runbook

> **這是 LLM Agent 的操作 Runbook。** 當使用者說「有新文件加入」或「幫我攝入新文件」時，依此流程執行。

## ✅ 完成定義

- [ ] 確認所有新文件已識別（與 log.md 最後一筆比對）
- [ ] 所有新文件已讀取，關鍵情報已萃取
- [ ] 相關 Wiki 頁面已更新（sources / projects / analyses）
- [ ] log.md 已在頂部追加新的操作記錄
- [ ] 如有新的專案進展，wiki/projects/ 對應頁面已更新

---

## 何時使用

使用者說「有新文件加入」、「攝入新文件」或類似指令時

---

## 前提條件

- 有 `raw/` 目錄的讀取權限
- `wiki/log.md` 可讀寫

---

## 流程

### 步驟 1：掃描新文件（2 分鐘）

1. 讀取 `wiki/log.md` 最新一筆，確認最後攝入的文件日期
2. 列出 `raw/BZSdata/SaaS/`、`raw/BZSdata/Projects/`、`raw/AI_knowhow/` 中的所有文件
3. 比對日期，找出**尚未攝入的新文件**

> ⚠️ 只處理確定是「新的」文件，不重複處理已在 log.md 中記錄的文件

### 步驟 2：讀取新文件

- 完整讀取每份新文件的全文
- 如果是英文，理解原文含義，準備以繁體中文摘要

### 步驟 3：識別影響範圍

判斷每份新文件應更新哪些 Wiki 頁面：

| 文件類型 | 必更新頁面 | 視情況更新 |
|----------|-----------|-----------|
| SaaS 業務日報 | `sources/bzs-sales-reports-2026.md` | `projects/` 相關專案頁 |
| Projects 業務日報 | `sources/bzs-sales-reports-2026.md` | `projects/` 相關專案頁 |
| AI 知識文章 | `sources/` 新建來源頁 | `topics/harness-engineering.md` |
| 市場競品資料 | `sources/` 新建來源頁 | `analyses/esign-domestic-comparison.md` |
| 法規文件 | `sources/` 新建來源頁 | `analyses/bzs-feature-requirements.md` |

### 步驟 4：萃取關鍵情報

對每份日報，提取以下資訊：

**成交記錄**
- 公司名稱、方案、金額、日期

**新商機**
- 公司名稱、行業、規模、主要需求、來源管道

**競品情報**
- 競品名稱、弱點、客戶跳槽原因

**專案進展**
- 哪些進行中的案子有新進展（對應到 `wiki/projects/`）

**技術需求**
- 新功能需求、Bug 回報、特殊場景

### 步驟 5：更新 Wiki 頁面

1. **更新 `sources/bzs-sales-reports-2026.md`**：在最末尾新增該日期的摘要章節
2. **更新相關 `projects/` 頁面**：如日報提到進行中的案子有進展，更新狀態
3. **如有全新知識域**（如 eIDAS 2.0）：新建 `sources/` 頁面，更新 `index.md`

### 步驟 6：追加 log.md

在 `wiki/log.md` **頂部**（YAML header 之後）新增：

```markdown
## [YYYY-MM-DD HH:MM] ingest | [簡短標題]

- **操作者**：LLM Agent (Antigravity / Claude Sonnet 4.6 Thinking)
- **來源文件**：
  - `raw/BZSdata/SaaS/YYYYMMDD日報.md`
- **修改頁面**：
  - `wiki/sources/bzs-sales-reports-2026.md`（新增「...」章節）
  - `wiki/log.md`
- **關鍵發現**：
  - **[發現 1]**：...
  - **[發現 2]**：...

---
```

---

## 驗證完成

- `log.md` 頂部有本次操作記錄 ✓
- `bzs-sales-reports-2026.md` 末尾有新章節 ✓
- 若有新的專案里程碑，對應的 `projects/` 頁面已更新 ✓

---

## 出問題時怎麼辦

**找不到新文件** → 確認 log.md 最後一筆日期，再次比對 raw/ 目錄列表

**日報內容很短或資訊不完整** → 仍需記錄，在 log.md 中標注「內容簡短，無重大發現」

**不確定某文件是否已攝入** → 搜尋 log.md 中的文件名稱，如找到則跳過

---

## 相關連結

- [AGENTS.md 操作規範](../../AGENTS.md)
- [LLM 知識庫管理技能](../skills/llm-wiki-management.md)
- [WikiLLM 索引](../index.md)
- [操作日誌](../log.md)
