import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

summary_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\sources\pm-breezysign-analytics-reports.md"

if os.path.exists(summary_path):
    with open(summary_path, 'rb') as f:
        data = f.read()
    content = data.decode('utf-8', errors='ignore')
    print("--- pm-breezysign-analytics-reports.md CONTENT ---")
    print(content)
else:
    print("已攝入摘要不存在！")
