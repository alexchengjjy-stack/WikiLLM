import os
import re
import shutil

# 定義 Wiki 根目錄與 Analyses 目錄
WIKI_DIR = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki"
ANALYSES_DIR = os.path.join(WIKI_DIR, "analyses")

# 28 個檔案的對照映射，均以 analyses/ 子目錄開頭
mapping = {
    "2026-h2-marketing-strategy-recommendations.md": "bzs/bzs-h2-marketing-strategy-2026.md",
    "ai-search-geo-empirical-report.md": "esign/esign-ai-search-geo-empirical-report.md",
    "antigravity-aipm-framework.md": "bzb/bzb-antigravity-aipm-framework.md",
    "breezy-brain-concept-market-analysis.md": "bzb/bzb-concept-market-analysis.md",
    "breezybrain-spec-defense.md": "bzb/bzb-spec-defense.md",
    "bzs-acquisition-channels.md": "bzs/bzs-acquisition-channels.md",
    "bzs-battle-cards.md": "bzs/bzs-battle-cards.md",
    "bzs-blog-marketing-posts-202605.md": "bzs/bzs-blog-marketing-posts-202605.md",
    "bzs-bu-role-based-tasklist.md": "bzs/bzs-bu-role-based-tasklist.md",
    "bzs-customer-personas.md": "bzs/bzs-customer-personas.md",
    "bzs-feature-requirements.md": "bzs/bzs-feature-requirements.md",
    "bzs-pricing-cost-structure-analysis-20260525.md": "bzs/bzs-pricing-cost-structure-analysis-20260525.md",
    "bzs-saas-customer-list.md": "bzs/bzs-saas-customer-list.md",
    "bzs-saas-funnel-ltv-cac-report.md": "bzs/bzs-saas-funnel-ltv-cac-report.md",
    "bzs-saas-marketing-synthesis-2026.md": "bzs/bzs-saas-marketing-synthesis-2026.md",
    "bzs-saas-ops-csm-reconciliation-202605.md": "bzs/bzs-saas-ops-csm-reconciliation-202605.md",
    "bzs-saas-paid-subscribers-by-plan.md": "bzs/bzs-saas-paid-subscribers-by-plan.md",
    "bzs-saas-plan-sales-comparison.md": "bzs/bzs-saas-plan-sales-comparison.md",
    "bzs-website-seo-geo-analysis.md": "bzs/bzs-website-seo-geo-analysis.md",
    "domestic-e-signature-comparison.md": "esign/esign-domestic-comparison.md",
    "dottedsign-price-hike-churn-analysis.md": "esign/esign-dottedsign-price-hike-churn-analysis.md",
    "dottedsign-website-seo-geo-analysis.md": "esign/esign-dottedsign-website-seo-geo-analysis.md",
    "esign-competitor-seo-geo-analysis-20260525.md": "esign/esign-competitor-seo-geo-analysis-20260525.md",
    "esign-competitor-seo-geo-analysis.md": "esign/esign-competitor-seo-geo-analysis.md",
    "esign-monitoring-snapshot-202605.md": "esign/esign-monitoring-snapshot-202605.md",
    "esign-pricing-feature-comparison.md": "esign/esign-pricing-feature-comparison.md",
    "global-e-signature-comparison.md": "esign/esign-global-comparison.md",
    "legalsign-website-seo-geo-analysis.md": "esign/esign-legalsign-website-seo-geo-analysis.md",
}

# 1. 建立物理移動的來源到目標絕對路徑映射
physics_moves = {}
for src_name, dest_rel in mapping.items():
    src_abs = os.path.join(ANALYSES_DIR, src_name)
    dest_abs = os.path.join(ANALYSES_DIR, dest_rel.replace('/', os.sep))
    physics_moves[src_abs] = dest_abs

# 2. 進行物理移動與改寫內部連結
print("=== 執行物理搬移 ===")
for src_abs, dest_abs in physics_moves.items():
    if os.path.exists(src_abs):
        os.makedirs(os.path.dirname(dest_abs), exist_ok=True)
        print(f"Moving {os.path.basename(src_abs)} -> {os.path.relpath(dest_abs, WIKI_DIR)}")
        shutil.move(src_abs, dest_abs)
    else:
        # 由於可能已搬移過，只提示，不中斷
        print(f"[提示] 檔案已被移動或不存在：{os.path.basename(src_abs)}")

# 3. 遍歷整個 wiki，更新所有相對連結與 Obsidian 雙鏈
def update_links_in_content(content, file_path):
    file_dir = os.path.dirname(file_path)
    
    # 3a. 處理 Markdown 連結
    def md_replacer(match):
        text = match.group(1)
        link = match.group(2)
        
        # 拆開錨點 (anchor)
        link_parts = link.split('#')
        clean_link = link_parts[0]
        anchor = '#' + link_parts[1] if len(link_parts) > 1 else ''
        
        # 取得 basename
        link_basename = os.path.basename(clean_link)
        
        if link_basename in mapping:
            new_dest_rel = mapping[link_basename]
            new_dest_abs = os.path.join(ANALYSES_DIR, new_dest_rel.replace('/', os.sep))
            new_rel_link = os.path.relpath(new_dest_abs, file_dir).replace(os.sep, '/')
            return f"[{text}]({new_rel_link}{anchor})"
        
        # 3b. 特殊處理：被搬移檔案的內部原有相對連結（如 ../sources/）需要加深一層
        is_moved_file = False
        for dest_abs in physics_moves.values():
            if os.path.normpath(file_path) == os.path.normpath(dest_abs):
                is_moved_file = True
                break
                
        if is_moved_file:
            # 如果連結是以 ../ 開頭，且後面不是 analyses，且不以 ../../ 開頭，需要多往上退一層
            if link.startswith("../") and not link.startswith("../analyses/") and not link.startswith("../../"):
                return f"[{text}](../{link})"
            
        return match.group(0)

    # 匹配 Markdown 連結
    content = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', md_replacer, content)

    # 3c. 處理 Obsidian 雙鏈 [[link]]
    def wiki_replacer(match):
        raw_inner = match.group(1)
        parts = raw_inner.split('|')
        link = parts[0].strip()
        display = '|' + parts[1] if len(parts) > 1 else ''
        
        link_name = link
        if not link_name.endswith('.md'):
            link_name += '.md'
        link_basename = os.path.basename(link_name)
        
        if link_basename in mapping:
            new_dest_rel = mapping[link_basename]
            new_basename_no_ext = os.path.splitext(os.path.basename(new_dest_rel))[0]
            return f"[[{new_basename_no_ext}{display}]]"
        
        return match.group(0)
        
    content = re.sub(r'\[\[([^\]]+)\]\]', wiki_replacer, content)
    
    return content

print("=== 執行連結修復 ===")
for root, dirs, files in os.walk(WIKI_DIR):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            
            # 使用多重編碼重試機制
            content = None
            used_encoding = 'utf-8'
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                try:
                    with open(file_path, 'r', encoding='cp950') as f:
                        content = f.read()
                        used_encoding = 'cp950'
                except UnicodeDecodeError:
                    print(f"[錯誤] 無法讀取檔案（編碼問題）：{file_path}，將使用 errors='ignore'")
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        used_encoding = 'utf-8'

            if content is not None:
                updated_content = update_links_in_content(content, file_path)
                
                if updated_content != content:
                    print(f"Updating links in {os.path.relpath(file_path, WIKI_DIR)} (encoding: {used_encoding})")
                    with open(file_path, 'w', encoding=used_encoding) as f:
                        f.write(updated_content)

print("=== 重構完成！ ===")
