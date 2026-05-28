# -*- coding: utf-8 -*-
import os
import subprocess
import datetime
import sys

# HTML/CSS 架構圖內容定義
html_template = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BreezyBrain 產品核心架構圖 (Product Architecture)</title>
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&family=Noto+Sans+TC:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #0b0f19;
            --grid-color: rgba(37, 99, 235, 0.07);
            --primary: #057857; /* 好好簽翠綠 */
            --primary-glow: rgba(5, 120, 87, 0.15);
            --secondary: #0284c7; /* 天空藍 */
            --secondary-glow: rgba(2, 132, 199, 0.15);
            --brain: #7c3aed; /* 大腦紫 */
            --brain-glow: rgba(124, 58, 237, 0.15);
            --border-glow: #ea580c; /* 安全橘 */
            --border-glow-bg: rgba(234, 88, 12, 0.1);
            --text-main: #f8fafc;
            --text-sub: #94a3b8;
            --card-bg: rgba(15, 23, 42, 0.65);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Inter', 'Noto Sans TC', sans-serif;
            background-color: var(--bg-color);
            background-image: 
                linear-gradient(var(--grid-color) 1px, transparent 1px),
                linear-gradient(90deg, var(--grid-color) 1px, transparent 1px);
            background-size: 20px 20px;
            color: var(--text-main);
            min-height: 100vh;
            padding: 40px 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            overflow-x: hidden;
            position: relative;
        }

        /* 背景微光裝飾 */
        body::before {
            content: "";
            position: absolute;
            width: 600px;
            height: 600px;
            top: 20%;
            left: 50%;
            transform: translate(-50%, -50%);
            border-radius: 50%;
            background: radial-gradient(circle, rgba(5, 120, 87, 0.08) 0%, transparent 70%);
            z-index: -1;
            pointer-events: none;
        }

        header {
            text-align: center;
            margin-bottom: 40px;
            max-width: 900px;
            z-index: 10;
        }

        .logo-title {
            font-family: 'Outfit', sans-serif;
            font-size: 14px;
            font-weight: 700;
            color: var(--primary);
            letter-spacing: 3px;
            text-transform: uppercase;
            margin-bottom: 8px;
        }

        h1 {
            font-family: 'Outfit', 'Noto Sans TC', sans-serif;
            font-size: 32px;
            font-weight: 800;
            margin-bottom: 12px;
            background: linear-gradient(135deg, #ffffff 30%, #a7f3d0 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -0.5px;
        }

        .subtitle {
            font-size: 15px;
            color: var(--text-sub);
            line-height: 1.6;
        }

        /* 產品架構圖總容器 */
        .architecture-container {
            width: 100%;
            max-width: 1100px;
            display: flex;
            flex-direction: column;
            gap: 28px;
            z-index: 10;
        }

        /* 每一層的大卡片 */
        .layer-wrapper {
            background: var(--card-bg);
            border: 1px solid rgba(148, 163, 184, 0.1);
            border-radius: 16px;
            padding: 24px;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3), inset 0 1px 1px rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(12px);
            position: relative;
            transition: all 0.3s ease;
        }

        .layer-wrapper:hover {
            border-color: rgba(148, 163, 184, 0.2);
            box-shadow: 0 15px 30px -5px rgba(0, 0, 0, 0.4);
        }

        /* 各層發光效果 */
        .layer-presentation { border-left: 4px solid var(--secondary); box-shadow: 0 0 20px rgba(2, 132, 199, 0.05); }
        .layer-application { border-left: 4px solid var(--primary); box-shadow: 0 0 20px rgba(5, 120, 87, 0.05); }
        .layer-brain { border-left: 4px solid var(--brain); box-shadow: 0 0 20px rgba(124, 58, 237, 0.05); }
        .layer-security { border-left: 4px solid var(--border-glow); box-shadow: 0 0 20px rgba(234, 88, 12, 0.05); }

        .layer-title {
            font-family: 'Outfit', 'Noto Sans TC', sans-serif;
            font-size: 16px;
            font-weight: 700;
            margin-bottom: 20px;
            letter-spacing: 0.5px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .layer-presentation .layer-title { color: var(--secondary); }
        .layer-application .layer-title { color: var(--primary); }
        .layer-brain .layer-title { color: var(--brain); }
        .layer-security .layer-title { color: var(--border-glow); }

        /* 卡片網格佈局 */
        .grid-layout {
            display: grid;
            gap: 20px;
        }

        .grid-3 { grid-template-columns: repeat(3, 1fr); }
        .grid-4 { grid-template-columns: repeat(4, 1fr); }

        /* 模組小元件樣式 */
        .module-card {
            background: rgba(30, 41, 59, 0.45);
            border: 1px solid rgba(255, 255, 255, 0.03);
            border-radius: 12px;
            padding: 18px;
            display: flex;
            flex-direction: column;
            gap: 8px;
            position: relative;
        }

        .layer-presentation .module-card { border-top: 2px solid var(--secondary); }
        .layer-application .module-card { border-top: 2px solid var(--primary); }
        .layer-brain .module-card { border-top: 2px solid var(--brain); }
        .layer-security .module-card { border-top: 2px solid var(--border-glow); }

        .module-header {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 14.5px;
            font-weight: 600;
            color: #ffffff;
        }

        .module-icon {
            width: 18px;
            height: 18px;
            opacity: 0.9;
        }

        .module-desc {
            font-size: 12.5px;
            color: var(--text-sub);
            line-height: 1.5;
        }

        .tech-badge-list {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-top: 4px;
        }

        .tech-badge {
            font-size: 10px;
            font-weight: 700;
            padding: 2px 6px;
            border-radius: 4px;
            background: rgba(255, 255, 255, 0.05);
            color: #e2e8f0;
            border: 1px solid rgba(255, 255, 255, 0.03);
        }

        /* 連接箭頭說明 */
        .flow-indicator {
            text-align: center;
            font-size: 12px;
            color: rgba(148, 163, 184, 0.4);
            font-weight: 700;
            letter-spacing: 2px;
            margin: 4px 0;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }

        .flow-line {
            flex-grow: 1;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(148, 163, 184, 0.25) 50%, transparent);
        }

        footer {
            margin-top: 60px;
            font-size: 11px;
            color: var(--text-sub);
            text-align: center;
            border-top: 1px solid rgba(148, 163, 184, 0.1);
            padding-top: 20px;
            width: 100%;
            max-width: 1100px;
        }

        /* 媒體列印樣式優化，保證 PDF 列印品質 */
        @media print {
            body {
                background-color: #ffffff !important;
                background-image: none !important;
                color: #0f172a !important;
                padding: 10px !important;
            }
            .layer-wrapper {
                background: #ffffff !important;
                border: 1px solid #cbd5e1 !important;
                box-shadow: none !important;
                margin-bottom: 20px !important;
                page-break-inside: avoid !important;
            }
            .module-card {
                background: #f8fafc !important;
                border: 1px solid #cbd5e1 !important;
            }
            .module-header, h1 {
                color: #0f172a !important;
                -webkit-text-fill-color: initial !important;
                background: none !important;
            }
            .tech-badge {
                background: #e2e8f0 !important;
                color: #0f172a !important;
                border: 1px solid #cbd5e1 !important;
            }
            .flow-line {
                background: #cbd5e1 !important;
            }
        }
    </style>
</head>
<body>

<header>
    <div class="logo-title">BreezyBrain Architecture Blueprint</div>
    <h1>BreezyBrain 產品核心分層架構</h1>
    <p class="subtitle">BreezyBrain 作為好好簽（BreezySign）的高階自動化中樞，以地端 Local LLM 作為推理心臟，向上連通客資（CRM）與合約生命週期（CLM），向下透過安全網閘對接雲端簽核與知識庫（KM）歸檔。</p>
</header>

<div class="architecture-container">

    <!-- 1. 展示與接口層 -->
    <div class="layer-wrapper layer-presentation">
        <div class="layer-title">
            <svg class="module-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
            展示與接口層 (Presentation & API Layer)
        </div>
        <div class="grid-layout grid-3">
            <div class="module-card">
                <div class="module-header">BreezyBrain Web 整合控制台</div>
                <div class="module-desc">無代碼視覺化配置後台。提供企業管理者進行 CRM 流轉管道、大腦 RAG 語意範本對照、視覺化工作流編排與法務人工審查介面。</div>
                <div class="tech-badge-list">
                    <span class="tech-badge">SaaS Console</span>
                    <span class="tech-badge">Web UI</span>
                </div>
            </div>
            <div class="module-card">
                <div class="module-header">CLI 命令列工具 (breezy-brain)</div>
                <div class="module-desc">供工程與系統維運人員一鍵操作。支援名片採集同步、地端降級簽署測試、BPM 流程手動調用與資料庫備份 CLI 工具。</div>
                <div class="tech-badge-list">
                    <span class="tech-badge">Go / Python</span>
                    <span class="tech-badge">CLI Tool</span>
                </div>
            </div>
            <div class="module-card">
                <div class="module-header">RESTful / MCP APIs Gateway</div>
                <div class="module-desc">為外部應用與 AI Agent 提供統一對接通道。映射為標準 MCP 協定的 Resources、Tools 與 Prompts 三大原語，內置 mTLS 憑證與速率限制。</div>
                <div class="tech-badge-list">
                    <span class="tech-badge">FastAPI</span>
                    <span class="tech-badge">MCP Server</span>
                </div>
            </div>
        </div>
    </div>

    <div class="flow-indicator">
        <div class="flow-line"></div>
        數據流：觸發商機 / 傳遞 API 變數
        <div class="flow-line"></div>
    </div>

    <!-- 2. 核心業務層 -->
    <div class="layer-wrapper layer-application">
        <div class="layer-title">
            <svg class="module-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="2" y="2" width="20" height="8" rx="2" ry="2"></rect><rect x="2" y="14" width="20" height="8" rx="2" ry="2"></rect><line x1="6" y1="6" x2="6.01" y2="6"></line><line x1="6" y1="18" x2="6.01" y2="18"></line></svg>
            核心業務層 (Application Layer)
        </div>
        <div class="grid-layout grid-3">
            <div class="module-card">
                <div class="module-header">微型客資管理 (BreezyCRM)</div>
                <div class="module-desc">支援名片拍照 Webhook 自動同步。配備「模糊去重防禦引擎」與「大腦合理推論補全」；提供 SaaS、經銷通路與客製專案之三軌獨立 Pipeline 跟進流程。</div>
                <div class="tech-badge-list">
                    <span class="tech-badge">Accounts/Contacts</span>
                    <span class="tech-badge">JSONB Schema</span>
                </div>
            </div>
            <div class="module-card">
                <div class="module-header">智能合約管理 (BreezyCLM)</div>
                <div class="module-desc">整合高精度 OCR 模組解析非結構化草稿。自動執行「大腦語意範本匹配」，完成動態合約派單變數填入，並監控保固、付款等履約義務期限。</div>
                <div class="tech-badge-list">
                    <span class="tech-badge">OCR Parser</span>
                    <span class="tech-badge">Obligation Track</span>
                </div>
            </div>
            <div class="module-card">
                <div class="module-header">知識管理智庫 (BreezyKM)</div>
                <div class="module-desc">合約簽署完成後之知識沈澱。自動呼叫 LLM 進行 100 字合約核心摘要，建立圖譜化關聯，並支援 Slack/Teams 到期通知。</div>
                <div class="tech-badge-list">
                    <span class="tech-badge">100w Summary</span>
                    <span class="tech-badge">Graphify</span>
                </div>
            </div>
        </div>
    </div>

    <div class="flow-indicator">
        <div class="flow-line"></div>
        雙向調用：語意提取 / 向量比對 / ReAct 思考
        <div class="flow-line"></div>
    </div>

    <!-- 3. AI 智能大腦中樞 -->
    <div class="layer-wrapper layer-brain">
        <div class="layer-title">
            <svg class="module-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M9.59 4.59A2 2 0 1 1 11 8H9m10.59 11.41A2 2 0 1 1 18 16h2m-9 0A8 8 0 1 0 3 9h2"></path></svg>
            AI 智能大腦中樞 (AI Brain Core - Hybrid/Local)
        </div>
        <div class="grid-layout grid-4">
            <div class="module-card">
                <div class="module-header">Ollama API / Model Router</div>
                <div class="module-desc">本地大腦核心模型調用代理。負責處理 RAG 嵌入，並內嵌模型降級路由（可自動降級或連通雲端備用大腦）。</div>
                <div class="tech-badge-list">
                    <span class="tech-badge">Ollama</span>
                    <span class="tech-badge">Router</span>
                </div>
            </div>
            <div class="module-card">
                <div class="module-header">Qwen 2.5 7B/14B 推理大腦</div>
                <div class="module-desc">核心開源大腦推理模型。在地端完成客資清洗、語意範本匹配、合約風險審查與個資脫敏（PII Masking），杜絕隱私洩漏。</div>
                <div class="tech-badge-list">
                    <span class="tech-badge">Local LLM</span>
                    <span class="tech-badge">Apache 2.0</span>
                </div>
            </div>
            <div class="module-card">
                <div class="module-header">ChromaDB / Qdrant RAG</div>
                <div class="module-desc">向量檢索與語意記憶庫。使用 BGE-M3 將條文向量化儲存，並支援 GDPR 被遺忘權之 metadata 過濾抹除機制。</div>
                <div class="tech-badge-list">
                    <span class="tech-badge">Vector DB</span>
                    <span class="tech-badge">Conditional Del</span>
                </div>
            </div>
            <div class="module-card">
                <div class="module-header">ReAct Agent Loop & Gate</div>
                <div class="module-desc">自動化思考決策迴圈。結合「人工確認守門員（Human-in-the-Loop）」，嚴禁 AI 直接發送合約，確保中高風險合約強制人工覆核。</div>
                <div class="tech-badge-list">
                    <span class="tech-badge">ReAct Loop</span>
                    <span class="tech-badge">BPM Gate</span>
                </div>
            </div>
        </div>
    </div>

    <div class="flow-indicator">
        <div class="flow-line"></div>
        傳簽授權：網閘安全封裝 / 憑證簽名
        <div class="flow-line"></div>
    </div>

    <!-- 4. 安全與外部對接邊界 -->
    <div class="layer-wrapper layer-security">
        <div class="layer-title">
            <svg class="module-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
            安全與外部對接邊界 (Security & Integration Boundary)
        </div>
        <div class="grid-layout grid-3">
            <div class="module-card">
                <div class="module-header">DMZ 網閘代理 (Proxy Gateway)</div>
                <div class="module-desc">針對企業 100% 物理隔離之地端環境，提供專屬的網路閘道代理方案，在限制外網的政策下只允許時戳通訊埠對外連通。</div>
                <div class="tech-badge-list">
                    <span class="tech-badge">DMZ Proxy</span>
                    <span class="tech-badge">Strict Port</span>
                </div>
            </div>
            <div class="module-card">
                <div class="module-header">BreezySign 雲端 API (AATL/LTV)</div>
                <div class="module-desc">對外呼叫電子簽章雲端主站。透過中華電信與國際憑證機構完成 AATL 認證與 LTV 長期時戳，完成法律效力完全之電子簽約。</div>
                <div class="tech-badge-list">
                    <span class="tech-badge">Cloud E-Sign</span>
                    <span class="tech-badge">AATL / LTV</span>
                </div>
            </div>
            <div class="module-card">
                <div class="module-header">地端降級電子簽名 (私有憑證)</div>
                <div class="module-desc">當客戶政策完全禁止對外連線時，系統自動啟用降級自簽模式，採用地端私密金鑰雜湊與 SHA256 加密，完成無外網內部簽核。</div>
                <div class="tech-badge-list">
                    <span class="tech-badge">Offline E-Sign</span>
                    <span class="tech-badge">Private CA</span>
                </div>
            </div>
        </div>
    </div>

    <footer>
        <p>架構圖編號: BZS-ARCH-20260528-01 | 蒙恬科技 (PenPower) BreezyBrain 專案開發小組 ． 2026H2 產品架構藍圖 (技術討論稿)</p>
    </footer>
</div>

</body>
</html>
"""

def main():
    # 確保 outputs 目錄存在
    os.makedirs("outputs", exist_ok=True)
    
    # 動態獲取當前時間戳
    now_str = datetime.datetime.now().strftime("%Y%m%d-%H%M")
    
    # 定義檔案名稱
    output_html_name = f"{now_str}-breezy-brain-architecture.html"
    output_pdf_name = f"{now_str}-breezy-brain-architecture.pdf"
    
    output_html_path = os.path.join("outputs", output_html_name)
    output_pdf_path = os.path.join("outputs", output_pdf_name)
    
    abs_html = os.path.abspath(output_html_path)
    abs_pdf = os.path.abspath(output_pdf_path)
    
    # 1. 寫入 HTML 檔案
    print("Writing architecture HTML file...")
    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(html_template)
    print(f"[SUCCESS] HTML written to: {abs_html}")
    
    # 2. 尋找 Edge 瀏覽器進行 PDF 列印
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
        print("[ERROR] Microsoft Edge or Google Chrome not found. Cannot export PDF.")
        sys.exit(1)
        
    # 3. 執行 Headless 轉換
    print(f"Calling browser: {browser_exe} for headless PDF generation...")
    cmd = [
        browser_exe,
        "--headless",
        "--disable-gpu",
        "--disable-software-rasterizer",
        "--disable-extensions",
        "--no-sandbox",
        "--print-to-pdf=" + abs_pdf,
        "--no-pdf-header-footer",
        "file:///" + abs_html.replace("\\", "/")
    ]
    
    try:
        subprocess.run(cmd, check=True, timeout=30)
        print(f"[SUCCESS] PDF successfully compiled and written to: {abs_pdf}")
        print(f"File size: {os.path.getsize(abs_pdf)} bytes")
        
        # 寫入一個臨時記錄檔方便回覆
        with open("outputs/arch_generation_result.txt", "w", encoding="utf-8") as f:
            f.write(f"HTML: {output_html_path}\n")
            f.write(f"PDF: {output_pdf_path}\n")
            
    except Exception as e:
        print(f"[ERROR] Failed to compile PDF: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
