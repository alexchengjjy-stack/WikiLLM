# -*- coding: utf-8 -*-
import os

paid_subscribers_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\analyses\bzs\bzs-saas-paid-subscribers-by-plan.md"
funnel_report_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\analyses\bzs\bzs-saas-funnel-ltv-cac-report.md"
complete_report_html_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs\bzs-202605-operations-complete-report.html"

# 1. Update bzs-saas-paid-subscribers-by-plan.md
if os.path.exists(paid_subscribers_path):
    with open(paid_subscribers_path, "r", encoding="utf-8") as f:
        ps_content = f.read()
    
    # Let's insert the sales plan analysis section before "### 相關連結"
    analysis_section = """
## BZS SaaS 各方案銷售佔比與客戶結構對照分析 (2026年5月底統計)

根據 2026 年 5 月底最新正式站營收實績與付費客戶分類，我們對 SaaS 各定價方案的銷售佔比與客戶結構進行了定量對比：

### 1. 金額營收佔比分析 (Revenue Share)
5 月份 SaaS 訂閱實收營收為 **NT$ 84,080**（排除專案與 API 實收 NT$ 281,122）。其銷售佔比呈現高度的「大客拉動」特徵：
* **企業方案 (Enterprise)**：
  - 新購電匯達 **NT$ 60,000** (太平洋旅行社 40人年租單)。
  - 其他企業新客與舊客續期分攤約達 **NT$ 10,000**。
  - **綜合佔比**：約佔 5 月 SaaS 實收總額的 **83.2%**。企業方案無疑是推動好好簽營收增長的絕對主力。
* **專業方案 (Professional) 與商務方案 (Business)**：
  - 新客新購約 **NT$ 3,200**，舊客自動扣款續訂約 **NT$ 10,880**。
  - **綜合佔比**：約佔 5 月 SaaS 實收總額的 **16.8%**。

### 2. 客戶數量結構分析 (Customer Count)
雖然企業方案在營收上佔比超過 8 成，但在「客戶數量結構」上，專業方案才是最廣泛的用戶底座：
* **企業版付費客戶**：累計 **142 家**，佔總付費企業數的 **35.7%**。其特徵為高客單價 (ACV 1.5 萬至 6 萬元不等)，決策鏈長，高度依賴客成引導 Onboarding 與 API/UNIFY 權限需求。
* **專業版付費客戶**：累計 **251 家**，佔總付費客戶的 **63.1%**。其特徵為低單價、月繳為主，多數為小微企業、SOHO 族或自然搜尋流入的自助轉化客戶。
* **API 整合方案客戶**：累計 **5 家**（合信數位、瑋勝、真站電商等），其年約與計量 AATL 費用多直接計入專案/API 實收中。

### 3. 戰略啟示與定價優化建議
* **企業方案是營收飛輪**：太平洋旅行社 6 萬大單的入帳再次證明，爭取一個大客年約的營收效益，大於獲得 200 個專業版月約。行銷資源應傾斜於企業方案 VIP 引流。
* **專業版是產品體驗底座**：251 家專業版客戶為好好簽提供了極佳的口碑基底與自動續期ARR。建議未來將「現場簽」等實用功能下放到專業版年繳方案，以低門檻刺激專業版月約轉換為年繳，鎖定長期留存。
* **API 方案中台化潛力大**：5 家 API 大戶背後代表著極高頻的簽署需求，其一次性對接費用與後續計量 AATL 憑證扣款，是專案營收 (NT$281,122) 的核心支柱。應盡快完善 API SDK 以降低大戶開發阻力。

"""
    
    pos = ps_content.find("## 相關連結")
    if pos != -1:
        updated_ps = ps_content[:pos] + analysis_section + "\n" + ps_content[pos:]
        with open(paid_subscribers_path, "w", encoding="utf-8") as f:
            f.write(updated_ps)
        print("bzs-saas-paid-subscribers-by-plan.md updated successfully.")
    else:
        print("Marker not found in paid subscribers file.")
else:
    print("paid subscribers file not found.")

# 2. Update bzs-saas-funnel-ltv-cac-report.md
if os.path.exists(funnel_report_path):
    with open(funnel_report_path, "r", encoding="utf-8") as f:
        funnel_content = f.read()
    
    # We will insert a section right after the frontmatter and before the first title:
    # "## 🌐 行銷與營運策略全局綜合摘要"
    summary_section = """
## 🌐 行銷與營運策略全局綜合摘要 (Executive Summary)

基於 2026 年 5 月底對外公開之正式站 (Production) 營運實績（總營收 NT$365,202，前 5 個月累計 NT$728,700），我們對好好簽 (BZS) 提出以下行銷與營運策略全局綜合摘要：

### 1. 數據大盤與財務合規核對
- **財務實績卓越**：5 月實收營收 NT$365,202 創歷史新高（MoM +87.49%），主因是線下專案/API 大單與 SaaS 太平洋旅行社年約（NT$60,000）的電匯入帳。
- **對帳口徑契合**：5 月 SaaS 後台扣款金流與客成新購登記完美達成 **$0 落差對齊**（新購 $73.2k + 續訂 $10.88k = 後台實收 $84.08k），對帳機制已步入規範化軌道。

### 2. 獲客與行銷渠道演進
- **從自然搜尋向「多軌並行」演進**：5 月新增註冊達 312 家。Google Ads 寬口徑 CPA 為 $14.52，窄口徑 B2B CPA 為 $56.00。
- **GEO 攔截極為成功**：數發部「113電簽0008」能量登錄與 ISO 認證徽章的正式部署，使好好簽在 ChatGPT / Perplexity 等大模型 GEO 評分提升至 **9.2 領先高位**，精準攔截點點簽漲價流失的大量簽署大客。

### 3. 客戶畫像與產品服務邊界
- **垂直整合需求爆發**：以得勝者（盧森眼科）為代表的醫療 HIS/PACS 座標對接、Dicom 自動轉存與混合雲離線時間戳記校時，成為 SLG 核心需求。
- **大戶範本共享剛需**：太平洋旅行社 40 人年租的導入確立了 **UNIFY 範本權限集中控制**（僅主帳號能自建/分享範本）對中大企業安全管理的剛性價值。
- **技術防禦與利潤保護**：針對聖美麗超過 10MB 的健檢 PDF 文件，嵌入 AATL 數位憑證時易超時失敗。我方主動婉拒年約，劃定了 **10MB 憑證限制防禦邊界**，成功規避低毛利、高維護成本的案件侵蝕淨利。

### 4. 全局營運與行銷決策
- > [!SUCCESS] **戰略定調：大膽放開預算，全力收割競品流失大客**
  - 在嚴格的 B2B 窄口徑下，LTV:CAC 獲客效率高達 **67 倍**，CAC 回本週期 **小於 12 個月**，證明現有行銷投放極度健康。下半年應大膽加碼 Google Ads 競品攔截（建議配比 40%），並與百加資通 BPM 夥伴建立分潤機制，以 API 中台化與無程式碼嵌入加速擴張。

"""
    
    pos = funnel_content.find("## 📈 歷年四大維度演進分析")
    if pos != -1:
        updated_funnel = funnel_content[:pos] + summary_section + "\n" + funnel_content[pos:]
        with open(funnel_report_path, "w", encoding="utf-8") as f:
            f.write(updated_funnel)
        print("bzs-saas-funnel-ltv-cac-report.md updated successfully.")
    else:
        print("Marker not found in funnel report file.")
else:
    print("funnel report file not found.")

# 3. Generate outputs/bzs-202605-operations-complete-report.html
complete_report_html = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>好好簽 (BreezySign) 2026年5月完整營運數據分析及執行報告</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;600;700;800&display=swap');
        
        :root {
            --bg-color: #0b0f17;
            --card-bg: rgba(22, 28, 45, 0.45);
            --card-border: rgba(255, 255, 255, 0.06);
            --text-primary: #f3f4f6;
            --text-secondary: #9ca3af;
            --accent-blue: #3b82f6;
            --accent-green: #10b981;
            --accent-amber: #f59e0b;
            --accent-red: #ef4444;
            --accent-purple: #8b5cf6;
            --glow-blue: rgba(59, 130, 246, 0.15);
        }

        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            background-color: var(--bg-color);
            color: var(--text-primary);
            font-family: 'Inter', sans-serif;
            min-height: 100vh;
            padding: 3rem 2rem;
            line-height: 1.6;
        }

        .container { max-width: 1300px; margin: 0 auto; }
        
        /* Header section */
        header {
            margin-bottom: 3rem;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding-bottom: 2rem;
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
        }
        .header-title h1 {
            font-family: 'Outfit', sans-serif;
            font-size: 2.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, #93c5fd, #3b82f6, #1d4ed8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }
        .header-title p { color: var(--text-secondary); font-size: 1.1rem; }
        .meta-pill {
            background: rgba(59, 130, 246, 0.1);
            border: 1px solid rgba(59, 130, 246, 0.2);
            color: #60a5fa;
            padding: 0.5rem 1.2rem;
            border-radius: 9999px;
            font-size: 0.9rem;
            font-weight: 600;
        }

        /* Layout Cards */
        .section-card {
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 20px;
            padding: 2.5rem;
            backdrop-filter: blur(16px);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
            margin-bottom: 2.5rem;
        }
        h2 {
            font-family: 'Outfit', sans-serif;
            font-size: 1.6rem;
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            gap: 0.8rem;
            border-left: 5px solid var(--accent-blue);
            padding-left: 1rem;
        }

        /* KPI Block */
        .kpi-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }
        .kpi-card {
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.04);
            border-radius: 12px;
            padding: 1.5rem;
            text-align: center;
        }
        .kpi-title { font-size: 0.85rem; color: var(--text-secondary); margin-bottom: 0.5rem; text-transform: uppercase; font-weight: 600; }
        .kpi-value { font-family: 'Outfit', sans-serif; font-size: 2rem; font-weight: 700; margin-bottom: 0.3rem; }
        .kpi-value.blue { color: var(--accent-blue); }
        .kpi-value.green { color: var(--accent-green); }
        .kpi-value.amber { color: var(--accent-amber); }
        .kpi-desc { font-size: 0.8rem; color: var(--text-secondary); }

        /* Tables */
        table { width: 100%; border-collapse: collapse; margin-top: 1rem; }
        th { text-align: left; padding: 1rem; color: var(--text-secondary); font-weight: 600; border-bottom: 1px solid rgba(255, 255, 255, 0.08); font-size: 0.9rem; }
        td { padding: 1rem; border-bottom: 1px solid rgba(255, 255, 255, 0.04); font-size: 0.95rem; }
        tr:last-child td { border-bottom: none; }
        .highlight-row { background: rgba(255, 255, 255, 0.02); font-weight: 600; }

        /* General UI Tags */
        .badge { display: inline-block; padding: 0.25rem 0.6rem; border-radius: 4px; font-size: 0.8rem; font-weight: 600; }
        .badge.green { background: rgba(16, 185, 129, 0.1); color: #34d399; }
        .badge.blue { background: rgba(59, 130, 246, 0.1); color: #60a5fa; }
        .badge.amber { background: rgba(245, 158, 11, 0.1); color: #fbbf24; }
        .badge.red { background: rgba(239, 68, 68, 0.1); color: #f87171; }

        /* Flex Layouts */
        .two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; }
        @media (max-width: 768px) {
            .two-col { grid-template-columns: 1fr; }
        }

        .flow-list { display: flex; flex-direction: column; gap: 1.2rem; }
        .flow-item { border-left: 3px solid rgba(255, 255, 255, 0.08); padding-left: 1.2rem; position: relative; }
        .flow-item::before {
            content: ''; position: absolute; left: -5px; top: 6px; width: 8px; height: 8px; border-radius: 50%; background: var(--accent-blue);
        }
        .flow-title { font-weight: 600; margin-bottom: 0.3rem; display: flex; justify-content: space-between; font-size: 1rem; }
        .flow-desc { font-size: 0.9rem; color: var(--text-secondary); }

        .alert-box {
            background: rgba(239, 68, 68, 0.03);
            border: 1px solid rgba(239, 68, 68, 0.12);
            border-radius: 12px;
            padding: 1.2rem;
            margin-top: 1.5rem;
            font-size: 0.9rem;
            color: #f87171;
        }

        .success-box {
            background: rgba(16, 185, 129, 0.03);
            border: 1px solid rgba(16, 185, 129, 0.12);
            border-radius: 12px;
            padding: 1.2rem;
            margin-top: 1.5rem;
            font-size: 0.9rem;
            color: #34d399;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="header-title">
                <h1>2026年5月好好簽 (BZS) 營運數據分析及執行報告</h1>
                <p>本報告僅基於對外公開之正式站 (Production) 實績，排除所有測試站 (Staging) 數據與未生效項目</p>
            </div>
            <div class="meta-pill">發布日期：2026-06-02</div>
        </header>

        <!-- 板塊一：全局綜合摘要 -->
        <div class="section-card">
            <h2>🌐 一、 行銷與營運策略全局綜合摘要</h2>
            <div class="kpi-grid">
                <div class="kpi-card">
                    <div class="kpi-title">5月實收總營收</div>
                    <div class="kpi-value blue">NT$ 365,202</div>
                    <div class="kpi-desc">MoM 成長 +87.49% (創歷史新高)</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-title">5月SaaS實收 / 對帳落差</div>
                    <div class="kpi-value green">NT$ 84,080 / $0</div>
                    <div class="kpi-desc">SaaS扣款與客成紀錄完美契合</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-title">5月新增註冊公司</div>
                    <div class="kpi-value">312 家</div>
                    <div class="kpi-desc">高意願 Leads 9 家，技術輔導 19 家</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-title">B2B窄口徑 LTV:CAC</div>
                    <div class="kpi-value amber">67 : 1</div>
                    <div class="kpi-desc">回本期 < 12 個月，行銷效率卓越</div>
                </div>
            </div>
            
            <div class="flow-list" style="margin-top: 1.5rem;">
                <div class="flow-item">
                    <div class="flow-title">財務與對帳機制規範化</div>
                    <div class="flow-desc">5 月份成功對齊 SaaS 實收（NT$84,080）與業務新購（NT$73,200）及舊客續期（NT$10,880）之對帳差額，時間差主要在於太平洋大單（6萬）的 5/26 電匯入帳與 6/1 生效。專案實收 NT$281,122 作為一次性對接費用，獨立拆分核算。</div>
                </div>
                <div class="flow-item">
                    <div class="flow-title">GEO攔截與點點簽跳槽紅利</div>
                    <div class="flow-desc">點點簽 4/21 漲價並改以件計費，我方部署數發部能量登錄（113電簽0008）與 ISO27001 認證徽章，使 GEO 大模型評分攀升至 9.2，精準攔截轉單大客（如太平洋旅行社 6 萬年繳吃到飽）。</div>
                </div>
                <div class="flow-item">
                    <div class="flow-title">確立技術防禦與服務邊界</div>
                    <div class="flow-desc">針對聖美麗大於 10MB 的健檢 PDF 文件，嵌入 AATL 憑證易超時失敗。我方主動婉拒年約，確立 10MB 凭證限制防禦邊界，防止低毛利、高維護成本案件侵蝕利潤。</div>
                </div>
            </div>

            <div class="success-box">
                <strong>💡 全局核心決策建議</strong>：在 LTV:CAC 獲客效率高達 67 倍且回本週期小於一年的情況下，財務科學證明我方目前行銷預算「投得太保守了」。下半年應大膽放開預算，加碼點點簽等競品關鍵字攔截（預算配比 40%），並與百加資通 BPM 通路合作，推廣 API 無程式碼元件化。
            </div>
        </div>

        <!-- 板塊二：四大維度演進 -->
        <div class="section-card">
            <h2>📈 二、 SaaS 歷年四大維度與成長漏斗演進</h2>
            <div class="two-col">
                <div>
                    <h3 style="margin-bottom: 1rem; font-size: 1.1rem; color: var(--accent-blue);">1. 獲客與營收雪球演進 (2024 - 2026)</h3>
                    <div class="flow-list">
                        <div class="flow-item">
                            <div class="flow-title">2024 年 (下半年)</div>
                            <div class="flow-desc">總註冊數 2,126 次，實收營收僅 95,400 NTD。主要靠自然流量，以專業版月約為主。</div>
                        </div>
                        <div class="flow-item">
                            <div class="flow-title">2025 年</div>
                            <div class="flow-desc">總註冊數 3,738 次，營收突破百萬，達 1,263,480 NTD。開始出現企業版多授權購買潮。</div>
                        </div>
                        <div class="flow-item">
                            <div class="flow-title">2026 年 (截至 5 月底)</div>
                            <div class="flow-desc">總註冊數 1,620 次，累計入帳達 728,700 NTD。迎來大單轉移潮，ARPU 攀升至 6,000 NTD/年以上。</div>
                        </div>
                    </div>
                </div>
                <div>
                    <h3 style="margin-bottom: 1rem; font-size: 1.1rem; color: var(--accent-blue);">2. 留存防禦與價值核算</h3>
                    <div class="flow-list">
                        <div class="flow-item">
                            <div class="flow-title">PLG Cold Start (冷啟動) 阻力</div>
                            <div class="flow-desc">後台數據顯示 50%~60% 用戶註冊後從未簽署。客成 (CSM) 主動介入（如豐盛富足資產、自強工業基金會）是成功付費轉化的核心因素。</div>
                        </div>
                        <div class="flow-item">
                            <div class="flow-title">LTV & CAC 雙軌獲客效益</div>
                            <div class="flow-desc">單一客戶終身價值 (LTV) 約 120,000 NTD。寬口徑下獲客效率為 258 倍；嚴格 B2B 窄口徑下（CAC $1,792）獲客效率仍高達 67 倍，遠超 3 倍行業標準。</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- 板塊三：客戶獲取管道分析 -->
        <div class="section-card">
            <h2>🚀 三、 好好簽 (BZS) 客戶獲取管道分析與漏斗演進</h2>
            <table>
                <thead>
                    <tr>
                        <th>管道類型</th>
                        <th>獲客管道</th>
                        <th>5月表現 / Leads 指標</th>
                        <th>營收與財務貢獻</th>
                        <th>已成交代表案例 (Production)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>SLG / 通路</strong></td>
                        <td>SI & ISV 生態系分銷</td>
                        <td>方鼎 HIS、商之器 PACS 等 API 整合討論</td>
                        <td class="success">佔 5 月總營收 77% (NT$281,122)</td>
                        <td>101客戶地端 BPM 交付、得勝者 PACS</td>
                    </tr>
                    <tr>
                        <td><strong>Inbound / 廣告</strong></td>
                        <td>Google Ads (Search + Pmax)</td>
                        <td>新增註冊 312 家；窄口徑 B2B CPA $56.00</td>
                        <td>SaaS 新購主力來源</td>
                        <td>太平洋旅行社 (NT$60k 年繳吃到飽)</td>
                    </tr>
                    <tr>
                        <td><strong>Inbound / 自然</strong></td>
                        <td>Google 自然搜尋 (SEO)</td>
                        <td>自然搜尋佔 Inbound 流量 50% 以上</td>
                        <td>奠定舊客自動續期 (ARR) 流量底座</td>
                        <td>聯尚有限公司、新合不動產</td>
                    </tr>
                    <tr>
                        <td><strong>GEO / 語意</strong></td>
                        <td>大模型 AI 搜尋推薦 (GEO)</td>
                        <td>GEO 能見度評分達 9.2/10 (破局領先)</td>
                        <td>攔截點點簽漲價轉移流量之關鍵</td>
                        <td>太平洋旅行社、豐盛富足資產</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- 板塊四：各方案佔比對照與 CSM -->
        <div class="section-card">
            <h2>📊 四、 SaaS 各方案銷售佔比與客成 (CSM) 對照分析</h2>
            <div class="two-col">
                <div>
                    <h3 style="margin-bottom: 1rem; font-size: 1.1rem; color: var(--accent-blue);">1. 5月 SaaS 方案銷售金額佔比</h3>
                    <table>
                        <thead>
                            <tr>
                                <th>方案名稱</th>
                                <th>5月實收金額</th>
                                <th>銷售佔比</th>
                                <th>特徵與定位</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>企業方案 (Enterprise)</strong></td>
                                <td class="success">NT$ 70,000+</td>
                                <td class="success">83.2%</td>
                                <td>新購大客為主（如太平洋年費 6 萬），營收飛輪。</td>
                            </tr>
                            <tr>
                                <td><strong>專業方案 (Professional)</strong></td>
                                <td>NT$ 14,080</td>
                                <td>16.8%</td>
                                <td>家數佔 63% 為主，自動扣繳，穩定的續約底座。</td>
                            </tr>
                            <tr>
                                <td><strong>商務與 API 方案</strong></td>
                                <td>-</td>
                                <td>-</td>
                                <td>API 費用計入專案實收，客單高。</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div>
                    <h3 style="margin-bottom: 1rem; font-size: 1.1rem; color: var(--accent-blue);">2. 客成 (CSM) 商機跟進結案狀態</h3>
                    <div class="flow-list">
                        <div class="flow-item">
                            <div class="flow-title">
                                <span>太平洋旅行社</span>
                                <span class="badge green">已成交</span>
                            </div>
                            <div class="flow-desc">已付款 6 萬訂閱 40 人企業版年約，6/1 生效。開通 UNIFY 共享範本權限控管。</div>
                        </div>
                        <div class="flow-item">
                            <div class="flow-title">
                                <span>行天宮恩主公醫院</span>
                                <span class="badge red">婉拒結案 (5/20)</span>
                            </div>
                            <div class="flow-desc">諮詢院內 AIO 簽名板 HIS 對接。因院方預算已滿暫無資源，已婉拒結案。</div>
                        </div>
                        <div class="flow-item">
                            <div class="flow-title">
                                <span>聖美麗健康管理</span>
                                <span class="badge red">婉拒結案 (5月)</span>
                            </div>
                            <div class="flow-desc">評估年約。因大檔案 (28MB) 憑證嵌入易超時失敗。我方主動婉拒，確立 10MB 防禦邊界。</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

with open(complete_report_html_path, "w", encoding="utf-8") as f:
    f.write(complete_report_html)
print("Complete report HTML created.")

print("All tasks completed successfully.")
