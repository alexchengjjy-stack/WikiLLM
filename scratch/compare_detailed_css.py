# -*- coding: utf-8 -*-
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

outputs_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs"

files = {
    "v3": "20260528-1820-breezy-brain-architecture_v3.html",
    "v4": "20260529-0939-breezy-brain-architecture_v4.html",
    "v5": "20260529-1004-breezy-brain-architecture_v5.html"
}

def extract_css(content):
    import re
    styles = re.findall(r"<style>(.*?)</style>", content, re.DOTALL)
    return styles[0].strip() if styles else ""

with open(os.path.join(outputs_dir, files["v3"]), "r", encoding="utf-8") as f:
    v3_css = extract_css(f.read())

with open(os.path.join(outputs_dir, files["v5"]), "r", encoding="utf-8") as f:
    v5_css = extract_css(f.read())

# 我們可以分別印出這兩個 CSS 的行數
print(f"V3 CSS length: {len(v3_css)} chars")
print(f"V5 CSS length: {len(v5_css)} chars")

# 我們將 V3 的 CSS 與 V5 的 CSS 寫入暫存檔案中做比對，或者印出主要類別
# 列出主要的 class 規則
def parse_rules(css_text):
    import re
    # 簡易規則解析： 類別名 { 內容 }
    rules = re.findall(r"([^{]+)\{([^}]+)\}", css_text)
    return {r[0].strip(): r[1].strip() for r in rules}

v3_rules = parse_rules(v3_css)
v5_rules = parse_rules(v5_css)

all_selectors = sorted(list(set(v3_rules.keys()) | set(v5_rules.keys())))
print(f"\nSelector comparison (V3 vs V5):")
for selector in all_selectors:
    if selector in v3_rules and selector in v5_rules:
        if v3_rules[selector] != v5_rules[selector]:
            print(f"\n[MODIFIED] {selector}:")
            print(f"  V3: {v3_rules[selector]}")
            print(f"  V5: {v5_rules[selector]}")
    elif selector in v3_rules:
        print(f"\n[ONLY IN V3] {selector}:")
        print(f"  V3: {v3_rules[selector]}")
    elif selector in v5_rules:
        print(f"\n[ONLY IN V5] {selector}:")
        print(f"  V5: {v5_rules[selector]}")
