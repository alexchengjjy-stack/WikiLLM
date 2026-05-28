---
title: "如何用Agent Skill创建技能以及技能包"
type: source
category: AI-Engineering
tags: [Agent-Skill, Skill-Creator, Claude-Code, Skill-Architecture]
date_created: 2026-04-19
source_url: "https://feicaiclub.feishu.cn/wiki/RZDGw7z1ViOskTkEK8WcAcjGnGd"
author: "废才俱乐部Club"
---

# 如何用Agent Skill创建技能以及技能包

> 來源目錄：`raw/AI_knowhow/如何用Agent Skill创建技能以及技能包 - 飛書雲端文件.md`

## 摘要與核心啟發

這篇源文件分享了設計一個「Skill Creator Agent」的思路，解決了手寫 Skill 提示詞過於冗長且非標準化的痛點。Skill 不只是指令，而是一種能被 Agent 讀取並轉化為特定工作流水線的特徵檔。透過結構化問答自動產生嚴格的 Markdown 技能文件，使用者能將自身的 Know-how 大量且一致地規模化。

## 關鍵知識點提取

### 1. Skill Creator 品質把控與機制
- **漸進式提問**：Creator 會依據用戶痛點識別所需細節，判定是否需要額外腳本（如 Python 解析）或輔助文件。
- **智能文檔拆分**：若參考資料過長 (>1000字)，自動外掛抽出為 `REFERENCE_{NAME}.md`；若有超過 3 個示例，則新建 `EXAMPLES.md`，以此維持 `SKILL.md` 的精練。
- **YAML 描述的重要性**：`description` 字段是 Claude 選擇/檢索何時調用該 Skill 的唯一依據。必須涵蓋：功能描述 + 使用場景 + 觸發關鍵字。

### 2. 多 Skill 工作流串聯 (Multi-Skill Pipeline)
- 建構複雜工作時，可在目錄下並存多個 Skill (如 PM, Designer, Dev)。
- 必須使用 `CLAUDE.md` 作為主控文件將這些孤島 Skill 串聯，定義指令映射（如輸入 `/PRD` 轉向 PM Skill，`/設計` 轉向 Designer）。
- **文檔傳遞**：上一個技能的工作成果落階成實體 Md 文件，成為下一個技能獲取上下文的最佳銜接點。

### 3. 名詞與能力區別
- **Skill**：強調標準化、可複用與分享。它是一份靜態的 SOP。
- **Agent**：強調擁有「獨立上下文」與「並行執行任務」的動態隔離環境。
- **Command**：類似臨時手動觸發的快捷鍵。日常流程依賴 Skill，複雜隔離任務依賴 Agent，單次簡單操作依賴 Command。
