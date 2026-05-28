---
title: "AI 產品管理（AI PM）"
type: skill
category: product
proficiency: intermediate
tags: [AI, 產品管理, PM, AIPM, MCP, Agent]
date_created: 2026-05-14
date_updated: 2026-05-14
related_projects: []
related_concepts: []
summary: "在 AI 時代進行產品管理的能力，包含 AI 功能規劃、Agent 工作流設計，與 MCP 整合評估。"
---

# AI 產品管理（AI PM）

> 傳統 PM 技能在 AI 時代的進化版：不只管理功能 Backlog，還要設計 AI Agent 的工作流程、評估 LLM 整合的技術可行性，並建立讓 AI 工具有效運作的 Harness 環境。

## 核心能力

- **AI 功能規劃**：識別哪些產品場景適合 AI 增強（生成、分類、摘要、推薦）
- **Agent 工作流設計**：設計多步驟 Agent 任務分解、工具調用、回饋迴路
- **MCP 整合評估**：評估 MCP 伺服器整合的技術成本與業務價值
- **需求文件撰寫（AI 時代版）**：PRD 包含 Prompt 設計、Few-shot Examples、失敗模式
- **AI 產品指標設計**：評估 AI 功能的品質指標（準確率、幻覺率、用戶滿意度）

## AIPM 框架理解

### 毒舌 PM 4.0 與 AIPM 4.0 核心洞見
* **PM 的新角色**：從傳統的「需求翻譯官與畫 wireframe 者」轉型為「Agent 技能編排者與系統設計師」，專注於將業務邏輯模組化。
* **AIPM 4.0 三層架構實踐**：
  1. **頂層規則 (`CLAUDE.md`)**：定義明確的團隊協作規則與行為契約（如 [[claude-rules-12-commandments|CLAUDE.md 12條規則]]），阻絕 AI 在長程開發中的隨機性與副作用。
  2. **技能體系 (Skills)**：將產品規劃、設計、開發、Debug（四階段調試）、審查與發布封裝為 8 大獨立的 Skills，明確執行邊界。
  3. **自動進化系統 (`EVOLUTION.md`)**：後台靜默收集用戶回饋，在同一個操作痛點出現 3 次以上時，提議將其「畢業」升級為 Skill 的正式規則，實現自我迭代。
* **Vibe Coding 時代的 AI-First 產品心法**：
  - **先編排，再開發**：編排成本幾乎為零。先用極低成本的 Markdown 文件配置 Skill 跑通業務邏輯，經快速驗證後再寫代碼，防止方向偏差。
  - **AI 是第一受眾**：產品設計的核心是「AI 能否輕鬆調用（CLI 與 API 優先）」，而非人類視覺界面。UI 界面不是預設的，而是被 Agent 工作流動態「推導」出來的。
  - **容器化動態介面**：界面只扮演技能的容器。底層 UI 的殼是固定的，具體的流程與按鈕透過載入不同的主題技能包動態渲染，徹底消除二次開發成本。

### MCP（Model Context Protocol）對業務的意義
- 鼎新電腦宣告轉向「業務中台 + MCP 框架」：ISV 可自行開發上架
- 對電子簽章廠商的啟示：API/SDK 必須達到 MCP 可串接的品質標準
- 相關需求頁：[BZS 功能需求（MCP 中台化）](../analyses/bzs-feature-requirements.md)

## 產品規劃案例

### 好好簽 API 中台化路徑
1. 當前：Webhook + REST API（鼎新、百加 101 等）
2. 近期：開放 MCP Server（讓 ISV 直接整合到 AI 工作流）
3. 未來：Smart Contract 觸發 → 自動簽署流程

### 功能優先級框架（從客戶日報萃取）
高頻需求（必做）：
- 範本管理 UNIFY 設定
- 批次簽可靠性提升
- Line 傳簽產生連結功能

中頻需求（規劃中）：
- 合約歸檔管理功能（Q2 底）
- 外部表單 AATL 支援
- 公開表單 API 化

低頻需求（觀察）：
- AI 錄音王硬體 Web API 串接
- 多次簽名暫存後一次 AATL 封裝

## 相關連結

- [BZS 功能需求與痛點](../analyses/bzs-feature-requirements.md)
- [[ai-agent-prompting|AI Agent Prompting 技能]]
- [[harness-engineering-practice|Harness Engineering 實踐]]
- [[antigravity-aipm-framework|AIPM ANTIGRAVITY 規範]]
- [[aipm-framework-4|Product Manager 4.0 系統架構]]
- [[claude-rules-12-commandments|CLAUDE.md 12條黃金行為指令]]
