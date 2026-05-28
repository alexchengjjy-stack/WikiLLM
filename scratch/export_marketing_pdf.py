import os
import subprocess
import markdown
import re

# 檔案路徑
file1 = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\analyses\bzs-saas-funnel-ltv-cac-report.md"
file2 = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\analyses\2026-h2-marketing-strategy-recommendations.md"

html_out = r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs\bzs-2026-marketing-strategy-and-funnel.html"
pdf_out = r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs\bzs-2026-marketing-strategy-and-funnel.pdf"

def strip_frontmatter(text):
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[2].strip()
    return text.strip()

with open(file1, "r", encoding="utf-8") as f:
    content1 = strip_frontmatter(f.read())

with open(file2, "r", encoding="utf-8") as f:
    content2 = strip_frontmatter(f.read())

# Combine contents with a page break
combined_md = content1 + "\n\n<div style='page-break-after: always;'></div>\n\n" + content2

# CSS Template for high fidelity export
html_template = """
<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Noto+Sans+TC:wght@300;400;500;700&family=Outfit:wght@400;600;800&display=swap');
body {
    font-family: 'Inter', 'Noto Sans TC', sans-serif;
    line-height: 1.8;
    color: #1e293b;
    max-width: 900px;
    margin: 0 auto;
    padding: 40px;
    background-color: #f8fafc;
}
h1, h2, h3 {
    font-family: 'Outfit', 'Noto Sans TC', sans-serif;
    color: #0f172a;
}
h1 {
    font-size: 2.2em;
    border-bottom: 2px solid #3b82f6;
    padding-bottom: 10px;
    margin-bottom: 20px;
    color: #1e3a8a;
}
h2 {
    font-size: 1.6em;
    margin-top: 40px;
    color: #1d4ed8;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 8px;
}
h3 {
    font-size: 1.3em;
    color: #2563eb;
    margin-top: 30px;
}
blockquote {
    border-left: 4px solid #3b82f6;
    background: #eff6ff;
    padding: 15px 20px;
    margin: 20px 0;
    border-radius: 0 8px 8px 0;
    color: #1e40af;
    font-weight: 500;
}
li {
    margin-bottom: 10px;
}
code {
    background: #e2e8f0;
    padding: 3px 6px;
    border-radius: 4px;
    font-family: 'Consolas', monospace;
    font-size: 0.9em;
    color: #b91c1c;
}
table {
    width: 100%;
    border-collapse: collapse;
    margin: 25px 0;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    background: white;
    border-radius: 8px;
    overflow: hidden;
}
th, td {
    padding: 15px;
    text-align: left;
    border-bottom: 1px solid #e2e8f0;
}
th {
    background-color: #f1f5f9;
    font-weight: 600;
    color: #334155;
}
.page-break {
    page-break-after: always;
}
@media print {
    body {
        background-color: white;
        padding: 0;
    }
    table {
        box-shadow: none;
        border: 1px solid #e2e8f0;
    }
}
</style>
</head>
<body>
{{content}}
</body>
</html>
"""

html_body = markdown.markdown(combined_md, extensions=['tables', 'fenced_code'])
final_html = html_template.replace("{{content}}", html_body)

with open(html_out, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"HTML saved to {html_out}")

try:
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    url = "file:///" + html_out.replace("\\", "/")
    
    # Run headless edge to print to pdf
    cmd = [
        edge_path,
        "--headless",
        "--disable-gpu",
        "--print-to-pdf=" + pdf_out,
        "--no-pdf-header-footer",
        url
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"PDF successfully generated at {pdf_out}")
    else:
        print(f"Error generating PDF: {result.stderr}")
except Exception as e:
    print(f"Exception during PDF generation: {e}")
