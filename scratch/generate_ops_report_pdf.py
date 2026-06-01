# -*- coding: utf-8 -*-
import os
import glob
import subprocess

def convert_html_to_pdf():
    outputs_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs\bzs"
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    
    if not os.path.exists(edge_path):
        print(f"[ERROR] msedge.exe not found at: {edge_path}")
        return False

    # 1. 尋找最新生成的 202605 營運報告 HTML 檔
    html_pattern = os.path.join(outputs_dir, "bzs-ops-report-*-v*.html")
    html_files = glob.glob(html_pattern)
    
    if not html_files:
        print("[ERROR] No HTML report files found matching the pattern.")
        return False
        
    # 依修改時間排序，拿最新的那一個
    html_files.sort(key=os.path.getmtime, reverse=True)
    latest_html = html_files[0]
    
    # 2. 定義對應的 PDF 檔名與路徑 (保持 timestamp 一致)
    pdf_filepath = latest_html.replace(".html", ".pdf")
    
    abs_html = os.path.abspath(latest_html)
    abs_pdf = os.path.abspath(pdf_filepath)
    url = "file:///" + abs_html.replace("\\", "/")

    cmd = [
        edge_path,
        "--headless",
        "--disable-gpu",
        "--disable-software-rasterizer",
        "--disable-extensions",
        "--no-sandbox",
        f"--print-to-pdf={abs_pdf}",
        "--no-pdf-header-footer",
        url
    ]

    print(f"Converting {os.path.basename(abs_html)} to PDF...")
    try:
        result = subprocess.run(cmd, capture_output=True, encoding="utf-8", timeout=30)
        if result.returncode == 0:
            print(f"[SUCCESS] PDF successfully generated at: {abs_pdf}")
            print(f"File size: {os.path.getsize(abs_pdf)} bytes")
            return True
        else:
            print(f"[ERROR] Edge headless failed with code {result.returncode}: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print("[ERROR] PDF conversion timed out (30s exceeded). Edge headless may be hung.")
        return False
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")
        return False

if __name__ == "__main__":
    convert_html_to_pdf()
