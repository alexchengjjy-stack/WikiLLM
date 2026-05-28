---
title: "Forge (OpenClaw Framework)"
type: concept
category: AI-Engineering
tags: [Forge, Open-Source, Framework, Agent-Platform]
date_created: 2026-04-19
date_updated: 2026-04-19
source_count: 5
summary: "開源的 Agent 容器底座 Forge，實現四大支柱 (身分、記憶、技能、心跳) 並能與 IM 高度整合。"
---

# Forge (OpenClaw Framework)

> Forge (受 OpenClaw 啟發) 是一個基於開源的 AI Agent 底層框架平台。它不提供寫死的業務功能，而是以容器之姿提供讓一個閒聊大模型擁有「個人執行助理」能力的四個核心支柱與運作機制。

---

## 核心設計四大支柱 (Four Pillars)

將模型轉換為能幹事的助理，Forge 給予了以下四點能力支撐：
1. **身分和規則 (Identity)**：透過注入檔案定義 AI 團隊的角色、溝通規矩。
2. **記憶 (Memory)**：以本地檔案 `MEMORY.md` 堆疊對話日誌的方式，進行進程的持久化，避免對話重置帶來的記憶斷片與上文丟失。
3. **技能 (Skills)**：將所有產品特有功能轉化成一份告知模型如何操作 MCP 等軟體端口的 Markdown `SKILL.md`。
4. **自主性 (Heartbeat/Scheduled Tasks)**：擁有心跳計時器，透過不斷的主動掃描喚醒機制，讓 Agent 能夠不待人類推送，而在特定條件或定時巡檢下自動開始工作。

## 提示詞分層架構 (Prompt Layering)

Forge 處理專案上文的時候，不只是一次性大雜燴。它包含：
- 第一層：基礎 SDK 功能與全局/專屬的 Agent/Skill 特徵檔。
- 第二層：專案客製化的 `SOUL.md`、`IDENTITY.md`、`USER.md`。
- 第三層：動態注入的 `MEMORY.md` (前 200 行 + 近日 Log)。
讓每個對局與專案能自由抽換底下的組合。

## 遠端遙控 (IM Remote Control)
Forge 把 Agent 解放出了電腦開發者終端，整合了如 Feishu (飛書)、Telegram 的即時通訊平台 (IM) 連線 API。這使得它成為真正在背景 24 小時守護的服務基建。
