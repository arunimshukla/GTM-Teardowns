# SquadStack.ai Public Surface Review

## Project Summary

| Field | Detail |
|:--|:--|
| Subject | SquadStack.ai (Squadrun Solutions Private Limited) |
| Type | Public website positioning, evidence, and machine-readable surface review |
| Reviewer | Arunim Shukla |
| Date of review | 7 November 2026 |
| Access | None. All observations come from public pages, files, or rendered page behaviour. |
| Benchmark | SquadStack's published conversational streaming ASR benchmark, used to reconcile the company's own claims |

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

SquadStack publishes 28 case studies, a speech recognition benchmark based on 863 calls, and a trust centre with a subprocessor list and audit records. The benchmark names the models tested, separates raw from semantic word error rate, and reports a statistical tie with Soniox. A buyer can inspect the test behind the result.

The commercial pages apply a different standard. The file SquadStack asks automated readers to treat as canonical gives Choice India a 200% reduction in customer acquisition cost. The case study says 70%. The homepage turns a four-recording listening exercise into a claim that 81% of BFSI leaders thought the agent was human. The ROI calculator takes the buyer's inputs and applies the same conversion lift, acquisition cost reduction, and connectivity target to each scenario.

The gap matters most on the pages a lender or security reviewer reads. The general calling window appears in descriptions of overdue collections without a clear distinction for the regulatory cutoff. The architecture page, engineering article, and subprocessor list leave a buyer to establish which components SquadStack owns and where they run.

The first corrections can be made in copy and configuration. The longer piece of work is to give every material commercial claim a source, a date, and a denominator, then use those fields across the website.

## Project Goals

- Can a buyer trace a headline number back to the case study or test that produced it?
- Do comparison pages identify the models, data, and methods behind their figures?
- Can a lender distinguish the general outbound window from the rules for overdue recovery?
- Do the public architecture and privacy disclosures describe the product a buyer is evaluating?
- Do the pages and files offered to automated readers lead to current evidence?

## Project Targets

| Target | Type |
|:--|:--|
| Homepage, pricing, and ROI calculator | Commercial pages |
| Case-study library and 28 live case studies | Customer evidence |
| Eight SquadStack comparison pages | Competitive framing |
| Turing-test and engineering articles, and the Arth benchmark | Technical evidence |
| Collections guides, trust centre, and public policies | Procurement evidence |
| `/llms.txt`, `/sitemap.xml`, and `/robots.txt` | Machine-readable files |
| Blog and industry templates, the Ayoconnect page, and consent banner | Editorial and page structure |

## Project Coverage

The review compared public copy, server HTML, rendered page content, and the client-side calculator. It reconciled the case-study tiles, checked all eight comparison pages and 150 live blog posts, and read the benchmark, trust centre, and public certificate. The findings describe the pages as checked on 7 November 2026.

The benchmark is used to reconcile what SquadStack reports across its own surfaces. No comparative product testing or independent replication of the benchmark was performed. Customer outcomes, live campaign settings, contractual privacy notices, and gated audit reports were outside the available evidence.

## Maturity Evaluation

| Category | Rating | Comment |
|:--|:--|:--|
| Positioning clarity | Moderate | The managed Voice AI offer is clear. The component and vendor boundaries are harder to establish. |
| Evidence and proof | Moderate | The case studies and benchmark are public. Headline figures frequently lack their source or scope. |
| Competitive framing | Weak | The comparison pages provide figures for named competitors without a source beside them. |
| Commercial evaluation | Weak | The calculator fixes the lift, and the pricing page leaves the commercial and live pilot periods unclear. |
| Procurement evidence | Weak | Collections guidance, the privacy policy, and the document links leave questions a lender has to resolve separately. |
| Machine readability | Weak | The canonical facts file disagrees with the case studies. The sitemap includes noindexed and redirected addresses. |

## Summary of Findings

| ID | Title | Type | Severity |
|:--:|:--|:--|:--|
| 1 | [The canonical facts file disagrees with the case studies](#1-the-canonical-facts-file-disagrees-with-the-case-studies) | Evidence | 🔴 High |
| 2 | [The Turing-test headline misstates what the test measured](#2-the-turing-test-headline-misstates-what-the-test-measured) | Evidence | 🔴 High |
| 3 | [Comparison pages publish figures without a source or method](#3-comparison-pages-publish-figures-without-a-source-or-method) | Competitive framing | 🔴 High |
| 4 | [The published collections window conflicts with recovery-call guidance](#4-the-published-collections-window-conflicts-with-recovery-call-guidance) | Procurement evidence | 🔴 High |
| 5 | [The public architecture leaves vendor and deployment boundaries unclear](#5-the-public-architecture-leaves-vendor-and-deployment-boundaries-unclear) | Positioning | 🔴 High |
| 6 | [The privacy policy describes the legacy crowd-work business](#6-the-privacy-policy-describes-the-legacy-crowd-work-business) | Procurement evidence | 🔴 High |
| 7 | [Case-study tiles mislabel the metrics they present](#7-case-study-tiles-mislabel-the-metrics-they-present) | Evidence | 🟠 Medium |
| 8 | [The ROI calculator applies three fixed assumptions](#8-the-roi-calculator-applies-three-fixed-assumptions) | Commercial evaluation | 🟠 Medium |
| 9 | [The pricing page leaves pilot terms and fees unclear](#9-the-pricing-page-leaves-pilot-terms-and-fees-unclear) | Commercial evaluation | 🟠 Medium |
| 10 | [The public document links leave current audit coverage unclear](#10-the-public-document-links-leave-current-audit-coverage-unclear) | Procurement evidence | 🟠 Medium |
| 11 | [The consent banner links to the wrong host](#11-the-consent-banner-links-to-the-wrong-host) | Page structure | 🟠 Medium |
| 12 | [A blog article carries product ratings readers cannot see](#12-a-blog-article-carries-product-ratings-readers-cannot-see) | Machine readability | 🟠 Medium |
| 13 | [Blog posts display their last edit in the date slot](#13-blog-posts-display-their-last-edit-in-the-date-slot) | Editorial | 🟠 Medium |
| 14 | [Published pages render with missing content or template errors](#14-published-pages-render-with-missing-content-or-template-errors) | Page structure | 🟠 Medium |
| 15 | [The sitemap and crawler files describe different URL sets](#15-the-sitemap-and-crawler-files-describe-different-url-sets) | Machine readability | 🟠 Medium |

## Detailed Findings

### 1. The canonical facts file disagrees with the case studies

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🔴 High** | 🟠 Medium | Evidence | Homepage, `/llms.txt`, and the case-study library |

**Description**

The canonical facts file says Choice India reduced customer acquisition cost by 200%. The case study says 70%. A reduction greater than 100% would take a nonnegative acquisition cost below zero. The same file gives redBus 75% connectivity. The case study reports 83–91% across regional campaigns by June.

The homepage publishes 90% lead connectivity without identifying the population or period behind the figure. Of the 28 live case studies, 21 put an absolute connectivity rate in a hero tile. The median of the printed figures is 85%, taking figures marked with a plus sign at their printed lower bound. Four tiles show 90%. The sample describes the published case studies. The population behind the homepage claim is unspecified.

**Recommendations**

1. Correct the Choice and redBus entries first. Give every headline result a denominator, period, and link to the evidence.
2. Maintain one claims register keyed to the case study or test, and use it to populate the homepage, `llms.txt`, case-study cards, comparison rows, and calculator assumptions.

### 2. The Turing-test headline misstates what the test measured

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🔴 High** | 🟢 Low | Evidence | Homepage, `/llms.txt`, comparison pages, and the Turing-test article |

**Description**

The homepage says 81% of BFSI leaders thought the AI was human. The article describes 1,563 attendees listening to four recordings, two human and two AI. Of those attendees, 1,273, or 81.4%, selected at least one AI recording as human. The article identifies the participants as event attendees.

If each listener had to select exactly two recordings, a random choice would select at least one AI recording in five of the six possible pairs, or 83.3% of the time. On that protocol, 290 listeners, or 18.6%, selected both human recordings. The result depends on the instructions and scoring, which the public account only partly describes.

The September and October rounds had different sample sizes. The Bolna and Yellow.ai pages date the 1,563-person result to November, while the article places it at Global Fintech Fest in October 2025.

**Recommendations**

1. State the measured result and sample directly. Use October 2025 and event attendees for the Global Fintech Fest result.
2. Link the public claim to the test description. Publish the selection instructions, scoring rule, and functional-test results in text if those results are used as evidence.

### 3. Comparison pages publish figures without a source or method

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🔴 High** | 🟠 Medium | Competitive framing | Eight `/squadstack-vs-*` pages and the public benchmark |

**Description**

Six comparison pages put the named competitor below a 25% proof-of-concept success rate. The Convin page gives 15%. The figures appear without a source, a date, or a definition of success. The ASCI Code asks that comparative claims be capable of substantiation.

The Sarvam page gives WER figures of 26.4% and 36.8%. SquadStack's public benchmark gives raw WER of 29.14% for Arth V2 and 33.25% for Saaras v4. It gives semantic WER of 8.85% and 10.84%, respectively. A separate test could produce the first pair. The comparison page gives the buyer no way to establish which test it uses.

**Recommendations**

1. Give each published competitor figure a source, date, and method, and remove figures the company cannot substantiate.
2. Label raw and semantic WER, model versions, and the evaluation corpus. Link to the published benchmark if the comparison uses its results.

### 4. The published collections window conflicts with recovery-call guidance

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🔴 High** | 🟢 Low | Procurement evidence | Homepage FAQ, `/llms.txt`, and the EMI and BNPL guides |

**Description**

The homepage and the BNPL collections guide present a 9:30 a.m. to 8:30 p.m. window in the context of collections. RBI circular RBI/2022-23/108 specifies an 8 a.m. to 7 p.m. window for covered overdue-loan recovery calls. SquadStack's EMI guide also gives 8 a.m. to 7 p.m. Microfinance loans covered by the separate RBI directions are outside the circular's scope.

A lender reading the public pages has no clear account of the window that applies to a covered overdue campaign. The pages establish the copy conflict. The production rules and call logs were outside the review.

**Recommendations**

1. State the applicable overdue recovery cutoff wherever the general outbound window appears in a collections context. Cite the relevant RBI directions and explain any separate campaign classes.
2. Have the product and compliance teams reconcile the public description with the actual campaign configuration.

### 5. The public architecture leaves vendor and deployment boundaries unclear

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🔴 High** | 🟠 Medium | Positioning | Homepage FAQ, `/llms.txt`, engineering article, and trust centre |

**Description**

The homepage says all models run in India. The canonical facts file describes the speech stack as owned. The engineering article describes voices powered by ElevenLabs and SquadStack's own TTS engine, and says it uses multiple language models.

The trust centre lists OpenAI, Google Gemini, and Plivo. Its OpenAI and Gemini entries describe storage in India. The entries leave the location of inference and the workloads routed to each provider unspecified. A buyer comparing in-house components, third-party processing, and data residency has to assemble the answer from three places.

**Recommendations**

1. Publish one architecture account covering the in-house components, third-party services, and the processing and storage regions for each applicable deployment.
2. Align the FAQ, engineering article, comparison pages, and subprocessor list with that account.

### 6. The privacy policy describes the legacy crowd-work business

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🔴 High** | 🟠 Medium | Procurement evidence | `/privacy-policy` and the trust centre |

**Description**

The public policy describes a mobile application that dispatches geographically distributed workers to collect, categorise, moderate, and verify data. It gives no account of call recording or AI processing. It points to the former trust-centre address and promises a last modified date that the page does not display.

The gap is in the public policy. An assessment of statutory duties would also need the applicable commencement dates, SquadStack's role in each workflow, and any customer or caller notices.

**Recommendations**

1. Publish a dated notice for the current business. Identify the relevant processing purposes, retention periods, disclosures, and the applicable contact route.
2. Align the public policy with the trust centre and have counsel review which notices apply to the website, buyers, and people receiving calls.

### 7. Case-study tiles mislabel the metrics they present

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🟠 Medium** | 🟢 Low | Evidence | Insurer, quick-commerce, and Kissht case studies |

**Description**

The insurer case study reports a 60% reduction in renewal costs and labels its hero tile 60% lower CAC. The quick-commerce story reports 40% lower hiring and engagement costs and also labels the tile lower CAC. Kissht's headline describes 82% growth in loan disbursals. Its tile presents the same figure as a conversion lift.

Each page gives the reader two measures under one number. A buyer trying to validate an acquisition or conversion claim needs the same measure on the card and in the underlying case.

**Recommendations**

1. Label each tile with the outcome measured in the study. Apply the same label to the cards reused on the homepage and pricing page.
2. Keep acquisition, renewals, hiring, and disbursals as separate measures in the claims register.

### 8. The ROI calculator applies three fixed assumptions

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🟠 Medium** | 🟢 Low | Commercial evaluation | `/roi-calculator` and `/pricing` |

**Description**

Under the heading “No hidden constants”, the script applies 1.4 times the existing conversions, one-third of the current CAC, and a 90% target connectivity rate. For valid positive inputs, spend becomes `1.4 ÷ 3` of the baseline, or 53.3% lower. Revenue becomes 40% higher. The input labelled current connectivity changes the displayed lift. The revenue calculation uses leads, conversion rate, and deal value.

The result is labelled illustrative. The buyer can change the size of the scenario, while the headline lift and savings are fixed by the model.

**Recommendations**

1. Show the three assumptions next to the inputs and identify where they come from. Label the change from 50% to 90% connectivity as 40 percentage points.
2. Add adjustable assumptions or documented scenarios as a second step, so a buyer can test how the result changes.

### 9. The pricing page leaves pilot terms and fees unclear

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🟠 Medium** | 🟢 Low | Commercial evaluation | `/pricing` and the homepage FAQ |

**Description**

The Pilot tier describes a 90-day commitment. The FAQ gives a live pilot of three to eight weeks. Both periods could apply to the same engagement, but the page leaves their relationship unclear. The fee comparison excludes seat and platform charges. A separate FAQ adds a one-time fee per use case. The page refers to a no-traction guarantee without stating its terms.

The homepage FAQ gives an indicative ₹2–₹5 per-minute range. The pricing page leaves a buyer to find that range elsewhere.

**Recommendations**

1. State the contract commitment and live validation period together. Put the setup fee next to the usage model, and define what the guarantee covers.
2. Carry the same indicative range and qualifications across both pages.

### 10. The public document links leave current audit coverage unclear

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🟠 Medium** | 🟢 Low | Procurement evidence | Footer certificate link and trust-centre resources |

**Description**

The ISO certificate linked in the footer shows a surveillance validity date of 10 November 2025 and a recertification date of 10 November 2027. The trust centre lists a later surveillance document. Its listed SOC 2 Type II report covers 1 November 2024 to 30 October 2025. The report is gated and the public resources list showed no later period or bridge letter.

The footer leads a reviewer to an older copy. The current certificate and audit coverage remain questions for the trust team.

**Recommendations**

1. Link the footer to the current certificate or the maintained trust-centre listing.
2. State the current SOC 2 coverage and the route for requesting the applicable report or bridge letter, if available.

### 11. The consent banner links to the wrong host

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🟠 Medium** | 🟢 Low | Page structure | Cookie banner |

**Description**

The banner's Cookie Policy link has the value `http:///cookie-policy`, which the browser resolves to `http://cookie-policy/`. The footer links to the policy on the company domain. The defect sits in the interface where the visitor is asked to decide about tracking.

**Recommendations**

1. Set the banner link to the published policy URL and check it in a fresh browser session.

### 12. A blog article carries product ratings readers cannot see

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🟠 Medium** | 🟢 Low | Machine readability | Travel article and its structured data |

**Description**

The travel article includes `Product` markup with an `AggregateRating` of 4.9 from 34 ratings. The rendered page shows no rating or review. Google's review snippet guidelines require the aggregate rating to be visible on the marked-up page.

**Recommendations**

1. Remove the product and rating block and retain the article markup. Check other pages using the same template.

### 13. Blog posts display their last edit in the date slot

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🟠 Medium** | 🟢 Low | Editorial | Blog article template |

**Description**

In the 150 live blog posts checked, 135 displayed a date different from `datePublished` and 75 displayed 6 November 2026. The Turing-test article displays 22 October 2026 while its publication metadata gives 5 October 2025. The event described in the article was in October 2025.

The visible date is useful to a reader assessing recency. Without a label or the original date, the reader has to distinguish the event, publication, and last edit from the body of the article.

**Recommendations**

1. Display the original publication date and a separately labelled updated date. Keep both aligned with the structured data.

### 14. Published pages render with missing content or template errors

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🟠 Medium** | 🟢 Low | Page structure | Industries hub, Ayoconnect page, and blog category pages |

**Description**

The Ayoconnect collections page returns successfully and carries a page title. In the rendered check it showed navigation with no main content. The industries hub is listed in `llms.txt` and its navigation insertion script raised an `insertBefore` error. Five of 11 primary-locale blog categories and 12 of 30 subcategories showed an empty main listing.

**Recommendations**

1. Publish the Ayoconnect content or withdraw the empty page. Remove empty archives from the sitemap.
2. Replace the industries hub's homepage-fetch script with the shared navigation when the template is next updated.

### 15. The sitemap and crawler files describe different URL sets

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🟠 Medium** | 🟢 Low | Machine readability | `/sitemap.xml`, `/llms.txt`, and `/robots.txt` |

**Description**

The sitemap lists 1,003 addresses, including 132 pages carrying `noindex` and six redirects. Eight destinations in `llms.txt` redirect, including the old team page and seven guide addresses. The crawler file puts two page exclusions in the wildcard group and gives named agents their own allow groups. Under RFC 9309, a named group takes precedence over the wildcard fallback for an agent that matches it.

The sitemap can be used to identify preferred pages. Redirecting and noindexed entries make that set harder to infer. The crawler configuration also needs to express the intended rules per agent.

**Recommendations**

1. List canonical, indexable pages in the sitemap and link directly to current destinations from `llms.txt`.
2. Apply the intended exclusions in each applicable crawler group and validate the rules against the agents named in the file.

## Consolidated Programme

| Workstream | Findings | Description |
|:--|:--|:--|
| Publish verifiable figures | 1, 2, 3, 7, 8 | Correct the case-study summaries and benchmark wording, then give each commercial figure an owner, period, and source. |
| Clarify the buying terms | 9 | Present the live pilot period, commercial commitment, and setup fee together. |
| Bring procurement evidence up to date | 4, 5, 6, 10, 11 | Align the published recovery rules, architecture, privacy policy, document links, and consent banner. |
| Repair the public templates and indexes | 12, 13, 14, 15 | Expose article dates, remove unsupported markup, repair empty or faulty pages, and align crawler-facing files. |

The first high-impact changes are the Turing-test wording and the collections-window copy. The claims register, benchmark sourcing, architecture description, and privacy notice require coordination across teams. The effort ratings distinguish the immediate public correction from the follow-on work.

## Appendix A: Severity and Effort Definitions

The impact and effort definitions follow [METHODOLOGY.md](./METHODOLOGY.md).

| Severity | Definition |
|:--|:--|
| 🔴 High | A material public claim is contradicted or a buyer cannot verify evidence central to the evaluation. |
| 🟠 Medium | A meaningful proof point, audience path, or commercial detail is weakened. |
| 🟢 Low | The issue concerns structure, attribution, accessibility, or editorial consistency. |
| 🔵 Informational | A relevant observation that is not itself a defect. |

| Effort | Definition |
|:--|:--|
| 🟢 Low | Copy, links, metadata, or configuration. Hours. |
| 🟠 Medium | A new page or reusable component built largely from existing material. Days. |
| 🔴 High | New content, data collection, process, or substantial structural work. Weeks. |

## Appendix B: Sources

| Findings | Sources |
|:--|:--|
| 1, 7 | [Canonical facts file](https://www.squadstack.ai/llms.txt), [case-study library](https://www.squadstack.ai/case-study), [Choice India](https://www.squadstack.ai/case-study/success-story-with-choice), [redBus](https://www.squadstack.ai/case-study/success-story-with-redbus-feedback-collection), [insurer](https://www.squadstack.ai/case-study/success-story-with-leading-general-insurer), [quick commerce](https://www.squadstack.ai/case-study/success-story-with-quick-commerce-platforms), and [Kissht](https://www.squadstack.ai/case-study/kissht-success-story) |
| 2, 3 | [Homepage](https://www.squadstack.ai/), [Turing-test article](https://www.squadstack.ai/blog/turing-test), comparisons for [Bolna](https://www.squadstack.ai/squadstack-vs-bolna), [Yellow.ai](https://www.squadstack.ai/squadstack-vs-yellow), [Convin](https://www.squadstack.ai/squadstack-vs-convin), [Gnani.ai](https://www.squadstack.ai/squadstack-vs-gnani), [Nurix](https://www.squadstack.ai/squadstack-vs-nurix), [GreyLabs](https://www.squadstack.ai/squadstack-vs-greylabs), [Sarvam](https://www.squadstack.ai/squadstack-vs-sarvam), and [Ringg](https://www.squadstack.ai/squadstack-vs-ringg), [ASR benchmark](https://huggingface.co/datasets/Squadstack/conversational-streaming-asr-benchmark), and [ASCI Code](https://www.ascionline.in/the-asci-code/) |
| 4 | [RBI circular RBI/2022-23/108](https://rbi.org.in/Scripts/NotificationUser.aspx?Id=12378&Mode=0), [EMI guide](https://www.squadstack.ai/blog/emi-reminder-calls-designing-compliant-ai-voice-scripts-for-india), and [BNPL guide](https://www.squadstack.ai/blog/ai-voice-agents-for-bnpl-collections-and-emi-upsell) |
| 5, 6, 10, 11 | [Engineering article](https://www.squadstack.ai/blog/inside-the-humanoid-ai-agent-stack), [subprocessors](https://trust.squadstack.ai/subprocessors), [trust-centre resources](https://trust.squadstack.ai/resources), [privacy policy](https://www.squadstack.ai/privacy-policy), [footer certificate](https://25336320.fs1.hubspotusercontent-eu1.net/hubfs/25336320/E-Copy-Squadrun%20Solutions%20Pvt%20Ltd-ISMS-CA.pdf), and [cookie policy](https://www.squadstack.ai/cookie-policy) |
| 8, 9 | [ROI calculator](https://www.squadstack.ai/roi-calculator), [pricing](https://www.squadstack.ai/pricing), and [homepage FAQ](https://www.squadstack.ai/) |
| 12, 13 | [Travel article](https://www.squadstack.ai/ai-agent-stack/conversational-ai-in-travel-a-smarter-way-to-serve-customers), [Google review snippet guidelines](https://developers.google.com/search/docs/appearance/structured-data/review-snippet), [blog](https://www.squadstack.ai/blog), and [Turing-test article](https://www.squadstack.ai/blog/turing-test) |
| 14, 15 | [Ayoconnect page](https://www.squadstack.ai/ayoconnectxsquadstack), [industries hub](https://www.squadstack.ai/industry/industries), [sitemap](https://www.squadstack.ai/sitemap.xml), [crawler rules](https://www.squadstack.ai/robots.txt), and [RFC 9309](https://www.rfc-editor.org/rfc/rfc9309#section-2.2.1) |

## Appendix C: Confidence and Limitations

Copy, metadata, URLs, and code are observations of the public surface on the date checked. Counts reflect the stated set of pages. The calculator result follows from its published client-side code. The Turing-test chance baseline assumes exactly two selections per listener.

Customer outcomes, buyer behaviour, campaign execution, inference location, and current audit status require evidence beyond these pages. The observations about regulatory and procurement copy identify what a buyer can establish from the public record.

The corrections process is documented in [METHODOLOGY.md](./METHODOLOGY.md).
