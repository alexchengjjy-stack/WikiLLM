---
title: Claude Code 與 Ollama 本地部署整合指南
description: 探討如何透過 CC Switch 將 Claude Code 介接至本地 Ollama 模型，實現低成本、私有化的 AI 編程 Agent 工作流。
date: 2026-05-18
tags:
  - AI
  - Agent
  - Claude Code
  - Ollama
  - 本地部署
  - 開發工具
---

# Claude Code 與 Ollama 本地部署整合指南

此文件整理自 [KnightLi 的教學文章](https://www.knightli.com/zh-tw/2026/05/15/claude-code-ollama-cc-switch-local-agent/)，主要探討如何保留 Claude Code 的 Agent 操作體驗，同時透過將推理請求轉發至本地模型以降低 API 成本與提高資料隱私。

## 1. 核心架構原理

Claude Code 擁有強大的 Agent 工作流（能自主讀取專案、修改檔案、執行命令與修復錯誤），但多輪操作在長上下文中極易消耗大量 API 額度。本方案的解決架構如下：

- **Claude Code 桌面端**：負責編程工作流、指令下達與專案操作。
- **CC Switch API 轉發層**：負責模型供應商配置與 OpenAI API 格式相容轉換。
- **Ollama 本地模型**：負責在本地機器上執行大語言模型（如 Qwen Coder, DeepSeek Coder 等）。

## 2. 關鍵配置與連線設定

在 CC Switch 端的設定要點：

- **供應商類型**：選擇 `OpenAI Chat Completions`
- **Base URL**：指向本地 Ollama 的 API 位址，預設為 `http://127.0.0.1:11434/v1`
- **API Key**：可使用任意佔位符（如 `ANTHROPIC_API_KEY`）
- **模型映射 (Critical)**：必須設定 `"inferenceModels"="[\"haiku\",\"sonnet\",\"opus\"]"`，將 Claude Code 預期的這三種模型角色映射至 Ollama 中實際可用的本地模型名稱，否則將導致呼叫失敗。

## 3. 本地部署的優勢與邊界

### 優勢
1. **零 API 成本**：所有請求皆在本機處理。
2. **高隱私與離線可用**：私有程式碼不需上傳雲端，且無網路環境亦可運作。
3. **保留 Agent 體驗**：維持了 Claude Code 在專案中自主尋找檔案、下指令並反覆修正的工作流，優於單純的聊天對話框。

### 侷限與風險
此方案不能完全取代雲端強大模型，其主要邊界與痛點包含：
- **長上下文理解較弱**：容易在大型專案或多輪對話中遺失關鍵細節。
- **工具呼叫 (Tool Calling) 穩定性低**：部分本地模型可能會產生幻覺，虛構不存在的檔案路徑或 API。
- **多模態相容性差**：處理截圖、UI 圖片等視覺能力尚未穩定，取決於 CC Switch 的轉換及本地模型的視覺能力。
- **硬體門檻**：純 CPU 機器推理極慢，需仰賴一定程度的 GPU 效能。

## 4. 最佳實踐建議

強烈建議將本地部署的 Claude Code 定位為**輔助工具**而非全自動工程師。

- **適用場景**：解釋單一檔案、重構小函式、生成 Shell 腳本、修復簡單 Bug 或補充單元測試。
- **避免使用**：跨檔案的大型重構、Monorepo 的架構判斷。
- **核心原則**：縮小每次下達任務的範圍（例如：「重構這個函式」而非「重構整個專案」），且所有的修改都必須手動檢查 diff 並執行測試後再採用。
