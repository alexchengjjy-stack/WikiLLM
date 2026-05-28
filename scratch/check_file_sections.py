# -*- coding: utf-8 -*-
with open('scratch/clean_extracted_reports.txt', 'r', encoding='utf-8') as f:
    text = f.read()

sections = text.split("=================== REPORT DATE:")
print(f"Total sections found: {len(sections)}")
for i, section in enumerate(sections):
    if i == 0:
        print(f"Header length: {len(section)} chars")
        continue
    lines = section.split("\n")
    date_header = lines[0].strip()
    non_empty_lines = [l for l in lines[1:] if l.strip()]
    print(f"Section {i}: Date Header: {date_header} | Total Lines: {len(lines)} | Non-empty Lines: {len(non_empty_lines)}")
    if non_empty_lines:
        print(f"  First non-empty line: {non_empty_lines[0][:100]}")
