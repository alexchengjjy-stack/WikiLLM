import os
import datetime
import sys

def main():
    # 強制輸出為 UTF-8
    sys.stdout.reconfigure(encoding='utf-8')
    root_dir = "raw"
    if not os.path.exists(root_dir):
        print(f"Error: Directory '{root_dir}' does not exist.")
        return

    all_files = []
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            full_path = os.path.join(root, f)
            try:
                mtime = os.path.getmtime(full_path)
                dt = datetime.datetime.fromtimestamp(mtime)
                size = os.path.getsize(full_path)
                all_files.append((full_path, dt, size))
            except Exception as e:
                pass

    # 按修改時間從新到舊排序
    all_files.sort(key=lambda x: x[1], reverse=True)

    print("--- 最近修改的 30 個 raw 檔案 ---")
    for path, dt, size in all_files[:30]:
        print(f"{path} | {dt.strftime('%Y-%m-%d %H:%M:%S')} | {size} bytes")

if __name__ == '__main__':
    main()
