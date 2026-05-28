---
title: "0代码，如何用Gemini 3.0开发AI产品"
type: source
category: AI-Engineering
tags: [Zero-Code, Gemini-3.0, AI-Studio-Builder, Product-Manager-Skill, Vibe-Coding]
date_created: 2026-04-19
source_url: "https://feicaiclub.feishu.cn/wiki/QaRMw4aOSib9AKkdDtWcMVkEnac"
author: "废才俱乐部Club"
---

# 0代码，如何用Gemini 3.0开发AI产品

> 來源目錄：`raw/AI_knowhow/0代码，如何用Gemini 3.0开发AI产品 - 飛書雲端文件.md`

## 摘要與核心啟發

本文紀錄了使用 Google AI Studio Builder 搭配 Gemini 3.0 Pro 的前沿零代碼開發方式。最大的開發卡點已不再是寫程式，而是「如何寫出完整的 Product Spec」。本方案透過設定嚴厲且主動挑戰盲點的 Claude PM Skill，幫缺乏產品經驗的生手把模糊的想法逼問成可落地的文檔。

## 關鍵知識點提取

### 1. PM 技能的人格模型與策略
- **人格模型 (Personality)**：與一般唯命是從的 AI 不同，此 PM Skill 設定為直白、不客套、專戳漏洞。它會主動挑戰用戶的不合理設計，逼迫用戶思考細節。
- **AI 優先原則**：每當用戶提出需求，AI 產品經理首先思考「這是否能利用 AI 自動完成或簡化？」，確保充分發揮模型能力而非只是在傳統工具硬塞 AI。
- **分層需求收集**：將需求拆解為必須收集（產品定位、核心功能）、盡量收集（佈局規範、場景）、可選收集（技術偏好）。

### 2. Google AI Studio Builder 的最佳對接
- **能力名單 (Reference.md)**：透過提供 `reference.md` 作為大腦外掛，讓 Claude 精確得知 AI Studio 具體有什麼外接功能 (如影像分析、Nano 生成等)，以便在 Spec 中精確標註要勾選的開關。
- **UI 佈局要極度具體**：文件寫作必須告訴 AI Studio "左欄佔 40%、右側佈局網格"，避免模糊造成 Builder 自由發揮產生災難結果。
- **閉環輸出**：`product-spec-template.md` 規定輸出格式，確保生出的 Product Spec 文件可直接扔丟進 Builder 完成產品構建。
