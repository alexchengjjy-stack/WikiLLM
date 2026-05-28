import re
import codecs

input_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch\log_extracted.md"
output_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch\log_extracted_decoded.md"

with open(input_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 定義一個解碼函數
def decode_unicode_escapes(match):
    try:
        return match.group(0).encode('utf-8').decode('unicode-escape')
    except Exception:
        return match.group(0)

# 使用正則表達式尋找 \uXXXX
decoded_content = re.sub(r'\\u[0-9a-fA-F]{4}', decode_unicode_escapes, content)

# 順便也處理一下其他轉義字符，像是 \n, \t, \" 等
# 因為它原本是 JSON 格式的內容
# 我們可以將常見的 \n 換成真正的換行，\" 換成雙引號，但要小心保留結構
# 這裡簡單處理一下 \n 方便閱讀
# 為了避免弄壞非字串的部分，我們先解 unicode-escape 即可
# 其實直接用 codecs 也能解：
# decoded_content = codecs.escape_decode(bytes(content, "utf-8"))[0].decode("utf-8")
# 但為了保險起見，我們只處理 \uXXXX 和 \n 即可

# 將 \n 轉移回換行符（JSON 中的 \\n）
decoded_content = decoded_content.replace('\\n', '\n').replace('\\t', '\t').replace('\\"', '"')

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(decoded_content)

print(f"解碼完成！已寫入 {output_path}")
