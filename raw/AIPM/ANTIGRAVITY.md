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
- **環境適配**：
    - 運行環境：Mac M3 16GB。
    - 策略：輸出的代碼應保持模組化與精簡，避免單次輸出過大導致 Context 溢出。

---

## 4. 技能加載路徑
當接收到指令時，請自動讀取對應路徑下的 `SKILL.md`：
- PM: `.antigravity/skills/product-spec-builder/SKILL.md`
(其餘角色依此類推)

---
*Last Updated: 2026-04-16 | System: Antigravity IDE*