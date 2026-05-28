import re

input_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch\log_extracted_decoded.md"
output_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch\metrics_summary.txt"

with open(input_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 尋找所有像 "BreezySign分析報表 202x.xx" 或是 "營收" 等關鍵字
# 我們將 content 按行分割
lines = content.split('\n')
extracted = []

print(f"Total lines in log: {len(lines)}")

# 我們尋找包含 "分析報表 202" 的行，並列出後續的 50 行
for i, line in enumerate(lines):
    if "分析報表 202" in line or "分析報表202" in line:
        block = [f"--- Found at line {i+1} ---", line]
        for j in range(1, 100):
            if i + j < len(lines):
                block.append(lines[i+j])
        extracted.append("\n".join(block))

with open(output_path, 'w', encoding='utf-8') as f:
    f.write("\n\n==========================================\n\n".join(extracted))

print(f"提取完成！已寫入 {output_path}")
