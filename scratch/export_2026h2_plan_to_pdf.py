import os
import re
import subprocess
import markdown
import sys

import datetime

# 檔案路徑與命名 (包含日期時間，遵循第 11 條版控規範與使用者防覆蓋規則)
input_md = r"C:\Users\alexc\.gemini\antigravity-ide\brain\b7a0975d-f1ab-44cd-b1df-cf79e79423d6\implementation_plan.md"
template_html = "outputs/bzs-report-template.html"

# 確保輸出目錄存在
os.makedirs("outputs", exist_ok=True)

# 動態產生帶有時間戳記的檔名
now_str = datetime.datetime.now().strftime("%Y%m%d-%H%M")
base_name = f"outputs/{now_str}-bzs-2026h2-cross-department-plan"

output_html = f"{base_name}.html"
output_pdf = f"{base_name}.pdf"

# 衝突檢測：若檔案已存在，則附加 _v1, _v2... 等版次後綴
if os.path.exists(output_html) or os.path.exists(output_pdf):
    version = 1
    while True:
        test_html = f"{base_name}_v{version}.html"
        test_pdf = f"{base_name}_v{version}.pdf"
        if not (os.path.exists(test_html) or os.path.exists(test_pdf)):
            output_html = test_html
            output_pdf = test_pdf
            break
        version += 1

abs_html = os.path.abspath(output_html)
abs_pdf = os.path.abspath(output_pdf)

# 1. 讀取 Markdown 計畫內容
if not os.path.exists(input_md):
    print(f"Error: implementation_plan.md 檔案不存在於路徑 {input_md}")
    sys.exit(1)

with open(input_md, 'r', encoding='utf-8') as f:
    text = f.read()

# 2. 讀取官方 HTML 模板
if not os.path.exists(template_html):
    print(f"Error: 官方 HTML 模板不存在於路徑 {template_html}")
    sys.exit(1)

with open(template_html, 'r', encoding='utf-8') as f:
    template_text = f.read()

# 3. 轉換 MD 為 HTML
html_content = markdown.markdown(text, extensions=['extra', 'codehilite', 'tables'])

# 4. 產品與品牌版型自動化映射演算法 (將 MD 元素無縫對齊官方 CSS 標籤)
# a. 將 <blockquote> 轉換為官方 `.highlight-box` 區塊
html_content = html_content.replace('<blockquote>', '<div class="highlight-box">')
html_content = html_content.replace('</blockquote>', '</div>')

# b. 將 <table> 轉換為官方帶有橫向滾動與邊框的 `.table-responsive` 區塊
html_content = html_content.replace('<table>', '<div class="table-responsive"><table>')
html_content = html_content.replace('</table>', '</table></div>')

# c. 智能切分 H2 大章節，並將其分別打包進精緻的官方 `.glass-card` 中，同時為 H2 套用 `.section-title`
parts = html_content.split('<h2>')
new_html_content = ""

# 第一部分（通常是 H1 與前言），包裹進首張 glass-card 中以求排版整齊
if parts[0].strip():
    # 移除原 Markdown 頂部的 H1，因為官方 header 已經渲染了 H1 標題
    clean_lead = re.sub(r'<h1>.*?</h1>', '', parts[0], flags=re.DOTALL)
    new_html_content += f'<div class="glass-card">{clean_lead}</div>'

# 後續的每一個 H2 大章節
for part in parts[1:]:
    if '</h2>' in part:
        title, body = part.split('</h2>', 1)
        # 包裹入 glass-card 並將標題套用為 section-title
        new_html_content += f"""
        <div class="glass-card">
            <h2 class="section-title">{title}</h2>
            {body}
        </div>
        """
    else:
        new_html_content += part

# 5. 動態擷取官方模板的 Header 與 Footer，完成極致拼接
header_index = template_text.find('</header>') + len('</header>')
footer_index = template_text.find('<footer>')

header_part = template_text[:header_index]
footer_part = template_text[footer_index:]

# 修正 Header 部分的標題與副標題，完美套用官方字體與 Layout
header_part = header_part.replace(
    '<title>BreezySign 好好簽 ． 專用商業簡報與技術報告模板</title>',
    '<title>BreezySign 好好簽 ． 2026H2 跨部門執行計畫 (PLG + SLG 雙軌戰略)</title>'
)
# 精準匹配 bzs-report-template.html 中的實際 h1 標籤
header_part = header_part.replace(
    '<h1>BreezySign 官方報告專用高階商務模板</h1>',
    '<h1>BreezySign 好好簽 ． 2026H2 跨部門執行計畫</h1>'
)
# 精準匹配 bzs-report-template.html 中的實際 subtitle，剔除與本執行無關的歷史去混淆描述
header_part = header_part.replace(
    '<p class="subtitle">本模板專為蒙恬科技電子簽章市場與技術優化小組打造，完美收束 BreezySign 官方視覺識別系統，適用於技術 SEO/GEO 快照與商業提案演示。</p>',
    '<p class="subtitle">本計畫對齊 PLG 與 SLG 雙軌成長戰略，制定 H2 業務、行銷、產品規劃與技術工程 (RD) 可執行之行動方針與財務利潤邊際安全防線。</p>'
)

# 修正 Footer 部分，將其更新為本次計畫的專屬聲明
footer_part = footer_part.replace(
    '<p>報告編號: BZS-TEMPLATE-20260526-01 | 蒙恬科技 (PenPower) 電子簽章市場與技術優化小組 ． 專用高階商務模板</p>',
    '<p>計畫編號: BZS-PLAN-20260527-02 | 蒙恬科技 (PenPower) 好好簽跨部門成果驗證小組 ． 2026H2 跨部門執行計畫 (討論稿)</p>'
)

# 6. 完成拼接
full_html = header_part + new_html_content + footer_part

# 寫入最終的 HTML
with open(output_html, 'w', encoding='utf-8') as f:
    f.write(full_html)
print(f"BreezySign 官方版型 HTML 檔案已順利更正並生成：{abs_html}")

# 7. 尋找 Edge/Chrome 執行檔進行 PDF 編譯
edge_paths = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe"
]

browser_exe = None
for path in edge_paths:
    if os.path.exists(path):
        browser_exe = path
        break

if not browser_exe:
    print("Error: 找不到 Microsoft Edge 或 Google Chrome 瀏覽器，無法轉為 PDF。")
    sys.exit(1)

# 執行 Headless 轉換 PDF
print(f"Using browser: {browser_exe}")
cmd = [
    browser_exe,
    "--headless",
    "--disable-gpu",
    "--run-all-compositor-stages-before-draw",
    f"--print-to-pdf={abs_pdf}",
    f"file:///{abs_html}"
]

print("正在調用 Edge 瀏覽器核心進行 PDF 無損編譯...")
try:
    subprocess.run(cmd, check=True)
    print("PDF 轉檔完美成功！已 100% 成功套用 BreezySign 官方 HTML/PDF 品牌版型！")
    print(f"輸出 PDF 路徑：{abs_pdf}")
except Exception as e:
    print(f"PDF 轉檔失敗：{e}")
    sys.exit(1)
