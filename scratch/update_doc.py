import os

main_file = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\analyses\bzs-saas-paid-subscribers-by-plan.md"
list_file = r"C:\Users\alexc\OneDrive\文件\WikiLLM\scratch\merged_list.md"

with open(main_file, "r", encoding="utf-8") as f:
    main_content = f.read()

with open(list_file, "r", encoding="utf-8") as f:
    new_list_content = f.read()

# Split main_content
# Header block: up to "> ... 進行歸類。\n\n"
header_end = main_content.find("## 🏢 企業方案")
header_block = main_content[:header_end]

# Footer block: from "## 相關連結"
footer_start = main_content.find("## 相關連結")
footer_block = main_content[footer_start:]

# New content
final_content = header_block + new_list_content + "\n" + footer_block

with open(main_file, "w", encoding="utf-8") as f:
    f.write(final_content)

print("Successfully merged and updated bzs-saas-paid-subscribers-by-plan.md")
