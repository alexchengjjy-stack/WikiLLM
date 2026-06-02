import os

sources_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\sources"

files = []
for root, dirs, filenames in os.walk(sources_dir):
    for f in filenames:
        if "report" in f.lower() or "analysis" in f.lower() or "pricing" in f.lower() or "bzs" in f.lower():
            files.append(f)

print("wiki/sources/ 下相關的已攝入檔案：")
for f in files:
    print(f"  - {f}")
