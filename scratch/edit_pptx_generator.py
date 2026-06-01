# -*- coding: utf-8 -*-
import os

filepath = r"scratch/generate_ops_report_pptx.py"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 定義要插入的投影片代碼 (Slide 3: 歷史營收與 MoM 趨勢)
slide_trend_code = """    # =========================================================
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

"""

# 尋找 Slide 3 的插入位置：在 "Slide 3: 重大專案與 API 串接進展 (表格)" 之前
target_anchor = "    # =========================================================\n    # Slide 3: 重大專案與 API 串接進展 (表格)"

if target_anchor in content:
    # 進行替換，將新 Slide 3 插入，並把原本的 Slide 3 改為三、，Slide 4 改為四、...
    updated_content = content.replace(target_anchor, slide_trend_code + target_anchor)
    
    # 修改後續 Slide 的標題與註解編號
    updated_content = updated_content.replace(
        'add_slide_header(slide_projects, "二、 重大專案里程碑與 API 串接進展")',
        'add_slide_header(slide_projects, "三、 重大專案里程碑與 API 串接進展")'
    )
    updated_content = updated_content.replace(
        '# Slide 4: 競品轉單效應與大檔案憑證限制限制 (雙欄卡片)',
        '# Slide 5: 競品轉單效應與大檔案憑證限制限制 (雙欄卡片)'
    )
    updated_content = updated_content.replace(
        'add_slide_header(slide_churn, "三、 點點簽轉單效應分析與大檔案憑證限制限制")',
        'add_slide_header(slide_churn, "四、 點點簽轉單效應分析與大檔案憑證限制限制")'
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print("PPTX generator script updated successfully with historical trend slide!")
else:
    print("ERROR: Could not find Slide 3 anchor in PPTX script!")
