import os

file_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\sources\breezysign-pricing.md"

if os.path.exists(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    content = data.decode('utf-8', errors='ignore')
    lines = content.split('\n')
    print("--- 1 to 42 lines ---")
    for i in range(min(42, len(lines))):
        print(f"{i+1:3d}: {lines[i]}")
else:
    print("檔案不存在！")
