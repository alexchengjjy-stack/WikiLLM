import os
import subprocess
import sys

html_file = r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs\esign-monitoring-snapshot-202605.html"
pdf_file = r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs\esign-monitoring-snapshot-202605.pdf"

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge_path):
    print(f"Error: msedge.exe not found at {edge_path}")
    sys.exit(1)

abs_html = os.path.abspath(html_file)
abs_pdf = os.path.abspath(pdf_file)

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
    result = subprocess.run(cmd, capture_output=True, encoding="utf-8", timeout=30)
    if result.returncode == 0:
        print(f"[SUCCESS] PDF successfully generated at: {abs_pdf}")
        print(f"File size: {os.path.getsize(abs_pdf)} bytes")
    else:
        print(f"[ERROR] Error generating PDF: {result.stderr}")
except subprocess.TimeoutExpired:
    print(f"[ERROR] PDF generation timed out (30s exceeded). Edge headless may be hung or attempting to download external assets.")
    print("Please run 'Stop-Process -Name msedge -Force' in PowerShell to clear hung background processes.")
except Exception as e:
    print(f"[ERROR] An unexpected error occurred: {e}")
