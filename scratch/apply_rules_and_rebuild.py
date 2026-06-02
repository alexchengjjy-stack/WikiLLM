import os
import re
import subprocess

workspace_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM"

# 1. 修改 Playbook: esign-competitor-monitoring-mechanism.md
playbook_path = os.path.join(workspace_dir, "wiki", "playbooks", "esign-competitor-monitoring-mechanism.md")
if os.path.exists(playbook_path):
    with open(playbook_path, 'r', encoding='utf-8') as f:
        playbook_content = f.read()
    
    # 檢查是否已包含此規範，如果沒有則加在結尾
    if "核心普查原則與限制規範" not in playbook_content:
        additional_rule = """

---

## ⚠️ 核心普查原則與限制規範

為確保情報普查的絕對嚴謹性與實事求是，未來凡是進行市場普查報告、對比報告（如競品 SEO/GEO 普查）或電子簽章能量登錄競品情報普查快照時，必須遵循以下鐵律：

1. **公開正式站為唯一基準**：對我方及競品的所有情報採集與指標比對，均必須以**對外公開之正式站（Production）各頁面公布的正式資訊為唯一基準**。
2. **嚴格排除非公開資訊**：我方內部的**工作報告、測試官網、產品規劃與進行中的專案開發進度**（例如尚未正式對外公布的 ISV/API 整合專案），**一律不得**作為我方已上線之資訊寫入普查快照中，以防超前描述與事實偏誤。
3. **實地探測與覆核**：必須實際執行爬取或探測各個個別競品網站之網頁最新情況，確保事實完全準確，嚴禁僅憑舊資料推估。
"""
        playbook_content += additional_rule
        with open(playbook_path, 'w', encoding='utf-8') as f:
            f.write(playbook_content)
        print("[SUCCESS] 成功將限制規範寫入 Playbook 檔案！")
    else:
        print("[INFO] Playbook 中已存在該限制規範。")
else:
    print(f"[ERROR] 找不到 Playbook 檔案: {playbook_path}")


# 2. 修改快照報告: esign-monitoring-snapshot-202606.md
snapshot_path = os.path.join(workspace_dir, "wiki", "analyses", "esign", "esign-monitoring-snapshot-202606.md")
if os.path.exists(snapshot_path):
    with open(snapshot_path, 'r', encoding='utf-8') as f:
        snapshot_content = f.read()
    
    target_str = "已將「113電簽0008」聲明正式同步上線 Production 官網。持續優化與鼎新 ERP 整合。"
    replacement_str = "已將「113電簽0008」聲明正式同步上線 Production 官網。"
    
    if target_str in snapshot_content:
        snapshot_content = snapshot_content.replace(target_str, replacement_str)
        with open(snapshot_path, 'w', encoding='utf-8') as f:
            f.write(snapshot_content)
        print("[SUCCESS] 成功修正快照報告中的好好簽產品動態！")
    else:
        print("[INFO] 快照報告中未找到目標字串或已被修正。")
else:
    print(f"[ERROR] 找不到快照報告: {snapshot_path}")


# 3. 修改 PDF 生成腳本: generate_competitor_snapshot_pdf.py
pdf_script_path = os.path.join(workspace_dir, "scratch", "generate_competitor_snapshot_pdf.py")
if os.path.exists(pdf_script_path):
    with open(pdf_script_path, 'r', encoding='utf-8') as f:
        pdf_content = f.read()
    
    target_str = "已將「113電簽0008」聲明正式同步上線 Production 官網。持續優化與鼎新 ERP 整合。"
    replacement_str = "已將「113電簽0008」聲明正式同步上線 Production 官網。"
    
    if target_str in pdf_content:
        pdf_content = pdf_content.replace(target_str, replacement_str)
        with open(pdf_script_path, 'w', encoding='utf-8') as f:
            f.write(pdf_content)
        print("[SUCCESS] 成功修正 PDF 生成腳本中的好好簽產品動態！")
    else:
        print("[INFO] PDF 生成腳本中未找到目標字串或已被修正。")
else:
    print(f"[ERROR] 找不到 PDF 生成腳本: {pdf_script_path}")


# 4. 修改 PPTX 生成腳本: generate_competitor_snapshot_pptx.py
pptx_script_path = os.path.join(workspace_dir, "scratch", "generate_competitor_snapshot_pptx.py")
if os.path.exists(pptx_script_path):
    with open(pptx_script_path, 'r', encoding='utf-8') as f:
        pptx_content = f.read()
    
    target_str = "已將「113電簽0008」聲明正式同步上線 Production 官網。持續優化與鼎新 ERP 整合。"
    replacement_str = "已將「113電簽0008」聲明正式同步上線 Production 官網。"
    
    if target_str in pptx_content:
        pptx_content = pptx_content.replace(target_str, replacement_str)
        with open(pptx_script_path, 'w', encoding='utf-8') as f:
            f.write(pptx_content)
        print("[SUCCESS] 成功修正 PPTX 生成腳本中的好好簽產品動態！")
    else:
        print("[INFO] PPTX 生成腳本中未找到目標字串或已被修正。")
else:
    print(f"[ERROR] 找不到 PPTX 生成腳本: {pptx_script_path}")


# 5. 重新生成 6 月份的 HTML, PDF, PPTX 快照報告
print("\n--- 重新編譯快照 PDF 與 HTML ---")
res_pdf = subprocess.run(["py", pdf_script_path], cwd=workspace_dir, capture_output=True, text=True, encoding='utf-8', errors='ignore')
print(res_pdf.stdout)
if res_pdf.returncode == 0:
    print("[SUCCESS] HTML 與 PDF 快照重新生成成功！")
else:
    print(f"[ERROR] HTML 與 PDF 快照重新生成失敗: {res_pdf.stderr}")

print("\n--- 重新編譯快照 PPTX ---")
res_pptx = subprocess.run(["py", pptx_script_path], cwd=workspace_dir, capture_output=True, text=True, encoding='utf-8', errors='ignore')
print(res_pptx.stdout)
if res_pptx.returncode == 0:
    print("[SUCCESS] PPTX 快照簡報重新生成成功！")
else:
    print(f"[ERROR] PPTX 快照簡報重新生成失敗: {res_pptx.stderr}")
