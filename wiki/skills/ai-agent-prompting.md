---
title: "AI Agent Prompting 技術"
type: skill
category: ai_tools
proficiency: advanced
tags: [AI, Prompting, LLM, Agent]
date_created: 2026-05-14
date_updated: 2026-05-14
related_projects: []
related_concepts: ["../concepts/harness-engineering.md", "../concepts/agents-md.md"]
summary: "設計有效 LLM 提示詞、建構 Agent 指令系統與 Context Engineering 的技能。"
---

# AI Agent Prompting 技術

> 涵蓋從基本提示詞設計到進階 Context Engineering，以及多 Agent 協作指令架構的實作能力。這是當代知識工作中最核心的 AI 工程技能之一。

## 核心能力

- **Prompt 設計原則**：指令明確化、角色設定（Persona）、輸出格式約束
- **Context Engineering**：控制 LLM 讀取的上下文內容，實現漸進式載入（Progressive Loading）
- **Agent 指令架構**：設計 AGENTS.md 規範、SKILL.md 技能包、工作流程（Workflow）
- **Chain of Thought**：引導 LLM 先思考再行動，降低幻覺（Hallucination）率
- **Few-shot Examples**：在提示中加入示例，快速對齊輸出格式

## 實作經驗

### WikiLLM 知識庫 Agent 系統
- 設計並維護 `AGENTS.md`：定義 Ingest / Query / Lint 三大工作流程
- 建立 Frontmatter 格式規範，讓 LLM 輸出可供 Obsidian Dataview 查詢
- 實踐「漸進式載入」：LLM 先讀 index.md，再按需讀詳細頁面

### 業務情報萃取 Prompt
- 從非結構化日報中提取 90+ 客戶名稱（正規表示式 + LLM 混合方案）
- 設計「關鍵發現」摘要格式，確保每次攝入後可快速掌握核心情報

## 工具與資源

- **Claude Sonnet / Gemini Pro**：主要工作模型
- **Antigravity（本工具）**：任務型 Agent 執行環境
- **參考資源**：[Harness Engineering](../topics/harness-engineering.md)

## 待深化方向

- [ ] 學習 MCP（Model Context Protocol）伺服器架設
- [ ] 實驗 Multi-Agent 協作（如 Agent Teams 方案）
- [ ] 研究 Evals 評估框架，量化 Prompt 品質

## 相關連結

- [Harness Engineering 主題](../topics/harness-engineering.md)
- [LLM 知識庫管理技能](llm-wiki-management.md)
- [ANTIGRAVITY Agent 主控規範](../analyses/antigravity-aipm-framework.md)
