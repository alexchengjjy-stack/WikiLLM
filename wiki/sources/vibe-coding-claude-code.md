---
title: "Product Manager 4.0 — How I Vibe Code with Claude Code"
type: source
category: AI-Engineering
tags: [Vibe-Coding, PM-4.0, Claude-Code, AI-Agent, Harness-Engineering]
date_created: 2026-04-19
source_url: "https://www.youtube.com/watch?v=yIKH0cKCxAk"
author: "废才俱乐部Club"
---

# Product Manager 4.0 — How I Vibe Code with Claude Code

> 來源目錄：`raw/AI_knowhow/Product Manager 4.0 — How I Vibe Code with Claude Code.md`

## 摘要與核心啟發

這份展示 Vibe Coding 開發全流程的實踐紀錄，提出了 **Product Manager 4.0** 的核心概念。運用 Claude Code 開發桌面端短篇小說寫作 Agent，深度實踐了以三層架構為核心的開發流程。打破了從前依賴人工寫代碼與介面限制的開發模式，主張將 AI 當成第一受眾，將框架的穩定性交給 Harness 機制。

## 關鍵知識點提取

### 1. PM 4.0 三層架構
- **頂層規則**：`CLAUDE.md` 定義整個團隊角色與工作流程。
- **技能體系 (Skills)**：覆蓋開發完整鏈路（如 Spec Builder, Design Brief Builder, Design Maker, Dev Planner, Dev Builder, Bug Fixer, Code Reviewer 等）。其中 Bug Fixer 強調系統性除錯（收集證據→分析模式→提出假設→驗證→實施）。
- **進化系統 (Evolution System)**：透過 back-end 掃描將用戶指令沉澱成規則。分為四層進化：靜默紀錄、滿三次自動畢業升級規則、技能最佳化建議、新技能創建建議。

### 2. 開發哲學與工程防護
- **Sub-agent 隔離機制**：每個 Task 皆開啟全新的獨立 Agent 實例，不繼承先前的上下文，避免被前面錯誤的幻覺或猜測污染。
- **Hooks 兜底機制**：依靠 Sensor 自動觸發關鍵檢查（Pre-commit, Code review 中斷攔截 stop-gate, 自動捕捉回饋 Detect feedback signal），確保流程不會因 AI 本身的不可預測而脫軌。

### 3. Vibe Coding 的三條重要心得
1. **先編排，再開發**：先用 Skill/Agent 將業務流程用極低成本跑通（Markdown 中驗證），驗證成功後再正式寫出代碼。
2. **產品第一受眾是 AI**：設計優先考量 AI 能否精準操作（CLI 化），人是通過 Agent 來操作產品。介面是為了被操作而生，而非開局首選。
3. **動態容器概念**：UI 介面不應鎖死功能。Agent 應用本身是一個介面容器，往內加載不同的 Skill（如不同小說題材）即可成為全新產品。
