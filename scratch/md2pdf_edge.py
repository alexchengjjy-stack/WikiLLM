import os
import subprocess
import markdown
import sys

# 檔案路徑
input_md = "outputs/breezysign-case-study-fuyou-travel.md"
output_html = "outputs/breezysign-case-study-fuyou-travel.html"
output_pdf = "outputs/breezysign-case-study-fuyou-travel.pdf"

# 確保路徑存在
abs_html = os.path.abspath(output_html)
abs_pdf = os.path.abspath(output_pdf)

# 讀取 MD
with open(input_md, 'r', encoding='utf-8') as f:
    text = f.read()

# 轉換 MD 為 HTML
html_content = markdown.markdown(text, extensions=['extra', 'codehilite'])

# 套用美觀的 CSS 排版
full_html = f"""
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <title>富友旅行社 成功案例</title>
    <style>
        body {{
            font-family: "Microsoft JhengHei", "Segoe UI", Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 40px;
            background-color: #fff;
        }}
        h1 {{
            color: #009CDF; /* 蒙恬/好好簽藍色 */
            border-bottom: 2px solid #009CDF;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #2c3e50;
            margin-top: 30px;
        }}
        p {{
            margin-bottom: 20px;
            font-size: 16px;
        }}
        strong {{
            color: #fb923c; /* 橘色強調 */
        }}
        blockquote {{
            border-left: 5px solid #009CDF;
            background-color: #f8fafc;
            padding: 15px 20px;
            margin: 20px 0;
            font-style: italic;
        }}
        ul {{
            margin-bottom: 20px;
        }}
        li {{
            margin-bottom: 10px;
        }}
    </style>
</head>
<body>
    {html_content}
</body>
</html>
"""

# 寫入 HTML
with open(output_html, 'w', encoding='utf-8') as f:
    f.write(full_html)

# 尋找 Edge 執行檔
edge_paths = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe" # 備用 Chrome
]

browser_exe = None
for path in edge_paths:
    if os.path.exists(path):
        browser_exe = path
        break

if not browser_exe:
    print("找不到 Edge 或 Chrome 瀏覽器，無法自動轉 PDF。")
    sys.exit(1)

# 執行 Headless 轉換
print(f"Using browser: {browser_exe}")
cmd = [
    browser_exe,
    "--headless",
    "--disable-gpu",
    "--run-all-compositor-stages-before-draw",
    f"--print-to-pdf={abs_pdf}",
    f"file:///{abs_html}"
]

print("Converting to PDF...")
subprocess.run(cmd, check=True)
print("PDF conversion completed successfully!")
