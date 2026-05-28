---
title: "WikiLLM 知識庫健康檢查與 Lint 優化報告"
type: analysis
analysis_type: synthesis
tags: [Lint, 健康檢查, 知識庫管理, 合規審查]
date_created: 2026-05-29
date_updated: 2026-05-29
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
- **[breezy-brain-integration-flow.md](../products/breezy-brain/breezy-brain-integration-flow.md)**: 於第 8769 位元組位置含有無效的二進位字元 ``。該字元目前已成功剔除，檔案已恢復 100% 正確編碼。

## 2. YAML Frontmatter 格式缺失

部分檔案未包含標準 frontmatter 或缺少關鍵欄位，不符合 `AGENTS.md` 元數據規範。

### 目錄: `analyses/`
- **[antigravity-aipm-framework.md](../analyses/antigravity-aipm-framework.md)**: Missing required frontmatter field: title
- **[antigravity-aipm-framework.md](../analyses/antigravity-aipm-framework.md)**: Missing required frontmatter field: type
### 目錄: `playbooks/seo-geo-starter-kit/`
- **[agent.md](../playbooks/seo-geo-starter-kit/agent.md)**: Missing required frontmatter field: title
- **[agent.md](../playbooks/seo-geo-starter-kit/agent.md)**: Missing required frontmatter field: type
- **[README.md](../playbooks/seo-geo-starter-kit/README.md)**: Missing required frontmatter field: title
- **[README.md](../playbooks/seo-geo-starter-kit/README.md)**: Missing required frontmatter field: type
### 目錄: `skills/`
- **[ai-research-agent-design.md](../skills/ai-research-agent-design.md)**: Missing required frontmatter field: title
- **[ai-research-agent-design.md](../skills/ai-research-agent-design.md)**: Missing required frontmatter field: type
- **[antigravity-role-switching.md](../skills/antigravity-role-switching.md)**: Missing required frontmatter field: title
- **[antigravity-role-switching.md](../skills/antigravity-role-switching.md)**: Missing required frontmatter field: type
### 目錄: `sources/`
- **[acrobat-enterprise-pricing.md](../sources/acrobat-enterprise-pricing.md)**: Source page missing 'source_file' field
- **[agent-skill-creator.md](../sources/agent-skill-creator.md)**: Source page missing 'source_file' field
- **[agent-teams-collaboration.md](../sources/agent-teams-collaboration.md)**: Source page missing 'source_file' field
- **[ai-agent-products-workflow.md](../sources/ai-agent-products-workflow.md)**: Source page missing 'source_file' field
- **[aipm-framework-4.md](../sources/aipm-framework-4.md)**: Missing required frontmatter field: type
- **[bzs-dingxin-isv-partnership-v2.md](../sources/bzs-dingxin-isv-partnership-v2.md)**: Missing required frontmatter field: title
- **[bzs-dingxin-isv-partnership-v2.md](../sources/bzs-dingxin-isv-partnership-v2.md)**: Missing required frontmatter field: type
- **[bzs-features-v2.md](../sources/bzs-features-v2.md)**: Missing required frontmatter field: title
- **[bzs-features-v2.md](../sources/bzs-features-v2.md)**: Missing required frontmatter field: type
- **[claude-code-ollama-local-deployment.md](../sources/claude-code-ollama-local-deployment.md)**: Missing required frontmatter field: type
- **[claude-rules-12-commandments.md](../sources/claude-rules-12-commandments.md)**: Missing required frontmatter field: type
- **[claude-seo-universal-tool.md](../sources/claude-seo-universal-tool.md)**: Missing required frontmatter field: type
- **[e-signature-tech-overview.md](../sources/e-signature-tech-overview.md)**: Source page missing 'source_file' field
- **[forge-openclaw-architecture.md](../sources/forge-openclaw-architecture.md)**: Source page missing 'source_file' field
- **[taiwan-e-signature-law-2024.md](../sources/taiwan-e-signature-law-2024.md)**: Source page missing 'source_file' field
- **[toxic-pm-system-3.md](../sources/toxic-pm-system-3.md)**: Source page missing 'source_file' field
- **[toxic-pm-system-4.md](../sources/toxic-pm-system-4.md)**: Source page missing 'source_file' field
- **[vibe-coding-claude-code.md](../sources/vibe-coding-claude-code.md)**: Source page missing 'source_file' field
- **[zero-code-gemini-studio.md](../sources/zero-code-gemini-studio.md)**: Source page missing 'source_file' field
### 目錄: `topics/`
- **[karpathy-autoresearch.md](../topics/karpathy-autoresearch.md)**: Missing required frontmatter field: title
- **[karpathy-autoresearch.md](../topics/karpathy-autoresearch.md)**: Missing required frontmatter field: type

## 3. 失效內部連結 / 缺失頁面 (Broken Links & Missing Pages)

✅ 無失效內部連結。

## 4. 孤立頁面與未註冊頁面

### 4.1 孤立頁面 (Orphaned Pages)
> 孤立頁面定義：除了 `index.md` 之外，沒有任何其他 Wiki 檔案連結至它。

#### 4.1.1 已在首頁註冊但無其他 Wiki 內頁交叉連結 (共 46 個):
- **[analyses/ai-search-geo-empirical-report.md](../analyses/ai-search-geo-empirical-report.md)**
- **[analyses/breezybrain-spec-analysis-report.md](../analyses/breezybrain-spec-analysis-report.md)**
- **[analyses/bzs-blog-marketing-posts-202605.md](../analyses/bzs-blog-marketing-posts-202605.md)**
- **[analyses/bzs-bu-role-based-tasklist.md](../analyses/bzs-bu-role-based-tasklist.md)**
- **[analyses/bzs-saas-marketing-synthesis-2026.md](../analyses/bzs-saas-marketing-synthesis-2026.md)**
- **[analyses/bzs-saas-ops-csm-reconciliation-202605.md](../analyses/bzs-saas-ops-csm-reconciliation-202605.md)**
- **[analyses/bzs-saas-plan-sales-comparison.md](../analyses/bzs-saas-plan-sales-comparison.md)**
- **[analyses/esign-competitor-seo-geo-analysis-20260525.md](../analyses/esign-competitor-seo-geo-analysis-20260525.md)**
- **[analyses/esign-competitor-seo-geo-analysis-20260527.md](../analyses/esign-competitor-seo-geo-analysis-20260527.md)**
- **[analyses/legalsign-website-seo-geo-analysis.md](../analyses/legalsign-website-seo-geo-analysis.md)**
- **[concepts/agent-teams-and-orchestration.md](../concepts/agent-teams-and-orchestration.md)**
- **[concepts/forge-openclaw-framework.md](../concepts/forge-openclaw-framework.md)**
- **[concepts/toxic-development-system.md](../concepts/toxic-development-system.md)**
- **[playbooks/seo-geo-starter-kit/README.md](../playbooks/seo-geo-starter-kit/README.md)**
- **[playbooks/seo-geo-starter-kit/agent.md](../playbooks/seo-geo-starter-kit/agent.md)**
- **[projects/cacafly-api-integration.md](../projects/cacafly-api-integration.md)**
- **[projects/enzhugong-hospital-aio.md](../projects/enzhugong-hospital-aio.md)**
- **[projects/huaxing-publishing-onboarding.md](../projects/huaxing-publishing-onboarding.md)**
- **[skills/ai-product-management.md](../skills/ai-product-management.md)**
- **[skills/ai-research-agent-design.md](../skills/ai-research-agent-design.md)**
- **[skills/antigravity-role-switching.md](../skills/antigravity-role-switching.md)**
- **[skills/harness-engineering-practice.md](../skills/harness-engineering-practice.md)**
- **[sources/acrobat-enterprise-pricing.md](../sources/acrobat-enterprise-pricing.md)**
- **[sources/acrobat-pricing.md](../sources/acrobat-pricing.md)**
- **[sources/agent-skill-creator.md](../sources/agent-skill-creator.md)**
- **[sources/agent-teams-collaboration.md](../sources/agent-teams-collaboration.md)**
- **[sources/ai-agent-products-workflow.md](../sources/ai-agent-products-workflow.md)**
- **[sources/bzs-dingxin-isv-partnership-v2.md](../sources/bzs-dingxin-isv-partnership-v2.md)**
- **[sources/bzs-features-v2.md](../sources/bzs-features-v2.md)**
- **[sources/bzs-search-terms-2026.md](../sources/bzs-search-terms-2026.md)**
- **[sources/bzs-si-blog-post-draft-v2.md](../sources/bzs-si-blog-post-draft-v2.md)**
- **[sources/bzs-si-blog-post-draft-v3.md](../sources/bzs-si-blog-post-draft-v3.md)**
- **[sources/bzs-si-blog-post-draft.md](../sources/bzs-si-blog-post-draft.md)**
- **[sources/claude-code-ollama-local-deployment.md](../sources/claude-code-ollama-local-deployment.md)**
- **[sources/docusign-pricing.md](../sources/docusign-pricing.md)**
- **[sources/forge-openclaw-architecture.md](../sources/forge-openclaw-architecture.md)**
- **[sources/google-aeo-geo-clarification.md](../sources/google-aeo-geo-clarification.md)**
- **[sources/karpathy-autoresearch-agent.md](../sources/karpathy-autoresearch-agent.md)**
- **[sources/moda-energy-registration-rules.md](../sources/moda-energy-registration-rules.md)**
- **[sources/penpower-milestones-history.md](../sources/penpower-milestones-history.md)**
- **[sources/signnow-pricing.md](../sources/signnow-pricing.md)**
- **[sources/taiwan-e-signature-enforcement-rules.md](../sources/taiwan-e-signature-enforcement-rules.md)**
- **[sources/toxic-pm-system-3.md](../sources/toxic-pm-system-3.md)**
- **[sources/toxic-pm-system-4.md](../sources/toxic-pm-system-4.md)**
- **[sources/vibe-coding-claude-code.md](../sources/vibe-coding-claude-code.md)**
- **[sources/zero-code-gemini-studio.md](../sources/zero-code-gemini-studio.md)**

#### 4.1.2 完全未在首頁註冊且無其他 Wiki 內頁連結 (流失頁面，共 9 個):
- **[analyses/breezy-brain-concept-market-analysis.md](../analyses/breezy-brain-concept-market-analysis.md)**
- **[analyses/bzs-battle-cards.md](../analyses/bzs-battle-cards.md)**
- **[analyses/esign-pricing-feature-comparison.md](../analyses/esign-pricing-feature-comparison.md)**
- **[playbooks/success-story-interview-playbook.md](../playbooks/success-story-interview-playbook.md)**
- **[skills/eraser-io.md](../skills/eraser-io.md)**
- **[sources/20260528-saas-daily.md](../sources/20260528-saas-daily.md)**
- **[sources/aipm-framework-4.md](../sources/aipm-framework-4.md)**
- **[sources/claude-rules-12-commandments.md](../sources/claude-rules-12-commandments.md)**
- **[sources/claude-seo-universal-tool.md](../sources/claude-seo-universal-tool.md)**

## 5. 潛在法規與政策矛盾分析 (Important!)

在對比新修改的「服務條款」與「隱私權政策」後，我們發現了以下**潛在矛盾點**，需要產品與法務進行覆核：

> [!WARNING]
> **個資存取日誌矛盾 (`pii_access.log`)**
> - **現狀政策**：在 2026-05-29 修改的隱私權政策中，已明文**移除**了「pii_access.log 獨立個資存取日誌」的宣告。
> - **規格書規格**：然而，[Product-Spec.md](../products/breezy-brain/Product-Spec.md) 第 1837 行的安全規範中，仍要求「*系統必須新增獨立於一般 [AGENT_CALL] 日誌之外的『個資存取稽核軌跡日誌』 (/storage/logs/pii_access.log)*」。
> - **建議**：這兩者在技術實施與對外合規宣告上存在衝突。若隱私權政策不再宣告此日誌，產品規格書應評估是否需將該功能拿掉，或者隱私權政策中應予補回以維持誠信。

> [!NOTE]
> **180 天錄影銷毀一致性**
> - 經全文檢索，除已修改的隱私權條款與 `log.md` 外，知識庫其餘分析文件均無殘留「錄影簽 180 天後自動銷毀」的舊時限陳述，政策修改的一致性維持良好。

## 6. 具體改善 Action Items

1. **修正 Frontmatter**：批次補齊 `skills/`、`playbooks/` 及 `sources/` 漏缺的 `type`、`title` 與 `source_file` 欄位。
2. **清除或登錄流失頁面**：
   - 將 `bzs-battle-cards.md` 等有價值的分析登錄於 [index.md](../index.md)。
   - 移除無用的舊日報草稿以保持目錄清潔。
3. **對齊規格書與合規條款**：
   - 決議是否保留 `pii_access.log` 功能。若移除，需修改 [Product-Spec.md](../products/breezy-brain/Product-Spec.md) 第 1837 行的文字；若保留，需評估隱私權宣告的揭露方式。

---
## 相關連結
- [內容索引首頁](../index.md)
- [BreezyBrain 產品需求文件 (Product Spec)](../products/breezy-brain/Product-Spec.md)
- [操作日誌](../log.md)
