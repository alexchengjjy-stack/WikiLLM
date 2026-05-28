# -*- coding: utf-8 -*-
import os
import sys
import re

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

outputs_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs"

with open(os.path.join(outputs_dir, "20260528-1820-breezy-brain-architecture_v3.html"), "r", encoding="utf-8") as f:
    v3_content = f.read()

# 尋找所有 class 包含 workflow-arrow 的行
lines = v3_content.splitlines()
for idx, line in enumerate(lines):
    if "workflow-arrow" in line:
        print(f"Line {idx+1}: {line}")
        # 印出前後 3 行
        for j in range(max(0, idx-3), min(len(lines), idx+4)):
            print(f"  [{j+1}] {lines[j]}")
        print("-" * 40)
