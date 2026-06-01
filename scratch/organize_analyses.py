# -*- coding: utf-8 -*-
import os
import re
import shutil

# 定義工作目錄為 WikiLLM 根目錄
WORKSPACE_DIR = r"c:\Users\alexc\OneDrive\文件\WikiLLM"
WIKI_DIR = os.path.join(WORKSPACE_DIR, "wiki")
ANALYSES_DIR = os.path.join(WIKI_DIR, "analyses")

# 33個需要搬移的檔案清單
analyses_files = [
    "bzb-antigravity-aipm-framework.md",
    "bzb-concept-market-analysis.md",
    "bzb-mvp-roadmap.md",
    "bzb-spec-analysis-report.md",
    "bzb-spec-defense.md",
    "bzs-acquisition-channels.md",
    "bzs-battle-cards.md",
    "bzs-blog-marketing-posts-202605.md",
    "bzs-bu-role-based-tasklist.md",
    "bzs-customer-personas.md",
    "bzs-feature-requirements.md",
    "bzs-h2-marketing-strategy-2026.md",
    "bzs-pricing-cost-structure-analysis-20260525.md",
    "bzs-saas-customer-list.md",
    "bzs-saas-funnel-ltv-cac-report.md",
    "bzs-saas-marketing-synthesis-2026.md",
    "bzs-saas-ops-csm-reconciliation-202605.md",
    "bzs-saas-paid-subscribers-by-plan.md",
    "bzs-saas-plan-sales-comparison.md",
    "bzs-website-seo-geo-analysis.md",
    "esign-ai-search-geo-empirical-report.md",
    "esign-competitor-seo-geo-analysis-20260525.md",
    "esign-competitor-seo-geo-analysis-20260527.md",
    "esign-competitor-seo-geo-analysis.md",
    "esign-domestic-comparison.md",
    "esign-dottedsign-price-hike-churn-analysis.md",
    "esign-dottedsign-website-seo-geo-analysis.md",
    "esign-global-comparison.md",
    "esign-legalsign-website-seo-geo-analysis.md",
    "esign-monitoring-snapshot-202605.md",
    "esign-monitoring-snapshot-202606.md",
    "esign-pricing-feature-comparison.md",
    "wikillm-kb-health-check-report.md"
]

# 決定檔案要搬移到哪一個子目錄
def get_dest_subdir(filename):
    if filename.startswith("bzs-"):
        return "bzs"
    elif filename.startswith("bzb-"):
        return "bzb"
    elif filename.startswith("esign-"):
        return "esign"
    elif filename.startswith("wikillm-"):
        return "wikillm"
    else:
        return None

# 1. 建立目標子目錄
subdirs = ["bzs", "bzb", "esign", "wikillm"]
for sd in subdirs:
    sd_path = os.path.join(ANALYSES_DIR, sd)
    if not os.path.exists(sd_path):
        os.makedirs(sd_path)
        print(f"[建立目錄] {sd_path}")

# 2. 物理搬移檔案，並記錄新舊絕對路徑
file_mapping = {}  # 舊檔名 -> 新絕對路徑
for f_name in analyses_files:
    src_path = os.path.join(ANALYSES_DIR, f_name)
    if os.path.exists(src_path):
        subdir = get_dest_subdir(f_name)
        if subdir:
            dst_path = os.path.join(ANALYSES_DIR, subdir, f_name)
            shutil.move(src_path, dst_path)
            file_mapping[f_name] = dst_path
            print(f"[移動檔案] {f_name} -> analyses/{subdir}/{f_name}")
        else:
            print(f"[跳過無效前綴] {f_name}")
    else:
        # 如果已經在子目錄中，則直接記錄其位置
        for sd in subdirs:
            check_path = os.path.join(ANALYSES_DIR, sd, f_name)
            if os.path.exists(check_path):
                file_mapping[f_name] = check_path
                print(f"[已在目標目錄] analyses/{sd}/{f_name}")
                break
        else:
            print(f"[找不到檔案] {f_name}")

# 3. 全域修復連結 (相對連結與 Obsidian 雙鏈)
# 正規表達式用來捕捉 markdown 相對連結 [text](path)
markdown_link_pattern = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')
# 正規表達式用來捕捉 Obsidian 雙鏈 [[path]] 或 [[path|alias]]
obsidian_link_pattern = re.compile(r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]')

def fix_links_in_content(content, file_path):
    file_dir = os.path.dirname(file_path)
    
    # 修復標準 Markdown 相對連結
    def replace_markdown_link(match):
        text = match.group(1)
        path = match.group(2)
        
        # 移除可能帶有的錨點
        path_without_anchor = path
        anchor = ""
        if "#" in path:
            path_without_anchor, anchor = path.split("#", 1)
            anchor = "#" + anchor
            
        # 取得純檔名
        base_name = os.path.basename(path_without_anchor)
        
        # 檢查該檔名是否屬於被重分類的 33 個檔案
        if base_name in file_mapping:
            new_dest_abs = file_mapping[base_name]
            # 計算從目前檔案所在目錄到新目標檔案的相對路徑
            new_rel_path = os.path.relpath(new_dest_abs, start=file_dir)
            new_rel_path = new_rel_path.replace("\\", "/") # 確保為 unix 格式斜線
            print(f"  [修正相對連結] {path} -> {new_rel_path}{anchor}")
            return f"[{text}]({new_rel_path}{anchor})"
        
        return match.group(0)
    
    # 修復 Obsidian 雙鏈
    def replace_obsidian_link(match):
        target = match.group(1).strip()
        alias = match.group(2)
        
        # 移除錨點
        target_without_anchor = target
        anchor = ""
        if "#" in target:
            target_without_anchor, anchor = target.split("#", 1)
            anchor = "#" + anchor
            
        base_name = os.path.basename(target_without_anchor)
        # 如果雙鏈沒寫副檔名，補上 .md 以便比對
        if not base_name.endswith(".md"):
            base_name_with_ext = base_name + ".md"
        else:
            base_name_with_ext = base_name
            
        if base_name_with_ext in file_mapping:
            # Obsidian 雙鏈路徑通常是相對 wiki 根目錄，或者僅僅是檔名
            # 如果原本的雙鏈包含 analyses/ 路徑，我們將其更新
            subdir = get_dest_subdir(base_name_with_ext)
            
            # 如果原本就包含了 analyses 路徑，如 [[analyses/esign-domestic-comparison]]
            if "analyses/" in target:
                new_target = f"analyses/{subdir}/{base_name}"
            # 如果原本是 [[wiki/analyses/esign-domestic-comparison]]
            elif "wiki/analyses/" in target:
                new_target = f"wiki/analyses/{subdir}/{base_name}"
            else:
                # 否則直接使用子目錄前綴或直接保留檔名（Obsidian 預設支援扁平搜尋）
                new_target = f"analyses/{subdir}/{base_name}"
                
            alias_str = f"|{alias}" if alias else ""
            print(f"  [修正雙鏈] [[{target}]] -> [[{new_target}{anchor}{alias_str}]]")
            return f"[[{new_target}{anchor}{alias_str}]]"
            
        return match.group(0)

    content = markdown_link_pattern.sub(replace_markdown_link, content)
    content = obsidian_link_pattern.sub(replace_obsidian_link, content)
    return content

print("\n開始全域修復連結...")
# 遍歷 wiki 下的所有 markdown 檔案
for root, dirs, files in os.walk(WIKI_DIR):
    for f in files:
        if f.endswith(".md"):
            f_path = os.path.join(root, f)
            try:
                with open(f_path, "r", encoding="utf-8") as file:
                    content = file.read()
                
                fixed_content = fix_links_in_content(content, f_path)
                
                if fixed_content != content:
                    with open(f_path, "w", encoding="utf-8") as file:
                        file.write(fixed_content)
                    print(f"[修復成功] {os.path.relpath(f_path, WIKI_DIR)}")
            except Exception as e:
                print(f"[Error 讀寫錯誤] {f_path}: {e}")

print("\n重構與連結修復完成！")
