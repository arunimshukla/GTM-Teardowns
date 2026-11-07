# Arcanna.ai Public Surface Review

## Project Summary

| Field | Detail |
|:--|:--|
| Subject | [Arcanna.ai](https://arcanna.ai/) |
| Type | Public website positioning, product evidence, and machine-readable surface review |
| Reviewer | Arunim Shukla |
| Date of review | 5 November 2026, with selected checks repeated on 7 November 2026 |
| Access | None. The review uses public pages, documentation, and page source. |

## Contents

1. [Project Summary](#project-summary)
2. [Executive Summary](#executive-summary)
3. [Project Goals](#project-goals)
4. [Project Targets](#project-targets)
5. [Project Coverage](#project-coverage)
6. [Maturity Evaluation](#maturity-evaluation)
7. [Summary of Findings](#summary-of-findings)
8. [Detailed Findings](#detailed-findings)
9. [Consolidated Programme](#consolidated-programme)
10. [Appendix A: Severity and Effort Definitions](#appendix-a-severity-and-effort-definitions)
11. [Appendix B: Sources](#appendix-b-sources)
12. [Appendix C: Confidence and Limitations](#appendix-c-confidence-and-limitations)

## Executive Summary

Arcanna gives a security operations buyer three reasons to evaluate the platform. Decisions can be governed by confidence thresholds, investigations can run alongside those decisions, and deployments can be adapted to the customer's environment. The site also publishes enough detail to test how those claims are presented.

The strongest proof is in the case studies. Orange identifies different accuracy results for different sources. Accenture names the measured change in triage time. The homepage publishes broader figures without showing their basis, and one Global SOC story presents two incompatible time totals without explaining the difference.

The larger gap is between the marketing description and the deployment questions a SOC lead has to answer. The confidence bands differ between pages. Offline installation is documented, while the public agentic setup instructions describe network dependencies. Arcanna can close much of the gap with evidence it already owns.

## Project Goals

- Can a buyer recover the scope and denominator behind each headline result?
- Do the marketing pages and user guide explain the same decision and deployment rules?
- Can a technical evaluator reach the documented paths for testing and installing the platform?
- Do the site's crawler-facing files lead to current evidence?

## Project Targets

| Target | Type |
|:--|:--|
| [Homepage](https://arcanna.ai/), [demo](https://arcanna.ai/demo), and platform pages | Commercial and product claims |
| [Orange](https://arcanna.ai/case-studies/orange), [Accenture](https://arcanna.ai/case-studies/global-mssp-decision-intelligence), [Global SOC](https://arcanna.ai/case-studies/global-soc-cuts-false-positives-meets-slas), and [TAQA](https://arcanna.ai/case-studies/taqa) case studies | Customer evidence |
| [Decision models](https://arcanna.ai/docs/decision-models), [assistant](https://docs.arcanna.ai/docs/ai-assistant/setup/), [integrations](https://arcanna.ai/platform/integrations), and marketplace docs | Product documentation |
| [Blog article](https://arcanna.ai/blog/mssp-ai-soc) source, [sitemap](https://arcanna.ai/sitemap.xml), and crawler files | Machine-readable surface |

## Project Coverage

The original review checked the marketing site and user guide on 5 November. This version retains the findings for which the public sources or representative examples could be checked again on 7 November. It compares published claims with their underlying descriptions and separates source-HTML checks from what a browser can render.

## Maturity Evaluation

| Category | Rating | Comment |
|:--|:--|:--|
| Evidence and proof | Moderate | The named cases provide useful scope. The commercial pages frequently omit it. |
| Product and deployment clarity | Weak | Confidence bands and deployment dependencies take several pages to reconcile. |
| Evaluation paths | Moderate | Marketplace and installation guides are public. The marketing site does little to direct evaluators to them. |
| Machine readability | Weak | Examples of useful customer and editorial evidence are missing from the sitemap or initial HTML. |

## Summary of Findings

| ID | Title | Type | Severity |
|:--|:--|:--|:--|
| 1 | [The homepage publishes four figures without a stated basis](#1-the-homepage-publishes-four-figures-without-a-stated-basis) | Evidence | 🔴 High |
| 2 | [The Accenture result changes between the case study and the facts file](#2-the-accenture-result-changes-between-the-case-study-and-the-facts-file) | Evidence | 🔴 High |
| 3 | [The Global SOC case study gives two unreconciled time totals](#3-the-global-soc-case-study-gives-two-unreconciled-time-totals) | Evidence | 🔴 High |
| 4 | [Decision confidence bands differ between public pages](#4-decision-confidence-bands-differ-between-public-pages) | Product evidence | 🔴 High |
| 5 | [The demo gives a broader hallucination claim than the product description](#5-the-demo-gives-a-broader-hallucination-claim-than-the-product-description) | Product evidence | 🔴 High |
| 6 | [The air-gapped investigation path is missing from the public setup guide](#6-the-air-gapped-investigation-path-is-missing-from-the-public-setup-guide) | Product documentation | 🟠 Medium |
| 7 | [The integration grid gives uneven paths to setup evidence](#7-the-integration-grid-gives-uneven-paths-to-setup-evidence) | Product documentation | 🟠 Medium |
| 8 | [The marketing site leaves out a documented evaluation route](#8-the-marketing-site-leaves-out-a-documented-evaluation-route) | Conversion path | 🟠 Medium |
| 9 | [Older blog articles leave their body out of the initial HTML](#9-older-blog-articles-leave-their-body-out-of-the-initial-html) | Machine readability | 🟠 Medium |
| 10 | [The sitemap omits live customer evidence](#10-the-sitemap-omits-live-customer-evidence) | Machine readability | 🟠 Medium |

## Detailed Findings

### 1. The homepage publishes four figures without a stated basis

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🔴 High** | 🟠 Medium | Evidence | [Homepage](https://arcanna.ai/), [Orange](https://arcanna.ai/case-studies/orange) and [Accenture](https://arcanna.ai/case-studies/global-mssp-decision-intelligence) case studies |

**Description**

The homepage presents response time of at most 10 seconds, seven hours per day reclaimed, 95% alert reduction, and 99% decision accuracy. The block gives no customer, measurement period, denominator, or source link.

Orange reports 96% decision accuracy on SIEM and EDR server detections and 80% for its primary SIEM. Those results have identifiable scopes. The 99% headline could come from a different evaluation. A buyer cannot trace it from the page.

**Recommendations**

1. Give each headline figure a source, measurement window, scope, and denominator.
2. Use the named Orange figures where the page is describing that deployment. State the basis for any aggregate or internal benchmark.

### 2. The Accenture result changes between the case study and the facts file

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🔴 High** | 🟢 Low | Evidence | [Accenture case study](https://arcanna.ai/case-studies/global-mssp-decision-intelligence) and [facts file](https://arcanna.ai/llms.txt) |

**Description**

The case study reports P1/P2 triage falling from 20 minutes to three minutes, an 85% reduction. The facts file links to that case under a headline giving a threefold improvement. The case study's published times give a baseline-to-result ratio of about 6.7 to one. The file gives no separate scope for its figure.

**Recommendations**

1. Use the 20-to-three-minute result in the file and the commercial summaries, with the case-study link.
2. If the threefold figure describes a different measure or population, label it and link its source.

### 3. The Global SOC case study gives two unreconciled time totals

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🔴 High** | 🟢 Low | Evidence | [Global SOC case study](https://arcanna.ai/case-studies/global-soc-cuts-false-positives-meets-slas) |

**Description**

The page associates 4,546 offloaded cases with 1,136 analyst hours saved. Applying its stated 18-to-three-minute change to those cases gives 68,190 minutes, or about 1,136.5 hours. Elsewhere on the same page, the triage result is accompanied by a total of 4,185 minutes, or 69.75 hours.

The totals can describe different populations or reporting windows. The page supplies no reconciliation that lets a buyer tell.

**Recommendations**

1. Give each total its own population, period, and calculation. Correct the figure if both statements refer to the same sample.

### 4. Decision confidence bands differ between public pages

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🔴 High** | 🟠 Medium | Product evidence | [Decision Layer](https://arcanna.ai/platform/decision-layer), [Decision Models](https://arcanna.ai/docs/decision-models), and [confidence guide](https://docs.arcanna.ai/docs/concepts/confidence-in-decisions/) |

**Description**

The Decision Layer gives autonomous execution at 90–100%, human validation at 70–89%, and recommendations below 70%. The Decision Models page starts its review band at 80%, leaving 70–79% unassigned in the displayed policy. The user guide separately labels scores below 60% low confidence and scores from 60% high confidence. A score interpretation can coexist with an execution policy. The pages leave that distinction to the reader.

**Recommendations**

1. Publish the default or example execution policy by product version, including the 70–79% band and what customers can configure.
2. Explain how a score category, an outlier flag, and an execution threshold relate. Link the marketing example to that explanation.

### 5. The demo gives a broader hallucination claim than the product description

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🔴 High** | 🟢 Low | Product evidence | [Demo](https://arcanna.ai/demo), [Investigation Layer](https://arcanna.ai/platform/investigation-layer), and [facts file](https://arcanna.ai/llms.txt) |

**Description**

The demo promises “Zero Hallucinations”. The Investigation Layer is described as governed GenAI, while the facts file makes a narrower statement about free-form generation in decision paths. The demo copy applies across the product and does not identify which workflow or output it means.

**Recommendations**

1. Scope the demo claim to the decision path and describe the safeguard that supports it.
2. Describe the controls and limits of generated investigation output separately.

### 6. The air-gapped investigation path is missing from the public setup guide

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🟠 Medium** | 🟠 Medium | Product documentation | [TAQA case study](https://arcanna.ai/case-studies/taqa) and [AI Assistant setup](https://docs.arcanna.ai/docs/ai-assistant/setup/) |

**Description**

The TAQA story describes an isolated on-premises deployment alongside agentic investigations. The public assistant setup guide describes internet access to model providers and MCP servers for its documented workflow. These pages may describe different configurations. An evaluator cannot determine the supported offline arrangement, required local services, or feature limits from the two pages.

**Recommendations**

1. Document a supported offline reference configuration if one is available. Identify model endpoints, MCP services, network dependencies, and features that differ from a connected deployment.
2. Link it from the case study and state the scope of the case deployment.

### 7. The integration grid gives uneven paths to setup evidence

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🟠 Medium** | 🟠 Medium | Product documentation | [Integration grid](https://arcanna.ai/platform/integrations), [Swimlane](https://docs.arcanna.ai/docs/integrations/swimlane/), and [Azure Sentinel guide](https://docs.arcanna.ai/docs/implementation-tutorials/azure-sentinel/) |

**Description**

Swimlane is presented as an integration on the marketing site. Its user-guide page remains a placeholder. The Azure Sentinel tutorial shows what a usable path looks like. It walks an evaluator through the integration. The grid does not distinguish between a working setup guide, a marketing brief, and a placeholder.

**Recommendations**

1. Link each tile to its best available setup evidence and label its status. Make a brief or example visibly distinct from an implementation guide.
2. Complete the Swimlane page or point the tile to a verified implementation resource.

### 8. The marketing site leaves out a documented evaluation route

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🟠 Medium** | 🟢 Low | Conversion path | [Decision Layer](https://arcanna.ai/platform/decision-layer) and installation guides for [AWS](https://docs.arcanna.ai/docs/admin-guide/aws-marketplace-installation/), [Azure](https://docs.arcanna.ai/docs/admin-guide/azure-marketplace-installation/), and [Google Cloud](https://docs.arcanna.ai/docs/admin-guide/gcp-marketplace-installation/) |

**Description**

The Decision Layer mentions AWS and Google Cloud marketplace availability. The public guide also documents Azure Marketplace and says the Azure image starts with a Community licence, with Azure infrastructure billed separately. A technical evaluator on the marketing page has to locate that route in the docs.

**Recommendations**

1. Link the AWS, Azure, and Google Cloud guides from the deployment section.
2. Explain the scope of the Community licence and any infrastructure charges next to the evaluation route.

### 9. Older blog articles leave their body out of the initial HTML

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🟠 Medium** | 🟠 Medium | Machine readability | Blog article template, sampled on the [MSSP](https://arcanna.ai/blog/mssp-ai-soc) and [Fortinet](https://arcanna.ai/blog/fortinet-ai-soc) articles |

**Description**

The multi-tenant MSSP article returns its title and introductory material in the initial HTML. The body arrives with client-side JavaScript. The Fortinet article returns the full text in its initial response. A reader that fetches HTML without running scripts can retrieve the evidence from one article and only the introduction from the other.

**Recommendations**

1. Use the full-text rendering approach already visible on the Fortinet article for older posts.
2. Check a sample against the raw response so the headline, body, and links are available together.

### 10. The sitemap omits live customer evidence

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🟠 Medium** | 🟢 Low | Machine readability | [Sitemap](https://arcanna.ai/sitemap.xml), [robots.txt address](https://arcanna.ai/robots.txt) (404 at review), and [Orange](https://arcanna.ai/case-studies/orange) and [TAQA](https://arcanna.ai/case-studies/taqa) case studies |

**Description**

The sitemap lists 75 addresses. The Orange and TAQA case studies and the Fortinet article are live and absent. The marketing site's `robots.txt` returns HTTP 404. A missing robots file does not block crawling. The sitemap omissions matter because they leave relevant proof out of the company's stated discovery set.

**Recommendations**

1. Generate the sitemap from the current indexable route set and include the named case studies.
2. Use canonical destinations and serve a plain-text robots file if the company wants to publish crawler rules or a sitemap directive.

## Consolidated Programme

| Workstream | Findings | Description |
|:--|:--|:--|
| Reconcile commercial claims | 1–3, 5 | Tie the homepage, demo, facts file, and case studies to scoped evidence. |
| Clarify implementation | 4, 6–8 | Explain decision thresholds, deployment dependencies, integrations, and evaluation routes. |
| Publish the evidence in retrievable form | 9, 10 | Render article bodies and include live customer proof in the sitemap. |

## Appendix A: Severity and Effort Definitions

Impact and effort follow [METHODOLOGY.md](./METHODOLOGY.md). High-impact findings concern material claims or evidence central to a buyer decision. Medium-impact findings concern a weakened proof point or path. Low effort covers changes normally measured in hours. Medium effort covers changes normally measured in days.

## Appendix B: Sources

| Findings | Sources |
|:--|:--|
| 1 | [Homepage](https://arcanna.ai/), [Orange](https://arcanna.ai/case-studies/orange), [Accenture](https://arcanna.ai/case-studies/global-mssp-decision-intelligence) |
| 2 | [Accenture](https://arcanna.ai/case-studies/global-mssp-decision-intelligence), [Facts file](https://arcanna.ai/llms.txt) |
| 3 | [Global SOC case study](https://arcanna.ai/case-studies/global-soc-cuts-false-positives-meets-slas) |
| 4 | [Decision Layer](https://arcanna.ai/platform/decision-layer), [Decision Models](https://arcanna.ai/docs/decision-models), [Confidence in decisions](https://docs.arcanna.ai/docs/concepts/confidence-in-decisions/) |
| 5 | [Demo](https://arcanna.ai/demo), [Investigation Layer](https://arcanna.ai/platform/investigation-layer), [Facts file](https://arcanna.ai/llms.txt) |
| 6 | [TAQA](https://arcanna.ai/case-studies/taqa), [AI Assistant setup](https://docs.arcanna.ai/docs/ai-assistant/setup/) |
| 7 | [Integrations](https://arcanna.ai/platform/integrations), [Swimlane](https://docs.arcanna.ai/docs/integrations/swimlane/), [Azure Sentinel tutorial](https://docs.arcanna.ai/docs/implementation-tutorials/azure-sentinel/) |
| 8 | [Decision Layer](https://arcanna.ai/platform/decision-layer), [AWS guide](https://docs.arcanna.ai/docs/admin-guide/aws-marketplace-installation/), [Azure guide](https://docs.arcanna.ai/docs/admin-guide/azure-marketplace-installation/), [Google Cloud guide](https://docs.arcanna.ai/docs/admin-guide/gcp-marketplace-installation/) |
| 9 | [MSSP article](https://arcanna.ai/blog/mssp-ai-soc), [Fortinet article](https://arcanna.ai/blog/fortinet-ai-soc) |
| 10 | [Sitemap](https://arcanna.ai/sitemap.xml), [Robots address](https://arcanna.ai/robots.txt), [Orange](https://arcanna.ai/case-studies/orange), [TAQA](https://arcanna.ai/case-studies/taqa), [Fortinet article](https://arcanna.ai/blog/fortinet-ai-soc) |

## Appendix C: Confidence and Limitations

The findings describe what a public reader could establish on the dates recorded. Customer results are company-published. No model, hosted deployment, or customer environment was tested. The source-HTML comparisons establish what the initial response includes. Search rankings, crawler execution, and sales effects remain outside scope.

The corrections process is documented in [METHODOLOGY.md](./METHODOLOGY.md).
