---
title: "How I Build AI Agent Products in 2025 (Full Workflow)"
type: source
category: AI-Engineering
tags: [Vibe-Coding, Google-AI-Studio, Claude-Code, AI-Agent, Workflow]
date_created: 2026-04-19
source_url: "https://www.youtube.com/watch?v=Phuew4RPwqA"
author: "废才俱乐部Club"
---

# How I Build AI Agent Products in 2025 (Full Workflow)

> 來源目錄：`raw/AI_knowhow/How I Build AI Agent Products in 2025 (Full Workflow).md`

## 摘要與核心啟發

本紀錄完整拆解了利用 AI 開發 Agent 產品的 0 到 1 實踐工作流。透過 **Google AI Studio** 與 **Claude Code** 這對工具組合的配合，搭配自製的 PM 技能包，在不親手撰寫代碼的狀態下完成強大的 TVC 廣告分鏡生成 AI 應用開發。它突顯了 Vibe Coding 時代開發的核心難點已經轉移至需求工程與迭代管理。

## 關鍵知識點提取

### 1. 0 到 1 四大開發環節
1. **需求收集 (Product Spec)**：啟動 Claude Code 裡的 PM 技能，AI 會持續追問極端邊界細節，確認後生成包含 AI 系統提示詞的產品需求文檔。
2. **快速搭建 (AI Studio Builder)**：將需求文檔拋入 Google AI Studio，直接勾選所需能力（如 Nano Banana 生圖、Gemini Intelligence 推理等）並快速搭建初期可運作原型。
3. **下載到本地 (Download Code)**：確認原型可用且代碼無明顯設計錯誤後，將源代碼打包下載並導入本地的 Claude Code 開發環境。
4. **本地迭代 (Local Iteration)**：依靠 Claude Code 繼續添加本地執行需要的配置功能（如 API Key 儲存），持續進入需求→代碼的迭代。

### 2. Vibe Coding 實踐心法
- **維持 PRD 的絕對最新**：需求只要改動，必定先修改產品需求文檔與變更日誌，並且將系統提示詞同步到程式碼配置中。一旦文檔跟不上代碼，AI 很快就會在後續迭代中失效與失控。
- **功能對齊檢查 (Check Alignment)**：由於生成式 AI（特別在 AI Studio 大量生成時）可能只實作部分功能。應設計專屬指令（如 `/check`）對照清單與成果差異，依賴 AI 產生「完整度報告」強迫補齊漏項，而非依賴人工眼球檢查。
- **提示詞即代碼 (Prompt as Logic)**：Agent 產品的業務邏輯核心往往不是程式語言的判斷式，而是系統提示詞（如 `constants.ts` 內定義的對話結構）。AI 的產品呈現、狀態機轉換均依賴這份文本的準確性。
