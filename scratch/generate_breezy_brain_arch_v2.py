# -*- coding: utf-8 -*-
import os
import subprocess
import datetime
import sys

# 16:9 橫向 HTML/CSS 架構圖內容定義
html_template = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BreezyBrain 產品核心架構圖 (16:9 Landscape Architecture)</title>
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&family=Noto+Sans+TC:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #0b0f19;
            --grid-color: rgba(37, 99, 235, 0.06);
            --primary: #057857; /* 好好簽翠綠 */
            --primary-glow: rgba(5, 120, 87, 0.15);
            --secondary: #0284c7; /* 天空藍 */
            --secondary-glow: rgba(2, 132, 199, 0.15);
            --brain: #7c3aed; /* 大腦紫 */
            --brain-glow: rgba(124, 58, 237, 0.15);
            --border-glow: #ea580c; /* 安全橘 */
            --text-main: #f8fafc;
            --text-sub: #94a3b8;
            --card-bg: rgba(15, 23, 42, 0.7);
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
            background-size: 24px 24px;
            color: var(--text-main);
            min-height: 100vh;
            padding: 30px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            overflow-x: hidden;
            position: relative;
        }

        header {
            text-align: center;
            margin-bottom: 24px;
            width: 100%;
            max-width: 1280px;
        }

        .logo-title {
            font-family: 'Outfit', sans-serif;
            font-size: 13px;
            font-weight: 700;
            color: var(--primary);
            letter-spacing: 3px;
            text-transform: uppercase;
            margin-bottom: 6px;
        }

        h1 {
            font-family: 'Outfit', 'Noto Sans TC', sans-serif;
            font-size: 28px;
            font-weight: 800;
            margin-bottom: 8px;
            background: linear-gradient(135deg, #ffffff 40%, #a7f3d0 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -0.5px;
        }

        .subtitle {
            font-size: 13.5px;
            color: var(--text-sub);
            line-height: 1.5;
        }

        /* 16:9 產品架構圖總容器 (橫向4直欄排列) */
        .architecture-container {
            width: 100%;
            max-width: 1280px;
            display: grid;
            grid-template-columns: 1fr 1.25fr 1.25fr 1fr; /* 四大直欄 */
            gap: 20px;
            aspect-ratio: 16 / 9; /* 強制 16:9 比例 */
            z-index: 10;
        }

        /* 每一欄的大卡片 */
        .column-wrapper {
            background: var(--card-bg);
            border: 1px solid rgba(148, 163, 184, 0.1);
            border-radius: 16px;
            padding: 20px;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.4), inset 0 1px 1px rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(12px);
            display: flex;
            flex-direction: column;
            gap: 16px;
            position: relative;
            height: 100%;
        }

        /* 各層發光邊框 */
        .layer-presentation { border-top: 4px solid var(--secondary); box-shadow: 0 0 20px rgba(2, 132, 199, 0.03); }
        .layer-application { border-top: 4px solid var(--primary); box-shadow: 0 0 20px rgba(5, 120, 87, 0.03); }
        .layer-brain { border-top: 4px solid var(--brain); box-shadow: 0 0 20px rgba(124, 58, 237, 0.03); }
        .layer-security { border-top: 4px solid var(--border-glow); box-shadow: 0 0 20px rgba(234, 88, 12, 0.03); }

        .layer-title {
            font-family: 'Outfit', 'Noto Sans TC', sans-serif;
            font-size: 15px;
            font-weight: 700;
            letter-spacing: 0.5px;
            display: flex;
            align-items: center;
            gap: 6px;
            padding-bottom: 8px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }

        .layer-presentation .layer-title { color: var(--secondary); }
        .layer-application .layer-title { color: var(--primary); }
        .layer-brain .layer-title { color: var(--brain); }
        .layer-security .layer-title { color: var(--border-glow); }

        /* 模組小卡片 */
        .module-card {
            background: rgba(30, 41, 59, 0.45);
            border: 1px solid rgba(255, 255, 255, 0.03);
            border-radius: 10px;
            padding: 12px 14px;
            display: flex;
            flex-direction: column;
            gap: 6px;
            flex-grow: 1;
        }

        .module-header {
            display: flex;
            align-items: center;
            gap: 6px;
            font-size: 13.5px;
            font-weight: 600;
            color: #ffffff;
        }

        .module-desc {
            font-size: 11.5px;
            color: var(--text-sub);
            line-height: 1.4;
        }

        .tech-badge-list {
            display: flex;
            flex-wrap: wrap;
            gap: 4px;
            margin-top: 2px;
        }

        .tech-badge {
            font-size: 9px;
            font-weight: 700;
            padding: 1px 4px;
            border-radius: 3px;
            background: rgba(255, 255, 255, 0.05);
            color: #cbd5e1;
        }

        .arrow-indicator {
            position: absolute;
            top: 50%;
            right: -16px;
            transform: translateY(-50%);
            color: rgba(148, 163, 184, 0.25);
            z-index: 20;
            pointer-events: none;
        }

        /* 移除最後一欄右側的箭頭 */
        .layer-security .arrow-indicator {
            display: none;
        }

        footer {
            margin-top: 24px;
            font-size: 10px;
            color: var(--text-sub);
            text-align: center;
            border-top: 1px solid rgba(148, 163, 184, 0.1);
            padding-top: 12px;
            width: 100%;
            max-width: 1280px;
        }

        /* 媒體列印樣式優化，保證橫向 PDF 列印品質 */
        @media print {
            @page {
                size: landscape;
                margin: 0;
            }
            body {
                background-color: #ffffff !important;
                background-image: none !important;
                color: #0f172a !important;
                padding: 20px !important;
            }
            .architecture-container {
                aspect-ratio: 16 / 9 !important;
            }
            .column-wrapper {
                background: #ffffff !important;
                border: 1px solid #cbd5e1 !important;
                box-shadow: none !important;
                height: 100% !important;
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
        }
    </style>
</head>
<body>

<header>
    <div class="logo-title">BreezyBrain 16:9 Landscape Blueprint</div>
    <h1>BreezyBrain 產品核心分層架構</h1>
    <p class="subtitle">BreezyBrain 作為好好簽（BreezySign）的高階自動化中樞。此 16:9 橫向架構詳細展示了名片 OCR 採集、微型 CRM、電子簽核連動 CLM 與知識智庫 KM 之數據流動閉環。</p>
</header>

<div class="architecture-container">

    <!-- 1. 展示與接口層 -->
    <div class="column-wrapper layer-presentation">
        <div class="layer-title">
            <svg style="width:16px;height:16px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="9" y1="3" x2="9" y2="21"></line></svg>
            展示與接口層 (Presentation)
        </div>
        <div class="module-card">
            <div class="module-header">Web 整合控制台</div>
            <div class="module-desc">無代碼控制面板。提供 CRM 銷售管道看板、大腦 RAG 語意範本對照、工作流編排與法務人工覆核介面。</div>
            <div class="tech-badge-list">
                <span class="tech-badge">Web UI</span>
                <span class="tech-badge">SaaS Console</span>
            </div>
        </div>
        <div class="module-card">
            <div class="module-header">CLI 工具 (breezy-brain)</div>
            <div class="module-desc">供維運與工程一鍵操作。支援名片採集同步、地端降級簽核測試、BPM 流程手動調用與資料庫備份 CLI。</div>
            <div class="tech-badge-list">
                <span class="tech-badge">CLI Tool</span>
                <span class="tech-badge">Go / Py</span>
            </div>
        </div>
        <div class="module-card">
            <div class="module-header">REST / MCP APIs Gateway</div>
            <div class="module-desc">為外部與 Agent 提供統一通道。映射為標準 MCP 協定的 Resources、Tools 與 Prompts 三大原語，支援 mTLS 安全加密。</div>
            <div class="tech-badge-list">
                <span class="tech-badge">MCP Server</span>
                <span class="tech-badge">FastAPI</span>
            </div>
        </div>
        <!-- 橫向指向箭頭 -->
        <div class="arrow-indicator">
            <svg style="width:24px;height:24px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </div>
    </div>

    <!-- 2. 核心業務層 (新增名片BCR與電子簽名項目) -->
    <div class="column-wrapper layer-application">
        <div class="layer-title">
            <svg style="width:16px;height:16px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="2" y="2" width="20" height="8" rx="2" ry="2"></rect><rect x="2" y="14" width="20" height="8" rx="2" ry="2"></rect></svg>
            核心業務層 (Application)
        </div>
        <div class="module-card">
            <div class="module-header">名片採集與 OCR (BCR)</div>
            <div class="module-desc">對接蒙恬名片雲 (WorldCard Cloud)。支援名片拍照上傳、高精度名片資訊 OCR 抽取，並由大腦補全缺失工商資料。</div>
            <div class="tech-badge-list">
                <span class="tech-badge">BCR Ingest</span>
                <span class="tech-badge">WorldCard</span>
            </div>
        </div>
        <div class="module-card">
            <div class="module-header">微型客資管理 (BreezyCRM)</div>
            <div class="module-desc">配備「模糊去重防禦引擎」與「大腦合理推論補全」；提供 SaaS、經銷通路與客製專案之三軌獨立銷售管道 (Pipeline)。</div>
            <div class="tech-badge-list">
                <span class="tech-badge">Deduplication</span>
                <span class="tech-badge">JSONB DB</span>
            </div>
        </div>
        <div class="module-card">
            <div class="module-header">電子簽名與 CLM 派單</div>
            <div class="module-desc">整合高精度 OCR 模組解析非結構化草案。自動執行「大腦語意範本匹配」，完成動態合約派單變數填入並追蹤履約期限。</div>
            <div class="tech-badge-list">
                <span class="tech-badge">BreezyCLM</span>
                <span class="tech-badge">E-Sign Dispatch</span>
            </div>
        </div>
        <div class="module-card">
            <div class="module-header">知識管理智庫 (BreezyKM)</div>
            <div class="module-desc">合約完簽後之知識沈澱。自動呼叫 LLM 進行 100 字合約核心摘要，建立圖譜化關聯，並支援 Slack/Teams 到期通知。</div>
            <div class="tech-badge-list">
                <span class="tech-badge">Graphify</span>
                <span class="tech-badge">KM Wiki</span>
            </div>
        </div>
        <!-- 橫向指向箭頭 -->
        <div class="arrow-indicator">
            <svg style="width:24px;height:24px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </div>
    </div>

    <!-- 3. AI 智能大腦中樞 -->
    <div class="column-wrapper layer-brain">
        <div class="layer-title">
            <svg style="width:16px;height:16px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"></path><path d="M12 6v6l4 2"></path></svg>
            AI 智能大腦中樞 (AI Brain Core)
        </div>
        <div class="module-card">
            <div class="module-header">Ollama API / Router</div>
            <div class="module-desc">本地大腦核心模型調用代理。負責處理 RAG 嵌入，並內嵌模型降級與雲端備用大腦路由。</div>
            <div class="tech-badge-list">
                <span class="tech-badge">Ollama</span>
                <span class="tech-badge">Router</span>
            </div>
        </div>
        <div class="module-card">
            <div class="module-header">Qwen 2.5 推理大腦</div>
            <div class="module-desc">核心開源大腦推理模型。完成客資清洗、範本匹配、合約風險審查與個資脫敏（PII Masking），杜絕隱私洩漏。</div>
            <div class="tech-badge-list">
                <span class="tech-badge">Local LLM</span>
                <span class="tech-badge">7B/14B</span>
            </div>
        </div>
        <div class="module-card">
            <div class="module-header">ChromaDB / Qdrant RAG</div>
            <div class="module-desc">向量檢索與記憶庫。將合約向量化儲存，並支援符合 GDPR 被遺忘權之 metadata 過濾抹除機制。</div>
            <div class="tech-badge-list">
                <span class="tech-badge">Vector DB</span>
                <span class="tech-badge">Conditional Del</span>
            </div>
        </div>
        <div class="module-card">
            <div class="module-header">ReAct Agent Loop & Gate</div>
            <div class="module-desc">自動化決策迴圈。結合「人工確認守門員（Human-in-the-Loop）」，低置信或中高風險合約強制人工覆核，確保法務安全。</div>
            <div class="tech-badge-list">
                <span class="tech-badge">ReAct Loop</span>
                <span class="tech-badge">HITL</span>
            </div>
        </div>
        <!-- 橫向指向箭頭 -->
        <div class="arrow-indicator">
            <svg style="width:24px;height:24px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </div>
    </div>

    <!-- 4. 安全與外部對接邊界 -->
    <div class="column-wrapper layer-security">
        <div class="layer-title">
            <svg style="width:16px;height:16px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
            安全與外部對接邊界 (Security)
        </div>
        <div class="module-card">
            <div class="module-header">DMZ 網閘代理 (Proxy)</div>
            <div class="module-desc">針對企業 100% 物理隔離之地端環境，提供專屬的網路閘道代理方案，只允許專用時戳通訊埠連通外網。</div>
            <div class="tech-badge-list">
                <span class="tech-badge">DMZ Proxy</span>
                <span class="tech-badge">Strict Port</span>
            </div>
        </div>
        <div class="module-card">
            <div class="module-header">BreezySign 雲端 API</div>
            <div class="module-desc">對外呼叫電子簽章雲端主站。透過中華電信與憑證機構完成 AATL 認證與 LTV 時戳，完成完全合規之電子簽約。</div>
            <div class="tech-badge-list">
                <span class="tech-badge">Cloud E-Sign</span>
                <span class="tech-badge">AATL / LTV</span>
            </div>
        </div>
        <div class="module-card">
            <div class="module-header">地端降級電子簽名</div>
            <div class="module-desc">當客戶完全禁止聯外時，系統自動啟用降級自簽模式，採用地端私鑰簽章與 SHA256 雜湊，完成內部安全簽核。</div>
            <div class="tech-badge-list">
                <span class="tech-badge">Offline E-Sign</span>
                <span class="tech-badge">Private CA</span>
            </div>
        </div>
    </div>

</div>

<footer>
    <p>架構圖編號: BZS-ARCH-169-20260528-02 | 蒙恬科技 (PenPower) BreezyBrain 專案開發小組 ． 2026H2 橫向產品架構藍圖 (技術討論稿)</p>
</footer>

</body>
</html>
"""

def main():
    # 確保 outputs 目錄存在
    os.makedirs("outputs", exist_ok=True)
    
    # 動態獲取當前時間戳
    now_str = datetime.datetime.now().strftime("%Y%m%d-%H%M")
    
    # 定義檔案名稱
    output_html_name = f"{now_str}-breezy-brain-architecture_v2.html"
    output_pdf_name = f"{now_str}-breezy-brain-architecture_v2.pdf"
    
    output_html_path = os.path.join("outputs", output_html_name)
    output_pdf_path = os.path.join("outputs", output_pdf_name)
    
    abs_html = os.path.abspath(output_html_path)
    abs_pdf = os.path.abspath(output_pdf_path)
    
    # 1. 寫入 HTML 檔案
    print("Writing 16:9 landscape architecture HTML file...")
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
        
        # 寫入結果供主腳本參照
        with open("outputs/arch_v2_generation_result.txt", "w", encoding="utf-8") as f:
            f.write(f"HTML: {output_html_path}\n")
            f.write(f"PDF: {output_pdf_path}\n")
            
    except Exception as e:
        print(f"[ERROR] Failed to compile PDF: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
