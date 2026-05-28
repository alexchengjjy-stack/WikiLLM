# -*- coding: utf-8 -*-
with open('scratch/clean_extracted_reports.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if 'REPORT DATE' in line:
            print(line.strip())
