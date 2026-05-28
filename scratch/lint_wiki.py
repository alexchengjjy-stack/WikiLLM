import os
import re
import yaml

WIKI_DIR = r"C:\Users\alexc\OneDrive\文件\WikiLLM\wiki"
RAW_DIR = r"C:\Users\alexc\OneDrive\文件\WikiLLM\raw"

def get_all_md_files(directory):
    md_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files

def parse_md_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Parse frontmatter
    frontmatter = {}
    body = content
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                frontmatter = yaml.safe_load(parts[1])
            except Exception as e:
                frontmatter = {"error": f"Yaml parsing error: {e}"}
            body = parts[2]
            
    # Extract links like [text](path.md) or [text](path.md#header)
    # Ignore web urls starting with http/https
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    links = []
    import urllib.parse
    for match in link_pattern.finditer(body):
        text, url = match.groups()
        # Clean url (remove anchors or query params) and decode url-encoded characters like %20
        url_clean = urllib.parse.unquote(url.split('#')[0].split('?')[0])
        # Ignore web links, mailto, etc.
        if url_clean.startswith(('http://', 'https://', 'mailto:', 'tel:')):
            continue
        # Ignore local image attachments or pdfs (check if it's md or not, keep others for check)
        links.append((url_clean, url, text))
        
    return frontmatter, links, body

def main():
    md_files = get_all_md_files(WIKI_DIR)
    
    # Store results
    file_metadata = {}
    all_links = []
    
    # Map absolute paths to relative representation for display
    def to_rel(abs_path):
        return os.path.relpath(abs_path, WIKI_DIR).replace('\\', '/')

    for filepath in md_files:
        rel_path = to_rel(filepath)
        if rel_path == "lint_report.md":
            continue
        frontmatter, links, body = parse_md_file(filepath)
        file_metadata[rel_path] = {
            "abs_path": filepath,
            "frontmatter": frontmatter,
            "links": links,
            "incoming_links": []
        }
        
    broken_links = []
    missing_pages = set()
    
    for source_rel, data in file_metadata.items():
        source_dir = os.path.dirname(data["abs_path"])
        for url_clean, original_url, text in data["links"]:
            # Skip empty links
            if not url_clean.strip():
                continue
            
            # Handle file:/// absolute paths
            if url_clean.startswith('file:///'):
                local_path = url_clean.replace('file:///', '')
                # On Windows, if path is like /C:/Users/..., strip the leading slash
                if re.match(r'^/[a-zA-Z]:', local_path):
                    local_path = local_path[1:]
                elif re.match(r'^/[a-zA-Z]/', local_path): # e.g. /c/...
                    local_path = local_path[1:]
                
                local_path = os.path.normpath(local_path)
                exists = os.path.exists(local_path)
                if not exists:
                    broken_links.append({
                        "source": source_rel,
                        "target_url": original_url,
                        "text": text,
                        "resolved_path": local_path,
                        "type": "absolute_file"
                    })
                continue
            
            # Target absolute path
            target_abs = os.path.normpath(os.path.join(source_dir, url_clean))
            
            # Check if exists
            exists = os.path.exists(target_abs)
            
            # Map back to wiki relative if inside wiki
            if target_abs.startswith(WIKI_DIR):
                target_rel = os.path.relpath(target_abs, WIKI_DIR).replace('\\', '/')
                if exists:
                    if target_rel in file_metadata:
                        file_metadata[target_rel]["incoming_links"].append(source_rel)
                else:
                    broken_links.append({
                        "source": source_rel,
                        "target_url": original_url,
                        "text": text,
                        "resolved_path": target_abs,
                        "type": "wiki"
                    })
                    missing_pages.add(target_rel)
            elif target_abs.startswith(RAW_DIR):
                # Under raw dir
                if not exists:
                    broken_links.append({
                        "source": source_rel,
                        "target_url": original_url,
                        "text": text,
                        "resolved_path": target_abs,
                        "type": "raw"
                    })
            else:
                # Outside both WIKI and RAW (e.g. temp attachments)
                if not exists:
                    # Let's see if it's local or temp
                    broken_links.append({
                        "source": source_rel,
                        "target_url": original_url,
                        "text": text,
                        "resolved_path": target_abs,
                        "type": "external_file"
                    })

    # Find orphans (nodes with 0 incoming links, excluding index.md, log.md, overview.md)
    # Actually, we should check if they are linked by ANY page OTHER THAN index.md and log.md
    orphans = []
    for rel_path, data in file_metadata.items():
        if rel_path in ["index.md", "log.md", "overview.md", "lint_report.md"]:
            continue
        
        # Filter incoming links that are not index.md or log.md
        real_incoming = [src for src in data["incoming_links"] if src not in ["index.md", "log.md", "overview.md"]]
        if not real_incoming:
            orphans.append((rel_path, data["frontmatter"].get("title", "Untitled")))
            
    # Check Frontmatter Quality
    frontmatter_errors = []
    for rel_path, data in file_metadata.items():
        fm = data["frontmatter"]
        if not fm:
            frontmatter_errors.append((rel_path, "Missing Frontmatter"))
            continue
        if "error" in fm:
            frontmatter_errors.append((rel_path, fm["error"]))
            continue
            
        # Required fields check
        required_fields = ["title", "type", "summary"]
        missing_fields = [field for field in required_fields if field not in fm]
        if missing_fields:
            frontmatter_errors.append((rel_path, f"Missing fields: {missing_fields}"))
            
        # Check folder-type consistency
        folder = rel_path.split('/')[0]
        if '/' in rel_path:
            expected_type = None
            if folder == "sources":
                expected_type = "source"
            elif folder == "entities":
                expected_type = "entity"
            elif folder == "concepts":
                expected_type = "concept"
            elif folder == "topics":
                expected_type = "topic"
            elif folder == "analyses":
                expected_type = "analysis"
            elif folder == "skills":
                expected_type = "skill"
            elif folder == "projects":
                expected_type = "project"
            elif folder == "playbooks":
                expected_type = "playbook"
            
            actual_type = fm.get("type")
            if expected_type and actual_type != expected_type:
                frontmatter_errors.append((rel_path, f"Type mismatch: folder is '{folder}', expected type '{expected_type}', but got '{actual_type}'"))

    # Generate markdown report content
    report_lines = []
    report_lines.append("# 🛠️ WikiLLM Lint 整理報告 (2026-05-28)")
    report_lines.append("")
    report_lines.append(f"> **整理狀態**：🟡 發現部分孤立頁面或失效連結 (檢查檔案數: {len(md_files)})  ")
    report_lines.append("> **維護人員**：LLM Agent (Antigravity)")
    report_lines.append("")
    report_lines.append("---")
    report_lines.append("")
    report_lines.append("## 🔍 損壞的相對連結 (Broken Links)")
    if broken_links:
        for bl in broken_links:
            report_lines.append(f"- ❌ 檔案 `[{bl['source']}](file:///{WIKI_DIR.replace('\\', '/')}/{bl['source']})` 中的連結 `[{bl['text']}]({bl['target_url']})` 指向不存在的路徑：`{bl['resolved_path']}` (類型: {bl['type']})")
    else:
        report_lines.append("- 🟢 無損壞的相對連結。")
    report_lines.append("")
    report_lines.append("## 📁 缺失的頁面 (Missing Pages)")
    if missing_pages:
        for mp in sorted(list(missing_pages)):
            report_lines.append(f"- ❓ 經由相對連結引用但不存在的頁面：`{mp}`")
    else:
        report_lines.append("- 🟢 無缺失的頁面。")
    report_lines.append("")
    report_lines.append("## 🔗 孤立頁面 (Orphan Pages)")
    report_lines.append("> 指除了 `index.md` 與 `log.md` 等導覽頁外，沒有被任何其他 Wiki 頁面連結到的檔案。")
    if orphans:
        for rel, title in sorted(orphans, key=lambda x: x[0]):
            report_lines.append(f"- 📭 `[{rel}](file:///{WIKI_DIR.replace('\\', '/')}/{rel})` ({title})")
    else:
        report_lines.append("- 🟢 無孤立頁面。")
    report_lines.append("")
    report_lines.append("## 📝 Frontmatter 格式錯誤與警告")
    if frontmatter_errors:
        for rel, err in sorted(frontmatter_errors, key=lambda x: x[0]):
            report_lines.append(f"- ⚠️ `[{rel}](file:///{WIKI_DIR.replace('\\', '/')}/{rel})`: {err}")
    else:
        report_lines.append("- 🟢 所有頁面的 Frontmatter 格式均正確。")
    
    report_content = "\n".join(report_lines)
    
    # Write to wiki/lint_report.md
    report_path = os.path.join(WIKI_DIR, "lint_report.md")
    with open(report_path, 'w', encoding='utf-8') as rf:
        rf.write(report_content)
        
    print("=== WIKI LINT RESULTS ===")
    print(f"Total MD files checked: {len(md_files)}")
    print(f"Broken links found: {len(broken_links)}")
    print(f"Missing pages: {len(missing_pages)}")
    print(f"Orphan pages: {len(orphans)}")
    print(f"Frontmatter errors: {len(frontmatter_errors)}")
    print(f"Detailed report written to: {report_path}")

if __name__ == "__main__":
    main()
