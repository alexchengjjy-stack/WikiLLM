# -*- coding: utf-8 -*-
import os

def update_paid_subscribers():
    path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\analyses\bzs\bzs-saas-paid-subscribers-by-plan.md"
    if not os.path.exists(path):
        print(f"[ERROR] {path} not found.")
        return False

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # 移除 BOM 與 \r
    has_bom = content.startswith('\ufeff')
    if has_bom:
        content = content.lstrip('\ufeff')
    content = content.replace("\r", "")

    # 1. 更新計數 141 -> 142
    old_header = "### 企業版 (Enterprise) (141 家)"
    new_header = "### 企業版 (Enterprise) (142 家)"
    if old_header in content:
        content = content.replace(old_header, new_header)
        print("[SUCCESS] Paid subscribers header count updated.")
    else:
        print("[WARNING] Paid subscribers header count not found.")

    # 2. 插入太平洋旅行社到 壹端-大瀚 之後
    old_row = "| 壹端-大瀚 | `-` |  |"
    new_row = "| 壹端-大瀚 | `-` |  |\n| 太平洋旅行社股份有限公司 | `-` | 5/26電匯 NT$60,000, 40人企業版方案年租(6/1生效) |"
    
    if old_row in content:
        content = content.replace(old_row, new_row)
        print("[SUCCESS] Pacific Travel added to paid subscribers list.")
    else:
        print("[WARNING] Old row '壹端-大瀚' not found in paid subscribers.")

    # 3. 更新 metadata 日期
    old_meta = "date_updated: 2026-05-22"
    new_meta = "date_updated: 2026-06-02"
    if old_meta in content:
        content = content.replace(old_meta, new_meta, 1)
        print("[SUCCESS] Paid subscribers metadata date updated.")

    if has_bom:
        content = '\ufeff' + content

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return True

def update_customer_list():
    path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\analyses\bzs\bzs-saas-customer-list.md"
    if not os.path.exists(path):
        print(f"[ERROR] {path} not found.")
        return False

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # 移除 BOM 與 \r
    has_bom = content.startswith('\ufeff')
    if has_bom:
        content = content.lstrip('\ufeff')
    content = content.replace("\r", "")

    # 1. 更新 太平洋旅行社股份有限公司 日報
    old_pac = "| 太平洋旅行社股份有限公司 | 20260513日報.md, 20260521日報.md |"
    new_pac = "| 太平洋旅行社股份有限公司 | 20260513日報.md, 20260521日報.md, 20260529週報.md, 2026.06.02營運報表 |"
    if old_pac in content:
        content = content.replace(old_pac, new_pac)
        print("[SUCCESS] Pacific Travel report reference updated.")

    # 2. 更新 豐盛富足資產管理有限公司 日報
    old_feng = "| 豐盛富足資產管理有限公司 | 20260328日報.md, 20260428日報.md |"
    new_feng = "| 豐盛富足資產管理有限公司 | 20260328日報.md, 20260428日報.md, 20260507日報.md, 2026.06.02營運報表 |"
    if old_feng in content:
        content = content.replace(old_feng, new_feng)
        print("[SUCCESS] Feng Sheng Fu Zu report reference updated.")

    # 3. 更新 富友旅行社有限公司 日報
    old_fuyou = "| 富友旅行社有限公司 | 20260421日報.md |"
    new_fuyou = "| 富友旅行社有限公司 | 20260421日報.md, 20260508日報.md, 2026.06.02營運報表 |"
    if old_fuyou in content:
        content = content.replace(old_fuyou, new_fuyou)
        print("[SUCCESS] Fu You Travel report reference updated.")

    # 4. 更新 耐斯旅行社有限公司 日報
    old_nice = "| 耐斯旅行社有限公司 | 20260516日報.md |"
    new_nice = "| 耐斯旅行社有限公司 | 20260516日報.md, 20260530日報.md, 2026.06.02營運報表 |"
    if old_nice in content:
        content = content.replace(old_nice, new_nice)
        print("[SUCCESS] Nice Tour report reference updated.")

    # 5. 更新 福安管理顧問企業社 日報
    old_fuan = "| 福安管理顧問企業社 | 20260519日報.md |"
    new_fuan = "| 福安管理顧問企業社 | 20260519日報.md, 20260522週報.md, 20260529週報.md, 2026.06.02營運報表 |"
    if old_fuan in content:
        content = content.replace(old_fuan, new_fuan)
        print("[SUCCESS] Fu An report reference updated.")

    # 6. 更新 聯合線上股份有限公司 日報
    old_udn = "| 聯合線上股份有限公司 | 20260417日報.md, 20260422日報.md |"
    new_udn = "| 聯合線上股份有限公司 | 20260417日報.md, 20260422日報.md, 20260520日報.md, 2026.06.02營運報表 |"
    if old_udn in content:
        content = content.replace(old_udn, new_udn)
        print("[SUCCESS] Joint Online report reference updated.")

    # 7. 插入 透明房訊 
    # '透明房訊' 應該插在 '得勝者...' 與 '微風...' 之間，或者 '星辰...' 與 '耐斯...' 之間？
    # '透' -> 't' (t'ou)，'得' -> 'd'，'星' -> 'x'，'耐' -> 'n'。
    # Unicode中 '透' (\u900f)，'得' (\u5f97)，'星' (\u661f)，'耐' (\u8010)。
    # 讓我們看看 '星辰' 之後是：
    # 星辰健康顧問...
    # 星辰行銷...
    # 耐斯旅行社有限公司 (第 256 行)
    # 既然 '透' (\u900f) > '耐' (\u8010) 且 > '星' (\u661f)，
    # 我們看看後面還有沒有比 '透' 大的。
    # 第 257 行是：'聖美麗健康管理顧問有限公司' (\u8056)
    # 第 258 行是：'聚利國際...' (\u805a)
    # 第 259 行是：'聯合線上股份有限公司' (\u806f)
    # 第 267 行是：'臺灣日通...' (\u81fa)
    # 第 273 行是：'茂禾...' (\u8302)
    # 第 288 行是：'豐盛富足資產管理有限公司' (\u8c50)
    # 第 299 行是：'車驅...' (\u8eca)
    # 第 308 行是：'金星...' (\u91d1)
    # 第 318 行是：'長虹...' (\u9577)
    # 第 322 行是：'雅德思...' (\u96c5)
    # 第 325 行是：'雙鍵...' (\u96d9)
    # 第 334 行是：'高飛...' (\u9ad8)
    # 第 335 行是：'鴻茂...' (\u9d3b)
    # 第 336 行是：'麟雲數據科技有限公司' (\u9e9f)
    # 第 337 行是：'黎海岸...' (\u9ece)
    # 第 338 行是：'默聲...' (\u9ed8)
    # 第 340 行是：'鼎偉...' (\u9f0e)
    # 所以 '透' (\u900f) 應該插在 '高飛' (\u9ad8) 與 '鴻茂' (\u9d3b) 之間？
    # '高' (\u9ad8) < '透' (\u900f) < '鴻' (\u9d3b)。
    # 我們看看第 334 行：'高飛高爾夫有限公司'。
    # 335 行：'鴻茂廣告有限公司'。
    # 所以 '透明房訊' 應該插在 '高飛高爾夫有限公司' 之後！
    old_row_t = "| 高飛高爾夫有限公司 | 2025H1_part_5.md |"
    new_row_t = "| 高飛高爾夫有限公司 | 2025H1_part_5.md |\n| 透明房訊 | 20260530日報.md, 2026.06.02營運報表 |"
    if old_row_t in content:
        content = content.replace(old_row_t, new_row_t)
        print("[SUCCESS] Transparent Housing added to customer list.")
    else:
        print("[WARNING] Old row '高飛高爾夫有限公司' not found.")

    # 8. 插入 財團法人自強工業科學基金會
    # '財' (\u8ca1) 應該插在 '貝' (\u8c9d) 與 '越' / '路' / '車' / '軟' / '達' 之間。
    # 讓我們看看第 292 行：'貝登堡智能股份有限公司' (\u8c9d)
    # 293 行：'財團法人流浪動物之家基金會' (\u8ca1)
    # '流' (\u6d41) ＆ '自' (\u81ea)？
    # '自強' 的 '自' 是 \u81ea。
    # 慢著，'財' 是 \u8ca1。'財團法人流浪動物之家基金會' ＆ '財團法人自強工業科學基金會'。
    # 這兩個都以 '財團法人' 開頭。
    # 比較 '流' (\u6d41) 與 '自' (\u81ea)。
    # '自' (\u81ea) > '流' (\u6d41)。
    # 所以 '財團法人自強工業科學基金會' 應該插在 '財團法人流浪動物之家基金會' 之後。
    # 我們看看第 293 行是 '財團法人流浪動物之家基金會'。
    # 第 294 行是 '貳輪嶼股份有限公司' (\u8cb3)。
    # '自' (\u81ea) 的 unicode 大小：
    # 慢著，'財團法人自強...' 以 '財' 開頭，所以它是在 '財...' 這一組裡。
    # '財團法人流浪動物之家基金會'：
    # '財' (\u8ca1) '團' (\u5718) '法' (\u6cd5) '人' (\u4eba) '流' (\u6d41)
    # '財團法人自強工業科學基金會'：
    # '財' (\u8ca1) '團' (\u5718) '法' (\u6cd5) '人' (\u4eba) '自' (\u81ea)
    # 因為 '自' (\u81ea) > '流' (\u6d41)，所以自強應該在流浪動物之後！
    # 那 '貳' (\u8cb3) 呢？
    # '貳' (\u8cb3) > '財' (\u8ca1)，所以 '貳輪嶼' 在 '財團法人自強' 之後。
    # 這很完美！所以自強應該插在 '財團法人流浪動物之家基金會' 之後！
    old_row_z = "| 財團法人流浪動物之家基金會 | 2025H1_part_7.md |"
    new_row_z = "| 財團法人流浪動物之家基金會 | 2025H1_part_7.md |\n| 財團法人自強工業科學基金會 | 20260515日報.md, 2026.06.02營運報表 |"
    if old_row_z in content:
        content = content.replace(old_row_z, new_row_z)
        print("[SUCCESS] Tzu Chiang Foundation added to customer list.")
    else:
        print("[WARNING] Old row '財團法人流浪動物之家基金會' not found.")

    # 9. 更新 metadata 日期
    old_meta = "date_updated: 2026-05-27"
    new_meta = "date_updated: 2026-06-02"
    if old_meta in content:
        content = content.replace(old_meta, new_meta, 1)
        print("[SUCCESS] Customer list metadata date updated.")

    if has_bom:
        content = '\ufeff' + content

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return True

def update_agents_md():
    path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\AGENTS.md"
    if not os.path.exists(path):
        print(f"[ERROR] {path} not found.")
        return False

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # 移除 BOM 與 \r
    has_bom = content.startswith('\ufeff')
    if has_bom:
        content = content.lstrip('\ufeff')
    content = content.replace("\r", "")

    # 尋找品質準則中「內容品質」的位置，加入新條款
    old_quality = """### 內容品質
- **準確性**：所有事實性陳述必須能追溯到具體來源
- **時效性**：標記過時或可能過時的資訊
- **平衡性**：若不同來源有不同觀點，呈現所有觀點並注明
- **可讀性**：使用清晰的標題、列表和段落結構"""

    new_quality = """### 內容品質
- **準確性**：所有事實性陳述必須能追溯到具體來源
- **時效性**：標記過時或可能過時的資訊
- **平衡性**：若不同來源有不同觀點，呈現所有觀點並注明
- **可讀性**：使用清晰的標題、列表和段落結構
- **資料來源一致性與落差處理（新！）**：若分析或撰寫報告時，發現其中所有的資料來源有落差（例如月報提到付費大客成長，但付費客戶名單或客戶清單未同步），LLM Agent **必須主動抓取相關資料進行更新**。若庫中無相關原始數據，**必須主動向操作者（使用者）詢問如何補上或處理**，避免資料時間或數據上的落差。"""

    if old_quality in content:
        content = content.replace(old_quality, new_quality)
        print("[SUCCESS] AGENTS.md quality standards updated.")
    else:
        print("[WARNING] AGENTS.md quality standards old block not found.")

    if has_bom:
        content = '\ufeff' + content

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return True

if __name__ == "__main__":
    update_paid_subscribers()
    update_customer_list()
    update_agents_md()
