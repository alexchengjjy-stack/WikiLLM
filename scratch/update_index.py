# -*- coding: utf-8 -*-
import os

def main():
    index_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\index.md"
    if not os.path.exists(index_path):
        print(f"[ERROR] {index_path} not found.")
        return

    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. 邊界定位法替換專案段落
    start_tag = "### 📁 工作專案追蹤 (Projects)"
    end_tag = "---"

    if start_tag in content:
        parts = content.split(start_tag, 1)
        before = parts[0]
        after_start = parts[1]

        # 尋找 start_tag 之後的第一個 ---
        if end_tag in after_start:
            subparts = after_start.split(end_tag, 1)
            middle = subparts[0]  # 這就是我們要替換的舊專案列表內容
            after = subparts[1]

            new_projects_content = """
> 記錄「正在做什麼」— 進行中的重要工作

* 🔴 **[鼎新電腦 API 對接](projects/ding-xin-api-integration.md)** — API 串接完成與連結時效調優，合約審核中；6/11 直播活動備戰
* 🔴 **[福安健康與職安 API](projects/fuan-api-integration.md)** — 點點簽跳槽大戶 (年用量 2 萬份)，API 專案報價 12 萬簽約中
* 🔴 **[聯合線上 API 對接與公開表單](projects/udn-api-integration.md)** — API 串接完成，業務流程與防偽簽署流程測試中
* 🔴 **[聖洋科技 API 串接](projects/cacafly-api-integration.md)** — 每年 8k-10k 份 API 對接，進行多品牌動態 Logo 規格規劃
* 🔴 **[工研院跨境電子簽章計畫](projects/itri-cross-border-esign.md)** — ⚡ 5/15 截止提交亮點簡報
* 🔴 **[太平洋旅行社 Onboarding](projects/pacific-travel-onboarding.md)** — 40人企業版年租正式生效啟用，後台 UNIFY 共享範本設定完成
* 🔴 **[得勝者 PACS 醫療影像電簽整合](projects/deshengzhe-pacs-integration.md)** — 盧森眼科與東港盧森 7 月上線，PACS AI 醫療影像串接測試中
* 🔴 **[鴻運聯邦 Onboarding](projects/hong-yun-onboarding.md)** — 現場平板簽署與證件上傳大用量需求，預備線上展示
* 🟡 **[華杏出版 Onboarding](projects/huaxing-publishing-onboarding.md)** — 5/26 簡報會後升級專業體驗版，進行 3 個月試用監控與帳號共用防禦
* 🟡 **[海沃管理顧問 Onboarding](projects/hai-wo-onboarding.md)** — 企業版體驗試用中，跟進點點簽轉單痛點，試用至 6/10
* 🟡 **[耐斯旅行社 Onboarding](projects/nice-tour-onboarding.md)** — 旅遊定型化契約 Line 傳簽與公開表單測試通過，引導線上訂閱商務方案月費制
* 🟡 **[麻吉行得通 Onboarding](projects/maji-mobility-onboarding.md)** — 500-600份年約轉單跟進，等待主管決策，7月初重啟聯繫
* 🟡 **[恩主公醫院 AIO 院內平台](projects/enzhugong-hospital-aio.md)** — 護理單位提案，進入預算估算
* 🟡 **[101 客戶 BPM 系統建置](projects/project-101-bpm-deployment.md)** — 交付地端原始碼與安裝文件，進行 isHealth API 檢測機制討論
* 🟡 **[百加資通 BPM 通路合作](projects/pai-plus-bpm-partnership.md)** — 精鈺金屬需求評估中；巨虹電子分潤已結算

"""
            content = before + start_tag + new_projects_content + end_tag + after
            print("[SUCCESS] Projects section replaced via boundary matching.")
        else:
            print("[ERROR] End tag --- not found after projects header.")
    else:
        print("[ERROR] Projects header start tag not found.")

    # 2. 替換 PM 數據分析報表條目
    old_source = "- [BZS PM 數據分析報表彙整 (2025.10-2026.05)](./sources/pm-breezysign-analytics-reports.md) — 好好簽過去 8 個月的 PM/業務關鍵營運日報彙整。"
    new_source = "- [PM BreezySign 分析報表 (2025.10 - 2026.06)](./sources/pm-breezysign-analytics-reports.md) — 產品經理的每月營運儀表板，包含公司整體數據、營收狀況、付費客戶及進件量追蹤。"

    # Check for both old and new sources since the previous script might have already replaced it
    if old_source in content:
        content = content.replace(old_source, new_source)
        print("[SUCCESS] Source summary entry replaced successfully.")
    elif new_source in content:
        print("[INFO] Source summary entry was already replaced in previous run.")
    else:
        # Check with LF ending
        old_source_lf = old_source.replace("\r\n", "\n")
        new_source_lf = new_source.replace("\r\n", "\n")
        content_lf = content.replace("\r\n", "\n")
        if old_source_lf in content_lf:
            content = content_lf.replace(old_source_lf, new_source_lf)
            print("[SUCCESS] Source summary entry replaced successfully (LF).")
        elif new_source_lf in content_lf:
            content = content_lf
            print("[INFO] Source summary entry was already replaced in previous run (LF).")
        else:
            print("[ERROR] Source summary entry not found.")

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[INFO] Index.md save completed.")

if __name__ == "__main__":
    main()
