import os
import subprocess
import sys

# 定義要轉換的 HTML 與 PDF 對照清單
targets = [
    {
        "html": r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs\esign-competitor-seo-geo-analysis-20260525.html",
        "pdf": r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs\esign-competitor-seo-geo-analysis-20260525.pdf"
    },
    {
        "html": r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs\esign-competitor-seo-geo-analysis.html",
        "pdf": r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs\esign-competitor-seo-geo-analysis.pdf"
    }
]

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge_path):
    print(f"Error: msedge.exe not found at {edge_path}")
    sys.exit(1)

for target in targets:
    abs_html = os.path.abspath(target["html"])
    abs_pdf = os.path.abspath(target["pdf"])
    
    url = "file:///" + abs_html.replace("\\", "/")
    
    cmd = [
        edge_path,
        "--headless",
        "--disable-gpu",
        "--disable-software-rasterizer",
        "--disable-extensions",
        "--no-sandbox",
        "--print-to-pdf=" + abs_pdf,
        "--no-pdf-header-footer",
        url
    ]
    
    print(f"Converting {os.path.basename(abs_html)} to PDF...")
    try:
        # 明確指定 encoding="utf-8" 並加入 30 秒 timeout 控制
        result = subprocess.run(cmd, capture_output=True, encoding="utf-8", timeout=30)
        if result.returncode == 0:
            print(f"  [SUCCESS] PDF successfully generated at: {abs_pdf}")
            print(f"  File size: {os.path.getsize(abs_pdf)} bytes")
        else:
            print(f"  [ERROR] Error generating PDF for {os.path.basename(abs_html)}: {result.stderr}")
    except subprocess.TimeoutExpired:
        print(f"  [ERROR] PDF conversion timed out (30s exceeded) for {os.path.basename(abs_html)}.")
        print("  Edge headless may be hung. Run 'Stop-Process -Name msedge -Force' in PowerShell.")
    except Exception as e:
        print(f"  [ERROR] An unexpected error occurred: {e}")

print("All conversion tasks completed.")
