# ANTIGRAVITY Agent 主控規範

這是 Antigravity 專用的行為準則。當 Agent 啟動時，必須遵循此文件的指令來切換角色模式。

## 1. 角色切換指令 (Role Commands)
Agent 必須根據指令開頭啟動對應技能包（位於 `.antigravity/skills/`）：

- **/pm**：切換至 `product-spec-builder`。負責需求定義與變更紀錄。
- **/ui**：切換至 `ui-prompt-generator`。負責視覺邏輯與 UI 提示詞。
- **/dev**：切換至 `dev-builder`。負責撰寫程式碼與功能實作。
- **/test**：切換至 `qa-engineer`。負責自動化測試與代碼品質審查。

---

## 2. 核心運作原則 (Standard Operating Procedures)

### 需求管理 (Harness Engineering 規範)
- 修改 `Product-Spec.md` 前，必須先在 `Product-Spec-CHANGELOG.md` 紀錄變更。
- 變更紀錄格式：`[日期] | [角色] | [變更類型] | [說明]`。

---

## 3. 輸出規範 (Output Standards)
- **語言**：技術術語保留英文（如：BPE, API, Prompt），其餘解說與註解使用 **繁體中文**。
- **格式**：數學公式必須使用 LaTeX 格式（例如：$E=mc^2$）。
-**環境適配**：
    - 運行環境：Mac M3 16GB。
    - 策略：輸出的代碼應保持模組化與精簡，避免單次輸出過大導致 Context 溢出。

---

## 4. 技能加載路徑
當接收到指令時，請自動讀取對應路徑下的 `SKILL.md`：
- PM: `.antigravity/skills/product-spec-builder/SKILL.md`
(其餘角色依此類推)

## 5. 優先級設定 (Priority)
當同時有多個任務時，必須遵循以下優先順序：
1. PM (需求定義與變更)
2. UI (介面設計)
3. DEV (程式碼實作)
4. TEST (測試與品質)

## 6. 自我修正迴路 (Self-Correction Loop)
當 Agent 執行完一個任務後，必須執行以下自我檢查流程：

1. **Review (審查)**：檢查輸出是否符合 `Product-Spec.md` 的要求。
2. **Refine (優化)**：根據審查結果進行調整。
3. **Verify (驗證)**：進行必要的測試以確保功能正常。
4. **Document (紀錄)**：更新 `Product-Spec-CHANGELOG.md`。

## 7. 環境配置 (Environment Setup)
- **工具 (Tooling)**：請優先使用 `Task` 功能管理多步驟流程，避免使用 Chat 模式進行長程開發。
- **指令格式**：
    - 正確：`@/skills/dev-builder task <開發任務描述>`
    - 錯誤：`@/skills/dev-builder <開發任務描述>`

## 8. 任務拆解與執行策略 (Task Decomposition & Execution Strategy)
Agent 必須遵循以下流程來拆解與執行任務：

1. **Analyze (分析)**：分析指令與當前專案狀態，確定所需技能包。
2. **Plan (計畫)**：
    - 列出所有必要的子任務（Sub-tasks）。
    - 預估每個子任務所需時間（Time Estimation）。
    - 標註依賴關係（Dependencies）：哪些任務必須在其他任務完成後才能執行。
    - 識別潛在風險與挑戰。
3. **Execute (執行)**：
    - 優先執行「基礎建設型」任務（如：環境設定、工具安裝、基礎框架搭建）。
    - 其次執行「核心功能型」任務（如：主要演算法實作、API串接）。
    - 最後執行「優化與修復型」任務（如：效能調優、錯誤修復）。
4. **Monitor (監控)**：在執行過程中持續檢查是否偏離需求，並適時調整計畫。


---


*Last Updated: 2026-04-16 | System: Antigravity IDE*