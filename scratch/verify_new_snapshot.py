import os

html_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs\bzs\bzs-esign-monitoring-snapshot-202606-20260602-1306-v1.html"

if os.path.exists(html_path):
    with open(html_path, 'rb') as f:
        data = f.read()
    content = data.decode('utf-8', errors='ignore')
    
    # 檢查是否含有 img 標籤與 bzs-logo
    if "bzs-logo" in content and "data:image/png;base64" in content:
        print("[SUCCESS] 驗證成功！新生成的 HTML 檔案中含有 BreezySign 的圖片 logo 數據！")
        # 列印出那一行的前 150 個字元
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if "bzs-logo" in line:
                print(f"第 {i+1} 行: {line[:150]}... (truncated)")
    else:
        print("[ERROR] 驗證失敗：HTML 檔案中仍舊沒有找到 logo 的 Base64 數據！")
else:
    print(f"錯誤: 找不到檔案 {html_path}")
