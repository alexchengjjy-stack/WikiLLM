# -*- coding: utf-8 -*-
import re

def get_clean_metrics():
    # 我們分析 metrics_summary.txt 或是 report_details.txt
    # 尋找每個月分真正有意義的文字
    
    files_to_try = [
        "scratch/metrics_summary.txt",
        "scratch/report_details.txt",
        "scratch/clean_extracted_reports.txt",
        "scratch/parsed_report_data.txt"
    ]
    
    reports = [
        "2025.10.02", "2025.11.03", "2025.12.02", "2026.01.05",
        "2026.02.02", "2026.03.03", "2026.04.02", "2026.05.05"
    ]
    
    print("Checking which file contains actual month data...")
    
    for filepath in files_to_try:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            print(f"File {filepath}: length = {len(content)}")
            
            # 統計每個報告日期出現的次數
            for r in reports:
                count = content.count(r)
                print(f"  - {r}: count = {count}")
        except Exception as e:
            print(f"Error reading {filepath}: {e}")

if __name__ == "__main__":
    get_clean_metrics()
