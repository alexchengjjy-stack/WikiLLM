# -*- coding: utf-8 -*-
import os

filepath = r"scratch/generate_ops_report_html.py"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 為了防止 CRLF/LF 的問題，我們使用更寬容的替換策略。
# 我們尋找「財務重要里程碑明細」和它的結尾 div 區塊
# 我們將定位到 </div>\n            </div>\n        </div>
# 這三個 div 分別結束了: highlight-box, Detailed breakdown list, chart-box。

# 我們定義要插入的趨勢表格和柱狀圖 HTML
new_content_to_insert = """

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
"""

# 用正則表達式尋找特定的 </div> 結構
# 我們要替換的目標是第一個玻璃卡片最後的 3 個 </div> 
# 也就是包含：
#                 </div> (highlight-box 結尾)
#             </div> (Detailed breakdown list column 結尾)
#         </div> (chart-box row 結尾)
# 
# 為了避免換行符不匹配，我們使用正規化換行的比對。

import re
pattern = r"(專案對接首期結算\)\。.*?</div>\s*</div>\s*</div>)(\s*)(</div>)"
match = re.search(pattern, content, re.DOTALL)
if match:
    print("Match found!")
    # 將新內容加在 chart-box 結束 (match.group(1)) 之後，但在玻璃卡片結束 (match.group(3)) 之前
    replacement = match.group(1) + new_content_to_insert + match.group(2) + match.group(3)
    new_text = content.replace(match.group(0), replacement)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("HTML report generator updated successfully!")
else:
    print("Target pattern NOT found! Trying fallback...")
    # 備用方案：尋找 "Vertical / API 專案實收業績" 後的第三個 </div>
    idx = content.find("專案對接首期結算")
    if idx != -1:
        print("Fallback index found!")
        # 尋找接下來的三個 </div>
        end_idx = idx
        for _ in range(3):
            end_idx = content.find("</div>", end_idx + 6)
        end_idx += 6 # 包含 "</div>" 字符本身
        
        # 現在 end_idx 是 chart-box 結束位置
        part1 = content[:end_idx]
        part2 = content[end_idx:]
        
        # 我們要把新內容加在 part1 後面，再接上 part2。
        # 另外，為了美觀，我們加上一些換行。
        new_text = part1 + new_content_to_insert + part2
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_text)
        print("Fallback update completed successfully!")
    else:
        print("FAILED: Fallback index also not found!")
