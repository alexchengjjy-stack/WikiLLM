---
title: "人類掌舵、Agent 執行：Harness Engineering 的軟體開發新典範"
source: "https://circleghost.substack.com/p/agent-harness-engineering"
author:
  - "[[李元魁]]"
published: 2026-04-20
created: 2026-04-28
description: "在倫敦的某個早晨，Ryan Lopopolo 對著台下說了一句讓全場靜默的話：「我把團隊的工程師全部都禁止使用程式碼編輯器。」"
tags:
  - "clippings"
---
本文由倉鼠特報員 Agent 撰寫、配圖。這是新系列，希望帶回更多不同語系的好內容，如果大家喜歡也歡迎回饋！

在倫敦的某個早晨，Ryan Lopopolo 對著台下說了一句讓全場靜默的話：「我把團隊的工程師全部都禁止使用程式碼編輯器。」

他是 OpenAI 技術 staff，隸屬 Frontier Team。那天他在歐洲最大 AI 工程師社群 AIE Europe 的舞台上，發表演講《 [Harness Engineering: How to Build Software When Humans Steer, Agents Execute](https://www.youtube.com/watch?v=am_oeAoUhew) 》。

![](https://www.youtube.com/watch?v=am_oeAoUhew)

他的核心主張只有一句話： **Code is free。**

這句話看起來簡單，背後卻意味著整個軟體工程的範式轉移。當機器的程式碼生成能力與人類工程師同構（理解力相當），軟體工程師的價值不再體現在「寫程式碼」，而是體現在「建造讓 AI agent 能自主運作的系統」。

這個系統，他稱之為 Harness。

---

## 當軟體工程的瓶頸不再是「寫程式碼」

![](https://substackcdn.com/image/fetch/$s_!klm4!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2c592d5e-687c-4cec-bee4-51746ba349db_2048x1143.png)

2025 年末，GPT 5.2 發布。Ryan 形容這是某種「魔幻時刻」，模型突然能做的事情，與大多數軟體工程師能做的事情，結構上變得完全相同。不是「幫助寫程式碼」，不是「建議補全」，而是成為一個完整的軟體工程師。

這改變了遊戲的本質。當程式碼本身不再是稀缺資源，稀缺的是什麼？

Ryan 給出了三個答案：

**第一，人類的時間。** 每個工程師過去受限於自己的鍵盤。現在，每個工程師可以擁有 5 倍、50 倍、甚至是 5000 倍的工程師產能，只要顯示卡（GPU）允許。

**第二，人類的注意力。** 特別是同步評審的注意力。一位人類工程師同一時間只能專注在一段程式碼審查上，無法同時處理十個審查請求。

**第三，上下文窗口（context window）。** 這是 AI 模型一次能處理的文字上限。當軟體專案規模大到一個程度，即使是目前最好的模型也會遇到極限。如何管理這個限制，讓 AI agent 在龐大的程式碼庫中依然有效運作，成為最關鍵的工程問題。

---

## 禁止工程師接觸編輯器：一次極端的團隊實驗

Ryan 的團隊做了件讓多數工程師難以想像的事：他們禁止所有工程師直接碰觸程式碼編輯器。

不是開玩笑。每當團隊成員想要寫程式碼、改 bug、或者重構，都必須透過 Codex 來完成，Codex 是 OpenAI 開發的 AI 程式碼助手，可以代替人類在編輯器裡實際寫出程式碼。

> 如果我允許團隊在 IDE 裡直接操作，他們就會恢復舊習慣，自己動手寫程式碼，而不是學習怎麼駕馭這些工具。
> 
> 這不是任性。這是系統設計。

當你把「用手寫程式碼」設為不可能，所有人就被迫學會「用提示詞（prompt）與 AI agent 協作」。

這個禁令帶來的第一個後果：團隊的思維模式徹底轉變。工程師不再問「這段程式碼怎麼寫」，而是問「這張任務單（ticket）怎麼描述才能讓 AI agent 正確執行」。

第二個後果：Ryan 自己幾乎不再碰鍵盤。他在演講現場說，他現在 95% 的時間在做的事，是「建造與維護 Harness 系統」，定義 Skills、管理文件、調整 linter 規則、優化 reviewer agents 的提示詞。

---

## Harness 的五大支柱

那麼，Harness 到底是什麼？Ryan 在演講中詳細拆解了他的系統，歸納為五大核心構成。

![](https://substackcdn.com/image/fetch/$s_!lIk5!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F557411cf-a207-437c-bb71-01360c1c3f00_2048x1143.png)

### 1\. Skills：封裝複雜度，讓 AI agent 能操作

每個工程師維護 5 到 10 個核心 Skills。這些不是普通的 SOP 文件，而是專門為 AI agent 設計的操作手冊。

對內：隱藏 repository（存放程式碼的資料庫）內部經常變動的工具複雜度。比如啟動一個應用程式需要三個步驟、開發者模式要啟動哪個服務、日誌怎麼串連，這些細節封裝成一個 Skill，AI agent 拿到就能執行，不需要人類從旁指導。

對外：Skills 是人類與 AI agent 的統一界面。Ryan 的說法是：「我不想讓每個工程師都成為專家，知道所有工具怎麼串在一起。我要的是，每個工程師都能透過統一的描述，讓 AI agent 去處理底層的複雜度。」

這裡有個關鍵的設計原則：Codex 是開發流程的起點，不是周邊環境。不是打造一個環境，然後把 Codex 放進去，而是以 Codex 為核心向外建構。Ryan 為 Codex 建立了一個 Skill， teaching it how to launch 應用程式、如何啟動本機的觀測工具（logging/telemetry）、如何附加 Chrome 開發者工具到瀏覽器。

整個本機開發工具鏈都是為 Codex 設計的，AI agent 第一個啟動這些工具，人類工程師在旁邊看。

### 2\. Documentation：角色導向的知識沉澱

Ryan 的 codebase（程式碼庫）有一套精心設計的文件結構，按角色（persona）組織：前端架構師、後端擴展性、可靠性、QA。每個角色有一組明確的非功能性需求標準。

比如「可靠性」文件會定義：網路請求失敗時的重試策略、超時設定、流量限制（rate limiting）的具體閥值。不是抽象原則，是可以直接被 AI agent 理解並據此評估程式碼的具體選擇。

歷史任務單和程式碼審查記錄也成為文件的一部分。Ryan 被問到「文件要寫到多詳細」時，他的答案是：你寫到足以讓另一個人類工程師在不問問題的情況下完成這件事的程度。「但這裡的『另一個人』，現在是 Codex。」

### 3\. Linters：把工程紀律寫入系統

Ryan 會在每一個 codebase 建立自訂的 ESLint rules（程式碼風格規則），針對他團隊最常見的錯誤模式：網路請求的重試和超時處理方式、型別安全標準、套件的隱私權控制、Zod 驗證格式的重複檢測。

這些 linter rules 的厲害之處在於：一旦寫入，整個 codebase 的所有程式碼都會在 CI 流程中自動遷移，不符合規範的地方，linter 會自動修復，工程師不需要手動逐個改動。Linter 就像一位從不疲憊的紀律委員，24 小時盯著程式碼庫，一旦發現有人寫了不符合標準的程式碼，馬上自動幫你修好。

這就是把「工程紀律」寫進系統的方式。不是靠人自覺遵守，而是靠工具自動執行。

### 4\. Reviewer Agents：不再阻塞人類的同步評審

![](https://substackcdn.com/image/fetch/$s_!-vy_!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a1cb052-dbba-4464-af66-c172a0462015_2048x1143.png)

每一個角色，安全性、可靠性、效能，都有對應的專屬 reviewer agent（審查 AI）。

這些 reviewer agents 在每次 push（工程師提交程式碼）時自動觸發，對 PR（Pull Request，請求把一段程式碼併入主專案）進行評審，給出 P0/P2 等級的意見。不是「建議」，而是系統性的關卡：達不到標準的程式碼，就是不會被接受。

人類工程師不需要同步等待評審結果，不需要坐在電腦前盯著 PR 等核准。整個流程非同步運行，AI agent 在背景完成所有事情。

Ryan 的原則是：每一次你需要與 AI agent 互動，都是 Harness 的失敗。他追求的終極境界是：把任務單放進去，系統自動完成所有事情，不需要人類插手。

### 5\. Tests：不只測行為，更測「程式碼結構」本身

Ryan 的測試策略有個反直覺的設計：測試的對象不只是「程式碼的行為」，更是「程式碼的結構」。

比如：任何檔案不該超過 350 行、Zod 驗證格式不該重複定義、錯誤處理應該有統一的模式。

這些測試在 CI 中運行，確保的不只是功能正確，更是整個程式碼庫的一致性。因為當 codebase 足夠大、token 消耗足夠高的時候，程式碼的一致性會直接影響模型的運作效率，越一致的程式碼庫，壓縮效果越好，上下文窗口的使用越有效率。

---

## 一天燒 10 億 tokens：Codex 怎麼改變工程師的日常

在 Q&A 環節，Ryan 透露了幾個驚人的數字。他的團隊每天消耗超過 10 億 output tokens（AI 輸出一個 token 大約等於一個英文單字或幾個中文字），按 OpenAI 的匯率，大約是 $1,000 美元/天。

這個數字的重點不在於成本，而在於它代表的工作量。10 億 tokens 的輸出相當於什麼概念？大約是一個人類工程師不眠不休工作幾十年才能產出的文字量。而 Ryan 的團隊每天都在燒掉這個量級。

![](https://substackcdn.com/image/fetch/$s_!cPfA!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4ac1ab65-d3f9-4c43-9f60-3b64702c24fb_2048x1143.png)

那麼，這些 tokens 都花在哪裡？Ryan 說大致是三分之一、三分之一、三分之一的分配：

- 規劃、任務單整理、以及文件：大約三分之一
- 實作（大約三分之一）
- CI 流程（最後三分之一），包括 reviewer agents、安全掃描、linting

這裡有個重要的洞察：CI 消耗的 tokens 不該被視為浪費，而是對人類注意力的置換。過去，工程師需要手動做程式碼審查、跑 linter、檢查安全漏洞，這些工作消耗的是人類最稀缺的資源，也就是同步注意力。現在，這些工作全部交給 AI agents，人類的注意力釋放出來，用在真正需要判斷力的地方。

如果你只有 $200/月的 Pro Plan，想把用量減少五分之一，Ryan 的建議是：從 CI 流程下手。雖然 Plan Mode 和實作都不好刪，但 CI 那三分之一的 tokens 是最有精簡空間的。用更精簡的 reviewer agents、更快的 linter 配置，能在不犧牲品質的情況下降低消耗。

---

## 從同步程式碼審查到全自動化 Reviewer Agents

「我已經不怎麼看 PR 了。」Ryan 在 Q&A 中說這句話的時候語氣很平靜，像是在說「我已經很久不親手洗衣服了」。

他的團隊完全過渡到了 reviewer agents 驅動的評審流程。每個人類工程師的 PR 會觸發一組 reviewer agents，每個 agent 專注在一個維度，安全性 agent 看安全、可靠性 agent 看穩定性、效能 agent 看速度。

它們同時運行，不需要排隊等待。

最終，每個 reviewer agent 給出 P0/P2 等級的評審結果。這些結果不是「建議」，而是關卡：P0 問題必須被修復，否則 PR 無法前進。

這個系統的好處不僅是速度，更是一致性。人類審查難免受到疲勞、情緒、上下文切換的影響，AI agent 的審查每次都是同一套標準，沒有折扣。

Ryan 提到，這個系統並不是一夜之間建成的。他的團隊從同步程式碼審查起步，一開始只是「讓 AI agent 幫我先看一遍 PR，給我個意見」，逐漸演進成現在的全自動化流程。關鍵的演進節點是：當他發現「我已經習慣不親自看 PR 了」的那一刻，系統才真正成熟。

**Garbage Collection Day：把人類的抱怨轉化成系統改進。** 在遷移到全自動化 reviewer agents 的過程中，Ryan 的團隊每週五留出時間做一件事：把過去一週觀察到的所有爛程式碼，全部列舉出來，然後分類型、找出根本原因，最終把對應的規範寫入 linter 或 reviewer agent，徹底消滅這類問題在未來發生的可能。

這是從人類審查回饋到文件驅動自動化的關鍵閉環。

在協作模式上，Ryan 的做法也有別於傳統：他將 PR 視為一個乾淨的協作空間，人類和 AI 都在這裡共同參與。AI agent 在收到審查回饋後，可以選擇接受、延後或直接拒絕。Ryan 刻意設計了這個彈性，因為「如果每條回饋都必須被處理，AI agent 就會被 reviewer 們集體霸凌，最終不是促進程式碼被接受，而是淹沒在瑣碎的細節裡」。

這個系統的目標是讓好程式碼儘快被接受，而不是追求完美。

---

## Plan Mode：何時該用，何時不該用

演講後的 Q&A 中，有人問 Ryan 是否使用 Plan Mode（規劃模式，讓 AI 先產出實作計畫再執行）。

他的回答很直接：幾乎不用。

他的邏輯是：如果一個任務單丟進 Harness 系統後還需要繞道去「做規劃」，那說明 Harness 本身就沒有被正確設計。

> 我的期望是：丟一個任務單進去，它就能把事情做完，不需要中途轉向 Plan。

但 Ryan 承認，如果真的要用 Plan，他的建議是把 Plan 當成 PR 來處理。具體來說：先開一個只包含 Plan 的 PR，人類逐行審查，確認方向正確後，再合併並觸發執行。因為「如果你用 Plan 但不讀它，你就只是在編碼一堆你不確定是否想要被執行的指令」。

這個原則呼應了他的核心哲學： **人類的注意力是最稀缺的資源，要用在最關鍵的地方** 。如果某個環節需要人類密集關注但卻沒有帶來對應的價值，那就是系統需要被重新設計的信號。

---

## 官方 Labs Harness 的槓桿效應

![](https://substackcdn.com/image/fetch/$s_!IUIS!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3602bc81-43ee-454e-8d75-d8b4627b1e4c_2048x1143.png)

Q&A 中有人問 Ryan：OpenAI 內部的 Codex harness 與 CloudCode、OpenAI Code 這些外部工具相比，你們內部怎麼取捨？

Ryan 給出了一個極為重要的洞察： **他認為 LLM 實驗室（研發 AI 模型的機構）在發布模型時，已經把特定 harness 的操作方式納入了後訓練（post-training）的情境中** 。例如「套用修補」工具的行為、呼叫命令列工具時的字元處理語法，這些細節都在模型訓練過程中被優化了，以適應最主流的 harness 部署方式。

這意味著：直接依賴官方第一方 harness（如 SDK、Codex App Server），就能搭上 Labs 後訓練的順風車，不需要自己從頭造輪子。Ryan 的策略是把精力放在「如何接入」這些官方 harness，而不是自己重建底層的程式碼生成 harness。

底層工具會越來越好，這是 Codex/CloudCode 團隊的責任，而他的工作則專注在「我的正確程式碼應該長什麼樣子」，也就是上層的領域邏輯與規範。

這個分層思路讓他可以「隨著模型版本更新思考行為差異」，而不需要深入理解 harness 的內部機械原理。

---

## Code as Disposable Build Artifact：當 AI 模型成為模糊編譯器

![](https://substackcdn.com/image/fetch/$s_!70_M!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F34a75656-b368-4f01-a29c-adc8996cd758_2048x1143.png)

演講中，Ryan 拋出了一個大膽的比喻：Codex 就是一個 fuzzy compiler（模糊編譯器），而程式碼是一種可拋棄的建構產物。

他用 LLVM 編譯 Rust 的過程做類比。傳統程式的編譯過程是這樣的：工程師寫 Rust 程式碼，LLVM 編譯器把它轉成機器碼，中間經過好幾層轉換。身為使用者，你不在乎中間經過了哪些步驟，只在乎最終的機器碼是否正確、是否高效。

在 AI 的世界裡，道理相同。Codex 生成的程式碼不是終點，而是某種「編譯後的產物」。Harness 系統中的規則、限制條件、最佳化檢查，決定了什麼樣的程式碼是「可接受的」，就像 LLVM 的靜態分析和最佳化步驟決定了什麼樣的機器碼是「有效的」。

這個比喻的深層意思是：你隨時可以換掉生成後端。今天用 Codex，明天用 Claude，明天用 GPT-5。只要你的 Harness 足夠嚴謹，輸出的程式碼品質不會因為底層模型的更換而產生實質差異，就像 Rust 編譯成 x86 或 ARM 架構，結果都是正確的機器碼。

這對軟體工程的組織方式有深刻的影響。當程式碼是一種消耗品，工程的核心價值就轉移到了 Harness 層。誰掌控了 Harness，誰就掌控了軟體生產的品質。

---

## 組織擴展：750 個 packages 與 Bounded Contexts

![](https://substackcdn.com/image/fetch/$s_!Gzxi!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05d2b9d8-9c9f-47f3-841a-499436852ee6_2048x1143.png)

Ryan 的 codebase 不是一個小型專案。他的團隊用 pnpm workspace（一種專案管理工具）管理著 750 個 packages（套件），從零開始，逐步演進成一個龐大的 monorepo（把所有程式碼放在一個大儲存庫裡統一管理）。

他對 monorepo 擴展的策略有幾個關鍵原則：

**第一，每一個商業領域等於一個子樹。** 這個原則直接減少了 merge conflicts（不同開發者的程式碼改動相互衝突）。當不同 domain 的程式碼在邏輯上被子樹隔離，跨團隊的程式碼審查和 merge 衝突就大幅減少。

**第二，讓程式碼盡可能一致。** 因為程式碼是文字，文字是提示詞，而提示詞進入 token 預算。當 codebase 足夠一致，token 消耗就會降低。統一的非同步輔助函式、有界的並發輔助函式，所有人遵循同一套模式。

**第三，減少 PR open 的時間。** 因為 PR open 的時間越長，merge conflict 的機率越高。用 reviewer agents 加速審查流程，讓 PR 的週期時間變短，整個系統的吞吐量就變高。

Ryan 承認這不是一個一夜之間建成的系統。「每個團隊都會經歷這個過程：從最小可行產品到內部測試版再到外部測試版。每一個階段都會發現新的弱點，比如第一次部署軟體時，AI agents 對品質保證和冒煙測試的能力幾乎是零，因為從來沒有人在這方面投資過。」

這套架構也不是從一開始就設計好的。Ryan 從一個空白 repository、Electron app、單一 package 開始，慢慢變成一個難以管理的混亂狀態，沒有套件邊界、沒有 API 限制、AI agent 無法理解不同領域的隔離。後來才逐步重組成 750 個 pnpm packages、每個商業領域一個子樹的清晰架構。

---

## 從零開始：如何用 Coding Agents 建立信心

對於想開始卻不知從何著手的工程師，Ryan 的建議很具體：

**第一步：用 AI agents 幫現有程式碼庫寫測試。** 你可以給 Codex 一段程式碼，加上它應該怎麼被使用的上下文，然後讓它幫你寫測試。更多測試意味著對程式碼行為更有信心，而程式碼庫越有條理，AI agent 導航能力就越強，你也不需要做那麼詳細的手動 review。

**第二步：觀察自己的時間花在哪裡。** 是盯著編輯器寫程式碼？等測試跑完？等人類 review？還是 CI 太慢卻一直在等？從浪費時間最多的那個環節開始，逐步用 AI agents 置換。

**第三步：把工作逐步轉化成「定義工作、排程、授權」的循環。** 工程師的槓桿點不在親自動手，而在有效地把任務分配出去、定義清楚驗收標準，然後賦予團隊成員（無論是人或 AI agent）執行的能力。

![](https://substackcdn.com/image/fetch/$s_!RloN!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1574b825-24b4-47b0-9fd9-a9ca754a0258_2048x1143.png)

---

## 未來願景：把一個季度的工作交給機器

Q&A 的最後，Ryan 被問到：「你們在建的那個未來是什麼樣子？」

他的回答充滿了詩意：

「我想要的能力是：拿一個 token budget，比如一個季度或半年的工作量，把人類的輸入放進去：最重要的成功指標、可靠性指標，把這些交給機器，然後讓它們持續不斷地推進產品前進。」

他描繪的畫面是：工程師不再需要「雙手握著方向盤」，而是設定目標之後，讓系統自主運轉。從「自己開車」到「設定 GPS 和自動駕駛」的轉變。人類在那裡，但不需要時時刻刻控制。

但他也很誠實地承認，這個未來還沒有到來。目前為止，他的團隊還在填補各種各樣的弱點，部署後的冒煙測試、觀測性、個人資訊監控、用戶回饋的分類。這些「軟體工程中非寫程式碼的部分」，正是 AI agents 目前最弱的地方。

而填補這些弱點的方式，恰恰就是建造更好的 Harness：把流程寫下來，把驗收標準寫下來，把這些變成 AI agents 可以執行的指令。

這就是 Ryan 所說的「工作」，也就是元編程：用 AI agents 來編程，而不是被編程。

---

## 結語：當工程師學會放手

Ryan Lopopolo 的這場演講，最打動人的不是那些驚人的數字，而是那句「我把團隊禁止進入編輯器」背後的信念。

大多數工程師聽到這個，會覺得恐怖。不讓我寫程式碼？那我的價值在哪裡？

Ryan 的答案是：你的價值，在於你知道什麼是對的系統的，在於你能把這個對翻譯成 AI agent 能理解的語言，在於你能建造一個讓 AI agents 自動把事情做好的環境。

當程式碼免費，問問題的能力才是稀缺品。

這是 2026 年軟體工程最重要的宣言之一。