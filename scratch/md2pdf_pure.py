import os
import markdown
from xhtml2pdf import pisa

# 檔案路徑
input_md = "outputs/breezysign-case-study-fuyou-travel.md"
output_pdf = "outputs/breezysign-case-study-fuyou-travel.pdf"

# 讀取 MD
with open(input_md, 'r', encoding='utf-8') as f:
    text = f.read()

# 轉換 MD 為 HTML
html_content = markdown.markdown(text, extensions=['extra'])

# 使用 xhtml2pdf 支援的 CSS，並強制載入微軟正黑體解決中文問題
# 備註：xhtml2pdf 的 css 支援較為基礎，需使用特定寫法
full_html = f"""
<html>
<head>
    <meta charset="UTF-8">
    <style>
        @font-face {{
            font-family: 'msjh';
            src: url('C:/Windows/Fonts/kaiu.ttf');
        }}
        body {{
            font-family: 'msjh';
            font-size: 14px;
            color: #333333;
            line-height: 1.5;
        }}
        h1 {{
            color: #009CDF;
            font-size: 20px;
            padding-bottom: 5px;
            border-bottom: 1px solid #009CDF;
        }}
        h2 {{
            color: #2c3e50;
            font-size: 16px;
            margin-top: 15px;
        }}
        p {{
            margin-bottom: 10px;
        }}
        strong {{
            color: #fb923c;
        }}
        ul {{
            margin-bottom: 10px;
        }}
        li {{
            margin-bottom: 5px;
        }}
    </style>
</head>
<body>
    {html_content}
</body>
</html>
"""

# 寫入 PDF
print("Converting Markdown to PDF using pure Python (xhtml2pdf)...")
with open(output_pdf, "w+b") as result_file:
    pisa_status = pisa.CreatePDF(full_html, dest=result_file)

if pisa_status.err:
    print("PDF conversion failed with errors.")
else:
    print("PDF conversion completed successfully without using Edge!")
