import json
import os

log_path = r"C:\Users\alexc\.gemini\antigravity-ide\brain\bfa43e7c-da6a-41f8-adba-24a8fbc39ce4\.system_generated\logs\transcript.jsonl"
output_path = r"c:\Users\alexc\OneDrive\文件\WikiLLM\scratch\log_extracted.md"

if not os.path.exists(log_path):
    print(f"Error: Log file not found at {log_path}")
    exit(1)

extracted = []
with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
            source = data.get("source")
            content = data.get("content", "")
            step_index = data.get("step_index")
            
            # We want model planner responses or user inputs
            if source == "MODEL" and content:
                # Clean up if it's a model response
                extracted.append(f"## Step {step_index} (MODEL)\n\n{content}\n\n---\n")
            elif source == "USER_EXPLICIT" and content:
                extracted.append(f"## Step {step_index} (USER)\n\n{content}\n\n---\n")
        except Exception as e:
            print(f"Error parsing line: {e}")

with open(output_path, 'w', encoding='utf-8') as out:
    out.write("\n".join(extracted))

print(f"Extracted logs written to {output_path}")
