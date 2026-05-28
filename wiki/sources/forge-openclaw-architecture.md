---
title: "Open Source! I Built My Own OpenClaw — It's Called Forge"
type: source
category: AI-Engineering
tags: [Forge, OpenClaw, AI-Agent, Harness-Engineering, Open-Source]
date_created: 2026-04-19
source_url: "https://www.youtube.com/watch?v=-bZSNRFh8NM"
author: "废才俱乐部Club"
---

# Open Source! I Built My Own OpenClaw — It's Called Forge

> 來源目錄：`raw/AI_knowhow/Open Source! I Built My Own OpenClaw — It's Called Forge.md`

## 摘要與核心啟發

這篇記錄了作者開發開源 Agent 產品 "Forge" (受 OpenClaw 啟發) 的過程及核心設計原理。它揭示了要把純粹聊天的「模型」轉換為能自主執行任務的「Agent」，必須建構包覆在模型外的四個支柱：身分 (Identity)、記憶 (Memory)、技能 (Skills)、自主性 (Autonomy)。Forge 展示了從 CLI 操作到依賴通訊軟體 (如飛書 IM) 遠端操控 Agent 的基礎架構。

## 關鍵知識點提取

### 1. Agent 核心四大支柱
1. **身分和規則 (Identity)**：透過文件定義模型角色與邊界，不再局限於原廠的預設對話模型。
2. **記憶 (Memory)**：由本地持久化文檔保持上下文連貫，避免 Token 歸零帶來的失憶症。
3. **技能 (Skill = Feature)**：提供工具。Skill 本質為 Markdown 檔案，告知模型於何時、以何種步驟使用特定工具，替代了傳統由軟體工程師寫死的介面功能操作。
4. **自主性 (Autonomy)**：導入 **Heartbeat (心跳機制)** 或稱為 Scheduled Tasks。讓 Agent 擁有定時喚醒、主動掃瞄現況、有事通知/無事靜默的能力，使其成為真正的「助理」而非被動的「客服」。

### 2. Prompt 分層架構 (Prompt Layering)
為了讓 Agent 靈活載入配置，Prompt 被設計為動態堆疊：
- **第一層 (SDK 處理)**：注入 `CLAUDE.md`，自動掛載關聯的 Skills 與 Sub-Agents，以及基礎工具。
- **第二層 (專案補充)**：由 Forge 獨有補充 `SOUL.md`、`IDENTITY.md`、`USER.md`，豐富人格。
- **第三層 (記憶堆疊)**：`MEMORY.md` 加上最近兩天的對話日誌。

### 3. 未來三大趨勢預測
1. **Feature is Skill, Skill is Feature**：擴充軟體不再仰賴 Code 撰寫新增功能，使用者只需提供描述操作邏輯的 Markdown (Skill)，即可用語言解鎖專屬功能。
2. **方案級編排 (Marketplace for Orchestration)**：單純的代理商與大模型價值遞減，能預存多智能體、多技能複合的「工作流編排方案」才是未來有價值的軟體封裝資產。
3. **基礎設施化 (Infrastructure)**：Agent 不再是「用完即關」的工具，而是 24 小時守護、掛載於飛書/Telegram 等 IM 的背景服務代理。
