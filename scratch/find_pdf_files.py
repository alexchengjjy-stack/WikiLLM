import os

raw_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM\raw"

pdf_files = []
for root, dirs, filenames in os.walk(raw_dir):
    for f in filenames:
        if f.endswith(".pdf") and ("2026.06.02" in f or "20260602" in f):
            pdf_files.append(os.path.join(root, f))

print("找到的相關 PDF 檔案：")
for f in pdf_files:
    print(f"  - {os.path.relpath(f, raw_dir)}")
