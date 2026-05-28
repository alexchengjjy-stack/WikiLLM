# 📂 原始來源管理

> 本目錄存放所有原始來源文件。這些文件是**不可變的** — LLM Agent 只會讀取，不會修改。

---

## 目前目錄結構

```
raw/
├── README.md                              # 本文件
├── signNow plans and pricing.md           # SignNow 定價（待歸類）
│
├── marketing/                             # 行銷策略與技術操作教學（SEO/GEO 實體優化等）
│   ├── Claude 一鍵生成高品質 SEO 文章教學！免費版也能用.md
│   ├── GEO 怎麼做？實測 5 招讓 AI 主動推薦你的品牌，真實對話案例讓你秒懂方法.md
│   ├── NotebookLM 超強SEO工具教學：10分鐘教你快速找到排名上不去的原因，輕鬆超越你的競爭對手！.md
│   ├── 忘掉Google SEO吧！2招超有感的AI SEO做法，品牌引用才是最關鍵！geo  aiseo  超簡單行銷.md
│   ├── 網站少了這個設定，ChatGPT、Google AI 搜尋完全看不見你 ! 3分鐘自己檢查 !.md
│   └── Google 澄清 AEO 及 GEO 搜尋迷思 傳統 SEO 仍是關鍵.md
│
├── AI_knowhow/                            # AI 工程化知識來源（共 19 份）
│   ├── Harness Engineering — AI 工程師的第三個維度.md
│   ├── Harness Engineering 完全解析：當 AI Agent 的護城河不再是模型，而是環境.md
│   ├── Harness Engineering 架構全景：AI 可以寫 Code，但不能自己上 Production.md
│   ├── Harness Engineering 深度解析：AI Agent 时代的工程范式革命.md
│   ├── Harness Engineering 的崛起：打造現代 AI 作業系統架構.md
│   ├── deusyuharness-engineering Harness Engineering 学习指南….md
│   ├── Open Source! I Built My Own OpenClaw — It's Called Forge.md
│   ├── Product Manager 4.0 — How I Vibe Code with Claude Code.md
│   ├── How I Build AI Agent Products in 2025 (Full Workflow).md
│   ├── Agent Teams I Made 3 AI Agents Write Articles Together  Deep Dive + Full Demo.md
│   ├── 如何用Agent Skill创建技能以及技能包 - 飛書雲端文件.md
│   ├── 毒舌产品经理 3.0  - 飛書雲端文件.md
│   ├── 毒舌产品经理 4.0 - 飛書雲端文件.md
│   ├── 0代码，如何用Gemini 3.0开发AI产品 - 飛書雲端文件.md
│   ├── Claude Code + Ollama 本地部署教學：用 CC Switch 打造免費 AI 編程助手.md
│   ├── 630 行代碼讓 AI 自己做研究：Karpathy AutoResearch 完整解析.md
│   ├── AutoResearch是什麼？GitHub破4萬顆星，這630行程式碼如何讓AI自己做研究？.md
│   ├── karpathyautoresearch AI agents running research on single-GPU nanochat training automatically.md
│   └── OpenAI共同創辦人Andrej Karpathy開源新專案，AI代理可持續自動調校LLM.md
│
└── BZSdata/                               # 好好簽（BreezySign）相關資料
    ├── eSign/                             # 電子簽章市場資料（共 10 份）
    │   ├── Check out Docusign eSignature plans.md
    │   ├── 價格方案  點點簽.md
    │   ├── 價格方案.md                    # 律果簽定價
    │   ├── 價格與方案 ，經濟實惠  BreezySign 好好簽 1.md
    │   ├── 價格與方案 ，經濟實惠  BreezySign 好好簽.md
    │   ├── 安全、合法且符合國際級資安規範的電子簽名解決方案.md
    │   ├── 律果簽獲得數發部「電子簽章解決方案服務能量登錄」認可！.md
    │   ├── 適用於企業的 Acrobat 定價和計劃.md
    │   ├── 電子簽章法修法與運用說明｜…moda.md
    │   └── 電子簽章的相關技術介紹｜…moda.md
    │
    ├── ProJects/                          # 好好簽企業專案業務日報（約 21+ 份）
    │   └── YYYYMMDD日報.md × N
    │
    └── SaaS/                              # 好好簽 SaaS 業務日報（約 32+ 份）
        └── YYYYMMDD日報.md × N
```

---

## 子目錄說明

| 目錄 | 內容 | 對應 Wiki 頁面 |
|------|------|---------------|
| `AI_knowhow/` | Harness Engineering、Vibe Coding、Agent 架構、毒舌 PM 等 AI 工程化文章 | `wiki/sources/he-*.md`、`wiki/topics/harness-engineering.md` 等 |
| `marketing/` | 行銷策略、SEO/GEO 實體優化、Schema Markup 操作指引等 | `wiki/skills/seo-optimization.md`、`wiki/skills/geo-optimization.md` 等 |
| `BZSdata/eSign/` | 台灣電子簽章市場競品定價、法規、技術說明 | `wiki/sources/*-pricing.md`、`wiki/sources/taiwan-e-signature-law-2024.md` 等 |
| `BZSdata/ProJects/` | 好好簽企業專案業務日報 | `wiki/sources/bzs-sales-reports-2026.md`（彙整） |
| `BZSdata/SaaS/` | 好好簽 SaaS 業務日報 | `wiki/sources/bzs-sales-reports-2026.md`（彙整）、`wiki/analyses/bzs-acquisition-channels.md` |
| 根目錄 | 尚未分類文件（`signNow plans and pricing.md`） | `wiki/sources/signnow-pricing.md` |

---

## 支援格式

| 格式 | 副檔名 | 說明 |
|------|--------|------|
| Markdown | `.md` | 最佳格式，LLM 可直接完整閱讀 |
| 純文字 | `.txt` | 簡單文字文件 |
| PDF | `.pdf` | 需要 LLM 支援 PDF 解析 |
| 圖片 | `.png`, `.jpg`, `.webp` | LLM 可視覺分析；存放於 `assets/` |

---

## 如何新增來源

### 方法一：Obsidian Web Clipper（網頁文章）

1. 安裝 [Obsidian Web Clipper](https://obsidian.md/clipper) 瀏覽器擴充
2. 在網頁上點擊 Web Clipper 圖示
3. 選擇存放到**對應子目錄**：
   - AI 知識類 → `raw/AI_knowhow/`
   - 電子簽章相關 → `raw/BZSdata/eSign/`
   - 好好簽業務日報 → `raw/BZSdata/ProJects/` 或 `raw/BZSdata/SaaS/`
4. （可選）按 `Ctrl+Shift+D` 下載文章中的所有圖片到本地

### 方法二：手動建立（會議記錄、筆記等）

1. 在對應子目錄中建立新的 `.md` 文件
2. 寫入內容

### 方法三：直接複製

1. 將任何支援格式的文件直接複製或移動到對應子目錄

---

## 攝入流程

來源文件放入此目錄後：

1. 告訴 LLM Agent：「請攝入 `raw/子目錄/檔名.md`」
2. LLM 會閱讀文件、與你討論重點、建立 Wiki 頁面
3. 原始文件保持不變，知識被整合進 `wiki/` 目錄

---

## `assets/` 子目錄

存放圖片與其他附件。在 Obsidian 設定中，可以將「附件資料夾路徑」設定為此目錄：

**Obsidian 設定** → **檔案與連結** → **附件資料夾路徑** → `raw/assets`

---

*最後更新：2026-04-27*
