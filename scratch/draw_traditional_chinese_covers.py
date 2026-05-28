import os
import sys
from PIL import Image, ImageDraw, ImageFont

# 定義要處理的圖片與對應的繁體中文文字
images_config = [
    {
        "file": r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs\bzs_blog_travel_cover.png",
        "category": "BreezySign 好好簽 ． 客戶成功案例",
        "title": "旅遊業防漏單大突破 ─ 定型化契約 100% 行動完簽"
    },
    {
        "file": r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs\bzs_blog_real_estate_cover.png",
        "category": "BreezySign 好好簽 ． 場域情境剖析",
        "title": "不動產與建設無紙化 ─ 開啟 80% 高速成交新商機"
    },
    {
        "file": r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs\bzs_blog_finance_loan_cover.png",
        "category": "BreezySign 好好簽 ． 客戶成功案例",
        "title": "貸款代辦信任防線 ─ 聲明錄影簽章防冒名爭議"
    },
    {
        "file": r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs\bzs_blog_moda_approval_cover.png",
        "category": "BreezySign 好好簽 ． 官方重大里程碑",
        "title": "賀！好好簽通過數發部電子簽章服務能量登錄"
    }
]

# 尋找 Windows 預設的繁體中文字型 (微軟正黑粗體)
font_paths = [
    r"C:\Windows\Fonts\msjhbd.ttc",  # Microsoft JhengHei Bold
    r"C:\Windows\Fonts\msjh.ttc",    # Microsoft JhengHei Regular
    r"C:\Windows\Fonts\mingliub.ttc" # MingLiU Bold
]

font_path = None
for path in font_paths:
    if os.path.exists(path):
        font_path = path
        break

if not font_path:
    print("Error: No suitable Traditional Chinese font found on the system.")
    sys.exit(1)

print(f"Using font: {font_path}")

for config in images_config:
    file_path = config["file"]
    if not os.path.exists(file_path):
        print(f"Error: File not found {file_path}")
        continue
        
    print(f"Processing image: {os.path.basename(file_path)}")
    
    # 讀取圖片
    img = Image.open(file_path).convert("RGBA")
    width, height = img.size
    
    # 建立一個半透明層用來畫深色底 bar
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw_overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(draw_overlay)
    
    # 依圖片高度動態決定比例
    bar_height = int(height * 0.22)
    top_y = height - bar_height
    
    # 畫出極具質感的 Slate 深藍半透明背景 bar (rgba(15, 23, 42, 0.85))
    draw.rectangle(
        [(0, top_y), (width, height)],
        fill=(15, 23, 42, 215)
    )
    
    # 在 bar 的頂部加一條好好簽品牌青色裝飾線 (#00d6ff)
    draw.rectangle(
        [(0, top_y), (width, top_y + 4)],
        fill=(0, 214, 255, 255)
    )
    
    # 疊加半透明層
    img = Image.alpha_composite(img, draw_overlay)
    
    # 在圖片上繪製文字
    draw_text = ImageDraw.Draw(img)
    
    # 動態調整字型大小
    cat_size = int(height * 0.038)
    title_size = int(height * 0.052)
    
    try:
        font_cat = ImageFont.truetype(font_path, cat_size)
        font_title = ImageFont.truetype(font_path, title_size)
    except Exception as e:
        print(f"Error loading font: {e}")
        continue
        
    # 文字起點
    padding_x = int(width * 0.05)
    cat_y = top_y + int(bar_height * 0.18)
    title_y = cat_y + int(bar_height * 0.35)
    
    # 1. 繪製分類小字 ─ 使用好好簽品牌青色 (#00d6ff)
    draw_text.text(
        (padding_x, cat_y),
        config["category"].upper(),
        fill=(0, 214, 255, 255),
        font=font_cat
    )
    
    # 2. 繪製主標題 ─ 白色
    draw_text.text(
        (padding_x, title_y),
        config["title"],
        fill=(255, 255, 255, 255),
        font=font_title
    )
    
    # 轉回 RGB 並覆蓋儲存
    final_img = img.convert("RGB")
    final_img.save(file_path, "PNG")
    print(f"  [SUCCESS] Successfully added Traditional Chinese to: {file_path}")

print("All image processing tasks completed successfully.")
