import os
import re
import subprocess
import markdown
import sys

# 檔案路徑
input_md = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\products\breezy-brain\Product-Spec.md"
output_html = r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs\BreezyBrain-Product-Spec.html"
output_pdf = r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs\BreezyBrain-Product-Spec.pdf"

# 確保輸出目錄存在
os.makedirs(os.path.dirname(output_html), exist_ok=True)

# 讀取 MD
with open(input_md, 'r', encoding='utf-8') as f:
    text = f.read()

# 解析 YAML Frontmatter
yaml_pattern = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)
match = yaml_pattern.match(text)
metadata = {}
body_text = text

if match:
    yaml_text = match.group(1)
    body_text = text[match.end():]
    for line in yaml_text.split('\n'):
        if ':' in line:
            parts = line.split(':', 1)
            if len(parts) == 2:
                key, val = parts
                metadata[key.strip()] = val.strip().strip('"').strip("'")

# 轉換 Markdown 內容為 HTML (啟用 tables 等 extra 擴充功能)
html_body = markdown.markdown(body_text, extensions=['extra', 'toc', 'sane_lists'])

# 建立漂亮的 Doc Header
header_html = ""
if metadata:
    title = metadata.get('title', 'BreezyBrain 產品需求文件 (Product Spec)')
    version = metadata.get('version', 'v1.0.0')
    date_updated = metadata.get('date_updated', '2026-05-21')
    status = metadata.get('status', 'active')
    
    header_html = f"""
    <div class="doc-header">
        <h1 class="doc-title">{title}</h1>
        <div class="doc-meta">
            <span class="meta-item"><strong>版本：</strong> {version}</span>
            <span class="meta-item"><strong>更新日期：</strong> {date_updated}</span>
            <span class="meta-item"><strong>狀態：</strong> <span class="badge">{status}</span></span>
        </div>
    </div>
    """

# 組合完整 HTML 頁面，套用專業的 CSS 設計系統 (Inter / Outfit + 護城河主題藍橘色系)
full_html = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <title>{metadata.get('title', 'BreezyBrain Product Spec')}</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;600;800&display=swap');
        
        body {{
            font-family: 'Outfit', 'Inter', "Segoe UI", "Microsoft JhengHei", sans-serif;
            line-height: 1.75;
            color: #1e293b;
            max-width: 900px;
            margin: 0 auto;
            padding: 30px;
            background-color: #fff;
            font-size: 15px;
        }}
        
        /* 頁首樣式 */
        .doc-header {{
            border-bottom: 2px solid #009CDF;
            padding-bottom: 20px;
            margin-bottom: 45px;
        }}
        .doc-title {{
            font-size: 30px;
            font-weight: 800;
            color: #0f172a;
            margin: 0 0 15px 0;
            line-height: 1.25;
        }}
        .doc-meta {{
            font-size: 13.5px;
            color: #64748b;
            display: flex;
            gap: 25px;
        }}
        .meta-item strong {{
            color: #475569;
        }}
        .badge {{
            background-color: #e0f2fe;
            color: #0369a1;
            padding: 2px 8px;
            border-radius: 12px;
            font-weight: 600;
            font-size: 12px;
            text-transform: uppercase;
        }}

        /* 標題與分頁控管 */
        h1 {{
            font-size: 24px;
            color: #0f172a;
            margin-top: 45px;
            margin-bottom: 20px;
            border-bottom: 1px solid #e2e8f0;
            padding-bottom: 8px;
            page-break-before: always; /* 每個主章節自動換頁，讓 PDF 排版非常工整 */
        }}
        h1:first-of-type {{
            page-break-before: avoid; /* 第一個 h1 不換頁 */
        }}
        h2 {{
            font-size: 19px;
            color: #009CDF; /* 好好簽藍色 */
            margin-top: 35px;
            margin-bottom: 15px;
            page-break-inside: avoid;
        }}
        h3 {{
            font-size: 16px;
            color: #1e293b;
            margin-top: 25px;
            margin-bottom: 12px;
            page-break-inside: avoid;
        }}
        h4 {{
            font-size: 14.5px;
            color: #334155;
            margin-top: 20px;
            margin-bottom: 10px;
            page-break-inside: avoid;
        }}

        p {{
            margin-top: 0;
            margin-bottom: 18px;
            text-align: justify;
        }}
        
        strong {{
            color: #0f172a;
            font-weight: 600;
        }}
        
        /* 引用與提示框 */
        blockquote {{
            border-left: 4px solid #009CDF;
            background-color: #f0f9ff;
            padding: 15px 20px;
            margin: 20px 0;
            border-radius: 0 8px 8px 0;
            color: #0369a1;
            font-style: normal;
        }}
        blockquote p {{
            margin: 0;
        }}

        /* 清單 */
        ul, ol {{
            margin-top: 0;
            margin-bottom: 20px;
            padding-left: 24px;
        }}
        li {{
            margin-bottom: 8px;
        }}

        /* 表格優化 (適合 PDF 寬度) */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 25px 0;
            font-size: 13.5px;
            page-break-inside: avoid;
        }}
        th {{
            background-color: #f1f5f9;
            color: #1e293b;
            font-weight: 600;
            text-align: left;
            padding: 10px 12px;
            border: 1px solid #cbd5e1;
        }}
        td {{
            padding: 10px 12px;
            border: 1px solid #cbd5e1;
            color: #334155;
            vertical-align: top;
        }}
        tr:nth-child(even) {{
            background-color: #f8fafc;
        }}

        /* 程式碼與區塊 */
        pre {{
            background-color: #0f172a;
            color: #f8fafc;
            padding: 16px;
            border-radius: 8px;
            overflow-x: auto;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 12.5px;
            line-height: 1.5;
            margin: 20px 0;
            page-break-inside: avoid;
        }}
        code {{
            font-family: 'Consolas', 'Courier New', monospace;
            background-color: #f1f5f9;
            color: #e11d48;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 13px;
        }}
        pre code {{
            background-color: transparent;
            color: inherit;
            padding: 0;
            border-radius: 0;
            font-size: inherit;
        }}

        /* 圖表佔位與通用圖片 */
        img {{
            max-width: 100%;
            width: 100%; /* 撐滿容器寬度 */
            height: auto;
            border-radius: 8px;
            margin: 20px 0;
            display: block;
        }}

        /* 大圖換頁容器 */
        .page-break {{
            margin: 35px 0;
        }}

        /* 列印最佳化 */
        @media print {{
            body {{
                padding: 0;
                font-size: 13.5px;
            }}
            h1, h2, h3, h4, table, pre {{
                page-break-inside: avoid;
            }}
            a {{
                text-decoration: none;
                color: #1e293b;
            }}
            /* 強制大圖單獨分頁並滿版 */
            .page-break {{
                page-break-before: always !important;
                page-break-after: always !important;
                page-break-inside: avoid !important;
                margin: 0 !important;
                padding: 0 !important;
            }}
            .page-break img {{
                width: 100% !important;
                max-width: 100% !important;
                height: auto !important;
                border: none !important;
                box-shadow: none !important;
            }}
        }}
    </style>
</head>
<body>
    {header_html}
    {html_body}
</body>
</html>
"""

# 寫入 HTML 暫存檔
with open(output_html, 'w', encoding='utf-8') as f:
    f.write(full_html)

# 尋找系統中的 Edge / Chrome 執行檔
edge_paths = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe"
]

browser_exe = None
for path in edge_paths:
    if os.path.exists(path):
        browser_exe = path
        break

if not browser_exe:
    print("Error: 找不到 Microsoft Edge 或 Google Chrome 瀏覽器，無法自動轉 PDF。")
    sys.exit(1)

# 執行 Headless 轉換 PDF
abs_html = os.path.abspath(output_html)
abs_pdf = os.path.abspath(output_pdf)

cmd = [
    browser_exe,
    "--headless",
    "--disable-gpu",
    "--no-sandbox",
    "--run-all-compositor-stages-before-draw",
    f"--print-to-pdf={abs_pdf}",
    f"file:///{abs_html}"
]

print(f"正在使用瀏覽器: {browser_exe}")
print("正在將 Product-Spec.md 轉換為 PDF...")
try:
    subprocess.run(cmd, check=True)
    print(f"轉換成功！PDF 檔案已輸出至: {output_pdf}")
except Exception as e:
    print(f"轉換失敗，錯誤訊息: {e}")
    sys.exit(1)
