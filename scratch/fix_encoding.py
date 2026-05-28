import os

FILE_PATH = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\products\breezy-brain\breezy-brain-integration-flow.md"

def inspect_invalid_byte():
    if not os.path.exists(FILE_PATH):
        print(f"File not found: {FILE_PATH}")
        return
        
    with open(FILE_PATH, 'rb') as f:
        data = f.read()
        
    length = len(data)
    pos = 8769
    print(f"File size: {length} bytes")
    print(f"Inspecting around byte position {pos}:")
    
    start = max(0, pos - 50)
    end = min(length, pos + 50)
    
    chunk = data[start:end]
    print(f"Binary chunk: {chunk}")
    
    # 用 errors='replace' 試印
    # text_repr = chunk.decode('utf-8', errors='replace')
    # print(f"Decoded with replacement: {text_repr}")
    
    # 嘗試找出所有的無效 UTF-8 位元組並修復它
    # 我們可以嘗試用 errors='ignore' 解碼成 utf-8，再重新以 utf-8 編碼寫入檔案
    try:
        clean_text = data.decode('utf-8', errors='ignore')
        # 測試是否能正常 decode
        clean_text.encode('utf-8')
        
        # 覆寫檔案
        with open(FILE_PATH, 'w', encoding='utf-8') as out:
            out.write(clean_text)
        print("Successfully cleaned and rewrote the file in UTF-8 format.")
    except Exception as e:
        print(f"Failed to clean file: {e}")

if __name__ == "__main__":
    inspect_invalid_byte()
