# -*- coding: utf-8 -*-
import os
import subprocess
import datetime
import sys

# v4 16:9 橫向 HTML/CSS 架構圖內容定義 (包含模組 SVG 圖示，強固型 16:9 排版)
html_template = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BreezyBrain 產品核心架構圖 (v4 16:9 Landscape Architecture)</title>
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&family=Noto+Sans+TC:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #0b0f19;
            --grid-color: rgba(37, 99, 235, 0.05);
            --primary: #057857; /* 好好簽翠綠 */
            --primary-glow: rgba(5, 120, 87, 0.15);
            --secondary: #0284c7; /* 天空藍 */
            --secondary-glow: rgba(2, 132, 199, 0.15);
            --brain: #7c3aed; /* 大腦紫 */
            --brain-glow: rgba(124, 58, 237, 0.15);
            --border-glow: #ea580c; /* 安全橘 */
            --text-main: #f8fafc;
            --text-sub: #94a3b8;
            --card-bg: rgba(15, 23, 42, 0.72);
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
            background-size: 22px 22px;
            color: var(--text-main);
            min-height: 100vh;
            padding: 24px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            overflow: hidden; /* 防止溢出干擾截圖 */
            position: relative;
        }

        header {
            text-align: center;
            margin-bottom: 20px;
            width: 100%;
            max-width: 1280px;
        }

        .logo-title {
            font-family: 'Outfit', sans-serif;
            font-size: 12px;
            font-weight: 700;
            color: var(--primary);
            letter-spacing: 3px;
            text-transform: uppercase;
            margin-bottom: 4px;
        }

        h1 {
            font-family: 'Outfit', 'Noto Sans TC', sans-serif;
            font-size: 26px;
            font-weight: 800;
            margin-bottom: 6px;
            background: linear-gradient(135deg, #ffffff 40%, #a7f3d0 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -0.5px;
        }

        .subtitle {
            font-size: 13px;
            color: var(--text-sub);
            line-height: 1.4;
        }

        /* 16:9 產品架構圖總容器 (橫向4直欄排列) */
        .architecture-container {
            width: 100%;
            max-width: 1280px;
            display: grid;
            grid-template-columns: 1fr 1.35fr 1.25fr 1fr; /* 寬度優化 */
            gap: 16px;
            aspect-ratio: 16 / 9; /* 強制 16:9 比例 */
            z-index: 10;
        }

        /* 每一欄的大卡片 */
        .column-wrapper {
            background: var(--card-bg);
            border: 1px solid rgba(148, 163, 184, 0.1);
            border-radius: 14px;
            padding: 16px;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.4), inset 0 1px 1px rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(12px);
            display: flex;
            flex-direction: column;
            gap: 8px; /* 緊湊間距 */
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
            font-size: 14px;
            font-weight: 700;
            letter-spacing: 0.5px;
            display: flex;
            align-items: center;
            gap: 6px;
            padding-bottom: 6px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }

        .layer-presentation .layer-title { color: var(--secondary); }
        .layer-application .layer-title { color: var(--primary); }
        .layer-brain .layer-title { color: var(--brain); }
        .layer-security .layer-title { color: var(--border-glow); }

        /* 模組小卡片 */
        .module-card {
            background: rgba(30, 41, 59, 0.4);
            border: 1px solid rgba(255, 255, 255, 0.02);
            border-radius: 8px;
            padding: 7px 10px; /* 內邊距以高度適配 16:9 */
            display: flex;
            flex-direction: column;
            gap: 4px;
            flex-grow: 1;
            justify-content: center;
        }

        .module-header {
            display: flex;
            align-items: center;
            gap: 6px;
            font-size: 12px;
            font-weight: 600;
            color: #ffffff;
            line-height: 1.2;
        }

        .module-header svg {
            flex-shrink: 0;
        }

        .layer-presentation .module-header svg { color: var(--secondary); }
        .layer-application .module-header svg { color: var(--primary); }
        .layer-brain .module-header svg { color: var(--brain); }
        .layer-security .module-header svg { color: var(--border-glow); }

        .module-desc {
            font-size: 10.5px;
            color: var(--text-sub);
            line-height: 1.35;
        }

        .tech-badge-list {
            display: flex;
            flex-wrap: wrap;
            gap: 3px;
            margin-top: 1px;
        }

        .tech-badge {
            font-size: 8px;
            font-weight: 700;
            padding: 1px 3px;
            border-radius: 2px;
            background: rgba(255, 255, 255, 0.05);
            color: #cbd5e1;
        }

        /* 流程指向小標誌 */
        .workflow-arrow {
            text-align: center;
            font-size: 8.5px;
            color: rgba(5, 120, 87, 0.4);
            margin: -4px 0;
            line-height: 1;
            font-weight: 600;
        }

        .arrow-indicator {
            position: absolute;
            top: 50%;
            right: -14px;
            transform: translateY(-50%);
            color: rgba(148, 163, 184, 0.2);
            z-index: 20;
            pointer-events: none;
        }

        /* 移除最後一欄右側的箭頭 */
        .layer-security .arrow-indicator {
            display: none;
        }

        footer {
            margin-top: 20px;
            font-size: 9.5px;
            color: var(--text-sub);
            text-align: center;
            border-top: 1px solid rgba(148, 163, 184, 0.1);
            padding-top: 10px;
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
                padding: 15px !important;
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
    <div class="logo-title">BreezyBrain 16:9 Landscape Blueprint - v4</div>
    <h1>BreezyBrain 產品核心分層架構</h1>
    <p class="subtitle">BreezyBrain 作為好好簽（BreezySign）的高階自動化中樞。此架構依據標準合約作業流程 (BCR ➡️ CRM ➡️ BPM ➡️ CLM ➡️ KM) 循序排列，展示資料流閉環。</p>
</header>

<div class="architecture-container">

    <!-- 1. 展示與接口層 -->
    <div class="column-wrapper layer-presentation">
        <div class="layer-title">
            <svg style="width:14px;height:14px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="9" y1="3" x2="9" y2="21"></line></svg>
            展示與接口層 (Presentation)
        </div>
        
        <!-- Web 整合控制台 -->
        <div class="module-card">
            <div class="module-header">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:13px;height:13px;"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="2" y1="20" x2="22" y2="20"></line><line x1="12" y1="17" x2="12" y2="20"></line></svg>
                Web 整合控制台
            </div>
            <div class="module-desc">無代碼配置後台。提供 CRM 銷售管道看板、大腦 RAG 語意範本對照、工作流編排與法務審查介面。</div>
            <div class="tech-badge-list">
                <span class="tech-badge">Web UI</span>
                <span class="tech-badge">SaaS</span>
            </div>
        </div>
        
        <!-- CLI 工具 -->
        <div class="module-card">
            <div class="module-header">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:13px;height:13px;"><polyline points="4 17 10 11 4 5"></polyline><line x1="12" y1="19" x2="20" y2="19"></line></svg>
                CLI 工具 (breezy-brain)
            </div>
            <div class="module-desc">供維運與工程一鍵操作。支援名片同步、地端降級簽核測試、BPM 流程手動調用與備份。</div>
            <div class="tech-badge-list">
                <span class="tech-badge">CLI Tool</span>
                <span class="tech-badge">Go / Py</span>
            </div>
        </div>
        
        <!-- REST / MCP APIs Gateway -->
        <div class="module-card">
            <div class="module-header">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:13px;height:13px;"><rect x="16" y="16" width="6" height="6" rx="1"></rect><rect x="2" y="16" width="6" height="6" rx="1"></rect><rect x="9" y="2" width="6" height="6" rx="1"></rect><path d="M12 8v8M5 16v-5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v5"></path></svg>
                REST / MCP APIs Gateway
            </div>
            <div class="module-desc">為外部與 Agent 提供統一通道。映射為標準 MCP 協定，支援 mTLS 安全加密。</div>
            <div class="tech-badge-list">
                <span class="tech-badge">MCP Server</span>
                <span class="tech-badge">FastAPI</span>
            </div>
        </div>
        
        <!-- 橫向指向箭頭 -->
        <div class="arrow-indicator">
            <svg style="width:20px;height:20px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </div>
    </div>

    <!-- 2. 核心業務層 -->
    <div class="column-wrapper layer-application">
        <div class="layer-title">
            <svg style="width:14px;height:14px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="2" y="2" width="20" height="8" rx="2" ry="2"></rect><rect x="2" y="14" width="20" height="8" rx="2" ry="2"></rect></svg>
            核心業務層 (Application Workflow)
        </div>
        
        <!-- 模組 1: 名片採集 (BCR) -->
        <div class="module-card">
            <div class="module-header">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:13px;height:13px;"><rect x="3" y="4" width="18" height="16" rx="2"></rect><circle cx="9" cy="10" r="2"></circle><path d="M15 13h4M15 17h4"></path></svg>
                名片採集與 OCR (BCR)
            </div>
            <div class="module-desc">對接蒙恬名片雲。支援拍照上傳、名片資訊 OCR 智慧擷取。</div>
            <div class="tech-badge-list">
                <span class="tech-badge">BCR Ingest</span>
                <span class="tech-badge">WorldCard</span>
            </div>
        </div>
        
        <div class="workflow-arrow">▼ 名片校正 ➡️ CRM 補全</div>
        
        <!-- 模組 2: 微型客資 (BreezyCRM) -->
        <div class="module-card">
            <div class="module-header">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:13px;height:13px;"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                微型客資管理 (BreezyCRM)
            </div>
            <div class="module-desc">配備「去重防禦」與「大腦合理瞎猜補全」；提供三軌獨立 Pipeline。</div>
            <div class="tech-badge-list">
                <span class="tech-badge">Deduplication</span>
                <span class="tech-badge">JSONB Schema</span>
            </div>
        </div>

        <div class="workflow-arrow">▼ 觸發商機 ➡️ BPM 審批</div>

        <!-- 模組 3: 工作流與審批 (BPM / Workflow) -->
        <div class="module-card">
            <div class="module-header">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:13px;height:13px;"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                工作流與審批引擎 (BPM)
            </div>
            <div class="module-desc">Node-based 視覺化工作流編排，結合「人工審批守門員」例外處理。</div>
            <div class="tech-badge-list">
                <span class="tech-badge">Node Editor</span>
                <span class="tech-badge">HITL Gate</span>
            </div>
        </div>

        <div class="workflow-arrow">▼ 審批通過 ➡️ CLM 送簽</div>

        <!-- 模組 4: 電子簽章 (CLM / E-Sign) -->
        <div class="module-card">
            <div class="module-header">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:13px;height:13px;"><path d="M12 20h9"></path><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path></svg>
                電子簽章與 CLM 派單
            </div>
            <div class="module-desc">自動執行「大腦語意範本匹配」，完成動態合約派單變數自動填寫。</div>
            <div class="tech-badge-list">
                <span class="tech-badge">BreezyCLM</span>
                <span class="tech-badge">Auto-Match</span>
            </div>
        </div>

        <div class="workflow-arrow">▼ 完簽 PDF ➡️ KM 歸檔</div>

        <!-- 模組 5: 知識管理 (BreezyKM) -->
        <div class="module-card">
            <div class="module-header">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:13px;height:13px;"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
                知識管理智庫 (BreezyKM)
            </div>
            <div class="module-desc">合約完簽之知識沉澱。自動 100 字合約摘要，建立知識圖譜關聯。</div>
            <div class="tech-badge-list">
                <span class="tech-badge">Graphify</span>
                <span class="tech-badge">RAG Storage</span>
            </div>
        </div>
        
        <!-- 橫向指向箭頭 -->
        <div class="arrow-indicator">
            <svg style="width:20px;height:20px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </div>
    </div>

    <!-- 3. AI 智能大腦中樞 -->
    <div class="column-wrapper layer-brain">
        <div class="layer-title">
            <svg style="width:14px;height:14px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"></path><path d="M12 6v6l4 2"></path></svg>
            AI 智能大腦中樞 (AI Brain Core)
        </div>
        
        <!-- Ollama API / Router -->
        <div class="module-card">
            <div class="module-header">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:13px;height:13px;"><polyline points="16 3 21 3 21 8"></polyline><line x1="4" y1="20" x2="21" y2="3"></line><polyline points="21 16 21 21 16 21"></polyline><line x1="15" y1="15" x2="21" y2="21"></line><line x1="4" y1="4" x2="9" y2="9"></line></svg>
                Ollama API / Router
            </div>
            <div class="module-desc">地端大腦模型代理。處理 RAG 嵌入，並內嵌模型降級與雲端備用大腦路由。</div>
            <div class="tech-badge-list">
                <span class="tech-badge">Ollama</span>
                <span class="tech-badge">Router</span>
            </div>
        </div>
        
        <!-- Qwen 2.5 推理大腦 -->
        <div class="module-card">
            <div class="module-header">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:13px;height:13px;"><path d="M9.59 4.59A2 2 0 1 1 11 8H9m10.59 11.41A2 2 0 1 1 18 16h2m-9 0A8 8 0 1 0 3 9h2"></path></svg>
                Qwen 2.5 推理大腦
            </div>
            <div class="module-desc">地端大腦推理模型。完成客資清洗、風險審查與個資脫敏（PII Masking）。</div>
            <div class="tech-badge-list">
                <span class="tech-badge">Local LLM</span>
                <span class="tech-badge">7B/14B</span>
            </div>
        </div>
        
        <!-- ChromaDB / Qdrant RAG -->
        <div class="module-card">
            <div class="module-header">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:13px;height:13px;"><ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path><path d="M3 12c0 1.66 4 3 9 3s9-1.34 9-3"></path></svg>
                ChromaDB / Qdrant RAG
            </div>
            <div class="module-desc">向量檢索記憶庫。合約向量化儲存，支援 GDPR 被遺忘權之 metadata 抹除。</div>
            <div class="tech-badge-list">
                <span class="tech-badge">Vector DB</span>
                <span class="tech-badge">PII Audit</span>
            </div>
        </div>
        
        <!-- ReAct Agent Loop & Gate -->
        <div class="module-card">
            <div class="module-header">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:13px;height:13px;"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"></path></svg>
                ReAct Agent Loop & Gate
            </div>
            <div class="module-desc">決策與推理迴圈。結合「人工確認守門員」，低置信或中高風險合約強制人工覆核。</div>
            <div class="tech-badge-list">
                <span class="tech-badge">ReAct Loop</span>
                <span class="tech-badge">HITL</span>
            </div>
        </div>
        
        <!-- 橫向指向箭頭 -->
        <div class="arrow-indicator">
            <svg style="width:20px;height:20px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </div>
    </div>

    <!-- 4. 安全與外部對接邊界 -->
    <div class="column-wrapper layer-security">
        <div class="layer-title">
            <svg style="width:14px;height:14px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
            安全與外部對接邊界 (Security)
        </div>
        
        <!-- DMZ 網閘代理 -->
        <div class="module-card">
            <div class="module-header">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:13px;height:13px;"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
                DMZ 網閘代理 (Proxy)
            </div>
            <div class="module-desc">針對企業 100% 物理隔離地端，提供網閘方案，限縮時戳通訊埠對外連通。</div>
            <div class="tech-badge-list">
                <span class="tech-badge">DMZ Proxy</span>
                <span class="tech-badge">Strict Port</span>
            </div>
        </div>
        
        <!-- BreezySign 雲端 API -->
        <div class="module-card">
            <div class="module-header">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:13px;height:13px;"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"></path></svg>
                BreezySign 雲端 API
            </div>
            <div class="module-desc">呼叫電子簽章主站。透過中華電信與憑證機構完成 AATL 認證與 LTV 時戳。</div>
            <div class="tech-badge-list">
                <span class="tech-badge">Cloud E-Sign</span>
                <span class="tech-badge">AATL / LTV</span>
            </div>
        </div>
        
        <!-- 地端降級電子簽名 -->
        <div class="module-card">
            <div class="module-header">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="width:13px;height:13px;"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path><circle cx="12" cy="16" r="1"></circle></svg>
                地端降級電子簽名
            </div>
            <div class="module-desc">當客戶禁止聯外時，系統啟用降級自簽模式，採用地端私鑰與 SHA256 雜湊簽核。</div>
            <div class="tech-badge-list">
                <span class="tech-badge">Offline E-Sign</span>
                <span class="tech-badge">Private CA</span>
            </div>
        </div>
    </div>

</div>

<footer>
    <p>架構圖編號: BZS-ARCH-169-20260529-04 | 蒙恬科技 (PenPower) BreezyBrain 專案開發小組 ． 2026H2 橫向工作流架構藍圖 (技術討論稿)</p>
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
    output_html_name = f"{now_str}-breezy-brain-architecture_v4.html"
    output_pdf_name = f"{now_str}-breezy-brain-architecture_v4.pdf"
    output_png_name = f"{now_str}-breezy-brain-architecture_v4.png"
    
    output_html_path = os.path.join("outputs", output_html_name)
    output_pdf_path = os.path.join("outputs", output_pdf_name)
    output_png_path = os.path.join("outputs", output_png_name)
    
    abs_html = os.path.abspath(output_html_path)
    abs_pdf = os.path.abspath(output_pdf_path)
    abs_png = os.path.abspath(output_png_path)
    
    # 1. 寫入 HTML 檔案
    print("Writing 16:9 landscape architecture v4 HTML file...")
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
        
    # 4. 執行 Headless PNG 截圖轉換 (指定 16:9 尺寸 1920x1080)
    print(f"Calling browser for headless PNG generation (Forced 1920x1080)...")
    cmd_png = [
        browser_exe,
        "--headless",
        "--disable-gpu",
        "--disable-software-rasterizer",
        "--disable-extensions",
        "--no-sandbox",
        "--window-size=1920,1080",
        "--screenshot=" + abs_png,
        "file:///" + abs_html.replace("\\", "/")
    ]
    
    try:
        subprocess.run(cmd_png, check=True, timeout=30)
        print(f"[SUCCESS] PNG successfully screenshotted and written to: {abs_png}")
        print(f"PNG Size: {os.path.getsize(abs_png)} bytes")
        
        # 寫入結果供主腳本參照
        with open("outputs/arch_v4_generation_result.txt", "w", encoding="utf-8") as f:
            f.write(f"HTML: {output_html_path}\n")
            f.write(f"PDF: {output_pdf_path}\n")
            f.write(f"PNG: {output_png_path}\n")
            
    except Exception as e:
        print(f"[ERROR] Failed to generate PNG: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
