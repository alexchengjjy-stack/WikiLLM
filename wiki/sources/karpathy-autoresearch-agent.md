---
title: "Karpathy AutoResearch：AI Agent 的自動化研究實驗迴圈"
type: source
source_file: "raw/AI_knowhow/630 行代碼讓 AI 自己做研究*.md 等4份文件"
date_ingested: 2026-05-18
tags: [AI 工程化, AI Agent, AutoResearch, Vibe Coding, Karpathy, 分散式協作]
author: "Antigravity (LLM)"
summary: "Andrej Karpathy 開源的 AutoResearch 專案解析，展示如何透過 630 行代碼建立一個 Frozen Metric 的 AI 研究迴圈，讓 Agent 自動化進行 ML 實驗。"
---

# Karpathy AutoResearch：極簡 AI 研究自動化迴圈

> 本文件彙整自 2026 年 3 月 Andrej Karpathy 發布的 `autoresearch` 開源專案相關探討，包含技術架構解析、社群反應與分散式協作願景。這項專案以短短的 630 行代碼，在兩天內引發了 AI 圈巨大的迴響。

## 核心概念：AI 實驗自動化

AutoResearch 的核心是一個極簡的自動化迴圈（Karpathy Loop），旨在讓 AI Agent 自行修改機器學習的訓練腳本（如 `train.py`），執行實驗並評估結果。

其運作流程如下：
1. **理解現狀**：Agent 讀取 `train.py`（包含模型架構與超參數）。
2. **提出假設**：根據人類撰寫的 `program.md`（研究方向指引），形成修改假設。
3. **修改代碼**：直接編輯 `train.py`，並 commit 到 feature branch。
4. **執行訓練**：嚴格執行 **5 分鐘固定時間** 的訓練。
5. **評估結果**：檢查驗證指標（如 `val_bpb`）是否改善，若變好則保留 commit，否則捨棄。
6. **循環迭代**：不斷重複上述過程（每小時約可執行 12 個實驗）。

## 核心設計哲學：Frozen Metric 與 Fixed Budget

這項專案能超越人類專家（Karpathy 本人）的手動調校，歸功於兩個精妙的設計決策：

### 1. 凍結指標 (Frozen Metric)
**這是 AutoResearch 避免 AI 產生幻覺或「作弊」的關鍵防線。**
- Agent 可以修改模型結構、優化器（如 Muon + AdamW）或訓練迴圈的任何邏輯，但**絕對無法修改評估標準 `val_bpb`**。
- 這體現了 AI Alignment 的縮影：**如果 Agent 能同時修改考卷與答案，它永遠能考滿分。** Karpathy 建立了一個外部標準，將評估權限鎖死，迫使 Agent 只能透過真實的性能提升來獲得認可。

### 2. 固定時間預算 (Fixed Budget)
- 無論模型變得多龐大或參數多複雜，訓練時間永遠固定為 5 分鐘。
- 這種設計讓所有實驗的結果能夠直接進行對比，促使 Agent 自動尋找「在特定硬體下，5 分鐘內能訓練出的最優模型」。
- 缺點是跨硬體的結果無法直接比較。

## 人類角色的轉變：從「實驗者」到「實驗設計者」

AutoResearch 揭示了 AI 工程化（Harness Engineering / Vibe Coding）的進一步演化：
研究人員的工作不再是緊盯 Loss 曲線並手動調參（實驗者），而是轉變為撰寫優質的 `program.md`，用自然語言提供方向與邊界（實驗設計者）。

> *"The role of the human shifts from 'experimenter' to 'experimental designer.'"* — VentureBeat

## 下一步願景：SETI@home 模式的分散式 Agent 協作

Karpathy 對此專案的願景並非僅是「取代單一博士生的工作」，而是**模擬整個博士研究社群**。

- **分散式大規模協作**：未來期望全球的 Agent 在各自的 GPU 上運行 AutoResearch，並將結果匯聚（類似 SETI@home）。
- **社群響應**：開源不到一週，已出現 `autoresearch-at-home` 等 Fork，甚至有 Hyperspace AI 將其搬上 P2P 網路，或嘗試使用本地端 LLM 來降低 API 成本（與 Claude Code + Ollama 本地部署的概念不謀而合）。
- **技術挑戰**：如何解決不同硬體算力（如 H100 與 RTX 4090）在「固定 5 分鐘」下跑出的結果難以跨裝置匯聚比較的問題，是分散式協作目前面臨的挑戰。

---

## 關聯資源與工具清單

- **官方 Repo**: `https://github.com/karpathy/autoresearch`
- **社群延伸**: `olelehmann1337/autoresearch-skill`（提供 Agent Skill 包）
- **關聯概念**:
  - [[vibe-coding-paradigm|Vibe Coding 範式]]
  - [[he-architecture-overview|Harness Engineering]]
