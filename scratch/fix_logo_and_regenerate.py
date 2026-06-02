import os
import shutil
import subprocess

outputs_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs"
assets_dir = os.path.join(outputs_dir, "assets")

# 1. 確保 assets 目錄存在
if not os.path.exists(assets_dir):
    os.makedirs(assets_dir)
    print(f"建立了 assets 目錄: {assets_dir}")

# 2. 複製 logo 檔案到 assets 目錄下
src_green = os.path.join(outputs_dir, "bzs-logo-green.png")
src_white = os.path.join(outputs_dir, "bzs-logo-white.png")

dst_green = os.path.join(assets_dir, "bzs-logo-green.png")
dst_white = os.path.join(assets_dir, "bzs-logo-white.png")

if os.path.exists(src_green):
    shutil.copy2(src_green, dst_green)
    print(f"複製綠色 logo 成功: {dst_green}")
else:
    print(f"錯誤: 找不到綠色 logo {src_green}")

if os.path.exists(src_white):
    shutil.copy2(src_white, dst_white)
    print(f"複製白色 logo 成功: {dst_white}")
else:
    print(f"錯誤: 找不到白色 logo {src_white}")

# 3. 重新運行 generate_competitor_snapshot_pdf.py 以生成快照
script_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch\generate_competitor_snapshot_pdf.py"
print(f"正在執行快照重新生成腳本: {script_path}...")
result = subprocess.run(
    ["py", script_path],
    cwd=r"c:\Users\alexc\OneDrive\文件\WikiLLM",
    capture_output=True,
    text=True,
    encoding="utf-8",
    errors="ignore"
)

print("Stdout:")
print(result.stdout)
print("Stderr:")
print(result.stderr)

if result.returncode == 0:
    print("[SUCCESS] 快照重新生成成功！")
else:
    print(f"[ERROR] 快照重新生成失敗，退出碼: {result.returncode}")
