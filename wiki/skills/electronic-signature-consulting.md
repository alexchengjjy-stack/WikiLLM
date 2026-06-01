---
title: "電子簽章產品顧問"
type: skill
category: product
proficiency: advanced
tags: [電子簽章, 產品顧問, 合規, AATL, 法規]
date_created: 2026-05-14
date_updated: 2026-05-14
related_projects: []
related_concepts: ["../concepts/e-signature-service.md"]
summary: "台灣電子簽章市場的產品顧問能力，涵蓋法規解釋、技術架構說明、合規邊界判斷。"
---

# 電子簽章產品顧問

> 具備向 B2B 客戶解釋電子簽章技術、法律效力、合規要求，並針對不同業務場景提供正確方案建議的能力。此技能橫跨法規、技術與業務三個層面。

## 核心能力

- **法規解釋**：台灣電子簽章法（2024 修法）、數發部能量登錄、外國憑證機構
- **技術說明**：AATL 數位憑證、PKI 架構、時間戳記、簽署軌跡
- **方案顧問**：依客戶場景推薦最適合的簽署方式（遠距/現場/Line傳簽/API）
- **合規邊界**：識別哪些場景**不適合**電子簽章（如電子印章代替自然人簽名的紅線）
- **競品比較**：國內外主要廠商的技術差異、定價邏輯、使用限制

## 重要合規知識點

### 電子印章使用紅線 ⚠️
- 電子印章**不可**用於需要確認「自然人身分」的場景
- 例：醫美術前同意書必須由醫師本人簽名，不可用公司章替代
- 例：需強制執行的票據類需有「人臉+筆跡」的直接證據

### AATL 使用場景判斷
- **必須用 AATL**：高風險合約（借貸、醫療、政府採購）
- **不必用 AATL**：內部流程表單（人資打卡、請假、內部請款）
- **AATL 限制**：單檔建議不超過 10MB；多份簽完後不可合併（各自嵌入憑證）

### 簽署方式適用場景

| 簽署方式 | 最適場景 | 注意事項 |
|----------|----------|----------|
| 遠距簽 | B2B 合約、委任書 | 需確認對方有 Email |
| 現場簽 | 臨櫃服務（醫院、診所、銀行） | 硬體需求：平板/AIO |
| Line 傳簽 | 小微企業、租車、保險 | 保留完整軌跡，適合需存證場景 |
| 簡訊簽 | 高齡者、無 Email 場景 | 費用較高（$2/則）|
| API 整合 | ERP、HIS、BPM 系統串接 | 需技術評估工期 |
| 外部表單 | 多份文件一次簽、客戶公開連結 | 好好簽獨有功能，競爭優勢 |

## 市場競品知識

- [國內電子簽章比較](../analyses/esign/esign-domestic-comparison.md)
- [全球電子簽章比較](../analyses/esign/esign-global-comparison.md)
- [[dottedsign-pricing|點點簽定價與方案對比]]：掌握國際化 B2B 計量計費（Business 任務包）與 API 原生整合特色。
- 了解 eIDAS 2.0 歐盟框架對台灣出海廠商的意義

## 相關連結

- [2024 台灣電子簽章法](../sources/taiwan-e-signature-law-2024.md)
- [電子簽章技術概覽](../sources/e-signature-tech-overview.md)
- [數發部能量登錄](../sources/moda-esignature-energy-registration.md)
- [eIDAS 2.0 歐盟框架](../sources/eidas2-overview.md)
- [[dottedsign-pricing|點點簽定價方案]]
- [客戶成功管理](customer-success-management.md)
