import os
import subprocess
import sys

html_file = r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs\esign-heading-optimization-report.html"
pdf_file = r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs\esign-heading-optimization-report.pdf"

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
    "--print-to-pdf=" + abs_pdf,
    "--no-pdf-header-footer",
    url
]

print(f"Converting {os.path.basename(abs_html)} to PDF...")
result = subprocess.run(cmd, capture_output=True, encoding="utf-8")

if result.returncode == 0:
    print(f"[SUCCESS] PDF successfully generated at: {abs_pdf}")
    print(f"File size: {os.path.getsize(abs_pdf)} bytes")
else:
    print(f"[ERROR] Error generating PDF: {result.stderr}")
