# -*- coding: utf-8 -*-
import os
import re
import sys

# 強制將標準輸出設為 utf-8，避免 cp950 編碼錯誤
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

outputs_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs"

files = {
    "v3": "20260528-1820-breezy-brain-architecture_v3.html",
    "v4": "20260529-0939-breezy-brain-architecture_v4.html",
    "v5": "20260529-1004-breezy-brain-architecture_v5.html"
}

def analyze_html(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 提取 title
    title = re.findall(r"<title>(.*?)</title>", content)
    title = title[0] if title else "No Title"
    
    # 提取 body 裡面的主要 div 結構
    body_content_match = re.search(r"<body>(.*?)</body>", content, re.DOTALL)
    body_content = body_content_match.group(1) if body_content_match else ""
    
    # 找尋包含的 class
    classes = set(re.findall(r'class=["\'](.*?)["\']', body_content))
    
    # 找尋 header 的內容
    header_match = re.search(r'<header.*?>(.*?)</header>', body_content, re.DOTALL)
    header_text = header_match.group(1).strip() if header_match else "No header"
    header_clean = re.sub(r'<[^>]+>', ' ', header_text)
    header_clean = " ".join(header_clean.split())[:300]
    
    # 找尋主要容器
    containers = re.findall(r'<div class="container">(.*?)</div>', body_content, re.DOTALL)
    
    print(f"Title: {title}")
    print(f"Header preview: {header_clean}")
    print(f"Classes used: {sorted(list(classes))}")
    print(f"Containers found: {len(containers)}")
    
    # 列出主要的 layout 類別
    grid_matches = re.findall(r'class="[^"]*grid[^"]*"', body_content)
    flex_matches = re.findall(r'class="[^"]*flex[^"]*"', body_content)
    print(f"Grid matches: {len(grid_matches)}, Flex matches: {len(flex_matches)}")
    
    # 提取所有 card 或架構圖節點的標題
    card_titles = re.findall(r'<h[34].*?>(.*?)</h[34]>', body_content)
    # 清理 card titles 中的 html 標籤
    card_titles_clean = [re.sub(r'<[^>]+>', '', t).strip() for t in card_titles]
    print(f"Card/Node Titles ({len(card_titles_clean)}): {card_titles_clean[:15]}")
    
    # 另外提取 style 中的一些特別樣式
    style_match = re.search(r"<style>(.*?)</style>", content, re.DOTALL)
    if style_match:
        style_text = style_match.group(1)
        glow_effects = re.findall(r"\b[\w-]*glow[\w-]*\b|\b[\w-]*animation[\w-]*\b|\b[\w-]*shadow[\w-]*\b", style_text)
        print(f"Glow/Animation/Shadow classes in CSS: {set(glow_effects)}")

for ver, filename in files.items():
    path = os.path.join(outputs_dir, filename)
    if os.path.exists(path):
        print(f"\n=== Version: {ver} ({filename}) ===")
        analyze_html(path)
        print("-" * 50)
