# -*- coding: utf-8 -*-
with open('scratch/clean_extracted_reports.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

out_lines = []
for i, line in enumerate(lines):
    if 'REPORT DATE:' in line:
        out_lines.append("\n" + "="*40 + "\n")
        out_lines.append(line.strip() + "\n")
        out_lines.append("="*40 + "\n")
        # 印出接下來的 60 行
        end_idx = min(i + 60, len(lines))
        for j in range(i + 1, end_idx):
            out_lines.append(lines[j].strip() + "\n")

with open('scratch/printed_metrics_output.txt', 'w', encoding='utf-8') as f:
    f.writelines(out_lines)
