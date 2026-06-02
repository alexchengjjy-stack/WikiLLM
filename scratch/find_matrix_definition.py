import os

files = [
    r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\analyses\esign\esign-monitoring-snapshot-202606.md",
    r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch\generate_competitor_snapshot_pdf.py",
    r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch\generate_competitor_snapshot_pptx.py"
]

for file in files:
    if os.path.exists(file):
        print(f"\n--- 檢查檔案: {os.path.basename(file)} ---")
        with open(file, 'rb') as f:
            data = f.read()
        content = data.decode('utf-8', errors='ignore')
        lines = content.split('\n')
        for idx, line in enumerate(lines):
            if "鼎新" in line or "113電簽0008" in line:
                print(f"第 {idx+1} 行: {line.strip()}")
    else:
        print(f"檔案不存在: {file}")
