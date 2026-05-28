# -*- coding: utf-8 -*-
import sys

def fix_file_precise(filename):
    with open(filename, 'rb') as f:
        data = bytearray(f.read())
    
    print(f"Original size: {len(data)} bytes")
    
    bad_bytes_removed = []
    
    while True:
        try:
            # 嘗試解碼整個 bytes
            data.decode('utf-8')
            print("Successfully decoded as UTF-8!")
            break
        except UnicodeDecodeError as e:
            # 記錄出錯的 index
            bad_idx = e.start
            bad_val = data[bad_idx]
            bad_bytes_removed.append((bad_idx, bad_val))
            
            # 列印出錯位置的上下文
            context = data[max(0, bad_idx-20):min(len(data), bad_idx+21)]
            print(f"Bad byte {hex(bad_val)} at index {bad_idx}. Context: {context}")
            
            # 移除該壞位元組 (可能有多個壞位元組，我們逐個移除)
            del data[bad_idx]
            
    print(f"Removed total {len(bad_bytes_removed)} bad bytes: {bad_bytes_removed}")
    
    # 寫回檔案
    with open(filename, 'wb') as f:
        f.write(data)
    print(f"Successfully fixed and wrote {filename}")

if __name__ == '__main__':
    fix_file_precise('wiki/index.md')
