# -*- coding: utf-8 -*-
import os
import glob
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# 1. 定義顏色 (對齊 BreezySign CIS)
C_PRIMARY = RGBColor(5, 120, 87)       # 翠綠 (Primary Emerald)
C_SECONDARY = RGBColor(2, 132, 199)   # 天藍 (Secondary Sky)
C_LBG = RGBColor(236, 253, 245)       # 極淺綠 (Light Background)
C_DARK = RGBColor(15, 23, 42)         # Slate 深藍灰 (Dark Text)
C_WHITE = RGBColor(255, 255, 255)
C_GRAY_LIGHT = RGBColor(241, 245, 249) # Table header background

def create_report_pptx():
    outputs_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs"
    template_path = os.path.join(outputs_dir, "templates", "bzs-presentation-template.pptx")
    
    if not os.path.exists(template_path):
        print(f"[ERROR] Template PPTX not found at: {template_path}")
        return False

    # 1. 尋找最新 HTML 以對齊 timestamp 檔名
    html_pattern = os.path.join(outputs_dir, "bzs", "bzs-ops-report-*-v*.html")
    html_files = glob.glob(html_pattern)
    if not html_files:
        print("[ERROR] No HTML report files found. Cannot align timestamp.")
        return False
        
    html_files.sort(key=os.path.getmtime, reverse=True)
    latest_html = html_files[0]
    parts = os.path.basename(latest_html).split("-")
    # parts: ['bzs', 'ops', 'report', '20260601', '1535', 'v3.html']
    timestamp = f"{parts[3]}-{parts[4]}" # 取得完整的 timestamp
    
    pptx_filename = f"bzs-ops-report-{timestamp}-v3.pptx"
    pptx_filepath = os.path.join(outputs_dir, "bzs", pptx_filename)

    # 2. 載入簡報 (保留格式與屬性)
    prs = Presentation(template_path)
    
    # 3. 刪除原模板簡報中所有的 mock slides (從後往前刪除)
    for i in range(len(prs.slides)-1, -1, -1):
        rId = prs.slides._sldIdLst[i].rId
        prs.part.drop_rel(rId)
        del prs.slides._sldIdLst[i]

    blank_layout = prs.slide_layouts[6] # Blank slide layout

    # Helper: 設定背景顏色
    def set_slide_bg(slide, color):
        slide.background.fill.solid()
        slide.background.fill.fore_color.rgb = color

    # Helper: 繪製圓角卡片
    def add_card(slide, left, top, width, height, bg_color, border_color):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1.5)
        return shape

    # Helper: 繪製實心矩形
    def add_rect(slide, left, top, width, height, color):
        shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = color
        shape.line.fill.background()
        return shape

    # Helper: 新增標準內容頁標頭 (CIS 線條與 Logo)
    def add_slide_header(slide, title_text):
        # 頂部翠綠線條
        add_rect(slide, 0, 0, Inches(13.33), Inches(0.15), C_PRIMARY)
        # 天藍輔助線
        add_rect(slide, 0, Inches(0.15), Inches(13.33), Inches(0.04), C_SECONDARY)
        
        # 標題文字區
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(8.5), Inches(0.8))
        tf = title_box.text_frame
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.name = 'Microsoft JhengHei'
        p.font.size = Pt(26)
        p.font.bold = True
        p.font.color.rgb = C_PRIMARY

        # 右上角置入官方 Logo
        logo_green_path = os.path.join(outputs_dir, "assets", "bzs-logo-green.png")
        if os.path.exists(logo_green_path):
            slide.shapes.add_picture(logo_green_path, Inches(10.5), Inches(0.38), width=Inches(2.0), height=Inches(0.4))
        return title_box

    # =========================================================
    # Slide 1: 封面頁 (Cover Slide)
    # =========================================================
    slide_cover = prs.slides.add_slide(blank_layout)
    set_slide_bg(slide_cover, C_PRIMARY)

    # 頂部天藍裝飾塊
    add_rect(slide_cover, Inches(0), Inches(0), Inches(13.33), Inches(0.2), C_SECONDARY)

    # 插入官方高保真反白 Logo
    logo_white_path = os.path.join(outputs_dir, "bzs-logo-white.png")
    if os.path.exists(logo_white_path):
        slide_cover.shapes.add_picture(logo_white_path, Inches(1.2), Inches(1.8), width=Inches(2.61), height=Inches(0.52))

    # 封面主標題
    title_box = slide_cover.shapes.add_textbox(Inches(1.2), Inches(3.0), Inches(11.0), Inches(3.5))
    tf = title_box.text_frame
    tf.word_wrap = True
    
    p1 = tf.paragraphs[0]
    p1.text = "BreezySign 好好簽"
    p1.font.name = 'Microsoft JhengHei'
    p1.font.size = Pt(54)
    p1.font.bold = True
    p1.font.color.rgb = C_WHITE
    
    p2 = tf.add_paragraph()
    p2.text = "2026 年 5 月營運月報與技術專案分析"
    p2.font.name = 'Microsoft JhengHei'
    p2.font.size = Pt(26)
    p2.font.bold = True
    p2.font.color.rgb = C_WHITE
    p2.space_before = Pt(15)

    p3 = tf.add_paragraph()
    p3.text = "蒙恬科技 ． 電子簽章業務與技術整合小組"
    p3.font.name = 'Microsoft JhengHei'
    p3.font.size = Pt(14)
    p3.font.color.rgb = RGBColor(200, 230, 215)
    p3.space_before = Pt(30)

    # =========================================================
    # Slide 2: 財務營收與新增獲客漏斗 (雙欄卡片)
    # =========================================================
    slide_financial = prs.slides.add_slide(blank_layout)
    set_slide_bg(slide_financial, C_WHITE)
    add_slide_header(slide_financial, "一、 2026年5月財務營收與獲客漏斗")

    # 左側卡片 (財務營收雙引擎)
    add_card(slide_financial, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.0), C_LBG, C_PRIMARY)
    left_box = slide_financial.shapes.add_textbox(Inches(1.1), Inches(1.7), Inches(5.0), Inches(4.6))
    tfl = left_box.text_frame
    tfl.word_wrap = True
    
    pl1 = tfl.paragraphs[0]
    pl1.text = "📊 實收總營收：NT$ 365,202"
    pl1.font.name = 'Microsoft JhengHei'
    pl1.font.size = Pt(20)
    pl1.font.bold = True
    pl1.font.color.rgb = C_PRIMARY
    
    pl_body = [
        "1. SaaS 實收：NT$ 84,080",
        "  - 新購業績：NT$ 73,200",
        "    (含太平洋旅行社大單 $60,000 + 9家新客新購 $13,200)",
        "  - 舊客自動續訂金流 (ARR)：NT$ 10,880",
        "2. 專案收入 (Vertical/API 分類)：NT$ 281,122",
        "  - 來自本月交付驗收之 API 串接與垂直領域客製化首期回報。"
    ]
    for item in pl_body:
        p = tfl.add_paragraph()
        p.text = item
        p.font.name = 'Microsoft JhengHei'
        p.font.size = Pt(13)
        p.font.color.rgb = C_DARK
        p.space_before = Pt(8)

    # 右側卡片 (獲客漏斗)
    add_card(slide_financial, Inches(6.9), Inches(1.5), Inches(5.6), Inches(5.0), RGBColor(240, 248, 255), C_SECONDARY)
    right_box = slide_financial.shapes.add_textbox(Inches(7.2), Inches(1.7), Inches(5.0), Inches(4.6))
    tfr = right_box.text_frame
    tfr.word_wrap = True
    
    pr1 = tfr.paragraphs[0]
    pr1.text = "🚀 新增註冊與獲客漏斗"
    pr1.font.name = 'Microsoft JhengHei'
    pr1.font.size = Pt(20)
    pr1.font.bold = True
    pr1.font.color.rgb = C_SECONDARY
    
    pr_body = [
        "1. 月新增註冊公司數：312 家",
        "2. Leads 電訪品質跟進：",
        "  - 當月累計電訪註冊客戶：30 家",
        "  - 表達「有興趣」：15 家 (轉換率高達 50%)",
        "  - 歸入「較高意願」：9 家，由業務專人持續輔導",
        "3. 體驗版測試中：合計 19 家仍在輔導中",
        "  - SaaS 體驗版 7 家，API/SI 方案 12 家"
    ]
    for item in pr_body:
        p = tfr.add_paragraph()
        p.text = item
        p.font.name = 'Microsoft JhengHei'
        p.font.size = Pt(13)
        p.font.color.rgb = C_DARK
        p.space_before = Pt(6)


    # =========================================================
    # Slide 3: 歷史營收與 MoM 趨勢 (表格)
    # =========================================================
    slide_trend = prs.slides.add_slide(blank_layout)
    set_slide_bg(slide_trend, C_WHITE)
    add_slide_header(slide_trend, "二、 2025.10 - 2026.05 SaaS 歷年實收與 MoM 趨勢")

    # 新增表格
    rows, cols = 9, 4
    left, top, width, height = Inches(0.8), Inches(1.5), Inches(11.73), Inches(4.7)
    table_shape = slide_trend.shapes.add_table(rows, cols, left, top, width, height)
    table = table_shape.table

    # 設定列寬
    table.columns[0].width = Inches(1.6)
    table.columns[1].width = Inches(2.2)
    table.columns[2].width = Inches(1.8)
    table.columns[3].width = Inches(6.13)

    # 表格資料
    table_data = [
        ["月份", "SaaS 實收營收", "付費公司數", "MoM 增減幅度 / 結構明細"],
        ["2025-10", "NT$ 64,014", "145 家", "基準月份 (企業 $35K | 專業 $27K)"],
        ["2025-11", "NT$ 114,880", "154 家", "+79.46% (↗) (企業 $78K | 專業 $34K)"],
        ["2025-12", "NT$ 181,440", "171 家", "+57.94% (↗) (企業 $134K | 專業 $46K)"],
        ["2026-01", "NT$ 161,586", "188 家", "-10.94% (↘) (企業 $129K | 專業 $26K)"],
        ["2026-02", "NT$ 129,310", "190 家", "-19.97% (↘) (企業 $97K | 專業 $26K)"],
        ["2026-03", "NT$ 134,903", "193 家", "+4.33% (↗) (企業 $98K | 專業 $29K)"],
        ["2026-04", "NT$ 194,779", "198 家", "+44.38% (↗) (企業 $142K | 專業 $34K)"],
        ["2026-05", "NT$ 84,080", "-", "-56.83% (↘)* (新購 $73K | 舊客 ARR $10K)"]
    ]

    for row_idx, row in enumerate(table_data):
        for col_idx, text in enumerate(row):
            cell = table.cell(row_idx, col_idx)
            cell.text = text
            p = cell.text_frame.paragraphs[0]
            p.font.name = 'Microsoft JhengHei'
            
            # 第一行表頭
            if row_idx == 0:
                cell.fill.solid()
                cell.fill.fore_color.rgb = C_SECONDARY
                p.font.bold = True
                p.font.size = Pt(13)
                p.font.color.rgb = C_WHITE
                p.alignment = PP_ALIGN.CENTER
            else:
                cell.fill.solid()
                cell.fill.fore_color.rgb = C_WHITE if row_idx % 2 != 0 else C_GRAY_LIGHT
                p.font.size = Pt(10.5)
                p.font.color.rgb = C_DARK
                if col_idx < 3:
                    p.alignment = PP_ALIGN.CENTER
                    if col_idx == 0:
                        p.font.bold = True
                else:
                    p.alignment = PP_ALIGN.LEFT
                    if "+" in text:
                        p.font.color.rgb = C_PRIMARY
                        p.font.bold = True
                    elif "-" in text and "MoM" not in text:
                        p.font.color.rgb = RGBColor(185, 28, 28)
                        p.font.bold = True

    # 底部註記文字
    note_box = slide_trend.shapes.add_textbox(Inches(0.8), Inches(6.3), Inches(11.73), Inches(0.5))
    tf_n = note_box.text_frame
    tf_n.word_wrap = True
    p_n = tf_n.paragraphs[0]
    p_n.text = "* 註：2026-05 SaaS 實收金流因大單（太平洋旅行社 $60K）合約於 6/1 生效扣款而呈技術性下降。若併計當月專案實收 NT$ 281,122，總實收高達 NT$ 365,202，總體實收 MoM 其實為 +87.49% 的強勁成長。"
    p_n.font.name = 'Microsoft JhengHei'
    p_n.font.size = Pt(9.5)
    p_n.font.italic = True
    p_n.font.color.rgb = RGBColor(100, 110, 120)

    # =========================================================
    # Slide 3: 重大專案與 API 串接進展 (表格)
    # =========================================================
    slide_projects = prs.slides.add_slide(blank_layout)
    set_slide_bg(slide_projects, C_WHITE)
    add_slide_header(slide_projects, "三、 重大專案里程碑與 API 串接進展")

    # 新增表格
    rows, cols = 6, 3
    left, top, width, height = Inches(0.8), Inches(1.6), Inches(11.73), Inches(4.6)
    table_shape = slide_projects.shapes.add_table(rows, cols, left, top, width, height)
    table = table_shape.table

    # 設定列寬
    table.columns[0].width = Inches(2.2)
    table.columns[1].width = Inches(3.2)
    table.columns[2].width = Inches(6.33)

    # 表格資料
    table_data = [
        ["客戶/專案名稱", "本月進展 / 里程碑", "技術串接與細節說明"],
        ["太平洋旅行社", "40人企業方案成交", "完成 UNIFY 範本權限配置，6/1 正式啟用開通。"],
        ["101 BPM 部署", "原始碼與文檔交付", "開通技術窗口 steven 帳號與 10 份憑證，提案 isHealth 偵測 API。"],
        ["鼎新 API 專案", "API 串接完成與調優", "串接完成。開啟連結時間由 60 秒調整為 15 分鐘以配合 AI 處理。"],
        ["聯合線上 udn", "串接完成進入測試", "API 串接完成，業務單位現正進行業務流程與簽署測試。"],
        ["福安職安 API", "專案報價與協議中", "專案報價 $12 萬，預估年簽 8K~10K，含 8000 份 AATL 憑證。"]
    ]

    for row_idx, row in enumerate(table_data):
        for col_idx, text in enumerate(row):
            cell = table.cell(row_idx, col_idx)
            cell.text = text
            p = cell.text_frame.paragraphs[0]
            p.font.name = 'Microsoft JhengHei'
            
            # 第一行表頭 (翠綠底白字)
            if row_idx == 0:
                cell.fill.solid()
                cell.fill.fore_color.rgb = C_PRIMARY
                p.font.bold = True
                p.font.size = Pt(14)
                p.font.color.rgb = C_WHITE
                p.alignment = PP_ALIGN.CENTER
            else:
                cell.fill.solid()
                cell.fill.fore_color.rgb = C_WHITE if row_idx % 2 != 0 else C_GRAY_LIGHT
                p.font.size = Pt(12)
                p.font.color.rgb = C_DARK
                if col_idx < 2:
                    p.alignment = PP_ALIGN.CENTER
                    p.font.bold = True
                else:
                    p.alignment = PP_ALIGN.LEFT


    # =========================================================
    # Slide 5: 競品轉單效應與大檔案憑證限制限制 (雙欄卡片)
    # =========================================================
    slide_churn = prs.slides.add_slide(blank_layout)
    set_slide_bg(slide_churn, C_WHITE)
    add_slide_header(slide_churn, "四、 點點簽轉單效應分析與大檔案憑證限制限制")

    # 左側卡片 (點點簽轉單效應)
    add_card(slide_churn, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.0), C_LBG, C_PRIMARY)
    left_box_c = slide_churn.shapes.add_textbox(Inches(1.1), Inches(1.7), Inches(5.0), Inches(4.6))
    tfl_c = left_box_c.text_frame
    tfl_c.word_wrap = True
    
    plc1 = tfl_c.paragraphs[0]
    plc1.text = "🔥 點點簽漲價與轉單效應分析"
    plc1.font.name = 'Microsoft JhengHei'
    plc1.font.size = Pt(20)
    plc1.font.bold = True
    plc1.font.color.rgb = C_PRIMARY
    
    plc_body = [
        "1. 點點簽改為「以件計費」：單份約 NT$45~50，面臨中大型用量客戶年租大漲 3-5 倍阻力。",
        "2. 轉單潮浮現：福安 (2萬份) 與太平洋旅行社 (2000份) 面臨巨大預算成本抗性，促使其移轉至好好簽。",
        "3. 定價核心優勢：好好簽「年約吃到飽」在中大用量企業市場具備壓倒性的性價比競爭優勢。"
    ]
    for item in plc_body:
        p = tfl_c.add_paragraph()
        p.text = item
        p.font.name = 'Microsoft JhengHei'
        p.font.size = Pt(13)
        p.font.color.rgb = C_DARK
        p.space_before = Pt(8)

    # 右側卡片 (聖美麗大檔案防線)
    add_card(slide_churn, Inches(6.9), Inches(1.5), Inches(5.6), Inches(5.0), RGBColor(254, 242, 242), RGBColor(239, 68, 68))
    right_box_c = slide_churn.shapes.add_textbox(Inches(7.2), Inches(1.7), Inches(5.0), Inches(4.6))
    tfr_c = right_box_c.text_frame
    tfr_c.word_wrap = True
    
    prc1 = tfr_c.paragraphs[0]
    prc1.text = "⚠️ 聖美麗健檢超大檔案限制結案"
    prc1.font.name = 'Microsoft JhengHei'
    prc1.font.size = Pt(20)
    prc1.font.bold = True
    prc1.font.color.rgb = RGBColor(185, 28, 28)
    
    prc_body = [
        "1. 聖美麗健康文件多為超大 PDF（單檔 > 10MB），好好簽考量現行架構在嵌入 AATL 數位憑證時易失敗。",
        "2. 技術與售後考量：為防範超載與技術支援成本極大化，我方主動予以婉拒年約。",
        "3. 後續動態：客戶已決定於 8/1 續約點點簽。",
        "4. 本案例確立我方未來「單檔 10MB 限額與 AATL 效能」之售前篩選防線。"
    ]
    for item in prc_body:
        p = tfr_c.add_paragraph()
        p.text = item
        p.font.name = 'Microsoft JhengHei'
        p.font.size = Pt(13)
        p.font.color.rgb = C_DARK
        p.space_before = Pt(8)


    # 4. 存檔 (考慮鎖定重試)
    try:
        prs.save(pptx_filepath)
        print(f"[SUCCESS] PPTX presentation generated at: {pptx_filepath}")
        print(f"File size: {os.path.getsize(pptx_filepath)} bytes")
        return True
    except PermissionError:
        print(f"[WARNING] {pptx_filename} is locked. Saving to alternates...")
        saved = False
        v = 2
        while not saved and v < 100:
            alt_path = pptx_filepath.replace(".pptx", f"_v{v}.pptx")
            try:
                prs.save(alt_path)
                print(f"[SUCCESS] PPTX successfully saved to: {alt_path}")
                saved = True
            except PermissionError:
                v += 1
        return saved
    except Exception as e:
        print(f"[ERROR] Failed to save PPTX: {e}")
        return False

if __name__ == "__main__":
    create_report_pptx()
