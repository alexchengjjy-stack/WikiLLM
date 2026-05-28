---
title: "Harness Engineering 的崛起：打造現代 AI 作業系統架構"
source: "https://jasonchuang.substack.com/p/harness-engineering-ai"
author:
  - "[[Jason Chuang]]"
published: 2026-03-27
created: 2026-04-18
description: "Explore harness engineering and its role in architecting modern AI operating systems. Discover how AI agents and context engineering transform AI infrastructure."
tags:
  - "clippings"
---
![](https://substackcdn.com/image/fetch/$s_!DsCo!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77e0ef9e-4b25-4c48-a7e9-d4d8e06e8bea_2752x1536.png)

**典範轉移：從孤立模型到 Agentic 系統**

AI 的應用格局已經從根本上改變。我們不再只是面對單一回應 prompt 的孤立模型，而是在架構一個讓 AI agent 自主運作、跨工具與資料來源協調複雜工作流程的系統。這個演進揭露了一個關鍵缺口：我們雖然已熟練掌握模型訓練，卻幾乎還沒真正觸碰到如何在生產環境中有效部署這些模型。

這就是 **harness engineering** 登場的時刻——一個以嚴謹的軟體工程思維對待 AI 部署的新興學科。就像作業系統的出現是為了管理硬體與應用程式之間的複雜性，harness engineering 在原始模型能力與真實商業價值之間，建立了一層不可或缺的基礎架構。

這個轉變相當劇烈。過去我們把語言模型當成進階版的自動補全工具；現在的 agentic 系統則能做出決策、協調工作流程、與外部系統互動——同時維持安全性、可靠性與可觀測性。OpenAI 在正式提出 harness engineering 概念時，將此定義為「agent 成為複雜問題解決主要介面的全新典範」。

這場轉型要求我們重新思考框架設計——一個能處理多步驟推理、跨長時間互動管理 context、並與既有基礎架構無縫整合的框架。問題已不再是「你的組織是否要採用 agentic 系統」，而是「你是否有足夠的工程基礎，讓這些系統在規模化後穩定運作」。

---

**基礎架構比喻：LLM 是 CPU、Context 是 RAM、Harness 是 OS**

要理解 harness engineering，我們需要轉換心智模型。把現代 AI 系統想像成一套運算基礎架構：LLM 扮演 CPU 的角色——負責執行指令的核心處理器；context window 則如同 RAM——暫存當下工作資料的揮發性記憶體；而 harness 就是作業系統——負責管理資源、排程任務、協調各元件互動的編排層。

這個比喻不只是詩意的修辭，更是架構上的精準類比。就像作業系統將硬體複雜性抽象化、為應用程式提供穩定介面，harness engineering 建立了基礎層，將 LLM 不可預測的輸出轉化為可靠、可組合的服務。Harness 負責記憶體管理（哪些 context 要保留或捨棄）、程序排程（哪個 agent 在何時回應）、以及 I/O 操作（與外部系統的介接）。

這帶來深遠的意義。當你用這個視角思考 AI 系統，你架構的不再是獨立模型，而是一套擁有自身資源分配策略、容錯模式與服務保證的 AI 作業系統。這也解釋了為什麼 harness engineering 會成為一門獨立學科——它需要融合傳統軟體架構與 AI 特有限制的跨域能力。

最成功的實作案例，都把 harness 視為關鍵基礎架構，而非可拋棄的黏合程式碼。他們投資於可觀測性、在元件間建立清晰的 API contract，並針對個別模型失效時的優雅降級進行設計。

![](https://substackcdn.com/image/fetch/$s_!Qo2l!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F39b28bbc-3771-4061-9a1b-20437b4ceb54_2970x2052.png)

---

**OpenClaw 時刻：開源 Agent 作為新一代全球電腦**

Harness engineering 面臨一個特殊挑戰：AI agent 的能力越來越強，但協調它們的基礎架構卻依然碎片化且封閉。 **OpenClaw 時刻** 正在發生——一個轉向將開源 agent 框架視為共享運算基底的趨勢，就像 Linux 成為雲端運算基礎一樣。

換個方式思考：我們正在從封閉在廠商生態系中的專有 AI agent，走向可互通的 agent 網路——像分散式全球電腦一樣運作。Harness 成為協調異質 agent 能力的核心核心（kernel），在跨多個模型供應商、工具整合與執行環境的工作流程中扮演編排者角色。

這個典範帶來即時的實際效益。建立在開放標準上的 harness 架構，讓組織在保有彈性的同時避免廠商鎖定。當 GPT-5 明天發布、Claude 4 下個月推出，你的 harness 層可以直接吸收升級，應用層不需要重寫。Agent swarm 自行適應；商業邏輯持續留存。

這個時刻之所以特別重要，在於 **可組合性** （composability）這個湧現特性。專注於程式碼生成、資料分析或客戶互動的個別 AI agent，現在可以透過標準化的 harness 協定，被編排成複雜的多 agent 系統。結果就像是智慧本身的微服務架構——每個 agent 對更大的認知工作流程貢獻其離散能力。

然而，這種去中心化帶來了傳統軟體工程尚未完全解決的協調複雜度。

---

**Long-Horizon 工程：多日工作流程的可靠性設計**

這裡才是 harness engineering 真正的難題：跨日（甚至數天）的工作流程。當 AI agent 需要跨 session 維持連貫性、協調多種工具、並在中斷後恢復執行，傳統的錯誤處理機制就會失效。這不是關於捕捉 exception，而是關於架構層級的韌性。

挑戰的核心在於規模化的 **context engineering** 。一個客服 agent 可能需要三天處理一個複雜案例，期間存取多個資料庫、等待人工審核、並與外部系統協調。每次中斷都製造狀態管理問題：agent 是否已完成那個 API 呼叫？哪個版本的客戶紀錄才是最新的？如何在不重複作業或遺失關鍵 context 的情況下繼續執行？

**Checkpoint 系統** 因此不可或缺。有效的 harness 架構需要在邏輯邊界點做明確的狀態快照——不只是記錄發生了什麼，而是精確捕捉 agent 可以安全重啟的位置。可以想像成資料庫的 transaction 機制，但適用於多步驟推理鏈。

實際作法是將長工作流程拆解為可驗證的子任務。與其用「解決客戶問題」作為單一 prompt，harness 工程師設計的編排層會將其拆成可測試的區塊：驗證用戶、取得歷史紀錄、分析模式、草擬回應、等待審核。每個區塊都有自己的 context 管理與恢復策略。

沒有這種設計紀律會發生什麼？沉默的失敗在三步之後才浮現——agent 信心十足地以過時假設繼續執行，製造出數天後人工審查才會發現的串聯錯誤。

---

**Harness Engineering 實戰手冊**

每當一個新工程學科成形，從業者就開始記錄模式——什麼有效、什麼慘敗、以及原因為何。Harness engineering 正到達這個轉折點，可重複使用的藍圖從早期生產部署中逐漸結晶。

這份手冊圍繞三大核心支柱： **可觀測性優先架構** 、 **以失敗模式作為設計輸入** ，以及 **context 壓縮策略** 。

在可觀測性方面，團隊正在建立結構化日誌系統，捕捉的不只是 agent 做了什麼，更是為何做出那個選擇——prompt chain、取得的 context、以及推理軌跡。這不是傳統監控，而是針對 AI 基礎架構的鑑識等級儀器化。

失敗模式設計翻轉了傳統思維。Harness 工程師不寄望 agent 不會出錯，而是系統化整理預期的失敗模式——API 逾時、context window 超載、幻覺出來的 function call——並建立明確的復原路徑。一種實際作法是將每個 agent 動作視為需要驗證才能提交的暫定提案，自然形成 rollback 點。

Context 壓縮已成為一門藝術。當工作流程延伸數天，儲存原始對話歷史在計算上變得過於昂貴。新興模式包含語義摘要層，將已完成子任務蒸餾為緊湊的狀態表示，在不超出 token budget 的前提下保留決策歷史。

這份手冊刻意保持不完整——早期智慧為迭代留下空間。但今日部署 agent 系統的組織越來越把這些模式視為基礎而非實驗性做法，顯示這門學科正從前沿研究快速成熟為生產等級的工程實踐。

---

**OpenAI 與 Harness Engineering 的起源**

2025 年初，當 OpenAI 正式提出「harness engineering」這個術語時，他們宣布的不是新技術，而是為一個在 Codex 部署過程中悄悄成形的新興學科命名。導火線是什麼？建置 GPT-4 與 Codex 的生產團隊，發現自己有 60-70% 的工程時間都花在模型本身以外的事情上。

這個比例揭示了關鍵事實：在 agent 優先架構中，wrapper 程式碼——也就是 agent harness——已成為主要的工程挑戰。OpenAI 的團隊觀察到一致的模式：開發者幾天內就能完成 agent 原型，卻要花上數個月打造讓它適合生產環境的基礎架構。模型能力沒問題；周圍的系統卻很脆弱。

OpenAI 框架特別有影響力的地方，在於他們聚焦於 Codex 特有的失敗模式。程式碼生成 agent 帶來獨特的風險：它們修改活躍系統、產生憑證、執行特權操作。設計不良的 agent harness 可能讓 Codex 刪除生產資料庫，或在日誌中暴露 API key。OpenAI 記錄這些失敗模式，不是理論上的風險，而是真實部署的事故案例。

業界反應立即。幾週內，Stripe、GitHub 和 Replit 的基礎架構團隊紛紛發布自己的 harness 模式，各自針對讓 AI 在生產環境撰寫並執行程式碼的特定限制。共同點是什麼？每個達到生產等級的 Codex 部署都需要一個精密的隔離層——一個能讓 agent 有足夠自由度發揮用處，又不至於造成危害的 harness。

---

**Harness Engineering 三大支柱：Context、Constraints、Cleanup**

每個成功 AI agent 實作的底層，都有三個支柱將功能性系統與脆弱原型區分開來。這是防止你的 agent 變成失控程序或僅是進階聊天機器人的結構框架。

**第一支柱：Context 編排** ——精確在對的時機提供 agent 所需資訊，同時不超載其工作記憶的藝術。實際上，這意味著設計能浮現相關文件的檢索系統、維護不膨脹 token budget 的對話歷史，並在 agent 應該「知道什麼」與「應該查詢什麼」之間建立清晰邊界。例如客服 agent 需要產品規格與近期互動紀錄，但把整個知識庫都丟給它，只會製造延遲與幻覺風險。

**第二支柱：架構性 constraints** ——建立護欄，讓 agent 在安全的操作邊界內運作。這不是限制能力，而是定義清晰的執行路徑。Harness 工程師透過驗證層、審核工作流程和資源限制來實作 constraints，防止串聯失敗。自動化基礎架構變更的 agent，可能有要求人工審核生產部署的 constraint、API 呼叫頻率限制，以及錯誤率飆升時的 rollback 觸發機制。

**第三支柱：Cleanup 協定** ——處理 AI 操作鮮少線性進行的現實。當 agent 遭遇意外回應或部分失敗，cleanup 邏輯決定是否重試、升級處理或優雅降級——即使個別動作出現問題，也能維持系統完整性。

---

**策略性 ROI：將商業流程編碼為可執行的自主性**

Harness engineering 的商業價值超越傳統軟體 ROI 指標——它代表將部落知識轉化為持久、可執行資產的過程。組織在良好架構的 harness 上投資，不只是自動化任務，而是將數十年的機構專業知識編碼進隨每次互動複利增值的系統中。

想想實際意義：正確架構的 harness 將每個商業流程轉化為可重用的模板，無論規模大小都維持一致品質。法務部門的合約審查邏輯、財務團隊的對帳工作流程、客服團隊的升級處理協定——每一個都成為隨時間增值而非折舊的資產。不同於傳統自動化腳本的僵化與脆弱，harness 管理的 agent 在模型升級時同步進化，同時保留反映組織智慧的商業邏輯。

經濟轉型體現在三個維度： **知識槓桿** ——領域專家花數天將流程編碼一次，換來系統以毫秒延遲執行數千次； **品質一致性** ——harness 消除人為疲勞、分心或人員流動帶來的不穩定性； **演進彈性** ——隨著 LLM 進步，同樣的 harness 基礎架構無縫升級，無需重寫。

成功實作與昂貴實驗的差異在哪？策略性 harness engineering 包含內建的 garbage collection 機制，能剪除過時 constraint、識別效能退化模式，並浮現優化機會。這些自我監控系統確保你的投資在初始部署後持續創造回報，建立傳統軟體開發模式無法比擬的複利優勢。

---

**總結建議**

Harness engineering 的崛起代表組織對待 AI 實作方式的根本轉變——從即興實驗轉向系統性基礎架構建設。隨著 codex agent 日益精進，約束、情境化並維護這些自主系統的學科，將成為功能性概念驗證與生產等級 AI 營運之間的關鍵分野。

給從業者的幾個重點：

- **Harness engineering 是基礎架構工作，不是 prompt engineering** ——它需要架構思維與軟體開發嚴謹度
- \*\*三大支柱（context、constraints、cleanup）\*\*提供評估與改善既有 agent 實作的框架
- **ROI 在部落知識轉化為可執行、可稽核的商業流程時才真正實現**
- **從限制條件明確、失敗成本可控的小範圍領域開始** ，讓成功模式可以被量測

最務實的建議？從識別組織中一個目前由人工不一致處理的重複性、多步驟流程開始。圍繞這個單一工作流程建立 harness，配備明確的護欄、完整的 context injection，以及嚴謹的錯誤處理。量測的不只是任務完成率，更是人工升級次數的減少，以及輸出一致性的提升。

AI 的未來不在於更好的模型——而在於更好的 harness。現在就掌握這門學科的組織，將隨 LLM 能力持續擴張而建立起複利增長的競爭優勢。

---

參考Youtube來源

![](https://www.youtube.com/watch?v=qua6FfJmydo)
![](https://www.youtube.com/watch?v=GxBrMX1NPiQ)