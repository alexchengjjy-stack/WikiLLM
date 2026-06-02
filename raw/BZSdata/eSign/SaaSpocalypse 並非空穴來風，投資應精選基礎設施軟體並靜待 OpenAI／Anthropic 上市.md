---
title: "SaaSpocalypse 並非空穴來風，投資應精選基礎設施軟體並靜待 OpenAI／Anthropic 上市"
source: "https://vocus.cc/article/6a1aa5a4fd8978000109551e?shem=rimspwouoe,"
author:
  - "[[上游洞見]]"
published: 2026-05-30
created: 2026-06-02
description: "OpenAI 與 Anthropic 合計體量已超越 Salesforce，AI 新創一年內 ARR 衝破 US$70 億。市場喊出的「SaaSpocalypse」是真危機還是過度恐慌？本文拆解 GenAI 如何瓦解 SaaS 三大護城河與單位經濟，並指出投資人該往哪找相對安全的角落。"
tags:
  - "clippings"
---
## 一、結論

****1\. 應用軟體首當其衝，基礎設施軟體相對安全**** ：GenAI 同步瓦解 SaaS 三大護城河（轉換成本、合規壁壘、使用習慣），AI 新創於 AI 軟體市佔從 36% 躍升至 63%，加上企業 Vibe Coding 自建趨勢增強，應用軟體（CRM、ERP、BI）受衝擊遠大於基礎設施軟體（資安、可觀測性、資料庫）。Bloomberg 預估傳統 SaaS 模式將在 2025-2035 僅以 CAGR 2% 成長。

為什麼會看到廣告

****2\. 單位經濟結構性惡化，商業模式面臨重塑**** ：Token 推論成本打破 SaaS 邊際成本趨近於零的假設，定價從 seat-based 轉向 UBP／Outcome-based，毛利率從 70-80% 承壓，LTV/CAC 中 GM 下降、Churn 上升、NNARR 放緩三者同步惡化。

****3\. 基礎設施軟體相對受惠，靜待 AI 龍頭 IPO**** ：企業軟體估值已從 ~6x 跌至 ~3.5x fwd EV/Sales，再大幅崩跌機率不大，但反轉需營收加速為證據。CSP、資安與受惠上雲的 Infra 軟體，基本面相對具支撐，並留意 OpenAI／Anthropic 於 4Q26-1H27 IPO 後引發的資金重配與 L/S 壓力。

****4\. 我們的 non-consensus／前瞻觀點包含**** ：1) Vertical SaaS 因 LLM 在訓練環節引入專家參與因此護城河更加弱化，反之 Vertical AI Startup 更具潛力；2) OpenAI／Anthropic 在 IPO 前將盡可能擴增 TAM 拉升 IPO 後估值，未來 12 個月對 SaaS 壓力只增不減；3) SaaS 敘事轉為 SoR = 單純資料庫性質將降低估值，惟向第三方工具收取 API 調用費為潛在變現路徑。

![zoomable](https://images.vocus.cc/456df483-2dd7-4ae2-a7cf-f7669a1cf4e2.png)

高盛數據顯示美國投資人對軟體股曝險正大幅下滑

---

## 二、產業簡介

本篇將更加著重討論企業軟體（Enterprise Software）族群，而非消費者軟體／網路族群，係因除遊戲（U、APP）與特定業者（DUOL…）外，多數次產業皆面臨總體經濟在內，比 AI 擔憂更值得憂慮的基本面因素，如：Fintech——支付／BNPL 業者商品化、加密貨幣市況差；電商——進入投資週期 & 新興市場競爭激烈；叫車／外送——進入投資週期／Robotaxi 擔憂；數位廣告——非 GOOGL、META 業者面臨產業結構性轉變。

### 企業軟體主要分為應用軟體與基礎設施軟體

企業軟體為面向企業組織而開發之軟體，協助企業的營運、決策過程、管理與協作等過程。企業軟體大致可分為：1) 應用軟體（Application Software）；2) 基礎設施軟體（Infrastructure Software）。

****應用軟體****

![vocus｜新世代的創作平台](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2F43918eb7-133f-4ac5-8b04-719434d84ee4.png&width=740&sign=RIooUuzKjzM7C3Np8MQm5a-d_gMLt5T5nSOKNM90PHo) ![zoomable](https://images.vocus.cc/43918eb7-133f-4ac5-8b04-719434d84ee4.png)

****基礎設施軟體****

![vocus｜新世代的創作平台](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2F1796166c-606f-4c68-a1e1-ee8ab2e78f84.png&width=740&sign=JXvPDr6LwHQ5yj1Ad0XeHtaBybR_ekwIGsa07dOtwJM) ![zoomable](https://images.vocus.cc/1796166c-606f-4c68-a1e1-ee8ab2e78f84.png)

### 商業模式：由授權制轉向訂閱／按使用量計費

企業軟體產業過去主要採取一次性授權（perpetual license）模式，客戶在前期支付高額費用取得軟體使用權，後續僅需支付維護與升級費用。這種模式的特點在於收入高度前置且具備明顯的週期性，軟體廠商的成長往往依賴新客戶導入或大型升級專案，收入波動較大。

隨著雲端化的普及，產業逐步轉向以訂閱制（subscription）為核心的 SaaS 模型，收入結構從一次性收款轉為持續性的 recurring revenue。這一轉變大幅提升了收入的可預測性與穩定性，使得企業軟體公司能夠建立長期客戶關係，並透過續約、升級與交叉銷售（upsell／cross-sell）持續擴大客戶價值（LTV）。

進一步地，隨著雲端基礎設施與資料處理能力的成熟，部分軟體開始從單純訂閱制演進至按使用量計費（usage-based pricing）。在這種模式下，收入與實際使用程度（例如 API 呼叫次數、資料處理量或運算量）直接掛鉤，使得軟體支出更貼近客戶所獲得的價值，也提高了擴張收入的彈性。然而，這同時也意味著收入波動性上升，並將部分風險從客戶轉移至供應商。

下圖以圖表解釋訂閱制對比授權模式的現金流變化，可以發現 SaaS 提供業者更穩定、可預測的現金流。因此雖然 SaaS 業者初期呈現負現金流，若能維持高客戶留存率，假以時日便能轉虧為盈。值得注意的是倘若每期獲取的新客戶越多，初期虧損會越大，但過了損益兩平點後後續的現金流爆發會更加驚人。

![vocus｜新世代的創作平台](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2F6ab67a1b-3faa-4524-89d9-c9edea2d4361.png&width=740&sign=Xp5oxkGNNsRcjZ19N5u5Cf73N2ltkWW4IRfcJqZCMew) ![zoomable](https://images.vocus.cc/6ab67a1b-3faa-4524-89d9-c9edea2d4361.png)

### 成長軌跡：Rule of 40

在軟體產業中，特別是 SaaS 模式下，Rule of 40（營收成長率 + 營業利潤率 ≈ 40%）之所以被廣泛採用，核心在於其能同時衡量「成長性」與「獲利能力」之間的平衡。由於 SaaS 公司通常採取前期高投入（特別是銷售與研發）以換取長期訂閱收入的模式，短期內利潤往往被刻意壓低，使得單純以盈餘或現金流評價公司，容易低估其長期價值；反之，若僅關注營收成長，又可能忽略資本效率與商業模式可持續性。Rule of 40 提供了一個簡化但有效的框架，將成長與獲利放在同一座標系下，使投資人能判斷企業是否在「燒錢換成長」與「效率經營」之間取得合理平衡。

更重要的是，Rule of 40 隱含了 SaaS 商業模式的核心假設：隨著規模擴大，固定成本（特別是研發）被攤提，且高毛利結構應帶來顯著的營運槓桿，使企業最終能從高成長自然過渡到高利潤。如果一家公司在高成長階段仍能維持接近或超過 40% 的綜合指標，代表其單位經濟（如 LTV/CAC）健康，成長具備可持續性；反之，若長期低於該門檻，則可能意味著獲客成本過高、留存不足或定價能力有限。也因此，在過去十年資金充裕、成長導向的環境下，Rule of 40 成為市場快速篩選優質 SaaS 公司的重要工具，並直接影響其估值溢價。

### 估值方法：EV/Sales → EV/FCF → P/E

軟體產業估值從 EV/Sales、EV/FCF 到 P/E 的演化，本質上反映的是企業價值來源隨成熟度提升而逐步轉變的過程。在發展初期，SaaS 公司通常處於高成長、低甚至負利潤的階段，由於大量投入銷售與研發以換取未來市場份額，其短期盈餘與現金流無法真實反映長期價值，因此市場傾向以營收作為未來現金流的代理變數，採用 EV/Sales 進行估值。隨著公司進入中期，成長開始放緩且營運模式逐漸成熟，企業開始產生穩定的自由現金流，此時投資人關注的重點轉向資本效率與現金流轉換能力，估值方法也隨之轉為 EV/FCF。最終，當公司進入成熟階段，成長趨於穩定、利潤結構清晰且可預測時，盈餘成為最能代表企業長期價值的指標，市場便以 P/E 作為主要估值基準。整體而言，這一演化並非估值方法的任意切換，而是隨著企業可觀測的現金流與獲利能力逐步清晰，投資人從依賴成長代理變數，轉向直接評估實際獲利能力的自然結果。

### 平台化業者可享有估值溢價

在軟體產業中，平台化業者之所以能長期獲得估值溢價，本質來自其更強的「複利型經濟模型」。首先，平台通常具備任務關鍵屬性，直接對應企業核心流程，因此展現出極高的留存（GDR 95–97%）與大額合約（ACV $100K+），確保收入基礎穩定。其次，平台具備模組化擴展能力，隨著客戶採用更多產品（4–6+ modules），帶動淨收入留存（NRR）長期維持在 120% 以上，形成內生型成長，而非單純依賴新客獲取。

更重要的是，平台能持續擴張 TAM。透過推出非核心產品（如 ServiceNow、Veeva 案例），平台可以在既有客戶基礎上疊加新營收來源，帶來額外成長曲線，顯著優於單點產品公司。這種「land and expand」策略，使得平台在規模化後仍能維持成長動能。

從財務角度來看，平台公司在跨越 US$1bn 營收門檻後，仍能同時維持較高成長與更強現金流轉換，顯示其單位經濟隨規模持續優化。最終，這些特性共同轉化為更高的估值倍數與更好的股價表現。

因此在選股上更應著重於選擇具備平台化能力的公司。

![平台化業者估值與股價表現優於非平台化業者。資料來源：a16z](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2F28fd07ae-7b79-40ce-ac15-5085f68d49ac.png&width=740&sign=M8KfBnMu3d0g4LLIZKEaSKEujkhUSxNIYF6HfeknL_0) ![zoomable](https://images.vocus.cc/28fd07ae-7b79-40ce-ac15-5085f68d49ac.png)

平台化業者估值與股價表現優於非平台化業者。資料來源：a16z

![新產品線能使原產品線放緩下獲得新成長曲線。資料來源：a16z](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2Ff68b0f70-b16a-435d-b8d5-e54a0173ad5e.png&width=740&sign=qGDBbtSGtEmXh0Gy2B97aATilMbfReXZN6xIrTsFKGc) ![zoomable](https://images.vocus.cc/f68b0f70-b16a-435d-b8d5-e54a0173ad5e.png)

新產品線能使原產品線放緩下獲得新成長曲線。資料來源：a16z

![平台化業者擁有較高 GRR 與 ACV。資料來源：a16z](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2F4705bfc4-4269-4b4e-85a4-20ef22df9656.png&width=740&sign=yn03S6__spxNdA_IiZr_IqjIqpyIOZ4QpLfeKVllQ7M) ![zoomable](https://images.vocus.cc/4705bfc4-4269-4b4e-85a4-20ef22df9656.png)

平台化業者擁有較高 GRR 與 ACV。資料來源：a16z

---

## 三、需求端

了解產業基本架構後，以下將從需求與供給兩端分別釐清企業軟體既有的供需狀況與檢視 SaaSpocalypse 的驅動因素。

### 1\. IT 支出仍未顯著釋放，企業裁員／供應商整併壓縮軟體業者獲利空間

如果說半導體產業以 CSP CAPEX 作為風向球，在軟體產業中類似指標便是企業 IT 支出，IT 支出通常涵括硬體、軟體採購與 IT 服務等。若要觀察企業 IT 支出動態以作為 Top-Down 的依歸，可參考第三方研調機構（Gartner、IDC、ETR 等）或外資券商（Morgan Stanley、JP Morgan、UBS 等）。

其中 Morgan Stanley 每季釋出之 CIO Survey 是更新頻率穩定且涵蓋面較廣的資料來源，調查涵括不同產業間客戶的 IT 支出動態（科技、零售、金融服務、製造業…）、不同面向的 IT 支出成長性（硬體、軟體、通訊設備、IT 服務）、成長性最高的支出專案（AI/ML、資安、雲端轉型…）。而在諸多問券調查中，我們認為最具參考性的為 Up-to-Down Ratio 指標（算法為「未來將增加 IT 支出的 CIO 比例／未來將減少 IT 支出的 CIO 比例」），根據 MS 近期的調查，Up-to-Down Ratio 在 4Q24 後仍未見起色，可得知至少現階段在企業採購上，IT 支出仍非處於大幅擴張的階段。

![資料來源：AlphaWise](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2F511e608b-e221-4761-84e0-8b78d4574e57.png&width=740&sign=TKiXux7ggnLOzAITPyWJ6MrxAQk5SYTNDysRyv0ivCI) ![zoomable](https://images.vocus.cc/511e608b-e221-4761-84e0-8b78d4574e57.png)

資料來源：AlphaWise

而回顧 2008 年至今的企業 IT 支出年增率，亦可發現自 3Q20-1Q22 較明顯的 IT 支出上升週期後，整體企業 IT 支出仍尚未看到明顯的上升拐點。而對比 CSP CAPEX 的逐年成長，似乎也解釋過去 12 個月軟體與半導體 & 電子下游間的營收與股價走勢分化的背後原因。

![vocus｜新世代的創作平台](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2F57ef313c-2448-4382-97ae-e9e0ad7efb6d.png&width=740&sign=WYMC_5PcK2TAK2f7UEBTL46uYiMirXtMLoA7Uqb4KsU) ![zoomable](https://images.vocus.cc/57ef313c-2448-4382-97ae-e9e0ad7efb6d.png)

誠然在過去 1 年營收與股價走勢處在上升週期的企業軟體業者不在少數，較知名的案例包含 Palantir、Cloudflare、CrowdStrike、Snowflake 與 MongoDB。然而在 IT 支出較為緊縮的大環境之下，若企業需要新增用於 AI/ML 的 IT 支出，勢必將排擠到原先花費在既有軟體的支出，進一步使既有軟體業者在續約談判、向上銷售等過程中遇到降價壓力。

而根據 ETR 的調查，供應商整併與裁員為企業在縮減 IT 支出的主要手段，因此提供單點產品的供應商（best-of-breed）在此框架下面臨 P/Q 雙降的壓力，而平台化業者透過綑綁銷售諸多產品線並給予客戶一定的初期折扣較可能搶奪單點供應商市佔。

![供應商整併為 IT 預算縮減主要節約手段之一。資料來源：ETR、凱基證券](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2F93d65081-21b5-4ae9-bfc2-babb026df887.png&width=740&sign=NTLw1453-3NDe5PZeix40XxgiTEIsav0ed2UKKwUimQ) ![zoomable](https://images.vocus.cc/93d65081-21b5-4ae9-bfc2-babb026df887.png)

供應商整併為 IT 預算縮減主要節約手段之一。資料來源：ETR、凱基證券

![AI 時代技能需求與雲端時代不同。資料來源：COATUE](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2F774070fe-0030-4192-b318-a946a83fb8f8.png&width=740&sign=NZoizk2ZDHVUgcGPgf9jSsOK4M6kRRAMWq6SIVWms-Q) ![zoomable](https://images.vocus.cc/774070fe-0030-4192-b318-a946a83fb8f8.png)

AI 時代技能需求與雲端時代不同。資料來源：COATUE

![trueup.io 預計科技大廠 2026 年裁員幅度將進一步擴大。資料來源：trueup.io](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2F877faeaa-a5ed-4041-887e-089015422640.png&width=740&sign=WpuN3sJdHs2_W5nx6qXuQcU7lgXDSZ6-ZH6SP2loChY) ![zoomable](https://images.vocus.cc/877faeaa-a5ed-4041-887e-089015422640.png)

trueup.io 預計科技大廠 2026 年裁員幅度將進一步擴大。資料來源：trueup.io

![Gartner 預計 AI 增加的工作將在 2030 後方才大於 AI 減少的工作數。資料來源：Gartner](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2Fa22a871f-b5af-4857-b483-d73cf7bf38e1.png&width=740&sign=p3VU_eLgAb5Wjr-EcxnDnuJHcxBbs0Iieza04Jd2qzY) ![zoomable](https://images.vocus.cc/a22a871f-b5af-4857-b483-d73cf7bf38e1.png)

Gartner 預計 AI 增加的工作將在 2030 後方才大於 AI 減少的工作數。資料來源：Gartner

### 2\. 企業上雲與數據整合成為關注焦點

過去一年，企業上雲的核心動機已從「成本與彈性」轉向「AI 能力部署」。隨著 GenAI 與 agent-based 應用快速落地，企業對於高效能運算資源、即時資料存取與彈性擴展能力的需求顯著提升，而這些能力對多數企業來說在本地基礎設施上難以有效實現。意味著上雲不再只是 IT 策略，而是 AI 策略的前提條件。企業若要部署 LLM、即時推薦系統或自動化 agent，幾乎不可避免地需要依賴 CSP 所提供的算力與資料服務。

各 CSP 均提及客戶加速上雲的趨勢

![vocus｜新世代的創作平台](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2F8a65cf1e-f3b8-4395-8632-0746a3b852a9.png&width=740&sign=7BN-JPTghcYiA-wUE09CS0-DWsUMEYQTbbLMa0rdFJo) ![zoomable](https://images.vocus.cc/8a65cf1e-f3b8-4395-8632-0746a3b852a9.png)

AI 的另一個關鍵影響，在於徹底改變企業對資料的使用方式。過去資料主要用於報表與分析，但在 AI 時代，資料必須能夠被即時調用、即時推理（real-time inference），甚至直接參與決策流程。這使得企業不得不將資料從分散的系統中抽離，並集中到可支援 AI 的雲端資料平台。

AI 的有效運作高度依賴資料完整性與一致性，這使得企業原本分散於 CRM、ERP、行銷系統與數據倉庫的資料架構，開始出現整合壓力。企業若無法建立統一的資料視圖（single source of truth），AI 模型的輸出將受到嚴重限制，甚至導致錯誤決策。

這一趨勢已直接反映在產業動態上。例如企業軟體公司正大幅強化資料整合能力，甚至透過併購來補強（如 IBM 收購 Confluent、Salesforce 收購 Informatica），目的在於打通分散資料源以支援 AI Agent 與自動化流程。同時，資料整合技術本身也逐步轉向支援混合雲與多雲環境，涵蓋資料移動、清洗與轉換等完整流程。因此，資料整合不再是 IT efficiency 的問題，而是 AI 能否落地的關鍵瓶頸。

而上述趨勢已在 CSP 業者的財報中，以及可觀測性的 Datadog、數據庫的 Snowflake 中反應，使這些業者成為少數軟體產業中於過去一年表現相對亮眼者。

![DDOG、Azure、GCP、AWS、SNOW 營收年增率呈現加速成長](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2F17f53bf4-04d1-4f59-9b8d-e5f7d5c3be89.png&width=740&sign=1XqCUc9PyZB03LNUko7KRy3YhwNBa4ZaP_f-L8_nmDI) ![zoomable](https://images.vocus.cc/17f53bf4-04d1-4f59-9b8d-e5f7d5c3be89.png)

DDOG、Azure、GCP、AWS、SNOW 營收年增率呈現加速成長

### 3\. 小結：慎選平台化業者與受惠企業上雲需求之基礎設施業者

企業正透過裁員、供應商整併等方式縮減 IT 預算，因此投資須慎選能受惠上雲、資料整合需求的基礎設施軟體業者。

---

## 四、供給端

### 1\. 在 AI 時代前，軟體產業早已競爭加劇

誠如前述，疫情後企業 IT 支出仍未見顯著擴張，各 SaaS 業者因而將成長寄託於平台化擴張／水平整合，希望成長出新的 S-Curve。較為知名的水平擴張案例包含：ServiceNow 擴張至 CRM 與 Salesforce 競爭、Atlassian 的 Jira Service Management 開始侵蝕部分 ServiceNow 客戶、CrowdStrike 在端點資安外開展出雲端資安、SIEM、身份資安等多條產品線……

除此之外，原先的各次產業裡的競爭也十分激烈，如：Salesforce 的四大產品線 Sales／Marketing／Commerce／Service 分別面臨 Hubspot／Adobe／Shopify／ServiceNow 競爭、Adobe Digital Media 業務面臨 Canva 競爭、在資料庫產業 Snowflake vs. Databricks／PostgresSQL vs. MongoDB、在 SIEM 領域 CRWD 與 PANW 透過差異化定價與效能優勢搶佔 Splunk、IBM 的市佔。

綜上，在討論 AI 顛覆論前更應先關注既有的競爭情境，若公司在 AI 競爭者湧現前便在流失市佔，殊難想像在 AI 出現後會有任何基本面上的反轉。一個簡單判斷公司是否在獲取市佔的方法，根據 Gartner 預估，應用軟體 2025-29F CAGR 約為 14%、基礎設施軟體約為 13%，若一間公司的成長率低於此數字則大概率在流失市佔。

### 2\. AI 瓦解 SaaS 護城河後，產業競爭愈發白熱化

我們看到過去 12 個月內，企業軟體業者的護城河正在崩塌，使產業競爭加劇，簡單整理幾個企業軟體護城河如下：

****轉換成本：****

- What's 轉換成本：在轉換軟體時需付出高昂技術成本，包含系統重建、資料遷移、API 重寫，同時需經歷員工重新訓練、流程重設等過程，亦可能需承擔系統停機時間與營運中斷風險。
- 案例：台灣南山人壽境界成就計畫事件意圖合併公司內現有的資料庫與數百種程式，然卻因系統資料轉移出錯，不僅投資額從最初 37 億元提升至百億等級、轉型期間高達 15.2 萬件保單出錯、時任董事長遭解職、暫時失去販售主力獲利產品投資型保單的資格。

****企業合規：****

- What's 企業合規？企業軟體依照不同的國家／產業會有不同的法規標準需要依循，包含 SOC2、HIPAA、PCI 等。不過單純的符合法規要求並非難事，更重要的是讓客戶「信任」後方才願意採購。
- 案例：在企業中最具合規與信任要求的資安領域，Wiz 憑藉 Agentless、Security Graph 與簡易的介面，在 18 個月達到 ARR US$100mn，最後被 Google 以 US$32bn 收購。顯示只要成功找到市場痛點、設計出優秀的產品一樣能在企業軟體市場快速成長。

****使用者習慣／產業標準：****

- What's 使用者習慣／產業標準？如 Adobe、Microsoft 365 等軟體因為其通用性，養成個人使用習慣、組織流程依賴，最後成為產業標準，並延伸公式／格式（doc、xlsx、PDF…）等生態系。

我們認為 AI 時代，所有 SaaS 業者的上述護城河將同步減弱，原因與案例整理如下：

![vocus｜新世代的創作平台](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2F3596a388-f842-4366-807c-04ed4bb83391.png&width=740&sign=mImp5EQl3pjiAhGnP_x6-VZxLuwM2HXPfOJXeWQzDzQ) ![zoomable](https://images.vocus.cc/3596a388-f842-4366-807c-04ed4bb83391.png)

我們想先澄清的是，轉換成本在 AI 時代可能是被高估的企業軟體護城河，係因現有的 AI 工具大多為在既有的 SaaS 之上建立各種應用，本質上並沒有「轉換」的過程。例如：Fintech 公司透過 Sierra 的 AI Agent 串接客戶帳戶、交易紀錄、卡片交付等 CRM 資料，使客戶獲得答案的速度提高 90%，每年節省超過 15,000 個小時。

> Six months later and Brex's Sierra-powered customer agent can handle everything from basic support questions to looking up account data, tracking card deliveries and retrieving transaction details. Customers now get their answers 90% faster, saving them over 15,000 hours per year. And if a customer needs to chat with a live agent, the seamless integration with Brex's contact center ensures they are reliably routed to the right person, with the correct context. — "How Brex made customer service 90% faster with AI."

當 AI Agent 已經能替分析師架設財務模型、自動生成圖片 & 影片之時，軟體公司圍繞在 GUI 之上累積的用戶學習成本、使用習慣等護城河便被大幅削弱，取而代之的是 Headless 架構的概念，意即透過 API 進行 Machine-to-Machine（M2M）的溝通。因此過往用戶大量手動操作的工具或仰賴 UI 作為價值主張的軟體價值將大幅削弱，例如：BI 工具（Power BI、Tableau）、Adobe、RPA 工具……

市場原先預期企業軟體公司可無縫在產品中融入 AI 後搭上浪潮使營收隨 AI 使用量同步成長，然實質上過去 12 個月營收貢獻有限。雖然 AI 有很多變現路徑，也在很多層面上使軟體公司受惠，包含：AI-Native 公司 workload 成長（DDOG）、導入 AI 前的數據遷移（SNOW、PLTR），用 AI 吸引客戶升級亦是一種商業策略，不過從 OpenAI 與 Anthropic 的 ARR 指數級成長來看，客戶是願意為了 AI 付錢的，疊加 SaaS 族群的悲觀情緒，因此有必要拿出顯微鏡檢視「AI 產品」本身的營收貢獻，事實上，在我們的逾 45 間的企業軟體觀察清單中公布該數字的僅有 Salesforce、ServiceNow、Adobe、Workday，而 Microsoft 有公布 M365 Copilot 付費席位數。相關數據整理如下：

![vocus｜新世代的創作平台](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2F97990a59-47cf-4e21-aeba-3e51d398b613.png&width=740&sign=L7MSCSRAKOCzceOKAbyM-uS5xpRrjwB-1O3zvP9YnMs) ![zoomable](https://images.vocus.cc/97990a59-47cf-4e21-aeba-3e51d398b613.png)

> 註：Salesforce ARR 計算排除 Informatica 貢獻、Microsoft 為 M365 Copilot 付費用戶數與 M365 商業版本付費用戶數、ServiceNow ACV／ARR 並不精準僅供參考

Takeaways：1) 可以合理假設除上述三間以外的企業軟體業者來自 AI 產品的直接營收貢獻恐皆小於 1%；2) MSFT 是客戶關係最強、渠道夥伴關係最緊密的軟體業者，在各式 CIO Survey 中也被視為 AI 最大受益者，M365 Copilot 於 9M23 GA、11M23 開始商業化，不過 C4Q25 公佈之 M365 Copilot 滲透率僅 3% 小於多數 sellside 預期之 High-Single Digit。

可以理解既有 SaaS 業者在導入 AI 之前需要基礎架構疏通、UBP 計價亦會較晚反應營收，然而當 OpenAI、Anthropic 兩者的 ARR 總和規模已超越 Salesforce 時，背後的含義應不僅限於單純的「營收滯後反應」，而是更深層的產業競爭結構與價值鏈轉移。

![OpenAI + Anthropic 體量已超越大型 SaaS 業者。資料來源：COATUE](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2Ff8bcb5fd-628d-4488-a5ce-c1b8978e1b16.png&width=740&sign=QPEV6YbpbqSrEr36ymPZnc4-EBV3ZuaEYypPxhLE0DQ) ![zoomable](https://images.vocus.cc/f8bcb5fd-628d-4488-a5ce-c1b8978e1b16.png)

OpenAI + Anthropic 體量已超越大型 SaaS 業者。資料來源：COATUE

在競爭環境上，可大致分為三種競爭群體：（a）既有業者間；（b）AI 模型／新創公司；（c）企業內部 Buy-or-Build 抉擇。

****（a）既有業者間：****

參照前段所述，軟體產業已進入競爭白熱化階段，在此期間，產品開發能力與迭代速度較快的 Product-Led-Growth 公司可利用 AI 加速產品推出速度，比大型軟體公司更快開發新產品。

正如 monday.com CEO Eran Zinman 在近期訪談所述，股價大幅下跌後反而更沒有後顧之憂的 all-in AI，並將原本競爭激烈的 CRM 與 Service 兩大垂直市場視為未來的巨大機會。他們正從頭打造 100% 以 Agent 為核心的新產品，因為這些老牌巨頭要改變龐大的組織架構與既有利益將極度困難，而 monday 具備靈活轉型的優勢。

****（b）AI 模型／新創公司：****

Claude Code／CoWork／Code Security、OpenAI Codex 等工具發布使 IGV（iShares Expanded Tech-Software Sector ETF，通常視作企業軟體族群的指標）跌幅達 25%（截至 4/x）。

來自 AI 勢力的競爭大致可分為：1) Coding Agent 能力邊界擴張，會稀釋 RPA 或傳統開發工具既有的價值，同時讓企業更容易開發工具產生（c）的狀況；2) 新創公司基於 AI 打造產品對現有 SaaS 業者產生競爭衝擊。

根據 Menlo Ventures 發布的「2025: The State of Generative AI in the Enterprise」，在 AI 市場中，除了營銷、客戶成功、資料科學與 IT 外，其餘領域的市佔率皆以新創公司佔多數。總體而言的市佔率，新創公司從 2024 年的 36% 大幅提升至 2025 年的 63%。

![AI Startup 市佔大幅攀升。資料來源：Menlo Ventures](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2F8e920a19-c331-4efd-8fa3-614d84a19981.png&width=740&sign=8DN8GG_gOAUnhprYRoNMsoVaeoDxsM934QIwDut8_BI) ![zoomable](https://images.vocus.cc/8e920a19-c331-4efd-8fa3-614d84a19981.png)

AI Startup 市佔大幅攀升。資料來源：Menlo Ventures

![在 Application 端皆以 AI 新創獲得較高市佔。資料來源：Menlo Ventures](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2Fce053f78-ac08-454a-99be-653a4a5d39d6.png&width=740&sign=wwstQVkkakBKiOz8MsZ2i-HdlcDcXgcaiRf9Bid-qp0) ![zoomable](https://images.vocus.cc/ce053f78-ac08-454a-99be-653a4a5d39d6.png)

在 Application 端皆以 AI 新創獲得較高市佔。資料來源：Menlo Ventures

Ramp 數據亦顯示成長最快的軟體業者皆非檯面上所熟知的 SaaS 公司。

![Ramp 數據顯示新創軟體業者成長迅速。資料來源：Ramp Rate](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2Fed49b628-c7a3-4576-be56-2f17a818b141.png&width=740&sign=pNInggNRuJnN5qKwtrw3LXlF1R_PUT6BcfAqwPmjcUA) ![zoomable](https://images.vocus.cc/ed49b628-c7a3-4576-be56-2f17a818b141.png)

Ramp 數據顯示新創軟體業者成長迅速。資料來源：Ramp Rate

我們觀察市場普遍對 LLM 業者的 Coding Agent 現狀有所了解，但忽略 AI 新創公司的競爭壓力。以 Salesforce 前 CEO 創辦的 Sierra 來說，該司之 AI Agent 產品應用於客服、訂單管理等應用，直接與 Salesforce Agentforce 競爭，目前 ARR 已達 US$150mn（Salesforce Agentforce ARR US$800mn，因 Salesforce Agentforce 應用案例包含 Slack 等，兩者實際差距應更小）。SoFi 在考量監管要求後採用 Sierra 產品，在部署三個月後，該 AI Agent 達到 61% 的問題攔截率，每週可處理超過 50,000 筆對話。同時，透過聊天完成的服務，其淨推薦值（NPS）提升 33 分。而市場普遍認為較具防禦性的 Finance & Operations 領域業者因監管包袱，在 AI 轉型緩慢使 Rillet（客戶數 >200，與全美前五十大事務所合作）、Campfire（客戶數 >100，多間客戶取代 Netsuite）、Numeric（客戶包含 Mercury、Replit、Plaid）等新創競爭浮現。

我們整理 ARR > US$100mn 的 AI 新創軟體公司如下：

![vocus｜新世代的創作平台](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2Fa0bfdea4-5a22-4ddc-b18b-09fdbd02e144.png&width=740&sign=dkhD8W8MRt1HbQnzwn4DWYmZYSnlkBrHUB5gZovQX_w) ![zoomable](https://images.vocus.cc/a0bfdea4-5a22-4ddc-b18b-09fdbd02e144.png)

如上表所示，這些 AI 新創（未計入 OpenAI、Anthropic 等模型業者）的 ARR 已逼近 US$7bn，已顯著與既有上市公司合計的 US$2bn 拉開差距。目前 AI 新創的著力方向主要集中在 Coding 工具與特定領域（客服中心、財會軟體……）中，Menlo Ventures 的資料亦顯示在 IT、資料科學等 AI 基礎建設領域仍由既有業者獲取較多價值，反應在 Snowflake、MongoDB、Datadog、Databricks 等業者近期的財報中。

另外，OpenAI／Anthropic 的野心更不僅限於模型層，包含 OpenAI 所推出的 OpenAI Frontier 以及 Frontier Alliances，便是透過將 AI 建立在 SoR 之上，連接分散的資料庫、CRM 系統、工單工具和內部應用程式，使 AI 與員工共用上下文脈絡、權限等。再將這樣的產品架構透過 OpenAI 本身的 FDE 和 OpenAI Frontier Alliances 合作夥伴（麥肯錫、BCG、Accenture、Capgemini）向企業分銷，複製傳統 SaaS 透過 IT Service 業者向企業銷售軟體的渠道，打破所謂「分銷管道」的護城河。

![OpenAI Frontier 建立於 SoR 之上攀取 AI 價值](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2F40c8908e-99f8-48bf-9c3a-78b28bfdcdc6.png&width=740&sign=9e_bkES_nPSd71NoWTVrvOD_6SwxuVSAwWQMOBhFPs4) ![zoomable](https://images.vocus.cc/40c8908e-99f8-48bf-9c3a-78b28bfdcdc6.png)

OpenAI Frontier 建立於 SoR 之上攀取 AI 價值

Anthropic 在近期推出的 Claude Managed Service 則是展現出類似作業系統（Operating System，OS）的特性，為未來未知應用建立平台。Claude Mythos 與 OpenAI GPT-5.4-Cyber 在公佈前先與關鍵基礎設施業者試用的特性近似於微軟發佈新作業系統前先讓端點資安業者試用，顯示 OpenAI／Anthropic 正積極擴展於基礎設施的佈局。

![Anthropic 推出 Claude Managed Service 建立類似作業系統概念](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2F0846d2ce-241d-4015-bc34-7539d281fa04.png&width=740&sign=6d_2ql1OmgEb62Y0BAwfqXpjn-RCy6EuB9GsBO37pAo) ![zoomable](https://images.vocus.cc/0846d2ce-241d-4015-bc34-7539d281fa04.png)

Anthropic 推出 Claude Managed Service 建立類似作業系統概念

同時我們認為部分 Vertical SaaS 的所謂「專業知識」的護城河被非常過度高估（除特定法規核可外），原因便在於自 2H25 起 LLM 在訓練環節便大量聘請各領域的專業人員（金融分析師、人類學家、記者、心理學家、工業工程師、電影製作人…）協助進行數據標注、回答評分、流程演示、提供標準答案等任務，因此對於一個專業人士的整個工作流程，我們認為 LLM 業者的掌控度不一定比 SaaS 業者差，甚至理應更好，因此對於市場普遍看好的「專業知識」護城河，我們持較保守的態度，而 Harvey（法律）、Legora（法律）、Heidi Health（醫療）、Abridge（醫療）、OpenEvidence（醫療）等新創公司的崛起、Anthropic Claude Excel 可建立 Financial Model 即是幾個代表性案例。反之，我們更看好 Vertical AI Startup 在 LLM 具備一定的專業能力下，挖掘更多產業客製化需求的潛力，甚至替代部分專業人員的未來。類似 Sequoia 於「 [Services: The New Software](https://sequoiacap.com/article/services-the-new-software/) 」所述之觀點。

最後，展望未來 12 個月，預計：1) Coding Agent 相對落後的 Google 也將於 5M26 的 Google I/O 2026 發佈相關產品；2) AI Agent 能力邊界擴張；3) 隨 OpenAI、Anthropic IPO 前夕（以及隨後的 AI 新創公司們）更多產品更新／財務資訊被揭露。我們認為市場對於 SaaS 之悲觀情緒在尚未見到基本面轉佳的跡象前較難修復。

****（c）企業內部 Buy-or-Build 抉擇：****

由於企業向外部採購軟體本質上便是希望降低成本與風險而做出的決策，AI Coding 大幅加速軟體開發過程與降低門檻極有可能造成企業購買軟體的誘因降低。在 Claude Code 盛行之前，BNPL 公司 Klarna 就已透過 Cursor、Neo4j 等基礎建設取代 Salesforce、Workday 等 SaaS 系統。

而根據華爾街日報近期對企業 CIO 們的訪查，企業內部正透過「自建部分程式降低 upgrade 費用」、「重新檢視軟體合約」等方式嘗試節省 IT 預算，案例包含：1) FedEx CIO 認為基於軟體與 AI 未來的不確定性，正在重新評估每個合作夥伴的軟體定價方式；2) Ernst & Young 全球成長和創新合夥人表示其不打算替代 SAP，但其正在透過 Vibe Coding 在 SAP 的基礎上建構自有的客製化程式並節省原先需從 SAP 購買升級套件的資金；3) Cisco 亦自建簡報軟體（presentation software）每年節省 US$5mn 費用，並希望透過 Vibe Coding 取代每年花費訂閱費用 US$50-200mn 的 SaaS。

Vibe Coding 風潮不僅限於大企業，SMB 亦透過自建軟體已取代部分 SaaS 軟體。AppGen 業者 Retool 調查 817 名客戶與開發者後，發現其中 35% 的受訪者已經用自建軟體取代至少一種 SaaS 工具，78% 的受訪者預計在 2026 年建立更多自己的工具，其中工作流程自動化、內部管理工具、BI/Dashboard、CRM 為替代比例最高的類別。netlify 的人才招募團隊（4 人）利用 Vibe Coding 建造招聘經理支援、招聘儀表板等功能每年節省 US$10k 成本。

企業完全自建 SaaS 系統並不合理，因為企業軟體在大多數情況下不作為公司間的差異化競爭因素，但是在 SaaS 之上開發自建功能是對未來的合理中性預期，SaaS 運作根基本就為以同套系統服務多個客戶，在此之下勢必犧牲深度客製化的可能，因而讓企業有動機去自建符合內部 workflow 需求的 SaaS 工具，即便不全然顛覆 SaaS，也會對 SaaS 業者在進行 upsell 上產生阻礙。

呈上述對於競爭環境加劇的論述，我們從高頻數據中似乎已經看到相對應的企業支出影響，YipitData 資料顯示在巨型 AI 支出者中，Adobe、Atlassian、Twilio、asana 等企業軟體支出已經轉負，更值得注意的是多數公司在年增率變化上已經轉負，除 Cloudflare、HubSpot、Snowflake 少數公司外。顯示 AI 帶來之成長效應對於既有 SaaS 業者確實有限。

![高頻數據顯示在 AI 支出者中，傳統 SaaS 業者成長正在放緩。資料來源：YipitData](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2Fee9d28bf-cba9-4285-848b-00408aeacacd.png&width=740&sign=kPPPK5wxYW4SDe7ketggT0cVOevrLbmpnkjvAzwoIqE) ![zoomable](https://images.vocus.cc/ee9d28bf-cba9-4285-848b-00408aeacacd.png)

高頻數據顯示在 AI 支出者中，傳統 SaaS 業者成長正在放緩。資料來源：YipitData

而早期 AI 導入者亦顯著減少於 PPM 軟體（asana、Atlassian、monday.com）的花費。

![YipitData 顯示 PPM 軟體支出正在放緩。資料來源：YipitData](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2F0e82b4da-ffcf-4430-bd3a-60d0fd63da67.png&width=740&sign=q0sMR9VQKKj2jamufQZC6yjPFiO7tJzXoGreGwWA4K0) ![zoomable](https://images.vocus.cc/0e82b4da-ffcf-4430-bd3a-60d0fd63da67.png)

YipitData 顯示 PPM 軟體支出正在放緩。資料來源：YipitData

上述三類競爭壓力已從高頻數據中獲得驗證（YipitData），我們認為接下來更關鍵的問題是：為什麼 SaaS 公司無法有效回應競爭？

****（1）大型 SaaS 業者習慣以 SLG 開展業務，產品迭代能力較慢 + 商業模式衝突****

SaaS 以 SLG 主導的成長模式使現今 SaaS 公司成長更依賴銷售人員的銷售能力而非全然的依靠產品能力進行成長。對比長期仰賴產品的 PLG 公司 Cloudflare、Snowflake、Datadog 等往往在新模型發布後即可支援，SLG 公司的產品發佈速度明顯在 AI 時代落後，我們認為這部分亦可能與 SLG 公司的商業模式多為 Seat-based 綁定，具創新者兩難有關（對企業主而言營收下滑風險，對銷售人員來說若 KPI 綁定於席次銷售則無動機）。

****（2）交付模式轉往 FDE****

AI 時代類似早期 mainframe 時期——多數工作流程尚未針對 AI 進行優化，企業若要導入 AI 需先經過諸多數據清洗、工作流程釐清與垂直整合，特別在 AI 諸多設定尚未標準化之際，面對異質的應用情境需要大幅客製化調整。

因此 FDE（Forward Deployed Engineer，前線部署工程師）的需求盛行。根據求職平台 Indeed 數據，FDE 的需求量暴增，光是 1M25-9M25 的職缺數就比去年同期成長超過 800%。

![FDE 職缺需求相較其餘工程師職缺快速成長。資料來源：Indeed、Financial Times](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2Fc6b4e99e-4b2b-4089-a866-17709ef8ed27.png&width=740&sign=b-A0RHkDzTOBgL5LBI7umuu03rPliwmKuwZ-hgRCU2k) ![zoomable](https://images.vocus.cc/c6b4e99e-4b2b-4089-a866-17709ef8ed27.png)

FDE 職缺需求相較其餘工程師職缺快速成長。資料來源：Indeed、Financial Times

在目前的上市公司中 Palantir 即為 FDE 模式的代表，在 AIP 推出後 PLTR 的 FDE 們借助 GenAI 技術可大幅縮短在客戶端客製軟體的時間，同時因為客戶對 GenAI 需求關注使 deal size 激增，讓 PLTR 在過去兩年成為極少數營收與 non-GAAP OPM 同步持續加速成長的軟體公司。

![PLTR 營收 YoY & OPM 均呈現加速成長](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2Fc2897705-d61c-44e2-bf58-151616cee592.png&width=728&sign=nQqI71dAKUgMOWdU0OUGw0GQn66t4rpJHka_JWu1kFQ) ![zoomable](https://images.vocus.cc/c2897705-d61c-44e2-bf58-151616cee592.png)

PLTR 營收 YoY & OPM 均呈現加速成長

OpenAI FDE 團隊經手過的案例包含：1) 歐洲半導體公司——客戶給了極大的自由度，要求 FDE 團隊檢視其整體價值鏈，找出最大的浪費並用 AI 解決。FDE 團隊花了數週時間深入了解晶片設計、驗證到效能測試的流程。最後團隊針對工程師花費 70-80% 時間進行的「晶片驗證」與「除錯」工作，發明名為「Debug Investigation and Triage Agent」的工具。模型會自動調查 Bug、撰寫報表，甚至嘗試修復代碼並發起 Pull Request，目前初步導入的部門已實現 20-30% 的效率提升；2) 亞太地區汽車製造業——供應鏈模擬與優化以應對複雜的全球供應鏈波動（例如：當中國到韓國的關稅增加 25% 時），結合 LLM 編排能力與公司內部的「確定性規則」，模型可以執行數百次模擬，根據成本、前置時間等變量找出最優解，並將原本分散在不同部門、需數天處理的數據整合為即時洞察；3) Morgan Stanley——將公司的研究報告庫提供給財富顧問，讓顧問能快速獲取洞察並提供給客戶，技術原型在 6-8 週內就已完成，但後續花了約 4 個月進行試點、標記數據與迭代，以建立足以投入生產的信任度，最後高達 98% 的顧問採用了該工具，且研究報告的使用率提升 3 倍。

我們認為這三個 case study 很好的解釋了 FDE 在 AI 時代的重要之處 & 為何 AI 導入企業的價值更可能被 AI 新創吃下而非傳統 SaaS 業者。

在案例一中，客戶僅給予效率提升的目標，但具體如何實現仍是模糊，在客戶的授權之下 OpenAI 得以重新從 Top-Down 角度重新檢視客戶的整個 workflow，而這正是多數僅負責單點運作的 SaaS 工具所無法切入之處。在案例二中，以合規的前提在既有 SaaS 數據之上建立分析系統，顯示雖 SaaS 不被取代但 AI 價值由 OpenAI 獲取。在案例三中則是新增需求，過往「研究報告庫提供給財富顧問並轉為精準洞察」這件事並沒有相對應的 SaaS 產品能提供服務無前例可參考，OpenAI 透過 Agent 能力邊界逐漸擴張能吃下更多潛在需求。

除了客製化、深入了解客戶需求外，FDE 模式更可以相較傳統 SaaS 交付模式更快發掘客戶需求打造 AI 平台。OpenAI 的 FDE 團隊在處理 Klarna 與 T-Mobile 等超大型客服系統時，發現傳統手寫 Prompt 來應付 400 條客服政策完全無法擴展。於是他們開發出能將指令與工具參數化、並包裹評估指標的框架，成功從 20 條政策擴展到 400 條。這個內部工具後來被開源，命名為 Swarm。由於市場反應極佳，最終推動 OpenAI 產品團隊釋出供廣大開發者使用的 Agent Kit。印證 FDE「從特定痛點中提煉出通用平台」的戰略價值。

然而，FDE 需兼具平台工程師、軟體工程師與解決方案建構者的角色使其為市場稀缺，即便是傳統上在協助企業做軟體導入的 SI／IT Service 業者（Accenture、Infosys、Cognizant）也需進行大規模員工 AI 培訓與汰舊換新來跟上浪潮。另外，OpenAI、Anthropic 等利用股票薪酬搶奪人才的吸引力亦為 SaaS 業者無法跟進之處。

****（3）不具模型開發能力影響 AI 產品性能****

而現今的 SaaS 業者多不具模型開發能力亦難根據自身需求微調模型，因此在 AI 模型的新能力與性能掌握度上會輸給模型廠商。最明顯的案例是 Excel 的 AI 功能，即便 Microsoft 為 Excel 的擁有者，Copilot 的性能卻屢遭用戶詬病，反之 Claude、ChatGPT Enterprise 的使用體驗更佳。

****SaaS 仍存放企業關鍵數據，API 收費為未來潛在可行路徑****

目前 SaaS 股的擁護者會認為 SaaS 公司仍具 SoR（System of Record）為 AI 無法替代之處，我們非常認同，甚至「單一」「真實」的資料來源會在 AI 時代更加重要，SaaS 業者亦相對應推出 Data Cloud 產品獲客戶快速採用。

![Salesforce Data Cloud 整合 3P 數據與 Salesforce 平台](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2Ffa5ebef4-f072-4406-8ef8-81926cc66e8e.png&width=740&sign=b5HAoQtqnmmnAx8mW7-r5TBiGgxYLbjdDRjkm7oKKvU) ![zoomable](https://images.vocus.cc/fa5ebef4-f072-4406-8ef8-81926cc66e8e.png)

Salesforce Data Cloud 整合 3P 數據與 Salesforce 平台

![vocus｜新世代的創作平台](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2F2f5ef409-e434-4eb7-99a0-cf07f83f045d.png&width=740&sign=B6FqcwOxv2OBYgrkxZlCjq-AwN1yr10T83pykCl-zFU) ![zoomable](https://images.vocus.cc/2f5ef409-e434-4eb7-99a0-cf07f83f045d.png)

不過值得思考的是當 SaaS 的敘事從「業務核心」轉向「CRUD 資料庫」（Create, Read, Update, and Delete）時，顯然對產品銷售與股價估值皆非正向幫助。而若 SaaS 轉向單純的 SoR，對後續的 upsell 會是一大阻力，同時在計費上更可能轉向 UBP 對現有的商業模式產生衝擊。

考量到企業的關鍵營運數據仍是存放在 SaaS 之上，SaaS 業者實際上可透過封鎖 API 調用的方式使第三方工具存取不到企業數據，然而此方式與客戶利益大幅相悖，實際發生機率極低。機率更高的情況是 SaaS 業者依照 API 調取量向第三方收取一定費用，從 Workday 這季 Earnings Call 可以初見端倪：

> "I think you should think of us as an evolving layer on top of hyperscale and in the same way that they charge for consumption of compute cycles and application cycles. We're going to continue to flex that muscle. There are some vendors out there, including some of our peers that would consider them at some level parasites on Workday. They get a free ride on our underlying system of record, and we're going to put an end to that. If you run stuff off of Workday, whether it's from our agents or third-party agents, there will be -- there's a consumption model tied to it." — Workday CEO Aneel Bhusri @ F4Q26 Earnings Call

我們認為這種收費方式可部分抵銷 SaaS 變向單純 SoR 產生的價值減損，惟倘若收費過高則會加速 AI 新創的競爭力。反而，更受影響的應該是圍繞在 Salesforce、SAP、ServiceNow、Workday 等大型 SaaS 生態系之上營運的小型業者。

### 3\. Unit Economic 重構使未來現金流預期出現下修

回顧 2025 年年初，DeepSeek 橫空出世使市場普遍期待「API 價格下滑 → AI 加速導入」的敘事，而企業軟體業者能從中捕捉多數增量 AI 預算並抵銷 API 的成本壓力。站在 3M26 回頭看，該假設至少有三大錯誤之處：1) 開源模型並未如預期的貼近閉源模型演進（Meta、DeepSeek 落後）；2) SLM 在效能上與 LLM 越拉越開；3) API 價格未若預期顯著下滑，近期甚至出現漲價趨勢。

![2H25 後閉源模型能力顯著超越開源模型](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2Fb3c2d7b8-fc43-4a49-8812-ae50a728db59.png&width=740&sign=QWVww6MB8OFk-omNfbk23S6VzCR-j2y6cKodigfEaXU) ![zoomable](https://images.vocus.cc/b3c2d7b8-fc43-4a49-8812-ae50a728db59.png)

2H25 後閉源模型能力顯著超越開源模型

![領先 LLM 業者透過高效能模型收取 API 溢價](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2Fdca11fd8-776a-4162-98f3-645d67993fe3.png&width=740&sign=GcXMiT1ZasjRfCeeuGasfi26E4wKmKvDuWcFd6vHFNM) ![zoomable](https://images.vocus.cc/dca11fd8-776a-4162-98f3-645d67993fe3.png)

領先 LLM 業者透過高效能模型收取 API 溢價

而這對 SaaS 業者的影響在於，在 AI 時代的成本無法像雲端時代有效降低至邊際成本 = 0（訂閱制運作之前提），在 AI Token 邊際成本並非為 0 之下，轉向以「變動成本收取溢價」的 UBP／Outcome Based 形式為順理成章。Salesforce 在 Agentforce 定價上便提供 Flex Credit（US$500 / per 100k Credits）及 Conversations（US$2 / per conversations），新創公司 Sierra 亦採用 Outcome Based 定價，依照客戶實際完成的對話收費。

![Outcome-based 定價能更精準反應服務價值](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2Fa538283b-a52d-40af-9808-2021e1eeb8e2.png&width=740&sign=bkJOEqosCs8WGK48LV-4K62cNh5IW6cwtpNYIL2wKL4) ![zoomable](https://images.vocus.cc/a538283b-a52d-40af-9808-2021e1eeb8e2.png)

Outcome-based 定價能更精準反應服務價值

Bloomberg 便預測以 Outcome 計價的軟體將在 2025-2035 年以 CAGR 30% 成長，與此同時傳統的訂閱制將僅以 CAGR 2% 成長。

![Bloomberg 預估傳統 SaaS 模式將在 2025-2035 僅以 CAGR 2% 成長。資料來源：Bloomberg Intelligence](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2F7595c1e4-17ad-4878-9eb0-7cc3d5dc5330.png&width=740&sign=HUoIA3wC67uohoTF2vBwkx9Css3ytP0bcg7NPCU57zY) ![zoomable](https://images.vocus.cc/7595c1e4-17ad-4878-9eb0-7cc3d5dc5330.png)

Bloomberg 預估傳統 SaaS 模式將在 2025-2035 僅以 CAGR 2% 成長。資料來源：Bloomberg Intelligence

我們認為此次 AI Agent 興起的 Outcome Based／SaaS 廣泛轉向 UBP 為近似於 on-prem 轉雲端帶動的授權轉訂閱浪潮，SaaS 將傳統套裝軟體客戶需自行維運的責任轉移至軟體業者，而 Outcome based 的定價方式更進一步把「任務」轉移給軟體業者。回顧套裝軟體與 SaaS 歷史，可發現隨更多責任轉移至 SaaS 業者，其需額外承擔基礎建設成本（自建或向 CSP 採購），毛利率從套裝軟體時期的約 90% 下滑至 70-80%。

未來軟體業者要維持 SaaS 時代 70-80% 的毛利率似乎並非易事，倘若 AI 產品以 50% 毛利率計算，意味著 SaaS 業者提供之 AI 功能比單純調用 API 貴上一倍，客戶自然會期待「顯著」勝出的性能表現，但我們迄今並沒有看到這一點，也讓 AI 時代軟體公司面臨更低的長期毛利率預期成為現實。（根據我們了解，微軟 M365 Copilot 在未折扣前的 OPM 約為 10%，遠低於 PBP 業務平均的 60%，折扣後甚至為虧損，然該數字並非為微軟官方公佈僅供讀者參考）同時新進者得以用全新的單位經濟與既有業者競爭，且在此競爭框架下新進者不一定無法獲利。

關注點是 AI Token 價格何時會出現下滑。我們預期未來 12 個月在 GPU、CPU、記憶體等基礎建設成本愈加高昂的情況下較難看到，根據 Bloomberg 的 H100 租賃指數顯示算力價格持續上漲，且 AI Token 價格下滑亦會使競爭者同步受惠。長期而言，即便 API 價格大幅下滑，SaaS 業者終究仍將額外多出 API 成本，對既有成本結構產生影響是不可避免的。

![資料來源：Bloomberg SDH100RT Index](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2F34e3b789-1293-4830-a171-fe7a37732cf8.png&width=740&sign=hVT8Ve-PttIrpNEHRda4-1vte51daphUUIlyDJXkiYI) ![zoomable](https://images.vocus.cc/34e3b789-1293-4830-a171-fe7a37732cf8.png)

資料來源：Bloomberg SDH100RT Index

### 4\. 小結：LTV/CAC 皆為負向影響，投資人須看到營收加速成長當作證據

若以簡易的 LTV／CAC 框架拆解上述影響，在 LTV 端 GM 會因為單位經濟轉變而降低，Churn Rate 因更多競爭者加入而上升。在 CAC 端 S&M 為因應更多競爭者湧現 SaaS 業者需投入更多資源在客戶端，NNARR 則因客戶轉向 AI-Native 的解決方案而成長放緩。

> LTV = Gross Margin / (Churn Rate + Discount Rate)
> 
> CAC = TTM S&M / NNARR

---

## 五、我們認同 SaaSpocalypse 之核心論述

整理完企業軟體產業目前的供需狀況後，回顧市場對 SaaSpocalypse 的三大論述與我們的想法。

### 1\. AI 大幅消除軟體進入門檻，SaaS 正在商品化

市場觀點：GenAI 盛行使寫程式門檻大幅下降，過往需要數月甚至數年的軟體開發時間被大幅壓縮，既有業者競爭加劇。

Our View：Yes & Yes，選股應避開應用軟體，聚焦 AI 顛覆性較低 + 符合企業上雲趨勢的基礎設施軟體。

### 2\. Seat-based 商業模式失效，單位經濟出現巨變

市場觀點：SaaS 商業模式的核心建立在 seat-based pricing（按使用者數收費）上，其邏輯是企業的軟體支出與員工數量高度正相關：公司營運擴張 → 招聘更多員工 → 購買更多授權 → SaaS 營收成長。

然而，此商業模式正被 AI 系統性的顛覆。隨著 AI agent 與自動化工具逐步取代人力執行重複性與流程性工作，企業在維持甚至提升產出的同時，對「人」的依賴正在下降。當一個 agent 可以完成過去需要 3–5 名員工才能完成的任務時，企業對應需要購買的 SaaS seats 也將同步減少。換言之，整體採購與席位的線性成長關係被打破。

在單位經濟端，過去 SaaS 雖然同樣依賴雲端基礎設施，但其運算需求主要集中於低強度、可預測的工作負載，使得新增用戶的邊際成本極低，從而形成高毛利與高營運槓桿。然而，在 AI 時代，隨著推論成本與使用量直接掛鉤，運算開始呈現明確的變動成本特性，SaaS 也因此從「邊際成本趨近於零的軟體模式」，轉向「成本隨使用量成長的運算密集型模式」，其單位經濟結構出現根本性改變。

Our View：我們認同長期而言「技術發展將帶動需求上升」（傑文斯悖論）的論述，然而短期內會面臨：1) 除半導體產業外，其餘產業未進入顯著的營運擴張週期，AI 帶動的營運效率改善短期更可能導向裁員，而非大幅擴招；2) AI 所需人才與過往不同，因此會經過一波汰舊換新。舉例而言，IT 諮詢龍頭埃森哲（ACN）便在 9M25 宣佈裁員 11,000 人以重塑組織能力、Atlassian 在 3M26 宣佈裁員約 1,600 人（~10% 員工數）已應對 AI 改變的人力結構。在單位經濟上亦從邊際成本 = 0，轉向重運算的 Token based 任務，商業模式亦從 SaaS 轉往 SaaS + UBP／Outcome based 形式，對未來 3-5 年營運產生不確定性。

### 3\. 對未來 3-5 年後的不確定性使軟體產業估值大幅收縮

市場論述：軟體公司相比其他產業，估值更多建立在 3-5 年之後的營運假設之上。在競爭環境加劇與商業模式轉變衍生的執行風險下，基本面較優秀的個股估值交易於 EV/Sales 10x 以上的美好時光不再。

Our Thoughts：很認同。投資人不應低估估值收縮對股價帶來的衝擊。事實上對比 2H25 後估值高點，如今估值已收縮至相對低位，判斷日後 SaaS 族群要再出現如 11M25 迄今的快速崩跌可能性不大，但反之在利率仍維持高位下（SaaS 股於估值於 2020 年後大幅受美國十年期國債殖利率影響，見下圖）且產業前景未卜下，估值難有顯著擴張空間。對任何產業來說，競爭加劇勢必引起估值緊縮，而非擴張。

![SaaS 股估值於 2020 年後大幅受美國十年期國債殖利率影響](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2F676431f4-3f14-4140-98ee-0e8f68d0132d.png&width=740&sign=BaChkqEzIXfMfrKtITTMGN9YxQKaqybDzhOMoEhjMak) ![zoomable](https://images.vocus.cc/676431f4-3f14-4140-98ee-0e8f68d0132d.png)

SaaS 股估值於 2020 年後大幅受美國十年期國債殖利率影響

---

## 六、投資機會 & 重點觀察指標

誠如前述對軟體產業的商業模式分析，軟體基於 EV/Sales 的估值大量仰賴於對於未來現金流的預期，因此即便近期軟體股的財報仍普遍符合甚至略優於預期，並不代表股價大幅下跌是不合理的，背後更多反應市場對於軟體產業在未來 3-5 年發展的不確定性，導致估值大幅收縮。

而對專注於軟體產業的研究員／投資人而言，AI 顛覆擔憂並非新鮮事，於 2025 年年中已展開諸多 Long Infra & Short Application 的討論，不同族群的股價表現也亦隨之已出現分化，因此若個股於 2H25 股價表現弱於 IGV，則後續需更多證據方能支撐其 AI 敘事。

需再次提醒，我們認為檯面上的 SaaS 業者多數可能都尚未做好應對 AI 的準備，但對比 on-prem 演進至 SaaS 世代時既有龍頭的忽視（ORCL、SAP…），至少如今的 SaaS 業者更積極擁抱 AI 帶來的產業變化。不過身為投資人，若必需投資企業軟體，應精選基礎設施軟體並靜待 OpenAI、Anthropic IPO 後的投資機會。在基礎設施軟體中，CSP 與資安軟體為更可能受惠於 AI 的族群。

### 1\. 展望未來 12 個月，我們認為對 SaaS 業者是一好兩壞

****（a）壞：CSP 為因應 CAPEX 稀釋現金流擔憂，擴大既有產品變現****

- MSFT：M365 E7 推出、資安產品加速推廣……
- Google：TPU 外賣、AI Overview／AI Mode、YouTube 訂閱與廣告、Wiz（資安）……
- Meta：擴大 ad load，整合 Manus、影片產生工具營收 run-rate 達到 US$10bn、2026 年將推出 mango 與 avocado 模型……
- Amazon：AI 加速資料庫遷移、AMZN DSP、低軌衛星、edge AI 裝置……

這些變化在企業 IT 支出未見回升下對企業軟體是負向意涵，同樣對 CSP 跨足之其他產業的競爭者不利（廣告、娛樂、硬體裝置……）。

****（b）壞：OpenAI／Anthropic IPO 前路演／後引起更多資金流動****

- 預計 OpenAI 與 Anthropic 將於 4Q26-1H27 IPO，而預計隨後諸多 AI 新創公司亦將展開 IPO 程序，更多客戶案例與財務狀況將隨之揭露，對 SaaSpocalypse 提供更多實質證據。
- 同時我們預計 Anthropic／OpenAI 在 IPO 前將盡可能的加速產品推出步伐，目的是盡可能的增加 TAM，係因在軟體股中，TAM 的成長持續性與可擴展性是決定估值的關鍵。因此我們可以合理想像在 2Q26-4Q26 這段期間 Anthropic／OpenAI 將持續在應用軟體／基礎設施軟體中攻城掠地（OpenAI 亦可能加速廣告產業佈局，對 Publisher 是負向意涵），類似於近期 Anthropic 發表 Claude for Work（-ve to MSFT）、Claude Managed Agents（-ve to NET、FSLY）。

![SaaS 業者常透過 TAM 故事擴張估值。資料來源：paloalto](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2F598bd4e0-02f6-45e6-8005-eb7309b682a6.png&width=740&sign=pm-3d0y1soinv2O1xJPTYAn03cOI-QHu0r0GYmaAt3k) ![zoomable](https://images.vocus.cc/598bd4e0-02f6-45e6-8005-eb7309b682a6.png)

SaaS 業者常透過 TAM 故事擴張估值。資料來源：paloalto

- 惟 Anthropic／OpenAI 仍有可能在此期間透過與既有 SaaS 業者合作的方式擴大 TAM（類似先前 Anthropic 與 FactSet、Thomson Reuters、Salesforce 等的 [合作](https://money.udn.com/money/story/123398/9342920) ），但我們預期這大概率為短期個別公司的股價催化，長線 SaaS 股價值遭稀釋的趨勢仍不變。
- 以 OpenAI 先前於募資時提供之 2027 年財測計算，IPO 後中性偏樂觀市值可達到 US$1tn 以上（EV/Sales 20x，考量 PLTR、CRWD、NET 等企業軟體可以交易在此估值之上且中國同業 Minimax、智譜 IPO 後估值落在 EV/Sales 112x）。而若 Anthropic 交易在同等市值，意味著兩間 AI 公司的市值合計已逼近 AMZN，勢必在 IPO 後引起資金流動，同時 L/S 配置更加盛行，為 SaaS 業者股價產生壓力。

****（c）好：低估值下 M&A 與私有化加速****

- 軟體族群估值已跌至 fwd-12M EV/Sales 3.5x 水位（vs. 近期高點 ~6x）為族群創造不錯的 M&A 機會與私募基金進場契機。Mergermarket 報告顯示 2025 年全球 M&A 活動回溫，總數量創下 2014 年以來除 2021 年的新高，預計 2026 年將持續保持強勁。AlixPartners 便估計 2026 年軟體併購將年增 40%。
- 雖企業軟體股評價下滑使私募基金對軟體股的投資出場難度增加（Blackstone 撤回 Liftoff IPO、Hellman & Friedman 需至 2H26 才會進行 Ultimate Kronos Group IPO），不過我們認為私募基金趁著軟體族群估值下跌之際將旗下 Portfolio 進行更好的平台化與 AI 整合是合理的舉措。Apollo CEO 表示正積極進攻軟體領域尋找合適機會，Novacap 甫於 2M26 完成 Technologies Fund VII US$3.8bn 的募資，意圖尋找北美的 B2B 軟體和技術服務 M&A 機會。
- 潛在的被收購方包含：SentinelOne（GOOGL、CSCO）、Elastic（IBM）、Netskope（HPE、AMZN）、Rubrik（MSFT、GOOGL、AMZN、PE）、Okta（GOOGL）、Hubspot（GOOGL）、Commvault（PE）、monday.com（PE）、GitLab（GOOGL、DDOG）。

### 2\. 重點觀察指標

****量化指標****

- 營收加速成長與否。
- - 目前僅 CRWD, PANW, NET, PLTR 有給出相對應之全年財測，Salesforce 給予 F2H27 有機營收加速成長之財測。
- NRR or GRR、模組採用率等客戶留存指標。

****質化論述****

- 相比 AI-Native 工具存有不可替代性或差異化優勢。
- - 例如 Salesforce 在官網中提及相比 Sierra 有與外部合作夥伴的 Zero-Copy 優勢。

![Salesforce 官網提及對比 Sierra 的產品優勢](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2Fb9278ccb-b269-4be1-a0f1-d8348e8f2787.png&width=740&sign=iLGoCcc2esAxG6OvrZCPzLXAuNjEAzilo5ttW2WR2SM) ![zoomable](https://images.vocus.cc/b9278ccb-b269-4be1-a0f1-d8348e8f2787.png)

Salesforce 官網提及對比 Sierra 的產品優勢

- - 或 Microsoft 在 [網站](https://www.microsoft.com/en-us/microsoft-365-copilot/copilot-vs-chatgpt-enterprise#teams) 中提及 Copilot 相比 ChatGPT Enterprise 有獲取 Teams 會議、了解組織架構、敏感資料保護、讀取 SharePoint 頁面等優勢。
- 特定環節之數據護城河於 AI 時代更加強化，進而為 SoR 業者延伸出更多變現途徑。

### 3\. 投資機會

****a. CSP：****

- Thesis：在 AI Agent 帶動上游記憶體、GPU、CPU 皆缺貨下，同步將使提供雲服務的業者受惠，中國的阿里雲、百度雲、騰訊雲便宣布因為 OpenClaw 帶動的基礎建設需求，AI 算力服務上漲 5-30% 不等，文件儲存價格上漲 30%。
- 催化劑：1) 2H26 後將有更多資料中心上線帶動營收年增率加速成長可能；2) 承 (1)，在營收加速成長可期後將減緩市場對於 FCF 下滑的擔憂，同時我們預期 CSP 管理層將在 2H26 密集與市場溝通 2027 年 CAPEX 成長幅度，建議投資人可關注 Capital Intensity（資本支出／營收）、OCF／Revenue 兩個指標的差距作為觀察指標。

![CSPs 在未來三年具緊密資料中心 pipeline](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2F0520f7b4-744a-4f0d-b43d-ae173c3fefc7.png&width=740&sign=ubYR5Sx06U1rhN3dsug2Cp05SXTytNPZ-4wCpmmS0GE) ![zoomable](https://images.vocus.cc/0520f7b4-744a-4f0d-b43d-ae173c3fefc7.png)

CSPs 在未來三年具緊密資料中心 pipeline

- 相關個股：MSFT, GOOGL, AMZN, DOCN。

****b. 資安：****

- Thesis：資安需 100% 準確性且多數有價值資料皆非公開，Threat Intelligence 資料來自真實客戶環境、威脅情資、MDR/IR 專家標註資料。而不同次產業將受惠於不同趨勢，如：EDR／XDR：AI 加速端點由防毒軟體升級、SASE／API／CDN 資安：AI 帶動網路流量增加，Cloudflare CEO Matthew Prince 預測 AI 流量將於 2027 年超越人類流量、Observability：開發者效率提升，軟體系統的複雜度也會呈指數級增長，需可觀測性解決方案、Identity：Agent to Agent 交流需身份權限管控。
- 同時資安領域亦是在 CIO 調查中最具韌性的企業軟體次產業。

![Jefferies CIO 調查顯示資安為 AI 時代下最具韌性的支出項目。資料來源：Jefferies CIO Survey](https://resize-image.vocus.cc/resize?compression=6&norotation=true&url=https%3A%2F%2Fimages.vocus.cc%2Fa7b36b1c-ad23-4c64-a620-112fd043bf22.png&width=740&sign=MymJ507fZgcJr1vgp4fWaifEQKQMPFupH810QiVqBXw) ![zoomable](https://images.vocus.cc/a7b36b1c-ad23-4c64-a620-112fd043bf22.png)

Jefferies CIO 調查顯示資安為 AI 時代下最具韌性的支出項目。資料來源：Jefferies CIO Survey

- 相關個股：CRWD, PANW, NET, DDOG。

---

## 參考資料

1. [20VC with Harry Stebbings（YouTube）](https://youtu.be/zjcYlEiwnKI)
2. [TrueUp — Tech Layoffs Tracker](https://www.trueup.io/layoffs)
3. [Retool — AI Build vs. Buy Report 2026](https://retool.com/blog/ai-build-vs-buy-report-2026)
4. [Altimeter Capital — OpenAI FDE 訪談（YouTube）](https://www.youtube.com/watch?v=cBD7_R-Cizg)
5. [經濟日報報導](https://money.udn.com/money/story/5603/9389004)
6. [經濟日報——Anthropic 與 Salesforce 等合作報導](https://money.udn.com/money/story/123398/9342920)
7. [Microsoft — Copilot vs. ChatGPT Enterprise](https://www.microsoft.com/en-us/microsoft-365-copilot/copilot-vs-chatgpt-enterprise)
8. [Freddy Business & Research（方格子）](https://vocus.cc/article/699d1ab8fd89780001fc812f)
9. Bloomberg SDH100RT Index（H100 租賃指數，無公開連結）
10. [Salesforce Data Cloud](https://www.salesforce.com/ap/data/)
11. a16z 引用 Jefferies 數據，X [@a16z](https://x.com/a16z) ： [貼文](https://x.com/a16z/status/2040105813776441368)
12. a16z 引用 YipitData 數據，X [@a16z](https://x.com/a16z) ： [貼文](https://x.com/a16z/status/2040080669221830684)
13. [Ramp — Top SaaS Vendors（2026/03）](https://ramp.com/velocity/top-saas-vendors-on-ramp-march-2026)
14. [Menlo Ventures — 2025: The State of Generative AI in the Enterprise](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/)
15. [Salesforce — Agentforce vs. Sierra](https://www.salesforce.com/compare/agentforce-vs-sierra/)
16. Morgan Stanley《4Q25 CIO Survey — Momentum Eases into 2026》
17. [OpenAI — Introducing OpenAI Frontier](https://openai.com/zh-Hant/index/introducing-openai-frontier/)
18. [OpenAI — Frontier Alliance Partners](https://openai.com/index/frontier-alliance-partners/)
19. [Anthropic — Managed Agents（Engineering）](https://www.anthropic.com/engineering/managed-agents)
20. [Anthropic — Managed Agents Overview（文件）](https://platform.claude.com/docs/en/managed-agents/overview)
21. [Palo Alto Networks 投資人資料](https://investors.paloaltonetworks.com/static-files/b97f7a32-619e-4605-9b9e-96f828d30ffa)
22. [科技報橘 — OpenAI 新模型 Cyber／Mythos 與 Anthropic](https://techorange.com/2026/04/10/openai-new-model-cyber-mythos-anthopic/)
23. [Novacap — Tech Fund VII 募資公告](https://novacapcorp.com/news/novacap-closes-tech-fund-vii-at-nearly-3-8-billion/)
24. Goldman Sachs《US Equities Weekly Rundown — April 10, 2026》
25. [知新聞報導](https://www.knews.com.tw/news/A6F6E2F7728B4F73E8A127A44AF16C7E)
26. [科技新報——AI 訓練公司高薪聘華爾街人才報導](https://technews.tw/2025/11/10/ai-training-companies-are-offering-up-to-150-an-hour-to-get-wall-streeters-to-train-their-models/)
27. [YipitData — Is AI Replacing SaaS?](https://www.yipitdata.com/resources/blog/is-ai-replacing-saas)
28. [Epoch AI — Frontier Data Centers](https://epoch.ai/data/data-centers/)
29. [a16z Growth — Anatomy of an Enterprise Platform Company](https://a16z.com/anatomy-of-an-enterprise-platform-company/)
30. [Sequoia — Services: The New Software](https://sequoiacap.com/article/services-the-new-software/)
31. [a16z — Death of Software? Nah](https://a16z.com/death-of-software-nah/)
32. [a16z — Good News: AI Will Eat Application Software](https://a16z.com/good-news-ai-will-eat-application-software/)
33. [mph International — AI Is Eating Software](https://mph-intl.com/blog/ai-is-eating-software/)
34. [ION Analytics / Mergermarket — Software Shakeout Delays Exits for Some, Opens Buying Window for Others](https://ionanalytics.com/insights/mergermarket/software-shakeout-delays-exits-for-some-opens-buying-window-for-others/)