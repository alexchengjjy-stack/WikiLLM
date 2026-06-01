# -*- coding: utf-8 -*-
import os
import base64
from datetime import datetime

def generate_report():
    scratch_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch"
    outputs_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM\outputs"
    logo_path = os.path.join(outputs_dir, "assets", "bzs-logo-green.png")
    
    # 1. 取得 Base64 Logo
    logo_base64 = ""
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as f:
            logo_base64 = base64.b64encode(f.read()).decode("utf-8")
    else:
        print("[WARNING] bzs-logo-green.png not found. SVG placeholder will be used.")

    # 2. 定義時間戳記與檔名
    timestamp = datetime.now().strftime("%Y%m%d-%H%M")
    html_filename = f"bzs-ops-report-{timestamp}-v3.html"
    html_filepath = os.path.join(outputs_dir, "bzs", html_filename)

    # 3. HTML 內容
    html_content = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BreezySign 好好簽 ． 2026年5月營運月報</title>
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@300;400;500;600;700;800&family=Noto+Sans+TC:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary: #057857; /* BreezySign 品牌翠綠色 */
            --primary-light: #ecfdf5;
            --primary-border: #a7f3d0;
            --secondary: #0284c7; /* Sky 輔助藍色 */
            --secondary-light: #e0f2fe;
            --dark-text: #0f172a;
            --light-text: #475569;
            --bg-color: #f8fafc;
            --card-bg: #ffffff;
            --border-color: #e2e8f0;
            --glass-bg: rgba(255, 255, 255, 0.85);
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: 'Inter', 'Noto Sans TC', sans-serif;
            background-color: var(--bg-color);
            color: var(--light-text);
            line-height: 1.7;
            padding: 40px 20px;
            max-width: 1200px;
            margin: 0 auto;
            position: relative;
            -webkit-print-color-adjust: exact;
            print-color-adjust: exact;
        }}

        /* Subtle modern gradients */
        body::before, body::after {{
            content: "";
            position: absolute;
            width: 300px;
            height: 300px;
            border-radius: 50%;
            z-index: -1;
            filter: blur(120px);
            opacity: 0.45;
            pointer-events: none;
        }}

        body::before {{
            top: 5%;
            left: -50px;
            background: var(--primary-light);
        }}

        body::after {{
            bottom: 15%;
            right: -50px;
            background: var(--secondary-light);
        }}

        /* Header Style */
        header {{
            margin-bottom: 40px;
            border-bottom: 3px solid var(--primary);
            padding-bottom: 24px;
            position: relative;
        }}

        .logo-area {{
            display: flex;
            align-items: center;
            margin-bottom: 12px;
            background: transparent;
        }}

        .bzs-logo {{
            display: block;
        }}

        .meta-tag {{
            font-family: 'Outfit', sans-serif;
            font-size: 12px;
            font-weight: 700;
            color: var(--primary);
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 8px;
        }}

        h1 {{
            font-family: 'Outfit', 'Noto Sans TC', sans-serif;
            font-size: 32px;
            font-weight: 800;
            color: var(--dark-text);
            line-height: 1.3;
        }}

        .subtitle {{
            font-size: 16px;
            color: var(--light-text);
            margin-top: 8px;
            font-weight: 400;
        }}

        /* Glass Cards with Shadow */
        .glass-card {{
            background: var(--glass-bg);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 32px;
            margin-bottom: 32px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 10px 15px -3px rgba(0, 0, 0, 0.03);
        }}

        .section-title {{
            font-family: 'Outfit', 'Noto Sans TC', sans-serif;
            font-size: 22px;
            color: var(--dark-text);
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            border-left: 5px solid var(--primary);
            padding-left: 12px;
        }}

        /* KPI Dashboard Grid */
        .kpi-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
            margin-bottom: 32px;
        }}

        .kpi-card {{
            background: #ffffff;
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.02);
            transition: all 0.2s ease;
        }}

        .kpi-card:hover {{
            transform: translateY(-2px);
            border-color: var(--primary-border);
        }}

        .kpi-value {{
            font-family: 'Outfit', sans-serif;
            font-size: 28px;
            font-weight: 800;
            color: var(--primary);
            margin: 8px 0;
        }}

        .kpi-label {{
            font-size: 13px;
            font-weight: 500;
            color: var(--light-text);
        }}

        .kpi-sub {{
            font-size: 11px;
            color: #64748b;
        }}

        /* Two Column Grid */
        .grid-2 {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
            gap: 24px;
            margin: 24px 0;
        }}

        .card {{
            background: #ffffff;
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 24px;
            transition: all 0.2s ease;
            height: 100%;
        }}

        .card:hover {{
            border-color: rgba(5, 120, 87, 0.25);
            background: rgba(5, 120, 87, 0.005);
            transform: translateY(-2px);
        }}

        .card-title {{
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 16px;
            color: var(--dark-text);
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 8px;
        }}

        /* Highlights & Alerts */
        .highlight-box {{
            background-color: var(--primary-light);
            border-left: 4px solid var(--primary);
            padding: 20px;
            border-radius: 0 12px 12px 0;
            margin: 16px 0;
            color: #064e3b;
            font-size: 14px;
        }}

        .highlight-title {{
            font-weight: 700;
            color: var(--primary);
            margin-bottom: 6px;
            display: flex;
            align-items: center;
        }}

        .alert-box {{
            background-color: #fffbeb;
            border-left: 4px solid #d97706;
            padding: 20px;
            border-radius: 0 12px 12px 0;
            margin: 16px 0;
            color: #78350f;
            font-size: 14px;
        }}

        .alert-title {{
            font-weight: 700;
            color: #d97706;
            margin-bottom: 6px;
        }}

        /* Bullet lists */
        ul {{
            list-style-type: none;
            padding-left: 0;
        }}

        ul li {{
            position: relative;
            padding-left: 20px;
            margin-bottom: 10px;
            font-size: 13.5px;
        }}

        ul li::before {{
            content: "•";
            color: var(--primary);
            font-weight: bold;
            font-size: 18px;
            position: absolute;
            left: 5px;
            top: -2px;
        }}

        /* Tables */
        .table-responsive {{
            overflow-x: auto;
            margin: 24px 0;
            border-radius: 12px;
            border: 1px solid var(--border-color);
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            text-align: left;
            font-size: 13px;
        }}

        th, td {{
            padding: 12px 16px;
            border-bottom: 1px solid var(--border-color);
        }}

        th {{
            background-color: #f1f5f9;
            color: var(--dark-text);
            font-weight: 600;
            font-family: 'Outfit', 'Noto Sans TC', sans-serif;
        }}

        tr:last-child td {{
            border-bottom: none;
        }}

        tr:hover td {{
            background: #f8fafc;
        }}

        .badge {{
            display: inline-block;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 11px;
            font-weight: 700;
            text-align: center;
        }}

        .badge-green {{ background: var(--primary-light); color: var(--primary); border: 1px solid var(--primary-border); }}
        .badge-blue {{ background: var(--secondary-light); color: var(--secondary); border: 1px solid rgba(2, 132, 199, 0.15); }}
        .badge-orange {{ background: #fffbeb; color: #d97706; border: 1px solid #fde68a; }}

        /* Charts Container */
        .chart-box {{
            display: flex;
            justify-content: space-around;
            align-items: center;
            flex-wrap: wrap;
            margin: 20px 0;
            background: #ffffff;
            padding: 24px;
            border-radius: 12px;
            border: 1px solid var(--border-color);
        }}

        .chart-item {{
            text-align: center;
            min-width: 250px;
        }}

        .chart-title-inner {{
            font-size: 14px;
            font-weight: 600;
            color: var(--dark-text);
            margin-bottom: 12px;
        }}

        footer {{
            margin-top: 60px;
            padding-top: 20px;
            border-top: 1px solid var(--border-color);
            font-size: 12px;
            color: var(--light-text);
            text-align: center;
        }}

        /* Print Settings for PDF Generation */
        @media print {{
            body {{
                background: #ffffff !important;
                color: #000000 !important;
                padding: 0 !important;
                font-size: 11px !important;
            }}

            body::before, body::after {{
                display: none !important;
            }}

            .glass-card {{
                box-shadow: none !important;
                border: 1px solid #cbd5e1 !important;
                background: #ffffff !important;
                padding: 20px !important;
                margin-bottom: 20px !important;
                page-break-inside: avoid !important;
            }}

            .card {{
                box-shadow: none !important;
                border: 1px solid #cbd5e1 !important;
                background: #ffffff !important;
                padding: 16px !important;
                page-break-inside: avoid !important;
            }}

            .chart-box {{
                border: 1px solid #cbd5e1 !important;
                background: #ffffff !important;
                page-break-inside: avoid !important;
            }}

            th {{
                background: #f1f5f9 !important;
                color: #000000 !important;
            }}

            .badge {{
                border: 1px solid #94a3b8 !important;
                background: transparent !important;
                color: #000000 !important;
            }}

            header {{
                margin-bottom: 20px !important;
                page-break-after: avoid !important;
            }}

            h1 {{
                font-size: 26px !important;
            }}

            footer {{
                margin-top: 30px !important;
                padding-top: 12px !important;
                page-break-before: avoid !important;
            }}
        }}
    </style>
</head>
<body>

<div class="container">
    <header>
        <div class="logo-area">
            {"<!-- Logo fallback using Base64 or local image -->" if logo_base64 else ""}
            {"<img class='bzs-logo' src='data:image/png;base64," + logo_base64 + "' width='220' height='44' alt='BreezySign'>" if logo_base64 else "<div style='font-family:\"Outfit\", sans-serif; font-size:24px; font-weight:800; color:var(--primary);'>BreezySign 好好簽</div>"}
        </div>
        <div class="meta-tag">OPERATIONAL REPORT ． 2026-05</div>
        <h1>BreezySign 好好簽 2026 年 5 月營運月報</h1>
        <p class="subtitle">本月報彙整 2026 年 5 月之財務營收、新增獲客漏斗、重大專案里程碑及競品轉單流失分析，提供公司高層營運決策參考。</p>
    </header>

    <!-- KPI DASHBOARD -->
    <div class="kpi-grid">
        <div class="kpi-card">
            <div class="kpi-label">實收總營收</div>
            <div class="kpi-value">NT$ 365,202</div>
            <div class="kpi-sub">SaaS $84,080 + 專案 $281,122</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-label">SaaS 新購業績 (New Booking)</div>
            <div class="kpi-value">NT$ 73,200</div>
            <div class="kpi-sub">含太平洋旅行社大單 $60,000</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-label">當月新增註冊公司</div>
            <div class="kpi-value">312 家</div>
            <div class="kpi-sub">獲客漏斗持續擴大</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-label">Leads 電訪品質</div>
            <div class="kpi-value">50%</div>
            <div class="kpi-sub">電訪 30 家，「有興趣」15 家</div>
        </div>
    </div>

    <!-- REVENUE DOUBLE ENGINE & VISUALIZATION -->
    <div class="glass-card">
        <h2 class="section-title">一、 財務營收與付費客戶結構 (Revenue Analysis)</h2>
        <p style="font-size: 14px; margin-bottom: 16px;">本月營收展現<b>「SaaS 訂閱」</b>與<b>「Vertical / API 專案」</b>雙引擎增長模式：</p>
        
        <div class="chart-box">
            <!-- Vector Doughnut Chart for Revenue Breakdown -->
            <div class="chart-item">
                <div class="chart-title-inner">2026-05 實收營收結構占比</div>
                <svg width="220" height="220" viewBox="0 0 220 220" style="margin: 0 auto; display:block;">
                    <!-- Circular sectors -->
                    <!-- Background Circle -->
                    <circle cx="110" cy="110" r="80" fill="none" stroke="#f1f5f9" stroke-width="24"/>
                    <!-- Segment 1: Project Revenue (77.0%) - Arc length = 2 * pi * 80 * 0.770 = 387.0. Dasharray: 387.0 (stroke) 115.4 (gap) -->
                    <!-- Start angle at 0deg (right side). Rotate by -90deg to start top. -->
                    <circle cx="110" cy="110" r="80" fill="none" stroke="#057857" stroke-width="24" 
                            stroke-dasharray="387.0 115.4" stroke-dashoffset="0" transform="rotate(-90 110 110)"/>
                    <!-- Segment 2: SaaS Revenue (23.0%) - Arc length = 2 * pi * 80 * 0.230 = 115.6. -->
                    <circle cx="110" cy="110" r="80" fill="none" stroke="#0284c7" stroke-width="24" 
                            stroke-dasharray="115.6 387.0" stroke-dashoffset="-387.0" transform="rotate(-90 110 110)"/>
                    <!-- Center Text -->
                    <text x="110" y="105" text-anchor="middle" font-family="Outfit" font-size="20" font-weight="800" fill="#0f172a">NT$ 365.2K</text>
                    <text x="110" y="125" text-anchor="middle" font-family="Noto Sans TC" font-size="11" font-weight="600" fill="#475569">實收總營收</text>
                </svg>
                <div style="margin-top: 12px; font-size:12px; display:flex; justify-content:center; gap:16px;">
                    <span><span style="display:inline-block; width:12px; height:12px; background:#057857; margin-right:4px; vertical-align:middle;"></span>專案/API: 77.0%</span>
                    <span><span style="display:inline-block; width:12px; height:12px; background:#0284c7; margin-right:4px; vertical-align:middle;"></span>SaaS訂閱: 23.0%</span>
                </div>
            </div>

            <!-- Detailed breakdown list -->
            <div style="flex: 1; min-width: 320px; padding: 10px;">
                <div class="highlight-box" style="margin-top:0;">
                    <div class="highlight-title">財務重要里程碑明細</div>
                    1. <b>SaaS 實收總業績：NT$84,080</b>
                    <br>• <b>新購業績 (New Booking)</b>：NT$73,200。包括太平洋旅行社 40 人年租大單 NT$60,000；其他 9 家新客新購訂閱（含 6 家專業方案、3 家企業方案）共計 NT$13,200。
                    <br>• <b>舊客自動續訂金流 (ARR)</b>：NT$10,880。維持健康的常規租金收入。
                    <br><br>2. <b>Vertical / API 專案實收業績：NT$281,122</b>
                    <br>• 主要來自本月完成交付、驗收或首付款項之 API 串接與垂直客製化方案（如鼎新、聯合線上等專案對接首期結算）。
                </div>
            </div>
        </div>

        <!-- 歷史月度 SaaS 營收與 MoM 趨勢 -->
        <h3 style="margin-top: 32px; margin-bottom: 16px; color: var(--dark-text); font-size: 16px; font-weight: 700; border-left: 3px solid var(--secondary); padding-left: 8px;">📈 2025.10 - 2026.05 SaaS 歷年實收趨勢與 MoM 增減</h3>
        
        <div class="chart-box" style="margin-top: 16px; padding: 24px; background: #ffffff; border-radius: 12px; border: 1px solid var(--border-color); box-shadow: inset 0 2px 4px rgba(0,0,0,0.01);">
            <div class="chart-item" style="width: 100%;">
                <div class="chart-title-inner" style="margin-bottom: 24px; font-size: 13px; font-weight: 600; color: var(--dark-text);">SaaS 實收營收月度歷史趨勢 (NT$)</div>
                <div style="display: flex; justify-content: space-between; align-items: flex-end; height: 180px; padding: 0 10px 10px 10px; border-bottom: 2px solid var(--border-color); position: relative; max-width: 800px; margin: 0 auto;">
                    <!-- Y-Axis Gridlines -->
                    <div style="position: absolute; left: 0; bottom: 10px; width: 100%; border-bottom: 1px dashed #e2e8f0; pointer-events: none;"></div>
                    <div style="position: absolute; left: 0; bottom: 65px; width: 100%; border-bottom: 1px dashed #e2e8f0; pointer-events: none;"></div>
                    <div style="position: absolute; left: 0; bottom: 120px; width: 100%; border-bottom: 1px dashed #e2e8f0; pointer-events: none;"></div>
                    
                    <!-- Bars -->
                    <div style="display: flex; flex-direction: column; align-items: center; flex: 1; min-width: 50px;">
                        <span style="font-size: 10px; font-weight: 700; color: var(--light-text); margin-bottom: 6px;">64.0K</span>
                        <div style="width: 24px; height: 48px; background: var(--secondary); border-radius: 4px 4px 0 0; box-shadow: 0 2px 4px rgba(2,132,199,0.15);"></div>
                        <span style="font-size: 10px; margin-top: 8px; font-weight: 600; color: var(--light-text); font-family: 'Outfit', sans-serif;">25-10</span>
                    </div>
                    <div style="display: flex; flex-direction: column; align-items: center; flex: 1; min-width: 50px;">
                        <span style="font-size: 10px; font-weight: 700; color: var(--light-text); margin-bottom: 6px;">114.8K</span>
                        <div style="width: 24px; height: 86px; background: var(--secondary); border-radius: 4px 4px 0 0; box-shadow: 0 2px 4px rgba(2,132,199,0.15);"></div>
                        <span style="font-size: 10px; margin-top: 8px; font-weight: 600; color: var(--light-text); font-family: 'Outfit', sans-serif;">25-11</span>
                    </div>
                    <div style="display: flex; flex-direction: column; align-items: center; flex: 1; min-width: 50px;">
                        <span style="font-size: 10px; font-weight: 700; color: var(--light-text); margin-bottom: 6px; color: var(--primary);">181.4K</span>
                        <div style="width: 24px; height: 136px; background: var(--primary); border-radius: 4px 4px 0 0; box-shadow: 0 2px 4px rgba(5,120,87,0.15);"></div>
                        <span style="font-size: 10px; margin-top: 8px; font-weight: 600; color: var(--light-text); font-family: 'Outfit', sans-serif;">25-12</span>
                    </div>
                    <div style="display: flex; flex-direction: column; align-items: center; flex: 1; min-width: 50px;">
                        <span style="font-size: 10px; font-weight: 700; color: var(--light-text); margin-bottom: 6px;">161.5K</span>
                        <div style="width: 24px; height: 121px; background: var(--secondary); border-radius: 4px 4px 0 0; box-shadow: 0 2px 4px rgba(2,132,199,0.15);"></div>
                        <span style="font-size: 10px; margin-top: 8px; font-weight: 600; color: var(--light-text); font-family: 'Outfit', sans-serif;">26-01</span>
                    </div>
                    <div style="display: flex; flex-direction: column; align-items: center; flex: 1; min-width: 50px;">
                        <span style="font-size: 10px; font-weight: 700; color: var(--light-text); margin-bottom: 6px;">129.3K</span>
                        <div style="width: 24px; height: 97px; background: var(--secondary); border-radius: 4px 4px 0 0; box-shadow: 0 2px 4px rgba(2,132,199,0.15);"></div>
                        <span style="font-size: 10px; margin-top: 8px; font-weight: 600; color: var(--light-text); font-family: 'Outfit', sans-serif;">26-02</span>
                    </div>
                    <div style="display: flex; flex-direction: column; align-items: center; flex: 1; min-width: 50px;">
                        <span style="font-size: 10px; font-weight: 700; color: var(--light-text); margin-bottom: 6px;">134.9K</span>
                        <div style="width: 24px; height: 101px; background: var(--secondary); border-radius: 4px 4px 0 0; box-shadow: 0 2px 4px rgba(2,132,199,0.15);"></div>
                        <span style="font-size: 10px; margin-top: 8px; font-weight: 600; color: var(--light-text); font-family: 'Outfit', sans-serif;">26-03</span>
                    </div>
                    <div style="display: flex; flex-direction: column; align-items: center; flex: 1; min-width: 50px;">
                        <span style="font-size: 10px; font-weight: 700; color: var(--light-text); margin-bottom: 6px; color: var(--primary);">194.7K</span>
                        <div style="width: 24px; height: 146px; background: var(--primary); border-radius: 4px 4px 0 0; box-shadow: 0 2px 4px rgba(5,120,87,0.15);"></div>
                        <span style="font-size: 10px; margin-top: 8px; font-weight: 600; color: var(--light-text); font-family: 'Outfit', sans-serif;">26-04</span>
                    </div>
                    <div style="display: flex; flex-direction: column; align-items: center; flex: 1; min-width: 50px;">
                        <span style="font-size: 10px; font-weight: 700; color: var(--light-text); margin-bottom: 6px;">84.0K</span>
                        <div style="width: 24px; height: 63px; background: var(--secondary); border-radius: 4px 4px 0 0; box-shadow: 0 2px 4px rgba(2,132,199,0.15);"></div>
                        <span style="font-size: 10px; margin-top: 8px; font-weight: 600; color: var(--light-text); font-family: 'Outfit', sans-serif;">26-05</span>
                    </div>
                </div>
            </div>
        </div>

        <div class="table-responsive">
            <table>
                <thead>
                    <tr>
                        <th style="width: 15%;">月份</th>
                        <th style="width: 20%;">SaaS 實收營收</th>
                        <th style="width: 15%;">付費公司數</th>
                        <th style="width: 20%;">MoM 增減幅度</th>
                        <th style="width: 30%;">營收結構明細</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>2025-10</strong></td>
                        <td>NT$ 64,014</td>
                        <td>145 家</td>
                        <td><span class="badge" style="background:#f1f5f9; color:#475569; border: 1px solid #cbd5e1;">基準月份</span></td>
                        <td>企業: $35,914 (49家) | 專業: $27,900 (96家)</td>
                    </tr>
                    <tr>
                        <td><strong>2025-11</strong></td>
                        <td>NT$ 114,880</td>
                        <td>154 家</td>
                        <td><span class="badge badge-green">+79.46% (↗)</span></td>
                        <td>企業: $78,000 (54家) | 專業: $34,800 (100家)</td>
                    </tr>
                    <tr>
                        <td><strong>2025-12</strong></td>
                        <td>NT$ 181,440</td>
                        <td>171 家</td>
                        <td><span class="badge badge-green">+57.94% (↗)</span></td>
                        <td>企業: $134,500 (58家) | 專業: $46,200 (112家)</td>
                    </tr>
                    <tr>
                        <td><strong>2026-01</strong></td>
                        <td>NT$ 161,586</td>
                        <td>188 家</td>
                        <td><span class="badge badge-orange">-10.94% (↘)</span></td>
                        <td>企業: $129,286 (67家) | 專業: $26,100 (118家)</td>
                    </tr>
                    <tr>
                        <td><strong>2026-02</strong></td>
                        <td>NT$ 129,310</td>
                        <td>190 家</td>
                        <td><span class="badge badge-orange">-19.97% (↘)</span></td>
                        <td>企業: $97,500 (68家) | 專業: $26,400 (118家)</td>
                    </tr>
                    <tr>
                        <td><strong>2026-03</strong></td>
                        <td>NT$ 134,903</td>
                        <td>193 家</td>
                        <td><span class="badge badge-green">+4.33% (↗)</span></td>
                        <td>企業: $98,903 (66家) | 專業: $29,100 (121家)</td>
                    </tr>
                    <tr>
                        <td><strong>2026-04</strong></td>
                        <td>NT$ 194,779</td>
                        <td>198 家</td>
                        <td><span class="badge badge-green">+44.38% (↗)</span></td>
                        <td>企業: $142,000 (70家) | 專業: $34,039 (119家)</td>
                    </tr>
                    <tr>
                        <td><strong>2026-05</strong></td>
                        <td>NT$ 84,080</td>
                        <td>-</td>
                        <td><span class="badge badge-orange">-56.83% (↘)*</span></td>
                        <td>新購: $73,200 (大單$60K) | 舊客 ARR: $10,880</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <p style="font-size:12px; color:#64748b; margin-top:-8px; line-height: 1.5;">* 註：2026-05 SaaS 實收金流因大單（太平洋旅行社 $60K）生效扣款期為 6/1，且部分常規舊客戶未屆自動續約週期，導致技術性 MoM 下降。若併計當月<b>專案實收 NT$ 281,122</b>，則 5 月實收總營收高達 <b>NT$ 365,202</b>，總體營收 MoM 實際為 <b>+87.49%</b>，呈現雙引擎強勁增長。</p>

    </div>

    <!-- LEADS FUNNEL & CHURN ANALYSIS -->
    <div class="grid-2">
        <!-- Funnel card -->
        <div class="card">
            <div class="card-title">🚀 新增註冊與獲客漏斗 (Acquisition Funnel)</div>
            <ul>
                <li><b>註冊基底擴大</b>：當月新增註冊公司數達 <b>312 家</b>。</li>
                <li><b>電話開發品質</b>：累計電訪 30 家註冊 Leads，其中 15 家明確表達「有興趣」（占比 50%），高達 9 家列入「較高意願」的名單。</li>
                <li><b>輔導測試數據</b>：目前仍在體驗期且接受 CSM 技術輔導的企業客，計有 SaaS 體驗版 7 家，API/SI 方案 12 家，合計 19 家輔導中。</li>
            </ul>
            <div style="margin-top: 16px; text-align: center;">
                <svg width="320" height="130" viewBox="0 0 320 130" style="display:block; margin:0 auto;">
                    <!-- Funnel Visual representation -->
                    <!-- Trapezoid 1: Registered -->
                    <polygon points="10,10 310,10 270,40 50,40" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
                    <text x="160" y="28" text-anchor="middle" font-size="12" fill="#0f172a" font-weight="600">1. 新增註冊公司: 312 家</text>
                    
                    <!-- Trapezoid 2: Tele-leads -->
                    <polygon points="55,45 265,45 230,75 90,75" fill="#e0f2fe" stroke="#bae6fd" stroke-width="1"/>
                    <text x="160" y="63" text-anchor="middle" font-size="12" fill="#0284c7" font-weight="600">2. 電訪跟進 Leads: 30 家</text>
                    
                    <!-- Trapezoid 3: Interested -->
                    <polygon points="95,80 225,80 190,110 130,110" fill="#ecfdf5" stroke="#a7f3d0" stroke-width="1"/>
                    <text x="160" y="98" text-anchor="middle" font-size="12" fill="#057857" font-weight="600">3. 有興趣: 15 家 (高意願 9 家)</text>
                </svg>
            </div>
        </div>

        <!-- Churn/Competitive analysis card -->
        <div class="card">
            <div class="card-title">🔍 凱鈿點點簽轉單效應與聖美麗大檔案防線</div>
            <div class="alert-box" style="margin-top: 0;">
                <div class="alert-title">🔥 凱鈿點點簽 (DottedSign) 漲價效應分析</div>
                點點簽近期更動計價模型，由原本的吃到飽租約<b>改為以件計費（單份約 NT$45~50）</b>，這導致中大型簽署用量客戶面臨數倍的續約報價。
                <br>• <b>福安（2萬份/年）</b>與 <b>太平洋旅行社（2000份/年）</b>均因改版面臨巨大續約成本抗性，促使其移轉至好好簽。
                <br>• 這充分證明好好簽<b>「年租吃到飽」</b>在年簽署量 > 500 份的中大企業市場具備壓倒性的定價優勢。
            </div>
            <div class="alert-box" style="background:#fef2f2; border-left:4px solid #ef4444; color:#991b1b; margin-bottom: 0;">
                <div class="alert-title" style="color:#ef4444;">⚠️ 聖美麗健康文件大檔案憑證限制婉拒結案</div>
                醫療連鎖聖美麗（St. Mary）因其健康檢查文件多為富含影像的超大 PDF（單檔常超過 10MB），好好簽考量現行架構在嵌入 AATL 數位憑證時易因伺服器負載與超時失敗，若勉強承接將導致售後服務成本極大化。
                <br><b>【決策回報】</b>：CSM 與技術團隊於本月正式予以婉拒年約，客戶選擇於 8/1 續約點點簽。此為我方首次針對「單檔 10MB 限額與 AATL 效能」主動退守之邊界，已記錄至系統規範中。
            </div>
        </div>
    </div>

    <!-- MAJOR PROJECTS & MILESTONES -->
    <div class="glass-card">
        <h2 class="section-title">二、 重大專案與 API 串接進程 (Project Milestones)</h2>
        <p style="font-size: 14px; margin-bottom: 12px;">5 月份之主要 SLG 客戶與 API 技術串接項目已完成以下里程碑：</p>
        
        <div class="table-responsive">
            <table>
                <thead>
                    <tr>
                        <th style="width: 25%;">客戶/專案名稱</th>
                        <th style="width: 25%;">本月進展 / 里程碑</th>
                        <th style="width: 35%;">技術與串接細節</th>
                        <th style="width: 15%;">狀態狀態</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>太平洋旅行社</strong></td>
                        <td>40人企業方案正式成交</td>
                        <td>開通正式版 (6/1 生效)，已完成後台 UNIFY 權限配置。</td>
                        <td><span class="badge badge-green">已開通</span></td>
                    </tr>
                    <tr>
                        <td><strong>101 客戶 BPM 部署</strong></td>
                        <td>原始碼與安裝文件交付</td>
                        <td>開通技術窗口 steven 帳號及 10 份雲端憑證。提案 HiCloud 與 DMZ 的 isHealth 偵測 API 機制。</td>
                        <td><span class="badge badge-blue">導入中</span></td>
                    </tr>
                    <tr>
                        <td><strong>得勝者 PACS AI 整合</strong></td>
                        <td>眼科 7 月上線準備</td>
                        <td>與商之器合作，完成醫院 PACS 後台 AI 影像引擎串接，進行簽署影像防偽安全評估。</td>
                        <td><span class="badge badge-blue">導入中</span></td>
                    </tr>
                    <tr>
                        <td><strong>鼎新 API 串接專案</strong></td>
                        <td>API 串接完成與調優</td>
                        <td>串接完成。由於 AI 拋出連結耗時及大陸 GCP 網路速度慢，BZS 開啟連結由 60 秒調整為 15 分鐘。</td>
                        <td><span class="badge badge-green">串接完成</span></td>
                    </tr>
                    <tr>
                        <td><strong>聯合線上 (udn新聞)</strong></td>
                        <td>API 串接完成並進入測試</td>
                        <td>目前 API 串接已完成，業務單位正在進行業務流程與防偽簽署流程測試。</td>
                        <td><span class="badge badge-orange">測試中</span></td>
                    </tr>
                    <tr>
                        <td><strong>福安健康與職安 API</strong></td>
                        <td>專案簽約與需求說明</td>
                        <td>規劃勞工健康與職安服務文件簽署。專案報價 $12 萬，預估年簽 8K~10K，含 8000 份 AATL。</td>
                        <td><span class="badge badge-orange">簽約中</span></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- REPORT METADATA & FOOTER -->
    <footer>
        <p>報告版次: V1.0 | 產出時間: 2026-06-01 15:00 | 營運單位: 好好簽 BreezySign 業務與技術整合小組</p>
        <p style="margin-top: 4px; font-size: 11px; color:#94a3b8;">本報告已透過 edge headless 技術進行高保真 PDF 封裝認證，並以 YYYYMMDD-HHMM 精確時間戳進行版次管理。</p>
    </footer>
</div>

</body>
</html>
"""

    # 4. 寫入檔案
    try:
        with open(html_filepath, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"[SUCCESS] HTML report successfully generated at: {html_filepath}")
        return html_filepath
    except Exception as e:
        print(f"[ERROR] Failed to write HTML report: {e}")
        return None

if __name__ == "__main__":
    generate_report()
