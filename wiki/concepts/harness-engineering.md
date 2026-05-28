---
title: "Harness Engineering（駕馭工程）"
type: concept
category: AI-Engineering
tags: [Harness-Engineering, AI-Agent, 軟體工程]
date_created: 2026-04-18
date_updated: 2026-04-18
source_count: 6
summary: "圍繞 AI Agent 建構約束機制、回饋迴路和執行基礎設施的系統工程學科"
---

# Harness Engineering（駕馭工程）

> Harness Engineering 是指在 agent-first 軟體開發中，建構一套控制與放大 agent 交付能力的工程學。「Harness」一詞來自馬術——韁繩、馬鞍、轡頭的總稱，不改變馬的能力，但決定牠能往哪走、走多快、出問題怎麼拉回來。

---

## 定義

**正式定義**（Wisely Chen）：在 agent-first 軟體開發中，建構一套控制與放大 agent 交付能力的工程學。它回答的不是「agent 能不能寫出某段 code」，而是「在大量 PR、高吞吐與長時間自主執行下，如何確保一致性、可維護性、安全性與可觀測性」。

**OS 比喻**（Jason Chuang）：LLM 是 CPU，Context Window 是 RAM，Harness 是作業系統——管理資源、排程任務、協調元件。

## 與相關概念的關係

```
Harness Engineering（系統層）
    └── Context Engineering（信息層）
            └── Prompt Engineering（訊息層）
```

| 概念 | 層次 | 核心問題 | 持久性 |
|------|------|---------|--------|
| Prompt Engineering | 對話層 | 怎麼說 | 每次對話重來 |
| Context Engineering | 信息層 | 模型看什麼 | 會話內有效 |
| **Harness Engineering** | **系統層** | **建什麼系統** | **沉澱在 repo，越用越好** |

## 起源

- **2025 年底**：零星提及
- **2026 年 2 月**：Mitchell Hashimoto 在博客中首次明確命名
- **2026 年 2 月**：OpenAI 發布百萬行代碼實驗報告
- **2026 年 2 月**：Martin Fowler 發表深度分析
- **2026 年 3-4 月**：快速席捲整個軟體工程界

## 核心哲學

> **Humans steer. Agents execute.** — OpenAI

不是「人類禁止 Agent」，也不是「Agent 自由奔跑」。是**人類建好框架，Agent 在框架裡全速運轉**。

## 實務控制三要素 (Guides, Sensors, Steering Loop)

根據 PM 4.0 中的 Harness Engineering 實踐，完善的駕馭系統需要具備三大控制組件：

1. **Guides (前饋控制)**：在 Agent 行動前，透過專門的 `Skills` 將方法論與步驟標準化注入系統（例如先行建立 `design-brief`，使得後續的建立不再偏離軌道），提高**一次做對**的機率。
2. **Sensors (反饋控制 / Hooks)**：
   * **確定性控制 (Hook Scripts)**：代碼行為觸發的反饋，不依賴模型判斷的硬性關卡（例如 \`pre-commit-check\` 若編譯失敗則鎖死提交，或 \`stop-gate\` 強制卡控要求先執行 Code Review）。
   * **推理型控制 (Agent Review)**：將非確定性的檢驗委託給專門的 Reviewer Agent，從語意與商業邏輯判斷（Spec 合規性與代碼質量）做防守。
3. **Steering Loop (迭代方向盤 / Evolution)**：Harness 需要具備學習能力。透過在背景靜默紀錄的 `feedback-observer` 收錄修正反饋，當特定修正需求累積到一定次數後，驅動系統將臨時提示「畢業」為真正的常駐規則，使基礎設施越用越好。

## 核心防護實踐 (Harness Controls)

Harness Engineering 的具體落地方案通常圍繞在對於大語言模型的多重防護網上，將其分為三大類來包圍 AI Agent 的不確定性：

1. **Guides (前饋控制)**：
   在 Agent 行動之前就注入標準和方法論，以提高模型一次做對的機率。
   - 例如：特製的 Skill 手冊（設定好開發前必須先跑 `product-spec-builder` 進行嚴格追問，以建立 Spec，而非讓 AI 直接跳去寫代碼）。

2. **Sensors (反饋控制)**：
   在 Agent 行動之後進行預期對齊，能在發現偏差時立即觸發修正。可用機制分兩種：
   - **推理性 Sensor (非確定性但語意精準)**：派遣對立的 AI 對開發中的產物進行兩階段 Review 審改。
   - **計算型 Sensor (確定性的 Hook 腳本防呆)**：例如 `pre-commit-check` (編譯不過就卡住不准提交)、`stop-gate` (沒跑過 Review 前不准 AI 宣佈停工)。

3. **Steering Loop (迭代方向盤)**：
   Harness 不只是擋死板的限制，也是一個進化的框架。每一次在進行 Vibe Coding 所遇到的除錯、使用者的抱怨與回饋，都必須納入經驗池。例如，當特定的用戶修正滿三次，即自動畢業轉化為寫死在 Config 裡的永久防護準則。保證**系統不再犯第二次錯**。

## 詳細探討

→ 詳見主題頁：[Harness Engineering](../topics/harness-engineering.md)

## 相關連結
- [AGENTS.md 標準](./agents-md.md)（概念）
- [Harness Engineering 主題頁](../topics/harness-engineering.md)（主題）
