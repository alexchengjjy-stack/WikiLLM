# -*- coding: utf-8 -*-
def main():
    filename = 'wiki/products/breezy-brain/Product-Spec.md'
    with open(filename, 'rb') as f:
        data = f.read()
        
    lines = data.split(b'\n')
    print(f"Total binary lines: {len(lines)}")
    
    # 尋找包含 b'1.5' 的行
    for idx, line in enumerate(lines):
        if b'1.5' in line:
            print(f"Line {idx+1}:")
            print(f"  Raw bytes: {line}")
            try:
                print(f"  Decoded (utf-8): {line.decode('utf-8')}")
            except Exception as e:
                print(f"  Decoded (utf-8) failed: {e}")
            try:
                print(f"  Decoded (cp950): {line.decode('cp950')}")
            except Exception as e:
                print(f"  Decoded (cp950) failed: {e}")

if __name__ == '__main__':
    main()
