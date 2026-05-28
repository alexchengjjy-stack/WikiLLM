# -*- coding: utf-8 -*-
import urllib.request
import re
import os
import ssl

def fetch_logo():
    url = "https://www.breezysign.com/"
    print(f"Fetching website content from: {url}")
    
    # 忽略 SSL 憑證驗證 (防禦安全策略攔截)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
            html = response.read().decode('utf-8')
        
        print("Successfully fetched HTML. Scanning for SVGs...")
        
        # 尋找所有 SVG 標籤
        svgs = re.findall(r'<svg[^>]*>.*?</svg>', html, re.DOTALL)
        print(f"Found {len(svgs)} SVG tags in HTML.")
        
        for idx, svg in enumerate(svgs):
            # 檢查是否含有 BreezySign 或是相關路徑
            if "Breezy" in svg or "breezy" in svg or "path" in svg:
                print(f"\n--- SVG {idx} (Potential Logo) ---")
                print(svg[:500] + "...")
                
        # 尋找是否含有 .svg 圖片連結
        svg_links = re.findall(r'src="([^"]+\.svg)"', html)
        print(f"Found SVG asset links: {svg_links}")
        for link in svg_links:
            if not link.startswith("http"):
                link = url.rstrip("/") + "/" + link.lstrip("/")
            print(f"Fetching external SVG from: {link}")
            try:
                req_ext = urllib.request.Request(link, headers=headers)
                with urllib.request.urlopen(req_ext, context=ctx, timeout=5) as resp_ext:
                    ext_svg = resp_ext.read().decode('utf-8')
                print("External SVG Content (first 300 chars):")
                print(ext_svg[:300])
                # 寫入本地存檔
                filename = os.path.basename(link)
                save_path = os.path.join(r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch", filename)
                with open(save_path, "w", encoding="utf-8") as f:
                    f.write(ext_svg)
                print(f"Saved to {save_path}")
            except Exception as e_ext:
                print(f"Failed to fetch {link}: {e_ext}")
                
    except Exception as e:
        print(f"Error fetching main page: {e}")

if __name__ == "__main__":
    fetch_logo()
