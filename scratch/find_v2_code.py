# -*- coding: utf-8 -*-
import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

log_path = r"C:\Users\alexc\.gemini\antigravity-ide\brain\aa48090c-57d5-4fce-a1f2-1bebc14760a8\.system_generated\logs\transcript.jsonl"

with open(log_path, "r", encoding="utf-8", errors="replace") as f:
    for line_num, line in enumerate(f):
        try:
            data = json.loads(line)
            content = data.get("content", "")
            
            # 檢查是否有寫入 v2.py 的動作
            # 或者是 tool_calls 中有 generate_breezy_brain_arch_v2.py
            tool_calls = data.get("tool_calls", [])
            for tc in tool_calls:
                args = tc.get("args", {})
                target_file = args.get("TargetFile", "")
                if "generate_breezy_brain_arch_v2.py" in target_file or "v2.html" in target_file:
                    print(f"--- Line {line_num+1} Tool Call ---")
                    print(f"Tool: {tc.get('name')}")
                    print(f"Args: {json.dumps(args, ensure_ascii=False)[:500]}...")
                    # 或者是寫入的程式碼內容
                    code_content = args.get("CodeContent", "")
                    if code_content:
                        print("Found CodeContent length:", len(code_content))
                        # 寫出到暫存檔以便我們查看
                        out_path = f"scratch/recovered_v2_from_log_{line_num}.py"
                        with open(out_path, "w", encoding="utf-8") as out_f:
                            out_f.write(code_content)
                        print(f"Recovered code written to: {out_path}")
            
            # 也搜尋 content 中是否有提及
            if "generate_breezy_brain_arch_v2.py" in content or "breezy-brain-architecture_v2" in content:
                print(f"--- Line {line_num+1} Content Match ---")
                print(content[:500] + "...")
                print("-" * 50)
        except Exception as e:
            print(f"Error parsing line {line_num+1}: {e}")
