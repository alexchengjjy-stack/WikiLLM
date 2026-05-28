import re

def extract():
    with open("c:/Users/alexc/OneDrive/文件/WikiLLM/scratch/metrics_summary.txt", "r", encoding="utf-8") as f:
        content = f.read()

    # Split the file by Step markers
    steps = re.split(r"## Step \d+", content)
    print(f"Total steps: {len(steps)}")

    reports = [
        "2025.10.02", "2025.11.03", "2025.12.02", "2026.01.05",
        "2026.02.02", "2026.03.03", "2026.04.02", "2026.05.05"
    ]

    output = []
    for r in reports:
        output.append(f"\n=================== {r} ===================\n")
        # Find steps that mention the report and contain model outputs with details
        found_steps = []
        for step in steps:
            if r in step and ("Dashboard-Company" in step or "Dashboard-Income" in step or "Never signing" in step or "Contact Us Leads" in step):
                # We only want the model's text response, which usually starts after (MODEL)
                if "(MODEL)" in step:
                    found_steps.append(step)
        
        if found_steps:
            # Let's take the longest one which likely contains the most complete extraction
            best_step = max(found_steps, key=len)
            output.append(best_step.strip())
        else:
            output.append("No detailed extraction found in logs.")

    with open("c:/Users/alexc/OneDrive/文件/WikiLLM/scratch/all_months_extracted.txt", "w", encoding="utf-8") as f_out:
        f_out.write("\n".join(output))
    print("Extraction completed and saved to scratch/all_months_extracted.txt")

if __name__ == "__main__":
    extract()
