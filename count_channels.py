import os, re
from collections import Counter

saas_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM\WikiLLM\raw\BZSdata\SaaS"
pattern = re.compile(r"-\u4f86\u6e90\u7ba1\u9053.+\uff1a(.*)")

daily = Counter()
for fname in sorted(os.listdir(saas_dir)):
    if not fname.endswith(".md") or "\u9031\u5831" in fname:
        continue
    with open(os.path.join(saas_dir, fname), encoding="utf-8", errors="ignore") as f:
        for line in f:
            m = pattern.search(line)
            if m:
                val = m.group(1).strip()
                daily[val if val else "(\u7a7a\u767d)"] += 1

total = sum(daily.values())
print(f"=== \u65e5\u5831\u4f86\u6e90\u7ba1\u9053\u7d71\u8a08\uff08\u5171 {total} \u7b46\uff09===")
for k, v in daily.most_common():
    print(f"  {v:3d}  {k}")
