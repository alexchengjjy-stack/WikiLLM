# Antigravity Agent 角色切換與指令指南

> **類型**：技能 (Skill)
> **級別**：初級 (Essential)
> **來源**：`raw/AIPM/Agent.md`

## 01. 指令系統 (Command System)
透過斜線指令，您可以將 Antigravity Agent 切換至特定領域的專業模式：

### `/pm` (Product Manager)
- **何時使用**：定義新功能、討論需求細節、撰寫 PRD、紀錄變更日誌。
- **核心文件**：`Product-Spec.md`

### `/ui` (UI Designer)
- **何時使用**：設計介面佈局、討論配色與視覺風格、生成 UI 提示詞。
- **核心文件**：`UI-Prompts.md`

### `/dev` (Developer)
- **何時使用**：撰寫程式碼、配置環境、實作功能、重構代碼。
- **核心文件**：原始代碼檔案

### `/test` (QA Engineer)
- **何時使用**：執行單元測試、檢查安全性漏洞、確認功能覆蓋率。
- **核心文件**：測試報告

---

## 02. 角色優先級 (Priority Hierarchy)
當多個角色任務重疊時，請遵循以下優先權執行：
1. **PM** (沒有正確的需求，就沒有正確的開發)
2. **UI** (視覺邏輯先行)
3. **DEV** (功能實作)
4. **TEST** (最後品質把關)

---

## 03. 指令調用規範
正確的調用格式應包含任務描述，例如：
`@/skills/dev-builder task 實作用戶登入 API`

---

## 04. 運作檢查表
每次切換角色後，Agent 應自動確認：
- [ ] 是否已加載對應的 `SKILL.md`？
- [ ] 當前環境是否支援 (Mac M3 16GB 優化)？
- [ ] 任務是否已拆解為子任務？
