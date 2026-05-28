import csv
import re
from io import StringIO

file_path = r"C:\Users\alexc\.gemini\antigravity-ide\brain\49388b83-c002-4a3d-b958-4b5448c94f44\.system_generated\steps\263\content.md"

def analyze_sheet():
    with open(file_path, 'r', encoding='utf-8') as f:
        # read the content and find where the actual CSV starts
        content = f.read()
        
    csv_start = content.find("日期,免費版註冊數(個人+企業),企業體驗版註冊")
    if csv_start == -1:
        print("Could not find CSV header.")
        return
        
    # Get the CSV string
    csv_text = content[csv_start:]
    
    # Use csv module
    reader = csv.reader(StringIO(csv_text))
    
    # Find indices of required columns from the header (row 0 or 1 in reader)
    headers = next(reader)
    # The header is actually spanning a few rows based on the preview, let's just find indices from the first row
    try:
        col_date = headers.index("日期")
        col_free_reg = headers.index("免費版註冊數(個人+企業)")
        col_trial_reg = headers.index("企業體驗版註冊")
        
        # Total amount column is tricky because it has newlines
        col_total_amount = -1
        for i, h in enumerate(headers):
            if "總金額" in h:
                col_total_amount = i
                break
    except ValueError as e:
        print("Header parsing error:", e)
        return
        
    print(f"Indices: Date={col_date}, FreeReg={col_free_reg}, TrialReg={col_trial_reg}, TotalAmt={col_total_amount}")
    
    total_reg_2026 = 0
    total_amt_2026 = 0
    
    # Read row by row
    for row in reader:
        if not row or len(row) <= max(col_date, col_free_reg, col_trial_reg, col_total_amount):
            continue
            
        date_val = row[col_date].strip()
        
        # Let's just look at rows that start with "總計2026"
        if date_val.startswith("總計2026"):
            free_reg = row[col_free_reg].replace(',', '').strip()
            trial_reg = row[col_trial_reg].replace(',', '').strip()
            amt = row[col_total_amount].replace(',', '').strip()
            
            f_r = int(free_reg) if free_reg.isdigit() else 0
            t_r = int(trial_reg) if trial_reg.isdigit() else 0
            a = int(amt) if amt.isdigit() else 0
            
            print(f"{date_val}: Free Reg={f_r}, Trial Reg={t_r}, Amount={a}")
            total_reg_2026 += (f_r + t_r)
            total_amt_2026 += a

    print("--- 2026 Summary ---")
    print(f"Total Registrations (Free+Trial): {total_reg_2026}")
    print(f"Total Amount (NTD): {total_amt_2026}")
    
if __name__ == "__main__":
    analyze_sheet()
