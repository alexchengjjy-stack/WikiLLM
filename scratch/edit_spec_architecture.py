# -*- coding: utf-8 -*-
import sys

def main():
    filename = 'wiki/products/breezy-brain/Product-Spec.md'
    
    with open(filename, 'rb') as f:
        raw_data = f.read()
        
    try:
        content = raw_data.decode('utf-8')
    except Exception as e:
        print(f"Error decoding with utf-8: {e}")
        sys.exit(1)

    # 1. 取代 frontmatter 中的 date_updated
    old_date = 'date_updated: 2026-05-28'
    new_date = 'date_updated: 2026-05-29'
    if old_date not in content:
        print(f"Warning: {old_date} not found in file (already updated?)")
    else:
        content = content.replace(old_date, new_date)

    # 2. 定位 1.5 節位置與第一個 mermaid 位置，並進行區間替換
    content_norm = content.replace('\r\n', '\n')
    
    start_key = '1.5 產品核心'
    start_idx = content_norm.find(start_key)
    if start_idx == -1:
        print(f"Error: key '{start_key}' not found in spec file")
        sys.exit(1)
        
    # 我們要把標題 "### 1.5 產品核心架構圖 (Product Architecture Diagram)" 包含在替換範圍中
    # 往回尋找 '###' 來定位標題的起點
    title_start = content_norm.rfind('###', 0, start_idx)
    if title_start == -1:
        title_start = start_idx
        
    end_key = '```mermaid'
    end_idx = content_norm.find(end_key, title_start)
    if end_idx == -1:
        print("Error: subsequent ```mermaid not found after 1.5 section")
        sys.exit(1)
        
    new_architecture_block = """### 1.5 產品核心架構圖 (Product Architecture Diagram)

為了方便各部門（產品、技術、銷售）在研發與對接時進行精準溝通，BreezyBrain 採用分層式架構設計。大腦中樞（地端 Local LLM）作為核心推理引擎，驅動前段客資 CRM、中段 CLM 合約管理與後段 KM 歸檔，並由 DMZ 網閘安全代理對接外部 BreezySign 雲端 API，或降級執行地端簽署。

為了適應不同的溝通與列印需求，本規格書提供了以下**三種不同形式的旗艦級架構示意圖**：

#### 1.5.1 形式一：產品核心分層架構藍圖 (BreezyBrain Layered Workflow Blueprint)
*   **設計形式**：分層規格說明型架構圖。以直欄將系統垂直切割，卡片內部包含詳細的中文功能說明與技術標籤（Tech Badges），強調模組歸屬與功能規格。
*   **線上預覽與列印**：[HTML 自適應網頁版](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/outputs/20260529-1139-breezy-brain-architecture_v6.html) | [高畫質 PDF 下載](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/outputs/20260529-1139-breezy-brain-architecture_v6.pdf)
*   **架構藍圖預覽**：
<div class="page-break" style="page-break-before: always; text-align: center; margin: 30px 0;">
  <img src="file:///c:/Users/alexc/OneDrive/文件/WikiLLM/outputs/20260529-1139-breezy-brain-architecture_v6.png" style="width: 100%; max-width: 100%; border: 1px solid #cbd5e1; box-shadow: 0 4px 12px rgba(0,0,0,0.15);" alt="BreezyBrain 產品核心分層架構 (V6 流程引導版)" />
</div>

#### 1.5.2 形式二：BreezyBrain 智慧工作流操作系統架構圖 (BreezyBrain Agent Framework)
*   **設計形式**：中央大腦驅動型架構圖。以深藍色發光霓虹風格展示，突顯「大腦中樞」與六大業務垂直支柱（BCR、CRM、BPM、CLM、KM、Integration）的雙向推理與控制流。
*   **架構藍圖預覽**：
<div class="page-break" style="page-break-before: always; text-align: center; margin: 30px 0;">
  <img src="file:///c:/Users/alexc/OneDrive/文件/WikiLLM/outputs/breezy_brain_framework.png" style="width: 100%; max-width: 100%; border: 1px solid #cbd5e1; box-shadow: 0 4px 12px rgba(0,0,0,0.15);" alt="BreezyBrain 智慧工作流操作系統架構圖 (BreezyBrain Agent Framework)" />
</div>

#### 1.5.3 形式三：WikiLLM Agent 系統架構編排藍圖 (WikiLLM Agent Orchestration Blueprint)
*   **設計形式**：Agent 管道流程型架構圖。以深藍色霓虹發光風格展示，呈現從 Raw Ingestion 到 Agent Engine（三層式架構：Planning, Execution, Memory）再到 Local Knowledge Base 的資料流向與協定。
*   **架構藍圖預覽**：
<div class="page-break" style="page-break-before: always; text-align: center; margin: 30px 0;">
  <img src="file:///c:/Users/alexc/OneDrive/文件/WikiLLM/outputs/wikillm_agent_framework.png" style="width: 100%; max-width: 100%; border: 1px solid #cbd5e1; box-shadow: 0 4px 12px rgba(0,0,0,0.15);" alt="WikiLLM Agent 系統架構編排藍圖 (WikiLLM Agent Orchestration Blueprint)" />
</div>

"""

    content_to_write_norm = content_norm[:title_start] + new_architecture_block + content_norm[end_idx:]
    
    if '\r\n' in content:
        content_to_write = content_to_write_norm.replace('\n', '\r\n')
    else:
        content_to_write = content_to_write_norm

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content_to_write)
        
    print("Successfully updated Product-Spec.md dynamically!")

if __name__ == '__main__':
    main()
