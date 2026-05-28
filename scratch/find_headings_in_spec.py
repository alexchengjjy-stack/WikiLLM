file_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\products\breezy-brain\Product-Spec.md"
output_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch\find_headings_output.txt"

keywords = ["Apache", "LLM", "Ollama", "Qwen", "7B", "授權", "部署", "模型", "選型", "資源計算", "MIT", "Llama", "Mistral"]

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

results = []
results.append(f"Total lines: {len(lines)}\n")

for i, line in enumerate(lines):
    line_num = i + 1
    found = []
    for kw in keywords:
        if kw.lower() in line.lower():
            found.append(kw)
    if found:
        results.append(f"Line {line_num} [{', '.join(found)}]: {line.strip()}\n")

with open(output_path, "w", encoding="utf-8") as f:
    f.writelines(results)

print(f"Done! Results written to {output_path}")
