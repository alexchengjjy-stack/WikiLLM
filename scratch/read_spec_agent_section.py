# -*- coding: utf-8 -*-
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

spec_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\products\breezy-brain\Product-Spec.md"

with open(spec_path, "r", encoding="utf-8", errors="replace") as f:
    lines = f.readlines()

# 讀取 3.4.1 之後的 100 行
print("=== Section 3.4.1 Content ===")
for line in lines[1509:1609]:
    print(line, end="")
