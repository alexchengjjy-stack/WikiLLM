import sys

sys.stdout.reconfigure(encoding='utf-8')

file_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\products\breezy-brain\Product-Spec.md"

try:
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()

    print(f"Original Line 202: {repr(lines[201])}")
    print(f"Original Line 204: {repr(lines[203])}")

    # 修改 Line 202 (第 202 行, 索引為 201)
    new_line_202 = (
        "*   **US 1.2 (非結構化解析)**：身為診所助理，我希望上傳一份紙本掃描的同意書後，"
        "系統能透過 Local LLM 的高精度 OCR 服務自動解析同意書內容，並將姓名、簽署日期等結構化欄位提取出來。\n\n"
        "### Epic 2: BCR 人脈與資料採集 (BCR & Data Ingestion)\n"
        "*   **US 2.1 (名片掃描與 OCR)**：身為銷售業務，我希望使用手機拍照或掃描儀上傳名片後，系統能串接 WorldCard Cloud 的 API 進行高精度名片解析。\n"
        "*   **US 2.2 (大腦資料清洗與補全)**：身為銷售業務，我希望當 OCR 解析出的資料有缺失時，大腦能自動清洗、修復並與政府工商登記資料比對，補齊稅號 (Tax ID) 等核心欄位，以維持客資的精準度。\n\n"
        "### Epic 3: 輕量企業級 BreezyCRM (BreezyCRM for Enterprise)\n"
        "*   **US 3.1 (多類型客資管理)**：身為銷售主管，我希望系統能將客戶區分為 SaaS 訂閱者 (SaaS Product)、零售經銷通路 (Retail Channel) 以及專案客製建置 (Project Custom) 等多種類型，以便針對不同業務特性進行精細化管理。\n"
        "*   **US 3.2 (自訂增強欄位)**：身為系統管理員，我希望系統預留動態擴充欄位空間（採用 JSONB 格式），讓我可以隨時於後台無代碼自訂客戶、聯絡人與商機的客製欄位，為未來的業務擴充和系統集成預留增強空間。\n\n"
        "#### 2.3.2 BreezyCRM 核心資料欄位 (Data Schema) & 預留客製化增強規格\n"
    )
    lines[201] = new_line_202

    # 修改 Line 204 (第 204 行, 索引為 203)
    new_line_204 = (
        "依據多通路銷售日報與客戶進件需求，BreezyCRM 分類管理 **SaaS 產品 (SaaS)**、**零售經銷通路 (Retail)** "
        "及 **專案客製工程 (Project)** 三種不同型態之客戶與商機。為了滿足極致的擴充性與「預留未來更新與增強的空間」，"
        "BreezyCRM 在 Accounts、Contacts 與 Deals 實體中均預留了 JSONB 格式的 `custom_fields` 動態擴充欄位。這使得系統在對接不同業務管道特有的客戶屬性"
        "或第三方系統 API（如名片 OCR 採集、經銷分潤、專案里程碑等）時，無須變更底層資料庫實體 Schema 即可完成無痛增強。BreezyCRM 主要維護以下三大實體：\n"
    )
    lines[203] = new_line_204

    # 寫回檔案
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(lines)
        
    print("Modification successful!")

except Exception as e:
    import traceback
    print("Error occurred:")
    print(traceback.format_exc())
