import os
import re
import urllib.request
import urllib.error

reports_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM\raw\BZSdata\PMBreezySign分析報表"
output_base_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch\all_images"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# 獲取所有 md 檔案
files = [f for f in os.listdir(reports_dir) if f.endswith('.md')]
files.sort()

print(f"找到 {len(files)} 個報表檔案。")

for filename in files:
    # 提取日期，例如 BreezySign分析報表 2025.10.02.md -> 2025.10.02
    date_match = re.search(r'\d{4}\.\d{2}\.\d{2}', filename)
    if not date_match:
        print(f"無法從檔案名稱提取日期: {filename}")
        continue
    report_date = date_match.group(0)
    
    filepath = os.path.join(reports_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取 ![](url) 中的 url
    urls = re.findall(r'!\[.*?\]\((https?://.*?)\)', content)
    if not urls:
        print(f"報表 {filename} 中未找到圖片連結。")
        continue
    
    print(f"\n處理報表 {filename} (日期: {report_date})，共找到 {len(urls)} 張圖片。")
    
    # 建立該日期的輸出目錄
    out_dir = os.path.join(output_base_dir, report_date)
    os.makedirs(out_dir, exist_ok=True)
    
    for i, url in enumerate(urls):
        img_name = f"img_{i+1}.png"
        img_path = os.path.join(out_dir, img_name)
        
        # 如果檔案已存在且大小大於 0，可跳過
        if os.path.exists(img_path) and os.path.getsize(img_path) > 0:
            print(f"  {img_name} 已存在，跳過。")
            continue
            
        print(f"  下載 {url} -> {img_name}...")
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as response:
                with open(img_path, 'wb') as img_file:
                    img_file.write(response.read())
            print(f"  成功下載 {img_name}")
        except urllib.error.HTTPError as e:
            print(f"  HTTP 錯誤 {e.code} ({img_name}): {e.reason}")
        except urllib.error.URLError as e:
            print(f"  URL 錯誤 ({img_name}): {e.reason}")
        except Exception as e:
            print(f"  下載失敗 ({img_name}): {e}")

print("\n所有下載任務結束。")
