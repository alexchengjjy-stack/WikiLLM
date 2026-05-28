def check():
    with open("c:/Users/alexc/OneDrive/文件/WikiLLM/scratch/metrics_summary.txt", "r", encoding="utf-8") as f:
        content = f.read()
    
    import re
    # Let's search for "2025.11.03", "2025.12.02", "2026.01.05", "2026.02.02", "2026.03.03"
    # Find any match, print 1000 characters after it.
    dates = ["2025.11.03", "2025.12.02", "2026.01.05", "2026.02.02", "2026.03.03"]
    for d in dates:
        print(f"\n====== SEARCHING {d} ======")
        matches = [m.start() for m in re.finditer(d, content)]
        print(f"Found {len(matches)} occurrences")
        # Print a few context blocks for each date
        count = 0
        for m in matches:
            # print 400 chars around the match
            start = max(0, m - 50)
            end = min(len(content), m + 350)
            print(f"Match {count} at index {m}:")
            print(content[start:end])
            print("-" * 50)
            count += 1
            if count >= 3:
                break

if __name__ == "__main__":
    check()
