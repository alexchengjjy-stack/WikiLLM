---
title: "WikiLLM 知識庫健康檢查與 Lint 優化報告"
type: analysis
analysis_type: synthesis
tags: [知識庫維護, Lint, 健康檢查, 知識庫管理, 合規審查]
date_created: 2026-05-29
date_updated: 2026-06-01
source_count: 0
sources: []
summary: "針對 WikiLLM 知識庫 170 個頁面進行全面 Lint 普查，分析編碼、Frontmatter 缺失、孤立頁面及潛在法規政策矛盾並給出優化方案。"
---

# WikiLLM 知識庫健康檢查與 Lint 優化報告

> **報告簡介**：本報告是針對 WikiLLM 知識庫進行全面靜態檢查與合規審核的成果。對 170 個 Markdown 檔案進行了編碼校驗、YAML 元數據完整性、死連結、孤立頁面及業務條款一致性審核。

---

## 1. 編碼錯誤 (Encoding Errors) ── 已修復

✅ 所有檔案皆為正確的 UTF-8 編碼。

在健康檢查初始階段，曾偵測到 **1 個** 核心文件存在非 UTF-8 二進位無效字元：
- **[breezy-brain-integration-flow.md](../../products/breezy-brain/breezy-brain-integration-flow.md)**: 於第 8769 位元組位置含有無效的二進位字元 ``。該字元目前已成功剔除，檔案已恢復 100% 正確編碼。

## 2. YAML Frontmatter 格式缺失

部分檔案未包含標準 frontmatter 或缺少關鍵欄位，不符合 `AGENTS.md` 元數據規範。

### 目錄: `root/`
- **[log.md](../../log.md)**: Missing required frontmatter field: type
### 目錄: `analyses/bzb/`
- **[bzb-antigravity-aipm-framework.md](../../analyses/bzb/bzb-antigravity-aipm-framework.md)**: Missing required frontmatter field: title
- **[bzb-antigravity-aipm-framework.md](../../analyses/bzb/bzb-antigravity-aipm-framework.md)**: Missing required frontmatter field: type
### 目錄: `playbooks/seo-geo-starter-kit/`
- **[agent.md](../../playbooks/seo-geo-starter-kit/agent.md)**: Missing required frontmatter field: title
- **[agent.md](../../playbooks/seo-geo-starter-kit/agent.md)**: Missing required frontmatter field: type
- **[README.md](../../playbooks/seo-geo-starter-kit/README.md)**: Missing required frontmatter field: title
- **[README.md](../../playbooks/seo-geo-starter-kit/README.md)**: Missing required frontmatter field: type
### 目錄: `skills/`
- **[ai-research-agent-design.md](../../skills/ai-research-agent-design.md)**: Missing required frontmatter field: title
- **[ai-research-agent-design.md](../../skills/ai-research-agent-design.md)**: Missing required frontmatter field: type
- **[antigravity-role-switching.md](../../skills/antigravity-role-switching.md)**: Missing required frontmatter field: title
- **[antigravity-role-switching.md](../../skills/antigravity-role-switching.md)**: Missing required frontmatter field: type
### 目錄: `sources/`
- **[acrobat-enterprise-pricing.md](../../sources/acrobat-enterprise-pricing.md)**: Source page missing 'source_file' field
- **[agent-skill-creator.md](../../sources/agent-skill-creator.md)**: Source page missing 'source_file' field
- **[agent-teams-collaboration.md](../../sources/agent-teams-collaboration.md)**: Source page missing 'source_file' field
- **[ai-agent-products-workflow.md](../../sources/ai-agent-products-workflow.md)**: Source page missing 'source_file' field
- **[aipm-framework-4.md](../../sources/aipm-framework-4.md)**: Missing required frontmatter field: type
- **[bzs-dingxin-isv-partnership-v2.md](../../sources/bzs-dingxin-isv-partnership-v2.md)**: Missing required frontmatter field: title
- **[bzs-dingxin-isv-partnership-v2.md](../../sources/bzs-dingxin-isv-partnership-v2.md)**: Missing required frontmatter field: type
- **[bzs-features-v2.md](../../sources/bzs-features-v2.md)**: Missing required frontmatter field: title
- **[bzs-features-v2.md](../../sources/bzs-features-v2.md)**: Missing required frontmatter field: type
- **[claude-code-ollama-local-deployment.md](../../sources/claude-code-ollama-local-deployment.md)**: Missing required frontmatter field: type
- **[claude-rules-12-commandments.md](../../sources/claude-rules-12-commandments.md)**: Missing required frontmatter field: type
- **[claude-seo-universal-tool.md](../../sources/claude-seo-universal-tool.md)**: Missing required frontmatter field: type
- **[e-signature-tech-overview.md](../../sources/e-signature-tech-overview.md)**: Source page missing 'source_file' field
- **[forge-openclaw-architecture.md](../../sources/forge-openclaw-architecture.md)**: Source page missing 'source_file' field
- **[taiwan-e-signature-law-2024.md](../../sources/taiwan-e-signature-law-2024.md)**: Source page missing 'source_file' field
- **[toxic-pm-system-3.md](../../sources/toxic-pm-system-3.md)**: Source page missing 'source_file' field
- **[toxic-pm-system-4.md](../../sources/toxic-pm-system-4.md)**: Source page missing 'source_file' field
- **[vibe-coding-claude-code.md](../../sources/vibe-coding-claude-code.md)**: Source page missing 'source_file' field
- **[zero-code-gemini-studio.md](../../sources/zero-code-gemini-studio.md)**: Source page missing 'source_file' field
### 目錄: `topics/`
- **[karpathy-autoresearch.md](../../topics/karpathy-autoresearch.md)**: Missing required frontmatter field: title
- **[karpathy-autoresearch.md](../../topics/karpathy-autoresearch.md)**: Missing required frontmatter field: type

## 3. 失效內部連結 / 缺失頁面 (Broken Links & Missing Pages)

- 檔案 **[analyses/bzb/bzb-antigravity-aipm-framework.md](../../analyses/bzb/bzb-antigravity-aipm-framework.md)** 中的連結 `[Harness Engineering](../topics/harness-engineering.md)` (解析為 `analyses/topics/harness-engineering.md`) 指向不存在的檔案。
- 檔案 **[analyses/bzb/bzb-antigravity-aipm-framework.md](../../analyses/bzb/bzb-antigravity-aipm-framework.md)** 中的連結 `[Vibe Coding](../concepts/vibe-coding-paradigm.md)` (解析為 `analyses/concepts/vibe-coding-paradigm.md`) 指向不存在的檔案。
- 檔案 **[analyses/bzb/bzb-mvp-roadmap.md](../../analyses/bzb/bzb-mvp-roadmap.md)** 中的連結 `[BreezyBrain 產品演進路線圖](../products/breezy-brain/breezy-brain-roadmap.md)` (解析為 `analyses/products/breezy-brain/breezy-brain-roadmap.md`) 指向不存在的檔案。
- 檔案 **[analyses/bzb/bzb-mvp-roadmap.md](../../analyses/bzb/bzb-mvp-roadmap.md)** 中的連結 `[BreezyBrain 產品規格書](../products/breezy-brain/Product-Spec.md)` (解析為 `analyses/products/breezy-brain/Product-Spec.md`) 指向不存在的檔案。
- 檔案 **[analyses/bzb/bzb-mvp-roadmap.md](../../analyses/bzb/bzb-mvp-roadmap.md)** 中的連結 `[BreezyBrain 需求變更日誌](../products/breezy-brain/Product-Spec-CHANGELOG.md)` (解析為 `analyses/products/breezy-brain/Product-Spec-CHANGELOG.md`) 指向不存在的檔案。
- 檔案 **[analyses/bzb/bzb-mvp-roadmap.md](../../analyses/bzb/bzb-mvp-roadmap.md)** 中的連結 `[Product-Spec.md](../products/breezy-brain/Product-Spec.md)` (解析為 `analyses/products/breezy-brain/Product-Spec.md`) 指向不存在的檔案。
- 檔案 **[analyses/bzb/bzb-spec-analysis-report.md](../../analyses/bzb/bzb-spec-analysis-report.md)** 中的連結 `[Product-Spec.md](../products/breezy-brain/Product-Spec.md)` (解析為 `analyses/products/breezy-brain/Product-Spec.md`) 指向不存在的檔案。
- 檔案 **[analyses/bzb/bzb-spec-defense.md](../../analyses/bzb/bzb-spec-defense.md)** 中的連結 `[Product-Spec.md#2.3.2](../products/breezy-brain/Product-Spec.md)` (解析為 `analyses/products/breezy-brain/Product-Spec.md`) 指向不存在的檔案。
- 檔案 **[analyses/bzb/bzb-spec-defense.md](../../analyses/bzb/bzb-spec-defense.md)** 中的連結 `[Product-Spec.md#3.1](../products/breezy-brain/Product-Spec.md)` (解析為 `analyses/products/breezy-brain/Product-Spec.md`) 指向不存在的檔案。
- 檔案 **[analyses/bzb/bzb-spec-defense.md](../../analyses/bzb/bzb-spec-defense.md)** 中的連結 `[Product-Spec.md#3.2](../products/breezy-brain/Product-Spec.md)` (解析為 `analyses/products/breezy-brain/Product-Spec.md`) 指向不存在的檔案。
- 檔案 **[analyses/bzb/bzb-spec-defense.md](../../analyses/bzb/bzb-spec-defense.md)** 中的連結 `[Product-Spec.md#2.7.2](../products/breezy-brain/Product-Spec.md)` (解析為 `analyses/products/breezy-brain/Product-Spec.md`) 指向不存在的檔案。
- 檔案 **[analyses/bzb/bzb-spec-defense.md](../../analyses/bzb/bzb-spec-defense.md)** 中的連結 `[BreezyBrain 產品規格書](../products/breezy-brain/Product-Spec.md)` (解析為 `analyses/products/breezy-brain/Product-Spec.md`) 指向不存在的檔案。
- 檔案 **[analyses/bzb/bzb-spec-defense.md](../../analyses/bzb/bzb-spec-defense.md)** 中的連結 `[新潛客資格確認 SOP](../playbooks/new-lead-qualification.md)` (解析為 `analyses/playbooks/new-lead-qualification.md`) 指向不存在的檔案。
- 檔案 **[analyses/bzb/bzb-spec-defense.md](../../analyses/bzb/bzb-spec-defense.md)** 中的連結 `[企業試用版跟進 Checklist](../playbooks/enterprise-trial-followup.md)` (解析為 `analyses/playbooks/enterprise-trial-followup.md`) 指向不存在的檔案。
- 檔案 **[analyses/bzs/bzs-saas-funnel-ltv-cac-report.md](../bzs/bzs-saas-funnel-ltv-cac-report.md)** 中的連結 `[BZS 2026 行銷廣告報表 (Google Ads & Pmax)](../sources/bzs-marketing-ads-2026.md)` (解析為 `analyses/sources/bzs-marketing-ads-2026.md`) 指向不存在的檔案。
- 檔案 **[analyses/bzs/bzs-saas-marketing-synthesis-2026.md](../bzs/bzs-saas-marketing-synthesis-2026.md)** 中的連結 `[2026 行銷廣告報表 (Google Ads & Pmax)](../sources/bzs-marketing-ads-2026.md)` (解析為 `analyses/sources/bzs-marketing-ads-2026.md`) 指向不存在的檔案。
- 檔案 **[analyses/bzs/bzs-saas-marketing-synthesis-2026.md](../bzs/bzs-saas-marketing-synthesis-2026.md)** 中的連結 `[BZS PM 數據分析報表彙整 (2025.10-2026.05)](../sources/pm-breezysign-analytics-reports.md)` (解析為 `analyses/sources/pm-breezysign-analytics-reports.md`) 指向不存在的檔案。
- 檔案 **[analyses/bzs/bzs-saas-marketing-synthesis-2026.md](../bzs/bzs-saas-marketing-synthesis-2026.md)** 中的連結 `[好好簽實際案例和場景](../sources/bzs-use-cases-and-clients.md)` (解析為 `analyses/sources/bzs-use-cases-and-clients.md`) 指向不存在的檔案。
- 檔案 **[analyses/bzs/bzs-saas-marketing-synthesis-2026.md](../bzs/bzs-saas-marketing-synthesis-2026.md)** 中的連結 `[業務引導 SOP](../playbooks/bzs-enterprise-trial-sop.md)` (解析為 `analyses/playbooks/bzs-enterprise-trial-sop.md`) 指向不存在的檔案。
- 檔案 **[analyses/bzs/bzs-saas-marketing-synthesis-2026.md](../bzs/bzs-saas-marketing-synthesis-2026.md)** 中的連結 `[SaaS 行銷數據分析與漏斗優化](../skills/saas-marketing-analytics.md)` (解析為 `analyses/skills/saas-marketing-analytics.md`) 指向不存在的檔案。
- 檔案 **[analyses/bzs/bzs-saas-ops-csm-reconciliation-202605.md](../bzs/bzs-saas-ops-csm-reconciliation-202605.md)** 中的連結 `[工作專案追蹤](../index.md)` (解析為 `analyses/index.md`) 指向不存在的檔案。
- 檔案 **[analyses/esign/esign-ai-search-geo-empirical-report.md](../../analyses/esign/esign-ai-search-geo-empirical-report.md)** 中的連結 `[實際 AI 搜尋測試與 GEO 實證方法](../topics/ai-search-testing.md)` (解析為 `analyses/topics/ai-search-testing.md`) 指向不存在的檔案。
- 檔案 **[analyses/esign/esign-domestic-comparison.md](../../analyses/esign/esign-domestic-comparison.md)** 中的連結 `[點點簽](../entities/dottedsign.md)` (解析為 `analyses/entities/dottedsign.md`) 指向不存在的檔案。
- 檔案 **[analyses/esign/esign-domestic-comparison.md](../../analyses/esign/esign-domestic-comparison.md)** 中的連結 `[律果簽](../entities/legalsign.md)` (解析為 `analyses/entities/legalsign.md`) 指向不存在的檔案。
- 檔案 **[analyses/esign/esign-domestic-comparison.md](../../analyses/esign/esign-domestic-comparison.md)** 中的連結 `[好好簽](../entities/breezysign.md)` (解析為 `analyses/entities/breezysign.md`) 指向不存在的檔案。
- 檔案 **[analyses/esign/esign-domestic-comparison.md](../../analyses/esign/esign-domestic-comparison.md)** 中的連結 `[FastSIGN](../entities/fastsign.md)` (解析為 `analyses/entities/fastsign.md`) 指向不存在的檔案。
- 檔案 **[analyses/esign/esign-domestic-comparison.md](../../analyses/esign/esign-domestic-comparison.md)** 中的連結 `[電子簽章解決方案服務能量登錄](../sources/moda-esignature-energy-registration.md)` (解析為 `analyses/sources/moda-esignature-energy-registration.md`) 指向不存在的檔案。
- 檔案 **[analyses/esign/esign-dottedsign-price-hike-churn-analysis.md](../../analyses/esign/esign-dottedsign-price-hike-churn-analysis.md)** 中的連結 `[點點簽](../entities/dottedsign.md)` (解析為 `analyses/entities/dottedsign.md`) 指向不存在的檔案。
- 檔案 **[analyses/esign/esign-dottedsign-price-hike-churn-analysis.md](../../analyses/esign/esign-dottedsign-price-hike-churn-analysis.md)** 中的連結 `[海沃管理顧問股份有限公司](../entities/hai-wo-management.md)` (解析為 `analyses/entities/hai-wo-management.md`) 指向不存在的檔案。
- 檔案 **[analyses/esign/esign-dottedsign-price-hike-churn-analysis.md](../../analyses/esign/esign-dottedsign-price-hike-churn-analysis.md)** 中的連結 `[太平洋旅行社 Onboarding](../projects/pacific-travel-onboarding.md)` (解析為 `analyses/projects/pacific-travel-onboarding.md`) 指向不存在的檔案。
- 檔案 **[analyses/esign/esign-dottedsign-price-hike-churn-analysis.md](../../analyses/esign/esign-dottedsign-price-hike-churn-analysis.md)** 中的連結 `[麻吉行得通 Onboarding](../projects/maji-mobility-onboarding.md)` (解析為 `analyses/projects/maji-mobility-onboarding.md`) 指向不存在的檔案。
- 檔案 **[analyses/esign/esign-dottedsign-price-hike-churn-analysis.md](../../analyses/esign/esign-dottedsign-price-hike-churn-analysis.md)** 中的連結 `[BreezySign 好好簽 20260522 日報](../sources/bzs-daily-report-20260522.md)` (解析為 `analyses/sources/bzs-daily-report-20260522.md`) 指向不存在的檔案。
- 檔案 **[analyses/esign/esign-dottedsign-price-hike-churn-analysis.md](../../analyses/esign/esign-dottedsign-price-hike-churn-analysis.md)** 中的連結 `[BreezySign 好好簽 20260522 週報](../sources/bzs-weekly-report-20260522.md)` (解析為 `analyses/sources/bzs-weekly-report-20260522.md`) 指向不存在的檔案。
- 檔案 **[analyses/esign/esign-dottedsign-price-hike-churn-analysis.md](../../analyses/esign/esign-dottedsign-price-hike-churn-analysis.md)** 中的連結 `[BreezySign 好好簽 20260527 業務日報](../sources/20260527-saas-daily.md)` (解析為 `analyses/sources/20260527-saas-daily.md`) 指向不存在的檔案。
- 檔案 **[analyses/esign/esign-dottedsign-price-hike-churn-analysis.md](../../analyses/esign/esign-dottedsign-price-hike-churn-analysis.md)** 中的連結 `[BreezySign 好好簽 2026-05-29 週報](../sources/bzs-weekly-report-20260529.md)` (解析為 `analyses/sources/bzs-weekly-report-20260529.md`) 指向不存在的檔案。
- 檔案 **[analyses/esign/esign-dottedsign-website-seo-geo-analysis.md](../../analyses/esign/esign-dottedsign-website-seo-geo-analysis.md)** 中的連結 `[SEO / GEO 優化評分標準](../concepts/seo-geo-optimization.md)` (解析為 `analyses/concepts/seo-geo-optimization.md`) 指向不存在的檔案。
- 檔案 **[analyses/esign/esign-legalsign-website-seo-geo-analysis.md](../../analyses/esign/esign-legalsign-website-seo-geo-analysis.md)** 中的連結 `[SEO / GEO 優化評分標準](../concepts/seo-geo-optimization.md)` (解析為 `analyses/concepts/seo-geo-optimization.md`) 指向不存在的檔案。
- 檔案 **[analyses/esign/esign-monitoring-snapshot-202605.md](../esign/esign-monitoring-snapshot-202605.md)** 中的連結 `[電子簽章能量登錄競品週期性觀測機制 (Playbook)](../playbooks/esign-competitor-monitoring-mechanism.md)` (解析為 `analyses/playbooks/esign-competitor-monitoring-mechanism.md`) 指向不存在的檔案。
- 檔案 **[analyses/esign/esign-monitoring-snapshot-202605.md](../esign/esign-monitoring-snapshot-202605.md)** 中的連結 `[電子簽章能量登錄競品週期性觀測機制](../playbooks/esign-competitor-monitoring-mechanism.md)` (解析為 `analyses/playbooks/esign-competitor-monitoring-mechanism.md`) 指向不存在的檔案。
- 檔案 **[analyses/esign/esign-monitoring-snapshot-202605.md](../esign/esign-monitoring-snapshot-202605.md)** 中的連結 `[電子簽章解決方案服務能量登錄許可名單](../sources/esign-solution-approved-list.md)` (解析為 `analyses/sources/esign-solution-approved-list.md`) 指向不存在的檔案。

## 4. 孤立頁面與未註冊頁面

### 4.1 孤立頁面 (Orphaned Pages)
> 孤立頁面定義：除了 `index.md` 之外，沒有任何其他 Wiki 檔案連結至它。

#### 4.1.1 已在首頁註冊但無其他 Wiki 內頁交叉連結 (共 54 個):
- **[analyses/bzb/bzb-spec-analysis-report.md](../../analyses/bzb/bzb-spec-analysis-report.md)**
- **[analyses/bzs/bzs-blog-marketing-posts-202605.md](../bzs/bzs-blog-marketing-posts-202605.md)**
- **[analyses/bzs/bzs-bu-role-based-tasklist.md](../bzs/bzs-bu-role-based-tasklist.md)**
- **[analyses/bzs/bzs-saas-marketing-synthesis-2026.md](../bzs/bzs-saas-marketing-synthesis-2026.md)**
- **[analyses/bzs/bzs-saas-ops-csm-reconciliation-202605.md](../bzs/bzs-saas-ops-csm-reconciliation-202605.md)**
- **[analyses/bzs/bzs-saas-plan-sales-comparison.md](../bzs/bzs-saas-plan-sales-comparison.md)**
- **[analyses/esign/esign-ai-search-geo-empirical-report.md](../../analyses/esign/esign-ai-search-geo-empirical-report.md)**
- **[analyses/esign/esign-competitor-seo-geo-analysis-20260525.md](../esign/esign-competitor-seo-geo-analysis-20260525.md)**
- **[analyses/esign/esign-competitor-seo-geo-analysis-20260527.md](../../analyses/esign/esign-competitor-seo-geo-analysis-20260527.md)**
- **[analyses/esign/esign-legalsign-website-seo-geo-analysis.md](../../analyses/esign/esign-legalsign-website-seo-geo-analysis.md)**
- **[analyses/esign/esign-monitoring-snapshot-202606.md](../../analyses/esign/esign-monitoring-snapshot-202606.md)**
- **[concepts/agent-teams-and-orchestration.md](../../concepts/agent-teams-and-orchestration.md)**
- **[concepts/forge-openclaw-framework.md](../../concepts/forge-openclaw-framework.md)**
- **[concepts/toxic-development-system.md](../../concepts/toxic-development-system.md)**
- **[entities/fastsign.md](../../entities/fastsign.md)**
- **[playbooks/bzs-enterprise-trial-sop.md](../../playbooks/bzs-enterprise-trial-sop.md)**
- **[playbooks/esign-competitor-monitoring-mechanism.md](../../playbooks/esign-competitor-monitoring-mechanism.md)**
- **[playbooks/output-file-governance-sop.md](../../playbooks/output-file-governance-sop.md)**
- **[playbooks/seo-geo-starter-kit/README.md](../../playbooks/seo-geo-starter-kit/README.md)**
- **[playbooks/seo-geo-starter-kit/agent.md](../../playbooks/seo-geo-starter-kit/agent.md)**
- **[products/breezy-brain/breezy-brain-roadmap.md](../../products/breezy-brain/breezy-brain-roadmap.md)**
- **[projects/cacafly-api-integration.md](../../projects/cacafly-api-integration.md)**
- **[projects/enzhugong-hospital-aio.md](../../projects/enzhugong-hospital-aio.md)**
- **[skills/ai-product-management.md](../../skills/ai-product-management.md)**
- **[skills/ai-research-agent-design.md](../../skills/ai-research-agent-design.md)**
- **[skills/antigravity-role-switching.md](../../skills/antigravity-role-switching.md)**
- **[skills/harness-engineering-practice.md](../../skills/harness-engineering-practice.md)**
- **[skills/saas-marketing-analytics.md](../../skills/saas-marketing-analytics.md)**
- **[sources/acrobat-enterprise-pricing.md](../../sources/acrobat-enterprise-pricing.md)**
- **[sources/acrobat-pricing.md](../../sources/acrobat-pricing.md)**
- **[sources/agent-skill-creator.md](../../sources/agent-skill-creator.md)**
- **[sources/agent-teams-collaboration.md](../../sources/agent-teams-collaboration.md)**
- **[sources/ai-agent-products-workflow.md](../../sources/ai-agent-products-workflow.md)**
- **[sources/bzs-daily-report-20260522.md](../../sources/bzs-daily-report-20260522.md)**
- **[sources/bzs-dingxin-isv-partnership-v2.md](../../sources/bzs-dingxin-isv-partnership-v2.md)**
- **[sources/bzs-features-v2.md](../../sources/bzs-features-v2.md)**
- **[sources/bzs-search-terms-2026.md](../../sources/bzs-search-terms-2026.md)**
- **[sources/bzs-si-blog-post-draft-v2.md](../../sources/bzs-si-blog-post-draft-v2.md)**
- **[sources/bzs-si-blog-post-draft-v3.md](../../sources/bzs-si-blog-post-draft-v3.md)**
- **[sources/bzs-si-blog-post-draft.md](../../sources/bzs-si-blog-post-draft.md)**
- **[sources/claude-code-ollama-local-deployment.md](../../sources/claude-code-ollama-local-deployment.md)**
- **[sources/docusign-pricing.md](../../sources/docusign-pricing.md)**
- **[sources/forge-openclaw-architecture.md](../../sources/forge-openclaw-architecture.md)**
- **[sources/google-aeo-geo-clarification.md](../../sources/google-aeo-geo-clarification.md)**
- **[sources/karpathy-autoresearch-agent.md](../../sources/karpathy-autoresearch-agent.md)**
- **[sources/moda-energy-registration-rules.md](../../sources/moda-energy-registration-rules.md)**
- **[sources/penpower-milestones-history.md](../../sources/penpower-milestones-history.md)**
- **[sources/pm-breezysign-analytics-reports.md](../../sources/pm-breezysign-analytics-reports.md)**
- **[sources/signnow-pricing.md](../../sources/signnow-pricing.md)**
- **[sources/taiwan-e-signature-enforcement-rules.md](../../sources/taiwan-e-signature-enforcement-rules.md)**
- **[sources/toxic-pm-system-3.md](../../sources/toxic-pm-system-3.md)**
- **[sources/toxic-pm-system-4.md](../../sources/toxic-pm-system-4.md)**
- **[sources/vibe-coding-claude-code.md](../../sources/vibe-coding-claude-code.md)**
- **[sources/zero-code-gemini-studio.md](../../sources/zero-code-gemini-studio.md)**

#### 4.1.2 完全未在首頁註冊且無其他 Wiki 內頁連結 (流失頁面，共 9 個):
- **[analyses/bzb/bzb-concept-market-analysis.md](../../analyses/bzb/bzb-concept-market-analysis.md)**
- **[analyses/bzs/bzs-battle-cards.md](../bzs/bzs-battle-cards.md)**
- **[analyses/esign/esign-pricing-feature-comparison.md](../esign/esign-pricing-feature-comparison.md)**
- **[playbooks/success-story-interview-playbook.md](../../playbooks/success-story-interview-playbook.md)**
- **[skills/eraser-io.md](../../skills/eraser-io.md)**
- **[sources/20260528-saas-daily.md](../../sources/20260528-saas-daily.md)**
- **[sources/aipm-framework-4.md](../../sources/aipm-framework-4.md)**
- **[sources/claude-rules-12-commandments.md](../../sources/claude-rules-12-commandments.md)**
- **[sources/claude-seo-universal-tool.md](../../sources/claude-seo-universal-tool.md)**

## 5. 潛在法規與政策矛盾分析 (Important!)

在對比新修改的「服務條款」與「隱私權政策」後，我們發現了以下**潛在矛盾點**，需要產品與法務進行覆核：

> [!WARNING]
> **個資存取日誌矛盾 (`pii_access.log`)**
> - **現狀政策**：在 2026-05-29 修改的隱私權政策中，已明文**移除**了「pii_access.log 獨立個資存取日誌」的宣告。
> - **規格書規格**：然而，[Product-Spec.md](../../products/breezy-brain/Product-Spec.md) 第 1837 行的安全規範中，仍要求「*系統必須新增獨立於一般 [AGENT_CALL] 日誌之外的『個資存取稽核軌跡日誌』 (/storage/logs/pii_access.log)*」。
> - **建議**：這兩者在技術實施與對外合規宣告上存在衝突。若隱私權政策不再宣告此日誌，產品規格書應評估是否需將該功能拿掉，或者隱私權政策中應予補回以維持誠信。

> [!NOTE]
> **180 天錄影銷毀一致性**
> - 經全文檢索，除已修改的隱私權條款與 `log.md` 外，知識庫其餘分析文件均無殘留「錄影簽 180 天後自動銷毀」的舊時限陳述，政策修改的一致性維持良好。

## 6. 具體改善 Action Items

1. **修正 Frontmatter**：批次補齊 `skills/`、`playbooks/` 及 `sources/` 漏缺的 `type`、`title` 與 `source_file` 欄位。
2. **清除或登錄流失頁面**：
   - 將 `bzs-battle-cards.md` 等有價值的分析登錄於 [index.md](../../index.md)。
   - 移除無用的舊日報草稿以保持目錄清潔。
3. **對齊規格書與合規條款**：
   - 決議是否保留 `pii_access.log` 功能。若移除，需修改 [Product-Spec.md](../../products/breezy-brain/Product-Spec.md) 第 1837 行的文字；若保留，需評估隱私權宣告的揭露方式。

---
## 相關連結
- [內容索引首頁](../../index.md)
- [BreezyBrain 產品需求文件 (Product Spec)](../../products/breezy-brain/Product-Spec.md)
- [操作日誌](../../log.md)
