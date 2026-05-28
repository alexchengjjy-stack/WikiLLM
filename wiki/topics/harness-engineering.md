---
title: "Harness Engineering"
type: topic
category: AI-Engineering
tags: [Harness-Engineering, AI-Agent, 軟體工程, 範式轉移]
date_created: 2026-04-18
date_updated: 2026-04-18
source_count: 9
sources: ["he-third-dimension.md", "he-complete-analysis.md", "he-architecture-overview.md", "he-deep-analysis.md", "he-ai-os-architecture.md", "he-learning-guide.md", "aipm-antigravity.md", "aipm-project-structure.md", "he-human-steer-agent-execute.md"]
summary: "2026 年最重要的 AI 工程新學科——圍繞 AI Agent 建構約束機制、回饋迴路和執行基礎設施的系統工程實踐"
---

# Harness Engineering

> **Harness Engineering（駕馭工程）** 是 2026 年興起的 AI 工程學科，核心理念是：圍繞 AI Agent 建構一套控制與放大其交付能力的系統工程實踐。它不改變模型的能力，而是建立讓模型能在真實世界中安全、可控、可靠地行動的執行環境。

---

## 一句話理解

> 模型是馬，Harness 是讓牠能被安全騎乘的整套裝備。 —— 溫煜鈞

```
傳統工程：人類寫代碼 → 機器執行
Harness Engineering：人類設計約束 → Agent 寫代碼 → 機器執行
```

**核心轉變：工程師的產出從代碼變成了約束系統。**

---

## 為什麼需要 Harness Engineering

### 模型能力不是瓶頸

多個獨立實驗證實：

| 實驗 | 結果 |
|------|------|
| Can.ac | 僅改 Harness 工具格式 → Grok Code Fast 1 從 6.7% 躍升至 **68.3%** |
| LangChain | 同一模型靠 Harness 改進 → Terminal Bench 2.0 從第 30 名跳到**第 5 名** |
| OpenAI Codex | 3 人 5 個月 100 萬行代碼、零手寫 |
| Manus | 同一模型重寫 5 次 Harness，每次提升都比換模型大 |

> **「Five independent teams. Same conclusion: the bottleneck is infrastructure, not intelligence.」** — Alex Lavaee

### AI 的行為模式問題

AI 面對複雜問題會本能地選擇「最乾淨的解法」，但對生產系統可能是災難：

| 事件 | AI 的「解法」 | 後果 |
|------|-------------|------|
| DataTalks.Club | 刪掉資料庫 | 資料永久丟失 |
| AWS 生產環境 | 刪掉整個環境重建 | 13 小時中斷 |
| 亞馬遜電商 | AI 變更導致 outage | 數百萬筆訂單丟失 |

---

## 三代範式演進

| 世代 | 時期 | 核心問題 | 比喻 | 局限 |
|------|------|---------|------|------|
| Prompt Engineering | 2022-2024 | 怎麼**說** | 寫一封完美的信 | 無法處理多步驟、缺乏記憶 |
| Context Engineering | 2025 | 模型**看到**什麼 | 附上所有相關附件 | 只管單一 Agent 的視角 |
| **[Harness Engineering](../concepts/harness-engineering.md)** | **2026** | **建什麼系統** | **設計整個郵務系統** | **仍在發展中** |

三者是嵌套關係：`Harness ⊃ Context ⊃ Prompt`。Prompt Engineering 沒有死——它被升職了，成為更大系統的子模組。

---

## 核心技術框架

### Guides × Sensors 矩陣（Birgitta Böckeler / Martin Fowler）

|  | Computational（確定性） | Inferential（推理性） |
|---|---|---|
| **Guide（前饋）** | LSP、型別系統、架構文檔 | [AGENTS.md](../concepts/agents-md.md)、AI 規劃、Skills |
| **Sensor（回饋）** | ESLint、semgrep、coverage | AI Code Review |

- **Guides** 在 Agent 行動**之前**介入（前饋控制）
- **Sensors** 在 Agent 行動**之後**介入（回饋控制）
- **成熟的 Harness 需要四個象限都有覆蓋**

### Harness 五維度（溫煜鈞）

| 維度 | 職責 |
|------|------|
| 資源管理 | Token 預算、成本控制、熔斷機制 |
| 狀態持久化 | Memory 系統 |
| 信息流控制 | Context 壓縮、決定模型看到什麼 |
| 安全邊界 | 工具權限、行為約束 |
| 任務編排 | Multi-agent 協調 |

### 四大支柱（知乎 Meta 交叉分析）

| 支柱 | 核心原則 |
|------|---------|
| 上下文架構 | 恰好提供所需上下文——不多不少（~40% 甜蜜區間） |
| Agent 專業化 | 專注特定領域的受限 Agent > 全權限通用 Agent |
| 持久化記憶 | 進度存在檔案系統，非上下文窗口 |
| 結構化執行 | 理解 → 規劃 → 執行 → 驗證 |

### Harness 五大支柱（Ryan Lopopolo / OpenAI）

| 支柱 | 核心職責 |
|------|---------|
| **Skills** | 封裝工具複雜度，作為 AI Agent 執行的標準化介面 |
| **Documentation** | 角色導向的知識沉澱，定義 AI 可執行的非功能性標準 |
| **Linters** | 將工程紀律寫入系統，透過 CI 自動化修正程式碼 |
| **Reviewer Agents** | 專職化 AI 審查（安全性、效能等），取代人類同步 Code Review |
| **Tests** | 測試「程式碼結構」與一致性，優化 Token 消耗與壓縮率 |

### 七元件參考架構（Wisely Chen）

1. Context System → 2. Architecture Guardrails → 3. Eval & Test → 4. CI/PR Automation → 5. Safety & Policy → 6. Observability → 7. Feedback Loops

### 三層防禦（Wisely Chen）

1. **分級審查**：根據爆炸半徑決定審查強度（Risk Tiering）
2. **四層防禦**：Test → Lint → CI Gate → LLM Judge
3. **控制平面**：PR 生命週期八步閉環

---

## 業界實戰案例

| 企業 | 規模 | 核心做法 | 關鍵洞察 |
|------|------|---------|---------|
| **OpenAI Frontier** | 日耗 10 億 Tokens | 禁止人類寫代碼；全自動 Reviewer Agents | Code is free；Harness 五大支柱；模糊編譯器隱喻 |
| **OpenAI Codex** | 3人/5月/100萬行 | Linter 錯誤訊息內嵌修復指令；GC Agent | 設計環境而非寫代碼 |
| **Anthropic** | 16 Agent / C 編譯器 | Planner-Generator-Evaluator | 模型無法可靠評估自身 |
| **Stripe Minions** | 每週千級 PR | Toolshed MCP + 預熱 Devbox | 明確退出條件 |
| **Datadog** | 可觀測性閉環 | Production telemetry 回饋修正 Harness | 沒有可觀測性，迴路不閉合 |
| **Manus** | 5 次重寫 | 每次都簡化 | 護城河在 Harness 不在模型 |
| **Hashimoto (Ghostty)** | AGENTS.md 實踐 | 每一行對應一個歷史失敗 | 每天最後 30 分鐘啟動 Agent |
| **Antigravity AIPM** | 角色與目錄解耦 | 透過 `/pm` 等指令切換技能包 (`SKILL.md`) | 用目錄與模板實現前饋約束 |

---

## 六大業界共識（跨 8 個獨立來源）

1. ⭐⭐⭐⭐⭐ **瓶頸在基礎設施，不在模型智能**
2. ⭐⭐⭐⭐⭐ **思考與執行必須分離**
3. ⭐⭐⭐⭐ 文檔必須是**活的回饋循環**
4. ⭐⭐⭐⭐ 上下文**不是越多越好**（~40% 甜蜜區間）
5. ⭐⭐⭐⭐ 約束必須**機械化執行**
6. ⭐⭐⭐⭐ 工程師角色從「寫代碼」轉向「設計環境 + 管理工作」

## 四大分歧

1. Harness 應越做越複雜還是越做越簡單？
2. 單 Agent 還是多 Agent？
3. 人類應介入到什麼程度？
4. 術語邊界怎麼畫？

## 三大空白

1. **棕地專案**改造方法論（零成功案例）
2. **功能行為驗證**的系統化方案
3. AI 生成代碼的**長期可維護性**

---

## 工程師角色轉變

### 從 in the loop 到 on the loop

- **in the loop**：AI 寫一段、人看一段（傳統）
- **on the loop**：人在迴圈**上方**設計規則、監控品質（Harness）

### 規劃是新的編碼

> 「永遠不要讓 Agent 在你審查和批准書面計劃之前寫代碼。」 — Boris Tane, Cloudflare

### 兩種並行管理模式

| 模式 | 描述 | 前提 |
|------|------|------|
| 有人值守 | 主動監管多個 Agent | Harness 不需很成熟 |
| 無人值守 | 發布任務後離開 | Harness 必須足夠成熟 |

---

## Harness 成熟度模型

| Level | 特徵 | 工程師角色 |
|-------|------|-----------|
| 0 | 無 Harness | 手動寫代碼 |
| 1 | AGENTS.md + 基礎 Linter | AI 輔助 |
| 2 | CI/CD + 自動測試 + 進度追蹤 | 規劃審查為主 |
| 3 | 多 Agent 分工 + 分層上下文 + 持久化記憶 | 環境設計為主 |
| 4 | 無人值守並行 + 自動熵管理 + 自我修復 | 架構師 + 品質把關 |

---

## 五大失效模式

1. **上下文腐壞** — AGENTS.md 與 repo 脫節
2. **架構漂移** — Agent 忠實複製壞模式（10 倍速）
3. **測試 Flake** — 無限阻塞或放行不該放的代碼
4. **安全外溢** — Prompt injection、權限過大
5. **供應鏈崩壞** — Agent 更頻繁新增依賴

---

## 趨勢展望

1. **Harness 成為真正的技術護城河**（模型提供商已承認）
2. **AGENTS.md 走向標準化**（跨工具）
3. **Harness 自身也被 AI 優化**（如 AutoAgent）
4. **越做越薄，而不是越做越複雜**
5. **更強的模型讓 Harness 更重要**，不是更不重要

---

## 相關連結

### 概念
- [Harness Engineering 概念](../concepts/harness-engineering.md)
- [AGENTS.md 標準](../concepts/agents-md.md)

### 來源（8 份）
- [AI 工程師的第三個維度](../sources/he-third-dimension.md) — 溫煜鈞
- [完全解析](../sources/he-complete-analysis.md) — BASHCAT/HackMD
- [架構全景](../sources/he-architecture-overview.md) — Wisely Chen
- [深度解析](../sources/he-deep-analysis.md) — Meta/知乎
- [AI 作業系統架構](../sources/he-ai-os-architecture.md) — Jason Chuang
- [學習指南](../sources/he-learning-guide.md) — deusyu/GitHub
- [ANTIGRAVITY Agent 主控規範](../analyses/antigravity-aipm-framework.md) — Antigravity IDE
- [AI 專案目錄結構設計 (AIPM)](../analyses/antigravity-aipm-framework.md) — Antigravity IDE
- [人類掌舵、Agent 執行](../sources/he-human-steer-agent-execute.md) — 李元魁 (轉載 Ryan Lopopolo)
