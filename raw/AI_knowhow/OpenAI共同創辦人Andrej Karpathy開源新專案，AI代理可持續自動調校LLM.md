---
title: "OpenAI共同創辦人Andrej Karpathy開源新專案，AI代理可持續自動調校LLM"
source: "https://www.ithome.com.tw/news/174306"
author:
  - "[[李建興]]"
published:
created: 2026-05-15
description: "OpenAI共同創辦人Andrej Karpathy公開Autoresearch專案，嘗試把大型語言模型部分研究流程，改寫成可在單張GPU上由AI代理反覆執行的自動實驗迴圈"
tags:
  - "clippings"
---
[![.](https://itadstatic.ithome.com.tw/B5/1778669972_6a045994513e4.gif)](https://itadapi.ithome.com.tw/ads/click?q=B5%7Eithome_index%7E2605B5003)

Andrej Karpathy以Autoresearch自動調校nanochat語言模型約2天，經276次實驗後，累積29項可改善驗證表現的調整。

[![.](https://itadstatic.ithome.com.tw/B3/1778458683_6a01203b556c7.jpg)](https://itadapi.ithome.com.tw/ads/click?q=B3%7Eithome_index%7E2605B3001)

OpenAI創始成員之一Andrej Karpathy在GitHub公開新專案 [Autoresearch](https://github.com/karpathy/autoresearch) ，嘗試把大型語言模型研究中部分原本仰賴人工執行的流程，改寫成可由AI代理反覆執行的自動實驗迴圈。該專案甫公開便獲得大量關注，其提供一個精簡的LLM訓練框架，讓代理可在固定時間內修改訓練程式、啟動實驗、檢查結果，再決定保留或捨棄變更，規範AI在有限運算資源下，處理原本多由研究人員手動完成的部分調整與比較工作。

Autoresearch公開後，很快吸引開發者社群的關注。GitHub頁面顯示，該專案已累積約1.8萬顆星標與約2,300次分叉，並已有數十筆議題與拉取請求。Andrej Karpathy在 [X發布的介紹貼文](https://x.com/karpathy/status/2030371219518931079?s=20) ，也累積超過889萬次查看、4,300次轉發與2.6萬次按讚。

Autoresearch把整個實驗架構簡化到最小可行規模，Andrej Karpathy說明，整個儲存庫真正重要的只有三個核心檔案。其中，prepare.py負責固定常數、資料準備與執行階段工具，train.py是唯一由代理修改的訓練主程式，program.md則由人類撰寫，用來交代任務目標與背景脈絡。使用者不必像傳統研究流程那樣直接改動各段Python程式碼，而是改為用文字設定代理的工作框架，再由代理自行嘗試不同的模型架構、超參數與訓練設定。

該專案強調可比較性，而不是單次執行最佳成績。Autoresearch每次訓練都限制在5分鐘內，並以指標評估模型在驗證資料上的表現，如此讓代理即使修改模型深度、批次大小、最佳化器或注意力機制，也能在相同時間預算下比較結果，較容易判斷哪些調整真正有效。Andrej Karpathy後續也提到，他讓 [Autoresearch持續調整nanochat模型約2天](https://x.com/karpathy/status/2031135152349524125) ，累積出約20項可改善驗證損失（Validation Loss）的變更，且其中一批調整在更大模型上仍能延續效果，最後使模型達到GPT-2水準所需時間，由2.02小時縮短至1.8小時。

Autoresearch適用條件包括單張Nvidia GPU、Python 3.10以上版本，以及uv套件管理工具，目前測試平臺為H100，而CPU、Apple MPS與其他平臺並非目前主要支援重點。