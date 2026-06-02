import subprocess

file_path = r"wiki/sources/breezysign-pricing.md"
cwd = r"c:\Users\alexc\OneDrive\文件\WikiLLM"

try:
    result = subprocess.run(
        ["git", "diff", "--", file_path],
        cwd=cwd,
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='ignore'
    )
    print("Uncommitted Diff：")
    print(result.stdout)
except Exception as e:
    print(f"錯誤: {e}")
