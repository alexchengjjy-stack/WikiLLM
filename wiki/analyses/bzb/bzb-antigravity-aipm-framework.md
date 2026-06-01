# Antigravity AIPM (AI Product Management) 框架分析報告

> **狀態**：已正式攝入 WikiLLM
> **核心來源**：`raw/AIPM/Agent.md`, `raw/AIPM/project.md`
> **關聯概念**：[Harness Engineering](../topics/harness-engineering.md), [Vibe Coding](../concepts/vibe-coding-paradigm.md)

## 01. 什麼是 AIPM？
AIPM 是一套專為 **Antigravity AI Agent** 設計的產品開發與專案管理框架。其核心目標是透過「角色化指令」與「標準化文件結構」，解決 AI 在長程開發中容易產生的「語意漂移」與「黑箱操作」問題。

## 02. 四大核心角色模式與 8 大 Skills 體系

隨著 AIPM 演進至 **AIPM 4.0**，原有的四大角色（/pm, /ui, /dev, /test）已經完全融會貫通並映射為產品開發全鏈路的 **8 大標準技能（Skills）**，藉此實現更高密度的功能模組化：

| 原始角色 | 對應 AIPM 4.0 技能包 (Skills) | 職責與輸出產出 |
| :--- | :--- | :--- |
| **/pm** | **Product Spec Builder** | 收集需求，撰寫面向 AI 的產品需求文檔 `Product-Spec.md` |
| **/ui** | **Design Brief Builder**<br>**Design Maker** | 制定設計視覺調性與規範文檔 `Design-Brief.md`<br>使用設計 MCP 工具全自動繪製 Pencil/Figma 原型圖 |
| **/dev** | **Dev Planner**<br>**Dev Builder** | 調研開源代碼與依賴，生成詳細開發進度排期 `DEV-PLAN.md`<br>依照任務清單執行增量代碼編寫與編譯 |
| **/test** | **Bug Fixer**<br>**Code Reviewer** | 採用嚴謹**四階段調試法**（收集證據->模式分析->假設驗證->修復）<br>執行代碼質量審查、測試回歸與 PRD 需求漂移檢測 |
| **部署** | **Release Builder** | 進行軟體編譯、構建、集成與發布 |

---

## 03. 核心運作原則：Harness Engineering 落地

AIPM 框架將 **[[harness-engineering|Harness Engineering]]** 的理念具體化為以下操作規範，藉以在 Vibe Coding 過程中提供堅固的品質安全網：

### 1. 執行層 Subagent 隔離原則
為了保障 AI 代理在複雜跨檔案重構時的記憶純淨度，AIPM 4.0 部署了四大隔離 Subagents（Implementer, Code Reviewer, Feedback Observer, Evolution Runner）：
- **核心約定**：**Subagent 隔離**。每個任務（Task）都必須使用一個全新啟動的實例，**絕對不復用或繼承之前的上下文記憶**。
- **目的**：避免上一個任務產生的錯誤假設、被遺棄的代碼細節污染後續的工程判斷。

### 2. 雙層 Hooks 兜底安全機制
僅靠自然語言指令要求 AI 決定協作時機是不穩定的，AIPM 4.0 引進了系統級的 Hooks 進行硬性限制：
- **Pre-commit Check**：在執行 git commit 前自動觸發編譯檢測，編譯不通過就直接阻止 commit。
- **Stop Gate**：當 Agent 宣告完成並準備停止時，強制攔截並檢查是否存在代碼已修改但未通過 `Code Reviewer` 審查的情況。未經審查禁止結束，保障代碼 100% 被審計。
- **Detect Feedback Signal**：自動捕捉用戶反饋消息中的負面詞，半自動記錄到 `feedback/` 目錄並更新索引，避免反饋流失。

### 3. 自我修正與 4 層進化系統
系統具備自我學習與成長能力，回饋意見會循序升級：
1. **第一層（靜默記錄）**：透過 Feedback Observer 記錄日常意見。
2. **第二層（畢業為規則）**：當同一項回饋意見（如「修改 UI 時必須同步更新設計稿」）在後台**出現 3 次以上**，系統自動提議將其「畢業」寫入對應的 Skill 檔案中成為正式行為約束。
3. **第三層（Skill 優化）**：針對持續低評分的 Skill 提議 Prompt 重構。
4. **第四層（全新 Skill 創生）**：發現無 Skill 覆蓋的重複場景時，自動生成並提議新增全新技能包。

---

## 04. 專案目錄標準結構 (AIPM 4.0)

AIPM 規範了標準的專案骨幹，確保 Agent 能精準加載技能：
- `project/`
    - `Product-Spec.md`（產品需求與 AI 能力定義）
    - `Product-Spec-CHANGELOG.md`（需求變更強制溯源紀錄）
    - `DEV-PLAN.md`（開發計畫排期，解決 session 重啟上下文丟失問題）
    - `.antigravity/` 或 `.claude/`
        - `skills/`（存放 Product Spec Builder, Dev Builder 等 Skills）
        - `feedback/`（存放 Feedback 紀錄與 `feedback-index.md` 索引）

---

## 05. 對 WikiLLM 的影響與應用

這套框架為 WikiLLM 的「文件自動化處理」提供了完美的 SOP。未來我們可以根據此規範，將 Wiki 的更新過程模擬為 PM 模式（定義更新目標，先編排再寫入）與 Dev 模式（執行文件修改與全域雙鏈健檢，Fail Loud 主動揭露錯誤），並透過進化系統讓 Wiki 寫入標準隨著協作次數的增加而自動變強。

---

**關聯文獻**：
- [[aipm-framework-4|Product Manager 4.0 系統架構]]
- [[claude-rules-12-commandments|CLAUDE.md 12條黃金行為指令]]
- [[vibe-coding-paradigm|Vibe Coding 編程範式革命]]
- [[harness-engineering-practice|Harness Engineering 實踐]]
