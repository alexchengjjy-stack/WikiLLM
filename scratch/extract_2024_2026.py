import re

input_path = r"C:\Users\alexc\.gemini\antigravity-ide\brain\49388b83-c002-4a3d-b958-4b5448c94f44\.system_generated\steps\53\content.md"

def extract_customers_by_year():
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            text = f.read()
            
        blocks = text.split("訂單編號: ")
        
        professional = set()
        business = set()
        enterprise = set()
        
        for block in blocks[1:]:
            # Check year by looking back at the text before "訂單編號" or inside the block for "購買日期: 202[4-6]"
            date_match = re.search(r"購買日期:\s*(202[456])", block)
            if not date_match:
                continue # Skip if not 2024, 2025, or 2026
                
            company_match = re.search(r"公司名稱:\s*(.+)", block)
            if company_match:
                name = company_match.group(1).strip()
            else:
                email_match = re.search(r"客戶電郵:\s*(.+)", block)
                name = email_match.group(1).strip() if email_match else None
                
            if not name or name == "Unknown" or "gmail.com" in name.lower() or "@" in name:
                # If name is just an email, let's skip for cleaner enterprise list, or just keep it
                pass
                
            if not name:
                continue
                
            if "專業方案" in block:
                professional.add(name)
            elif "商務方案" in block:
                business.add(name)
            elif "企業方案" in block:
                enterprise.add(name)
                
        print("--- Enterprise 2024-2026 ---")
        for e in sorted(list(enterprise)):
            print(e)
            
        print("\n--- Business 2024-2026 ---")
        for b in sorted(list(business)):
            print(b)
            
        print("\n--- Professional 2024-2026 ---")
        for p in sorted(list(professional)):
            print(p)
            
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    extract_customers_by_year()
