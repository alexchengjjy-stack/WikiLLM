import sys

sys.stdout.reconfigure(encoding='utf-8')
log_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\log.md"

with open(log_path, "r", encoding="utf-8", errors="replace") as f:
    content = f.read()

# 統一換行符
content = content.replace("\r\n", "\n")

# 準備新日誌
new_entry = """## [2026-05-27 18:45] update | 整合三大安全原則與負向流程規格至 Product-Spec.md 並修復損壞之 MVP 路線圖
- **操作者**: LLM Agent (Antigravity)
- **變更與修復檔案**：
  - **修復分析文件**：[wiki/analyses/breezybrain-mvp-roadmap.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/analyses/breezybrain-mvp-roadmap.md) — 補齊第二章 4-Phase 產品路線圖演進，移除第三章重複簡陋的大綱，保留並梳理完整的安全性死角與改善建議。
  - **實質整合規格書**：[wiki/products/breezy-brain/Product-Spec.md](file:///c:/Users/alexc/OneDrive/文件/WikiLLM/wiki/products/breezy-brain/Product-Spec.md) — 將三大安全性原則（1. 操作及資料流程、2. 資訊安全性、3. 個資安全性）防線實質整合至 3.5.1、3.5.5、3.3.2 以及 Epic 7 業務工作流中（包括 Rejected 退回機制、mTLS/Pinning 加密通訊、Qdrant Payload Filter、pii_access.log 個資存取軌跡等）。
- **關鍵發現**：
  - 原規格書的 3.5.1 標題為「MCP 護城河防衛核心思維與威脅模型」，原 `breezybrain-mvp-roadmap.md` 中的安全分析與之呼應。已順利將安全性評估所提出的具體修補措施合規寫入規格書本體。
"""

# 在 "# 🗃️ 操作日誌\n\n" 或是第一個 "## [" 之前插入
target_marker = "# 🗃️ 操作日誌\n\n"
if target_marker not in content:
    target_marker = "# 🗃️ 操作日誌\n"

if target_marker in content:
    parts = content.split(target_marker)
    updated_content = parts[0] + target_marker + new_entry + "\n" + parts[1]
else:
    # 備用方案：在 "---" 結束後（即 YAML 後面）插入
    lines = content.split("\n")
    yaml_end = -1
    yaml_count = 0
    for idx, line in enumerate(lines):
        if line.strip() == "---":
            yaml_count += 1
            if yaml_count == 2:
                yaml_end = idx
                break
    if yaml_end != -1:
        updated_content = "\n".join(lines[:yaml_end+1]) + "\n\n" + new_entry + "\n" + "\n".join(lines[yaml_end+1:])
    else:
        updated_content = new_entry + "\n" + content

with open(log_path, "w", encoding="utf-8") as f:
    f.write(updated_content)

print("wiki/log.md updated successfully!")
