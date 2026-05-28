import os
import urllib.request
import urllib.error

# 圖片 URL 列表
urls = [
    # Dashboard-Company (1張)
    "https://breezysign.notion.site/image/attachment%3A70ab0597-11df-4bce-b471-7894afb97b14%3Aimage.png?table=block&id=3574c12a-560a-808c-b04c-dda92277926d&spaceId=55abce07-47b9-4d73-ba51-826bae7c8fa4&width=2000",
    # Dashboard-Income (1張)
    "https://breezysign.notion.site/image/attachment%3Afbd6f80e-aa87-4a49-8287-e53bbd57b19c%3Aimage.png?table=block&id=3574c12a-560a-80d1-be36-e024d650e4da&spaceId=55abce07-47b9-4d73-ba51-826bae7c8fa4&width=2000",
    # Paid Company (1張)
    "https://breezysign.notion.site/image/attachment%3A1d39a548-75bb-404d-888f-0f8fd5cfac9d%3Aimage.png?table=block&id=3574c12a-560a-80bf-bdc2-e6673d2a25dc&spaceId=55abce07-47b9-4d73-ba51-826bae7c8fa4&width=2000",
    # Contact Us Leads (8張)
    "https://breezysign.notion.site/image/attachment%3A223333be-94a7-4462-95f6-52fd72577426%3Aimage.png?table=block&id=3574c12a-560a-8014-90b5-d2ad8358bcf5&spaceId=55abce07-47b9-4d73-ba51-826bae7c8fa4&width=2000",
    "https://breezysign.notion.site/image/attachment%3Aaef44343-c261-4957-8bf5-4ddbbcc368ad%3Aimage.png?table=block&id=3574c12a-560a-804f-83c4-d91b0a8afe9b&spaceId=55abce07-47b9-4d73-ba51-826bae7c8fa4&width=2000",
    "https://breezysign.notion.site/image/attachment%3Ae3d4a7ee-a367-434d-9be8-10c709f62ff8%3Aimage.png?table=block&id=3574c12a-560a-80eb-ba32-c72c37f5283d&spaceId=55abce07-47b9-4d73-ba51-826bae7c8fa4&width=2000",
    "https://breezysign.notion.site/image/attachment%3A02c160ce-ffa1-458d-a5c5-8b162f6218e5%3Aimage.png?table=block&id=3574c12a-560a-80e3-821b-c032150d23a9&spaceId=55abce07-47b9-4d73-ba51-826bae7c8fa4&width=2000",
    "https://breezysign.notion.site/image/attachment%3Aa730b4f1-2e16-4c27-b38c-397fad989f46%3Aimage.png?table=block&id=3574c12a-560a-806f-aa33-ea6e926de7f6&spaceId=55abce07-47b9-4d73-ba51-826bae7c8fa4&width=2000",
    "https://breezysign.notion.site/image/attachment%3Add7c6a75-c291-496c-8ce5-49812ec4e76b%3Aimage.png?table=block&id=3574c12a-560a-8020-9c0f-c89076c7d5c0&spaceId=55abce07-47b9-4d73-ba51-826bae7c8fa4&width=2000",
    "https://breezysign.notion.site/image/attachment%3Aa1ee6ae1-4849-414f-842b-6bd097fd7c3c%3Aimage.png?table=block&id=3574c12a-560a-80bd-bbb7-c4e35dcb1538&spaceId=55abce07-47b9-4d73-ba51-826bae7c8fa4&width=2000",
    "https://breezysign.notion.site/image/attachment%3A5021472a-8fb9-4b21-9544-d79b7b83e527%3Aimage.png?table=block&id=3574c12a-560a-80e5-93cd-e7abaef5f97c&spaceId=55abce07-47b9-4d73-ba51-826bae7c8fa4&width=1600"
]

out_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch\images_202605"
os.makedirs(out_dir, exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

for i, url in enumerate(urls):
    filename = f"img_{i+1}.png"
    filepath = os.path.join(out_dir, filename)
    print(f"Downloading {url} to {filepath}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            with open(filepath, 'wb') as f:
                f.write(response.read())
        print(f"Successfully downloaded {filename}")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code} for {filename}: {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL Error for {filename}: {e.reason}")
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
