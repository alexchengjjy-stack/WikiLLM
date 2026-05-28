# -*- coding: utf-8 -*-
import io

def main():
    log_path = "wiki/log.md"
    
    # 讀取日誌內容
    with io.open(log_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. 修正 Frontmatter 與 10:04 標題的合併問題
    bad_frontmatter = 'date_updated: 2026-05-## [2026-05-29 10:04] update | 修正產出 BreezyBrain 產品核心分層架構 v5（以 V3 玻璃卡片中文詳細版為基底，融合發光圖示與 16:9 橫幅比例）'
    good_frontmatter = 'date_updated: 2026-05-29\n---\n\n## [2026-05-29 10:04] update | 修正產出 BreezyBrain 產品核心分層架構 v5（以 V3 玻璃卡片中文詳細版為基底，融合發光圖示與 16:9 橫幅比例）'
    content = content.replace(bad_frontmatter, good_frontmatter)
    
    # 2. 逐行修復，清除 raser.io 殘留的重複行
    lines = content.splitlines()
    new_lines = []
    for line in lines:
        if "raser.io" in line:
            # 清除包含 raser.io 的重複混亂行，改回正確乾淨的描述
            line = "  - **無損 16:9 PNG 生成**：Edge Headless 截圖命令行強制設定 `--window-size=1920,1080`，使卡片在大 Padding 與充足間距下完美呈現，100% 防截斷。"
        new_lines.append(line)
        
    final_content = "\n".join(new_lines) + "\n"
    
    # 寫回檔案
    with io.open(log_path, "w", encoding="utf-8") as f:
        f.write(final_content)
    print("[SUCCESS] log.md repaired successfully.")

if __name__ == "__main__":
    main()
