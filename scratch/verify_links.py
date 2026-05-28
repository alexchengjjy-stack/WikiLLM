import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

files_to_check = [
    r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\analyses\breezybrain-mvp-roadmap.md",
    r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\products\breezy-brain\Product-Spec.md"
]

link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

all_ok = True

for file_path in files_to_check:
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}", file=sys.stderr)
        all_ok = False
        continue
    
    print(f"Checking links in: {os.path.basename(file_path)}")
    base_dir = os.path.dirname(file_path)
    
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    
    matches = link_pattern.findall(content)
    for text, link in matches:
        # 忽略網路連結、錨點連結
        if link.startswith("http://") or link.startswith("https://") or link.startswith("#"):
            continue
        
        # 移除錨點
        path_only = link.split("#")[0]
        if not path_only:
            continue
            
        # 轉換為絕對路徑
        target_abs_path = os.path.normpath(os.path.join(base_dir, path_only))
        
        if not os.path.exists(target_abs_path):
            print(f"  [FAIL] Link '{text}' -> '{link}' (Resolved to: {target_abs_path}) does not exist.")
            all_ok = False
        else:
            # 成功日誌
            pass

if all_ok:
    print("All internal markdown links are VALID!")
else:
    print("Link checking FAILED. Some links are broken.", file=sys.stderr)
    sys.exit(1)
