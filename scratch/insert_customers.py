import re

file_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\analyses\bzs-saas-customer-list.md"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

header_end = 0
for i, line in enumerate(lines):
    if line.startswith("| -------------------"):
        header_end = i
        break

table_lines = lines[header_end + 1:]
header_lines = lines[:header_end + 1]

new_customers = [
    "| 三亞旅行社有限公司 | 20260519日報.md |\n",
    "| 方睿科技股份有限公司 | 20260519日報.md |\n",
    "| 美科實業股份有限公司 | 20260519日報.md |\n",
    "| 福安管理顧問企業社 | 20260519日報.md |\n"
]

table_lines.extend(new_customers)
# sort the table lines by the customer name (the part after the first '|')
table_lines.sort(key=lambda x: x.split('|')[1].strip())

with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(header_lines)
    f.writelines(table_lines)

print("Customers added and sorted successfully.")
