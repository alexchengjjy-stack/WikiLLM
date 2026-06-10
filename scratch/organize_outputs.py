import os
import shutil

# 定義工作區基礎路徑
base_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM"
outputs_dir = os.path.join(base_dir, "outputs")
scratch_dir = os.path.join(base_dir, "scratch")

# 定義目標子目錄
subdirs = {
    "bzs": os.path.join(outputs_dir, "bzs"),
    "bzb": os.path.join(outputs_dir, "bzb"),
    "esign": os.path.join(outputs_dir, "esign"),
    "assets": os.path.join(outputs_dir, "assets")
}

# 確保所有子目錄存在
for path in subdirs.values():
    os.makedirs(path, exist_ok=True)

# 檔案分類對照表
files_mapping = {
    # 好好簽 BZS 相關
    "bzs": [
        "20260515-si-article-landing-page.html",
        "20260515-si-blog-post.html",
        "20260515-si-blog-post-v2.html",
        "20260515-si-blog-post-v3.html",
        "breezysign-case-study-fuyou-travel.html",
        "breezysign-case-study-fuyou-travel.md",
        "breezysign-case-study-fuyou-travel.pdf",
        "bzs-2026-marketing-strategy-and-funnel.html",
        "bzs-2026-marketing-strategy-and-funnel.pdf",
        "bzs-202605-operations-complete-report.html",
        "bzs-202605-operations-dashboard.html",
        "bzs-blog-marketing-posts-202605.html",
        "bzs-blog-marketing-posts-202605.pdf",
        "bzs-pricing-cost-structure-analysis-20260525.html",
        "bzs-pricing-cost-structure-analysis-20260525.pdf"
    ],
    # 好好腦 BZB 相關
    "bzb": [
        "BreezyBrain-Product-Spec.html",
        "BreezyBrain-Product-Spec.pdf",
        "BreezyBrain-Product-Spec.zip",
        "BreezyBrain_General_Edition.pptx",
        "BreezyBrain_General_Edition_v2.pptx",
        "BreezyBrain_General_Edition_v3.pptx",
        "BreezyBrain_Internal_Proposal.pptx",
        "BreezyBrain_PenPower_Edition.pptx",
        "BreezyBrain_PenPower_Edition_v2.pptx",
        "BreezyBrain_PenPower_Edition_v3.pptx",
        "breezy_brain_framework.png",
        "arch_v2_generation_result.txt",
        "arch_v5_generation_result.txt"
    ],
    # 電子簽章 esign 相關
    "esign": [
        "20260515-esign-monitoring-snapshot-v1.html",
        "esign-competitor-seo-geo-analysis-20260525.html",
        "esign-competitor-seo-geo-analysis-20260525.pdf",
        "esign-competitor-seo-geo-analysis.html",
        "esign-competitor-seo-geo-analysis.pdf",
        "esign-heading-optimization-report.html",
        "esign-heading-optimization-report.pdf",
        "esign-monitoring-snapshot-202605.html",
        "esign-monitoring-snapshot-202605.pdf",
        "esign-monitoring-snapshot-202605.pptx"
    ],
    # 圖片與品牌資產
    "assets": [
        "bzs-logo-green.png",
        "bzs-logo-white.png",
        "bzs_blog_finance_loan_cover.png",
        "bzs_blog_moda_approval_cover.png",
        "bzs_blog_real_estate_cover.png",
        "bzs_blog_travel_cover.png",
        "wikillm_agent_framework.png"
    ]
}

# 執行移動
print("開始搬移 outputs/ 根目錄下的舊檔案...")
for category, files in files_mapping.items():
    dest_dir = subdirs[category]
    for file in files:
        src_path = os.path.join(outputs_dir, file)
        dest_path = os.path.join(dest_dir, file)
        
        if os.path.exists(src_path):
            try:
                shutil.move(src_path, dest_path)
                print(f"成功移動: {file} -> outputs/{category}/")
            except Exception as e:
                print(f"移動失敗: {file}, 原因: {e}")
        else:
            # 檢查是否已經在目標資料夾了（以防重複執行）
            if os.path.exists(dest_path):
                print(f"檔案已存在於目標目錄: outputs/{category}/{file}")
            else:
                print(f"找不到檔案: {file}")

# 移動特定 Python 腳本至 scratch/
script_file = "generate_pptx.py"
src_script = os.path.join(outputs_dir, script_file)
dest_script = os.path.join(scratch_dir, script_file)

if os.path.exists(src_script):
    try:
        shutil.move(src_script, dest_script)
        print(f"成功移動腳本: {script_file} -> scratch/")
    except Exception as e:
        print(f"移動腳本失敗: {script_file}, 原因: {e}")
else:
    if os.path.exists(dest_script):
        print(f"腳本已存在於 scratch/: {script_file}")
    else:
        print(f"找不到腳本檔案: {script_file}")

print("搬移作業完成。")
