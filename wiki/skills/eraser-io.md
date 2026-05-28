---
title: "Eraser.io 架構圖繪製與 Diagram-as-Code"
type: skill
category: ai_tools
proficiency: advanced
tags: [架構圖, Diagram-as-Code, 技術文檔, 視覺設計]
date_created: 2026-05-28
date_updated: 2026-05-28
related_projects: []
related_concepts: []
summary: "使用 Eraser.io 進行技術架構圖設計與 Diagram-as-Code 代碼化繪圖技能。"
---

# Eraser.io 架構圖繪製與 Diagram-as-Code

> 本頁面記錄使用 Eraser.io 作為技術架構圖與流程圖輸出工具的技能規範。Eraser.io 專為開發者設計，結合了手動繪圖畫布與「圖表即程式碼 (Diagram-as-Code)」的雙重優勢，能夠高效產出具備高科技美感、結構清晰的架構圖。

---

## 核心要點
*   **Diagram-as-Code 雙軌編輯**：可用簡單的類 Markdown 語法定義節點、容器與連線關係，自動渲染成圖，並支援滑鼠直覺微調與手動補充。
*   **高質感科技美學**：內建「藍圖網格 (Blueprint Grid)」與「深色星雲 (Dark Nebula)」主題，具備霓虹發光漸層邊框，使技術架構圖具備 WOW 的第一印象。
*   **自動化圖示著色與對齊**：內建豐富的 AWS、GCP、Kubernetes、OpenAI、Anthropic 等科技標誌，在深色主題下能自動重新染色（Re-color），維持視覺色調統一。

---

## 詳細內容

### 1. 應用場景與實績
在 WikiLLM 與 BreezySign 專案中，Eraser.io 主要用於以下高階技術交付物的視覺化：
*   **WikiLLM Agent 系統架構圖**：例如 [wikillm_agent_framework.png](../outputs/wikillm_agent_framework.png)，清晰展現了 Raw Ingestion 到 Agent Engine（三層式架構）再到 Local Knowledge Base 的資料流向與協定。
*   **BreezyBrain 架構部署與防禦**：用於繪製 CLM、BPM 整合連動，以及 MCP 伺服器的多層護城河防禦拓撲圖。

### 2. Eraser.io 設計規範與最佳實踐
為了在專案文檔中維持高品質且一致的視覺風格，應遵守以下繪圖規範：

*   **背景與主題選擇**：
    *   偏好使用 **Blueprint**（深藍底＋淺藍網格）作為系統架構圖背景，傳達專業與系統化感。
    *   使用 **Dark**（純深藍偏黑）主題作為精緻流程圖或高階商業簡報插圖。
*   **層級容器 (Containers)**：
    *   使用嵌套容器（如 Applications、Core Engine、Infrastructure）來區分系統邊界與元件層級。
    *   保持容器左上角的標題層級（Container Labels）簡潔（如 `Top Layer`, `Middle Layer`），避免過度繁雜。
*   **連線與路由 (Routing)**：
    *   連線應設定為 **Rounded**（圓角折線），在多條線路交會與分流時利用箭頭引導，並維持元件間的呼吸安全距離。
    *   在線條上加註關鍵協定或傳輸模式（如 `IPC`, `mTLS`, `HTTPS`）。
*   **匯出格式**：
    *   統一匯出為高解析度、去背景或匹配背景之 PNG/SVG 格式，存放於專案的 `outputs/` 目錄中，並以 `kebab-case` 命名（例如 `wikillm-agent-framework.png`）。

---

## 相關連結
*   [文件輸出格式與版面配置規範](../skills/document-output-formats.md) ── 關於 HTML/PDF/PPTX 模板與 Logo 規範。
*   [BreezyBrain 產品需求規格書](../products/breezy-brain/Product-Spec.md) ── 系統架構圖的文字規格基礎。
