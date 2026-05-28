---
title: "毒舌产品经理 3.0"
type: source
category: AI-Engineering
tags: [Product-Manager-3.0, AI-Agent, Claude-Code, Develop-Pipeline]
date_created: 2026-04-19
source_url: "https://feicaiclub.feishu.cn/wiki/VXxKw0LToiJJn7kxFNDc3q7tnJg"
author: "废才俱乐部Club"
---

# 毒舌产品经理 3.0

> 來源目錄：`raw/AI_knowhow/毒舌产品经理 3.0  - 飛書雲端文件.md`

## 摘要與核心啟發

這篇文件介紹了「毒舌產品經理 3.0」的 AI 開發流程，主要透過主控 (`CLAUDE.md`) 搭配三個專工 Skill（毒舌產品經理、UI提示詞設計師、全棧開發工程師）來實現從想法到可運行項目的自動化。強調了在沒有設計稿與完整文件前，絕對不要讓 AI 自由發揮寫代碼的重要性。

## 關鍵知識點提取

### 1. 三項核心技能 (Skills) 工作流
- **毒舌產品經理**：負責需求收集。會毫不客氣地挑出邏輯矛盾，潑冷水，並主動詢問「此處是否需要 AI 增強？」。負責產出 `Product-Spec.md` 與 `CHANGELOG.md`。
- **UI 提示詞設計師**：負責省去繁雜設計溝通。能根據前者生成的需求，制定出一套完整的 UI 提示詞（`UI-Prompts.md`），後續可直接丟交給 Midjourney 完成原型圖。
- **全棧開發工程師**：讀取需求與原型圖，進行項目結構創建與代碼實現。支持本地運行測試並自動比對功能缺漏。

### 2. 開發的閉環模式
- **主控調度層**：依靠根目錄的 `CLAUDE.md` 來進行工作流與技能間的跳轉與銜接，使得使用者只需透過 `/prd`、`/ui`、`/dev` 即可引導進程。
- **0-1 模式與迭代模式的自動切換**：啟動時自動檢查專案中是否有 Product Spec，有則進入迭代追加模式，沒有則進入 0-1 原始草創模式，並自動進行衝突檢查。
- **文檔與代碼強同步**：修改或增加功能，強制「先叫 PM 更新文檔，再叫 Dev 去寫代碼」。
