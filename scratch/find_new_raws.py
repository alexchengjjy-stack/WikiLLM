import os
import re

base_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM\WikiLLM"
raw_dir = os.path.join(base_dir, "raw")
wiki_sources_dir = os.path.join(base_dir, "wiki", "sources")

# 1. 掃描 raw/ 目錄下的所有檔案
raw_files = set()
for root, dirs, files in os.walk(raw_dir):
    # 排除隱藏目錄
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    for f in files:
        if f.startswith('.') or f == 'README.md':
            continue
        full_path = os.path.join(root, f)
        # 取得相對於 base_dir 的路徑，並統一使用斜線 '/'
        rel_path = os.path.relpath(full_path, base_dir).replace('\\', '/')
        raw_files.add(rel_path)

# 2. 掃描 wiki/sources 下已攝入的 source_file
ingested_files = set()
source_file_pattern = re.compile(r'^source_file:\s*["\']?([^"\']+)["\']?', re.MULTILINE)

if os.path.exists(wiki_sources_dir):
    for root, dirs, files in os.walk(wiki_sources_dir):
        for f in files:
            if not f.endswith('.md'):
                continue
            full_path = os.path.join(root, f)
            with open(full_path, 'r', encoding='utf-8', errors='ignore') as file_obj:
                content = file_obj.read()
                # 簡單正則表達式尋找 YAML 中的 source_file
                match = source_file_pattern.search(content)
                if match:
                    source_path = match.group(1).strip()
                    # 統一使用斜線
                    source_path = source_path.replace('\\', '/')
                    ingested_files.add(source_path)

# 3. 找出未被攝入的 raw 檔案
new_files = sorted(list(raw_files - ingested_files))

print(f"Total raw files found: {len(raw_files)}")
print(f"Total ingested files referenced: {len(ingested_files)}")
print(f"\nNew/Un-ingested files ({len(new_files)}):")
for nf in new_files:
    print(f"- {nf}")
