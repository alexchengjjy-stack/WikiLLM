import os
import re

# 定義路徑
base_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM"
outputs_dir = os.path.join(base_dir, "outputs")
log_path = os.path.join(base_dir, "wiki", "log.md")

# 1. 搜集子目錄中的檔案列表，建立對照表
# mapping 格式: { "file_name": "sub_dir" }
file_to_subdir = {}
for sub in ["bzs", "bzb", "esign", "assets", "templates"]:
    sub_path = os.path.join(outputs_dir, sub)
    if os.path.exists(sub_path):
        for f in os.listdir(sub_path):
            if os.path.isfile(os.path.join(sub_path, f)):
                file_to_subdir[f] = sub

print(f"搜集到 {len(file_to_subdir)} 個已歸檔檔案。")

# 2. 讀取 log.md
with open(log_path, "r", encoding="utf-8") as file:
    content = file.read()

# 3. 替換連結
# 我們需要替換形如 outputs/filename 或是 outputs/filename 的字串
# 但不要替換本來就已經在子目錄中的 outputs/bzs/filename
# 另外要同時考慮 windows 絕對路徑 file:///c:/.../outputs/filename

replaced_count = 0

# 定義替換函數
def replacer(match):
    global replaced_count
    full_path = match.group(0)
    file_name = match.group(2)
    
    if file_name in file_to_subdir:
        sub = file_to_subdir[file_name]
        # 重建新路徑，保留前面的 outputs/ 或是 file:///.../outputs/
        prefix = match.group(1)
        new_path = f"{prefix}outputs/{sub}/{file_name}"
        replaced_count += 1
        return new_path
    else:
        return full_path

# Regex 匹配:
# group 1: (file:///.*outputs/ 或 outputs/) 且後方不接 bzs/, bzb/, esign/, assets/, templates/
# group 2: 檔名 (不含斜線)
pattern = re.compile(r"((?:file:///[^)\s]*/outputs/|outputs/))(?!(?:bzs|bzb|esign|assets|templates)/)([^)\s/]+\.[a-zA-Z0-9]+)")

new_content = pattern.sub(replacer, content)

# 4. 寫回 log.md
if replaced_count > 0:
    with open(log_path, "w", encoding="utf-8") as file:
        file.write(new_content)
    print(f"成功修正 log.md 中的 {replaced_count} 處失效連結。")
else:
    print("未在 log.md 中找到符合的舊連結。")
