# -*- coding: utf-8 -*-
import os

path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\index.md"
if not os.path.exists(path):
    print("index.md path not found")
    exit(1)

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

target = "* **[BreezyBrain 產品需求文件 (Product Spec)](products/breezy-brain/Product-Spec.md)** — MVP 階段需求定義，含 CRM, CLM, BPM, KM, UI 白牌自訂性、Docker 容器化與 GCP MVP 部署架構規格。"
replacement = "* **[BreezyBrain 產品需求文件 (Product Spec)](products/breezy-brain/Product-Spec.md)** — MVP 階段需求定義，含四種形式架構展示圖，涵蓋 CRM, CLM, BPM, KM, UI 白牌自訂性、Docker 容器化與 GCP MVP 部署架構規格。"

if target in content:
    content = content.replace(target, replacement)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[SUCCESS] index.md successfully updated with UTF-8 encoding.")
else:
    print("[ERROR] Target string not found in index.md. Let me double check content.")
