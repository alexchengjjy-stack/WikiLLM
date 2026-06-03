# -*- coding: utf-8 -*-
import os
import re
import base64
import subprocess
import markdown
import sys
from datetime import datetime

def main():
    workspace_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM"
    wiki_dir = os.path.join(workspace_dir, "wiki")
    outputs_dir = os.path.join(workspace_dir, "outputs")
    
    # 確保 outputs/bzs 目錄存在
    os.makedirs(os.path.join(outputs_dir, "bzs"), exist_ok=True)
    
    # 輸入 MD 檔案路徑
    md_path = os.path.join(wiki_dir, "analyses", "esign", "esign-monitoring-snapshot-202606.md")
    if not os.path.exists(md_path):
        print(f"[ERROR] MD file not found at: {md_path}")
        sys.exit(1)
        
    # 讀取 MD
    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()
        text = text.lstrip('\ufeff')
        
    # 解析 YAML Frontmatter
    yaml_pattern = re.compile(r'^---\s*[\r\n]+(.*?)\r?\n---\s*[\r\n]+', re.DOTALL)
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

    # 轉換 Markdown 內容為 HTML
    html_body = markdown.markdown(body_text, extensions=['extra', 'toc', 'sane_lists'])
    
    # 獲取 Base64 Logo
    logo_path = os.path.join(outputs_dir, "assets", "bzs-logo-green.png")
    logo_base64 = ""
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as f:
            logo_base64 = base64.b64encode(f.read()).decode("utf-8")
            
    if logo_base64:
        logo_html = f'<img class="bzs-logo" src="data:image/png;base64,{logo_base64}" width="220" height="44" alt="BreezySign">'
    else:
        logo_html = '<div style="font-family:\'Outfit\', sans-serif; font-size:24px; font-weight:800; color:var(--primary);">BreezySign 好好簽</div>'

    # 定義時間戳記與檔名 (SOP 規範)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M")
    base_name = f"bzs-esign-monitoring-snapshot-202606-{timestamp}-v1"
    
    output_html_path = os.path.join(outputs_dir, "bzs", f"{base_name}.html")
    output_pdf_path = os.path.join(outputs_dir, "bzs", f"{base_name}.pdf")

    # 漂亮且合規的 HTML 封裝 (套用翠綠色系)
    full_html = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{metadata.get('title', '電子簽章能量登錄競品情報普查快照 (2026 年 6 月)')}</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;600;800&family=Noto+Sans+TC:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary: #057857; /* BreezySign 品牌翠綠色 */
            --primary-light: #ecfdf5;
            --primary-border: #a7f3d0;
            --secondary: #0284c7; /* Sky 輔助藍色 */
            --secondary-light: #e0f2fe;
            --dark-text: #0f172a;
            --light-text: #475569;
            --bg-color: #f8fafc;
            --card-bg: #ffffff;
            --border-color: #e2e8f0;
            --glass-bg: rgba(255, 255, 255, 0.85);
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Inter', 'Noto Sans TC', sans-serif;
            background-color: var(--bg-color);
            color: var(--light-text);
            line-height: 1.75;
            padding: 40px 30px;
            max-width: 960px;
            margin: 0 auto;
            position: relative;
            -webkit-print-color-adjust: exact;
            print-color-adjust: exact;
        }}

        /* Header Style */
        header {{
            margin-bottom: 40px;
            border-bottom: 3px solid var(--primary);
            padding-bottom: 24px;
            position: relative;
        }}

        .logo-area {{
            display: flex;
            align-items: center;
            margin-bottom: 15px;
            background: transparent;
        }}

        .meta-tag {{
            font-family: 'Outfit', sans-serif;
            font-size: 12px;
            font-weight: 700;
            color: var(--primary);
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 8px;
        }}

        h1 {{
            font-family: 'Outfit', 'Noto Sans TC', sans-serif;
            font-size: 28px;
            font-weight: 800;
            color: var(--dark-text);
            line-height: 1.3;
        }}

        .subtitle {{
            font-size: 15px;
            color: var(--light-text);
            margin-top: 10px;
            font-weight: 400;
        }}

        /* Markdown body styling */
        h2 {{
            font-family: 'Outfit', 'Noto Sans TC', sans-serif;
            font-size: 20px;
            color: var(--dark-text);
            margin-top: 35px;
            margin-bottom: 18px;
            border-left: 5px solid var(--primary);
            padding-left: 12px;
            page-break-after: avoid;
        }}

        h3 {{
            font-family: 'Outfit', 'Noto Sans TC', sans-serif;
            font-size: 16px;
            color: var(--secondary);
            margin-top: 25px;
            margin-bottom: 12px;
            page-break-after: avoid;
        }}

        p {{
            margin-bottom: 18px;
            text-align: justify;
            font-size: 14.5px;
        }}

        /* Strong style */
        strong {{
            color: var(--dark-text);
            font-weight: 600;
        }}

        /* Lists */
        ul, ol {{
            margin-bottom: 20px;
            padding-left: 20px;
        }}

        li {{
            margin-bottom: 8px;
            font-size: 14px;
        }}

        /* Quote boxes / blockquotes */
        blockquote {{
            border-left: 4px solid var(--primary);
            background-color: var(--primary-light);
            padding: 16px 20px;
            margin: 20px 0;
            border-radius: 0 8px 8px 0;
            color: #064e3b;
        }}
        
        blockquote p {{
            margin-bottom: 0;
            font-size: 13.5px;
        }}
        
        /* Alerts within blockquote style */
        blockquote strong {{
            color: var(--primary);
        }}

        /* Tables (Optimized for PDF) */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 25px 0;
            font-size: 13px;
            page-break-inside: avoid;
        }}

        th {{
            background-color: #f1f5f9;
            color: var(--dark-text);
            font-weight: 700;
            padding: 12px 14px;
            border: 1px solid var(--border-color);
            text-align: left;
        }}

        td {{
            padding: 12px 14px;
            border: 1px solid var(--border-color);
            color: var(--light-text);
            vertical-align: top;
            line-height: 1.6;
        }}

        tr:nth-child(even) td {{
            background-color: #f8fafc;
        }}

        hr {{
            border: 0;
            height: 1px;
            background: var(--border-color);
            margin: 30px 0;
        }}

        footer {{
            margin-top: 50px;
            padding-top: 20px;
            border-top: 1px solid var(--border-color);
            font-size: 11px;
            color: var(--light-text);
            text-align: center;
        }}

        /* Print formatting */
        @media print {{
            body {{
                background: #ffffff !important;
                color: #000000 !important;
                padding: 0 !important;
                font-size: 12px !important;
            }}
            h2, h3, table, blockquote {{
                page-break-inside: avoid !important;
            }}
            a {{
                text-decoration: none;
                color: inherit;
            }}
        }}
    </style>
</head>
<body>

<div class="container">
    <header>
        <div class="logo-area">
            {logo_html}
        </div>
        <div class="meta-tag">COMPETITIVE INTELLIGENCE SNAPSHOT ． {metadata.get('date_created', '2026-06-01')}</div>
        <h1>{metadata.get('title', '電子簽章能量登錄競品情報普查快照 (2026 年 6 月)')}</h1>
        <p class="subtitle">{metadata.get('summary', '')}</p>
    </header>

    <div class="doc-body">
        {html_body}
    </div>

    <footer>
        <p>報告版次: V1.0 | 產出時間: {datetime.now().strftime("%Y-%m-%d %H:%M")} | 營運單位: 好好簽 BreezySign 業務與技術整合小組</p>
        <p style="margin-top: 4px; font-size: 10px; color:#94a3b8;">本報告由自動化轉換引擎產生，並透過 Microsoft Edge Headless 進行封裝存證。好好簽正式 Production 官網為唯一比對基準。</p>
    </footer>
</div>

</body>
</html>
"""

    # 寫入 HTML
    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"[SUCCESS] HTML successfully written to: {output_html_path}")

    # 搜尋 Edge
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
        print("[ERROR] Microsoft Edge not found. Cannot convert to PDF.")
        sys.exit(1)

    # 執行 Edge Headless 轉檔
    cmd = [
        browser_exe,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={output_pdf_path}",
        "--no-pdf-header-footer",
        f"file:///{os.path.abspath(output_html_path)}"
    ]

    print("Converting HTML to PDF via Edge Headless...")
    try:
        subprocess.run(cmd, check=True)
        print(f"[SUCCESS] PDF successfully generated at: {output_pdf_path}")
        print(f"File size: {os.path.getsize(output_pdf_path)} bytes")
    except Exception as e:
        print(f"[ERROR] Failed to convert to PDF: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
