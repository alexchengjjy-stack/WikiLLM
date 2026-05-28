---
title: "Obsidian 知識管理"
type: skill
category: ai_tools
proficiency: intermediate
tags: [Obsidian, 知識管理, PKM, Dataview, Markdown]
date_created: 2026-05-14
date_updated: 2026-05-14
related_projects: []
related_concepts: []
summary: "使用 Obsidian 進行個人知識管理（PKM），包含插件配置、Dataview 查詢與知識圖譜建立。"
---

# Obsidian 知識管理

> Obsidian 是以本地 Markdown 為核心的知識管理工具，WikiLLM 整個知識庫即以 Obsidian Vault 形式組織。掌握此工具可視覺化知識網絡、快速搜尋並進行進階查詢。

## 核心能力

- **Vault 架構設計**：目錄結構規劃、Template 設定、Attachment 管理
- **Dataview 查詢**：用類 SQL 語法查詢 Frontmatter 元資料
- **Graph View**：視覺化頁面連結網絡，發現知識空白
- **快速筆記**：Daily Note + Templater 自動產生日誌頁面
- **插件管理**：Dataview、Templater、Calendar、Git 同步

## 常用 Dataview 查詢

### 查詢所有技能頁（按熟練度）
```dataview
TABLE proficiency, summary, date_updated
FROM "wiki/skills"
SORT proficiency DESC
```

### 查詢進行中的專案
```dataview
TABLE status, priority, summary
FROM "wiki/projects"
WHERE status = "active"
SORT priority DESC
```

### 查詢本週更新的頁面
```dataview
TABLE type, summary
FROM "wiki"
WHERE date_updated >= date(today) - dur(7 days)
SORT date_updated DESC
```

### 查詢特定標籤的所有頁面
```dataview
TABLE type, summary, date_updated
FROM "wiki"
WHERE contains(tags, "AI")
SORT date_updated DESC
```

## 插件推薦配置

| 插件 | 用途 | 設定重點 |
|------|------|----------|
| **Dataview** | 動態查詢 | 啟用 JS 查詢、內聯查詢 |
| **Templater** | 自動填入 Frontmatter | 新頁面觸發器 |
| **Git** | 版本控制與備份 | 每日自動 commit |
| **Calendar** | Daily Note 導航 | 連結到 log.md |
| **Local Graph** | 局部知識圖譜 | 調整 depth=2 |

## 待深化方向

- [ ] 設定 Templater 自動填入 WikiLLM Frontmatter
- [ ] 建立 Canvas 視覺化電子簽章市場地圖
- [ ] 研究 Obsidian Publish 作為對外輸出管道

## 相關連結

- [LLM 知識庫管理](llm-wiki-management.md)
- [WikiLLM 索引](../index.md)
