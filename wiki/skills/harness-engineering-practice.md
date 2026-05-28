---
title: "Harness Engineering 實踐"
type: skill
category: ai_tools
proficiency: advanced
tags: [Harness Engineering, AI工程化, Agent, AGENTS.md, Karpathy]
date_created: 2026-05-14
date_updated: 2026-05-26
related_projects: []
related_concepts: ["../concepts/harness-engineering.md", "../concepts/agents-md.md"]
summary: "將 Harness Engineering 理念落地於實際工作流程：建立 Skills、Linters、Docs 讓 AI Agent 成為領域專家。"
---

# Harness Engineering 實踐

> Harness Engineering 是一套讓 AI Agent 在特定環境中持續發揮最高效能的工程方法論，核心在於「瓶頸不在模型，在基礎設施」。此技能頁記錄將此理念應用於個人工作流的實踐心得。

## 核心理念（個人理解）

三代演進模式：
1. **Prompt 時代**：對話框直接輸入 → AI 輸出 → 效果不穩定
2. **Context 時代**：給予背景資料 → 輸出品質提升
3. **Harness Engineering 時代**：建立基礎設施（Skills / Docs / Linters / Tests）→ AI 成為「環境專家」

**最關鍵洞見**：AI 生成的程式碼/文件是「建構產物（Build Artifact）」，不是目標本身。目標是建立可讓 AI 持續生成高品質產物的環境。

## 五大支柱實踐狀態

| 支柱 | 定義 | 在 WikiLLM 中的實踐 | 完成度 |
|------|------|---------------------|--------|
| **Skills** | 給 Agent 的領域知識包 | AGENTS.md + 各 wiki/ 頁面 | ⬛⬛⬛⬛⬜ 80% |
| **Docs** | 讓 Agent 讀懂系統的文件 | index.md、log.md、overview.md | ⬛⬛⬛⬛⬜ 80% |
| **Linters** | 防止 Agent 犯錯的規則 | AGENTS.md 品質準則 | ⬛⬛⬛⬜⬜ 60% |
| **Reviewer Agents** | 驗證 Agent 輸出的機制 | 手動 Lint 工作流 | ⬛⬛⬜⬜⬜ 40% |
| **Tests** | 驗證知識庫正確性的測試 | 尚未建立 | ⬜⬜⬜⬜⬜ 0% |

## Karpathy 程式碼指南四大黃金實踐原則

此技能深度整合了 Andrej Karpathy 針對 LLM 編碼陷阱倡導的四大核心開發規範，在 WikiLLM 的 Harness 環境中全面落地：

1. **編碼前先思考 (Think Before Coding)**：
   * *實踐*：AI 在動手編輯前，必須在 Thought 區塊中大聲說出假設、可能產生的副作用，在不確定需求時**絕不盲猜**，主動請求人類澄清（嚴格對齊本庫之「思考優先」原則）。
2. **簡單至上 (Simplicity First)**：
   * *實踐*：拒絕為一次性或臨時性任務編寫複雜的類或抽象層，採用最扁平、直觀且代碼量最少的方式解決。
3. **手術式修改 (Surgical Changes)**：
   * *實踐*：嚴格落實**正交編輯**。僅修改與本次任務直接關聯之代碼，絕不擅自「順便改進」無關鄰近區域或註解，以維護 Git diff 的乾淨度與系統穩定性。
4. **目標驅動型執行 (Goal-Driven Execution)**：
   * *實踐*：為任務配置明確的聲明式成功指標（Test Suites / Verify Loops）。例如：在修正圖片文字後，立刻執行 `convert_blog_posts_to_pdf.py` 重新生成討論稿 PDF，以驗證渲染成效，形成自我驗證閉環。

## 個人應用場景

### WikiLLM 作為 Harness 環境
- `AGENTS.md` = Skills Doc（Agent 操作手冊）
- `wiki/index.md` = 導覽地圖（讓 Agent 找到正確頁面）
- `wiki/log.md` = 操作歷史（讓 Agent 了解近期狀態）
- YAML Frontmatter = 結構化輸出規範（Linter）

### 下一步目標
- 建立 `wiki/skills/`（Skill Pack 概念）
- 為常見任務建立 `wiki/playbooks/`（SOP 前饋控制）

## 待深化方向

- [ ] 研究 Reviewer Agent 的實作方式（如：讓另一個 LLM 檢查輸出）
- [ ] 建立自動化測試：驗證所有 Wiki 頁面 Frontmatter 格式正確
- [ ] 實驗「棕地改造」：將現有散亂工作流程遷移至 Harness 架構

## 相關連結

- [Harness Engineering 主題頁](../topics/harness-engineering.md)
- [Harness Engineering 概念](../concepts/harness-engineering.md)
- [AI Agent Prompting](ai-agent-prompting.md)
- [LLM 知識庫管理](llm-wiki-management.md)
- [Karpathy 程式碼指南概念](../concepts/karpathy-coding-guidelines.md)
