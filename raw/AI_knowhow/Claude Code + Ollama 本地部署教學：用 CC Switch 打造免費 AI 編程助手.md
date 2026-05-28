---
title: "Claude Code + Ollama 本地部署教學：用 CC Switch 打造免費 AI 編程助手"
source: "https://www.knightli.com/zh-tw/2026/05/15/claude-code-ollama-cc-switch-local-agent/"
author:
  - "[[KnightLi]]"
published: 2026-05-15
created: 2026-05-18
description: "整理 Claude Code 透過 CC Switch 接入 Ollama 本地模型的思路：它可以保留 Claude Code 的 Agent 操作能力，同時把推理請求轉到本地模型，但在長上下文、大型工程和多模態相容性上仍有明顯邊界。"
tags:
  - "clippings"
---
最近 `Claude Code` 這類 AI 編程助手很受關注。它的吸引力不只是能聊天寫程式碼，而是可以讀取專案、修改檔案、執行命令、安裝依賴，甚至根據錯誤反覆修正，接近一個可操作的 Agent。

問題在於成本。專案一大，上下文變長，多輪 Agent 操作很容易消耗大量 API 額度。對於只是想試用、改小工具、寫腳本、處理本地私有專案的使用者來說，大家自然會想到：能不能保留 Claude Code 的操作體驗，但把模型換成本地執行？

這套方案的關鍵工具是 `CC Switch` 。它可以讓 Claude Code 透過 OpenAI 相容 API 連接本地 `Ollama` 服務，從而把請求轉發到本地模型，而不是直接走官方 Claude API。

## 這套方案解決什麼問題

可以把整個流程理解為：

```text
Claude Code 桌面端
+ CC Switch API 轉發層
+ Ollama 本地模型
```

Claude Code 仍然負責編程工作流和專案操作，CC Switch 負責模型供應商配置與 API 相容，Ollama 則負責在本機執行模型。

<iframe width="1123" height="280" frameborder="0" allow="attribution-reporting; run-ad-auction" src="https://googleads.g.doubleclick.net/pagead/ads?client=ca-pub-9230324840884748&amp;output=html&amp;h=280&amp;num_ads=1&amp;adk=2652405725&amp;adf=2370273430&amp;w=1123&amp;fwrn=4&amp;fwrnh=100&amp;lmt=1779035741&amp;rafmt=1&amp;armr=3&amp;sem=mc&amp;pwprc=7012339427&amp;ad_type=text_image&amp;format=1123x280&amp;url=https%3A%2F%2Fwww.knightli.com%2Fzh-tw%2F2026%2F05%2F15%2Fclaude-code-ollama-cc-switch-local-agent%2F&amp;fwr=0&amp;pra=3&amp;rh=200&amp;rw=1122&amp;rpe=1&amp;resp_fmts=3&amp;asro=0&amp;aiactd=0&amp;aicctd=0&amp;ailctd=0&amp;aimartd=4&amp;aieuf=1&amp;aicrs=1&amp;fa=27&amp;uach=WyJXaW5kb3dzIiwiMTkuMC4wIiwieDg2IiwiIiwiMTQ4LjAuNzc3OC4xNjgiLG51bGwsMCxudWxsLCI2NCIsW1siQ2hyb21pdW0iLCIxNDguMC43Nzc4LjE2OCJdLFsiR29vZ2xlIENocm9tZSIsIjE0OC4wLjc3NzguMTY4Il0sWyJOb3QvQSlCcmFuZCIsIjk5LjAuMC4wIl1dLDBd&amp;abgtt=6&amp;dt=1779069530465&amp;bpp=6&amp;bdt=1986&amp;idt=6&amp;shv=r20260512&amp;mjsv=m202605120101&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;cookie_enabled=1&amp;eoidce=1&amp;prev_fmts=0x0&amp;nras=2&amp;correlator=8228143292682&amp;frm=20&amp;pv=1&amp;u_tz=480&amp;u_his=1&amp;u_h=1080&amp;u_w=1920&amp;u_ah=1032&amp;u_aw=1920&amp;u_cd=32&amp;u_sd=1&amp;dmc=16&amp;adx=226&amp;ady=932&amp;biw=1905&amp;bih=911&amp;scr_x=0&amp;scr_y=0&amp;eid=95390788&amp;oid=2&amp;pvsid=313147943442323&amp;tmod=2076972085&amp;uas=0&amp;nvt=1&amp;ref=https%3A%2F%2Fwww.google.com%2F&amp;fc=1408&amp;brdim=0%2C0%2C0%2C0%2C1920%2C0%2C0%2C0%2C1920%2C911&amp;vis=1&amp;rsz=%7C%7Cs%7C&amp;abl=NS&amp;fu=128&amp;bc=31&amp;bz=0&amp;ifi=2&amp;uci=a!2&amp;btvi=1&amp;fsb=1&amp;dtd=4995" title="Advertisement" aria-label="Advertisement"></iframe>

這並不代表本地模型會突然變成 Claude。它真正有價值的地方，是讓 Claude Code 的 Agent 工作流可以用在低成本、離線、私有化的本地場景。

## 基本準備

開始之前，需要先準備幾個元件：

1. 安裝 `Git` 。
2. 安裝 `Ollama` 。
3. 拉取一個適合編程的本地模型。
4. 安裝 `CC Switch` 。
5. 本機可以使用 Claude Code。

模型方面，可以先從偏程式碼能力的模型開始，例如 Qwen Coder、DeepSeek Coder，或其他具備較好工具呼叫和程式碼生成能力的模型。模型越大，效果可能越好，但記憶體與 GPU 壓力也會同步上升。

如果電腦記憶體有限，建議先用較小模型跑通流程，再逐步嘗試更大的模型。

## CC Switch 關鍵配置

<iframe width="1123" height="280" frameborder="0" allow="attribution-reporting; run-ad-auction" src="https://googleads.g.doubleclick.net/pagead/ads?client=ca-pub-9230324840884748&amp;output=html&amp;h=280&amp;num_ads=1&amp;adk=2652405725&amp;adf=954940372&amp;w=1123&amp;fwrn=4&amp;fwrnh=100&amp;lmt=1779035741&amp;rafmt=1&amp;armr=3&amp;sem=mc&amp;pwprc=7012339427&amp;ad_type=text_image&amp;format=1123x280&amp;url=https%3A%2F%2Fwww.knightli.com%2Fzh-tw%2F2026%2F05%2F15%2Fclaude-code-ollama-cc-switch-local-agent%2F&amp;fwr=0&amp;pra=3&amp;rh=200&amp;rw=1122&amp;rpe=1&amp;resp_fmts=3&amp;asro=0&amp;aiactd=0&amp;aicctd=0&amp;ailctd=0&amp;aimartd=4&amp;aieuf=1&amp;aicrs=1&amp;fa=27&amp;uach=WyJXaW5kb3dzIiwiMTkuMC4wIiwieDg2IiwiIiwiMTQ4LjAuNzc3OC4xNjgiLG51bGwsMCxudWxsLCI2NCIsW1siQ2hyb21pdW0iLCIxNDguMC43Nzc4LjE2OCJdLFsiR29vZ2xlIENocm9tZSIsIjE0OC4wLjc3NzguMTY4Il0sWyJOb3QvQSlCcmFuZCIsIjk5LjAuMC4wIl1dLDBd&amp;abgtt=6&amp;dt=1779069530483&amp;bpp=1&amp;bdt=2004&amp;idt=1&amp;shv=r20260512&amp;mjsv=m202605120101&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;cookie_enabled=1&amp;eoidce=1&amp;prev_fmts=0x0%2C1123x280&amp;nras=3&amp;correlator=8228143292682&amp;frm=20&amp;pv=1&amp;u_tz=480&amp;u_his=1&amp;u_h=1080&amp;u_w=1920&amp;u_ah=1032&amp;u_aw=1920&amp;u_cd=32&amp;u_sd=1&amp;dmc=16&amp;adx=226&amp;ady=1823&amp;biw=1905&amp;bih=911&amp;scr_x=0&amp;scr_y=0&amp;eid=95390788&amp;oid=2&amp;pvsid=313147943442323&amp;tmod=2076972085&amp;uas=0&amp;nvt=1&amp;ref=https%3A%2F%2Fwww.google.com%2F&amp;fc=1408&amp;brdim=0%2C0%2C0%2C0%2C1920%2C0%2C0%2C0%2C1920%2C911&amp;vis=1&amp;rsz=%7C%7Cs%7C&amp;abl=NS&amp;fu=128&amp;bc=31&amp;bz=0&amp;ifi=3&amp;uci=a!3&amp;btvi=2&amp;fsb=1&amp;dtd=4992" title="Advertisement" aria-label="Advertisement"></iframe>

Ollama 啟動後，預設本地 API 位址通常是：

```text
http://127.0.0.1:11434/v1
```

在 CC Switch 中選擇 OpenAI 相容的供應商類型，常見選項是：

```text
OpenAI Chat Completions
```

然後把 base URL 指向 Ollama 的本地位址。

API key 欄位對本地 Ollama 來說通常不需要真實金鑰，但很多工具仍會要求環境變數或佔位值。可以使用：

```text
ANTHROPIC_API_KEY
```

或其他本地配置可接受的佔位變數。

<iframe width="1123" height="280" frameborder="0" allow="attribution-reporting; run-ad-auction" src="https://googleads.g.doubleclick.net/pagead/ads?client=ca-pub-9230324840884748&amp;output=html&amp;h=280&amp;num_ads=1&amp;adk=2652405725&amp;adf=4104435823&amp;w=1123&amp;fwrn=4&amp;fwrnh=100&amp;lmt=1779035741&amp;rafmt=1&amp;armr=3&amp;sem=mc&amp;pwprc=7012339427&amp;ad_type=text_image&amp;format=1123x280&amp;url=https%3A%2F%2Fwww.knightli.com%2Fzh-tw%2F2026%2F05%2F15%2Fclaude-code-ollama-cc-switch-local-agent%2F&amp;fwr=0&amp;pra=3&amp;rh=200&amp;rw=1122&amp;rpe=1&amp;resp_fmts=3&amp;asro=0&amp;aiactd=0&amp;aicctd=0&amp;ailctd=0&amp;aimartd=4&amp;aieuf=1&amp;aicrs=1&amp;fa=27&amp;uach=WyJXaW5kb3dzIiwiMTkuMC4wIiwieDg2IiwiIiwiMTQ4LjAuNzc3OC4xNjgiLG51bGwsMCxudWxsLCI2NCIsW1siQ2hyb21pdW0iLCIxNDguMC43Nzc4LjE2OCJdLFsiR29vZ2xlIENocm9tZSIsIjE0OC4wLjc3NzguMTY4Il0sWyJOb3QvQSlCcmFuZCIsIjk5LjAuMC4wIl1dLDBd&amp;abgtt=6&amp;dt=1779069530497&amp;bpp=1&amp;bdt=2018&amp;idt=1&amp;shv=r20260512&amp;mjsv=m202605120101&amp;ptt=9&amp;saldr=aa&amp;abxe=1&amp;cookie_enabled=1&amp;eoidce=1&amp;prev_fmts=0x0%2C1123x280%2C1123x280&amp;nras=4&amp;correlator=8228143292682&amp;frm=20&amp;pv=1&amp;u_tz=480&amp;u_his=1&amp;u_h=1080&amp;u_w=1920&amp;u_ah=1032&amp;u_aw=1920&amp;u_cd=32&amp;u_sd=1&amp;dmc=16&amp;adx=226&amp;ady=2740&amp;biw=1905&amp;bih=911&amp;scr_x=0&amp;scr_y=0&amp;eid=95390788&amp;oid=2&amp;pvsid=313147943442323&amp;tmod=2076972085&amp;uas=0&amp;nvt=1&amp;ref=https%3A%2F%2Fwww.google.com%2F&amp;fc=1408&amp;brdim=0%2C0%2C0%2C0%2C1920%2C0%2C0%2C0%2C1920%2C911&amp;vis=1&amp;rsz=%7C%7Cs%7C&amp;abl=NS&amp;fu=128&amp;bc=31&amp;bz=0&amp;ifi=4&amp;uci=a!4&amp;btvi=3&amp;fsb=1&amp;dtd=4985" title="Advertisement" aria-label="Advertisement"></iframe>

有一個配置項需要特別注意：

```text
"inferenceModels"="[\"haiku\",\"sonnet\",\"opus\"]"
```

它表示把 Claude Code 預期的模型角色映射到本地供應商。實際使用時，需要把 `haiku` 、 `sonnet` 、 `opus` 對應到 Ollama 或 CC Switch 中可用的模型名稱。映射錯了，Claude Code 可能無法呼叫模型，或者一直回落到非預期配置。

## Claude Code 強在哪裡

Claude Code 最有價值的地方不是單次補全，而是整套編程工作流：

- 讀取並理解專案結構；
- 根據任務定位相關檔案；
- 直接修改程式碼；
- 執行命令與測試；
- 觀察錯誤後繼續迭代；
- 在一個會話中完成多步任務。

這也是很多人想把 Claude Code 保留下來的原因。普通聊天介面可以生成程式碼片段，但不會自然地在倉庫裡操作。Claude Code 更像是一個能執行任務的開發助手。

## Ollama 在這裡扮演什麼角色

Ollama 負責本地模型的執行與管理。它處理模型下載、載入和本地推理。

它的優點很明確：請求留在本機，反覆使用不會產生 API 帳單，在網路受限時也能使用。對私有程式碼來說，這也比把每一輪上下文都送到雲端模型更容易接受。

代價同樣明確。本地模型高度依賴硬體和模型品質。較小模型能處理簡單修改、解釋、腳本生成，但遇到大型跨檔案重構或細節很多的架構判斷時，能力會明顯下降。

## 體驗邊界在哪裡

這套方案不適合被理解成對 Claude 雲端強模型的完整替代。

你可能遇到這些問題：

- 長上下文理解能力較弱；
- 複雜任務中的工具呼叫不穩定；
- 純 CPU 機器推理速度較慢；
- 更容易幻覺出不存在的檔案路徑或 API；
- 多輪規劃可靠性不足；
- 大型專案重構成功率較低。

所以更合理的期待是：把它當成免費本地開發助手，而不是頂級雲端模型的完美替身。

## 多模態相容性還不穩定

有些使用者希望 Claude Code 處理截圖、UI 圖片、流程圖或其他多模態輸入。這一部分取決於本地模型和轉發層的支援情況。

如果選用的 Ollama 模型不支援視覺，或者 CC Switch 沒有正確轉換請求格式，多模態功能就可能失效。即使用了視覺模型，行為也可能和 Claude 官方 API 不完全一致。

因此目前更建議把這套方案用在文字與程式碼工作流上，多模態能力暫時按實驗功能看待。

## 適合誰嘗試

這套方案適合：

- 想低成本體驗 Claude Code 工作流的開發者；
- 經常寫腳本、小工具、自動化流程的使用者；
- 希望程式碼盡量留在本機的團隊；
- 想學習 AI 編程助手但不想持續消耗 API 的新手；
- 正在測試不同本地程式碼模型的人。

如果你高度依賴長上下文、大型 monorepo、嚴格程式碼審查品質，或複雜全專案重構，它可能還不夠穩。

## 使用建議

建議先從小任務開始。

例如：

- 解釋單個檔案；
- 重構一個小函式；
- 生成一段 shell 腳本；
- 修復一個簡單錯誤；
- 增加一個小功能；
- 為局部模組補單元測試。

每次修改後，最好自己跑測試，或至少檢查 diff。本地模型可以提高效率，但不應該盲目接受所有修改。

如果模型經常丟失上下文，就縮小任務範圍。不要讓它「重構整個專案」，而是改成「重構這個函式」或「為這個檔案增加校驗」。

## 小結

`Claude Code + CC Switch + Ollama` 是一個很有意思的組合。它把 Claude Code 的 Agent 式開發體驗保留下來，同時把模型推理搬到本地。

它最大的優勢是成本低、資料更私有、工作流順手；限制也很明顯，模型品質、硬體性能、長上下文和工具呼叫穩定性都會影響最終體驗。

如果你已經在用 Ollama，又想要一套更接近實戰的本地 AI 編程流程，這個方案值得試試。只是要記住：先從小任務開始，每次改動都要驗證，把本地模型當助手，而不是自動工程師。