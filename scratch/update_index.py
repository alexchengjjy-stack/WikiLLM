# -*- coding: utf-8 -*-
import os

def update():
    index_path = r"wiki/index.md"
    if not os.path.exists(index_path):
        print(f"Error: {index_path} not found.")
        return
        
    encodings = ["utf-8-sig", "utf-8", "cp950", "big5", "utf-16"]
    content = None
    used_encoding = None
    
    for enc in encodings:
        try:
            with open(index_path, 'r', encoding=enc) as f:
                content = f.read()
            used_encoding = enc
            print(f"[SUCCESS] Read index.md with encoding: {enc}")
            break
        except Exception:
            continue
            
    if content is None:
        # 終極降級防禦：以 ignore 解碼，避免崩潰
        try:
            with open(index_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            used_encoding = 'utf-8'
            print("[SUCCESS] Read index.md using utf-8 with errors='ignore'")
        except Exception as e:
            print(f"[ERROR] Fatal: cannot read index.md even with ignore: {e}")
            return
        
    # 1. 替換競品報告這行
    old_comp = "  * [電子簽章 4 大官網第二次 SEO/GEO 雙軌普查與對比報告 (2026-05-25)](analyses/esign-competitor-seo-geo-analysis-20260525.md)"
    new_comp = """  * [電子簽章 4 大官網第二次 SEO/GEO 雙軌普查與對比報告 (2026-05-25)](analyses/esign-competitor-seo-geo-analysis-20260525.md)
  * [電子簽章 4 大官網第三次 SEO/GEO 雙軌普查與對比報告 (官網正式上線完工版)](analyses/esign-competitor-seo-geo-analysis-20260527.md) ── 正式站重構完工版對比，好好簽憑藉微格式與 FAQ 完整部署，GEO 中高水準破局領先。"""
    
    if old_comp in content:
        content = content.replace(old_comp, new_comp)
        print("Successfully updated competitor report in index.md")
    else:
        print("Warning: old competitor report line not found in index.md")
        
    # 2. 替換好好簽官網分析報告這行
    old_bzs = "  * [好好簽官網 SEO/GEO 分析](analyses/bzs-website-seo-geo-analysis.md)"
    new_bzs = "  * [BreezySign 好好簽官網 SEO/GEO 深度分析報告 (全新完工版)](analyses/bzs-website-seo-geo-analysis.md) ── 官網重構上線後，技術 SEO 暴增至 9.5，GEO 能見度提升至 7.5，完全消滅薄內容並破局實體混淆。"
    
    if old_bzs in content:
        content = content.replace(old_bzs, new_bzs)
        print("Successfully updated BZS SEO report in index.md")
    else:
        # 容錯匹配
        old_bzs_alt = "  * [BreezySign 好好簽官網 SEO/GEO 深度分析報告 (全新完工版)](analyses/bzs-website-seo-geo-analysis.md)"
        if old_bzs_alt in content:
            content = content.replace(old_bzs_alt, new_bzs)
            print("Successfully updated BZS SEO report (alt line) in index.md")
        else:
            print("Warning: old BZS SEO report line not found in index.md")
            
    # 3. 替換 Outputs 區塊的連結時間戳
    content = content.replace(
        "outputs/20260527-1337-bzs-website-seo-geo-analysis.html",
        "outputs/20260527-1340-bzs-website-seo-geo-analysis.html"
    )
    content = content.replace(
        "outputs/20260527-1337-bzs-website-seo-geo-analysis.pdf",
        "outputs/20260527-1340-bzs-website-seo-geo-analysis.pdf"
    )
    content = content.replace(
        "outputs/20260527-1337-esign-competitor-seo-geo-analysis.html",
        "outputs/20260527-1340-esign-competitor-seo-geo-analysis.html"
    )
    content = content.replace(
        "outputs/20260527-1337-esign-competitor-seo-geo-analysis.pdf",
        "outputs/20260527-1340-esign-competitor-seo-geo-analysis.pdf"
    )
    print("Successfully updated outputs timestamp in index.md content")
            
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("All index.md replacements completed successfully via script in utf-8.")

if __name__ == "__main__":
    update()
