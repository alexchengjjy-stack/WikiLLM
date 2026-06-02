# -*- coding: utf-8 -*-
import os

target_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\analyses\bzs\bzs-saas-paid-subscribers-by-plan.md"

if os.path.exists(target_path):
    with open(target_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract Frontmatter
    fm_end_pos = content.find("---", 4)
    if fm_end_pos != -1:
        frontmatter = content[:fm_end_pos+3]
        body = content[fm_end_pos+3:].strip()
    else:
        print("Frontmatter not closed properly.")
        exit(1)
    
    # We want to re-construct the body:
    # 1. Main H1 Header
    # 2. Section: BZS SaaS 各方案銷售佔比與客戶結構對照分析 (2026年5月底統計) (as H2)
    # 3. Section: BZS SaaS 實質付費客戶分類清單 (2024-2026) (as H2)
    # 4. Related Links & Sources
    
    # Let's extract the analysis block
    analysis_start = body.find("## BZS SaaS 各方案銷售佔比與客戶結構對照分析")
    # Find next section, which is ## 相關連結
    analysis_end = body.find("## 相關連結", analysis_start)
    
    if analysis_start != -1 and analysis_end != -1:
        analysis_block = body[analysis_start:analysis_end].strip()
        # Remove the analysis block from body to get the clean list block
        # We need to replace the analysis block with empty string, but be careful with newlines.
        list_block = body[:analysis_start].strip()
        # Find where list starts (it was originally # BZS SaaS 實質付費客戶分類清單 (2024-2026))
        # Let's clean the list header to make it ## 二、 BZS SaaS 實質付費客戶分類清單 (2024-2026)
        list_header_old = "# BZS SaaS 實質付費客戶分類清單 (2024-2026)"
        list_header_new = "## 二、 BZS SaaS 實質付費客戶分類清單 (2024-2026)"
        if list_header_old in list_block:
            list_block = list_block.replace(list_header_old, list_header_new)
        
        # Clean analysis block title to: ## 一、 BZS SaaS 各方案銷售佔比與客戶結構對照分析 (2026年5月底統計)
        analysis_block = analysis_block.replace(
            "## BZS SaaS 各方案銷售佔比與客戶結構對照分析",
            "## 一、 BZS SaaS 各方案銷售佔比與客戶結構對照分析 (2026年5月底統計)"
        )
        
        related_block = body[analysis_end:].strip()
        
        # Assemble new body
        new_body = """# BZS SaaS 實質付費客戶分類清單 (按方案)

> 本清單包含實質付費方案結構對照分析，以及篩選自 2024-2026 歷史「訂閱訂單」金流紀錄的實質付費企業與個人名單。

{analysis}

{list}

{related}""".format(
            analysis=analysis_block,
            list=list_block,
            related=related_block
        )
        
        full_new_content = frontmatter + "\n\n" + new_body
        
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(full_new_content)
        print("Successfully swapped sections in paid subscribers file.")
    else:
        print("Could not locate analysis or related block in the file.")
else:
    print("paid subscribers file not found.")
