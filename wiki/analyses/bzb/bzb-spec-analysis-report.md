---
title: "BreezyBrain 需求規格深度分析與規劃報告"
type: analysis
analysis_type: deep_dive
tags: [BreezyBrain, 架構規劃, 流程防錯, 安全防範, 產品Roadmap]
date_created: 2026-05-29
date_updated: 2026-05-29
source_count: 3
sources: ["../products/breezy-brain/Product-Spec.md", "bzb-spec-defense.md", "bzb-mvp-roadmap.md"]
summary: "針對 BreezyBrain 進行分層架構、順逆向流程管道、安全性防護規格與三階段路線圖規劃的正式評估報告。"
---

# 🧠 BreezyBrain 需求規格 (Product Spec) 深度分析與規劃報告

> **文件類型**：技術評估與架構分析報告
> **語言**：繁體中文
> **關聯文件**：[Product-Spec.md](../products/breezy-brain/Product-Spec.md) | [bzb-spec-defense.md](bzb-spec-defense.md) | [bzb-mvp-roadmap.md](bzb-mvp-roadmap.md)

本報告基於 WikiLLM 知識庫內部的正式報告與正反攻防討論，針對自研產品 **BreezyBrain (好好腦)** 進行全局性的架構拆解、智能業務流程整理、關鍵安全防禦剖析以及三階段產品路線圖 (Roadmap) 規劃。

---

## 1. 🗂️ 系統架構分層設計 (System Architecture)

為了實現高可用、高安全性並支援地端與雲端雙軌運行，BreezyBrain 採用了標準的 **分層解耦架構**，各層之間透過定義良好的 API / CLI 進行通訊，防止資料庫內存直連：

### 1.1 展示與接口層 (Presentation Layer)
*   **Web Console**：提供直觀的 CRM 銷售看板、BPM 審批清單、以及大腦模型路由與 Token 配額設定。
*   **CLI Tool**：提供技術IT人員進行地端安裝部署 (`breezy-brain-cli install`)、資料庫手動合併 (`merge-accounts`) 及合約版本比對 (`clm diff`) 的高效率命令行介面。

### 1.2 核心應用與業務層 (Application Layer)
*   **BreezyCRM**：管理 SaaS、經銷商及專案客戶，內建模糊去重及欄位缺失容錯機制。
*   **BCR (Business Card Recognition)**：串接名片雲進行高精度 OCR 採集。
*   **BPM / Workflow**：拖拉式節點編排引擎，包含人工防衛審批與例外回滾機制。
*   **BreezyCLM / E-Sign**：自動填入變數，進行合約生命週期與催簽通知。
*   **BreezyKM**：對已簽署 PDF 自動化摘要、向量化與圖譜化歸檔。

### 1.3 AI 智能大腦中樞 (AI Brain Core)
*   基於地端 Local LLM (Ollama/Qwen 2.5) 保障商業機密，提供 Model Router 自動根據任務長度與類型路由，並利用 ChromaDB/Qdrant 實現地端 RAG 與 Long-term Memory。

### 1.4 安全與外部對接邊界 (Security & Boundary)
*   在無外網隔離環境中，透過 **DMZ 網閘代理 (Proxy)** 限定通訊埠連通外部，呼叫 BreezySign API 以保障 AATL 數位憑證與 LTV 時戳之有效性；若為極端完全斷網，則降級為地端自簽私有 CA 簽署。

---

## 2. 🔄 核心業務流程與數據管道 (Operations & Data Flow)

BreezyBrain 的數據處理流程分為**順向自動化閉環**與**反向例外防禦**：

### 2.1 順向核心數據管道 (Data Pipeline)
1.  **名片進件**：業務上傳名片 ➡️ BCR 辨識 ➡️ **CRM 模糊去重機制**（利用 `公司名稱+聯絡人` 比對，相似度 >85% 則自動合併至舊 Account）➡️ 地端 LLM 比對工商庫自動補齊缺失欄位（如資本額）➡️ 判定潛力等級 `potential_level`。
2.  **合約匹配與發送**：CRM 商機變更為 `Won` ➡️ CLM 自動讀取非結構化合約草案 ➡️ 大腦提取 JSON 變數並執行**語意範本匹配** ➡️ 自動套用對應的 BreezySign 範本。
3.  **大腦審閱與送簽**：大腦分析合約條文風險 ➡️ 提供置信度評分與原文高亮 ➡️ 低風險合約進入**低風險快速通道**（業務於 Web 端顯性點擊「確認」後發送）；高風險合約路由至 BPM 法務主管審核 ➡️ 網閘代理 ➡️ 呼叫 BreezySign API 發送簡訊/LINE 傳簽。
4.  **智庫歸檔與履約**：雙方簽署完成 ➡️ 自動觸發 OCR 與向量化 (`bge-m3`) ➡️ 自動抽取合約中的保固、付款日期等履約義務 ➡️ 寫入系統行事曆 ➡️ 觸發 KM 知識庫圖譜化 (Graphify) 沉澱為企業第二大腦。

### 2.2 逆向與負向流程規範 (Negative & Exception Workflows)
*   **拒絕/退回機制 (Rejected Flow)**：人工審批拒絕或外部客戶拒簽時，Deal 自動退回 `Negotiating` 階段，系統將 Draft PDF 移至備份目錄，並標記大腦欄位為 `[Pending-Correction]`。
*   **過期作廢 (Cron-based Expiry)**：合約設定 14 天 TTL，過期前 3 天自動進行 LINE / SMS 催簽。過期時，系統自動標記合約為 `Voided`，防止業務誤用無效契約。
*   **流量回壓 (Queue Backpressure)**：限制地端 Ollama 同步並發數，當佇列積壓 >10 件時對新 Webhook 拋出 `HTTP 429 Too Many Requests`，保障地端 GPU 不會崩潰。

---

## 3. 🛡️ 規格防範與資安隱私防護 (Security & Compliance)

針對企業客戶高度敏感的個資與法務法規，系統設計了多層隱性安全防線：

### 3.1 資訊安全性 (Information Security)
*   **防範提示詞注入 (Prompt Injection)**：在 LLM System Prompt 中採用「指令與資料分離」架構，將 OCR 文本置於 XML 標籤內，並加入輕量前置過濾。一旦發現 `ignore prior instructions` 等越獄字眼，置信度直接清零，強制跳轉法務人工審查。
*   **雙向 TLS 加密 (mTLS)**：地端 CLM與 DMZ 網閘代理之間強制執行雙向 TLS 認證；DMZ 與雲端 API 通訊採用 Certificate Pinning（證書指紋硬編碼），防範中間人攻擊 (MITM)。
*   **私鑰保護與雜湊防偽**：地端降級自簽憑證之私鑰必須託管於作業系統安全金鑰鏈 (KMS)，完簽合約立即計算 SHA256 雜湊並寫入 Append-only（唯追加）的系統日誌，以防手動篡改。

### 3.2 個資安全性 (Privacy Security)
*   **GDPR 被遺忘權實作**：在寫入向量資料庫 (ChromaDB/Qdrant) 時，所有 Vector Payload 必須強制附加 `{account_id, contact_id}`。當 CRM 執行客戶個資刪除時，同步呼叫向量庫的 Payload Filter 執行物理擦除，確保無隱形個資殘存。
*   **LLM KV Cache 租戶防污染**：調用地端 Ollama 時設定 `keep_alive = 0s` 參數，任務結束立刻清空推理內存，防止 A 客戶的 KV Cache 污染 B 客戶的問答結果；大企業客戶可租用獨立的容器實例進行物理隔離。
*   **PII 個資稽核軌跡**：所有個資存取行為均強制記錄於 `/storage/logs/pii_audit.log` 唯追加稽核檔（權限設為 `0600`，且嚴禁 MCP / API 讀取回傳），以通過個資稽核。

---

## 4. 🗺️ 三階段產品演進路線圖 (Product Roadmap)

為了能快速投入市場驗證並降低研發硬體成本，產品實施了**三階段漸進式路線圖**：

| 階段別 | 技術架構 (Tier) | AI 大腦與推理規格 | 核心業務功能 |
| :--- | :--- | :--- | :--- |
| **Phase 1: MVP Core**<br>*(當前驗證階段)* | **Tier 1 輕量架構**<br>・SQLite<br>・ChromaDB<br>・地端單主機 | ・Ollama Qwen 2.5 7B<br>・地端 Embedding (`bge-m3`) | ・名片 BCR 進件與 CRM 模糊去重<br>・自動合約變數提取與範本匹配<br>・低風險快速通道（Web 端確認） |
| **Phase 2: Growth**<br>*(自動化與增強)* | **Tier 2 標準架構**<br>・PostgreSQL<br>・Qdrant 單節點<br>・雙軌轉檔 (WASM+LibreOffice) | ・AI 提示詞注入過濾<br>・Ollama KV Cache 即時清理<br>・Azure OpenAI 雲端 Fallback | ・BreezySign 自動發送與 LINE 催簽<br>・合約 AI 高風險審查與原文引用<br>・個資 RLS 權限與 PII Audit Log |
| **Phase 3: Enterprise**<br>*(集團與圖譜化)* | **Tier 3 集群架構**<br>・PostgreSQL 主從分區<br>・Qdrant 3 節點集群<br>・Neo4j 圖資料庫 | ・地端私鑰 KMS 託管<br>・部門級 Ollama 容器實例隔離<br>・LoRA 本地增量微調 | ・視覺化 BPM 節點式工作流編排<br>・合約/客戶知識圖譜 (Graphify) 導航<br>・一鍵式地端 CLI 安裝與每日備份 |

---

## 5. ✍️ 結論與建議

BreezyBrain 的規格設計極為紮實，克服了市面上大部分 iPaaS/RAG 系統在地端部署與個資隱私上的致命漏洞。
1.  **目前核心重點**：應確實執行 **Phase 1 MVP** 的開發收斂，利用輕量架構快速實現「掃描名片 ➡️ CRM 商機 ➡️ 語意匹配 CLM ➡️ 快速送簽」的完整閉環。
2.  **中長期規劃**：在 Phase 2 開始時，應將主力放在 **「雙重確認防線」與「GDPR 被遺忘權向量擦除」** 的實作上，這是進入醫療、金融或跨國企業市場的必要法規敲門磚。
3.  **視覺化輔助**：為使團隊溝通一致，本報告規劃的系統拓撲與分層關係已完全同步生成於 [BreezySign 拓撲圖](../outputs/20260529-1155-breezysign-architecture.html)，該關係圖已支援**高解析度橫向顯示**及**白底 PDF 高對比度列印模式**，確保紙本與流式 PDF 列印品質無損。
