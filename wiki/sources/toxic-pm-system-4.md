---
title: "毒舌产品经理 4.0 - Harness Engineering 實踐"
type: source
category: AI-Engineering
tags: [Product-Manager-4.0, Harness-Engineering, AI-Agent, Context-Firewall, Steering-Loop]
date_created: 2026-04-19
source_url: "https://feicaiclub.feishu.cn/wiki/GsOKwveahi6x4ekYN9VcWcSpnry"
author: "废才俱乐部Club"
---

# 毒舌产品经理 4.0 - Harness Engineering 實踐

> 來源目錄：`raw/AI_knowhow/毒舌产品经理 4.0 - 飛書雲端文件.md`

## 摘要與核心啟發

本文檔為毒舌產品經理系列演進到 4.0 的系統架構。其不僅涵蓋 Vibe Coding 的技能組合，更是將 **Harness Engineering (駕馭工程)** 的理論徹底落地。透過 Guides (前饋控制)、Sensors (反饋防護)、Context Firewall (上下文隔離) 與 Steering Loop (進化方向盤) 將大語言模型從一個寫碼工具轉化為一個被保護在嚴密護城河內、且能在高吞吐量下穩定工作的軟體工廠。

## 關鍵知識點提取：Harness Engineering 落地四象限

### 1. Guides (前饋控制)：8 個行動前注入的 Skill
- Harness 的前饋控制代表「在 Agent 行動前將方法論注入以提高一次做對的機率」。
- **包含**：`product-spec-builder`、`design-brief-builder`、`design-maker`、`dev-planner`、`dev-builder`、`bug-fixer`、`code-review`、`release-builder`。
- **設計圖最高權威**：UI 變更檢查清單必經：更新 Spec → 更新設計稿 → 開發，若衝突皆以設計稿 (Figma/Pencil MCP) 為準。

### 2. Context Firewall (隔離代理)：4 個無上文污染的 Sub-Agents
- **運作核心**：每個 Task 都派出全新的實例，絕不復用舊有記憶。只夾帶完整的「需求與規範」，而切斷歷史執行盲點。
- **配置**：`implementer` (編碼自檢), `code-reviewer` (兩階段審查), `feedback-observer` (捕捉回饋), `evolution-runner` (生成建議)。

### 3. Sensors (反饋控制)：Hook 腳本與兩階段 Review
- Harness 強調雙層防護。不只依賴模型自然語言推理，更依賴硬體級別的「確定性阻斷 (Hooks)」。
- **推理性 Sensor (非確定性但語意清晰)**：如 `code-review` 包含 Stage 1 查合規完整性、Stage 2 查代碼質量。
- **計算型 Sensor (確定性 Hooks)**：
  - `pre-commit-check`：無法通過編譯不准 commit。
  - `stop-gate`：防呆。代碼未審查不許收工停止。
  - `detect-feedback-signal`：自動捕捉用戶不滿的糾正信號。
  - `mark-review-needed`：一有代碼變更便加上待審查標籤。

### 4. Steering Loop (進化方向盤)：四層進化路徑
- 將一次性的 Prompt 方案升級為會演變的系統。所有的修正不會只改代碼，而是修改 Harness。
- **四層機制**：
  1. 靜默記錄抱怨到 Feedback 文件。
  2. 抱怨滿三次則「畢業」，進化至特定 Skill 中成為永久防護。
  3. 當特定 Skill 給分持續低迷，建議優化該 Skill。
  4. 反覆發生且沒有合適 Skill 的情境，系統提議創建新的專職 Skill。
