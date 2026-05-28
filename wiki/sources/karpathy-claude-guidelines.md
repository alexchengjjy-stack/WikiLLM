---
title: "Karpathy 啟發的 Claude 程式碼指南 (CLAUDE.md)"
type: source
source_file: "raw/AI_knowhow/multica-aiandrej-karpathy-skills A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls.md"
date_ingested: 2026-05-26
tags: [ai-pm, vibe-coding, harness-engineering, coding-guideline, karpathy]
author: "multica-ai / Andrej Karpathy"
original_date: "2026-05-26"
language: "繁體中文"
summary: "源自 Andrej Karpathy 對 LLM 編碼陷阱觀察的 CLAUDE.md 指南，提出編碼前三思、簡單至上、手術改變與目標驅動四大原則。"
---

# Karpathy 啟發的 Claude 程式碼指南 (CLAUDE.md)

> 本文摘錄與總結自開源專案 `andrej-karpathy-skills`，該專案旨在解決著名 AI 學者 Andrej Karpathy 所指出的 LLM 編碼四大致命陷阱，並為 `Claude Code` 與 `Cursor` 等編碼代理提供了具體的 `CLAUDE.md` 指南與實踐原則。

## 核心要點

Andrej Karpathy 觀察到當前 LLM 在進行軟體開發時有著以下共通病灶：
- **盲信假設**：默默做出錯誤假設且不加驗證，不尋求澄清或指出不一致處。
- **過度複雜化**：極度喜歡堆砌抽象層與無用代碼，將 100 行能搞定的程式臃腫化為 1000 行。
- **附帶刪改**：因不完全理解而擅自更改/刪除無關的註解與程式碼，造成意料之外的副作用。
- **缺乏明確成功標準**：被動接受指令（命令式），而非設定檢測指標（聲明式）以發揮自主除錯能力。

為此，專案提煉出 **四大黃金原則**，構建了 AI 程式碼編寫的新標準。

---

## 詳細內容

### 原則一：編碼前先思考 (Think Before Coding)
*   **口號**：不要妄下斷言。不要掩飾困惑。坦誠地權衡利弊。
*   **行動指南**：
    *   **明確假設**：如果不確定需求，請向人類詢問澄清，不要盲目猜測。
    *   **列出多種解釋**：存在歧義時，將不同解讀大聲說出來，不要默默替用戶做決定。
    *   **適時提出異議**：若發現更簡單、更直覺的做法，應主動向人類反饋。
    *   **有困惑即停**：遇到程式碼不清楚的地方，立刻暫停並請求解釋。

### 原則二：簡單至上 (Simplicity First)
*   **口號**：用最少的程式碼解決問題。不要進行任何推測。
*   **行動指南**：
    *   **拒絕過度設計**：除了被要求的功能，不自行增添未要求的「配置性」或「擴充性」。
    *   **不為一次性代碼做抽象**：保持程式碼扁平直觀，避免多餘的類或抽象層。
    *   **縮減代碼量**：如果 200 行的代碼可以優化為 50 行，請毫不猶豫地重寫。
    *   **自我測試**：思考「資深工程師會覺得這太複雜嗎？」若是，請立刻簡化。

### 原則三：手術式修改 (Surgical Changes)
*   **口號**：只碰你必須碰的東西。只收拾你自己的爛攤子。
*   **行動指南**：
    *   **正交編輯**：不要擅自「順手改進」與本次任務無關的相鄰代碼、註解或格式。
    *   **保持風格一致**：即使自己有不同的編碼偏好，也必須嚴格遵循現有 codebase 的編寫風格。
    *   **清理自己造成的殘留**：在重構後，必須清除自己本次修改產生的無效 imports、變數與函數。
    *   **保留無關死代碼**：若在 codebase 中發現與任務無關的死代碼，可以指出，但絕不擅自刪除。

### 原則四：目標驅動型執行 (Goal-Driven Execution)
*   **口號**：定義成功標準。循環直至驗證通過。
*   **行動指南**：
    *   **聲明式目標**：不要對 AI 下達命令式的「去新增驗證」或「去修復 Bug」；應下達「編寫針對無效輸入的測試，並循環修改代碼直至測試 100% 通過」。
    *   **驗證循環 (Validation Loops)**：將多步驟任務編制為明確的步驟與 `verify: [check]` 自我驗證循環，讓 AI 系統能獨立完成測試閉環。
    *   **善用 LLM 迴圈優勢**：LLM 雖然不擅長一次性寫出完美代碼，但極其擅長在「擁有明確成功標準（如 Test Suites）」的前提下進行自我修正與循環調試。

---

## 相關連結
- [Vibe Coding 範式](../concepts/vibe-coding-paradigm.md) — 探討如何以人機協同發揮 LLM 之大腦優勢。
- [Harness Engineering 架構設計](../concepts/harness-engineering.md) — 探討如何為 AI Agent 鋪設成功標準的裝配工程。
- [index.md](../index.md) — 知識庫首頁。

## 來源引用
- [andrej-karpathy-skills.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/raw/AI_knowhow/multica-aiandrej-karpathy-skills%20A%20single%20CLAUDE.md%20file%20to%20improve%20Claude%20Code%20behavior,%20derived%20from%20Andrej%20Karpathy%27s%20observations%20on%20LLM%20coding%20pitfalls.md) ── 原始開源專案 clippings。
