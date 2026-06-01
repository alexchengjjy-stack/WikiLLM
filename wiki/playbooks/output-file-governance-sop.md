---
title: "輸出檔案治理與 Skill 迭代規範"
type: playbook
playbook_type: sop
category: operations
tags: [SOP, 文件治理, 版本控制, 好好簽, 好好腦, outputs, skills]
date_created: 2026-06-01
date_updated: 2026-06-01
related_skills: ["document-output-formats.md"]
summary: "規範 WikiLLM outputs 輸出檔案的命名規則、物理目錄分類隔離以及個人技能 (Skill) 頁面的增量迭代更新流程。"
---

# 輸出檔案治理與 Skill 迭代規範 (SOP)

> **完成定義 (Definition of Done)**：
> 1. 所有導出的輸出檔（HTML, PDF, PPTX 等）均按照統一的命名規則命名，且必須移入物理隔離的專用子目錄中。
> 2. 全面廢除無時間戳記的 Master 預設覆寫檔案，每一次導出皆必須以最新時間戳作為唯一交付版。
> 3. Skill 個人技能頁面保持單一檔案，精熟度更新與經歷累積均以「時間戳記 Log (Timeline)」方式增量追加，不產生多個歷史版本檔案。
> 4. 所有 `analyses/` 目錄下的分析報告均按照統一前綴分類，全域 Markdown 相對與雙鏈連結完整對齊，無失效內部連結。

---

## 何時使用
1. 當需要將 Wiki 庫內容導出、生成營運月報（BreezySign 報告）或產品需求規格書（BreezyBrain Spec）為 HTML、PDF 或 PPTX 格式時。
2. 當需要使用或修改共享品牌資產（如 Logo、背景圖）與報告/簡報模板時。
3. 當使用者的個人技能有更新，或是學會了新工具並需要更新 `wiki/skills/` 頁面時。
4. 當需要於 `wiki/analyses/` 目錄下新建或更新分析報告、進行市場普查或競品觀測時。

## 前提條件
1. 已經安裝必要的自動化生成腳本（如 Python 套件 `python-pptx`, `markdown`）。
2. 生成器已配置 Edge Headless 或 Chrome Headless 瀏覽器路徑以利轉檔。

---

## 流程規範

### 第一階段：輸出檔案分類與命名 (Outputs Governance)

#### 1. 識別產品歸屬與前綴
*   **如果**屬於現役好好簽（BreezySign）相關業務、營運月報、行銷規劃、競品分析，**則**前綴使用小寫 `bzs`。
*   **如果**屬於下一代好好腦（BreezyBrain）相關規格書、架構圖、內部提案簡報，**則**前綴使用小寫 `bzb`。

#### 2. 套用統一檔名規則
*   **檔名結構**：`[bzs | bzb]-[類型與主題名稱]-YYYYMMDD-HHMM-[版本號].[副檔名]`
    *   *現役好好簽範例*：`bzs-ops-report-20260601-1535-v2.html`
    *   *下一代好好腦範例*：`bzb-spec-20260601-1800-v1.pdf`
*   ⚠️ **警告**：全面廢除 `BreezyBrain-Product-Spec.html` 這種不帶日期版本的 master 檔案，防範版本混淆。

#### 3. 物理歸檔至指定子目錄
將生成的檔案輸出到以下指定子目錄，不得直接堆放於 `outputs/` 根目錄：
*   **現役好好簽相關輸出** ➡️ `outputs/bzs/`
*   **下一代好好腦相關輸出** ➡️ `outputs/bzb/`
*   **共享品牌與圖片資產**（如 Logo、Cover 圖檔） ➡️ `outputs/assets/`
*   **報告和簡報的 HTML/PPTX 模板** ➡️ `outputs/templates/`

---

### 第二階段：個人技能增量迭代 (Skill Update)

*   ⚠️ **警告**：嚴禁為 Skill 頁面新建版本檔案（例如建立 `eraser-io-v2.md`）。Obsidian 中的技能頁面為「活實體」，必須維持單一 Markdown 檔案。

#### 1. 更新 Frontmatter 與精熟度
*   當學會新技能或熟練度提升時，修改該 Skill 檔案的 YAML Frontmatter：
    *   `proficiency`：更新精熟度等級（`beginner` | `intermediate` | `advanced` | `expert`）。
    *   `date_updated`：更新為當前日期（`YYYY-MM-DD`）。

#### 2. 增量追加時間戳記 Log (Timeline)
*   **流程**：在該 Skill Markdown 頁面的最底部，新增一個 `## 歷程 Log` 或 `## 實作經驗 Timeline` 標題。
*   **增量追加**：每一次更新均在該標題下方以逆序（最新在最上）追加一個無序列表，記錄時間戳與實作經驗。
    *   *範例*：
        ```markdown
        ## 實作經驗 Timeline
        
        *   **[2026-06-01]**：重構 outputs 檔案治理結構，編寫歸檔腳本並修正 `generate_ops_report_html.py` 使其能自動將檔案導出至 `outputs/bzs/` 子目錄中。
        *   **[2026-05-29]**：在 `bzs-ops-report` 中插入 2025-10 至 2026-05 SaaS 月度實收趨勢與 MoM 增減表格，並使用純 CSS 柱狀圖進行美觀的數據視覺化。
        ```

---

### 第三階段：分析報告命名與分類 (Analyses Governance)

為了確保 Wiki 庫內分析研究資產 (`wiki/analyses/`) 的結構化、防範檔名發散，並實現精準的物理隔離與前綴化管理，制定以下規則：

#### 1. 識別分析主題與物理子目錄分類
所有建立於 `wiki/analyses/` 目錄下的 Markdown 報告，必須依其研究主題歸類至以下四大子資料夾中，並在檔名加上對應的前綴：
*   **現役好好簽 (BreezySign) 相關分析** ➡️ 子目錄：`wiki/analyses/bzs/` ； 檔名前綴：`bzs-`
    *   *範例路徑*：`wiki/analyses/bzs/bzs-saas-marketing-synthesis-2026.md`
    *   *業務範疇*：SaaS 營運數據、CSM 客戶成功對帳、行銷管道分析、用戶畫像與功能需求。
*   **下一代好好腦 (BreezyBrain) 相關分析** ➡️ 子目錄：`wiki/analyses/bzb/` ； 檔名前綴：`bzb-`
    *   *範例路徑*：`wiki/analyses/bzb/bzb-spec-analysis-report.md`
    *   *業務範疇*：需求規格分析、Spec 答辯防禦、產品 MVP 路線圖、技術架構評估。
*   **電子簽章市場與競品觀測相關分析** ➡️ 子目錄：`wiki/analyses/esign/` ； 檔名前綴：`esign-`
    *   *範例路徑*：`wiki/analyses/esign/esign-monitoring-snapshot-202606.md`
    *   *業務範疇*：國內外競品對比（如 DottedSign、LegalSign）、定期普查快照（SEO/GEO 觀測）、定價與功能對比。
*   **WikiLLM 知識庫本體維護與 AI 工具分析** ➡️ 子目錄：`wiki/analyses/wikillm/` ； 檔名前綴：`wikillm-`
    *   *範例路徑*：`wiki/analyses/wikillm/wikillm-kb-health-check-report.md`
    *   *業務範疇*：知識庫健康檢查報告、LLM Agent 方法論評估、AI 工具鏈實測。

#### 2. 套用統一檔名結構
根據報告的「時效性」與「更新頻率」，分為三種類型，並套用相應的命名結構與版本管理邏輯：

| 報告類型 | 定義與特色 | 命名結構 | 檔案路徑與命名範例 |
| :--- | :--- | :--- | :--- |
| **長效結構型** (Static/Structural) | 屬於長期累積、演進的對比與架構分析。**直接在單一檔案內增量修改或重寫**以維持最新，不產生歷史版本檔案。 | `[Prefix]-[主題名稱].md` | `wiki/analyses/esign/esign-domestic-comparison.md`<br>`wiki/analyses/bzb/bzb-spec-analysis-report.md` |
| **週期性快照型** (Periodic Snapshot) | 屬於定期（如每月、每季）進行的市場觀測、SEO/GEO 普查或營運報告。**每一次觀測均建立獨立新檔案**以保留歷史軌跡。 | `[Prefix]-[主題名稱]-[YYYYMM].md` | `wiki/analyses/esign/esign-monitoring-snapshot-202606.md`<br>`wiki/analyses/bzs/bzs-saas-ops-csm-reconciliation-202605.md` |
| **單一事件型** (Event-driven/Ad-hoc) | 針對特定日期發生的事件（如競品突然漲價、特定會議的即時問答歸檔）。**檔名包含具體日期**。 | `[Prefix]-[主題名稱]-[YYYYMMDD].md` | `wiki/analyses/esign/esign-competitor-seo-geo-analysis-20260525.md`<br>`wiki/analyses/bzs/bzs-pricing-cost-structure-analysis-20260525.md` |

⚠️ **警告**：
*   嚴禁使用中文檔名，且必須包含適當的分類前綴，以防跨平台或腳本解析時編碼異常。
*   檔名應採用 kebab-case 格式，全部小寫並以連字號 `-` 分隔。

#### 3. YAML Frontmatter 與 Tags 規範
所有分析報告必須包含 frontmatter，且 `analysis_type` 與 `tags` 的使用需標準化：
*   **YAML Frontmatter 結構**：
    ```yaml
    ---
    title: "分析報告標題"
    type: analysis
    analysis_type: comparison | deep_dive | question | synthesis | snapshot
    tags: [好好簽 | 好好腦 | 競品分析 | 知識庫維護, 標籤1, 標籤2]
    date_created: YYYY-MM-DD
    date_updated: YYYY-MM-DD
    source_count: 1
    sources: ["來源1.md"]
    summary: "一句話摘要"
    ---
    ```
*   **`analysis_type` 分類定義**：
    *   `comparison`：國內外競品或方案的橫向對比分析。
    *   `deep_dive`：單一主題、技術架構或法律條款的深度研析。
    *   `question`：針對特定疑難問答的歸檔（例如 Spec 答辯）。
    *   `synthesis`：跨來源資料的綜合摘要。
    *   `snapshot`：週期性普查、SEO/GEO 觀測快照。
*   **`tags` 規範**：
    *   必須包含與前綴對應的核心標籤，例如：
        *   `bzs-` 開頭必須有 `好好簽`。
        *   `bzb-` 開頭必須有 `好好腦`。
        *   `esign-` 開頭必須有 `競品分析`。
        *   `wikillm-` 開頭必須有 `知識庫維護`。

#### 4. 全域連結安全防禦 (Broken Links Defense)
*   **重命名與搬移安全機制**：當對分析報告進行重命名或搬移至子目錄時，**必須**全域掃描並替換 `wiki/` 目錄下的所有 `.md` 檔案，同步將舊的 Markdown 相對連結與 Obsidian 雙鏈代碼（如 `[[old-base-name]]`、`[[old-base-name#章節]]`、`../analyses/old-base-name.md`）替換為最新正確路徑，以確保無失效內部連結。

---

## 驗證完成
1. 輸出檔案是否位於 `outputs/bzs/` 或 `outputs/bzb/` 底下？
2. 檔名是否帶有 `YYYYMMDD-HHMM-v[N]` 格式？
3. `outputs/` 根目錄是否維持乾淨、沒有堆放新生成的檔案？
4. Skill 頁面是否只有單一檔案，且在底部追加了時間戳記 Timeline Log？

## 出問題時怎麼辦
*   **情況 A：生成腳本回報 `FileNotFoundError`**
    *   *原因*：可能腳本內部仍在使用舊的根目錄路徑（如 `outputs/bzs-logo-green.png`）。
    *   *解決辦法*：檢查並修改該腳本的輸入/輸出路徑，將其重定向至 `outputs/assets/` 或 `outputs/templates/`。
*   **情況 B：Obsidian 內部連結失效（出現紅色連結）**
    *   *原因*：因為重構移除了舊檔案或變更了路徑。
    *   *解決辦法*：在 `wiki/index.md` 與相關文件中，將舊的 `outputs/` 連結修改為 `outputs/bzs/` 或 `outputs/bzb/` 格式。

---

## 相關連結
- [輸出檔案格式轉換 (Skills)](../skills/document-output-formats.md)
- [工作項目分類與打標指南](./work-categorization-guideline.md)
