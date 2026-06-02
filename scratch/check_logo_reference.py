import os

html_202606 = r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs\bzs\bzs-esign-monitoring-snapshot-202606-20260601-1842-v1.html"
html_202605 = r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs\bzs\esign-monitoring-snapshot-202605.html"

md_202606 = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\analyses\esign\esign-monitoring-snapshot-202606.md"
md_202605 = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\analyses\esign\esign-monitoring-snapshot-202605.md"

def scan_file_for_logo(path):
    if not os.path.exists(path):
        print(f"檔案不存在: {path}")
        return
    print(f"\n--- 掃描檔案 {os.path.basename(path)} ---")
    with open(path, 'rb') as f:
        data = f.read()
    content = data.decode('utf-8', errors='ignore')
    
    # 尋找 img 標籤或包含 logo 的行
    lines = content.split('\n')
    found = False
    for i, line in enumerate(lines):
        if "logo" in line.lower() or "img" in line.lower() or "src=" in line.lower():
            # 不要印出極長的 base64
            display_line = line
            if len(display_line) > 150:
                display_line = display_line[:150] + "... (truncated)"
            print(f"第 {i+1} 行: {display_line}")
            found = True
    if not found:
        print("未找到包含 logo, img, src 的行。")

scan_file_for_logo(html_202606)
scan_file_for_logo(html_202605)
scan_file_for_logo(md_202606)
scan_file_for_logo(md_202605)
