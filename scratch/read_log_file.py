import os

file_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\log.md"

if os.path.exists(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    print("log.md 前 1000 個 bytes：")
    print(data[:1000].decode('utf-8', errors='ignore'))
else:
    print("log.md 不存在！")
