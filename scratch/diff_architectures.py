# -*- coding: utf-8 -*-
import os
import sys
import difflib

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

outputs_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs"

files = {
    "v3": "20260528-1820-breezy-brain-architecture_v3.html",
    "v4": "20260529-0939-breezy-brain-architecture_v4.html",
    "v5": "20260529-1004-breezy-brain-architecture_v5.html"
}

def get_content(ver):
    path = os.path.join(outputs_dir, files[ver])
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

v3_content = get_content("v3")
v4_content = get_content("v4")
v5_content = get_content("v5")

# 1. 比較 V3 和 V4
print("=== Comparing v3 and v4 ===")
v3_lines = v3_content.splitlines()
v4_lines = v4_content.splitlines()
diff = list(difflib.unified_diff(v3_lines, v4_lines, fromfile="v3", tofile="v4", lineterm=""))
# 只打印前面 60 行有差異的部分
for line in diff[:60]:
    print(line)

# 2. 比較 V4 和 V5
print("\n=== Comparing v4 and v5 ===")
v5_lines = v5_content.splitlines()
diff2 = list(difflib.unified_diff(v4_lines, v5_lines, fromfile="v4", tofile="v5", lineterm=""))
for line in diff2[:60]:
    print(line)
