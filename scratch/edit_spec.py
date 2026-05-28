import sys

sys.stdout.reconfigure(encoding='utf-8')
file_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\products\breezy-brain\Product-Spec.md"

with open(file_path, "r", encoding="utf-8", errors="replace") as f:
    content = f.read()

# 統一換行符為 \n 防止 Windows \r\n 造成匹配失敗
content = content.replace("\r\n", "\n")

# 1. 替換 Epic 7 (負向流程與催簽)
target_epic7 = """*   **防錯重試機制 (Error Handling)**：
    - 若外部 BreezySign API 傳簽超時或發生 5xx 錯誤，BPM 流程中樞需提供「自動重試」機制（間隔 5 分鐘重試 3 次）。
    - 若重試依然失敗，系統必須進入 `Error` 狀態並觸發 UI 警報，供管理員或業務人工點擊「手動更換通道」（例如從 LINE 傳簽切換回 Email 傳簽）。

*   **介面定義 (API/CLI Interfaces)**："""

replacement_epic7 = """*   **防錯重試機制 (Error Handling)**：
    - 若外部 BreezySign API 傳簽超時或發生 5xx 錯誤，BPM 流程中樞需提供「自動重試」機制（間隔 5 分鐘重試 3 次）。
    - 若重試依然失敗，系統必須進入 `Error` 狀態並觸發 UI 警報，供管理員或業務人工點擊「手動更換通道」（例如從 LINE 傳簽切換回 Email 傳簽）。
*   **異常與負向流程規範 (Negative Workflows & Exception States)**：
    - **拒絕/退回流程**：在 BPM 審查中若人工將審核狀態設為 `Rejected` (拒絕)，或外部 BreezySign 傳回簽署拒絕 (`Declined`) 時，對應的 `Deal` 必須自動退回 `Negotiating` 階段。同時，系統將當前 Draft (合約草稿) 自動移回 `/raw` 目錄下，以防止簽署區殘存無效合約，並於大腦介面附帶人工填寫的修改建議以利後續重新生成。
    - **自動催簽與過期狀態 (Cron-based Expiry & Reminder)**：系統設定發送簽署合約後的過期時限 `signing_ttl` (預設為 14 天)。系統會透過後台 Cron 任務，每 3 天自動呼叫一次 `notify_send` 進行 LINE/Email 催簽。若發送超過 14 天仍未完成簽署，系統自動將任務設定為 `Expired` (過期)，並將 KM 中儲存之 Draft 標記為 `Voided` (無效)，防止使用者進行過期或無效合約的後續流程。

*   **介面定義 (API/CLI Interfaces)**："""

# 2. 替換 3.3.2 (網路通訊加密 mTLS, Pinning)
target_332 = """   - `404 Not Found`：資源不存在。
   - `500 Internal Server Error`：模組內部運行錯誤。

#### 3.3.3 統一 CLI 設計規範 (Unified CLI Specification)"""

replacement_332 = """   - `404 Not Found`：資源不存在。
   - `500 Internal Server Error`：模組內部運行錯誤。
4. **網路與通訊安全加密規範 (Network Communication Security)**：
   - **HTTPS/TLS 1.3 強制協定**：所有模組之間的 API 請求以及外部通訊，必須強制採用 HTTPS 協定，且協定版本不得低於 TLS 1.3，以防範網路竊聽。
   - **雙向 TLS (mTLS) 驗證**：地端模組（如 CLM 模組）與外部/DMZ 代理伺服器溝通時，必須啟用雙向 TLS 驗證 (mTLS)，通訊雙方均需校驗彼此的憑證鏈與有效性，杜絕未授權的外部偽造服務。
   - **憑證綁定 (Certificate Pinning)**：地端模組與 DMZ 代理向外部 BreezySign (好好簽) API 發送請求時，必須執行嚴格的憑證綁定。程式中需寫死 BreezySign API 的憑證公開金鑰指紋 (Fingerprint)，在 TLS 握手時進行校驗，有效防範 any 中間人攻擊 (MITM)。

#### 3.3.3 統一 CLI 設計規範 (Unified CLI Specification)"""

# 3. 替換 3.5.1 三大安全防線
target_351 = """#### 3.5.1 MCP 護城河防衛核心思維與威脅模型

*   **防數據扒皮 (Anti-Exfiltration)**：Agent 禁止直接讀取原始合約全文。Resources 唯讀資料預設僅回傳經 AI 蒸餾之「脫敏結構化摘要」，敏感個資 (PII) 自動遮蔽。
*   **防算力濫用 (Anti-Resource Abuse)**：對 Prompts 模板強制注入元提示詞 (Meta-Prompt)，限制 Agent 僅能進行合約審查相關之邏輯推理，拒絕回答通用性或無關之問題。
*   **防流程繞過 (Anti-Bypass / BPM Gate Lock)**：工具 (Tools) 執行涉及合約送簽、商機狀態修改等寫入操作時，系統強制限於 `Pending_Approval` 狀態，必須於 Web UI 經由人工顯性確認後方可發送，杜絕 Agent 自主進行法律簽署。
*   **計費與速率限制 (Rate Limiting & Quota)**：為防止 API Key 遭刷爆或本地 LLM 算力癱瘓，實行 Token 角色權限隔離與速率配額管理。"""

replacement_351 = """#### 3.5.1 MCP 護城河防衛核心思維與威脅模型

*   **操作及資料流程防線 (Operations & Data Flow Moat)**：
    - **防流程繞過 (Anti-Bypass / BPM Gate Lock)**：工具 (Tools) 執行涉及合約送簽、商機狀態修改等寫入操作時，系統強制限於 `Pending_Approval` 狀態，必須於 Web UI 經由人工顯性確認或 CLI 確認後方可發送，杜絕 Agent 自主進行法律簽署。
    - **負向流程與異常狀態**：整合異常與負向流程 (Negative Workflows)，當 BPM 審查 Reject 或簽署 Declined 時，Deal 自動退回 Negotiating 階段，合約 Draft 移回 `/raw` 避險。
    - **隊列積壓與負載控制 (Queue Backpressure)**：為防止大數據上傳或 LLM 併發請求造成崩潰，實施 Redis/Celery 隊列限制（如 12GB VRAM 最多執行 1 個任務），超過上限立即返回 `HTTP 429 Too Many Requests` 與 `Retry-After` 頭部。
    - **快取清理與守護進程 (File Sandbox & Daemon Watchdog)**：使用 `finally` 區塊強制 `rm -rf` 清理 `/storage/tmp/conv/` 下的暫存檔案；同時為 LibreOffice CLI 設定 30 秒的最大執行超時，超時則強行發送 `SIGKILL` 終止該進程。
*   **資訊安全防線 (Information Security Moat)**：
    - **防數據扒皮 (Anti-Exfiltration)**：Agent 禁止直接讀取原始合約全文。Resources 唯讀資料預設僅回傳經 AI 蒸餾之「脫敏結構化摘要」，敏感個資 (PII) 自動遮蔽。
    - **提示詞注入與越獄防禦 (Prompt Injection Defense)**：Ollama 提示詞中採用 XML 標記包裝與 System Instruction 隔離，規避大腦被誘導執行用戶任意命令。對 OCR 轉譯文字進行敏感詞過濾（如 "ignore prior instructions"），若有注入痕跡則降低置信度，並標記 `Jailbreak_Attempt` 送交人工複核。
    - **地端私鑰與憑證管理 (KMS & Document Hash)**：強制地端私鑰不以明文檔案形式存放，需利用地端作業系統金鑰庫（Linux Keyring / Windows Credential Manager / AWS KMS 代理）加密存取；簽署完成時，系統立即計算 PDF 文件之 SHA256 值並寫入 append-only 的 `system_audit.log` 稽核日誌。
    - **通訊加密**：規範模組溝通強制採用 HTTPS/TLS 1.3，地端向外發送請求時，需執行雙向 TLS (mTLS) 與憑證綁定 (Certificate Pinning) 以防範中間人攻擊 (MITM)。
*   **個資安全防線 (Personal Data & Privacy Security Moat)**：
    - **計費與速率限制 (Rate Limiting & Quota)**：為防止 API Key 遭刷爆或本地 LLM 算力癱瘓，實行 Token 角色權限隔離與速率配額管理。
    - **被遺忘權 Qdrant Filter (Right to Be Forgotten)**：ChromaDB/Qdrant 寫入時，向量 payload 強制附加 metadata：`account_id`、`deal_id`、`contact_id`。當刪除客戶時，執行 Qdrant 的 Conditional Delete 指令，依 payload 條件一次性物理刪除該 `account_id` 及其聯絡人的所有向量。
    - **KV Cache 避免跨 Session 串擾 (KV Cache Cross-contamination)**：地端 Ollama 調用時，於 HTTP Header 設置 `keep_alive = 0s` 以即時釋放當前對話之 KV Cache，防範不同客戶對話間的個資殘留或記憶污染。"""

# 4. 替換 3.5.5 個資稽核軌跡
target_355 = """#### 3.5.5 Token 權限隔離、頻率限制與審計日誌

*   **Agent-scoped Token**：外部 Agent 必須配置以 `bb-agent-` 為前綴之專屬 API Token。系統在 API Gateway 根據此 Token 執行細粒度角色存取控制 (RBAC)。
*   **速率限制與算力防禦 (Rate Limiting & Cost Defense)**：
    *   限制單一 Agent Token 每分鐘最多 30 次 MCP 請求。
    *   針對需要調用 Ollama 推理算力的 Tools（如 `risk_assess`），限制每日最高調用額度（預設為 50 次），超過後自動將任務降級至 CPU 背景慢速佇列處理，或拒絕請求，保障地端伺服器不被惡意 Agent 癱瘓。
*   **審計時序日誌 (Audit Trail with `[AGENT_CALL]`)**：
    *   所有的 MCP 資源讀取與工具調用，BreezyBrain 的核心日誌系統將強制寫入 `wiki/log.md` 或系統後端日誌中，並高亮標記 `[AGENT_CALL | Agent-ID]`。
    *   日誌必須詳細記錄：調用時間、調用者 IP、執行的 Resource/Tool 名稱、傳入參數之 SHA256 雜湊值（防敏感資訊外洩），以及消耗之 Ollama 推理 tokens 數，便於系統管理員隨時稽核與安全審查。"""

replacement_355 = """#### 3.5.5 Token 權限隔離、頻率限制與審計日誌

*   **Agent-scoped Token**：外部 Agent 必須配置以 `bb-agent-` 為前綴之專屬 API Token。系統在 API Gateway 根據此 Token 執行細粒度角色存取控制 (RBAC)。
*   **速率限制與算力防禦 (Rate Limiting & Cost Defense)**：
    *   限制單一 Agent Token 每分鐘最多 30 次 MCP 請求。
    *   針對需要調用 Ollama 推理算力的 Tools（如 `risk_assess`），限制每日最高調用額度（預設為 50 次），超過後自動將任務降級至 CPU 背景慢速佇列處理，或拒絕請求，保障地端伺服器不被惡意 Agent 癱瘓。
*   **審計時序日誌 (Audit Trail with `[AGENT_CALL]`)**：
    *   所有的 MCP 資源讀取與工具調用，BreezyBrain 的核心日誌系統將強制寫入 `wiki/log.md` 或系統後端日誌中，並高亮標記 `[AGENT_CALL | Agent-ID]`。
    *   日誌必須詳細記錄：調用時間、調用者 IP、執行的 Resource/Tool 名稱、傳入參數之 SHA256 雜湊值（防敏感資訊外洩），以及消耗之 Ollama 推理 tokens 數，便於系統管理員隨時稽核與安全審查。
*   **個資存取稽核軌跡日誌 (PII Access Audit Trail Log)**：
    - **專屬稽核日誌**：系統必須新增獨立於一般 `[AGENT_CALL]` 日誌之外的 **「個資存取稽核軌跡日誌」 (`/storage/logs/pii_access.log`)**。
    - **記錄時機**：凡是涉及 PII (個人識別資訊，如姓名、電話、身分證字號、Email) 的讀取操作，或經由 CLI/API 存取聯絡人時，系統必須自動寫入該日誌。
    - **日誌格式與欄位**：以 JSON 格式記錄事件，包含以下欄位：
      ```json
      {
        "timestamp": "2026-05-27T18:33:24Z",
        "operator": { "type": "agent", "id": "bb-agent-001" },
        "action": "READ_CONTACT",
        "target_contact_id": "con-6654-uuid",
        "accessed_fields": ["email", "mobile"],
        "purpose": "breezysign_dispatch"
      }
      ```
    - **存取限制與防篡改**：該日誌檔案權限強制設定為 `0600` (僅限系統 administrator/root 可讀寫)。**嚴禁任何 MCP 工具或 API 將此日誌內容回傳給 Agent**，防止 Agent 透過漏洞篡改或擦除個資存取軌跡，確保日誌的絕對嚴密性。"""

# 檢查目標字串是否存在
checks = {
    "target_epic7": target_epic7 in content,
    "target_332": target_332 in content,
    "target_351": target_351 in content,
    "target_355": target_355 in content
}

missing = [k for k, v in checks.items() if not v]
if missing:
    print(f"Error: Target strings not found in Product-Spec.md: {missing}", file=sys.stderr)
    sys.exit(1)

# 替換內容
content = content.replace(target_epic7, replacement_epic7)
content = content.replace(target_332, replacement_332)
content = content.replace(target_351, replacement_351)
content = content.replace(target_355, replacement_355)

# 寫回檔案
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Product-Spec.md updated successfully with perfect target strings!")
