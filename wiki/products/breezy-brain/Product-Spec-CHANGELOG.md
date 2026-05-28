---
title: "BreezyBrain 需求變更紀錄"
type: changelog
date_created: 2026-05-20
date_updated: 2026-05-28
---

# BreezyBrain 需求變更紀錄 (CHANGELOG)

> 依據 AIPM 規範，所有對於 `Product-Spec.md` 的修改，都必須先在此處進行紀錄。
> 格式規範：`[日期] | [角色] | [變更類型] | [說明]`

## [2026-05-28 14:20] | PM | 修正 + 新增 | 修復規格書毀損並落實 CRM 多類型與自訂欄位擴充規格 — v1.5.2
- **背景**：修復規格書第 202 行因轉碼錯誤導致的 Unicode 損毀（US 1.2 截斷、Epic 2 & 3 標題遺失），並落實使用者對於 CRM 客資管理之 SaaS product, Retail channel, Project 多類型與動態 Pipeline 以及預留擴充空間之指示。
- **變更內容**：
  - **修復 2.2** 節之 US 1.2，並補齊 **Epic 2: BCR 人脈與資料採集** 與 **Epic 3: 輕量企業級 BreezyCRM** 的主標題與 User Stories。
  - **強化 2.3.2 核心資料欄位**：強調 `custom_fields` (JSONB) 動態欄位設計之目的，即為 SaaS product、Retail channel、Project 客製化功能預留極致的增強擴充空間。
- **版本變更**：v1.5.1-MVP → v1.5.2-MVP

## [2026-05-28 10:50] | PM | 新增 | 跨境出海與多簽署廠商合規規格 — v1.5.1
- **背景**：針對產品開拓全球市場（如美國、歐盟）的訂閱服務需要，規劃海外電子簽章法規適配與多簽署服務接串架構。
- **變更內容**：
  - **修改 1.4.1 技術架構**：將雲端連動時戳擴充為可介接 DocuSign / Adobe Sign 等全球認證機構。
  - **新增 3.11 跨境出海與多法規相容性規格**：
    - 定義多市場法律適配要求，包含美國 **ESIGN Act** / 各州 **UETA**（審計軌跡、IP 與簡訊雙因子驗證）與歐盟 **eIDAS**（AdES/QeDS 合格憑證與 EUTL 成員機構）。
    - 規劃 MVP 後的 **「簽署代理中樞 (E-Signature Broker)」** 抽象層架構，規範對接 DocuSign 與 Adobe Sign API，採用統一封套狀態機介面 `breezybrain://clm/envelope/` 以防止供應商綁定，並設定 Model Router 依 CRM 客資「國家/地區」與「幣別」執行智能跨境派發路由。
- **版本變更**：v1.5.0-MVP → v1.5.1-MVP

## [2026-05-28 10:40] | PM | 新增 | KM高頻高並發、UI自訂彈性、Docker支持與GCP部署規格 — v1.5.0
- **背景**：針對企業客戶實際運作場景，補足大用量多人並發、跨平台部署一致性、客戶品牌 CI 白牌化 (White-labeling) 以及首發 GCP MVP 雲端架構之核心產品與工程規格。
- **變更內容**：
  - **新增 2.8.6.1 多人並發、高頻存取與多大模型調度規格**：明定 pgBouncer 連線池與 RLS 行級隔離防護、Redis 緩存 Embedding / 問答快取設計，以及 Model Router 自動調度地端 Ollama 與雲端 Vertex AI Gemini 1.5 的高可用雙軌路由機制。
  - **新增 2.8.7 企業專屬大腦培養與維護機制**：設計「企業術語字典」、人機協作 (HIL) 讚踩糾偏反饋微調迴圈（每週增量 LoRA 訓練），以及個資 (PII) 過濾與作廢合約物理抹除規則。
  - **新增 Epic 10: 客戶公司自訂性與 UI 彈性規格 (White-labeling)**：支持企業上傳專屬 Logo、自訂Favicon與 Title、CSS 變數主題色彩調配（深淺色模式）、自訂導覽與佈局卡片排列，並保留第三方 SDK 程式碼注入掛載口。
  - **修改 3.8.1 地端一鍵部署為 Docker 容器化與跨平台支持規格**：將所有服務元件容器化交付，明確定義 Linux 伺服器、Windows WSL2 vGPU 推理、以及 macOS M 系列 Metal 統一記憶體加速等跨平台支持標準，並規劃離線 Tarball 安裝。
  - **新增 3.10 MVP 於 Google Cloud Platform (GCP) 部署架構**：規劃 Cloud Run (無伺服器 API 與前端)、Cloud SQL for PostgreSQL (RLS 關係庫)、Memorystore for Redis (快取層)、以及 Compute Engine VM 託管 Qdrant 與 Ollama GPU。同時將 Vertex AI Gemini 1.5 Flash 定位為高效能託管推理源與超載 Fallback 端，整合 Secret Manager 金鑰保護與 Cloud Armor 安全網閘。
- **版本變更**：v1.4.0-MVP → v1.5.0-MVP

## [2026-05-28 10:20] | PM | 新增 | 補齊四大隱性死角工程規格 — v1.4.0
- **背景**：針對混合與地端部署模式 (方案 B) 的安全防禦、權限過濾、高可用部署與資料保障，補齊在企業級落地部署時所面臨的隱性死角。
- **變更內容**：
  - **更新 Frontmatter** 版本號至 `v1.4.0-MVP`，更新日期至 `2026-05-28`。
  - **新增 3.6 企業級 RBAC 角色與權限矩陣 (Enterprise RBAC Matrix)**：定義 `Admin` (管理員)、`Legal_Master` (法務主管)、`Sales_Leader` (銷售主管)、`Sales_Rep` (銷售業務) 四種角色的權限邊界，以及基於 RLS 的大腦 RAG 語意問答 Context 檢索過濾。
  - **新增 3.7 地端金鑰鏈管理與完簽 PDF 雜湊防偽存證規格 (Local KMS & PDF SHA256 Hash Spec)**：要求地端私鑰以作業系統安全金鑰鏈 (Windows Credential / Linux Keyring) 進行託管；完簽 PDF 即時計算 SHA256 雜湊，並以 append-only 形式寫入資料庫與 `system_audit.log` 審計日誌中以防範合約篡改。
  - **新增 3.8 地端一鍵部署安裝 CLI 工具規格 (One-click Deployment CLI Spec)**：規劃 `breezy-brain-cli install` 容器化 Docker-compose 一鍵部署工具，支援自動探測地端 GPU 顯存 (VRAM) 資源並自適應選擇載入量化版模型（Qwen 2.5 7B/14B/32B/BGE-M3）。
  - **新增 3.9 資料備份與災難復原機制規格 (Backup & Disaster Recovery Spec)**：定義每日增量備份（PostgreSQL 數據、檔案目錄及向量庫快照）、AES-256 加密與冷儲存傳輸機制，並提供一鍵式災難還原指令 `breezy-brain-cli restore`。
- **版本變更**：v1.3.0-MVP → v1.4.0-MVP

---

## [2026-05-27 17:50] | PM | 新增 | 防禦型 MCP 伺服器規格與護城河防護架構 — v1.3.0
- **背景**：配合外部與內部 AI Agent 動態調用需求，將原本 API/CLI 介面擴展為 MCP 伺服器，並全面收斂對應的護城河防禦機制。
- **變更內容**：
  - **新增 3.5 防禦型 MCP 伺服器規格 (Defensive MCP Server Spec)**，包含：
    - **3.5.1 MCP 護城河防衛核心思維與威脅模型**：定義防數據扒皮、防算力濫用、防流程繞過與計費限流防護網。
    - **3.5.2 Resources (資源) 定義與防禦**：定義客戶客資、履約義務、合約知識摘要的 URI 規範，實施 PII 隱碼與差分隱私數值干擾。
    - **3.5.3 Tools (工具) 定義與防禦**：對齊 `ocr_extract` (路徑沙箱)、`template_match`、`risk_assess` (片段引用限制)、`breezysign_dispatch` (BPM 審批強制鎖)、`crm_update` 的防禦對策。
    - **3.5.4 Prompts (提示模板) 定義與防禦**：定義 `review_contract` 與 `draft_followup` 模板，強制注入元提示詞 (Meta-Prompt) 防範大腦算力挪作他用。
    - **3.5.5 Token 權限隔離、頻率限制與審計日誌**：使用 `bb-agent-` Token 角色隔離 (RBAC)，限制每分鐘 30 次請求與 Ollama 算力配額，所有 MCP 調用強制標記 `[AGENT_CALL]` 稽核日誌。
- **版本變更**：v1.2.0-MVP → v1.3.0-MVP

---

## [2026-05-26 15:23] | PM | 修正 | 地端部署模型之開源授權原則放寬 ── 納入 MIT 授權以對齊商業化安全考量
- **背景**：配合 B2B 企業業務合規要求，為地端部署的開源模型授權提供更寬裕的安全邊界。
- **變更內容**：
  - **修改 3.2.1 節授權原則**：將標題改為「開源模型選型與資源計算（Apache 2.0 / MIT 授權優先）」。
  - **放寬模型授權界限**：正式明文規定 BreezyBrain 地端部署的所有 LLM 模型，優先採用 **Apache 2.0 或 MIT** 授權，確保商業用途完全無任何智慧財產權與授權疑慮。

## [2026-05-21 10:59] | PM | 新增 | Epic 9 儀表板與報告中樞 (Dashboard & Report Hub) — v1.2.0
- **背景**：應用戶需求，為 BreezyBrain 各功能模組新增統一視覺化儀表板與多格式報告匯出能力。
- **變更內容**：
  - **新增 Epic 9：儀表板與報告中樞**，包含：
    - **2.9.1 儀表板架構概覽**：六大子儀表板 + 報告匯出的整體架構圖
    - **2.9.2 六大子儀表板規格**：
      - D1 總覽儀表板：8 個 KPI Card + 5 個視覺化元件（趨勢折線 / 圓餅圖 / 業績排行 / 風險警示 / 義務熱圖）
      - D2 CRM 銷售漏斗：漏斗圖 / 試用到期警示 / 競品分析 / 來源管道效率 + 4 個篩選器
      - D3 CLM 合約生命週期：合約狀態 Kanban / 簽署週期分析 / 風險清單 / 互動式月曆 + 快速動作
      - D4 BPM 工作流監控：積壓儀表 / 錯誤任務列表 / 人工審核佇列 / Gantt-like 時序圖 + 紅/黃告警機制
      - D5 KM 知識庫：健康度儀表 / 向量覆蓋率 / 熱門查詢排行 / 互動式知識圖譜 + RAG 搜尋框
      - D6 AI 大腦績效：推理速度 / 置信度分布直方圖 / Fallback 統計 / 模型版本比較表
    - **2.9.3 報告匯出規格**：
      - 5 種匯出格式：PDF（含圖表）/ Excel（多 Sheet）/ CSV（UTF-8 BOM）/ JSON（API 對接）/ Markdown（KM 歸檔）
      - 6 種預設報告模板：月度業務 / 合約風險稽核 / KM 健康度 / AI 績效 / 到期義務 / 系統全貌
      - 排程自動報告：Cron 表達式 + Email / LINE / Slack 推播
    - **2.9.4 完整 CLI/API 介面**：`dashboard overview/crm/clm/bpm/km/llm` + `report export/schedule`
- **版本變更**：v1.1.0-MVP → v1.2.0-MVP

---

## [2026-05-21 10:21] | PM | 修正 + 新增 | KM DB 分層架構修正：Obsidian 定位變更 + 2.8.6 三層 KM DB 規格（v1.1.0 補皮）
- **背景**：使用者否定「Obsidian 可支撓中大型企業大量合約資料」的設計預設。
- **問題診斷**：Obsidian 底層為純 Markdown 檔案系統，無多人並發鎖、無 RBAC、無向量搜尋、Vault > 5,000 頁時的查詢效能爆降，不適合作為中大型企業的 KM 主要資料庫。
- **變更內容**：
  - **修正 2.8.2 設計原則**：清晰讓 Markdown 為「知識交換格式」而非主要儲存層，確立 PostgreSQL + Qdrant 為 Primary Storage。
  - **修正 2.8.4**：重座小標題為「Web UI 為主，Dataview 為輔」，新增 KM 查詢層三層架構圖表，列入 Obsidian 五大根本性限制對比表。
  - **新增 2.8.6 KM DB 分層架構規格**：
    - 三功能層：Metadata DB (PostgreSQL) + Vector DB (ChromaDB/Qdrant) + Graph Layer (pgvector/Neo4j)
    - Tier 1 MVP：SQLite + ChromaDB（< 1,000 份）
    - Tier 2 中型：PostgreSQL + Qdrant 單節點（1,000~50,000 份）
    - Tier 3 大型：PostgreSQL HA + Qdrant 集群 + Neo4j（> 50,000 份）
    - PostgreSQL 核心表設計（km_contracts + km_obligations + Row-level Security）
    - 規模分層決策樹（年合約份數 + 並發用戶數作為分支標準）
    - Tier 1 → Tier 2 零資料遷移升級路徑承諾

---

## [2026-05-21] | PM | 新增 | Epic 8 KM WikiLLM 架構 + Apache 2.0 模型選型 + Agent + Ollama 完整架構規格 (v1.1.0)
- **背景**：應用戶需求，將 KM 知識智庫升級為可被 Obsidian Dataview 查詢的結構化知識庫，並完整規劃 Agent 架構、Ollama 整合與 Apache 2.0 開源模型選型。
- **變更內容**：
  - **新增 Epic 8**：KM 知識庫實踐 WikiLLM 架構模式，定義完整目錄結構（index.md/log.md/sources/entities/topics/analyses）、YAML Frontmatter 頁面格式規範、Agent 自動攝入五步驟流程、Dataview 查詢範例以及 km ingest/lint CLI 與 API 介面。
  - **新增章範 3.4**：Agent + Ollama 完整架構規格，包含：
    - 整體 Agent 架構圖（Planner + Tool Dispatcher + Ollama）
    - Ollama 部署指令與 OpenAI Compatible API 規格
    - Agent Tool 清單 10 個工具（ocr_extract/km_search/risk_assess/breezysign_dispatch 等）
    - ReAct 迴圈完整範例（旅遊定型化契約自動派單）
    - 6 大商品/服務場景 Agent 實踐對應表
    - 完整 RAG 鏈路規格（Query Embedding → Vector Retrieval → Context Assembly → LLM Generation）
    - 向量資料庫選型（ChromaDB/Qdrant，均 Apache 2.0）
    - Agent 框架選型（LangChain/LlamaIndex）與 Ollama 整合程式碼範例
  - **升級章範 3.2.1**：開源模型選型表大幅沬豐，明確列出已驗證 Apache 2.0 授權的推薦模型（Qwen 2.5 7B/14B/32B、Qwen3 8B、BGE-M3、nomic-embed-text），並說明排除 Llama 3.x 與部分 Mistral 的原因。
  - **載入 KM Embedding 模型**：明確指定 BGE-M3 (Apache 2.0) 為向量化模型。
- **版本變更**：v1.0.0-MVP → v1.1.0-MVP

---

## [2026-05-20] | PM | 變更 | 重構模組交互為 API/CLI 雙軌介面，並同步收斂情境防禦規格
- **背景**：應架構重構與安全防護要求，將 BreezyBrain 各模組交互全面升級為 API/CLI 雙軌介面，並同步將防衛分析報告中所有的防禦對策收斂至規格書。
- **變更內容**：
  - 在 `Product-Spec.md` 的 Epic 1 到 Epic 7，為每個模組補齊對應的 CLI 指令與 API 端點定義。
  - 將 CRM 的模糊去重、合理補全、離線合併等防禦規格收斂入規格書 Epic 3。
  - 將大檔案非同步轉檔 WASM 雙軌降級、任務 Heartbeat 心跳與 5 分鐘 TTL 收斂入規格書 3.1 節。
  - 將地端 LLM 算力不足回退時的「顯性授權」防禦、動態網路探測鎖定收斂入規格書 3.2.4 節。
  - 將 AI 審核大腦偽陰性漏洞的「雙重確認」與「高亮可信度與原文引用」收斂入規格書 Epic 7。
  - 修改 `breezy-brain-integration-flow.md`，以 API/CLI 呼叫重新定義 5 階段自動化流程，並附上 Bash 工作流編排範例。
  - 在 `breezybrain-spec-defense.md` 中將所有防護狀態 Checkbox 勾選為已完成。

## [2026-05-20] | PM | 變更 | 完善 CRM 稅號、範本語意匹配與地端無外網簽署規格
- **背景**：進行最後產品規格 Lint Check，發現三個關鍵死角：B2B 去重缺失統一編號、大腦自動填表單缺少範本匹配規則、地端無外網環境無法串接中華電信 LTV 時戳。
- **變更內容**：
  - 在 `Product-Spec.md` 的 Account 資料欄位補上 `tax_id` (統一編號)，並建立 WorldCard 的 OCR 映射。
  - 在 Epic 1 (US 1.1) 中補上「大腦範本語意匹配 (Semantic Template Mapping)」規則。
  - 在技術架構與計費方案 (1.4.1) 中新增「物理隔離地端環境之 DMZ 網閘代理 (Proxy Gateway) 與降級簽署規格」。

---

## [2026-05-20] | PM | 變更 | CLM 與 BPM (Workflow) 工作與核心規格確立
- **背景**：補足 BreezyBrain 作為企業級合約與流程管理系統的 CLM 與 BPM 規格，明確定義合約版本追蹤、履約履約提醒，以及視覺化節點工作流、高風險審批路由機制。
- **變更內容**：
  - 在 `Product-Spec.md` 中新增「Epic 6: 合約生命週期管理 (CLM)」與「Epic 7: 視覺化工作流與審批引擎 (BPM & Workflow)」。
  - 明確 CLM 的版本變更管理、履約義務提醒與範本變數套用規格。
  - 明確 BPM 的視覺化拖拉節點設計、高風險條件審批路由（防錯機制）以及 API 錯誤重試機制。

---

## [2026-05-20] | PM | 變更 | KM、Files Manager 與 LLM 大腦核心工作規格確立
- **背景**：補足 BreezyBrain 大腦與知識庫、檔案管理的規格細節，定義系統如何利用 Local LLM 進行自動化非結構化資料抽取、合約審查與智能知識檢索。
- **變更內容**：
  - 在 `Product-Spec.md` 中新增「Epic 4: 檔案管理器與知識智庫 (Files Manager & KM)」與「Epic 5: LLM 大腦工作清單 (LLM Brain Job List & Agentic Tasks)」。
  - 詳細規定 Files Manager 的實體存儲架構、KM 向量智庫的索引關聯，以及 LLM 在 BCR 欄位校正、CLM 合約抽取、AI-review 與個人化跟進信件生成等五大 AI 工作清單。

---

## [2026-05-20] | PM | 變更 | BreezyCRM 欄位規格與 WorldCard Cloud 整合確立
- **背景**：配合自行開發小型 CRM (BreezyCRM) 的決定，定義其核心資料庫欄位與銷售跟進階段，並指定蒙恬名片雲 (WorldCard Cloud) 為前端名片採集源。
- **變更內容**：
  - 在 `Product-Spec.md` 中新增「2.1 BreezyCRM 資料欄位與銷售階段規格」。
  - 明確定義 Account (客戶)、Contact (聯絡人)、Deal (商機) 的資料欄位，並將名片 OCR 輸入源無縫對接 WorldCard Cloud 的 API 欄位格式。
  - 對齊既有銷售 SOP (`new-lead-qualification.md` & `enterprise-trial-followup.md`) 定義五大銷售階段 (Stages)。

---

## [2026-05-20] | PM | 變更 | 非 PDF 文件強制於客戶端轉檔規格確立
- **背景**：為簡化地端伺服器 (Server-side) 轉檔之 CPU 負擔，並確保電子簽章 (BreezySign API) 的輸入源格式一致性，決議將非 PDF 格式文件於客戶端進行轉檔。
- **變更內容**：
  - 移除 `Product-Spec.md` 中非 PDF 格式轉檔的 `[TBD]` 待決議事項。
  - 於「3.1 技術限制與處理規格」中新增第 3 點「非 PDF 檔案格式限制與客戶端轉檔」，強制要求 10MB 以下之 .docx 等非 PDF 格式文件在上傳前，由客戶端瀏覽器/桌面端 (WASM) 自動轉換為標準 PDF 格式上傳。

---

## [2026-05-20] | PM | 變更 | 地端 LLM 軟硬體規格與雲端回退 (Fallback) 機制確立
- **背景**：解決地端算力不足（純 CPU 推理）導致大檔案解析超時（>3 分鐘）的風險，為地端部署提供軟硬體基準與高可用回退方案。
- **變更內容**：
  - 移除 `Product-Spec.md` 中的「當地端算力不足時之雲端回退機制 [TBD]`。
  - 新增「3.2 地端 Local LLM 軟硬體與雲端回退規格」，定義以 Qwen 2.5 7B (Q4) 為核心之開源模型選型、最低與推薦硬體配置。
  - 確立當佇列處理超過 180 秒時，自動回退至雲端安全 API（如 OpenAI Azure / 國內合規大模型）之高可用回退機制。

---

## [2026-05-20] | PM | 變更 | 大檔案上傳與處理容錯規格確立 (異步佇列機制)
- **背景**：根據內部測試數據，20MB 以上之大檔案在傳輸與大模型處理時，有 50% 機率 (10 次中 5 次) 發生 Timeout。
- **變更內容**：
  - 移除 `Product-Spec.md` 中大檔案技術瓶頸的 `[TBD]` 待決議事項。
  - 新增「3.1 技術限制與處理規格」，限制單一上傳檔案上限為 10MB，並強制要求 5MB 以上檔案需採用「異步佇列 (Async Task Queue)」與「狀態通知」機制，避免 HTTP Timeout。

---

## [2026-05-20] | PM | 變更 | 定價策略規格確立 (SaaS 訂閱與混合落地雙軌制)
- **背景**：針對電子簽章法律效力 (AATL/LTV) 與客戶隱私 (LLM/CRM) 的雙重考量，確立混合式定價模式。
- **變更內容**：
  - 在 `Product-Spec.md` 中移除「定價策略 TBD」的待決議事項。
  - 新增「1.4 定價策略與商業模式」規格，明確定義 SaaS 訂閱、混合落地建置，以及不論何種模式皆採用的「簽署以份計費」機制。
  - 詳列成本考量因子（LLM 地端硬體、AATL 時戳、Mail 發送等）。

---

## [2026-05-20] | PM | 變更 | CRM 系統依賴轉換為「自建微型 CRM」
- **背景**：依據最新產品決策，避免依賴外部第三方 SaaS (如 Pipedrive)，以提升系統內聚性與掌握度。
- **變更內容**：
  - 取消 Pipedrive 的直接綁定。
  - 將系統六大支柱之一的 CRM 定位轉移為「自行開發小型 CRM (BreezyCRM)」。
  - 修改 `Product-Spec.md` 與 `breezy-brain-manifesto.md` 中對於 Pipedrive 的引用。

---

## [2026-05-20] | PM | 初始化 | 建立第一版產品需求面定義與 MVP 範圍
- **背景**：正式將 BreezyBrain 專案導入 AIPM 規範結構。
- **變更內容**：
  - 確認產品定位為「BreezySign 企業版高階自動化中樞模組」，不正面競爭通用 iPaaS。
  - 定義護城河為 Local LLM 的「AI 合約審閱與資料抽取」及「Graphify 知識圖譜化」。
  - 確立 MVP 首要受眾為：旅遊服務業、醫療/醫美診所、健康管理顧問等具備大量標準合約派發需求的中小企業。
  - 產出 `Product-Spec.md` v1.0.0-MVP 草案。
