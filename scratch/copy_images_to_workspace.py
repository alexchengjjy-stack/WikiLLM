import shutil
import os

# 來源檔案路徑
src_dir = r"C:\Users\alexc\.gemini\antigravity-ide\brain\7cf2a8d1-06aa-4454-8653-960628818c63"
dst_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs"

files_to_copy = [
    ("bzs_travel_case_1779701691260.png", "bzs_blog_travel_cover.png"),
    ("bzs_real_estate_1779701707261.png", "bzs_blog_real_estate_cover.png"),
    ("bzs_finance_loan_1779701725411.png", "bzs_blog_finance_loan_cover.png"),
    ("bzs_moda_approval_1779701746206.png", "bzs_blog_moda_approval_cover.png")
]

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

print("Starting copying cover images to outputs directory...")
for src_name, dst_name in files_to_copy:
    src_path = os.path.join(src_dir, src_name)
    dst_path = os.path.join(dst_dir, dst_name)
    
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
        print(f"  [SUCCESS] Copied to: {dst_path}")
    else:
        print(f"  [ERROR] Source file not found: {src_path}")

print("All copies done.")
