# -*- coding: utf-8 -*-
import urllib.request
import os
import ssl

def download_group_svgs():
    base_url = "https://www.breezysign.com/"
    svg_files = [
        "Group37836.svg",
        "Group38213.svg",
        "Group%2040261.svg",
        "Group%209329.svg",
        "Group%209331.svg"
    ]
    
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    scratch_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch"
    
    for filename in svg_files:
        link = base_url + filename
        dest_filename = filename.replace("%20", "_")
        dest_path = os.path.join(scratch_dir, dest_filename)
        
        print(f"Downloading: {link} -> {dest_path}")
        try:
            req = urllib.request.Request(link, headers=headers)
            with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
                content = response.read().decode('utf-8')
            with open(dest_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  [SUCCESS] Saved. Size: {len(content)} chars.")
            # 印出前 300 個字元以供分析
            print(f"  Snippet: {content[:300]}...")
        except Exception as e:
            print(f"  [FAILED] {e}")

if __name__ == "__main__":
    download_group_svgs()
