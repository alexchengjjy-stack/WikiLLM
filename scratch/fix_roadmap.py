import sys

sys.stdout.reconfigure(encoding='utf-8')
file_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\analyses\breezybrain-mvp-roadmap.md"

# 1. 讀取原檔案
with open(file_path, "r", encoding="utf-8", errors="replace") as f:
    lines = f.readlines()

# 2. 擷取原檔案前51行 (包含 title, 核心要點, 詳細內容第一章)
part1 = lines[:51]

# 3. 擷取詳細版的第三章內容 (從原檔案第55行到143行，即 lines[54:143])
# 原來第 54 行是 "將 BreezyBrain 的多### 3. 三大安全與流程..."
# 我們從 "### 3. 三大安全與流程維度之整體規格完善度評估" 開始 (lines[55]) 直到 lines[143] (即 3.3 底下的 PII Access Audit Log 的內容)
part3 = lines[55:143]

# 4. 準備正確的第二章 4-Phase Roadmap 內容
roadmap_content = """### 2. 四階段產品演進路線圖 (Product Roadmap)

基於 [BreezyBrain 產品演進路線圖](../products/breezy-brain/breezy-brain-roadmap.md) 的設計，BreezyBrain 的產品生命週期將分為以下四個主要演進階段：

*   **Phase 1: MVP Core (機制與基本功能階段) [進行中]**
    *   **核心目標**：完成 OCR 名片解析與 CRM 商機建立的機制，並建立基於 Antigravity AI Engine 的 WikiLLM 本地知識庫攝入系統。
    *   **關鍵指標**：商機聯絡人同步成功率 > 98%，大腦自動處理時間 < 3 秒。
*   **Phase 2: Auto-Sign (自動化簽署與即時通知)**
    *   **核心目標**：串接 BreezySign (好好簽) API 以實現合約自動發送與簽署，並導入 LINE / SMS 催簽與通知模組。
    *   **關鍵指標**：合約發送與簽署時間由小時級降至 10 分鐘以內，LINE 簽署引導覆蓋率 > 40%。
*   **Phase 3: AI-CoPilot (契約審查與工作流增強)**
    *   **核心目標**：在 BPM 工作流中導入 AI 輔助，提供 MS-Word / PDF 契約條款 AI 審核、自動合規標註與多部門並行審批路由。
    *   **關鍵指標**：合約人工核對時間縮減 70%，簽署流程出錯率降至 0%。
*   **Phase 4: Graphify-Enterprise (知識圖譜與企業整合)**
    *   **核心目標**：開發知識圖譜生成引擎 (Graphify Engine)，自動將企業契約、規章與專案資料庫轉換為 Graph 結構，提供大腦動態語義導航與全域智能檢索。
    *   **關鍵指標**：企業知識碎片化問題降低 90%，實現 ESign 與 KM 的深度閉環。

---

"""

# 5. 準備第三章的開頭與詳細評估內容
# part3[0] 應該是 "### 3. 三大安全與流程維度之整體規格完善度評估\n"
# 為了格式整齊，我們可以直接把 part3 串接起來
part3_text = "".join(part3)

# 6. 結尾相關連結與引用
related_links = """

## 相關連結
- [BreezyBrain 產品規格書](../products/breezy-brain/Product-Spec.md)
- [BreezyBrain 需求變更日誌](../products/breezy-brain/Product-Spec-CHANGELOG.md)

## 來源引用
- [Product-Spec.md](../products/breezy-brain/Product-Spec.md) — 2.8.6 規模與分層架構、3.1-3.2 技術與模型規格、3.5 MCP 伺服器防禦規格
"""

# 7. 組裝完整文件內容
new_content = "".join(part1) + roadmap_content + "### 3. 三大安全與流程維度之整體規格完善度評估\n\n" + part3_text.strip() + related_links

# 8. 寫回檔案
with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("File reconstructed successfully!")
