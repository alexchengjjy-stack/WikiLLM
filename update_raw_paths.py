import os

base_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM\WikiLLM"
raw_dir = os.path.join(base_dir, "raw")
wiki_dir = os.path.join(base_dir, "wiki")

file_map = {}
for root, dirs, files in os.walk(raw_dir):
    for f in files:
        if f.startswith('.'):
            continue
        rel_path = os.path.relpath(os.path.join(root, f), base_dir)
        rel_path = rel_path.replace("\\", "/")
        file_map[f] = rel_path

for root, dirs, files in os.walk(wiki_dir):
    for f in files:
        if not f.endswith(".md"):
            continue
        
        filepath = os.path.join(root, f)
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        
        new_content = content
        for raw_filename, new_rel_path in file_map.items():
            old_pattern_1 = "raw/" + raw_filename
            old_pattern_2 = "raw\\" + raw_filename
            
            if old_pattern_1 in new_content and old_pattern_1 != new_rel_path:
                new_content = new_content.replace(old_pattern_1, new_rel_path)
            if old_pattern_2 in new_content and old_pattern_2 != new_rel_path:
                new_content = new_content.replace(old_pattern_2, new_rel_path)

        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(new_content)
            print(f"Updated: {filepath}")

print("Update completed.")
