import os

file_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\sources\breezysign-pricing.md"

if os.path.exists(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    content = data.decode('utf-8', errors='ignore')
    lines = content.split('\n')
    print(f"總行數: {len(lines)}")
    print("--- 最後 50 行 ---")
    start = max(0, len(lines) - 50)
    for i in range(start, len(lines)):
        print(f"{i+1:3d}: {lines[i]}")
else:
    print("檔案不存在！")
