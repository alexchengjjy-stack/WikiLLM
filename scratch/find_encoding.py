# -*- coding: utf-8 -*-
def main():
    filename = 'wiki/products/breezy-brain/Product-Spec.md'
    with open(filename, 'rb') as f:
        data = f.read()
    
    print(f"File size: {len(data)} bytes")
    
    encodings = ['utf-8', 'cp950', 'utf-16', 'utf-8-sig', 'gbk']
    for enc in encodings:
        print(f"\n--- Trying {enc} ---")
        try:
            text = data.decode(enc)
            print(f"Decoding successful! First 300 characters:")
            print(text[:300])
        except Exception as e:
            print(f"Decoding failed: {e}")

if __name__ == '__main__':
    main()
