---
title: "輸出檔案格式轉換 (HTML, PPTX & PDF)"
type: skill
category: tools
proficiency: expert
tags: [HTML, PPTX, PDF, 文件轉換, 簡報製作, python-pptx, Headless, 視覺化, 知識輸出, Native Shapes, 向量繪圖]
date_created: 2026-05-15
date_updated: 2026-06-10
related_projects: []
related_concepts: []
summary: "掌握使用大模型結合自動化程式將 Wiki 知識庫內容導出為企業級展示格式的專家級技能。包含互動架構圖、PPTX 原生幾何向量繪製，以及透過 Headless 瀏覽器無痛渲染高保真 PDF 的終極技術。"
---

# 輸出檔案格式轉換 (Document Output Formats & Visual Asset Generation)

> **核心目標**：將 Markdown 格式的「第二大腦」知識網絡，轉譯為適合外部會議、高階長官（CEO, CTO, CMO）討論展示，或具備動態互動感的網頁與簡報。

---

## 1. HTML 網頁與互動式架構圖導出 (HTML & Interactive Diagram Export)

當需要展示複雜的系統架構（例如 BreezyBrain 的六大支柱與 AI 大腦流向）時，除靜態圖片外，**互動式 HTML 架構圖**能提供最佳的體驗。

### 🎨 互動式 HTML 架構圖美學規範
*   **深色科技感主題 (Dark Space Theme)**：使用 `#0A192F`（深藍色）或 `#0F172A`（Slate 深灰）作為背景，文字使用白色 `#FFFFFF`。
*   **玻璃擬態面板 (Glassmorphism)**：使用 `backdrop-filter: blur(10px)` 與半透明邊框（`rgba(255,255,255,0.1)`），營造現代 UI 質感。
*   **霓虹發光邊框 (Neon Glowing Borders)**：針對不同系統採用發光陰影（`box-shadow: 0 0 15px var(--glow-color)`），例如：
    *   `--glow-cyan` (RGB: 56, 189, 248) ➡️ 技術、BPM、BCR 模組。
    *   `--glow-green` (RGB: 74, 222, 128) ➡️ 協作、CLM 模組。
    *   `--glow-orange` (RGB: 251, 146, 60) ➡️ 電子簽章、BreezySign 模組。
*   **動態 SVG 箭頭**：跨系統的聯動（如 `call BZS API`）使用 SVG `<path>` 搭配 CSS 動態虛線流動動畫（`stroke-dasharray`）。

### 🛠️ 代碼生成 Prompt 範本
可向 Agent 發出以下指令以快速繪製：
> 「請為我使用單一 HTML 檔案生成一個互動式的系統架構圖，寬度自適應。背景採用深藍色科技風，六個主要組件以 CSS 玻璃擬態卡片呈現，並帶有對應的霓虹陰影。使用 SVG 繪製組件間的關聯箭頭，當滑鼠懸停在卡片上時，卡片應有微幅放大與發光加強的動態效果。」

---

## 2. 程式化 PPTX 商業簡報生成 (Programmatic PPTX Generation)

用於向企業長官（CEO、CTO、CMO）進行正式提案時，手動調整 PPTX 排版低效且容易出錯。透過 Python `python-pptx` 程式庫，可快速生成具備一致排版與配色的商業簡報。

### 📐 投影片排版與配色原則
*   **比例規範**：統一採用 **16:9 寬螢幕**（寬 13.33 英寸，高 7.5 英寸），避免 4:3 的陳舊感。
*   **配色一致性**：背景使用實心深藍色，標題使用亮天藍色，重點字與數值指標使用好好簽橘色或發光綠色，正文使用白色。
*   **排版安全區**：標題框固定於 `(0.6, 0.4, 12.13, 0.8)` 吋，內容框固定於 `(0.6, 1.3, 12.13, 5.6)` 吋，防止文字溢出與重疊。

### 🐍 核心 Python 代碼腳本結構
當需要批量生成簡報時，可執行以下腳本：

```python
# -*- coding: utf-8 -*-
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

# 1. 初始化 16:9 簡報
prs = Presentation()
prs.slide_width = Inches(13.33)
prs.slide_height = Inches(7.5)

# 2. 定義科技配色
COLOR_BG = RGBColor(10, 25, 47)      # 深藍背景
COLOR_CYAN = RGBColor(56, 189, 248)  # 霓虹藍（標題）
COLOR_WHITE = RGBColor(255, 255, 255)# 正文白

# 3. 建立空白幻燈片並設定背景
blank_layout = prs.slide_layouts[6]
slide = prs.slides.add_slide(blank_layout)
slide.background.fill.solid()
slide.background.fill.fore_color.rgb = COLOR_BG

# 4. 寫入標題與內容
title_box = slide.shapes.add_textbox(Inches(0.6), Inches(0.4), Inches(12.13), Inches(0.8))
title_box.text_frame.paragraphs[0].text = "投影片標題"
title_box.text_frame.paragraphs[0].font.name = 'Microsoft JhengHei'
title_box.text_frame.paragraphs[0].font.size = Pt(28)
title_box.text_frame.paragraphs[0].font.color.rgb = COLOR_CYAN

prs.save("outputs/output_presentation.pptx")
```

---

## 3. 💎 原生 PPT 幾何向量繪製 (Native PPTX Vector Shapes)

相對於插入靜態截圖，**原生幾何圖形 (Native Shapes)** 是架構圖產出的最高階技術。透過直接在 Python 腳本中計算座標、呼叫 PPTX 的幾何繪圖指令（例如 `shapes.add_shape`），可以「畫出」一個具有三大優勢的終極架構圖：

1.  **完美契合黃金比例**：透過矩陣計算直接繪製在畫布上，絕對不會有因為靜態圖片比例不對而遭裁切的問題。
2.  **無限解像度 (Infinite Resolution)**：這是向量繪圖，無論投放在多大的會議室螢幕上，邊緣永遠銳利不模糊。
3.  **全量可編輯性 (100% Editable)**：直接使用 PPT 的原生 `text_frame` 生成，因此長官可以隨時在 PowerPoint 軟體中直接點擊架構圖並修改內部文字！

### 🐍 核心繪製邏輯範例
```python
# 繪製一顆支援完整編輯的圓角矩形支柱
pillar = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
pillar.fill.solid()
pillar.fill.fore_color.rgb = RGBColor(0, 156, 223)

# 寫入可供高管事後編輯的文字
p_text = pillar.text_frame.paragraphs[0]
p_text.text = "可編輯的模組名稱"
p_text.font.bold = True
```

---

## 4. 📄 高保真 PDF 轉檔技術 (Headless Edge)

當需要產出供非技術人員或外部客戶傳閱的 PDF 文件（如 Blog 客戶案例）時，純 Python 轉檔套件（如 `xhtml2pdf`, `reportlab`）常會因 **Windows 底層字型讀取權限 (PermissionError)** 而導致轉檔崩潰或中文字體變黑方塊。

業界最高規且免安裝外部函式庫的解法，是利用系統內建的 **Headless 瀏覽器核心 (Edge / Chrome)** 進行自動化渲染：

1.  **無損排版與字型支援**：瀏覽器天生具備最完美的 CSS 與 TTF/TTC 字體渲染能力，絕不會發生字型遺失問題。
2.  **腳本呼叫範例**：先透過 `markdown` 模組將文字轉為 HTML 並包裝 CSS 後，呼叫 `subprocess` 進行列印。

```python
import subprocess
import os

# 尋找系統內的 Edge 或 Chrome 執行檔
browser_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
abs_html = os.path.abspath("outputs/source.html")
abs_pdf = os.path.abspath("outputs/result.pdf")

# 利用 Headless 模式無痛輸出 PDF
cmd = [
    browser_exe,
    "--headless",
    "--disable-gpu",
    "--run-all-compositor-stages-before-draw",
    f"--print-to-pdf={{abs_pdf}}",
    f"file:///{{abs_html}}"
]
subprocess.run(cmd, check=True)
```

---

## 5. 輸出路徑與資產存放規範

1.  **純靜態 HTML、PDF 與 互動網頁**：儲存於 [outputs/](../../outputs/) 資料夾，命名格式為 `[項目名稱]-landing-page.html` 或 `[項目名稱]_case_study.pdf`。
2.  **PPTX 簡報檔案**：儲存於 [outputs/](../../outputs/) 資料夾，命名格式為 `[項目名稱]_Internal_Proposal.pptx`（若有版本更新應加上 `_v2`, `_v3`）。
3.  **大模型日誌登錄**：每次生成新的 PPTX、HTML 或 PDF 資產後，必須在 `wiki/log.md` 登錄核心產出與路徑。

---

## 🔗 6. 實戰案例連結

*   **互動式 HTML 案例**：[20260515-si-article-landing-page.html](../../outputs/bzs/20260515-si-article-landing-page.html)
*   **自動化 PPTX 提案案例**：[BreezyBrain_PenPower_Edition_v3.pptx](../../outputs/bzb/BreezyBrain_PenPower_Edition_v3.pptx) (原生向量架構圖展現)
*   **Headless PDF 產出案例**：[breezysign-case-study-fuyou-travel.pdf](../../outputs/bzs/breezysign-case-study-fuyou-travel.pdf)

---

## 相關連結
- [其他文件轉為 Markdown (輸入技能)](markitdown-document-conversion.md)
- [系統整合 (SI) SEO 文章優化架構](../sources/bzs-si-article-structure.md)
- [BreezyBrain 產品定義宣言](../products/breezy-brain/breezy-brain-manifesto.md)

