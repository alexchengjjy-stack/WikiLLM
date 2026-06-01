# -*- coding: utf-8 -*-
"""
outputs 目錄檔案重構與治理腳本
此腳本自動建立 outputs 底下的四個子目錄，並將現有 160 個檔案歸類搬移，移除臨時文字檔。
"""
import os
import shutil
import glob

# 設定路徑
base_dir = r"c:\Users\alexc\OneDrive\文件\WikiLLM"
outputs_dir = os.path.join(base_dir, "outputs")
scratch_dir = os.path.join(base_dir, "scratch")

# 子目錄定義
subdirs = {
    "bzs": os.path.join(outputs_dir, "bzs"),        # 現役好好簽輸出
    "bzb": os.path.join(outputs_dir, "bzb"),        # 下一代好好腦輸出
    "assets": os.path.join(outputs_dir, "assets"),  # 共享圖片與品牌資產
    "templates": os.path.join(outputs_dir, "templates") # 生成模板
}

def main():
    print("=== 開始進行 outputs 目錄物理整理 ===")
    
    # 1. 建立子目錄
    for name, path in subdirs.items():
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"建立子目錄: {path}")
        else:
            print(f"子目錄已存在: {path}")
            
    # 2. 獲取 outputs 下的所有檔案
    all_files = glob.glob(os.path.join(outputs_dir, "*"))
    
    for file_path in all_files:
        if os.path.isdir(file_path):
            # 略過子目錄本身
            continue
            
        file_name = os.path.basename(file_path)
        
        # 排除 README.md 和腳本本身（如果有）
        if file_name.lower() in ["readme.md"]:
            continue
            
        # 3. 分類規則判定
        target_dir = None
        should_delete = False
        
        # 臨時/除錯檔案判定
        if file_name.endswith(".txt") and (
            "result" in file_name or 
            file_name == "run_log.txt" or 
            file_name == "scratch_run_log.txt"
        ):
            should_delete = True
        elif file_name == "generate_pptx.py":
            # 如果是 generate_pptx.py，這應該是在 scratch 下的，outputs 下的是重複檔案，直接刪除
            should_delete = True
        
        # 模板與資產判定 (優先權較高)
        elif "template" in file_name.lower():
            target_dir = subdirs["templates"]
        elif "logo" in file_name.lower() or "cover" in file_name.lower():
            target_dir = subdirs["assets"]
            
        # 好好腦 (bzb / BreezyBrain / Agent Framework 等) 判定
        elif any(k in file_name.lower() for k in ["bzb", "breezy-brain", "breezy_brain", "wikillm_agent"]):
            target_dir = subdirs["bzb"]
        elif any(k in file_name for k in ["BreezyBrain-Product-Spec", "BreezyBrain_General_Edition", "BreezyBrain_Internal_Proposal", "BreezyBrain_PenPower_Edition"]):
            target_dir = subdirs["bzb"]
            
        # 好好簽 (bzs / esign / dottedsign) 判定
        elif any(k in file_name.lower() for k in ["bzs", "esign", "dottedsign"]):
            target_dir = subdirs["bzs"]
            
        # 其他檔案（例如 20260515-si-article 等 si 相關好好簽案子）
        elif file_name.startswith("2026") or "si-article" in file_name or "si-blog" in file_name:
            # 這些都屬於好好簽 (bzs) 的專案/行銷產出
            target_dir = subdirs["bzs"]
        else:
            # 未知檔案，預設歸入 bzs 作為業務產出
            target_dir = subdirs["bzs"]
            
        # 4. 執行移動或刪除
        if should_delete:
            try:
                os.remove(file_path)
                print(f"[刪除] 臨時/重複檔案: {file_name}")
            except Exception as e:
                print(f"[錯誤] 無法刪除 {file_name}: {e}")
        elif target_dir:
            dest_path = os.path.join(target_dir, file_name)
            try:
                # 執行搬移（若目標已存在則覆蓋）
                if os.path.exists(dest_path):
                    os.remove(dest_path)
                shutil.move(file_path, dest_path)
                print(f"[移動] {file_name} -> {os.path.basename(target_dir)}/")
            except Exception as e:
                print(f"[錯誤] 無法移動 {file_name}: {e}")

    print("=== outputs 目錄物理整理完成 ===")

if __name__ == "__main__":
    main()
