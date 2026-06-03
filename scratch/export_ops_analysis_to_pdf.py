# -*- coding: utf-8 -*-
import os
import re
import sys
import subprocess
import markdown

def export_markdown_to_pdf():
    # 1. 定義路徑
    workspace_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM"
    input_md_path = os.path.join(workspace_dir, "wiki", "analyses", "bzs", "bzs-saas-ops-report-202605.md")
    
    # 讀取 Logo 並轉為 base64
    logo_path = os.path.join(workspace_dir, "outputs", "assets", "bzs-logo-green.png")
    logo_base64 = ""
    if os.path.exists(logo_path):
        import base64
        with open(logo_path, "rb") as f:
            logo_base64 = base64.b64encode(f.read()).decode("utf-8")
    else:
        print("[WARNING] bzs-logo-green.png not found for PDF report.")
    
    # 1.1 尋找最新 HTML 以對齊 timestamp 檔名
    import glob
    html_pattern = os.path.join(workspace_dir, "outputs", "bzs", "bzs-ops-report-*-v*.html")
    html_files = glob.glob(html_pattern)
    if not html_files:
        print("[ERROR] No HTML report files found. Cannot align timestamp.")
        return False
    html_files.sort(key=os.path.getmtime, reverse=True)
    latest_html = html_files[0]
    parts = os.path.basename(latest_html).split("-")
    timestamp = f"{parts[3]}-{parts[4]}" # 取得完整的 timestamp
    
    output_html_name = f"bzs-saas-ops-analysis-{timestamp}-v4.html"
    output_pdf_name = f"bzs-saas-ops-analysis-{timestamp}-v4.pdf"
    
    output_html_path = os.path.join(workspace_dir, "outputs", "bzs", output_html_name)
    output_pdf_path = os.path.join(workspace_dir, "outputs", "bzs", output_pdf_name)
    
    if not os.path.exists(input_md_path):
        print(f"[ERROR] Markdown file not found at: {input_md_path}")
        return False
        
    # 2. 讀取 Markdown 內容
    with open(input_md_path, "r", encoding="utf-8") as f:
        raw_content = f.read()
        
    try:
        formatted_time = f"{timestamp[:4]}-{timestamp[4:6]}-{timestamp[6:8]} {timestamp[9:11]}:{timestamp[11:13]}"
    except Exception:
        formatted_time = "2026-06-03 17:46"
        
    # 3. 解析 Frontmatter
    frontmatter = {}
    content_body = raw_content
    if raw_content.startswith("---"):
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n", raw_content, re.DOTALL)
        if match:
            frontmatter_text = match.group(1)
            content_body = raw_content[match.end():]
            # 簡易解析 YAML key-value
            for line in frontmatter_text.split("\n"):
                if ":" in line:
                    key, value = line.split(":", 1)
                    frontmatter[key.strip()] = value.strip().strip('"').strip("'")

    # 4. 轉換 Markdown 為 HTML
    # 啟用 extra 支援表格與代碼區，codehilite 支援語法高亮
    html_body = markdown.markdown(content_body, extensions=['extra', 'codehilite'])
    
    # 5. 構建精美的 CSS 樣式 (對齊 BreezySign 品牌色與高質感排版)
    # 使用品牌翠綠 (#057857) 與輔助天藍 (#0284c7)
    title = frontmatter.get("title", "BreezySign 好好簽 2026年5月營運分析報告")
    tags = frontmatter.get("tags", "[好好簽, SaaS營運, 營運月報, 2026-05]")
    date_updated = frontmatter.get("date_updated", "2026-06-03")
    summary = frontmatter.get("summary", "")
    
    full_html_content = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@300;400;500;600;700;800&family=Noto+Sans+TC:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary: #057857; /* 品牌翠綠色 */
            --primary-light: #ecfdf5;
            --primary-border: #a7f3d0;
            --secondary: #0284c7; /* 輔助藍色 */
            --secondary-light: #e0f2fe;
            --dark-text: #0f172a;
            --light-text: #475569;
            --border-color: #cbd5e1;
            --page-width: 820px;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Inter', 'Noto Sans TC', sans-serif;
            background-color: #ffffff;
            color: var(--light-text);
            line-height: 1.8;
            padding: 60px 50px;
            max-width: var(--page-width);
            margin: 0 auto;
            -webkit-print-color-adjust: exact;
            print-color-adjust: exact;
        }}

        /* 封面頁樣式 */
        .cover-page {{
            height: 980px; /* 大致對齊 A4 單頁高度 */
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 50px;
            page-break-after: always;
        }}

        .cover-header {{
            border-top: 6px solid var(--primary);
            padding-top: 30px;
        }}

        .cover-meta {{
            font-family: 'Outfit', sans-serif;
            font-size: 13px;
            font-weight: 700;
            color: var(--primary);
            letter-spacing: 3px;
            text-transform: uppercase;
            margin-bottom: 10px;
        }}

        .cover-title {{
            font-family: 'Outfit', 'Noto Sans TC', sans-serif;
            font-size: 38px;
            font-weight: 800;
            color: var(--dark-text);
            line-height: 1.3;
            margin-bottom: 20px;
        }}

        .cover-subtitle {{
            font-size: 18px;
            color: var(--light-text);
            font-weight: 400;
            margin-bottom: 40px;
        }}

        .cover-summary {{
            background-color: var(--primary-light);
            border-left: 5px solid var(--primary);
            padding: 24px;
            border-radius: 0 8px 8px 0;
            font-size: 15px;
            color: var(--dark-text);
            line-height: 1.7;
        }}

        .cover-footer {{
            font-size: 13px;
            color: #94a3b8;
            border-top: 1px solid #e2e8f0;
            padding-top: 20px;
        }}

        .cover-footer table {{
            width: 100%;
            border-collapse: collapse;
        }}

        .cover-footer td {{
            padding: 4px 0;
            border: none;
            font-size: 13px;
            color: #64748b;
        }}

        /* 內容頁樣式 */
        .content-container {{
            margin-top: 40px;
        }}

        h1 {{
            display: none; /* 隱藏本文中的 H1，因為封面已有大標題 */
        }}

        /* 每個 H2 設為新的一頁，維持 PDF 排版美觀 */
        h2 {{
            font-family: 'Outfit', 'Noto Sans TC', sans-serif;
            font-size: 22px;
            color: var(--dark-text);
            margin-top: 40px;
            margin-bottom: 20px;
            padding-bottom: 8px;
            border-bottom: 2px solid var(--primary);
            page-break-before: always;
        }}

        /* 第一個 H2 不需要強制換頁 */
        .content-container > h2:first-of-type {{
            page-break-before: avoid;
            margin-top: 10px;
        }}

        h3 {{
            font-family: 'Noto Sans TC', sans-serif;
            font-size: 16px;
            color: var(--dark-text);
            margin-top: 24px;
            margin-bottom: 12px;
            border-left: 4px solid var(--secondary);
            padding-left: 10px;
        }}

        p {{
            margin-bottom: 16px;
            font-size: 14.5px;
            text-align: justify;
        }}

        strong {{
            color: var(--dark-text);
            font-weight: 700;
        }}

        /* 列表樣式 */
        ul {{
            margin-bottom: 20px;
            padding-left: 20px;
        }}

        li {{
            margin-bottom: 8px;
            font-size: 14px;
            list-style-type: square;
        }}

        /* 引用塊樣式 (轉為 Alert Box) */
        blockquote {{
            background-color: var(--primary-light);
            border-left: 5px solid var(--primary);
            padding: 16px 20px;
            margin: 20px 0;
            border-radius: 0 6px 6px 0;
            font-style: normal;
            font-size: 14px;
            color: var(--dark-text);
        }}

        blockquote p {{
            margin-bottom: 0;
        }}

        /* 表格樣式 */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 13.5px;
            background: #ffffff;
            box-shadow: 0 1px 3px rgba(0,0,0,0.02);
        }}

        th, td {{
            padding: 10px 14px;
            border: 1px solid var(--border-color);
            text-align: left;
        }}

        th {{
            background-color: var(--primary-light);
            color: var(--primary);
            font-weight: 700;
        }}

        tr:nth-child(even) td {{
            background-color: #f8fafc;
        }}

        /* 分頁防斷裂 */
        .content-container table, blockquote, ul {{
            page-break-inside: avoid;
        }}

        /* 頁碼與頁尾 */
        footer {{
            margin-top: 60px;
            border-top: 1px solid #e2e8f0;
            padding-top: 20px;
            font-size: 11px;
            color: #94a3b8;
            text-align: center;
        }}

        /* 列印模式調優 */
        @media print {{
            body {{
                padding: 40px 30px;
                font-size: 12px;
            }}
            .cover-page {{
                height: 100%;
                page-break-after: always;
            }}
            h2 {{
                margin-top: 30px;
                font-size: 20px;
            }}
            p, li {{
                font-size: 13px;
            }}
        }}
    </style>
</head>
<body>

    <!-- 封面頁 -->
    <div class="cover-page">
        <div class="cover-header">
            <div class="logo-area" style="margin-bottom: 24px;">
                <img src="data:image/png;base64,{logo_base64}" width="220" height="44" alt="BreezySign">
            </div>
            <div class="cover-meta">BreezySign 好好簽 ． Monthly Operations Analysis</div>
            <h1 class="cover-title">2026 年 5 月營運月報<br><span style="font-size:26px; font-weight:600; color:var(--light-text);">業務與深度技術專案分析報告</span></h1>
            <div class="cover-subtitle">編譯自 WikiLLM 知識庫 ． 雙引擎財務勾稽與競品觀測</div>
            
            <div class="cover-summary">
                <strong>報告摘要：</strong><br>
                {summary}
            </div>
        </div>
        
        <div class="cover-footer">
            <table>
                <tr>
                    <td style="width:15%;"><strong>發布單位：</strong></td>
                    <td style="width:35%;">蒙恬科技 電子簽章業務與技術整合小組</td>
                    <td style="width:15%;"><strong>編譯日期：</strong></td>
                    <td style="width:35%;">{date_updated}</td>
                </tr>
                <tr>
                    <td><strong>文件版次：</strong></td>
                    <td>V4.0 (對齊 Dashboard 看板)</td>
                    <td><strong>檔案編號：</strong></td>
                    <td>BZS-OPS-202605-ANALYSIS-V4</td>
                </tr>
                <tr>
                    <td><strong>關鍵標籤：</strong></td>
                    <td colspan="3">{tags}</td>
                </tr>
            </table>
        </div>
    </div>

    <!-- 內容頁 -->
    <div class="content-container">
        {html_body}
    </div>

    <!-- 頁尾 -->
    <footer>
        <p>報告版次: V4.0 | 產出時間: {formatted_time} | 營運單位: 好好簽 BreezySign 業務與技術整合小組</p>
        <p style="margin-top: 4px; font-size: 10px;">本報告為內部機密文件，已通過 Edge Headless 進行高保真 PDF 封裝，禁止非授權散布。</p>
    </footer>

</body>
</html>
"""
    
    # 6. 寫入 HTML 檔案
    try:
        with open(output_html_path, "w", encoding="utf-8") as f:
            f.write(full_html_content)
        print(f"[SUCCESS] HTML analysis successfully generated at: {output_html_path}")
    except Exception as e:
        print(f"[ERROR] Failed to write HTML analysis: {e}")
        return False
        
    # 7. 尋找 Edge 執行檔
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
        print("[ERROR] Neither Edge nor Chrome found. Cannot export PDF.")
        return False
        
    # 8. 呼叫 Headless 瀏覽器轉成 PDF
    abs_html = os.path.abspath(output_html_path)
    abs_pdf = os.path.abspath(output_pdf_path)
    url = "file:///" + abs_html.replace("\\", "/")
    
    cmd = [
        browser_exe,
        "--headless",
        "--disable-gpu",
        "--disable-software-rasterizer",
        "--disable-extensions",
        "--no-sandbox",
        f"--print-to-pdf={abs_pdf}",
        "--no-pdf-header-footer",
        url
    ]
    
    print(f"Using browser: {browser_exe}")
    print(f"Converting HTML analysis to PDF...")
    try:
        result = subprocess.run(cmd, capture_output=True, encoding="utf-8", timeout=45)
        if result.returncode == 0:
            print(f"[SUCCESS] PDF analysis successfully generated at: {abs_pdf}")
            print(f"File size: {os.path.getsize(abs_pdf)} bytes")
            return True
        else:
            print(f"[ERROR] Browser headless failed with code {result.returncode}: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print("[ERROR] PDF conversion timed out (45s exceeded).")
        return False
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    export_markdown_to_pdf()
