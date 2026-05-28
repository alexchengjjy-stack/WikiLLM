# WikiLLM — LLM Agent 操作指南

> 本文件定義了 LLM Agent 在此知識庫中的行為規範、工作流程和頁面格式。
> 所有 Wiki 內容使用**繁體中文**撰寫。英文來源應翻譯為中文摘要。
> 使用**標準 Markdown 連結**格式。所有頁面包含 **YAML Frontmatter** 以支援 Dataview 查詢。

---

## 知識庫結構

```
WikiLLM/
├── AGENTS.md               # 本文件 — LLM Agent 操作指南
├── raw/                     # 原始來源文件（不可變）
│   ├── README.md            # raw/ 目錄說明與分類指引
│   ├── AI_knowhow/          # AI 工程化知識（Harness Engineering、Vibe Coding 等）
│   ├── skills/              # 技能原始素材（課程筆記、工具心得）
│   ├── projects/            # 專案原始素材（會議記錄、需求文件草稿）
│   ├── BZSdata/
│   │   ├── eSign/           # 電子簽章市場（競品定價、法規、技術）
│   │   ├── ProJects/        # 好好簽企業專案日報
│   │   └── SaaS/            # 好好簽 SaaS 業務日報
│   └── [散佈文件]           # 尚未分類的來源
└── wiki/                    # LLM 維護的知識庫
    ├── index.md             # 內容索引（按類別組織）
    ├── log.md               # 操作時序日誌（逆序，最新在最上）
    ├── overview.md          # 知識庫總覽與全局綜合摘要
    ├── sources/             # 來源摘要頁（每個來源一頁）
    ├── entities/            # 實體頁面（公司/人物/產品/專案）
    ├── concepts/            # 概念頁面（方法/框架/技術/流程）
    ├── topics/              # 主題頁面（跨來源綜合分析）
    ├── analyses/            # 分析頁面（問答結果/比較/深度分析）
    ├── skills/              # 個人技能頁面（工具技能 + 職能技能）
    ├── projects/            # 工作專案追蹤（進行中的重要工作）
    └── playbooks/           # SOP / Runbook / Checklist
```

> **新增來源時**：請將文件放入 `raw/` 下的正確子目錄（詳見 `raw/README.md`），攝入指令中需包含完整路徑。

---

## 頁面格式規範

### YAML Frontmatter

所有 Wiki 頁面**必須**包含 frontmatter。以下是各類頁面的標準 frontmatter：

**來源摘要頁 (`wiki/sources/`)**
```yaml
---
title: "來源標題"
type: source
source_file: "raw/子目錄/filename.md"
date_ingested: 2026-04-18
tags: [標籤1, 標籤2]
author: "作者（如有）"
original_date: "原始發布日期（如有）"
language: "原始語言"
summary: "一句話摘要"
---
```

**實體頁面 (`wiki/entities/`)**
```yaml
---
title: "實體名稱"
type: entity
entity_type: company | person | product | project | team | system
aliases: ["別名1", "別名2"]
tags: [標籤1, 標籤2]
date_created: 2026-04-18
date_updated: 2026-04-18
source_count: 1
sources: ["來源1.md"]
summary: "一句話摘要"
---
```

**概念頁面 (`wiki/concepts/`)**
```yaml
---
title: "概念名稱"
type: concept
category: methodology | framework | technology | process | standard | tool
tags: [標籤1, 標籤2]
date_created: 2026-04-18
date_updated: 2026-04-18
source_count: 1
sources: ["來源1.md"]
summary: "一句話摘要"
---
```

**主題頁面 (`wiki/topics/`)**
```yaml
---
title: "主題名稱"
type: topic
tags: [標籤1, 標籤2]
date_created: 2026-04-18
date_updated: 2026-04-18
source_count: 1
sources: ["來源1.md"]
summary: "一句話摘要"
---
```

**分析頁面 (`wiki/analyses/`)**
```yaml
---
title: "分析標題"
type: analysis
analysis_type: comparison | deep_dive | question | synthesis | recommendation
tags: [標籤1, 標籤2]
date_created: 2026-04-18
date_updated: 2026-04-18
source_count: 1
sources: ["來源1.md"]
summary: "一句話摘要"
---
```

**技能頁面 (`wiki/skills/`)**
```yaml
---
title: "技能名稱"
type: skill
category: ai_tools | sales | product | writing | data | devops | legal
proficiency: beginner | intermediate | advanced | expert
tags: [標籤1, 標籤2]
date_created: 2026-04-18
date_updated: 2026-04-18
related_projects: ["project-name.md"]
related_concepts: ["concept-name.md"]
summary: "一句話描述這個技能"
---
```

**專案頁面 (`wiki/projects/`)**
```yaml
---
title: "專案名稱"
type: project
status: planning | active | on_hold | completed | cancelled
priority: high | medium | low
tags: [標籤1, 標籤2]
date_started: 2026-04-18
date_updated: 2026-04-18
related_entities: ["entity-name.md"]
related_skills: ["skill-name.md"]
summary: "一句話描述這個專案"
---
```

**Playbook 頁面 (`wiki/playbooks/`)**
```yaml
---
title: "流程名稱"
type: playbook
playbook_type: sop | runbook | checklist | decision_tree | template
category: sales | customer_success | product | operations | ai_workflow
tags: [標籤1, 標籤2]
date_created: 2026-04-18
date_updated: 2026-04-18
related_skills: ["skill-name.md"]
summary: "一句話描述這個流程"
---
```

### 頁面命名

- 使用 kebab-case 英文命名：`agile-methodology.md`、`project-alpha.md`
- 名稱應簡潔且具描述性
- 避免使用中文檔名（確保跨平台相容性）

### 連結格式

使用標準 Markdown 相對路徑連結：

```markdown
<!-- 從 sources/ 連結到 entities/ -->
[公司名稱](../entities/company-name.md)

<!-- 從 entities/ 連結到 concepts/ -->
[敏捷方法論](../concepts/agile-methodology.md)

<!-- 從任何頁面連結到來源摘要 -->
[來源標題](../sources/source-file-summary.md)
```

### 頁面內容結構

每個頁面在 frontmatter 之後應遵循以下結構：

```markdown
# 頁面標題

> 一段簡短的概述（2-3 句）

## 核心要點
- 重點 1
- 重點 2

## 詳細內容
（主要內容區域，根據頁面類型調整）

## 相關連結
- [相關頁面1](../path/to/page.md)
- [相關頁面2](../path/to/page.md)

## 來源引用
- [來源名稱](../sources/source-summary.md) — 具體引用的觀點或資訊
```

---

## 工作流程

### 📥 Ingest（來源攝入）

當使用者提供新來源文件並要求攝入時，按以下步驟執行：

1. **閱讀來源**：完整閱讀 `raw/` 中的來源文件（包含子目錄路徑）。如果是英文，理解原文含義。
2. **與使用者討論**：總結 3-5 個關鍵觀點，與使用者討論哪些值得強調或深入探討。
3. **建立來源摘要頁**：
   - 在 `wiki/sources/` 中建立新頁面
   - `source_file` 填寫完整相對路徑（含子目錄），如 `raw/AI_knowhow/filename.md`
   - 內容包含：概述、核心論點、關鍵資訊、值得注意的引述
   - 所有內容翻譯為繁體中文
4. **更新實體與概念頁面**：
   - 檢查來源中提及的實體和概念
   - 若頁面已存在：更新內容，增加新資訊，注明來源
   - 若頁面不存在：評估是否值得建立新頁面（重要的實體/概念應建立）
   - 標記任何**矛盾**：新來源與現有知識的不一致
5. **更新主題頁面**：
   - 若來源屬於已有主題，更新該主題頁
   - 若來源開啟新主題，考慮建立新主題頁
6. **同步專案頁面（新！）**：
   - 若業務日報提到進行中案子的里程碑（如鼎新 API 進展、工研院時程），更新 `wiki/projects/` 對應頁面
   - 若日報提到新的未記錄的重要工作，評估是否建立新的 `wiki/projects/` 頁面
7. **更新索引**：
   - 在 `wiki/index.md` 中新增所有新建頁面的條目
   - 更新已修改頁面的摘要（如有變化）
8. **追加日誌**：
   - 在 `wiki/log.md` 頂部追加操作記錄（最新的在最上面）
   - 格式：`## [YYYY-MM-DD HH:MM] ingest | 來源標題`
   - 列出所有建立/修改的頁面與關鍵發現

### 🧠 Skill Update（技能更新）

當使用者提到學到新東西、完成課程、或說「我現在會 X 了」時：

1. **識別技能**：判斷這是「工具技能」（ai_tools）還是「職能技能」（sales/product/...）
2. **找到或建立技能頁**：
   - 若 `wiki/skills/` 已有對應頁面：更新 `proficiency`、加入新的實作經驗段落
   - 若沒有：新建頁面（使用技能 Frontmatter 模板）
3. **連結相關頁面**：技能頁應連結到相關的 sources/、concepts/ 和 projects/
4. **更新 index.md 與 log.md**

### 📁 Project Update（專案更新）

當業務日報或使用者提到進行中工作的新進展時：

1. **識別專案**：判斷這是 `wiki/projects/` 已有的案子還是全新的工作
2. **找到或建立專案頁**：
   - 若已有：更新「目前狀態」中的 `[ ]` 待辦項目為 `[x]`，新增里程碑記錄
   - 若沒有：新建頁面（使用專案 Frontmatter 模板），status 設為 active
3. **更新 date_updated 欄位**
4. **追加 log.md 記錄**

### 📋 Playbook Create（流程建立）

當使用者說「幫我建立 XXX 流程」、「記錄這個 SOP」時：

1. **確認流程類型**：sop（標準程序）/ runbook（操作手冊）/ checklist（清單）
2. **套用 SOP Builder 結構**：
   - 完成定義（最重要，放最前面）
   - 何時使用
   - 前提條件
   - 流程（編號步驟，每步以動詞開頭）
   - 驗證完成
   - 出問題時怎麼辦
3. **撰寫規則**：具體（數字/名稱/閾值）、警告放步驟前、決策點用「如果 X，則 Y」
4. **建立 `wiki/playbooks/` 頁面**，更新 index.md 與 log.md

### 🔍 Query（查詢）

當使用者提出問題時，按以下步驟執行：

1. **讀取索引**：先讀 `wiki/index.md` 找出可能相關的頁面分類
2. **深入閱讀**：讀取相關 Wiki 頁面，收集資訊
3. **綜合回答**：
   - 基於 Wiki 中已編譯的知識回答
   - 引用具體來源和頁面
   - 指出知識庫中的空白處（如果問題超出現有知識範圍）
4. **歸檔有價值的回答**（重要！）：
   - 若回答具有持久價值（分析、比較、綜合），主動提議存入 `wiki/analyses/`
   - 問答中發現的新連結、對比、洞見都是知識資產，不應只停留在聊天記錄中
   - 建立分析頁後更新 `wiki/index.md` 和追加 `wiki/log.md`

### 🔧 Lint（健康檢查）

當使用者要求進行 lint 或健康檢查時：

1. **讀取 log.md**：快速掌握近期操作，了解哪些頁面最近被修改
   - 可用規律前綴快速瀏覽：`## [YYYY-MM-DD` 開頭的行即為各次操作
2. **讀取 index.md**：盤點所有已知頁面
3. **矛盾檢查**：掃描頁面，找出相互矛盾的說法
4. **孤立頁面**：找出沒有任何頁面連結過來的孤立頁面
5. **缺失頁面**：找出在其他頁面中被提及但尚未建立的概念/實體
6. **陳舊內容**：找出可能已被新來源取代的舊資訊
7. **缺失交叉引用**：找出應該相互連結但沒有連結的頁面
8. **建議**：
   - 建議值得調查的新問題
   - 建議可能有用的新來源
   - 建議可以合併或拆分的頁面
9. **追加日誌**：記錄 lint 操作和發現的問題

---

## 索引與日誌規範

### index.md — 內容導覽

`wiki/index.md` 是**內容導向**的目錄：
- 每個 Wiki 頁面列一行：連結 + 一行摘要
- 按類別（sources / entities / concepts / topics / analyses）組織
- **每次 ingest 或建立新頁面都必須更新**
- Query 時優先讀 index.md 找到相關頁面，再深入閱讀

### log.md — 操作時序

`wiki/log.md` 是**時序導向**的操作記錄：
- 追加式（append-only），最新記錄在最上面
- 每筆記錄格式：`## [YYYY-MM-DD HH:MM] 操作類型 | 標題`
  - 操作類型：`ingest`、`analyze`、`update`、`lint`、`init`
- 每筆記錄列出：操作者、來源文件、新建/修改頁面、關鍵發現
- **每次操作都必須追加**，包含 ingest、query 結果歸檔、lint

---

## 品質準則

### 內容品質
- **準確性**：所有事實性陳述必須能追溯到具體來源
- **時效性**：標記過時或可能過時的資訊
- **平衡性**：若不同來源有不同觀點，呈現所有觀點並注明
- **可讀性**：使用清晰的標題、列表和段落結構

### 連結品質
- 每個頁面至少應有 1 個向外的連結（指向相關頁面）
- 每個頁面應被至少 1 個其他頁面連結（避免孤立）
- 連結文字應有描述性（避免「點此」式連結）

### Frontmatter 品質
- `date_updated` 應在每次修改時更新
- `source_count` 應準確反映引用的來源數量
- `tags` 應保持一致性（使用已有的 tag，而非建立近似的新 tag）
- `summary` 不超過 50 字
- `source_file` 必須填寫完整相對路徑（含子目錄）

---

## 常用 Dataview 查詢範例

使用者可在 Obsidian 中使用以下 Dataview 查詢：

```dataview
// 列出所有來源，按攝入日期排序
TABLE date_ingested, summary
FROM "wiki/sources"
SORT date_ingested DESC
```

```dataview
// 列出特定標籤的頁面
TABLE type, summary, date_updated
FROM "wiki"
WHERE contains(tags, "AI")
SORT date_updated DESC
```

```dataview
// 找出最近更新的頁面
TABLE type, summary
FROM "wiki"
SORT date_updated DESC
LIMIT 10
```

```dataview
// 列出所有實體，按引用來源數排序
TABLE entity_type, source_count, summary
FROM "wiki/entities"
SORT source_count DESC
```

---

## 注意事項

1. **不要修改 `raw/` 目錄**中的任何檔案。原始來源是不可變的。
2. **每次操作都要更新 `log.md`**，保持操作歷史完整。
3. **每次新增或修改頁面都要更新 `index.md`**。
4. **發現矛盾時主動標記**，不要靜默忽略。
5. **保持頁面精簡**：一個主題/實體/概念一頁，避免超大頁面。
6. **交叉引用很重要**：建立頁面時，思考它與哪些現有頁面有關。
7. **好的回答是知識資產**：有價值的 Query 結果主動存入 `wiki/analyses/`。
8. **source_file 路徑**：攝入新來源後，`source_file` 欄位必須填寫含子目錄的完整路徑。
9. **日報攝入時同步更新專案頁**：若日報提到進行中工作有里程碑（如合約進展、API 上線、提案通過），務必更新 `wiki/projects/` 對應頁面的狀態。
10. **技能頁是活的**：定期（每季或學到新東西時）更新 `wiki/skills/`，更新 `proficiency` 等級與實作經驗。
11. **報告產出與版次管理**：產出的報告檔案需包含日期時間資訊。若遇到同名檔案，應在檔名後方依序加上 V1、V2... 等版本號以保留每一個歷史版次，儘量避免覆蓋。同時，往後一律不再輸出無時間戳記之預設覆寫檔案，全面以帶有精確時間戳之版控檔案作為唯一產出與交付，防範版本混淆。
12. **普查與情報快照實測規範**：未來凡是進行市場普查報告、對比報告（如競品 SEO/GEO 普查）或電子簽章能量登錄競品情報普查快照等，**均必須實際執行爬取或探測各個個別競品網站之網頁最新情況，確保事實完全準確**。嚴禁僅憑舊資料推估或超前描述。在比較基準上，競品數據必須以對外公開之正式站（Production）為唯一基準，最多僅能加入我方好好簽之預備測試站（Staging）作為對照，以求數據的絕對嚴謹性與實事求是。
