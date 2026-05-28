import re

def parse_metrics():
    with open("c:/Users/alexc/OneDrive/文件/WikiLLM/scratch/metrics_summary.txt", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Let's find all steps and analyze where reports are extracted
    # Split by "=== Found at line" or "Step" boundaries
    steps = re.split(r"===+", content)
    print(f"Total blocks split: {len(steps)}")
    
    # We want to search for monthly reports data.
    # Let's save a summary of lines that look like they contain the extracted data
    output = []
    
    reports = [
        "2025.10.02", "2025.11.03", "2025.12.02", "2026.01.05",
        "2026.02.02", "2026.03.03", "2026.04.02", "2026.05.05"
    ]
    
    for r in reports:
        output.append(f"\n=================== REPORT SEARCH: {r} ===================\n")
        # Find blocks containing report date and keywords like "Dashboard"
        found = False
        for step in steps:
            if r in step and ("Dashboard-Company" in step or "Dashboard-Income" in step or "Never signing" in step):
                # Clean up step a bit
                output.append(step.strip())
                found = True
                output.append("\n" + "-"*50 + "\n")
        if not found:
            output.append(f"No direct detailed block found for {r} with Dashboard keywords.\n")

    with open("c:/Users/alexc/OneDrive/文件/WikiLLM/scratch/parsed_report_data.txt", "w", encoding="utf-8") as f_out:
        f_out.write("\n".join(output))
    print("Parsed data written to scratch/parsed_report_data.txt")

if __name__ == "__main__":
    parse_metrics()
