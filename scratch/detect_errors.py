# -*- coding: utf-8 -*-
def analyze_file(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    
    print(f"File: {filename}, Total bytes: {len(data)}")
    
    # 測試 UTF-8 解碼
    try:
        data.decode('utf-8')
        print("UTF-8: OK (No decode errors)")
    except UnicodeDecodeError as e:
        print(f"UTF-8: Failed at position {e.start} to {e.end}")
        print(f"Reason: {e.reason}")
        err_bytes = data[e.start:e.end]
        print(f"Error bytes: {err_bytes}")
        context_start = max(0, e.start - 50)
        context_end = min(len(data), e.end + 50)
        print(f"Context bytes: {data[context_start:context_end]}")
        # 看看如果用 errors='replace' 解碼出來是什麼
        print(f"Context (UTF-8 replaced): {data[context_start:context_end].decode('utf-8', errors='replace')}")
        print(f"Context (CP950 replaced): {data[context_start:context_end].decode('cp950', errors='replace')}")

    # 測試 CP950 解碼
    try:
        data.decode('cp950')
        print("CP950: OK (No decode errors)")
    except UnicodeDecodeError as e:
        print(f"CP950: Failed at position {e.start} to {e.end}")
        print(f"Reason: {e.reason}")
        err_bytes = data[e.start:e.end]
        print(f"Error bytes: {err_bytes}")

if __name__ == '__main__':
    analyze_file('wiki/index.md')
