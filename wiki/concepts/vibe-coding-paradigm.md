---
title: "Vibe Coding Paradigm"
type: concept
category: AI-Engineering
tags: [Vibe-Coding, Zero-Code, AI-Agent, Workflow]
date_created: 2026-04-19
date_updated: 2026-04-19
source_count: 5
summary: "Vibe Coding：以自然語言引導 AI 開發產品的新範式，強調需求對齊、設計優先與持續迭代。"
---

# Vibe Coding Paradigm (編程範式革命)

> Vibe Coding 泛指在 AI Agent 大行其道的時代，人類從「親手寫程式碼」退居二線，轉而將精力集中在「透過自然語言交流與需求挖掘」來指揮 AI 開發軟體的工作方法。

---

## 核心哲學與實踐心法

### 1. 先編排，再開發
傳統開發常常陷入修改底層架構的泥淖。Vibe Coding 主張**在投入開發前，先用極低成本的 Markdown 文件配置 Skill 與 Agent 將業務流程（Logic）跑通**。跑通了再轉譯為代碼，方向不會錯；跑不通幾分鐘就能推翻重來。

### 2. 第一受眾是 AI，而非人類
開發考量的第一優先級不再是 UI 的按鈕與佈局，而是「這套服務能否提供給 AI 調用的介面 (CLI / API)」。**人類是在使用 Agent，AI 才是直接操作工具的對象**。產品介面是被功能「推」出來的結果，是用容器來承載動態技能的畫布。

### 3. 設計圖優於一切的優先級 (Design First)
沒有設計圖讓 AI 自己發揮，大多都會組合出糟糕的設計。Vibe Coding 中有一個核心層級約定：
- **視覺呈現**：以設計工具 (如 Figma, Pencil) 中的設計圖為最高依據。
- **UI 佈局與調性**：以 Design Brief (設計規範) 為主。
- **邏輯與功能**：以 Product Spec (產品文件) 為主。
當遇到程式或 UI 衝突時，永遠以設計稿優先。

### 4. Prompt as Logic
軟體的業務邏輯再也不是 `if-else` 的判斷語句，而是存在於 `constants.ts` 中的系統提示詞。提示詞寫得愈好、約束得愈緊，生成結果的品質便愈穩定。

## Vibe Coding 的可靠性防護：CLAUDE.md 12 條行為契約

雖然 Vibe Coding 賦予了人類以自然語言快速構建原型與產品的非凡能力，但其最大的命門在於 AI 隨機性所帶來的高出錯率（無約束時高達 41%）。為使 Vibe Coding 真正邁向「工程級」的生產可用，必須導入 [[claude-rules-12-commandments|CLAUDE.md 12 條黃金行為契約]]，將出錯率極限壓縮至 3%。

### 1. 行為契約的兩階段演進
* **第一階段：基礎寫碼行為約束（錯誤率 41% → 11%）**
  由 Forrest Chang 基於 Andrej Karpathy 對 AI 寫碼盲點的抱怨總結出 4 條基礎規則（**思考優先、簡單至上、手術式修改、目標導向**）。這 4 條規則為 Vibe Coding 奠定了「不猜測、拒絕過度工程、不隨手重構周邊代碼」的紀律底線。
* **第二階段：多步驟 AI 代理協作優化（錯誤率 11% → 3%）**
  當 Vibe Coding 邁向大型專案與多步驟 Agent-orchestration 長任務時，AI 面臨長上下文丟失、測試作假、風格融合混亂等新型盲點。Mnimiy 擴充的 8 條新規則（**只做判斷事、token 預算制、衝突攤開講、寫前先讀、驗證業務意圖、每步 checkpoint、遵循現有慣例、fail loud**）成功封鎖了所有長程開發的失控漏洞。

### 2. 注意力預算與 Token 最佳實踐
實證數據打破了傳統提示詞工程（Prompt Engineering）的多項迷思，為 Vibe Coding 提供了極具價值的工程指導：
* **情境隔離防止注意力爭奪**：規則由 4 條擴展至 12 條時，指令遵循度僅從 78% 微幅變動至 76%。因為 12 條規則涵蓋了完全不同的觸發情境（如長任務、測試、代碼衝突等），不會在單一任務執行中互相爭奪 AI 的注意力預算。
* **抽象規則遠優於給予範例 (Few-shot)**：在 Vibe Coding 提示詞中，寫 3 個範例所消耗的 token 預算相當於 10 條抽象規則。更糟的是，範例會導致 AI 產生「過度擬合 (Over-fitting)」而不知變通。**因此，以高度精煉的抽象行為規則（如 12-rule template）來約束 AI，是防範 token 崩塌與提升模型表現的黃金準則**。
* **動作指令大於情緒勒索**：對 AI 進行情緒勒索（如「請仔細思考」、「你要表現得像個資深工程師」）是純雜訊，會導致遵循度崩潰至 30%。**指令必須是具體可驗證的動作**（例如：寫前讀出導出、checkpoint 匯報）。

---

## 關聯實踐
- [[toxic-development-system|毒舌開發系統]]：透過特定 AI 模型挖掘真正需求。
- [[harness-engineering|Harness Engineering]]：為防範 Vibe Coding 過程的幻覺，所需的系統性防護機制。
- [[aipm-framework-4|Product Manager 4.0 (AIPM 4.0)]]：將 Vibe Coding 心法容器化、進化升級的系統架構。
