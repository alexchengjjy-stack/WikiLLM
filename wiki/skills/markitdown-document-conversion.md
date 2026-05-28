---
title: "其他文件轉為 Markdown 格式 (MarkItDown)"
type: skill
category: ai_tools
proficiency: intermediate
tags: [MarkItDown, Markdown, 文件轉換, RAG, 知識庫預處理, Python,微軟]
date_created: 2026-05-14
date_updated: 2026-05-14
related_projects: []
related_concepts: []
summary: "運用微軟開源工具 MarkItDown 將各類辦公室與多媒體檔案（PDF、Word、Excel、PPT、圖片、音訊）轉換為乾淨且適合大模型（LLM）提取解析的標準 Markdown 格式。"
---

# 其他文件轉為 Markdown 格式 (MarkItDown)

> **MarkItDown** 是由微軟（Microsoft）開源的強大 Python 庫與命令列工具（[GitHub 專案](https://github.com/microsoft/markitdown) / [MCP 版本](https://github.com/mcp/microsoft/markitdown)），專為大語言模型（LLM）的檢索增強生成（RAG）與底層知識庫攝入所設計。它能將結構混亂的多樣化檔案，高效轉譯為具備高度語意結構的純文字 Markdown。

---

## 🛠️ 支援轉換的檔案類型矩陣

MarkItDown 能處理極度廣泛的專有格式與多媒體媒介：

| 檔案類型 | 支援副檔名 | 轉換處理邏輯與輸出特色 |
|---------|----------|--------------------|
| **PDF 文件** | `.pdf` | 提取文字段落與基礎排版，支援表格重構，濾除無效頁首頁尾干擾。 |
| **Word 文書** | `.docx` | 完美保留 `H1~H6` 標題階層、粗體斜體、項目符號清單與內嵌超連結。 |
| **Excel 試算表** | `.xlsx` | 將多頁籤表格直譯為標準的 Markdown 表格格式，便於 LLM 建構對比矩陣。 |
| **PowerPoint 簡報** | `.pptx` | 逐頁拆解投影片標題與文字方塊，並提取演講者備忘錄（Speaker Notes）。 |
| **網頁存檔** | `.html` | 智慧濾除廣告、導覽列與側邊欄等雜訊，單一萃取核心內文區塊。 |
| **圖像與視覺** | `.jpg`, `.png` | 支援透過介接視覺模型（如 GPT-4o 視覺端點）進行圖片描述與 OCR 辨識輸出。 |
| **音訊轉錄** | `.mp3`, `.wav` | 介接語音識別端點產生逐字稿文字嵌入。 |

---

## 💻 快速安裝與 Python 實作指引

### 安裝套件
直接透過 `pip` 進行輕量化安裝：
```bash
pip install markitdown
```

### 基礎檔案轉換實作 (Python API)
將單一簡報或試算表轉換為乾淨的 Markdown 輸出字串：

```python
from markitdown import MarkItDown

# 初始化轉換器
md = MarkItDown()

# 轉換 Word 文件
result_docx = md.convert("raw/projects/enterprise_contract_v2.docx")
print(result_docx.text_content)

# 轉換帶有多個 Sheet 的 Excel 試算表
result_xlsx = md.convert("raw/BZSdata/pricing_matrix_2026.xlsx")
# 自動輸出標準 | 欄位 | 欄位 | 表格語法
print(result_xlsx.text_content)
```

### 結合視覺端點轉換圖片/掃描檔
若文件包含純掃描圖片或需解析視覺圖表，可傳入支援 ChatCompletion 介面的 LLM Client 進行智慧解析：

```python
from markitdown import MarkItDown
from openai import OpenAI

# 介接 OpenAI Client
client = OpenAI()
md = MarkItDown(llm_client=client, llm_model="gpt-4o")

# 自動呼叫視覺模型解析合約掃描檔或系統架構圖
result_image = md.convert("raw/projects/architecture_flow.png")
print(result_image.text_content)
```

---

## 🧠 在 WikiLLM 與 RAG 系統中的戰略價值

1. **消除資訊斷點**：過去 RAG 系統直接切分（Chunking）PDF 或 Word 檔案時，極易切碎表格欄位或混入頁尾流水號。透過 MarkItDown 轉譯為純淨 Markdown，可大幅提升向量檢索的語意連貫度。
2. **自動化攝入流水線（Ingestion Pipeline）**：未來新增至 `raw/` 目錄下的二進制或辦公室軟體檔案，Agent 可自動呼叫此技能批次轉檔，確保知識庫底層統一為標準化 `.md` 格式。

---

## ⚠️ 特殊處理：處理純圖片/掃描版投影片 (SOP)

在實戰中（如 BZS 戰略推案簡報），常會遇到 **「全圖片構成」** 的 PPTX 檔案。此類檔案底層無文字層，標準轉換會輸出無意義的圖片標記。

### 1. 識別特徵
- 轉檔後的 `.md` 檔案大小極小。
- 內容僅包含大量的 `![](PictureX.jpg)` 或 `<!-- Slide number: X -->` 標記。
- 呼叫 `python-pptx` 遍歷 Shapes 時，文字內容回傳為空。

### 3. 處置流程 (Fallback Strategy)
當偵測到上述特徵時，必須啟動 **「視覺還原模式」**：

1.  **提取媒體資源**：
    - 將 `.pptx` 改名為 `.zip` 並解壓縮。
    - 從 `ppt/media/` 目錄中提取所有投影片圖片（通常為 `.png` 或 `.jpg`）。
2.  **AI 視覺解析 (OCR & Contextual Synthesis)**：
    - 使用具備視覺能力的大模型（如 Gemini 1.5 Pro/Flash 或 GPT-4o）。
    - 逐張輸入圖片，要求模型：*「請讀取此投影片圖片內容，還原為結構化 Markdown，包含標題、內文、數據指標與重要備註。」*
3.  **結構化重組**：
    - 將各頁提取的內容彙整至 `wiki/sources/` 對應的來源頁面。
    - **強制規範**：文檔頂部需標註 `> 本文件為透過 LLM AI 視覺辨識技術提取之文字還原版`，以利後續人工校對。

### 4. 核心價值
確保知識庫不因「文件封閉性」而產生斷點，實現從視覺信號到語意知識的完整攝入。

---

## 🔗 相關資源與延伸閱讀

- [Microsoft MarkItDown GitHub Repository](https://github.com/microsoft/markitdown)
- [MCP (Model Context Protocol) 整合架構](https://github.com/mcp/microsoft/markitdown)
- [WikiLLM 新文件攝入 Runbook](../playbooks/wikillm-ingest-runbook.md)
- [AI 專案目錄結構設計規範](../analyses/antigravity-aipm-framework.md)
