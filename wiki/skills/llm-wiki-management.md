---
title: "LLM 知識庫管理"
type: skill
category: ai_tools
proficiency: expert
tags: [LLM, 知識庫, Obsidian, WikiLLM, 第二大腦]
date_created: 2026-05-14
date_updated: 2026-05-14
related_projects: []
related_concepts: ["../concepts/agents-md.md"]
summary: "設計、維護與擴充 LLM 驅動的個人知識管理系統（WikiLLM）的完整技能。"
---

# LLM 知識庫管理

> 利用 LLM Agent 自動化「攝入 → 摘要 → 連結 → 查詢」整個知識管理週期，將散落的原始素材轉化為結構化、可查詢的知識資產。WikiLLM 是此技能的核心實踐場域。

## 核心能力

- **知識庫架構設計**：目錄結構、頁面類型、Frontmatter Schema 設計
- **Ingest 工作流程**：從非結構化原始文件萃取知識並標準化存入 Wiki
- **知識連結建立**：實體、概念、主題頁面的交叉引用網絡
- **Obsidian 整合**：Dataview 查詢、Graph View 知識圖譜、Canvas 視覺化
- **操作日誌維護**：時序追蹤所有操作，確保知識庫版本可溯源

## 系統設計原則

### 1. 三層知識架構
```
raw/         → 不可變的原始來源
wiki/        → LLM 維護的結構化知識
AGENTS.md    → LLM 的操作規範
```

### 2. 頁面類型設計
| 類型 | 路徑 | 用途 |
|------|------|------|
| `source` | `wiki/sources/` | 每份原始文件的摘要頁 |
| `entity` | `wiki/entities/` | 公司/產品/人物實體頁 |
| `concept` | `wiki/concepts/` | 方法論/框架/技術概念 |
| `topic` | `wiki/topics/` | 跨來源的主題綜合 |
| `analysis` | `wiki/analyses/` | 問答結果與深度分析 |
| `skill` | `wiki/skills/` | 個人技能（新增）|
| `project` | `wiki/projects/` | 工作專案追蹤（新增）|
| `playbook` | `wiki/playbooks/` | SOP/Runbook（新增）|

### 3. 漸進式載入策略
- LLM 優先讀 `index.md` 找目標頁面
- 按需讀詳細頁面，避免浪費 Context Window
- `log.md` 提供近期操作快速掌握

## 實作心得

- **「歸檔有價值的回答」** 是知識庫最容易被忽略的環節——對話中的洞見若不立刻存入 analyses/，就永遠消失了
- **source_file 完整路徑** 必須含子目錄，否則日後 lint 無法驗證來源
- **tag 一致性** 比 tag 數量重要；過多近似 tag 會讓 Dataview 查詢結果分裂

## 相關連結

- [AGENTS.md 操作規範](../../AGENTS.md)
- [AI Agent Prompting](ai-agent-prompting.md)
- [Obsidian 知識管理](obsidian-knowledge-management.md)
- [Wiki 索引](../index.md)
