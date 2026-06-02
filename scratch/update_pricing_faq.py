import os

file_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\sources\breezysign-pricing.md"

with open(file_path, 'rb') as f:
    raw_data = f.read()

print(f"檔案二進位大小: {len(raw_data)} bytes")

target_str = "相較於點點簽 (凱鈿行動 `113電簽0003`)、律果簽 (`113電簽0005`)、捷鵬國際 (`113電簽0007`) 及 FastSIGN (全景軟體 `113電簽0001`)，好好簽擁有同等甚至更長效的國家合規背書，所簽署之合約在台灣法律上具備「推定為親自簽名」之法律效力。"
replacement_str = "好好簽擁有國家合規背書，所簽署之合約在台灣法律上具備「推定為親自簽名」之法律效力。"

encodings = ['utf-8', 'big5', 'cp950', 'utf-16', 'utf-16-le', 'utf-16-be']
success = False

for enc in encodings:
    try:
        target_bytes = target_str.encode(enc)
        replacement_bytes = replacement_str.encode(enc)
        if target_bytes in raw_data:
            new_data = raw_data.replace(target_bytes, replacement_bytes)
            
            # 同時也更新 date_updated (如果是 2026-06-02 則無須，但可能需要更新)
            # 這裡我們可以用 bytes replace
            # 原 date_updated: 2026-06-02 已經在截圖中了，如果不是也可以試著替換
            # 為了保險，我們只替換 FAQ 內容即可
            with open(file_path, 'wb') as f_out:
                f_out.write(new_data)
            print(f"成功！使用編碼 {enc} 找到目標並進行了替換。")
            success = True
            break
    except Exception as e:
        print(f"嘗試編碼 {enc} 時出錯: {e}")

if not success:
    print("未能使用任何已知編碼在檔案中匹配到目標字串。")
    # 我們試著模糊搜索，看看 "113電簽0008" 這幾個字以不同編碼在檔案中的位置
    for enc in ['utf-8', 'big5', 'cp950']:
        try:
            sub_bytes = "113電簽0008".encode(enc)
            if sub_bytes in raw_data:
                print(f"發現 '113電簽0008' 的 {enc} 編碼形式存在於檔案中。")
        except:
            pass
