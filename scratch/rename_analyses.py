# -*- coding: utf-8 -*-
"""
analyses 目錄分析報告重命名與連結修復一體化腳本
此腳本自動將不符前綴規範的分析報告進行正名，並全域掃描 wiki 下所有 Markdown 文件以更新引用連結。
"""
import os
import glob
import re

# 設定路徑
base_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM"
wiki_dir = os.path.join(base_dir, "wiki")
analyses_dir = os.path.join(wiki_dir, "analyses")

# 定義重命名對照表 (舊檔名 -> 新檔名)
rename_map = {
    # 1. 好好簽相關 (2026-h2 -> bzs-h2)
    "2026-h2-marketing-strategy-recommendations.md": "bzs-h2-marketing-strategy-2026.md",
    
    # 2. 好好腦相關 (breezybrain / breezy-brain -> bzb)
    "antigravity-aipm-framework.md": "bzb-antigravity-aipm-framework.md",
    "breezy-brain-concept-market-analysis.md": "bzb-concept-market-analysis.md",
    "breezybrain-mvp-roadmap.md": "bzb-mvp-roadmap.md",
    "breezybrain-spec-analysis-report.md": "bzb-spec-analysis-report.md",
    "breezybrain-spec-defense.md": "bzb-spec-defense.md",
    
    # 3. 競品與電子簽章通用 (ai-search / domestic / global / dottedsign -> esign)
    "ai-search-geo-empirical-report.md": "esign-ai-search-geo-empirical-report.md",
    "domestic-e-signature-comparison.md": "esign-domestic-comparison.md",
    "global-e-signature-comparison.md": "esign-global-comparison.md",
    "dottedsign-price-hike-churn-analysis.md": "esign-dottedsign-price-hike-churn-analysis.md",
    "dottedsign-website-seo-geo-analysis.md": "esign-dottedsign-website-seo-geo-analysis.md",
    "legalsign-website-seo-geo-analysis.md": "esign-legalsign-website-seo-geo-analysis.md",
    
    # 4. 知識庫本身維護 (kb-health -> wikillm-kb-health)
    "kb-health-check-report.md": "wikillm-kb-health-check-report.md"
}

def main():
    print("=== 開始執行 analyses 分析報告重命名與連結修復 ===")
    
    # 1. 執行物理重命名
    renamed_count = 0
    for old_name, new_name in rename_map.items():
        old_path = os.path.join(analyses_dir, old_name)
        new_path = os.path.join(analyses_dir, new_name)
        
        if os.path.exists(old_path):
            try:
                # 檢查目標是否已存在，若存在則先移除
                if os.path.exists(new_path):
                    os.remove(new_path)
                os.rename(old_path, new_path)
                print(f"[重命名] {old_name} -> {new_name}")
                renamed_count += 1
            except Exception as e:
                print(f"[錯誤] 無法重命名 {old_name}: {e}")
        else:
            print(f"[略過] 檔案不存在: {old_name}")
            
    print(f"物理重命名完成，共修改 {renamed_count} 個檔案。\n")
    
    # 2. 全域掃描並更新引用連結
    print("=== 開始全域掃描並修正 Markdown 引用連結 ===")
    
    # 獲取 wiki 目錄下所有子目錄的 markdown 檔案
    md_files = glob.glob(os.path.join(wiki_dir, "**", "*.md"), recursive=True)
    
    # 建立正則表達式以便匹配舊檔名
    # 我們需要防範檔名的一部分被匹配，所以使用邊界或精確匹配
    # 因為是 markdown 連結，通常長相如 [文字](path/to/old-name.md) 或是 [[old-name]]
    updated_files_count = 0
    
    for file_path in md_files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            original_content = content
            modified = False
            
            # 遍歷對照表進行字串替換
            for old_name, new_name in rename_map.items():
                # 去除副檔名的 basename，供 Obsidian 雙鏈 [[basename]] 替換
                old_base = os.path.splitext(old_name)[0]
                new_base = os.path.splitext(new_name)[0]
                
                # 替換相對路徑連結中的檔名，例如: analyses/old-name.md -> analyses/new-name.md
                # 為防範誤殺，我們搜尋舊檔名做精確字串替換
                if old_name in content:
                    content = content.replace(old_name, new_name)
                    modified = True
                    
                # 替換雙鏈連結，例如: [[old-name]] -> [[new-name]] 或 [[old-name|別名]] -> [[new-name|別名]]
                # 雙鏈在 obsidian 中長相為 [[old_base]] 或 [[old_base|...]] 或 [[old_base#...]]
                # 用正則精確替換
                pattern_wiki = r'\[\[' + re.escape(old_base) + r'(\|.*?)?\]\]'
                def wiki_repl(match):
                    alias = match.group(1) if match.group(1) else ""
                    return f"[[{new_base}{alias}]]"
                
                if re.search(pattern_wiki, content):
                    content = re.sub(pattern_wiki, wiki_repl, content)
                    modified = True
                    
                # 替換 obsidian 中含有標題錨點的雙鏈，例如: [[old-base#章節]] -> [[new-base#章節]]
                pattern_anchor = r'\[\[' + re.escape(old_base) + r'(#.*?)?\]\]'
                def anchor_repl(match):
                    anchor = match.group(1) if match.group(1) else ""
                    return f"[[{new_base}{anchor}]]"
                
                if re.search(pattern_anchor, content):
                    content = re.sub(pattern_anchor, anchor_repl, content)
                    modified = True
            
            if modified and content != original_content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                rel_path = os.path.relpath(file_path, base_dir)
                print(f"[修正連結] 更新文件: {rel_path}")
                updated_files_count += 1
                
        except Exception as e:
            print(f"[錯誤] 無法處理檔案 {file_path}: {e}")
            
    print(f"全域連結修復完成，共更新了 {updated_files_count} 個文件。")
    print("=== analyses 目錄分類與正名治理完成 ===")

if __name__ == "__main__":
    main()
