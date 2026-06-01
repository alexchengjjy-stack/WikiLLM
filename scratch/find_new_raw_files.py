import os
import re
import sys

# 重新設定 stdout 編碼為 utf-8，解決 Windows 下的 cp950 錯誤
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def get_source_files_in_wiki(wiki_sources_dir):
    source_files = set()
    if not os.path.exists(wiki_sources_dir):
        return source_files
    
    # 讀取 wiki/sources 內所有 md 檔的 frontmatter
    for root, dirs, files in os.walk(wiki_sources_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    # 提取 YAML frontmatter
                    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
                    if match:
                        yaml_content = match.group(1)
                        # 用 regex 尋找 source_file: "..." 或 source_file: ...
                        sf_match = re.search(r'source_file:\s*["\']?(.*?)["\']?\s*$', yaml_content, re.MULTILINE)
                        if sf_match:
                            src = sf_match.group(1).strip()
                            # 統一使用正斜線 / 以便比對
                            src = src.replace('\\', '/')
                            source_files.add(src)
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    return source_files

def get_raw_files(raw_dir):
    raw_files = []
    if not os.path.exists(raw_dir):
        return raw_files
    
    for root, dirs, files in os.walk(raw_dir):
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, os.path.dirname(raw_dir))
                # 統一使用正斜線 /
                raw_files.append(rel_path.replace('\\', '/'))
    return raw_files

def main():
    workspace = r"c:\Users\alexc\OneDrive\文件\WikiLLM"
    raw_dir = os.path.join(workspace, "raw")
    wiki_sources_dir = os.path.join(workspace, "wiki", "sources")
    
    ingested_sources = get_source_files_in_wiki(wiki_sources_dir)
    all_raw_files = get_raw_files(raw_dir)
    
    print(f"Total raw files: {len(all_raw_files)}")
    print(f"Total ingested source files in wiki/sources: {len(ingested_sources)}")
    
    new_files = []
    for f in all_raw_files:
        # 排除 README.md
        if f.endswith('README.md'):
            continue
        # 比對是否在 ingested_sources 中
        if f not in ingested_sources:
            new_files.append(f)
            
    print(f"\n--- 未攝入的新檔案數量: {len(new_files)} ---")
    
    # 寫入文字檔
    out_path = os.path.join(workspace, "scratch", "new_raw_files.txt")
    with open(out_path, 'w', encoding='utf-8') as out_f:
        for nf in new_files:
            print(nf)
            out_f.write(nf + '\n')
            
    print(f"\n未攝入的檔案已寫入至: {out_path}")

if __name__ == "__main__":
    main()
