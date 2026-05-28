import sys
import traceback

file_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\products\breezy-brain\Product-Spec.md"
output_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch\headings_list.txt"

try:
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    results = []
    for i, line in enumerate(lines):
        line_num = i + 1
        if line.strip().startswith("#"):
            results.append(f"Line {line_num:4d}: {line.strip()}\n")
            
    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(results)
    print("Success")
except Exception as e:
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("ERROR:\n")
        f.write(traceback.format_exc())
    print("Fail")
