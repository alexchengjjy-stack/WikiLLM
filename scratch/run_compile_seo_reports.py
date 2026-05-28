# -*- coding: utf-8 -*-
import sys
import os

# 將 scratch 目錄加入 sys.path 以載入 compile_bzs_report.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from compile_bzs_report import compile_markdown_to_bzs_report

def run():
    print("Starting compiling BZS SEO/GEO analysis reports to HTML/PDF templates...")
    
    # 1. 編譯好好簽官網單獨的分析報告 (bzs-website-seo-geo-analysis)
    md_bzs = r"wiki/analyses/bzs-website-seo-geo-analysis.md"
    title_bzs = "BreezySign 好好簽官網 SEO/GEO 深度分析報告"
    subtitle_bzs = "本報告針對好好簽官網技術重構、Schema 結構化資料上線與數發部能量登錄白名單文字同步 Production 正式站後的二次評估成果。"
    out_name_bzs = "bzs-website-seo-geo-analysis"
    
    res_bzs = compile_markdown_to_bzs_report(
        input_md_path=md_bzs,
        output_base_name=out_name_bzs,
        report_title=title_bzs,
        report_subtitle=subtitle_bzs,
        report_no="BZS-SEO-20260527-02",
        plan_no="BZS-ANALYSIS-20260527-02"
    )
    
    # 2. 編譯 4 大官網第三次普查對比報告 (esign-competitor-seo-geo-analysis-20260527)
    md_comp = r"wiki/analyses/esign-competitor-seo-geo-analysis-20260527.md"
    title_comp = "電子簽章 4 大官網第三次 SEO/GEO 雙軌普查與對比報告"
    subtitle_comp = "本報告對台灣電子簽章市場 4 大對外正式官網進行第三次技術與 AI 搜尋能見度 (GEO) 雙軌普查，展示好好簽正式站優化完工後的爆發式領先格局。"
    out_name_comp = "esign-competitor-seo-geo-analysis"
    
    res_comp = compile_markdown_to_bzs_report(
        input_md_path=md_comp,
        output_base_name=out_name_comp,
        report_title=title_comp,
        report_subtitle=subtitle_comp,
        report_no="BZS-COMP-20260527-03",
        plan_no="BZS-ANALYSIS-20260527-03"
    )
    
    # 3. 編譯電子簽章能量登錄競品情報普查快照 (esign-monitoring-snapshot-202605)
    md_snap = r"wiki/analyses/esign-monitoring-snapshot-202605.md"
    title_snap = "電子簽章能量登錄競品情報普查快照 (2026 年 5 月)"
    subtitle_snap = "本期快照依據《普查與情報快照實測規範》對 4 大官網進行全量實地爬取與對齊，整合官網、內容、SEM 廣告與人才招募等六大情報通道。"
    out_name_snap = "esign-monitoring-snapshot-202605"
    
    res_snap = compile_markdown_to_bzs_report(
        input_md_path=md_snap,
        output_base_name=out_name_snap,
        report_title=title_snap,
        report_subtitle=subtitle_snap,
        report_no="BZS-SNAP-20260527-04",
        plan_no="BZS-ANALYSIS-20260527-04"
    )
    
    if res_bzs and res_comp and res_snap:
        print("[SUCCESS] All BZS SEO/GEO reports and Snapshots successfully compiled!")
        print(f"BZS SEO HTML: {res_bzs['html']}")
        print(f"BZS SEO PDF: {res_bzs['pdf']}")
        print(f"Competitor HTML: {res_comp['html']}")
        print(f"Competitor PDF: {res_comp['pdf']}")
        print(f"Snapshot HTML: {res_snap['html']}")
        print(f"Snapshot PDF: {res_snap['pdf']}")
    else:
        print("[ERROR] Some report compilation failed.")

if __name__ == "__main__":
    run()
