# -*- coding: utf-8 -*-
import sys

try:
    with open('wiki/index.md', 'rb') as f:
        content = f.read()
    
    # 嘗試用 cp950 (Big5) 解碼
    try:
        decoded = content.decode('cp950')
        print("Successfully decoded index.md with cp950")
    except Exception as e:
        print("Failed to decode with cp950, trying with errors='replace':", e)
        decoded = content.decode('cp950', errors='replace')
        
    with open('wiki/index.md', 'w', encoding='utf-8') as f:
        f.write(decoded)
    print("Successfully wrote index.md in UTF-8")
except Exception as e:
    print("Error during conversion:", e)
    sys.exit(1)
