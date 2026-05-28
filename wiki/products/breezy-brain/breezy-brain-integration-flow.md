---
title: "BreezyBrain 跨系統自動化數據流與 API 整合規格"
type: product-specification
product_line: BreezySeries
status: concept
date_created: 2026-05-19
tags:
  - "下一代產品"
  - "BreezyBrain"
  - "API整合"
  - "數據流"
---

# 🔄 BreezyBrain 跨系統自動化數據流與 API 整合規格

本文件定義了 BreezyBrain（好好腦）五大資訊系統與 KM 之間，如何透過大模型（LLM AI Model）與 API 進行自動化聯動。核心著重於從「人脈採集」到「自動調用 BreezySign API (call BZS API)」的閉環。

---

## 🚀 一、 核心自動化工作流 (End-to-End Workflow)

數據流動分為四大階段，實現全流程免手動輸入：

```
+---------------+     人脈資料同步     +--------------------+     建立專案與跟進     +---------------------+
| BCR 名片 OCR  |  ===============>  |  CRM (BreezyCRM)   |  ====================>  | CLM/BPM (Word協作)  |
+---------------+                    +--------------------+                         +----------+----------+
                                                                                               |
                                                                                               | AI-review 與審批
                                                                                               v
+----### 階段 1：名片採集與 CRM 資料建立 (BCR ➡️ CRM)
* **觸發點 (Trigger)**：業務人員拍照名片並由 BCR OCR 解析成功。
* **API/CLI 呼叫**：
  * **CLI 指令**：`breezy-brain crm sync-card --file /path/to/card_ocr.json --auto-complete true --format json`
    * **成功輸出 (stdout)**：
      ```json
      {
        "success": true,
        "data": {
          "account_id": "acc-9987-uuid",
          "contact_id": "con-6654-uuid",
          "deal_id": "deal-3211-uuid",
          "is_merged": false
        },
        "error": null
      }
      ```
  * **API 端點**：`POST /api/v1/crm/sync-card`
    * **Request Body**：
      ```json
      {
        "file_path": "/path/to/card_ocr.json",
        "auto_complete": true
      }
      ```
    * **Response Body (HTTP 200 OK)**：
      ```json
      {
        "success": true,
        "data": {
          "account_id": "acc-9987-uuid",
          "contact_id": "con-6654-uuid",
          "deal_id": "deal-3211-uuid",
          "is_merged": false
        },
        "error": null
      }
      ```
* **動作 (Action)**：大腦自動校正 OCR raw text，並在 CRM 中建立 `Account` (以 `tax_id` 去重，支援 >85% 模糊比對) 與 `Contact`，並自動開啟一個 `Deal`。

### 階段 2：客戶專案記錄跟進 (CRM followup/Status)
* **流程**：業務人員在 BreezyCRM 中推進銷售階段。
* **API/CLI 呼叫**：
  * **CLI 指令**：`breezy-brain brain run --job generate_followup --input '{"deal_id": "deal_uuid"}' --format json`
    * **成功輸出 (stdout)**：
      ```json
      {
        "success": true,
        "data": {
          "job_id": "job-8876-uuid",
          "status": "pending"
        },
        "error": null
      }
      ```
  * **API 端點**：`POST /api/v1/brain/jobs`
    * **Request Body**：
      ```json
      {
        "job_type": "generate_followup",
        "deal_id": "deal_uuid"
      }
      ```
    * **Response Body (HTTP 200 OK)**：
      ```json
      {
        "success": true,
        "data": {
          "job_id": "job-8876-uuid",
          "status": "pending"
        },
        "error": null
      }
      ```
* **大腦輔助**：讀取 `enterprise-trial-followup` SOP，自動產出個人化跟進信件草稿。

### 階段 3：合約協作與 BPM AI 審核 (CLM ➡️ BPM)
* **協作**：銷售與法務在 CLM 線上編輯 Word 合約，上傳時觸發 BPM 流。
* **API/CLI 呼叫**：
  * **CLI 指令**：`breezy-brain bpm run --workflow-id wfl_contract_review --deal-id <deal_uuid> --format json`
    * **成功輸出 (stdout)**：
      ```json
      {
        "success": true,
        "data": {
          "task_id": "task-5543-uuid",
          "status": "processing",
          "workflow_id": "wfl_contract_review"
        },
        "error": null
      }
      ```
  * **API 端點**：`POST /api/v1/bpm/run`
    * **Request Body**：
      ```json
      {
        "workflow_id": "wfl_contract_review",
        "deal_id": "deal_uuid"
      }
      ```
    * **Response Body (HTTP 202 Accepted)**：
      ```json
      {
        "success": true,
        "data": {
          "task_id": "task-5543-uuid",
          "status": "processing",
          "workflow_id": "wfl_contract_review"
        },
        "error": null
      }
      ```
* **大腦輔助**：自動呼叫 `clm_review` 任務對 Draft 進行 AI-review，輸出包含 `confidence_score` 與 `original_text_quote` 的 JSON 報告。

### 階段 4：自動調用好好簽 API 發送傳簽 (BPM ➡️ ESign) ── 🔌 **核心自動化**
* **觸發點 (Trigger)**：BPM 流程經 AI 審核（無中高風險且大於 0.8 置信度，並經由業務在 CLI 或 UI 進行「雙重確認」點擊）。
* **API/CLI 呼叫**：
  * **CLI 指令**：`breezy-brain clm dispatch --deal-id <deal_uuid> --template-id tpl_contract_2026_v4 --format json`
    * **成功輸出 (stdout)**：
      ```json
      {
        "success": true,
        "data": {
          "envelope_id": "env-bzs-8876a9f0",
          "signing_url": "https://api.breezysign.com/sign/env-bzs-8876a9f0",
          "status": "sent"
        },
        "error": null
      }
      ```
  * **API 端點**：`POST /api/v1/clm/dispatch` (BPM 核心將自動調用 BreezySign API 完成發送)
    * **Request Body**：
      ```json
      {
        "deal_id": "deal_uuid",
        "template_id": "tpl_contract_2026_v4"
      }
      ```
    * **Response Body (HTTP 200 OK)**：
      ```json
      {
        "success": true,
        "data": {
          "envelope_id": "env-bzs-8876a9f0",
          "signing_url": "https://api.breezysign.com/sign/env-bzs-8876a9f0",
          "status": "sent"
        },
        "error": null
      }
      ```
* **API 調用邏輯 (Call Specification)**：
  ```json
  POST https://api.breezysign.com/v1/templates/use
  Authorization: Bearer <BZS_API_KEY>
  Content-Type: application/json

  {
    "template_id": "tpl_contract_2026_v4",
    "document_name": "好好簽BreezyBrain_下一代合作合約_CRM同步案",
    "signers": [
      {
        "role": "Client",
        "name": "BreezyCRM.Contact.Name",
        "email": "BreezyCRM.Contact.Email",
        "mobile": "BreezyCRM.Contact.Mobile",
        "verification_method": "SMS_OTP"
      },
      {
        "role": "BZS_Sales",
        "name": "CRM.Owner.Name",
        "email": "CRM.Owner.Email"
      }
    ],
    "meta_data": {
      "crm_deal_id": "breezycrm_deal_9987",
      "bpm_process_id": "bpm_proc_6654",
      "auto_archive": true
    }
  }
  ```
* **傳簽特徵**：支援 **LINE 傳簽** (由 API 自動產生 LINE 專屬簽署連結發送至聯絡人手機)。

### 階段 5：知識沉澱與圖譜化歸檔 (ESign ➡️ KM)
* **觸發點 (Trigger)**：雙方完成簽署後，BreezySign Webhook 自動向 KM 發送完成通知。
* **API/CLI 呼叫**：
  * **CLI 指令**：`breezy-brain km extract --file /storage/contracts/deal_9987_signed.pdf --account-id <account_uuid> --format json`
    * **成功輸出 (stdout)**：
      ```json
      {
        "success": true,
        "data": {
          "file_path": "/storage/contracts/deal_9987_signed.pdf",
          "summary": "本合約為方睿科技與好好簽之企業SaaS訂閱合約，金額為新台幣50,000元，保固期至2027-05-20。",
          "obligations": [
            { "due_date": "2027-05-20", "description": "保固期滿與維護合約續約通知" }
          ]
        },
        "error": null
      }
      ```
  * **API 端點**：`POST /api/v1/km/extract`
    * **Request Body**：
      ```json
      {
        "file_path": "/storage/contracts/deal_9987_signed.pdf",
        "account_id": "account_uuid"
      }
      ```
    * **Response Body (HTTP 200 OK)**：
      ```json
      {
        "success": true,
        "data": {
          "file_path": "/storage/contracts/deal_9987_signed.pdf",
          "summary": "本合約為方睿科技與好好簽之企業SaaS訂閱合約，金額為新台幣50,000元，保固期至2027-05-20。",
          "obligations": [
            { "due_date": "2027-05-20", "description": "保固期滿與維護合約續約通知" }
          ]
        },
        "error": null
      }
      ```
* **動作 (Action)**：地端服務將已簽署 PDF 自動歸檔，提取重要期日，並透過本地 embedding 模型向量化存入 ChromaDB，完成 `Graphify` 雙鏈知識關聯。一代合作合約_CRM同步案",
    "signers": [
      {
        "role": "Client",
        "name": "BreezyCRM.Contact.Name",
        "email": "BreezyCRM.Contact.Email",
        "mobile": "BreezyCRM.Contact.Mobile",
        "verification_method": "SMS_OTP"
      },
      {
        "role": "BZS_Sales",
        "name": "CRM.Owner.Name",
        "email": "CRM.Owner.Email"
      }
    ],
    "meta_data": {
      "crm_deal_id": "breezycrm_deal_9987",
      "bpm_process_id": "bpm_proc_6654",
      "auto_archive": true
    }
  }
  ```
* **傳簽特徵**：支援 **LINE 傳簽** (由 API 自動產生 LINE 專屬簽署連結發送至聯絡人手機)。

### 階段 5：知識沉澱與圖譜化歸檔 (ESign ➡️ KM)
* **觸發點 (Trigger)**：雙方完成簽署後，BreezySign Webhook 自動向 KM 發送完成通知。
* **API/CLI 呼叫**：
  * **CLI 指令**：`breezy-brain km extract --file /storage/contracts/deal_9987_signed.pdf --account-id <account_uuid>`
  * **API 端點**：`POST /api/v1/km/extract`
* **動作 (Action)**：地端服務將已簽署 PDF 自動歸檔，提取重要期日，並透過本地 embedding 模型向量化存入 ChromaDB，完成 `Graphify` 雙鏈知識關聯。

---

## 🛠️ 三、 CLI/API 自動化工作流編排範例

為了讓地端 IT 與自動化排程器 (如 CRON, Windows Task Scheduler) 能夠靈活調度系統，開發者可以使用以下 Shell 腳本，透過 CLI 介面串接整個生命週期：

```bash
#!/bin/bash
# BreezyBrain CLI 數據整合與自動化發送流程示範

# 1. 偵測地端網絡連線
NET_STATUS=$(breezy-brain system check-network)
echo "網路狀態偵測結果: $NET_STATUS"

# 2. 接收並同步名片
echo "正在匯入蒙恬名片數據..."
CRM_RESULT=$(breezy-brain crm sync-card --file ./raw_ocr_sample.json --auto-complete true)
DEAL_ID=$(echo $CRM_RESULT | jq -r '.deal_id')
ACCOUNT_ID=$(echo $CRM_RESULT | jq -r '.account_id')
echo "CRM 實體已建立。Deal ID: $DEAL_ID, Account ID: $ACCOUNT_ID"

# 3. 強制前端轉檔後的草案進入 BPM 審批流
echo "正在觸發 BPM 合約 AI 審核..."
BPM_TASK=$(breezy-brain bpm run --workflow-id wfl_contract_review --deal-id $DEAL_ID)
TASK_ID=$(echo $BPM_TASK | jq -r '.task_id')

# 4. 輪詢檢查任務狀態，處理 TTL 逾時
for i in {1..20}; do
  STATUS_JSON=$(breezy-brain task status --task-id $TASK_ID)
  TASK_STATUS=$(echo $STATUS_JSON | jq -r '.status')
  
  if [ "$TASK_STATUS" == "Success" ]; then
    echo "AI 審核通過！"
    break
  elif [ "$TASK_STATUS" == "Timeout_Failed" ] || [ "$TASK_STATUS" == "Error" ]; then
    echo "任務解析超時或出錯。正在手動嘗試重試..."
    breezy-brain task retry --task-id $TASK_ID
  fi
  sleep 15
done

# 5. 業務雙重確認防線，手動執行發送
echo "執行業務雙重確認並正式呼叫 BreezySign 送簽..."
breezy-brain clm dispatch --deal-id $DEAL_ID --template-id tpl_contract_2026_v4 --confidence-threshold 0.8
echo "電子合約已正式發送！"


---

## 🔗 二、 相關項目連結

- **產品核心定義**：[[breezy-brain-manifesto|BreezyBrain 好好腦產品宣言]]
- **研發落地路線圖**：[[breezy-brain-roadmap|BreezyBrain 四階段產品落地路線圖]]
- **好好簽 API 提案**：[[api-proposal-flow|好好簽 API 提案與報價工作流]]
