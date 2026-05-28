import re

h1_file = r"raw/BZSdata/小匯整/BreezySign SaaS 2026H1.md"

with open(h1_file, 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        # 尋找可能跟週報日期、新訂閱、當週相關的行
        if "當週新訂閱" in line or "當週金額" in line or "當週客戶情況" in line or "SaaS 202" in line or "週報如下" in line:
            print(f"Line {i+1}: {line.strip()}")
