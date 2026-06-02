import os

scripts = [
    r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch\generate_competitor_snapshot_pdf.py",
    r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch\convert_snapshot_to_pdf.py",
    r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch\process_logo.py"
]

for script in scripts:
    if os.path.exists(script):
        print(f"\n======================================")
        print(f"腳本名稱: {os.path.basename(script)}")
        print(f"======================================")
        with open(script, 'rb') as f:
            data = f.read()
        content = data.decode('utf-8', errors='ignore')
        
        # 我們搜尋 template, html, logo 相關內容
        lines = content.split('\n')
        # 如果腳本不長，印出全部，否則印出含有關鍵字的行
        if len(lines) < 200:
            for idx, line in enumerate(lines):
                print(f"{idx+1:3d}: {line}")
        else:
            print(f"行數較多 ({len(lines)} 行)，過濾關鍵字：")
            for idx, line in enumerate(lines):
                if any(x in line.lower() for x in ["template", "html", "logo", "src", "bzs-", "img"]):
                    print(f"{idx+1:3d}: {line.strip()}")
    else:
        print(f"腳本不存在: {script}")
