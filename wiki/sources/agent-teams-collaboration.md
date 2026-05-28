---
title: "Agent Teams: I Made 3 AI Agents Write Articles Together"
type: source
category: AI-Engineering
tags: [Agent-Teams, Multi-Agent, Claude, Workflow, Human-On-The-Loop]
date_created: 2026-04-19
source_url: "https://www.youtube.com/watch?v=jFWthWczry4"
author: "废才俱乐部Club"
---

# Agent Teams: I Made 3 AI Agents Write Articles Together | Deep Dive + Full Demo

> 來源目錄：`raw/AI_knowhow/Agent Teams I Made 3 AI Agents Write Articles Together  Deep Dive + Full Demo.md`

## 摘要與核心啟發

本實踐深入探討了大模型能力的一大進階功能：Agent Teams（多智能體團隊協作）。作者展示了如何配置含有總編 (Team Lead)、寫手 (Teammate) 與編輯 (Teammate) 的團隊，利用共享的 Tasklist 與獨立的 Context Window 來全自動完成深度文章的調查、撰寫與審核循環。此實踐破除了對 Sub-agent 的迷思，重新定義了人機協作應從 "Human In the Loop" 退居到 "Human On the Loop"。

## 關鍵知識點提取

### 1. Agent Teams vs Sub-Agent
- **Sub-Agent**：如同委派任務的打工仔，執行完將結果於「同一個上下文窗口」內交還，彼此無法溝通。
- **Agent Teams**：各 Teammate 擁有獨立且完整的 Context Window。它們能藉由 Mailbox 互相質疑、通信、並共享同一個 Tasklist。
- **適用場景**：通訊及協調皆消耗巨大 Token 成本，因此單一 Agent 能幹完的勿用團隊。真正的價值在於需要多角度思考、討論與協作的複雜任務（例如要求一方產出，另一方以 Checklist 審核，兩造抗衡的場景）。

### 2. 寫作系統的四層分離設計
1. **章程、文化與畫像**：
   - `CLAUDE.md`：專案核心，定立角色、團隊架構與相互依存關係。
   - `SOUL.md`：團隊的魂（溝通風格、做決策的態度），使系統回應具備一致的團隊性格。
   - `USER.md`：個人化偏好文件，隨著每次任務的完結而不斷自動沉澱用戶需求。
2. **技能配置 (Skills)**：每一個 Teammate 所屬的工作執行 Sops 與資源讀取權限。
3. **方法論與驗收清單**：寫手依賴分析框架，而編輯依賴嚴格的 Checklists，這是品質防護重點。
4. **輸出模板**：以 Markdown 模板確保每一次 Agent 的輸出格式統一。

### 3. Human On the Loop
- 對比過去「Human in the Loop」（環中人，每步皆須人為確認推動）。
- 新範式為「**Human On the Loop**」（環上人）：Agent Teams 負責自動化運行循環（寫作→被退件修正→再審查），人類不需要緊盯或點頭，只在**循環結束或無法取得共識的關鍵節點**從外部介入裁量並引導最終方向。
