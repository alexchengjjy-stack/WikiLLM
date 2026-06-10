---
title: "BreezyBrain 規格與情境正反攻防分析報告"
type: analysis
analysis_type: deep_dive
tags: [BreezyBrain, 規格審查, 安全防範, 流程防錯, 攻防論證]
date_created: 2026-05-20
date_updated: 2026-05-20
source_count: 3
sources: ["../products/breezy-brain/Product-Spec.md", "../playbooks/new-lead-qualification.md", "../playbooks/enterprise-trial-followup.md"]
summary: "針對 BreezyBrain CRM 同步、轉檔、地端 LLM 及 BPM 工作流之正反面極端情境攻防，提出相應之安全防禦與容錯降級規格。"
---

# BreezyBrain 規格與情境正反攻防分析報告

> 本報告針對 `Product-Spec.md` 確立之規格，從**「正面設計路徑」**與**「反面邊界威脅/漏洞」**進行深度攻防論證，以確保系統在極端例外或硬體限制下仍具備極高的高可用性與法務安全性。

---

## 🛡️ 攻防焦點一：BreezyCRM 與 WorldCard 名片採集去重與資料缺失
* 業務痛點：業務在展會或外訪時頻繁掃名片，易有重複輸入、離線延遲及欄位不完整問題。

### 1. 正面路徑 (Pros)
* 透過 WorldCard Cloud 掃描名片，API 即時推播結構化 JSON，BreezyCRM 自動建立 Account、Contact 及 Deal，並自動關聯，省去業務手動建檔時間。

### 2. 反面攻擊情境 (Cons & Risks)
*   **情境 1A：重複進件衝突**
    *   *威脅*：不同業務在同場活動掃描同一個客戶名片，或同一業務重複掃描。若系統僅以 Email 為 Unique Key，當名片上無 Email 或填寫公司總機 Email 時，會建立重複的 Account，造成銷售爭議。
*   **情境 1B：離線狀態與同步打架**
    *   *威脅*：地端伺服器斷線，業務在 CRM 找不到該客戶，手動新增；隨後 WorldCard 網路恢復同步，產生兩筆名字相近但 ID 不同的資料，大腦處理時資訊會割裂。
*   **情境 1C：評估欄位缺失**
    *   *威脅*：名片上通常無「員工人數」、「資本額」等潛力評估關鍵指標，大腦若無預設值，將無法進行 `potential_level` (高/中/低) 的自動分級。

### 3. PM 推薦防禦規格 (Defense)（已收斂至 [Product-Spec.md#2.3.2](../../products/breezy-brain/Product-Spec.md#2.3.2)）
- [x] **Account 模糊去重機制**：BreezyCRM 接收 WorldCard 資訊時，優先以 `(公司名稱 + 聯絡人姓名)` 進行模糊比對。若匹配度 > 85%，則僅在既有 Account 下「新增 Contact」，不建立新 Account。
- [x] **離線暫存與合併**：資料同步以「時間戳記」及「名片識別碼 (Card ID)」為準，提供手動合併 (Merge Accounts) 功能。
- [x] **大腦「合理瞎猜」與欄位補全**：當缺少資本額/規模時，地端 LLM 根據「公司名稱」上網搜尋或比對內部工商智庫；若無外網，則預設歸類為 `🟡 中潛力`，並提示業務「待補充關鍵欄位」。

---

## 🛡️ 攻防焦點二：大檔案上傳、客戶端轉檔與任務佇列失聯
* 業務痛點：10MB 以上之非 PDF 檔案在上傳時，因傳輸慢、轉檔耗 CPU，容易導致系統超時卡死。

### 1. 正面路徑 (Pros)
* 客戶端 (WASM) 在上傳前完成 Word 轉 PDF，減輕伺服器負擔；5MB 以上檔案走非同步佇列，回傳 `task_id` 後 HTTP 連線即刻釋放。

### 2. 反面攻擊情境 (Cons & Risks)
*   **情境 2A：客戶端設備性能低下 (WASM 崩潰)**
    *   *威脅*：業務使用低配平板或舊款手機在現場簽約，WASM 在客戶端跑 10MB Word 轉檔時，瀏覽器直接 OOM 崩潰或卡死。
*   **情境 2B：任務佇列「黑洞」 (Silent Task Failure)**
    *   *威脅*：伺服器寫入佇列回傳 `task_id` 後，地端 Docker 容器或 Ollama 崩潰重啟。任務死在佇列中，前端頁面持續顯示 `Processing (處理中)`，客戶無限等待。

### 3. PM 推薦防禦規格 (Defense)（已收斂至 [Product-Spec.md#3.1](../../products/breezy-brain/Product-Spec.md#3.1)）
- [x] **雙軌轉檔 Fallback**：若前端 WASM 初始化失敗或轉檔超過 15 秒，自動降級為「直接上傳 raw 檔」，由地端伺服器之背景服務 (如 LibreOffice Headless) 進行非同步轉檔，但前端需跳出「正在由伺服器處理轉檔，需耗時較久」提示。
- [x] **任務心跳偵測與逾時重試 (Task Heartbeat & TTL)**：
  - 每個非同步任務在 Redis/資料庫中設定 TTL (存活時間，預設 5 分鐘)。
  - 地端代理定期發送心跳。若任務處於 `Processing` 超過 5 分鐘且無心跳，系統自動將狀態改為 `Timeout_Failed`，前端顯示「處理逾時，點此手動重試」。

---

## 🛡️ 攻防焦點三：地端 Local LLM 算力不足與雲端 Fallback 的隱私破口
* 業務痛點：企業為隱私選擇混合落地，但地端無 GPU 時處理速度極慢（2 tokens/s）。

### 1. 正面路徑 (Pros)
* 地端 CPU 處理過長 (>3 分鐘) 時，系統自動回退至雲端安全 API 解析，保障服務高可用性。

### 2. 反面攻擊情境 (Cons & Risks)
*   **情境 3A：隱私合規破口 (Compliance Breach)**
    *   *威脅*：客戶（如醫療診所、法務部門）之合約內含極度敏感個資，當系統「全自動」切換回雲端 API 時，敏感合約流向外網，直接違反客戶的資訊安全合規政策 (GDPR/醫療個資法)。
*   **情境 3B：物理隔離網閘 (Intranet Lock)**
    *   *威脅*：混合落地部署在 100% 無外網的區域網路內，雲端 Fallback 機制呼叫時必定失敗，且會因 http connection timeout 再次卡死背景執行緒。

### 3. PM 推薦防禦規格 (Defense)（已收斂至 [Product-Spec.md#3.2](../../products/breezy-brain/Product-Spec.md#3.2)）
- [x] **「顯性授權」回退機制 (Explicit Opt-in)**：
  - 嚴禁「全自動」回退至雲端。
  - **規格**：當任務排隊超時，系統發送通知：「地端算力繁忙，預計還需 X 分鐘。是否授權透過安全雲端大腦 (Azure OpenAI) 進行加速解析？[授權雲端解析] [繼續地端排隊]」。
- [x] **動態網路探測 (Network Probe)**：地端服務啟動時自動進行 `ping` 雲端端點。若探測無外網，則在後台設定中**強制關閉雲端 Fallback 選項**，直接以地端佇列硬撐，避免無效連線嘗試。

---

## 🛡️ 攻防焦點四：大腦 CLM 「AI 審閱」的判定誤差與法務災難
* 業務痛點：大腦可能漏看關鍵霸王條款（偽陰性），或把所有條款都判斷為高風險（偽陽性）。

### 1. 正面路徑 (Pros)
* 大腦審閱低風險合約直接傳簽；中/高風險合約進入 BPM 審批流，交由法務主管覆核。

### 2. 反面攻擊情境 (Cons & Risks)
*   **情境 4A：大腦偽陰性 (False Negative - 致命漏洞)**
    *   *威脅*：大腦判斷「無風險」，但實際合約中藏有「若逾期一日，需賠償合約金額 100 倍」的霸王條款。系統免審批直通 ESign，客戶雙方簽完字，造成致命虧損。
*   **情境 4B：大腦偽陽性 (False Positive - 效率歸零)**
    *   *威脅*：地端小模型 (7B) 理解力有限，將正常的「若有未盡事宜，雙方友好協商」也判斷為「高風險：管轄權限不明確」，導致 99% 的合約都被卡在法務審批隊列，BPM 自動化形同虛設。

### 3. PM 推薦防禦規格 (Defense)（已收斂至 [Product-Spec.md#2.7.2](../../products/breezy-brain/Product-Spec.md#2.7.2)）
- [x] **「雙重確認」防線**：大腦的「低風險直接傳簽」規格修正為**「低風險快速通道（仍需業務確認）」**。大腦審完低風險後，系統呈現簡化報告：「大腦評估此合約無異常條款，是否確認發送？[確認發送]」，嚴禁大腦 100% 自主決定合約發送。
- [x] **高亮可信度評分 (Confidence Score)**：LLM 輸出結構化 JSON 時，必須針對每個風險點給出 `confidence` (0.0 - 1.0) 與「引用原文段落」。若可信度評分低於 0.8，即使判定為無風險，也必須強制進入法務人工審查佇列。

---

## 相關連結
- [BreezyBrain 產品規格書](../../products/breezy-brain/Product-Spec.md)
- [新潛客資格確認 SOP](../../playbooks/new-lead-qualification.md)
- [企業試用版跟進 Checklist](../../playbooks/enterprise-trial-followup.md)
