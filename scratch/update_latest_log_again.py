# -*- coding: utf-8 -*-
import os

def main():
    log_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\log.md"
    if not os.path.exists(log_path):
        print(f"[ERROR] {log_path} not found.")
        return

    with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # 移除 BOM 與 \r
    has_bom = content.startswith('\ufeff')
    if has_bom:
        content = content.lstrip('\ufeff')
    content = content.replace("\r", "")

    # 我們要替換的舊段落
    old_block = """    - [bzs-saas-customer-list.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/analyses/bzs/bzs-saas-customer-list.md) ── 增量更新太平洋旅行社、自強基金會、豐盛富足、富友、耐斯、福安與聯合線上的日報引用，並新增「透明房訊」與「自強基金會」。"""

    new_block = """    - [bzs-saas-customer-list.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/analyses/bzs/bzs-saas-customer-list.md) ── 增量更新太平洋旅行社、自強基金會、豐盛富足、富友、耐斯、福安與聯合線上的日報引用，並新增「透明房訊」與「自強基金會」。
    - [bzs-acquisition-channels.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/analyses/bzs/bzs-acquisition-channels.md) ── 重構獲客管道與成效矩陣，整合最新 5 月底廣告支出、Leads 漏斗、GEO/AIO 攔截與高佔比 SI/ISV 通路實績。"""

    if old_block in content:
        content = content.replace(old_block, new_block, 1)
        print("[SUCCESS] Log entry updated successfully.")
    else:
        print("[ERROR] Old block not found in log.md.")

    if has_bom:
        content = '\ufeff' + content

    with open(log_path, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    main()
