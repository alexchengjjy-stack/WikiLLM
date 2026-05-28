# -*- coding: utf-8 -*-
import os
import subprocess
import sys

def main():
    workspace_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM"
    html_path = os.path.join(workspace_dir, "outputs", "bzs-2026-marketing-strategy-and-funnel.html")
    pdf_path = os.path.join(workspace_dir, "outputs", "bzs-2026-marketing-strategy-and-funnel.pdf")

    if not os.path.exists(html_path):
        print(f"[ERROR] 找不到 HTML 檔案：{html_path}")
        sys.exit(1)

    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. 替換第 124 行 (價值維度 LTV:CAC 舊數據)
    old_target_1 = '<li><strong>2026 年 LTV : CAC = 258 : 1</strong> (業界標準為 3 : 1，此處以匯率 32 換算，CAC 約為 465 NTD)。</li>'
    new_target_1 = """<li><strong>2026 年 LTV : CAC 獲客效率雙軌核算</strong>：
    <ul>
        <li><span style="color: #0284c7; font-weight: 600;">寬口徑 (包含免費個人註冊，CAC 約為 465 NTD)</span>：<code>LTV : CAC = 258 : 1</code>。</li>
        <li><span style="color: #0f172a; font-weight: 600;">窄口徑 (僅限企業註冊 + 聯絡專人，CAC 約為 1,792 NTD)</span>：<code>LTV : CAC = 67 : 1</code>。</li>
    </ul></li>"""

    # 2. 替換第 130 行 (Top Funnel 舊數據)
    old_target_2 = '<li><strong>Top Funnel (廣告觸及 ➔ 註冊試用)</strong>：透過 Pmax 低價曝光與 Search 高轉換率 (6%) 的配合，我們獲得了源源不絕且極為便宜 ($14.52 CPA) 的 Leads。</li>'
    new_target_2 = '<li><strong>Top Funnel (廣告觸及 ➔ 註冊試用)</strong>：透過 Pmax 低價曝光與 Search 高轉換率 (6%) 的配合，我們獲得了源源不絕的 Leads。寬口徑混合 CPA 為極其便宜的 <strong>$14.52 USD</strong> (約 465 NTD)；實質 B2B 窄口徑 CPA 則為 <strong>$56.00 USD</strong> (約 1,792 NTD)，依然處於極佳的獲客回本區間。</li>'

    # 3. 替換第 154 行 (行銷操作建議 Acquisition 舊數據)
    old_target_3 = '<li><strong>推估</strong>：我們的混合獲客成本 (Blended CPA) 僅為 <strong>$14.52 USD</strong> (約 465 NTD)。代表漏斗頂端進件效率極高。</li>'
    new_target_3 = """<li><strong>推估 (CPA 獲客成本雙軌計算)</strong>：
    <ul>
        <li><span style="color: #0284c7; font-weight: 600;">寬口徑 CPA (包含免費個人註冊)</span>：僅為 <strong>$14.52 USD</strong> (約 **465 NTD**)，代表漏斗頂端高流量進件效率極高。</li>
        <li><span style="color: #0f172a; font-weight: 600;">窄口徑 CPA (僅計算企業註冊 + 聯絡專人)</span>：為 <strong>$56.00 USD</strong> (約 **1,792 NTD**)，精確反映了高價值 B2B 企業潛客與實質 SQL 的獨立開發成本。</li>
    </ul></li>"""

    # 4. 替換第 165 行 (行銷操作建議 LTV:CAC 舊數據)
    old_target_4 = '<li><strong>佐證結論</strong>：以匯率 32 換算，CPA 約為 465 NTD。<code>LTV : CAC = 120,000 NTD : 465 NTD = 258 倍</code>。在 SaaS 業界，大於 3 倍即屬健康，258 倍代表我們的行銷預算<strong>投得太保守了</strong>，市場上還有大把便宜的潛在客戶等著我們去買。</li>'
    new_target_4 = """<li><strong>佐證結論 (LTV : CAC 獲客效率雙軌評估)</strong>：
    <ul>
        <li><span style="color: #0284c7; font-weight: 600;">寬口徑計算 (含個人註冊，CAC $465)</span>：<code>LTV : CAC = 120,000 NTD : 465 NTD = 258 倍</code>。</li>
        <li><span style="color: #0f172a; font-weight: 600;">窄口徑計算 (僅限企業註冊+聯絡專人，CAC $1,792) ── [推薦商業決策基準]</span>：<code>LTV : CAC = 120,000 NTD : 1,792 NTD = 67 倍</code>。</li>
    </ul>
    在 SaaS 業界，LTV : CAC 大於 3 倍即屬極度健康，大於 5 倍即屬卓越。好好簽即使只看窄口徑實質 B2B 獲客，高達 <strong>67 倍</strong> 的比例依然代表我們的行銷預算<strong>投得太保守了</strong>，市場上還有大把便宜的潛在企業客戶等著我們去買。</li>"""

    # 執行精準替換
    content = content.replace(old_target_1, new_target_1)
    content = content.replace(old_target_2, new_target_2)
    content = content.replace(old_target_3, new_target_3)
    content = content.replace(old_target_4, new_target_4)

    # 寫入更新後的 HTML 檔案
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[SUCCESS] HTML 看板資料已完成雙軌化更新：{html_path}")

    # Edge Headless PDF 轉檔
    html_url = "file:///" + os.path.abspath(html_path).replace("\\", "/")
    print(f"準備使用 Edge 進行 PDF 轉檔...")
    print(f"HTML 網址為：{html_url}")

    # 尋找 Edge 執行檔
    edge_paths = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        os.path.expandvars(r"%LocalAppData%\Microsoft\Edge\Application\msedge.exe")
    ]
    edge_exe = None
    for p in edge_paths:
        if os.path.exists(p):
            edge_exe = p
            break

    if not edge_exe:
        print("[ERROR] 找不到 Microsoft Edge 執行路徑！請手動完成轉檔。")
        sys.exit(1)

    cmd = [
        edge_exe,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        html_url
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"[SUCCESS] 淺色 PDF 行銷與漏斗報告已成功重新渲染輸出：{pdf_path}")
    except Exception as e:
        print(f"[ERROR] Edge PDF 轉檔失敗：{e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
