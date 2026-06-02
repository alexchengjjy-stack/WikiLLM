import os

file_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\wiki\sources\breezysign-pricing.md"

if os.path.exists(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    content = data.decode('utf-8', errors='ignore')
    
    sensitive_words = ["恩主公", "醫院", "捷鵬", "點點簽", "DottedSign", "律果", "FastSIGN", "IDExpert", "Docusign", "Adobe"]
    
    print("敏感詞檢查結果：")
    for word in sensitive_words:
        count = content.count(word)
        print(f"'{word}': 出現 {count} 次")
        if count > 0:
            # 尋找出現的行
            lines = content.split('\n')
            for idx, line in enumerate(lines):
                if word in line:
                    print(f"  第 {idx+1} 行: {line}")
else:
    print("檔案不存在！")
