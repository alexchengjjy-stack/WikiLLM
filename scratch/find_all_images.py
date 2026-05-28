# -*- coding: utf-8 -*-
import urllib.request
import re
import os
import ssl

def find_all_images():
    url = "https://www.breezysign.com/"
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
        
        print("Extracting all static assets (img tags, sources, backgrounds, hrefs)...")
        
        # 1. 尋找所有 src 屬性
        srcs = re.findall(r'src="([^"]+)"', html)
        # 2. 尋找所有 href 屬性
        hrefs = re.findall(r'href="([^"]+)"', html)
        # 3. 尋找 url(...) CSS 引用
        css_urls = re.findall(r'url\([\'"]?([^\'"\)]+)[\'"]?\)', html)
        
        all_assets = set(srcs + hrefs + css_urls)
        print(f"Found {len(all_assets)} unique assets.")
        
        # 篩選出可能的圖案資產
        img_assets = []
        for asset in all_assets:
            lower_asset = asset.lower()
            if any(ext in lower_asset for ext in ['.svg', '.png', '.jpg', '.webp']):
                img_assets.append(asset)
                
        print("\n=== IMAGE & SVG ASSETS FOUND ===")
        for asset in sorted(img_assets):
            print(asset)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_all_images()
