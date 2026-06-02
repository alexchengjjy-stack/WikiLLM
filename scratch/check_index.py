import os

file_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\index.md"

if os.path.exists(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    content = data.decode('utf-8', errors='ignore')
    
    print("index.md 中包含 breezysign-pricing.md 的行：")
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if "breezysign-pricing.md" in line:
            print(f"第 {i+1} 行: {line}")
else:
    print("index.md 不存在！")
