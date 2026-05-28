# -*- coding: utf-8 -*-
import os
import re
import subprocess
import markdown
import sys
import datetime

def compile_markdown_to_bzs_report(input_md_path, output_base_name, report_title, report_subtitle, report_no, plan_no):
    """
    將任意 Markdown 檔案轉換為 100% 完美套用 BreezySign 官方 HTML/PDF 報告品牌版型的通用編譯器。
    
    參數:
      input_md_path: 來源 Markdown 檔案路徑
      output_base_name: 輸出的檔案基底名稱 (例如 'bzs-website-seo-geo-analysis')
      report_title: 官方 Header 中要替換的 H1 主標題
      report_subtitle: 官方 Header 中要替換的副標題描述
      report_no: 報告編號 (例如 'BZS-SEO-20260527-01')
      plan_no: 計畫/分析編號 (例如 'BZS-ANALYSIS-20260527-01')
    """
    template_html = r"outputs/bzs-report-template.html"
    
    # 確保輸出目錄存在
    os.makedirs("outputs", exist_ok=True)
    
    # 1. 讀取 Markdown 內容
    if not os.path.exists(input_md_path):
        print(f"[ERROR] Markdown file not found at: {input_md_path}")
        return False
        
    with open(input_md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()
        
    # 移除 Markdown 中的 Frontmatter YAML，避免其直接渲染到 HTML 中
    md_text = re.sub(r'^---.*?---', '', md_text, flags=re.DOTALL)
    
    # 2. 讀取官方 HTML 模板
    if not os.path.exists(template_html):
        print(f"[ERROR] BZS HTML template not found at: {template_html}")
        return False
        
    with open(template_html, 'r', encoding='utf-8') as f:
        template_text = f.read()
        
    # 3. 轉換 Markdown 為 HTML 元素
    html_content = markdown.markdown(md_text, extensions=['extra', 'codehilite', 'tables'])
    
    # 4. 產品與品牌版型自動化映射演算法 (將 MD 元素無縫對齊官方 CSS 標籤)
    # a. 將 <blockquote> 轉換為官方 `.highlight-box` 區塊
    html_content = html_content.replace('<blockquote>', '<div class="highlight-box">')
    html_content = html_content.replace('</blockquote>', '</div>')
    
    # b. 將 <table> 轉換為官方帶有橫向滾動與邊框的 `.table-responsive` 區塊
    html_content = html_content.replace('<table>', '<div class="table-responsive"><table>')
    html_content = html_content.replace('</table>', '</table></div>')
    
    # c. 智能切分 H2 大章節，並將其分別打包進精緻的官方 `.glass-card` 中，同時為 H2 套用 `.section-title`
    parts = html_content.split('<h2>')
    new_html_content = ""
    
    # 第一部分（通常是 H1 與前言），包裹進首張 glass-card 中以求排版整齊
    if parts[0].strip():
        clean_lead = re.sub(r'<h1>.*?</h1>', '', parts[0], flags=re.DOTALL)
        new_html_content += f'<div class="glass-card">{clean_lead}</div>'
        
    # 後續的每一個 H2 大章節
    for part in parts[1:]:
        if '</h2>' in part:
            title, body = part.split('</h2>', 1)
            new_html_content += f"""
            <div class="glass-card">
                <h2 class="section-title">{title}</h2>
                {body}
            </div>
            """
        else:
            new_html_content += part
            
    # 5. 動態擷取官方模板的 Header 與 Footer，完成拼接
    header_index = template_text.find('</header>') + len('</header>')
    footer_index = template_text.find('<footer>')
    
    header_part = template_text[:header_index]
    footer_part = template_text[footer_index:]
    
    # 修正 Header 部分的標題與副標題，完美套用官方字體與 Layout
    header_part = header_part.replace(
        '<title>BreezySign 好好簽 ． 專用商業簡報與技術報告模板</title>',
        f'<title>BreezySign 好好簽 ． {report_title}</title>'
    )
    header_part = header_part.replace(
        '<h1>BreezySign 官方報告專用高階商務模板</h1>',
        f'<h1>{report_title}</h1>'
    )
    header_part = header_part.replace(
        '<p class="subtitle">本模板專為蒙恬科技電子簽章市場與技術優化小組打造，完美收束 BreezySign 官方視覺識別系統，適用於技術 SEO/GEO 快照與商業提案演示。</p>',
        f'<p class="subtitle">{report_subtitle}</p>'
    )
    
    # 修正 Footer 部分，將其更新為本次計畫的專屬聲明
    footer_part = footer_part.replace(
        '<p>報告編號: BZS-TEMPLATE-20260526-01 | 蒙恬科技 (PenPower) 電子簽章市場與技術優化小組 ． 專用高階商務模板</p>',
        f'<p>報告編號: {report_no} | 蒙恬科技 (PenPower) 電子簽章市場與技術優化小組 ． 專用高階商務模板</p>'
    )
    
    # 6. 完成拼接
    full_html = header_part + new_html_content + footer_part
    
    # 7. 動態產生帶有時間戳記且防重複的檔名 (遵循使用者防覆蓋規則)
    now_str = datetime.datetime.now().strftime("%Y%m%d-%H%M")
    base_out_path = f"outputs/{now_str}-{output_base_name}"
    
    output_html = f"{base_out_path}.html"
    output_pdf = f"{base_out_path}.pdf"
    
    if os.path.exists(output_html) or os.path.exists(output_pdf):
        version = 1
        while True:
            test_html = f"{base_out_path}_v{version}.html"
            test_pdf = f"{base_out_path}_v{version}.pdf"
            if not (os.path.exists(test_html) or os.path.exists(test_pdf)):
                output_html = test_html
                output_pdf = test_pdf
                break
            version += 1
            
    abs_html = os.path.abspath(output_html)
    abs_pdf = os.path.abspath(output_pdf)
    
    # 寫入 HTML
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"[SUCCESS] HTML successfully compiled and written to: {abs_html}")
    
    # 8. 尋找 Edge/Chrome 執行檔進行 PDF 編譯
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
        print("[ERROR] Microsoft Edge or Google Chrome not found. Cannot export PDF.")
        return False
        
    cmd = [
        browser_exe,
        "--headless",
        "--disable-gpu",
        "--disable-software-rasterizer",
        "--disable-extensions",
        "--no-sandbox",
        "--print-to-pdf=" + abs_pdf,
        "--no-pdf-header-footer",
        "file:///" + abs_html.replace("\\", "/")
    ]
    
    print(f"Calling browser: {browser_exe} for headless PDF generation...")
    try:
        subprocess.run(cmd, check=True, timeout=40)
        print(f"[SUCCESS] PDF successfully compiled and written to: {abs_pdf}")
        print(f"File size: {os.path.getsize(abs_pdf)} bytes\n")
        
        return {
            "html": output_html,
            "pdf": output_pdf
        }
    except Exception as e:
        print(f"[ERROR] Failed to compile PDF: {e}")
        return False

if __name__ == "__main__":
    # 此為測試/可作為腳本手動運行入口，具體編譯邏輯由外部控制
    print("BreezySign Universal PDF Report Compiler Loaded.")
