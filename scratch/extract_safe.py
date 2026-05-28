import re
import traceback

input_path = r"C:\Users\alexc\.gemini\antigravity-ide\brain\49388b83-c002-4a3d-b958-4b5448c94f44\.system_generated\steps\53\content.md"
output_txt_path = r"C:\Users\alexc\OneDrive\文件\WikiLLM\scratch\extracted_customers.txt"

def extract_safely():
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            text = f.read()
            
        # Splitting roughly by order block
        blocks = text.split("訂單編號:")
        
        professional = set()
        business = set()
        enterprise = set()
        
        for block in blocks[1:]:
            # Must contain 2024, 2025, or 2026 to be included
            if not re.search(r"202[456]", block):
                continue
                
            company_match = re.search(r"公司名稱:\s*(.+)", block)
            if company_match:
                name = company_match.group(1).strip()
            else:
                email_match = re.search(r"客戶電郵:\s*(.+)", block)
                if email_match:
                    name = email_match.group(1).strip()
                else:
                    name = None
                    
            if not name or "gmail" in name.lower() or name == "Unknown":
                # Filter out pure personal emails if they don't have a company name
                if "@" in name:
                    continue
            
            # Filter empty names
            if not name.strip():
                continue
                
            if "專業方案" in block:
                professional.add(name)
            elif "商務方案" in block:
                business.add(name)
            elif "企業方案" in block:
                enterprise.add(name)
                
        with open(output_txt_path, 'w', encoding='utf-8') as out:
            out.write("=== ENTERPRISE ===\n")
            for e in sorted(list(enterprise)):
                out.write(e + "\n")
                
            out.write("\n=== BUSINESS ===\n")
            for b in sorted(list(business)):
                out.write(b + "\n")
                
            out.write("\n=== PROFESSIONAL ===\n")
            for p in sorted(list(professional)):
                out.write(p + "\n")
                
    except Exception as e:
        with open(output_txt_path, 'w', encoding='utf-8') as out:
            out.write("ERROR OCCURRED:\n")
            out.write(traceback.format_exc())

if __name__ == "__main__":
    extract_safely()
