# Project Structure:

此文件定義專案的目錄結構與檔案用途，確保 AI Agent 與開發者遵循統一的架構。

## 目錄結構 (Directory Tree)

project/
├── Product-Spec.md                 # 產品需求文件 (由 /pm 模式自動生成/更新)
├── Product-Spec-CHANGELOG.md       # 需求變更紀錄 (由 /pm 模式強制維護)
├── UI-Prompts.md                   # UI/UX 提示詞清單 (由 /ui 模式生成)
├── ANTIGRAVITY.md                  # Antigravity Agent 主控配置文件 (核心指令集)
└── .antigravity/                   # Antigravity 專用配置資料夾
    └── skills/                     # 角色技能包目錄
        ├── product-spec-builder/   # [PM 角色]
        │   ├── SKILL.md            # PM 思考邏輯與行為準則
        │   └── templates/          # 需求文件格式模板
        ├── ui-prompt-generator/    # [UI 角色]
        │   ├── SKILL.md            # UI 轉譯邏輯與視覺標準
        │   └── templates/          # 提示詞生成模板
        ├── dev-builder/            # [Dev 角色]
        │   └── SKILL.md            # 代碼風格與技術棧規範 (React/Python)
        └── qa-engineer/            # [QA 角色]
            └── SKILL.md            # 測試覆蓋率與安全性檢查標準
        

## 檔案關連說明
- **ANTIGRAVITY.md**: Agent 的進入點，定義如何切換不同技能包。
- **SKILL.md**: 每個角色的「專業知識庫」，定義該角色如何處理特定任務。
- **Templates**: 確保 Agent 產出的內容具備一致性。