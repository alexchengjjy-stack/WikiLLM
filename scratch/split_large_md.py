import os
import glob

# 目標目錄與檔案
target_dir = r"raw\BZSdata\小匯整"
split_dir = os.path.join(target_dir, "split")
MAX_LINES = 2000

if not os.path.exists(split_dir):
    os.makedirs(split_dir)

# 找出所有 .md 檔
md_files = glob.glob(os.path.join(target_dir, "*.md"))

for file_path in md_files:
    filename = os.path.basename(file_path)
    print(f"Processing {filename}...")
    
    # 處理特殊編碼或可能存在的隱藏字元，採用 replace 以免崩潰
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
        
    total_lines = len(lines)
    if total_lines == 0:
        print(f"  -> File is empty, skipping.")
        continue
        
    part_num = 1
    current_chunk = []
    
    for i, line in enumerate(lines):
        current_chunk.append(line)
        
        # 判斷是否達到切分條件：
        # 1. 已經超過 MAX_LINES，且當前行是純空白行 (保留段落完整性)
        # 2. 或者是整個檔案的最後一行
        if (len(current_chunk) >= MAX_LINES and line.strip() == "") or i == total_lines - 1:
            out_name = f"{os.path.splitext(filename)[0]}_part_{part_num}.md"
            out_path = os.path.join(split_dir, out_name)
            
            with open(out_path, 'w', encoding='utf-8') as out_f:
                out_f.writelines(current_chunk)
                
            print(f"  -> Created {out_name} (Lines: {len(current_chunk)})")
            
            current_chunk = []
            part_num += 1

print("\nAll files successfully split into smart chunks!")
