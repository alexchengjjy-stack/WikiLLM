import os
import urllib.request
import urllib.error

# 圖片 URL 列表
urls = [
    # Dashboard-Company
    "https://breezysign.notion.site/image/attachment%3Ab9b29df9-0e7d-4d56-bfe3-54b660ece2bd%3Aimage.png?table=block&id=2874c12a-560a-8007-a50e-ee46ebbaa6e7&spaceId=55abce07-47b9-4d73-ba51-826bae7c8fa4&width=1890",
    # Dashboard-Income
    "https://breezysign.notion.site/image/attachment%3A0f3aa7b0-4cc9-4205-8141-162b59fc7ccd%3Aimage.png?table=block&id=2804c12a-560a-8028-a87e-f14c0fbcf230&spaceId=55abce07-47b9-4d73-ba51-826bae7c8fa4&width=2000",
    # Contact Us Leads (5張圖片)
    "https://breezysign.notion.site/image/attachment%3A1924fb49-37fd-46b4-9753-5b22d41fd81f%3Aimage.png?table=block&id=2804c12a-560a-8056-a116-c3979e3c2cfd&spaceId=55abce07-47b9-4d73-ba51-826bae7c8fa4&width=1890",
    "https://breezysign.notion.site/image/attachment%3Aa636b690-584e-443d-816f-e66418d0661b%3Aimage.png?table=block&id=2874c12a-560a-8070-a247-c08e54b8890f&spaceId=55abce07-47b9-4d73-ba51-826bae7c8fa4&width=1980",
    "https://breezysign.notion.site/image/attachment%3Adf2256d9-c4d5-4136-af1e-85d809fd792d%3Aimage.png?table=block&id=2874c12a-560a-80bf-92ae-f68b49846d67&spaceId=55abce07-47b9-4d73-ba51-826bae7c8fa4&width=1890",
    "https://breezysign.notion.site/image/attachment%3A75e9aade-9cfe-4910-9c4c-bfb04ee8f8ec%3Aimage.png?table=block&id=2934c12a-560a-8055-863b-d1a32c2242c4&spaceId=55abce07-47b9-4d73-ba51-826bae7c8fa4&width=2000",
    "https://breezysign.notion.site/image/attachment%3A0db0df8d-067c-430a-b576-a285465e6aa4%3Aimage.png?table=block&id=2874c12a-560a-80b3-a304-e2977e31a8dd&spaceId=55abce07-47b9-4d73-ba51-826bae7c8fa4&width=1790"
]

out_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch\images"
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
