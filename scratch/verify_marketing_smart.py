import csv
from io import StringIO

file_path = r"C:\Users\alexc\.gemini\antigravity-ide\brain\49388b83-c002-4a3d-b958-4b5448c94f44\.system_generated\steps\263\content.md"

def analyze_smart():
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    csv_start = content.find("日期,免費版註冊數(個人+企業),企業體驗版註冊")
    if csv_start == -1:
        print("Could not find CSV header.")
        return
        
    csv_text = content[csv_start:]
    reader = csv.reader(StringIO(csv_text))
    headers = next(reader)
    
    col_date = headers.index("日期")
    col_free_reg = headers.index("免費版註冊數(個人+企業)")
    col_trial_reg = headers.index("企業體驗版註冊")
    
    col_total_amount = -1
    for i, h in enumerate(headers):
        if "總金額" in h:
            col_total_amount = i
            break
            
    current_year = 2024
    last_month = 7
    
    yearly_data = {
        2024: {"reg": 0, "amt": 0},
        2025: {"reg": 0, "amt": 0},
        2026: {"reg": 0, "amt": 0}
    }
    
    for row in reader:
        if not row or len(row) <= max(col_date, col_free_reg, col_trial_reg, col_total_amount):
            continue
            
        date_val = row[col_date].strip()
        
        if date_val.startswith("總計"):
            # try to find month
            # eg "總計2024/7/1-7/31" or "總計8/1-8/31"
            import re
            match = re.search(r"總計(?:202[456]/)?(\d{1,2})/", date_val)
            if match:
                month = int(match.group(1))
                if month < last_month and (last_month - month) > 5:
                    # Year rollover (e.g. from 12 to 1)
                    current_year += 1
                last_month = month
                
                free_reg = row[col_free_reg].replace(',', '').strip()
                trial_reg = row[col_trial_reg].replace(',', '').strip()
                amt = row[col_total_amount].replace(',', '').strip()
                
                f_r = int(free_reg) if free_reg.isdigit() else 0
                t_r = int(trial_reg) if trial_reg.isdigit() else 0
                a = int(amt) if amt.isdigit() else 0
                
                if current_year in yearly_data:
                    yearly_data[current_year]["reg"] += (f_r + t_r)
                    yearly_data[current_year]["amt"] += a
                    
    print("=== True Pipeline Marketing Numbers ===")
    for y in [2024, 2025, 2026]:
        print(f"Year {y}: Total Reg = {yearly_data[y]['reg']}, Total Amt = {yearly_data[y]['amt']} NTD")

if __name__ == "__main__":
    analyze_smart()
