import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

playbook_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\playbooks\esign-competitor-monitoring-mechanism.md"

if os.path.exists(playbook_path):
    with open(playbook_path, 'rb') as f:
        data = f.read()
    content = data.decode('utf-8', errors='ignore')
    print("--- esign-competitor-monitoring-mechanism.md CONTENT ---")
    print(content)
else:
    print("SOP 檔案不存在！")
