# -*- coding: utf-8 -*-
def main():
    filename = 'wiki/products/breezy-brain/Product-Spec.md'
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    print(f"Total lines: {len(lines)}")
    # 列印 45 到 95 行 (1-based index 46 到 96)
    for idx in range(45, min(len(lines), 95)):
        print(f"{idx+1}: {repr(lines[idx])}")

if __name__ == '__main__':
    main()
