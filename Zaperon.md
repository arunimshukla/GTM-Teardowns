# Zaperon Public Surface Review

> **Lead finding.** Zaperon’s reporting guide calls its audit trail **tamper-proof**. The guide does not explain how changes are prevented or detected, or which parts of the record the protection covers. [Read the finding](#1-the-reporting-guide-leaves-the-audit-trail-integrity-and-siem-path-unclear).

## Project Summary

| Field | Detail |
|:--|:--|
| Subject | [Zaperon](https://www.zaperon.com/) |
| Type | Public website and security evidence review |
| Reviewer | Arunim Shukla |
| Date of review | 29 October 2026, rechecked 7 November 2026 |
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

The October review began with the marketing site's server response. The homepage and a sampled VPN article returned the same title and lacked readable page content in the initial HTML. The homepage also lacked share tags and described the company in SSE terms while the funding coverage described a wider AI governance platform.

The November check found readable HTML and Open Graph metadata on the homepage. Its description now includes Shadow AI governance. The sampled VPN address returns 404, so the recheck establishes the current homepage state. The earlier homepage observations are historical and are excluded from the finding totals.

The two findings that remain are in the reporting guide. It makes a strong integrity claim without a mechanism, and it names regulatory regimes without specifying how the documented report data supports them.

## Project Goals

- Does the initial response identify and describe the current business?
- Can a security reviewer verify the mechanism behind the reporting claims?
- Can an Indian regulated buyer map the retention and export details to a specific requirement?

## Project Targets

| Target | Type |
|:--|:--|
| [Marketing homepage](https://www.zaperon.com/) and the legacy VPN article address | Website and page source |
| [October seed-round coverage](https://indianstartupnews.com/funding/cybersecurity-startup-zaperon-raises-rs-7-crore-to-launch-enterprise-grade-ai-security-frameworks-12612842) | External positioning reference |
| [Real-time Reports guide](https://docs.zaperon.com/real-time-reports) | Product documentation |
| [CERT-In directions of 28 April 2022](https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf) | Primary regulatory source |

## Project Coverage

The original review sampled two marketing URLs and the reporting guide. The 7 November check repeated those requests and compared the current homepage against the earlier observations. The guide's published mechanism, export path, and stated retention are the scope of the open findings.

## Maturity Evaluation

| Category | Rating | Comment |
|:--|:--|:--|
| Positioning and metadata | Improved | The rechecked homepage carries page content, social metadata, and AI governance wording. |
| Reporting evidence | Weak | The guide describes the outcomes of the audit trail without the integrity control. |
| Procurement evidence | Weak | The retention statement gives a maximum. The named regulatory requirements are left to the buyer to map. |

## Summary of Findings

| ID | Title | Type | Severity |
|:--|:--|:--|:--|
| 1 | [The reporting guide leaves the audit-trail integrity and SIEM path unclear](#1-the-reporting-guide-leaves-the-audit-trail-integrity-and-siem-path-unclear) | Product evidence | 🔴 High |
| 2 | [The retention statement cannot be mapped to the listed requirements](#2-the-retention-statement-cannot-be-mapped-to-the-listed-requirements) | Procurement evidence | 🟠 Medium |

## Detailed Findings

### 1. The reporting guide leaves the audit-trail integrity and SIEM path unclear

| Severity | Effort to fix | Type | Target |
|:---:|:---:|:---:|:---:|
| **🔴 High** | 🟢 Low | Product evidence | [Real-time Reports guide](https://docs.zaperon.com/real-time-reports) |

**Description**

The guide describes the audit trail as tamper-proof. It does not identify how changes are prevented or detected, or which part of the record the protection covers. The same guide refers to integration with Splunk, Microsoft Sentinel, and IBM QRadar. The path it documents is CSV export and ingestion into those tools.

A security reviewer needs to know the control behind the integrity claim and whether getting events into a SIEM is a file handoff or a continuous integration. The guide establishes the documented path. Other integrations or controls may exist.

**Recommendations**

1. Name the integrity mechanism, the record it covers, and any relevant limits. Use narrower wording if the public guide cannot substantiate the absolute claim.
2. Describe CSV export and ingestion explicitly. Link any separate connector or streaming setup that is supported.

### 2. The retention statement cannot be mapped to the listed requirements

| Severity | Effort to fix | Type | Target |
|:---:|:---:|:---:|:---:|
| **🟠 Medium** | 🟠 Medium | Procurement evidence | [Real-time Reports guide](https://docs.zaperon.com/real-time-reports) and [CERT-In directions](https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf) |

**Description**

The guide names RBI, SEBI, GDPR, HIPAA, and SOC 2 in its discussion of regulatory and audit needs. It gives report retention as up to six months without mapping the statement to a specific control or direction.

CERT-In's directions include a rolling 180-day requirement for ICT system logs for covered entities. A maximum of six months for product reports establishes neither the guaranteed retention for those logs nor the relevant storage or retrieval arrangements. A buyer has to establish whether the reports cover the logs it is responsible for.

**Recommendations**

1. Map each relevant direction or control to the report fields, log types, export path, and minimum retention the product supports.
2. State the applicable location and retrieval arrangements for the logs. Separate product support from the customer's own obligations.

## Consolidated Programme

| Workstream | Findings | Description |
|:--|:--|:--|
| Make reporting claims verifiable | 1 | Put the integrity mechanism and documented SIEM data path next to the reporting claims. |
| Map reports to specific requirements | 2 | Publish the controls, coverage, and retention details a buyer can check during procurement. |

## Appendix A: Severity and Effort Definitions

Impact and effort follow [METHODOLOGY.md](./METHODOLOGY.md). High-impact findings concern material claims or evidence central to a buyer decision. Medium-impact findings concern a weakened proof point or path. Low effort covers changes normally measured in hours. Medium effort covers changes normally measured in days.

## Appendix B: Sources

| Findings | Sources |
|:--|:--|
| 1 | [Real-time Reports](https://docs.zaperon.com/real-time-reports) |
| 2 | [Real-time Reports](https://docs.zaperon.com/real-time-reports), [CERT-In directions and FAQs](https://cert-in.org.in/Directions70B.jsp), [Directions of 28 April 2022](https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf) |

## Appendix C: Confidence and Limitations

The homepage recheck applies to the sampled address. It establishes that the October homepage problems no longer reproduce there. The live guide establishes what Zaperon documents. Product behaviour, log integrity, connector availability, and compliance were outside the review.

Revalidation sources include the [Zaperon homepage](https://www.zaperon.com/) and [October seed-round coverage](https://indianstartupnews.com/funding/cybersecurity-startup-zaperon-raises-rs-7-crore-to-launch-enterprise-grade-ai-security-frameworks-12612842).

The corrections process is documented in [METHODOLOGY.md](./METHODOLOGY.md).
