# -*- coding: utf-8 -*-
import os
import subprocess
import datetime
import sys

# BreezySign Architecture (Eraser Neon Blueprint) - 完美融合用戶高對比、大字體與純英文極簡描述需求
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BreezySign Architecture (Eraser Neon Blueprint)</title>
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #010205; /* 極深黑底色以加強對比 */
            --grid-color: rgba(30, 58, 138, 0.15); /* 藍色背景網格 */
            
            --blue-neon: #00e5ff;
            --blue-glow: rgba(0, 229, 255, 0.45);
            
            --green-neon: #00ff87;
            --green-glow: rgba(0, 255, 135, 0.45);
            
            --purple-neon: #d53dff;
            --purple-glow: rgba(213, 61, 255, 0.45);
            
            --orange-neon: #ff7c00;
            --orange-glow: rgba(255, 124, 0, 0.45);
            
            --text-main: #ffffff; /* 純白主文字 */
            --text-sub: #cbd5e1; /* 調亮副文字以提升對比度 */
            --card-bg: #040814; /* 完全不透明卡片背景 */
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-color);
            background-image: 
                linear-gradient(var(--grid-color) 1px, transparent 1px),
                linear-gradient(90deg, var(--grid-color) 1px, transparent 1px);
            background-size: 26px 26px;
            color: var(--text-main);
            min-height: 100vh;
            padding: 24px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            position: relative;
        }

        /* 標題區樣式 (放大標題) */
        header {
            text-align: center;
            margin-bottom: 24px;
            width: 100%;
            max-width: 1366px;
            z-index: 10;
        }

        h1 {
            font-family: 'Outfit', sans-serif;
            font-size: 52px; /* 顯著放大標題字體 */
            font-weight: 800;
            letter-spacing: 1px;
            color: #ffffff;
            margin-bottom: 6px;
            text-shadow: 0 0 12px rgba(255, 255, 255, 0.15);
        }

        .subtitle {
                   /* 16:9 架構圖總容器 */
        .architecture-container {
            width: 100%;
            max-width: 1366px;
            height: 768px; /* 固定 16:9 解析度，確保 Edge 無損輸出 */
            position: relative;
            background: rgba(3, 6, 12, 0.8);
            border: 2px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 20px 25px;
            display: grid;
            grid-template-columns: 260px 320px 320px 260px; /* 拓寬列寬以適配大字體 */
            justify-content: space-between;
            align-content: center;
            gap: 15px;
            z-index: 10;
        }

        /* 大欄位容器 */
        .column-wrapper {
            background: var(--card-bg);
            border-radius: 16px;
            padding: 12px 10px;
            display: flex;
            flex-direction: column;
            gap: 8px;
            height: 100%;
            justify-content: flex-start;
            position: relative;
            z-index: 30;
        }

        /* 四欄不同的霓虹發光邊框 (加強發光與粗度) */
        .layer-presentation {
            border: 3px solid var(--blue-neon);
            box-shadow: 0 0 30px var(--blue-glow), inset 0 0 15px rgba(0, 229, 255, 0.08);
        }
        .layer-application {
            border: 3px solid var(--green-neon);
            box-shadow: 0 0 30px var(--green-glow), inset 0 0 15px rgba(0, 255, 135, 0.08);
        }
        .layer-brain {
            border: 3px solid var(--purple-neon);
            box-shadow: 0 0 30px var(--purple-glow), inset 0 0 15px rgba(213, 61, 255, 0.08);
        }
        .layer-security {
            border: 3px solid var(--orange-neon);
            box-shadow: 0 0 30px var(--orange-glow), inset 0 0 15px rgba(255, 124, 0, 0.08);
        }

        /* 欄位標題 (放大) */
        .layer-title {
            font-family: 'Outfit', sans-serif;
            font-size: 20px; /* 大幅放大字體 */
            font-weight: 700;
            text-align: center;
            padding-bottom: 12px;
            border-bottom: 2px solid rgba(255, 255, 255, 0.15);
            letter-spacing: 0.8px;
            text-transform: uppercase;
        }
        .layer-presentation .layer-title { color: var(--blue-neon); text-shadow: 0 0 6px var(--blue-glow); }
        .layer-application .layer-title { color: var(--green-neon); text-shadow: 0 0 6px var(--green-glow); }
        .layer-brain .layer-title { color: var(--purple-neon); text-shadow: 0 0 6px var(--purple-glow); }
        .layer-security .layer-title { color: var(--orange-neon); text-shadow: 0 0 6px var(--orange-glow); }

        /* 子卡片 (Eraser 經典卡片 - 提高對比與大字體) */
        .node-card {
            background: #060a16; /* 完全不透明的深黑卡片底色 */
            border: 2px solid rgba(255, 255, 255, 0.15); /* 明確的卡片邊界對比 */
            border-radius: 12px;
            padding: 8px; /* 增加內邊距 */
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            gap: 6px;
            min-height: 96px; /* 提高卡片高度以完美裝載大字體 */
            flex-grow: 1;
            transition: all 0.2s ease;
        }
        .node-card:hover {
            transform: scale(1.02);
            border-color: rgba(255, 255, 255, 0.3);
            box-shadow: 0 6px 15px rgba(255, 255, 255, 0.08);
        }

        /* 卡片發光邊界 (加粗) */
        .layer-presentation .node-card { border-left: 5px solid var(--blue-neon); }
        .layer-application .node-card { border-left: 5px solid var(--green-neon); }
        .layer-brain .node-card { border-left: 5px solid var(--purple-neon); }
        .layer-security .node-card { border-left: 5px solid var(--orange-neon); }

        .node-icon {
            width: 32px;
            height: 32px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.05);
        }
        .node-icon svg {
            width: 18px !important;
            height: 18px !important;
        }
        .layer-presentation .node-icon { color: var(--blue-neon); filter: drop-shadow(0 0 6px var(--blue-glow)); }
        .layer-application .node-icon { color: var(--green-neon); filter: drop-shadow(0 0 6px var(--green-glow)); }
        .layer-brain .node-icon { color: var(--purple-neon); filter: drop-shadow(0 0 6px var(--purple-glow)); }
        .layer-security .node-icon { color: var(--orange-neon); filter: drop-shadow(0 0 6px var(--orange-glow)); }

        .node-title {
            font-family: 'Outfit', sans-serif;
            font-size: 16px; /* 大幅放大標題 */
            font-weight: 700;
            color: #ffffff;
        }

        .node-desc {
            font-size: 12.5px; /* 顯著放大描述 */
            color: var(--text-sub);
            line-height: 1.4;
        }

        /* 垂直流向箭頭 */
        .vertical-flow-arrow {
            text-align: center;
            font-size: 14px; /* 顯著放大 */
            line-height: 1;
            margin: -6px 0;
            opacity: 0.85;
        }��題 */
            font-weight: 700;
            color: #ffffff;
        }

        .node-desc {
            font-size: 15.5px; /* 顯著放大描述 */
            color: var(--text-sub);
            line-height: 1.4;
        }

        /* 垂直流向箭頭 */
        .vertical-flow-arrow {
            text-align: center;
            font-size: 20px; /* 顯著放大 */
            line-height: 1;
            margin: -4px 0;
            opacity: 0.85;
        }
        .layer-presentation .vertical-flow-arrow { color: var(--blue-neon); }
        .layer-application .vertical-flow-arrow { color: var(--green-neon); }
        .layer-brain .vertical-flow-arrow { color: var(--purple-neon); }
        .layer-security .vertical-flow-arrow { color: var(--orange-neon); }

        /* 覆蓋於背景上的 SVG 畫布，專門繪製霓虹發光連接線 */
        .flow-canvas {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 20;
        }

        footer {
            margin-top: 24px;
            font-family: 'Fira Code', sans-serif;
            font-size: 13px; /* 放大頁尾 */
            color: var(--text-sub);
            text-align: center;
            z-index: 10;
        }

        /* 列印媒體優化 */
        @media print {
            body {
                background: #ffffff !important;
                color: #000000 !important;
            }
            .architecture-container {
                border: 1px solid #cbd5e1 !important;
                background: #ffffff !important;
            }
            .column-wrapper {
                background: #ffffff !important;
                border: 1px solid #cbd5e1 !important;
            }
            .node-card {
                background: #f8fafc !important;
                border: 1px solid #cbd5e1 !important;
            }
            .node-title, h1 {
                color: #000000 !important;
            }
        }
    </style>
</head>
<body>

<header>
    <h1>BreezySign Architecture</h1>
    <div class="subtitle">Eraser.io Style Interactive Dataflow Diagram</div>
</header>

<div class="architecture-container">

    <!-- 絕對定位 SVG 發光關係線條 (加強線寬與霓虹強度) -->
    <svg class="flow-canvas" viewBox="0 0 1366 768">
        <defs>
            <!-- 藍色發光濾鏡 -->
            <filter id="glow-blue" x="-30%" y="-30%" width="160%" height="160%">
                <feGaussianBlur stdDeviation="6.0" result="blur" />
                <feMerge>
                    <feMergeNode in="blur" />
                    <feMergeNode in="SourceGraphic" />
                </feMerge>
            </filter>
            <!-- 綠色發光濾鏡 -->
            <filter id="glow-green" x="-30%" y="-30%" width="160%" height="160%">
                <feGaussianBlur stdDeviation="6.0" result="blur" />
                <feMerge>
                    <feMergeNode in="blur" />
                    <feMergeNode in="SourceGraphic" />
                </feMerge>
            </filter>
            <!-- 紫色發光濾鏡 -->
            <filter id="glow-purple" x="-30%" y="-30%" width="160%" height="160%">
                <feGaussianBlur stdDeviation="6.0" result="blur" />
                <feMerge>
                    <feMergeNode in="blur" />
                    <feMergeNode in="SourceGraphic" />
                </feMerge>
            </filter>

            <!-- 各色箭頭標記 -->
            <marker id="arrow-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#00e5ff" />
            </marker>
            <marker id="arrow-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#00ff87" />
            </marker>
            <marker id="arrow-purple" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#d53dff" />
            </marker>
        </defs>

        <!-- Presentation ➡️ Application (CLI Tool 底部引出，分叉指向 CRM、BCR、CLM) -->
        <!-- M: CLI 卡片中心偏右 (X=210, Y=630) H:340 V:分叉對齊 -->
        <path d="M 210 635 H 320" stroke="#00e5ff" stroke-width="4.6" fill="none" filter="url(#glow-blue)" />
        <!-- 分支 1 指向 CRM (Y=175) -->
        <path d="M 320 635 V 175 H 430" stroke="#00e5ff" stroke-width="4.6" fill="none" filter="url(#glow-blue)" marker-end="url(#arrow-blue)" />
        <!-- 分支 2 指向 BCR (Y=285) -->
        <path d="M 320 635 V 285 H 430" stroke="#00e5ff" stroke-width="4.6" fill="none" filter="url(#glow-blue)" marker-end="url(#arrow-blue)" />
        <!-- 分支 3 指向 CLM (Y=510) -->
        <path d="M 320 635 V 510 H 430" stroke="#00e5ff" stroke-width="4.6" fill="none" filter="url(#glow-blue)" marker-end="url(#arrow-blue)" />

        <!-- Application ➡️ AI Brain Core (從 BCR/CLM 右側引出指向 Ollama Router/Qwen LLM) -->
        <!-- 從 CRM 右側 (Y=175) 指向 Ollama Router (Y=220) -->
        <path d="M 755 175 H 805 V 220 H 880" stroke="#00ff87" stroke-width="4.6" fill="none" filter="url(#glow-green)" marker-end="url(#arrow-green)" />
        <!-- 從 CLM 右側 (Y=510) 指向 Qwen LLM (Y=350) -->
        <path d="M 755 510 H 805 V 350 H 880" stroke="#00ff87" stroke-width="4.6" fill="none" filter="url(#glow-green)" marker-end="url(#arrow-green)" />

        <!-- AI Brain Core ➡️ Security & Boundary (從 ReAct Loop 右側引出指向 DMZ Gateway) -->
        <!-- 從 ReAct Loop 右側 (Y=610) 指向 DMZ Gateway (Y=275) -->
        <path d="M 1190 610 H 1220 V 275 H 1250" stroke="#d53dff" stroke-width="4.6" fill="none" filter="url(#glow-purple)" marker-end="url(#arrow-purple)" />
    </svg>

    <!-- 1. Presentation Layer -->
    <div class="column-wrapper layer-presentation">
        <div class="layer-title">Presentation Layer</div>
        
        <!-- Web Console -->
        <div class="node-card">
            <div class="node-icon">
                <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="9" y1="3" x2="9" y2="21"></line></svg>
            </div>
            <div class="node-title">Web Console</div>
            <div class="node-desc">Web-based integration portal</div>
        </div>
        
        <div class="vertical-flow-arrow">⬇</div>

        <!-- CLI Tool -->
        <div class="node-card" style="margin-top: auto; margin-bottom: 20px;">
            <div class="node-icon">
                <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 17 10 11 4 5"></polyline><line x1="12" y1="19" x2="20" y2="19"></line></svg>
            </div>
            <div class="node-title">CLI Tool</div>
            <div class="node-desc">Command-line management CLI</div>
        </div>
    </div>

    <!-- 2. Application Layer (全英文、簡潔描述) -->
    <div class="column-wrapper layer-application">
        <div class="layer-title">Application Layer</div>
        
        <!-- BreezyCRM -->
        <div class="node-card">
            <div class="node-icon">
                <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
            </div>
            <div class="node-title">BreezyCRM</div>
            <div class="node-desc">Micro CRM system</div>
        </div>
        
        <div class="vertical-flow-arrow">⬇</div>

        <!-- BCR -->
        <div class="node-card">
            <div class="node-icon">
                <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="16" rx="2"></rect><circle cx="9" cy="10" r="2"></circle><path d="M15 13h4M15 17h4"></path></svg>
            </div>
            <div class="node-title">BCR</div>
            <div class="node-desc">Business card OCR capture</div>
        </div>

        <div class="vertical-flow-arrow">⬇</div>

        <!-- BPM / Workflow -->
        <div class="node-card">
            <div class="node-icon">
                <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
            </div>
            <div class="node-title">BPM / Workflow</div>
            <div class="node-desc">Visual approval engine</div>
        </div>

        <div class="vertical-flow-arrow">⬇</div>

        <!-- CLM / E-Sign -->
        <div class="node-card">
            <div class="node-icon">
                <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9"></path><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path></svg>
            </div>
            <div class="node-title">BreezyCLM / E-Sign</div>
            <div class="node-desc">Contract life-cycle dispatch</div>
        </div>

        <div class="vertical-flow-arrow">⬇</div>

        <!-- BreezyKM -->
        <div class="node-card">
            <div class="node-icon">
                <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
            </div>
            <div class="node-title">BreezyKM</div>
            <div class="node-desc">Contract summary & archive</div>
        </div>
    </div>

    <!-- 3. AI Brain Core (全英文、簡潔描述) -->
    <div class="column-wrapper layer-brain">
        <div class="layer-title">AI Brain Core</div>
        
        <!-- Ollama Router -->
        <div class="node-card">
            <div class="node-icon">
                <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 3 21 3 21 8"></polyline><line x1="4" y1="20" x2="21" y2="3"></line><polyline points="21 16 21 21 16 21"></polyline><line x1="15" y1="15" x2="21" y2="21"></line><line x1="4" y1="4" x2="9" y2="9"></line></svg>
            </div>
            <div class="node-title">Ollama Router</div>
            <div class="node-desc">RAG embedding & model router</div>
        </div>
        
        <div class="vertical-flow-arrow">⬇</div>

        <!-- Qwen LLM -->
        <div class="node-card">
            <div class="node-icon">
                <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2"><path d="M9.59 4.59A2 2 0 1 1 11 8H9m10.59 11.41A2 2 0 1 1 18 16h2m-9 0A8 8 0 1 0 3 9h2"></path></svg>
            </div>
            <div class="node-title">Qwen LLM (Local)</div>
            <div class="node-desc">Local inference & PII masking</div>
        </div>

        <div class="vertical-flow-arrow">⬇</div>

        <!-- ChromaDB / Qdrant -->
        <div class="node-card">
            <div class="node-icon">
                <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2"><ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path><path d="M3 12c0 1.66 4 3 9 3s9-1.34 9-3"></path></svg>
            </div>
            <div class="node-title">ChromaDB / Qdrant</div>
            <div class="node-desc">Vector search & memory store</div>
        </div>

        <div class="vertical-flow-arrow">⬇</div>

        <!-- ReAct Agent Loop -->
        <div class="node-card">
            <div class="node-icon">
                <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"></path></svg>
            </div>
            <div class="node-title">ReAct Agent Loop</div>
            <div class="node-desc">Autonomous decision & HITL gate</div>
        </div>
    </div>

    <!-- 4. Security & Boundary (全英文、簡潔描述) -->
    <div class="column-wrapper layer-security">
        <div class="layer-title">Security & Boundary</div>
        
        <!-- DMZ Gateway -->
        <div class="node-card">
            <div class="node-icon">
                <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
            </div>
            <div class="node-title">DMZ Gateway</div>
            <div class="node-desc">Network isolated port proxy</div>
        </div>
        
        <div class="vertical-flow-arrow">⬇</div>

        <!-- BreezySign Cloud -->
        <div class="node-card">
            <div class="node-icon">
                <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"></path></svg>
            </div>
            <div class="node-title">BreezySign Cloud</div>
            <div class="node-desc">Cloud AATL & LTV signing</div>
        </div>

        <div class="vertical-flow-arrow">⬇</div>

        <!-- Offline Local Sign -->
        <div class="node-card">
            <div class="node-icon">
                <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path><circle cx="12" cy="16" r="1"></circle></svg>
            </div>
            <div class="node-title">Offline Local Sign</div>
            <div class="node-desc">Offline private CA signature</div>
        </div>
    </div>

</div>

<footer>
    <p>BreezySign Neon Blueprint ． 2026H2 Dataflow & Integration Architecture (Technical Draft)</p>
</footer>

</body>
</html>
"""

def main():
    # 確保 outputs 目錄存在
    os.makedirs("outputs", exist_ok=True)
    
    # 動態獲取當前時間戳
    now_str = datetime.datetime.now().strftime("%Y%m%d-%H%M")
    
    # 定義檔案名稱 (使用 breezysign-architecture)
    output_html_name = f"{now_str}-breezysign-architecture.html"
    output_pdf_name = f"{now_str}-breezysign-architecture.pdf"
    output_png_name = f"{now_str}-breezysign-architecture.png"
    
    output_html_path = os.path.join("outputs", output_html_name)
    output_pdf_path = os.path.join("outputs", output_pdf_name)
    output_png_path = os.path.join("outputs", output_png_name)
    
    abs_html = os.path.abspath(output_html_path)
    abs_pdf = os.path.abspath(output_pdf_path)
    abs_png = os.path.abspath(output_png_path)
    
    # 1. 寫入 HTML 檔案
    print("Writing BreezySign Architecture HTML file...")
    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(html_template)
    print(f"[SUCCESS] HTML written to: {abs_html}")
    
    # 2. 尋找 Edge 或 Chrome 瀏覽器進行 PDF / PNG 轉換
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
        print("[ERROR] Microsoft Edge or Google Chrome not found. Cannot export PDF/PNG.")
        sys.exit(1)
        
    # 3. 執行 Headless PDF 轉換
    print(f"Calling browser for headless PDF generation...")
    cmd_pdf = [
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
        subprocess.run(cmd_pdf, check=True, timeout=30)
        print(f"[SUCCESS] PDF successfully compiled and written to: {abs_pdf}")
    except Exception as e:
        print(f"[ERROR] Failed to compile PDF: {e}")
        sys.exit(1)
        
    # 4. 執行 Headless PNG 截圖轉換 (指定緊湊尺寸以減少留白並在 PDF 中放大文字)
    print(f"Calling browser for headless PNG generation (Forced 1400x1020)...")
    cmd_png = [
        browser_exe,
        "--headless",
        "--disable-gpu",
        "--disable-software-rasterizer",
        "--disable-extensions",
        "--no-sandbox",
        "--window-size=1400,1020",
        "--screenshot=" + abs_png,
        "file:///" + abs_html.replace("\\", "/")
    ]
    
    try:
        subprocess.run(cmd_png, check=True, timeout=30)
        print(f"[SUCCESS] PNG successfully screenshotted and written to: {abs_png}")
        print(f"PNG Size: {os.path.getsize(abs_png)} bytes")
        
        # 寫入結果供主腳本參照
        with open("outputs/arch_breezysign_generation_result.txt", "w", encoding="utf-8") as f:
            f.write(f"HTML: {output_html_path}\n")
            f.write(f"PDF: {output_pdf_path}\n")
            f.write(f"PNG: {output_png_path}\n")
            
    except Exception as e:
        print(f"[ERROR] Failed to generate PNG: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
