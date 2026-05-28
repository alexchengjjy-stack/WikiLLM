import os
import re

reports_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM\raw\BZSdata\PMBreezySign分析報表"
files = sorted([f for f in os.listdir(reports_dir) if f.endswith(".md")])

print(f"Found {len(files)} report files:")

for file in files:
    filepath = os.path.join(reports_dir, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract date from filename, e.g. "BreezySign分析報表 2025.10.02.md" -> 2025.10
    date_match = re.search(r"(\d{4}\.\d{2})", file)
    date_str = date_match.group(1) if date_match else "unknown"
    
    print(f"\n--- Report: {file} ({date_str}) ---")
    
    # Split content by sections
    sections = re.split(r"###\s+", content)
    for section in sections:
        if not section.strip():
            continue
        lines = section.strip().split("\n")
        section_name = lines[0].strip()
        
        # Find markdown images ![](url)
        images = re.findall(r"!\[.*?\]\((.*?)\)", section)
        # Find pdf files mentions
        pdfs = re.findall(r"([\w\-\s]+\.pdf)", section)
        
        print(f"  Section: [{section_name}]")
        if pdfs:
            print(f"    PDFs: {pdfs}")
        if images:
            print(f"    Images ({len(images)}):")
            for img in images:
                # print short version of url
                short_url = img.split("?")[0]
                print(f"      {short_url}")
