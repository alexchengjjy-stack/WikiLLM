# -*- coding: utf-8 -*-
from PIL import Image
import os

def process_logo():
    src_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch\breezysign_logo.png"
    outputs_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs"
    
    png_green = os.path.join(outputs_dir, "bzs-logo-green.png")
    png_white = os.path.join(outputs_dir, "bzs-logo-white.png")
    
    if not os.path.exists(src_path):
        print(f"Error: source image not found at {src_path}")
        return
        
    img = Image.open(src_path)
    
    # 1. 生成無損透明 RGBA 綠色 Logo
    img_rgba = img.convert("RGBA")
    img_rgba.save(png_green, "PNG")
    print(f"[SUCCESS] Green logo saved to: {png_green}")
    
    # 2. 生成無損透明 RGBA 純白色反白 Logo (保留原始 Alpha 進行完美抗鋸齒)
    data = img_rgba.getdata()
    new_data = []
    
    for item in data:
        # item 是 (R, G, B, A)
        r, g, b, a = item
        # 將所有非透明像素的顏色重置為純白色 (255, 255, 255)，保留原始透明度 A
        new_data.append((255, 255, 255, a))
        
    img_white = Image.new("RGBA", img_rgba.size)
    img_white.putdata(new_data)
    img_white.save(png_white, "PNG")
    print(f"[SUCCESS] White logo saved to: {png_white}")
    print(f"Image size: {img_rgba.size}")

if __name__ == "__main__":
    process_logo()
