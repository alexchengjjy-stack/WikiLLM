---
title: "人類掌舵、Agent 執行：Harness Engineering 的軟體開發新典範"
type: source
source_file: "raw/AI_knowhow/人類掌舵、Agent 執行：Harness Engineering 的軟體開發新典範.md"
date_ingested: 2026-04-28
tags: [Harness-Engineering, AI-Agent, 軟體工程, 範式轉移, OpenAI]
author: "李元魁 (轉載/整理 Ryan Lopopolo 演講)"
original_date: "2026-04-20"
language: "繁體中文"
summary: "OpenAI Frontier Team 成員 Ryan Lopopolo 的演講，主張「禁止工程師手寫代碼」，並提出 Harness 五大支柱：Skills、Docs、Linters、Reviewer Agents 與 Tests。"
---

# 人類掌舵、Agent 執行：Harness Engineering 的軟體開發新典範

> 本文整理自 OpenAI Frontier Team 技術 staff Ryan Lopopolo 在 AIE Europe 的演講，核心主張為「Code is free」。當程式碼生成能力普及，工程師的價值在於建造讓 AI Agent 自主運作的環境（Harness）。

## 核心要點

- **禁止人類寫程式碼**：透過禁止工程師在 IDE 直接編程，強迫團隊轉換思維，學會「用提示詞與 AI Agent 協作」，將精力集中於系統與 Harness 的設計。
- **瓶頸轉移**：軟體工程的瓶頸不再是寫程式碼，而是**人類的時間**、**人類的注意力**（特別是同步代碼審查）以及**上下文窗口限制**。
- **Harness 五大支柱**：
  1. **Skills**：封裝底層工具複雜度，作為人類與 AI Agent 的統一操作介面。
  2. **Documentation**：角色導向的知識沉澱，為 AI 提供具體的非功能性需求標準。
  3. **Linters**：將工程紀律寫入系統，自動化修正不符合標準的程式碼。
  4. **Reviewer Agents**：取代人類的同步代碼審查，實現非同步、全自動化的 P0/P2 關卡檢查。
  5. **Tests**：不僅測試行為，更測試「程式碼結構」，以確保 codebase 的一致性，進而優化 Token 消耗。
- **CI 的價值**：CI 流程消耗了約 1/3 的 Token，但這是對「人類稀缺注意力」的有效置換。

## 詳細內容與洞察

### Reviewer Agents 與自動化閉環
團隊利用專屬的 Reviewer Agents（如安全性、可靠性、效能等）對 PR 進行非同步審查。每週五設立 "Garbage Collection Day"，將失敗或劣質的程式碼轉換為 Linter 或 Reviewer Agent 的新規則，形成持續改進的閉環。

### 模糊編譯器 (Fuzzy Compiler) 的隱喻
Ryan 將 Codex 等 LLM 視為模糊編譯器，生成的程式碼只是「可拋棄的建構產物」。Harness 系統中的規則與限制，就像是傳統編譯器中的靜態分析，決定了產出是否有效。這意味著底層模型可以隨時替換，只要 Harness 系統夠嚴謹。

### 擴展與架構策略
在管理包含 750 個 Packages 的 Monorepo 時，團隊堅持：
1. 每一個商業領域為一個子樹，減少合併衝突。
2. 保持程式碼極度一致，因為一致的文字能降低 Token 消耗。
3. 縮短 PR 開放時間，提升系統吞吐量。

### Plan Mode 的局限性
Ryan 認為如果 Harness 設計得當，就不需要讓 AI 進入 Plan Mode 進行規劃；若必須使用，則應將 Plan 當作 PR 來進行人類審查，以免浪費注意力在無法執行的指令上。

## 相關連結
- [Harness Engineering (主題)](../topics/harness-engineering.md)
