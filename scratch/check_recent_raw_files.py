import os
import sys
import time

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def main():
    workspace = r"c:\Users\alexc\OneDrive\文件\WikiLLM"
    raw_dir = os.path.join(workspace, "raw")
    
    recent_files = []
    now = time.time()
    two_weeks_ago = now - 14 * 24 * 3600  # 14 天內
    
    for root, dirs, files in os.walk(raw_dir):
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                mtime = os.path.getmtime(full_path)
                if mtime > two_weeks_ago:
                    rel_path = os.path.relpath(full_path, os.path.dirname(raw_dir))
                    recent_files.append((rel_path.replace('\\', '/'), mtime))
                    
    # 按修改時間降序排序（最新在最前）
    recent_files.sort(key=lambda x: x[1], reverse=True)
    
    print(f"最近 14 天內修改的檔案數量: {len(recent_files)}")
    for f, t in recent_files[:30]:  # 列出前 30 個
        time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))
        print(f"[{time_str}] {f}")

if __name__ == "__main__":
    main()
