import os
import glob

template_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs\templates\bzs-report-template.html"

print("--- 檢查範本中的 logo 引用 ---")
if os.path.exists(template_path):
    with open(template_path, 'rb') as f:
        data = f.read()
    content = data.decode('utf-8', errors='ignore')
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if "logo" in line.lower() or "img" in line.lower():
            display_line = line
            if len(display_line) > 150:
                display_line = display_line[:150] + "... (truncated)"
            print(f"範本第 {i+1} 行: {display_line}")
else:
    print("範本不存在！")

# 尋找 scratch 中的相關腳本
scratch_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch"
py_files = glob.glob(os.path.join(scratch_dir, "*.py"))
print("\n--- 搜尋 scratch 中的 python 腳本內容 ---")
for py_file in py_files:
    with open(py_file, 'rb') as f:
        data = f.read()
    content = data.decode('utf-8', errors='ignore')
    # 我們搜尋是否有將 Markdown 轉 HTML 或是替換 logo 或是生成 HTML 的腳本
    if "bzs-logo" in content or "logo-area" in content or "esign-monitoring-snapshot" in content:
        print(f"找到可能相關的腳本: {os.path.basename(py_file)}")
