---
title: "multica-ai/andrej-karpathy-skills: A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls."
source: "https://github.com/multica-ai/andrej-karpathy-skills"
author:
  - "[[多引擎人工智慧]]"
published:
created: 2026-05-26
description: "A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls. - multica-ai/andrej-karpathy-skills"
tags:
  - "clippings"
---
## Karpathy 啟發的 Claude 程式碼指南

> 來看看我的新專案 [Multica——](https://github.com/multica-ai/multica) 一個用於運行和管理具有可重複使用技能的編碼代理的開源平台。
> 
> 請在 X 上關注我： [https://x.com/jiayuan\_jy](https://x.com/jiayuan_jy)

一個用於改進 Claude Code 行為的單一 `CLAUDE.md` 文件，源自 [Andrej Karpathy](https://x.com/karpathy/status/2015883857489522876) 對 LLM 編碼陷阱的觀察。

英文 | [簡體中文](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/README.zh.md)

## 問題

來自 Andrej 的貼文：

> 「這些模型會替你做出錯誤的假設，然後不加核實地照搬這些假設。它們不會處理自身的錯誤，不會尋求澄清，不會指出不一致之處，不會提出權衡取捨，也不會在應該提出異議的時候提出異議。”

> 「他們真的很喜歡把程式碼和 API 搞得過於複雜，堆砌抽象層，不清理無用程式碼……明明 100 行就能搞定的事情，他們卻要用 1000 多行來實現一個臃腫的結構。”

> “他們有時仍然會因為不完全理解而更改/刪除註釋和程式碼，即使這些更改/刪除與任務無關，也會產生副作用。”

## 解決方案

一份文件中包含四項原則，直接針對這些問題：

| 原則 | 地址 |
| --- | --- |
| **編碼前三思** | 錯誤的假設、隱藏的困惑、忽略的權衡取捨 |
| **簡單至上** | 過度複雜化，臃腫的抽象概念 |
| **手術改變** | 正交編輯，觸碰不該觸碰的程式碼 |
| **目標驅動型執行** | 透過先測試後驗證的成功標準來發揮優勢 |

## 四大原則詳解

### 1\. 編碼前先思考

**不要妄下斷言。不要掩飾困惑。坦誠地權衡利弊。**

法學碩士們常常默默地選擇一種解釋並堅持下去。這項原則迫使他們進行明確的推理：

- **明確陳述假設** —如果不確定，請詢問而不是猜測。
- **提出多種解釋** －當歧義存在時，不要默默地做出選擇。
- **必要時提出異議** －如果有更簡單的方法，就說出來。
- **感到困惑時停下來** ——說出不清楚的地方並要求澄清。

### 2\. 簡單至上

**用最少的程式碼解決問題。不要進行任何推測。**

克服過度設計的傾向：

- 除了要求的功能外，沒有其他功能。
- 不為一次性程式碼進行抽象
- 沒有提供任何未要求的“靈活性”或“可配置性”。
- 對於不可能的情況，不進行錯誤處理。
- 如果200行可以縮減到50行，那就重寫它。

**測試：** 資深工程師會認為這太複雜嗎？如果會，請簡化。

### 3\. 手術改變

**只碰你必須碰的東西。只收拾你自己的爛攤子。**

編輯現有程式碼時：

- 不要「改進」相鄰的程式碼、註解或格式。
- 不要重構沒有損壞的程式碼。
- 即使你的想法不同，也要保持與現有風格一致。
- 如果你發現無關的死代碼，請指出來——不要刪除它。

當你的更改創建了孤立文件時：

- 移除因您的修改而不再使用的匯入項目/變數/函數。
- 除非另有要求，否則不要刪除現有的死代碼。

**測試要求：** 每一行修改後的程式碼都應該直接追溯到使用者的請求。

### 4\. 目標驅動型執行

**定義成功標準。循環直至驗證通過。**

將緊迫的任務轉化為可驗證的目標：

| 而不是… | 轉換為… |
| --- | --- |
| 新增驗證 | “編寫針對無效輸入的測試，然後確保它們都能通過。” |
| “修復漏洞” | “編寫一個能夠重現該問題的測試，然後讓它通過。” |
| 重構 X | “確保測試前後均通過” |

對於多步驟任務，請簡要說明計劃：

```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

嚴格的成功標準能讓LLM系統獨立運作。而寬鬆的標準（「只要能運作就好」）則需要不斷澄清。

## 安裝

**選項 A：Claude Code 外掛程式（建議）**

在 Claude Code 中，首先添加市場：

```
/plugin marketplace add forrestchang/andrej-karpathy-skills
```

然後安裝插件：

```
/plugin install andrej-karpathy-skills@karpathy-skills
```

這會將這些指南安裝為 Claude Code 插件，使該技能可在您的所有專案中使用。

**選項 B：CLAUDE.md（每個項目一個）**

新項目：

```
curl -o CLAUDE.md https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md
```

現有項目（追加）：

```
echo "" >> CLAUDE.md
curl https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md >> CLAUDE.md
```

## 與遊標一起使用

此倉庫包含一個已提交的 Cursor 專案規則（[`.cursor/rules/karpathy-guidelines.mdc`](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/.cursor/rules/karpathy-guidelines.mdc) ），因此在 Cursor 中開啟專案時，適用相同的準則。 有關設定、在其他項目中使用此規則以及它與 Claude Code 的關係，請參閱 **[CURSOR.md 檔案。](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/CURSOR.md)**

## 關鍵見解

來自 Andrej：

> 「LLM（學習型學習模式）非常擅長循環往復，直到達到特定目標……不要告訴它該做什麼，給它設定成功標準，然後看著它運行。”

「目標驅動執行」原則體現了這一點：將命令式指令轉換為聲明式目標，並進行驗證迴圈。

## 如何知道它是否有效

如果看到以下情況，則表示這些指導原則有效：

- **減少差異中不必要的變更** －僅顯示請求的變更。
- **減少因過度複雜化而導致的重寫** ——程式碼第一次就很簡單
- **澄清問題應該在實施之前進行** ，而不是在犯錯之後。
- **簡潔、精簡的 PR——** 不進行敷衍了事的重構或「改進」。

## 客製化

這些指南旨在與專案特定說明相結合。您可以將其新增至現有指南中 `CLAUDE.md` ，也可以建立新指南。

對於項目特定的規則，請新增下列部分：

```
## Project-Specific Guidelines

- Use TypeScript strict mode
- All API endpoints must have tests
- Follow the existing error handling patterns in \`src/utils/errors.ts\`
```

## 權衡說明

這些準則傾向於 **謹慎而非速度** 。對於瑣碎的任務（例如簡單的拼字錯誤修正、顯而易見的一行程式碼），請自行判斷—並非每次修改都需要完全嚴謹。

目標是減少重要工作中代價高昂的錯誤，而不是減慢簡單任務的速度。