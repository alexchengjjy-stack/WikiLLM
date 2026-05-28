---
title: "Agent Teams & Orchestration"
type: concept
category: AI-Engineering
tags: [Agent-Teams, Multi-Agent, Human-On-The-Loop, Orchestration]
date_created: 2026-04-19
date_updated: 2026-04-19
source_count: 5
summary: "建立具有總控 Team Lead 與各職能 Teammate 的多智能體團隊，探討 Human-On-The-Loop 監督模式與 Context Firewall 的記憶隔離工程。"
---

# Agent Teams 與智能體編排

> 多智能體協作不只是將任務發包出去，而是賦予各個 Agent 獨立上下文窗口、平行溝通的管道，並藉由共用的目標清單完成自我修正的循環工作流。

---

## Agent Teams 核心運作機制

### 1. 角色區分與通信 (Roles & Mailbox)
Agent Teams 將團隊分為不同層級：
- **Team Lead (總編/主控)**：負責梳理總目標，派發任務。
- **Teammates (隊員)**：擁有獨立而完整的上下文窗口（Context Window），可以認領任務、並通過 Mailbox 和其他 Agent (如執行者與審改者)互相批評與通信。
- 此種配置與過往 Sub-agent (打工仔) 單次執行就歸還結果的模式大相逕庭。

### 2. Context Firewall (上下文隔離)
每個發派的 Teammate 或新建的 Task，其運行的 Agent 實例皆為「**乾淨的上下文 (Clean Context)**」。
目的在於防止前一個任務中可能出現的錯誤假設或幻覺，污染了後續其他 Agent 的判斷。大腦應清空，只加載任務規則、目前 Spec 規範即可執行。

### 3. Human On the Loop (在環上)
AI 在一個共用的「Tasklist」上進行循環與攻防（如寫稿 $\leftrightarrow$ 審核 $\leftrightarrow$ 退件 $\leftrightarrow$ 修改）。
由於 Agent 的交流高度自動化且自主性強，人類無須步步干預 (**Human in the Loop**)，而是退居在更高維度，當某一個迴圈出現死結或抵達關鍵決定點時介入修正方向 (**Human on the Loop**)。

## 延伸系統依賴
- **SOUL.md**：注入整體團隊溝通與協作調性的文本檔。
- **配置方案復用**：這類編排被打包為「Marketplace」級別的工作流，成為一套可以套用到多個場景的開箱即用解決方案。
