# Karpathy AutoResearch：極簡 AI 研究自動化迴圈

> **狀態**：已攝入 WikiLLM
> **核心來源**：`raw/AI_knowhow/630 行代碼讓 AI 自己做研究...`
> **關鍵概念**：Frozen Metric, Karpathy Loop, AI Agent Researcher

## 01. 什麼是 AutoResearch？
**AutoResearch** 是由 OpenAI 共同創辦人 Andrej Karpathy 發布的一個 630 行 Python 腳本專案。它展示了如何透過一個極簡的自動化迴圈，讓 AI Agent 在不間斷的實驗中自我優化機器學習模型。

### 核心運作邏輯 (The Karpathy Loop)
1. **讀取與理解**：Agent 閱讀 `train.py` (模型定義與訓練邏輯)。
2. **提出假設**：根據 `program.md` (人類的研究指引) 形成改進點。
3. **實作與提交**：修改代碼並透過 Git 提交到新分支。
4. **受控實驗**：嚴格執行 **5 分鐘** 的訓練。
5. **評估與決策**：檢查預定義的評估指標（如 `val_bpb`）。
   - 若指標提升：保留該改動 (Merge)。
   - 若指標退化：捨棄該分支。
6. **循環往復**：回到步驟 1，一晚可跑約 100 場實驗。

---

## 02. 三大核心設計哲學

### 1. 凍結指標 (Frozen Metric) — 防止作弊
Agent 可以修改 `train.py` 中的任何邏輯，但**絕對禁止修改評估函數**。這確保了 Agent 只能透過真實的技術改進來提升分數，而不能透過修改「考試題目」來作弊。這是解決 AI Alignment 問題的一個微縮原型。

### 2. 固定預算 (Fixed Time Budget)
不論 Agent 如何調整模型規模或架構，訓練時間固定為 5 分鐘。這使得所有實驗在相同的硬體成本下具備直接的可比性。

### 3. 角色重定義：人類作為實驗設計者
人類的工作不再是手動調參，而是撰寫高品質的 `program.md`，即提供「研究方向的指引」。人類從 **實驗執行者 (Experimenter)** 轉變為 **實驗設計者 (Experimental Designer)**。

---

## 03. 實戰成效與影響
- **超越專家**：Agent 在兩天內跑完 650 場實驗，找到的優化結果優於 Karpathy 本人十多年的經驗累積。
- **可轉移性**：在小模型 (Depth 12) 上找到的優化點，可無損轉移至大模型 (Depth 24)。
- **社群震盪**：引發了關於「AI 自我調優 (Self-Tuning)」與「分佈式研究社群 (AgentHub)」的大量討論。

---

## 04. 對 WikiLLM 的啟示
- **SOP 化**：WikiLLM 的知識攝入與文件優化亦可參考此「閉環」邏輯。
- **指標化管理**：在產出內容時（如 SEO 文章），應建立「不可更改的檢核指標」，由 Agent 自我迭代直到達標。
