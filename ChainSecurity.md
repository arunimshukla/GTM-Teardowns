# ChainSecurity Public Surface Review

## Project Summary

| Field | Detail |
|:--|:--|
| Subject | ChainSecurity (Decentralized Security AG) |
| Type | Public website positioning and evidence review |
| Reviewer | Arunim Shukla |
| Date of review | 3 August 2026 |
| Benchmark | Trail of Bits |
| Access | None. All observations come from public pages. |

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

ChainSecurity holds a strong position in the smart contract security market. The firm has specialised expertise, a credible academic origin, recognised researchers, a distinctive audit process, and high profile engagements including Aave V4.

The problem identified in this review is not a shortage of evidence. It is that the strongest evidence ChainSecurity owns is difficult to find, inconsistently presented, or held inside PDF files and code repositories that the website does not link to.

The result is that a prospective client has to assemble the firm's credibility without help. The pages reviewed do not make clear how much work ChainSecurity has completed, how its audit process differs from anyone else's, what services it sells, who performs the research, or what happens after an audit request is submitted. Each of those gaps sits at a point where an institutional or protocol buyer is forming a judgement about expertise and commercial fit.

Trail of Bits publishes 620 audits, 946 publications, 200 or more repositories, and an
operating history since 2012 in a fixed bar at the top of every page. Each figure links to
a filtered view of the underlying library. ChainSecurity publishes no comparable figure
anywhere. A visitor cannot determine whether the archive holds 40 audits or 400 without
clicking through pages of five.

Most of the recommendations in this report do not require a rebrand or a rebuilt website.
The largest immediate gains come from organising and exposing material the firm already
owns.

## Project Goals

The review was framed by the following questions:

* Can a prospective client determine the volume and recency of ChainSecurity's work from
  the website alone?
* Does the website present the firm's audit methodology as a differentiator?
* Is the evidence contained in published audit reports available in a form a buyer can scan?
* Is the path from first visit to audit request clear, and does it set expectations?
* Are the firm's research, tools, and people connected to its commercial pages?

## Project Targets

| Target | Address | Type |
|:--|:--|:--|
| Positioning page | `/why` | Website |
| Institutional page | `/institutional` | Website |
| About page | `/about` | Website |
| Research index | `/blog` | Website |
| Research post | `/blog/auditors-wishlist-for-ethereum-security-in-2026` | Website |
| Audit library | `/smart-contract-audit-reports`, pages 1 and 2 | Website |
| Audit detail page | `/security-audit/aave-v4` | Website |
| Testimonials | `/testimonials` | Website |
| Request form | `/request-audit` | Website |
| Code repositories | `github.com/ChainSecurity` | Repository |
| Benchmark | `trailofbits.com/services/blockchain/` | Website |
| Benchmark | `trailofbits.com/services/research-and-development/` | Website |

## Project Coverage

The review covered public website positioning, the structure of the audit library and its
detail pages, research content, the audit request path, and the firm's public code
repositories. Pages were fetched and their content extracted on 3 August 2026.

The following were not assessed: the technical quality of published audit reports, page
speed, mobile rendering, social media accounts, website analytics, internal commercial data,
and competitors other than the selected benchmark.

Trail of Bits was chosen as a benchmark for how a security firm presents evidence. It is not
a proxy for ChainSecurity's competitive landscape. OpenZeppelin, Spearbit and Cantina,
Zellic, and Sherlock compete more directly for the same protocol budgets.

## Maturity Evaluation

| Category | Rating | Comment |
|:--|:--|:--|
| Positioning clarity | $\textcolor{#E5484D}{\textsf{High}}$ | The specialism is clear. The service list and the founding story are not. |
| Evidence and proof | $\textcolor{#E8830C}{\textsf{Weak}}$ | The evidence exists inside reports and repositories. The website does not present it. |
| Competitive framing | $\textcolor{#E8830C}{\textsf{Weak}}$ | No comparison with alternatives appears on any reviewed page. |
| Conversion path | $\textcolor{#E8830C}{\textsf{Weak}}$ | The request page asks the buyer for work and offers nothing in exchange. |
| Content standards | $\textcolor{#2EA043}{\textsf{Moderate}}$ | The research is strong. It is undated, unattributed, and cites other firms' tools. |
| Editorial standards | $\textcolor{#2EA043}{\textsf{Moderate}}$ | Individual pages are well written. Consistency across pages is poor. |
| Accessibility | $\textcolor{#E8830C}{\textsf{Weak}}$ | Client logos carry no alternative text. |
| Technical credibility | $\textcolor{#4493F8}{\textsf{Satisfactory}}$ | Public repositories and compiler level work exist and are genuinely uncommon. |

## Summary of Findings

| ID | Title | Type | Severity |
|:--:|:--|:--|:--|
| 1 | [The website publishes no record of completed work](#1-the-website-publishes-no-record-of-completed-work) | Evidence | 🔴 High |
| 2 | [Audit detail pages omit the findings data held in the reports](#2-audit-detail-pages-omit-the-findings-data-held-in-the-reports) | Evidence | 🔴 High |
| 3 | [The audit request page asks for estimation work and offers nothing in return](#3-the-audit-request-page-asks-for-estimation-work-and-offers-nothing-in-return) | Conversion path | 🔴 High |
| 4 | [An audit page reports a review in progress with no date](#4-an-audit-page-reports-a-review-in-progress-with-no-date) | Editorial | 🟠 Medium |
| 5 | [The firm describes its own origin three different ways](#5-the-firm-describes-its-own-origin-three-different-ways) | Positioning | 🟠 Medium |
| 6 | [The audit methodology has no page of its own](#6-the-audit-methodology-has-no-page-of-its-own) | Positioning | 🟠 Medium  |
| 7 | [A third party credential appears once, inside a single research post](#7-a-third-party-credential-appears-once-inside-a-single-research-post) | Evidence | 🟠 Medium |
| 8 | [The most valuable engagement is absent from the homepage](#8-the-most-valuable-engagement-is-absent-from-the-homepage) | Evidence | 🟠 Medium |
| 9 | [The flagship research post names competitor tools exclusively](#9-the-flagship-research-post-names-competitor-tools-exclusively) | Content strategy | 🟠 Medium |
| 10 | [Public code repositories are not linked from the website](#10-public-code-repositories-are-not-linked-from-the-website) | Evidence | 🟠 Medium |
| 11 | [No page describes what the firm sells](#11-no-page-describes-what-the-firm-sells) | Page structure | 🟠 Medium |
| 12 | [Client logos carry no alternative text](#12-client-logos-carry-no-alternative-text) | Accessibility | 🟠 Medium |
| 13 | [The research index shows no publication dates](#13-the-research-index-shows-no-publication-dates) | Editorial | 🟢 Low |
| 14 | [Research posts carry no author attribution](#14-research-posts-carry-no-author-attribution) | Evidence | 🟢 Low |
| 15 | [No pages exist for the ecosystems the firm covers](#15-no-pages-exist-for-the-ecosystems-the-firm-covers) | Page structure | 🟢 Low |
| 16 | [The flagship research post contradicts its own structure](#16-the-flagship-research-post-contradicts-its-own-structure) | Editorial | 🟢 Low |

## Detailed Findings

### 1. The website publishes no record of completed work

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🔴 High** | 🟢 Low | Evidence | Homepage, `/why`, `/smart-contract-audit-reports` |

**Description**

No count of completed audits, clients, or years of operation appears on any reviewed page.
The audit library lists five entries at a time behind a button reading SHOW MORE AUDITS. A visitor who wants to know the size of the archive has to click repeatedly and count.

Trail of Bits places four figures in a fixed bar visible on every page: 620 audits, 946 publications, 200 or more repositories, and an operating history beginning in 2012. Each figure is a link into a filtered view of the corresponding library.

A count is the cheapest form of proof available to a professional services firm. In this case the underlying data already exists inside the content management system, because the library pages are generated from it.

**Recommendations**

1. Publish a single line of figures across the site. A suggested form is: number of audits since 2017, number of clients, and number of ETHSecurity Badge holders on staff. Link each figure to the evidence behind it.

2. Generate these figures from the content management system so they update without manual intervention, and add filtered library views so each figure is clickable.

### 2. Audit detail pages omit the findings data held in the reports

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🔴 High** | 🟠 Medium | Evidence | `/security-audit/aave-v4` and the audit page template |

**Description**

The Aave V4 page is the most commercially valuable page in the audit library. It contains a client logo, a heading, a link to download a PDF, a testimonial, a two sentence description of the client, and a prose summary.

It does not contain a review date, severity counts, a findings table, a scope statement, a line count, a duration or effort figure, the commit reference reviewed, or the names of the auditors. The prose mentions version 0.5.7, but as prose rather than as a labelled field.

Trail of Bits publishes severity, difficulty, and an exploitation scenario for each finding, along with a maturity evaluation of the codebase, all as readable web pages rather than as downloadable files.

Every item missing from the ChainSecurity page already exists inside the PDF report. This is a task of extracting data that has already been produced.

**Recommendations**

1. Add a summary block to the audit page template holding the review date, scope, line count, severity counts, and resolution status. Populate the Aave V4 page first and use it as the template for the rest of the library.

2. Publish findings tables as web pages rather than only as downloadable files, so the content is readable without a download and is retrievable by search engines.

### 3. The audit request page asks for estimation work and offers nothing in return

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🔴 High** | 🟠 Medium | Conversion path | `/request-audit` |

**Description**

The entire body copy of the page reads: "Please answer the questions below and click the Submit button." Below it are five required fields, including project name, a free text description, an estimated line count, and a requested delivery date.

The page does not state a response time, describe the engagement models available, explain how to count lines of code despite requiring that number, or say what happens after submission.

The equivalent Trail of Bits page offers a free hour with an engineer, described as a working session rather than a sales call.

One page asks the buyer to perform unpaid estimation work before any contact. The other offers the buyer expert time before any commitment. That difference affects which firm a buyer contacts first.

**Recommendations**

1. Add a stated response time, a short description of what happens after submission, and a definition of how line counts should be calculated. Make the delivery date field optional.

2. Offer a low commitment first step, such as a scoping call with an engineer, and make that the primary action on the page.

### 4. An audit page reports a review in progress with no date

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🟠 Medium** | 🟢 Low | Editorial | `/security-audit/aave-v4` |

**Description**

The Aave V4 page states that version 0.5.7 of the code is still under review. No date appears anywhere on the page. The library index carries a date, but the detail page does not.

A reader has no way to establish whether that statement was written four days ago or fourteen months ago. The statement appears on the page carrying the firm's most recognisable client name.

**Recommendations**

1. Add a publication date and a last updated date to every audit detail page.

2. Add an automated check that flags any page containing an in progress status that has not been updated within a set period.

### 5. The firm describes its own origin three different ways

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🟠 Medium** | 🟢 Low | Positioning | `/why`, `/institutional`, X profile |

**Description**

Three descriptions of the firm's origin appear across three surfaces:

| Surface | Statement |
|:--|:--|
| `/why` | Founded by ETH Zurich researchers and refined within PwC Switzerland |
| `/institutional` | A PwC Switzerland spin-off |
| X profile | Born at ETH, ex-PwC |

The verifiable sequence is that the company was incorporated in October 2017 as an ETH Zurich spin-off, the team was acquired by PwC Switzerland in January 2020, and the business now operates as Decentralized Security AG.

A firm founded at a university and later acquired is a different entity from a firm spun out of an accounting practice. Two of the three descriptions are inaccurate, in different directions.

**Recommendations**

1. Write one paragraph describing the origin and history, and use it on every surface without variation.

2. Consider removing the PwC reference entirely. The academic origin and the audit record carry the credibility on their own, and the accounting firm reference invites a question about the nature of the current business that has no useful answer.

### 6. The audit methodology has no page of its own

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🟠 Medium** | 	🟠 Medium | Positioning | `/why` |

**Description**

ChainSecurity runs a process consisting of Independent Dual Audits, a Warden Role, an Audit Defense, and a Fixes Review. Two auditors work independently to avoid arriving at the same conclusions, an internal reviewer challenges their findings, and the team defends the report before it is issued.

No other firm reviewed in this category describes a comparable process publicly.

The description currently sits inside a horizontal card carousel at the foot of `/why`. It has no dedicated address, no diagram, and no comparison with standard practice. It is not linked from the homepage, from `/institutional`, or from `/request-audit`.

The strongest differentiator on the property cannot be linked to.

**Recommendations**

1. Give the methodology its own page with a permanent address, and link to it from the homepage, the institutional page, and the audit request page.

2. Add a diagram of the process and a short comparison with how single reviewer audits are conducted, so the value of the additional steps is legible to a buyer who has not commissioned an audit before.

### 7. A third party credential appears once, inside a single research post

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🟠 Medium** | 🟢 Low | Evidence | `/blog/auditors-wishlist-for-ethereum-security-in-2026` |

**Description**

Seven members of staff hold the ETHSecurity Badge. This is stated once, in the first paragraph of one research post, in the middle of a sentence.

The badge is awarded by a third party rather than self declared. In the Ethereum security funding round held between 23 April and 14 May 2026, donations directed to badge holders were matched at four times the standard rate from a shared pool of approximately 637 ETH, which was the largest such pool assembled to date. The round distributed funding across 134 projects. Two hundred people hold the badge worldwide, and 172 of them took part.

The correct framing is concentration rather than scarcity. Seven holders at a firm of roughly 23 people is close to four percent of everyone who holds the badge, working in one office.

The published summary of that funding round separately credits ChainSecurity with entering the round as a full team. That is independent corroboration currently going unused.

**Recommendations**

1. State the credential on the homepage, on `/why`, on the company LinkedIn page, and next to each badge holder on `/about`. State the worldwide total alongside the firm's count.

2. Verify the count of current employees holding the badge before each republication. The claim depends on staff who may leave.

### 8. The most valuable engagement is absent from the homepage

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🟠 Medium** | 🟢 Low | Evidence | Homepage |

**Description**

The homepage features the WBTC Solana Bridge, Circle Gateway, and Pendle Boros engagements. The Aave V4 audit is not featured on the homepage and does not appear in the trusted by strip, despite carrying an attributed quotation from Stani Kulechov, founder and chief executive of Aave Labs.

That combination of a recognised client name and an attributed quotation from a named executive is the strongest single piece of proof the firm holds. It currently sits two clicks from the entry page.

**Recommendations**

1. Feature the Aave V4 engagement and the attributed quotation on the homepage, and add the client to the trusted by strip.

2. Establish a rule for what qualifies for homepage placement, based on client recognition and the strength of the accompanying evidence, and review placements quarterly.

### 9. The flagship research post names competitor tools exclusively

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🟠 Medium** | 🟢 Low | Content strategy | `/blog/auditors-wishlist-for-ethereum-security-in-2026` |

**Description**

The post, published 4 May 2026, is a strong and clearly argued piece of writing. It names the tools of the trade: Echidna and Medusa, both produced by Trail of Bits, Foundry, produced by Paradigm, and Tenderly, a commercial vendor, which is linked.

It names no ChainSecurity tools. The firm's own deployment validation tooling, the Compound Proposal Decoder, and Securify are all absent.

The firm's most widely read piece of research currently promotes the tooling of a direct competitor and links to a paid vendor.

**Recommendations**

1. Add the firm's own tools to the post where they are relevant, with links to the repositories.

2. Add a step to the research review process requiring that the firm's own tools be considered for inclusion wherever tooling is discussed.

### 10. Public code repositories are not linked from the website

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🟠 Medium** | 🟢 Low | Evidence | Site footer, navigation, `github.com/ChainSecurity` |

**Description**

The organisation account holds 24 repositories and has 70 followers. It is not linked from the footer, from the navigation, or from any reviewed page. The footer carries links to X and LinkedIn only.

For a firm selling to engineering teams, the public code is a primary source of credibility. It is currently unreachable from the commercial site.

**Recommendations**

1. Add the repository link to the footer alongside the existing social links.

2. Feature specific repositories on the relevant service and research pages, so the tooling appears where it supports a commercial argument.

### 11. No page describes what the firm sells

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🟠 Medium** | 🟠 Medium | Page structure | Site wide |

**Description**

No page on the site sets out the firm's services. The three cards on `/institutional`, covering Audits, System Design Advisory, and C-Level Workshops, are the only service descriptions present, and they sit behind a page addressed to a specific segment.

A visitor arriving from a search result or a referral has no page to read that answers what the
firm does.

Trail of Bits maintains a dedicated services page for blockchain work.

**Recommendations**

1. Create a services page listing each offering with a short description and a link to relevant published work.

2. Give each service its own page, so that individual services can rank in search and be linked to directly in commercial conversations.

### 12. Client logos carry no alternative text

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🟠 Medium** | 🟢 Low | Accessibility | Homepage trusted by strip |

**Description**

The logos in the trusted by strip extract as raw file paths and the bare numbers 1, 2, 3, 4, 6, 7. No alternative text is set on any of them.

This makes the client list unreadable to screen readers, invisible to search engines, and unavailable to any system that reads the page as text rather than rendering it. The sequence also skips 5, which suggests a removed image rather than a deliberate set.

**Recommendations**

1. Set alternative text on every logo to the client's name.

2. Add an automated check to the publishing process that fails when an image is published without alternative text.

### 13. The research index shows no publication dates

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🟢 Low** | 🟢 Low | Editorial | `/blog` |

**Description**

Dates appear on individual post pages but not on the index. As a result, a disclosure from 2021 concerning ERC-1155, an article from 2022 written before the Ethereum merge, and a post from 2026 concerning EIP-7702 appear in one undifferentiated list.

A related instance appears in the Curve post mortem, which opens by stating that the team informed Curve on 14 April, without giving the year, on a page carrying no date. That leaves a significant disclosure unverifiable.

For a research publication, an undated post cannot be cited.

**Recommendations**

1. Display publication dates on the index and add the year to any date referenced in body copy.

2. Add a review date to older posts and mark superseded material, so that readers can judge currency without checking the underlying facts themselves.

### 14. Research posts carry no author attribution

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🟢 Low** | 🟢 Low | Evidence | `/blog` |

**Description**

No post carries an author name. Trail of Bits attributes every talk and paper to a named
researcher.

For a firm whose commercial argument rests on the expertise of specific individuals and on lowstaff turnover, anonymous research removes the connection between the writing and the people being sold. It also weakens the credential described in finding 7, because there is no page linking a named individual to a body of published work.

**Recommendations**

1. Add author names to all posts, and link each name to a profile on `/about`.

2. Give each researcher a profile page listing their published work, talks, and credentials.

### 15. No pages exist for the ecosystems the firm covers

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🟢 Low** | 🔴 High | Page structure | Site wide |

**Description**

The audit library already carries tags for Solana, Starknet, zero knowledge systems, compilers, TON, TRON, account abstraction, and real world assets. This represents genuine depth across multiple execution environments, including work on the Vyper compiler and on Fuel's Sway compiler, which few firms can claim.

No page collects this work by ecosystem. Trail of Bits maintains ecosystem sections, each
linking to the relevant published assessments.

**Recommendations**

1. Create pages for the two or three ecosystems where the firm has the deepest record, each listing the relevant audits.

2. Generate ecosystem pages from the existing library tags, so the pages populate automatically as new work is published.

### 16. The flagship research post contradicts its own structure

| Severity | Effort to fix | Type | Target |
|:--|:--|:--|:--|
| **🟢 Low** | 🟢 Low | Editorial | `/blog/auditors-wishlist-for-ethereum-security-in-2026` |

**Description**

The post is framed around five critical security improvements and then numbers its final section as item six. The summary bullets do not match the section headings. The fifth heading reads "Account compromises and signing flows" while the corresponding summary bullet refers towallet usability.

The issue is small. It appears in a research publication whose argument concerns rigour.

**Recommendations**

1. Correct the numbering and align the summary bullets to the headings.

2. Add a structural check to the editorial process covering heading numbering and summary alignment.

## Consolidated Programme

The 16 findings group into five workstreams.

| Workstream | Findings | Description |
|:--|:--|:--|
| Publish verifiable figures | 1, 7 | Counts of completed work, clients, operating history, and staff credentials, each linked to evidence |
| Standardise audit pages | 2, 4 | A findings summary block on the audit template, populated first on the Aave V4 page |
| Present the methodology | 6 | A dedicated page, a diagram, and links from every commercial page |
| Clarify services and the request path | 3, 11 | A services page, and a request page that sets expectations and offers a first step |
| Connect research to people and tools | 9, 10, 13, 14, 15, 16 | Author names, dates, repository links, ecosystem pages, and editorial consistency |

Findings 5, 8, and 12 are single corrections that do not require a programme.

The low effort items are: publishing figures, adding dates and author names, linking the repositories, correcting the origin description, setting alternative text, featuring the Aave V4 engagement, and correcting the editorial inconsistencies. The higher effort items are the audit page template, the methodology page, the services page, and the ecosystem pages.

The objective is that a technical or institutional buyer can establish the firm's experience, its differentiation, and how to engage it, within a few minutes, from evidence that is current, attributable, and verifiable.

## Appendix A: Severity and Effort Definitions

| Severity | Definition |
|:--|:--|
| 🔴 High | The issue causes a prospective buyer to lose confidence, contradicts a public statement by the company, or blocks the path to enquiry. |
| 🟠 Medium | Nothing is broken. The strongest available evidence or differentiator is not visible to buyers. |
| 🟢 Low | Structure, attribution, or editorial consistency. The cost accumulates rather than being felt immediately. |
| 🔵 Informational | An observation that is not a defect. |

| Effort | Definition |
|:--|:--|
| 🟢 Low | Copy, links, or metadata. Hours. |
| 🟠 Medium | A new page or template, using content that already exists. Days. |
| 🔴 High | New content, new structure, or new data collection. Weeks. |

## Appendix B: Sources

* ChainSecurity: `/why`, `/institutional`, `/about`, `/blog`,
  `/blog/auditors-wishlist-for-ethereum-security-in-2026`, `/smart-contract-audit-reports`,
  `/security-audit/aave-v4`, `/testimonials`, `/request-audit`
* `github.com/ChainSecurity`
* `trailofbits.com/services/blockchain/`
* `trailofbits.com/services/research-and-development/`
* Published results of the Ethereum security funding round, May 2026

## Appendix C: Confidence and Limitations

Observations of page content are recorded as they appeared on 3 August 2026 and are stated with high confidence.

The staff count of approximately 23 is taken from public listings and changes over time. It should be confirmed before the concentration claim in finding 7 is published.

This review has no access to website analytics. It can establish that a page fails to present available evidence. It cannot establish how any page performs. A page can be poorly constructed and still convert. The argument made throughout is that these pages ask the buyer to perform work the seller should have performed.
