# Massive Computing Inc. Generative Engine Surface Review

> **Lead finding.** Massive published two `llms.txt` files. One used the domain name and the other used the company name. **Neither file linked to the other.** [Read the finding](#1-two-llmstxt-files-exist-and-disagree-on-the-name-of-the-company).

## Project Summary

| Field          | Detail                                                                    |
| -------------- | --------------------------------------------------------------------------- |
| Subject        | [Massive](https://www.joinmassive.com/), `joinmassive.com/llms.txt` and the wider machine-readable surface  |
| Type           | Generative engine optimisation review                                      |
| Reviewer       | Arunim Shukla                                                              |
| Date of review | 11 August 2026                                                             |
| Access         | None. Every observation comes from publicly fetchable files and pages.     |
| Companion      | [Massive Computing Inc. Public Surface Review](./Massive.md), July 2026    |

## Contents

1. [Project Summary](#project-summary)
2. [Executive Summary](#executive-summary)
3. [Scope](#scope)
4. [The Format Under Review](#the-format-under-review)
5. [Composition of the File](#composition-of-the-file)
6. [Maturity Evaluation](#maturity-evaluation)
7. [Summary of Findings](#summary-of-findings)
8. [Detailed Findings](#detailed-findings)
9. [Appendix A: Severity and Effort Definitions](#appendix-a-severity-and-effort-definitions)
10. [Appendix B: Sources](#appendix-b-sources)
11. [Appendix C: Confidence and Limitations](#appendix-c-confidence-and-limitations)
12. [Appendix D: Evidence Check and Measurement](#appendix-d-evidence-check-and-measurement)
13. [Appendix E: Proposed File Structure](#appendix-e-proposed-file-structure)

## Executive Summary

Massive publishes two files telling automated readers what the company is. They do not agree on the name of the company.

The better of the two sits on the documentation subdomain and cannot be reached from the apex domain. The file a reader arrives at instead lists 186 addresses. Nine tenths of them repeat their own link text. None of them is documentation.

This format is a summary rather than an index, which means whatever the file is weighted towards is what the company has said it is. This one is weighted towards other companies. Pages about other firms' products outnumber pages about Massive's own by 11 to one. The largest single block is a catalogue of integrations for identity concealment browsers, and it sits below a sentence claiming the company is entirely ethical.

The compliance summary omits the audit named on the product page. The partner earnings figure would require 300,000 to 1.2 million consenting devices at the rates in the linked FAQ. A product line named in the opening sentence has no link in the file.

The immediate copy and link fixes are estimated in hours.

## Scope

The 11 August 2026 review examined the raw [marketing](https://www.joinmassive.com/llms.txt) and [documentation](https://docs.joinmassive.com/llms.txt) files, their linked and omitted pages across Massive’s public hosts, and the [MCP repository](https://github.com/joinmassive/mcp-server). The counts describe the files at the time of review. Network performance, pricing competitiveness, assistant retrieval, and referral attribution were outside scope. The July FAQ finding is referenced without counting it again.

## The Format Under Review

[The llms.txt format](https://llmstxt.org/) was proposed in September 2024 by Jeremy Howard of Answer.AI. It is a plain text file at the root of a domain. The format specifies a heading carrying the name of the project, a summary in a block quote, sections containing lists of links written as a name, an address and a note, and a final section named Optional marking material a reader may skip when room is short.

Two properties of the format matter here and are frequently missed.

The first is that it is a summary rather than an index. A sitemap is exhaustive by design and is read that way. This format is a statement of what the publisher considers representative. Whatever the file is weighted towards is what the publisher has said the company is.

The second is that the note after each link exists so a reader can decide whether fetching the page is worth the cost. A note that repeats the link text carries no information. It spends context to say nothing.

Adoption across the major assistants is uneven and undocumented. The file is inexpensive insurance on a rising curve rather than a lever with a known effect. That argues for doing the work properly and against overstating what it returns.

## Composition of the File

| Section                              | Links   | Percent |
| ------------------------------------ | ------- | ------- |
| Blog articles                        | 68      | 36.6    |
| Web data marketplace                 | 30      | 16.1    |
| Implementation guides                | 26      | 14.0    |
| Glossary                             | 26      | 14.0    |
| Solutions                            | 11      | 5.9     |
| Products                             | 5       | 2.7     |
| Startups programme                   | 5       | 2.7     |
| Monetisation kit                     | 3       | 1.6     |
| Case studies                         | 3       | 1.6     |
| Legal                                | 3       | 1.6     |
| About, press, careers                | 3       | 1.6     |
| Launch checklist, questions, contact | 3       | 1.6     |
| Total                                | 186     | 100     |

Two ratios follow from the table, and between them they are the review.

Pages about other companies' products, being 30 marketplace listings and 26 browser integrations, total 56 links. Pages about Massive's own products total 5. That is 11 to one.

Dictionary definitions total 26. Customer evidence totals 3. That is nearly 9 to one.

## Maturity Evaluation

| Category                   | Rating                                       | Comment                                                                             |
| -------------------------- | -------------------------------------------- | ------------------------------------------------------------------------------------- |
| Specification adherence    | $\textcolor{#E8830C}{\textsf{Weak}}$         | Both files use part of the format. Neither uses all of it, and they fail in opposite ways. |
| Entity resolution          | $\textcolor{#F85149}{\textsf{Poor}}$         | Three names for the company across four of its own machine-readable surfaces.       |
| Documentation exposure     | $\textcolor{#F85149}{\textsf{Poor}}$         | Around 150 documentation pages and three interface specifications are absent.       |
| Cross-surface consistency  | $\textcolor{#F85149}{\textsf{Poor}}$         | Nine published contradictions between sources the company controls.                 |
| Evidence and proof         | $\textcolor{#F85149}{\textsf{Poor}}$         | The strongest credential is omitted. Two regulations are described as certifications. |
| Content weighting          | $\textcolor{#E8830C}{\textsf{Weak}}$         | Pages about other companies outnumber pages about this one by 11 to one.            |
| Recency signalling         | $\textcolor{#E8830C}{\textsf{Weak}}$         | No dates anywhere. A third of the library labels itself as belonging to last year.  |
| Documentation file quality | $\textcolor{#4493F8}{\textsf{Satisfactory}}$ | The file on the documentation subdomain is well built. It cannot be reached from the apex domain. |

## Summary of Findings

| ID | Title                                                                                                                                                                                                            | Type                | Severity        |
| -- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | --------------- |
| 1  | [Two `llms.txt` files exist and disagree on the name of the company](#1-two-llmstxt-files-exist-and-disagree-on-the-name-of-the-company)                                                                          | Machine readability | 🔴 High          |
| 2  | [The marketing facts file omits the documentation](#2-the-marketing-facts-file-omits-the-documentation)                                                                          | Machine readability | 🔴 High          |
| 3  | [The compliance summary omits the audit the company holds and calls two regulations certifications](#3-the-compliance-summary-omits-the-audit-the-company-holds-and-calls-two-regulations-certifications)          | Evidence            | 🔴 High          |
| 4  | [The partner earnings figure is disproved by a page listed in the same file](#4-the-partner-earnings-figure-is-disproved-by-a-page-listed-in-the-same-file)                                                        | Evidence            | 🔴 High          |
| 5  | [The product list contradicts the file's own summary sentence](#5-the-product-list-contradicts-the-files-own-summary-sentence)                                                                                     | Positioning         | 🔴 High          |
| 6  | [The file is weighted towards evasion tooling and against the claim the business rests on](#6-the-file-is-weighted-towards-evasion-tooling-and-against-the-claim-the-business-rests-on)                             | Positioning         | 🔴 High          |
| 7  | [Three product facts are published with different values on surfaces the company controls](#7-three-product-facts-are-published-with-different-values-on-surfaces-the-company-controls)                             | Evidence            | 🟠 Medium        |
| 8  | [Nine tenths of the entries repeat their own link text](#8-nine-tenths-of-the-entries-repeat-their-own-link-text)                                                                                                  | Content strategy    | 🟠 Medium        |
| 9  | [The file carries no priority marker and the customer evidence sits at the bottom](#9-the-file-carries-no-priority-marker-and-the-customer-evidence-sits-at-the-bottom)                                            | Machine readability | 🟠 Medium        |
| 10 | [The content library labels itself as belonging to last year and the current work is missing](#10-the-content-library-labels-itself-as-belonging-to-last-year-and-the-current-work-is-missing)                     | Content strategy    | 🟠 Medium        |
| 11 | [Thirty third-party providers are listed with no statement of relationship](#11-thirty-third-party-providers-are-listed-with-no-statement-of-relationship)                                                         | Positioning         | 🟠 Medium        |
| 12 | [Duplicate pages are listed with nothing marking which one is authoritative](#12-duplicate-pages-are-listed-with-nothing-marking-which-one-is-authoritative)                                                       | Content strategy    | 🟢 Low           |
| 13 | [The site serves six languages and publishes one file](#13-the-site-serves-six-languages-and-publishes-one-file)                                                                                                   | Machine readability | 🟢 Low           |
| 14 | [An earlier blog host is still live and carries pre-2024 positioning](#14-an-earlier-blog-host-is-still-live-and-carries-pre-2024-positioning)                                                                     | Content strategy    | 🔵 Informational |

## Detailed Findings

### 1. Two `llms.txt` files exist and disagree on the name of the company

| Severity | Effort to fix | Type                | Target                                                      |
|:---:|:---:|:---:|:---:|
| 🔴 High   | 🟢 Low         | Machine readability | [Marketing llms.txt](https://www.joinmassive.com/llms.txt) and [documentation llms.txt](https://docs.joinmassive.com/llms.txt) |

**Description**

Two files exist. The one at the apex domain opens with the domain name. The one on the documentation subdomain opens with the company name. The site footer names the legal entity as Massive Computing, Inc.

Neither file links the other.

The apex file carries the summary block quote the format asks for and no Optional section. The documentation file carries the Optional section and no summary. The documentation file also lists three interface specifications, describes each link in working prose, and points at plain text rather than rendered pages. Neither file follows the format completely, and the two fail in opposite ways. Someone inside this company understands the format. That person did not write the file at the apex domain.

The apex heading is a domain string with irregular capitalisation rather than a name. That matters more here than it would elsewhere. Massive is a common English adjective, which is presumably why the domain carries a prefix at all. Resolving this company against that word is already difficult, and the one file whose purpose is to say who the company is offers a third variant.

A brand page exists. It is in the site footer and in neither file.

The two files publish different names and do not link to one another.

**Recommendations**

1. Set the heading of both files to the company name. Add the summary to the documentation file and the Optional section to the apex file.

2. List the documentation file as the first entry of a new documentation section in the apex file, and add the brand page, so the naming question has a published answer.

<a name="2-the-documentation-is-absent-from-the-file-that-models-reach-first"></a>

### 2. The marketing facts file omits the documentation

| Severity | Effort to fix | Type                | Target                     |
|:---:|:---:|:---:|:---:|
| 🔴 High   | 🟢 Low         | Machine readability | [Marketing llms.txt](https://www.joinmassive.com/llms.txt) and the [documentation site](https://docs.joinmassive.com/residential/introduction) |

**Description**

The company sells four interfaces. The apex file links no documentation of any kind.

The documentation property runs to around 150 pages covering residential proxies, ISP proxies, rendering, the reseller interface, the reporting interface, and the monetisation kit. A second documentation host serves the reseller interface separately. Three interface specification files are published. The code organisation is linked in the site footer and contains the company's own protocol server. None of that appears in the file.

The apex file lists 26 identity-concealment browser guides, 30 marketplace listings, and 26 glossary entries. It does not link to an authentication guide.

The site navigation links to the documentation. The apex file omits it.

**Recommendations**

1. Add a documentation section as the second section of the apex file, carrying the documentation file, the three interface specifications, the residential quickstart, the render overview, and the code organisation. Ten links.

2. Publish a combined full text file from the documentation property, which already serves plain text versions of every page, so a reader with room available can take the technical corpus in one request.

### 3. The compliance summary omits the audit the company holds and calls two regulations certifications

| Severity | Effort to fix | Type     | Target                                    |
|:---:|:---:|:---:|:---:|
| 🔴 High   | 🟢 Low         | Evidence | [Marketing llms.txt](https://www.joinmassive.com/llms.txt) and [web access product page](https://www.joinmassive.com/web-access) |

**Description**

The summary sentence states that the company holds compliance certifications including AppEsteem, GDPR, CCPA, and membership of AMTSO.

The web access page, which the same file links, states that the company is SOC 2 Type 1 audited and displays the badge.

The file omits the SOC 2 Type 1 audit that the product page reports.

GDPR and CCPA are regulations. No body issues GDPR certificates to proxy networks. Compliance with either is a self-attested legal position, and describing it as certification alongside AppEsteem, which is a genuine third-party certification, either misreads the compliance stack or inflates it. The live page states it correctly. The two surfaces describe the credentials differently.

The two pages carrying the abuse controls are in the site footer and in neither file. For a residential proxy network, in a category with a long record of operators taking bandwidth without asking, the page saying what a customer may not target is the most credibility-bearing document on the property.

**Recommendations**

1. Rewrite the summary sentence to say the company is SOC 2 Type 1 audited, AppEsteem certified, an AMTSO member, and compliant with GDPR and CCPA. Ten minutes, and nothing is given up.

2. Add a trust and compliance section carrying the blocked destinations page, the best practices page, the surviving kit privacy policy, and the documentation page describing how consent is obtained.

### 4. The partner earnings figure is disproved by a page listed in the same file

| Severity | Effort to fix | Type     | Target                             |
|:---:|:---:|:---:|:---:|
| 🔴 High   | 🟢 Low         | Evidence | [Marketing llms.txt](https://www.joinmassive.com/llms.txt) and [FAQ](https://www.joinmassive.com/faq) |

**Description**

The monetisation section describes a tiered partner programme paying up to $720,000 a year.

The questions page, listed four sections earlier in the same file, states that application partners earn between 5 and 20 cents per user per month.

$720,000 a year is $60,000 a month. At 20 cents a user that requires 300,000 consenting monthly devices. At 5 cents it requires 1.2 million. That is not a programme tier. It is one partner at the far end of a long tail, published with no denominator and no cohort.

The file publishes the ceiling without a device count, cohort, or period over which the per-user rates apply. The linked FAQ supplies rates but does not substantiate the ceiling.

The figures on the questions page are separately stale. That page still describes revenue as arising from running scientific simulations, which is finding 1 of the July review and remains open.

**Recommendations**

1. Replace the ceiling with a per-user figure and a scale qualifier. If a ceiling is kept, publish the device count that produces it.

2. Move the earnings representation into the documentation, where it can be maintained against programme data, and refer to it by address from both the file and the questions page rather than restating it in either.

### 5. The product list contradicts the file's own summary sentence

| Severity | Effort to fix | Type        | Target                     |
|:---:|:---:|:---:|:---:|
| 🔴 High   | 🟢 Low         | Positioning | [Marketing llms.txt](https://www.joinmassive.com/llms.txt) |

**Description**

The opening sentence names five things the company offers. One of them is ISP proxies.

The products section lists web access, search, rendering, the protocol server, and the marketplace. ISP proxies is named in the summary and linked nowhere in the file.

The page exists. It is in the primary navigation, in the footer, and in the pricing table at $1.80 per address. It has 11 documentation pages describing carrier-backed infrastructure at 10 gigabits per second. A product line with its own documentation section is invisible in the file that claims to index the company.

Three further surfaces are missing. The interactive trial is in the primary navigation and is the highest-intent surface on the site, being the one thing a model could suggest a developer actually do. Pricing appears nowhere, although four anchored price points exist and the company's own protocol server tells agents that the live cost reference is the pricing page. The language model render interface is a live pricing tab with its own documentation page and its own endpoint, and its only trace in the file is a subordinate clause inside the description of something else.

Products is 5 of 186 links. It is both incomplete and contradicted from within.

**Recommendations**

1. Rebuild the products section to carry web access, ISP proxies, search, rendering, language model rendering, the protocol server, the trial, pricing, and the marketplace. Nine entries, each with a working description and an entry price where one applies.

2. List pricing as a named entry rather than as anchors on the homepage, so the address the company's own protocol server points at can be resolved from the file.

### 6. The file is weighted towards evasion tooling and against the claim the business rests on

| Severity | Effort to fix | Type        | Target                     |
|:---:|:---:|:---:|:---:|
| 🔴 High   | 🟠 Medium      | Positioning | [Marketing llms.txt](https://www.joinmassive.com/llms.txt) |

**Description**

The first substantive assertion in the file is that Massive is a 100 percent ethical data collection infrastructure provider.

Twenty-six links later the file lists integration instructions for GoLogin, Dolphin Anty, Kameleo, Linken Sphere, Octo Browser, Multilogin, MoreLogin, VMLogin, Xlogin, Genlogin, MostLogin, Hidemyacc, Undetectable, Incogniton, AdsPower, and eleven others. At least 22 of the 26 are identity concealment or multiple-session browsers. Several state the purpose in the product name. The documented commercial uses of that category are running many accounts on one platform, advertising fraud, automated purchasing of limited stock, and creating accounts in bulk.

The surrounding material reinforces it. The render interface is described in the file as captcha bypass. The article list carries a piece on bypassing address bans, a piece on bypassing regional blocking, a ranking of identity concealment browsers, and a definition of browser fingerprinting.

That is 31 entries. The number of entries supporting the consent claim is zero. The claim itself is one unfalsifiable sentence with nothing behind it.

This matters more here than it would in a sitemap. A sitemap is exhaustive by design. This format is a summary, and the whole premise of a summary is that the publisher chose what was representative. The company has represented itself, at 14 percent of the file, as an integration layer for identity concealment software, and at nothing at all as a consent-based network.

**Recommendations**

1. Put a trust and compliance section above the guides, and move the guides into the Optional section or cut them to the index plus the five most trafficked entries. The guides are legitimate long-tail acquisition and competitors publish the same material. What needs correcting is the weighting, not their existence.

2. Describe the render interface by what it does rather than by what it defeats, matching the live product page, which speaks of full browser rendering and automatic handling of challenges.

### 7. Three product facts are published with different values on surfaces the company controls

| Severity | Effort to fix | Type     | Target                                                       |
|:---:|:---:|:---:|:---:|
| 🟠 Medium | 🟠 Medium      | Evidence | [Marketing llms.txt](https://www.joinmassive.com/llms.txt), [FAQ](https://www.joinmassive.com/faq), [web access](https://www.joinmassive.com/web-access), [documentation](https://docs.joinmassive.com/residential/introduction), and [MCP repository](https://github.com/joinmassive/mcp-server) |

**Description**

Three product facts carry different values across the company's own sources. All of the sources are machine-readable and all of them are reachable.

On platforms supported by the monetisation kit, the file says Windows, Android, and Fire Stick. The questions page says 64-bit Windows 7 and later, macOS 10.10 and later, and Android. The documentation says Windows on desktop, and Android, FireOS, iOS, Tizen, and webOS elsewhere. Apple mobile support appears in one of the three. Apple desktop support appears in a different one.

On session persistence, the product page says up to 12 minutes. The residential documentation says the duration is adjustable and defaults to 15 minutes. The ISP documentation says sessions do not expire at all. A default above a stated maximum is incoherent, so one of the two is wrong. This is the sort of detail a developer meets in the first hour of integration.

On the dashboard address, the live site signs users in at one host, the usage alerts documentation names a second, and the protocol server repository names a third. Two of those three are machine-readable instructions to an agent.  The file names none of the three and cannot settle it.

The common cause is restatement. Each fact is written out separately on three surfaces, and each surface drifted on its own.

**Recommendations**

1. Give each fact one canonical location in the documentation, and have the file and the questions page refer to it by address rather than restate it.

2. Clarify session duration by product, including defaults, limits, and any configurable values.

### 8. Nine tenths of the entries repeat their own link text

| Severity | Effort to fix | Type             | Target                     |
|:---:|:---:|:---:|:---:|
| 🟠 Medium | 🟠 Medium      | Content strategy | [Marketing llms.txt](https://www.joinmassive.com/llms.txt) |

**Description**

The note after each link exists so a reader can decide whether fetching the page is worth the cost. This file has filled it with page titles.

The solutions section, the guides, the marketplace, the glossary, and the article library all do this without a single exception. So do the checklist, the questions page, the privacy pages, the press page, the careers page, and the legal pages. That is 170 of 186 entries, or 91 percent. An entry reading Apify, followed by a note reading Apify, Web Data Marketplace, has spent context to say nothing.

Around ten entries carry something a reader could act on. The strongest is a case study note recording that a customer moved from 82 percent to over 95 percent success rates. It is specific, numeric, attributed, and checkable. There are three notes of that kind in the file and 26 dictionary definitions. The thing that works is the thing done least.

Three of the eleven solutions entries additionally disagree with themselves. The link text has been softened and the note has not. One is labelled Amazon data access and described as Amazon proxies. Another is labelled web data collection and described as proxies for web scraping. A reader has no basis for choosing between the two names. This reads as a repositioning that rewrote the link text and never went back for the notes.

**Recommendations**

1. Rewrite the notes for the 24 entries that carry commercial weight, being the products, the case studies, the startups programme, and the solutions. Model them on the case study note: a number, a named party, and an outcome someone could check.

2. Reconcile the three solutions entries where the link text and the note name the page differently. Leave the glossary as titles, or move it into the Optional section, where a note carrying nothing costs nothing.

### 9. The file carries no priority marker and the customer evidence sits at the bottom

| Severity | Effort to fix | Type                | Target                     |
|:---:|:---:|:---:|:---:|
| 🟠 Medium | 🟢 Low         | Machine readability | [Marketing llms.txt](https://www.joinmassive.com/llms.txt) |

**Description**

The one structural device this format provides is a final section named Optional, marking material a reader may skip when room is short. It is the only way the file has of saying that one thing matters more than another. It is absent across 186 links.

The documentation file has one. The convention is understood inside the company and was not applied to the file that needed it more.

The ordering compounds it. Guides and marketplace listings come before the case studies, the article library, and the glossary. The case studies sit below 56 guide and marketplace links about other companies’ products. The only proof in the file sits underneath the identity concealment browser catalogue.

**Recommendations**

1. Add an Optional section carrying the glossary, the guides beyond the index, the marketplace beyond a featured set, and the long tail of the article library. Around 90 links move below the line and none is deleted.

2. Reorder what remains so that products, documentation, trust and compliance, pricing, and case studies come before everything else.

### 10. The content library labels itself as belonging to last year and the current work is missing

| Severity | Effort to fix | Type             | Target                            |
|:---:|:---:|:---:|:---:|
| 🟠 Medium | 🟠 Medium      | Content strategy | [Marketing llms.txt](https://www.joinmassive.com/llms.txt) and [company blog](https://www.joinmassive.com/blog) |

**Description**

Twenty-two of the 68 article entries carry a 2025 stamp in the title or the note. The concentration falls where it costs most. All five of the ranked list articles carry it. Six of the nine head-to-head comparisons carry it. So do the pricing guide, the buyer's guide, the setup guide, and both market maps.

The older titles include pages about provider selection, comparison, and pricing.

The current work is absent. The site navigation surfaces an essay published on 20 July 2026 by the head of innovation, under a heading announcing the latest from the blog. It is not in the file. Nothing from 2026 is in the file.

Set against the absence of the ISP page, the trial page, pricing, the two abuse control pages, the brand page, the partners page, and the entire documentation property, all of which are in the current navigation or footer, the file has not been regenerated against the current site.

There are no dates anywhere in it. No publication dates, no revision dates, and no revision date on the file itself. Across a library of 68 articles, recency is the most useful note the format allows and it is used nowhere.

**Recommendations**

1. Add a year, or a year and month, to every article and case study entry, and put a revision date under the heading of the file.

2. Generate the file from the sitemap at build time rather than maintaining it by hand.

### 11. Thirty third-party providers are listed with no statement of relationship

| Severity | Effort to fix | Type        | Target                     |
|:---:|:---:|:---:|:---:|
| 🟠 Medium | 🟢 Low         | Positioning | [Marketing llms.txt](https://www.joinmassive.com/llms.txt) |

**Description**

The marketplace section lists 30 providers. Several are direct or adjacent competitors, among them Apify, Crawlbase, Diffbot, DataForSEO, Browse AI, Scrape.do, Parsera, and Lightpanda.

Every note is the page title. Nothing says these are marketplace listings rather than recommendations, nothing states the relationship, and nothing explains what the marketplace is for.

The section gives 30 alternatives pages on Massive’s own domain without explaining their relationship to Massive. Marketplace listings outnumber product links six to one.

**Recommendations**

1. Add a one-sentence preamble to the section, which the format allows, saying these are vetted third-party providers building on or integrating with Massive infrastructure.

2. Cut the inline list to the marketplace index plus the providers with published case studies, and move the rest into the Optional section.

### 12. Duplicate pages are listed with nothing marking which one is authoritative

| Severity | Effort to fix | Type             | Target                                     |
|:---:|:---:|:---:|:---:|
| 🟢 Low    | 🟠 Medium      | Content strategy | [Marketing llms.txt](https://www.joinmassive.com/llms.txt), [blog](https://www.joinmassive.com/blog), and [glossary](https://www.joinmassive.com/glossary) |

**Description**

The file lists several sets of pages covering the same idea, on the same domain, with nothing marking which one carries the company's position.

Address rotation is covered by five entries. Two of them are separate glossary addresses carrying an identical title, and one of those two has link text that disagrees with its own title. Residential proxies are covered by six entries. ISP proxies by four. Identity concealment browsers by 26 guides and a ranked article.

The same duplication appears on the compliance surface. Three privacy policies are listed. One is described as a personal information and kit privacy policy, one as a kit privacy policy, and one as a website privacy policy. Two of the three describe themselves as the kit privacy policy and nothing distinguishes them. This company's defensibility rests on documented consent, and the document establishing consent exists in two versions the file cannot tell apart.

The file does not identify a primary resource for those topics or a governing kit privacy policy.

**Recommendations**

1. Consolidate the duplicate glossary and article pages, redirect the losers, and list only the survivor in the file.

2. Establish which of the two kit privacy policies governs, retire the other, and say in the note what each remaining policy covers.

### 13. The site serves six languages and publishes one file

| Severity | Effort to fix | Type                | Target                     |
|:---:|:---:|:---:|:---:|
| 🟢 Low    | 🟠 Medium      | Machine readability | [Marketing llms.txt](https://www.joinmassive.com/llms.txt) and [web access product page](https://www.joinmassive.com/web-access) |

**Description**

The site offers English, Spanish, Brazilian Portuguese, French, Russian, and Chinese. One file exists, in English, covering only the unprefixed addresses.

The English language-prefixed version of the web access page is indexed while that page's own canonical declaration points at the unprefixed address. The prefixed version is therefore both indexed and duplicative.

**Recommendations**

1. Publish a file at each locale root, or add a language section to the existing file listing them, so a reader arriving in another language is not silently handed the English surface.

2. Confirm how the language-prefixed addresses are being canonicalised before publishing the per-language files, so the duplication is not carried into them.

### 14. An earlier blog host is still live and carries pre-2024 positioning

| Severity        | Effort to fix | Type             | Target                 |
|:---:|:---:|:---:|:---:|
| 🔵 Informational | 🟢 Low         | Content strategy | Legacy blog at `blog.joinmassive.com`, compared with the [current company blog](https://www.joinmassive.com/blog) |

**Description**

A fourth content host is live at `blog.joinmassive.com`. Its about page describes the blog as covering alternative business models and distributed computing, and describes the company as a platform letting developers pay for software with idle processing power and bandwidth.

That is the position the company held before 2024. It is the same problem as finding 1 of the July review, on a different host, and worse in one respect. This host is in neither file, so a crawler that finds it gets no signal that the current blog supersedes it.

**Recommendations**

1. Redirect the host to the current blog, or list it in the file with a note saying it is an archive.

2. Whichever is chosen, choose it. Leaving the host live and unlisted is the worst of the three options available.

## Appendix A: Severity and Effort Definitions

| Severity        | Definition                                                                                                                       |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| 🔴 High          | A model answering a buying question from this file returns something false, or something that contradicts what the company sells. |
| 🟠 Medium        | Nothing is false. The strongest available evidence is unreachable, unweighted, or undated.                                       |
| 🟢 Low           | Structure and hygiene. The cost accumulates rather than being felt at once.                                                      |
| 🔵 Informational | An observation that is not a defect.                                                                                             |

| Effort   | Definition                                                                |
| -------- | --------------------------------------------------------------------------- |
| 🟢 Low    | Copy, links, or a single figure. Minutes to hours.                        |
| 🟠 Medium | A new section, a consolidation, or a reconciliation across surfaces. Days. |
| 🔴 High   | New content, new structure, or a change to the build pipeline. Weeks.     |

## Appendix B: Sources

- [Marketing llms.txt](https://www.joinmassive.com/llms.txt), fetched 11 August 2026
- [Documentation llms.txt](https://docs.joinmassive.com/llms.txt), fetched 11 August 2026
- [Web access product page](https://www.joinmassive.com/web-access), including navigation, footer, pricing table, and compliance block
- [FAQ](https://www.joinmassive.com/faq)
- [Massive homepage](https://www.joinmassive.com/), team section
- [Massive documentation](https://docs.joinmassive.com/residential/introduction), including residential, ISP, render, reseller, reporting, and monetisation kit sections
- `api-docs.joinmassive.com`
- `blog.joinmassive.com/about`
- [Massive MCP repository](https://github.com/joinmassive/mcp-server)
- [The llms.txt proposal](https://llmstxt.org/), Jeremy Howard, Answer.AI, September 2024
- [Massive Computing Inc. Public Surface Review](./Massive.md), July 2026

## Appendix C: Confidence and Limitations

Counts, quotations, and arithmetic are stated with high confidence. Every one was taken from the raw file and can be reproduced by fetching it.

The characterisation of the identity concealment browser category in finding 6 is supportable from the product names alone. The finding is about weighting rather than about the legitimacy of any single guide. Competitors publish the same material. The argument is that this format is a summary, and this summary runs 31 to zero against the company's own central claim.

Finding 13 rests on one indexed language-prefixed address set against a conflicting canonical declaration, rather than on a crawl. It is stated with moderate confidence and should be checked before it is relied on.

Finding 7 establishes that three dashboard addresses are published across the company's own sources. It does not establish which of them still resolve. That should be verified before the finding is cited.

The review did not measure whether assistants retrieve or use either file.

This review has no view of referral traffic from assistant surfaces, no data on which pages assistants currently retrieve, and no way to know whether the marketplace listings are paid placements. If the marketplace is a paid channel the severity on finding 11 is too high, though the absence of framing would remain a defect.

<a name="appendix-d-expected-results-and-measurement"></a>

## Appendix D: Evidence Check and Measurement

This appendix records what the files could support during the review and how to test any change in assistant answers.

**What the file can answer**

The following twelve questions were checked against the published material. This is a source check.

| Question                                        | Answerable now | Reason                                                 |
| ------------------------------------------------ | -------------- | -------------------------------------------------------- |
| Is the company SOC 2 audited?                    | No             | Omitted, and a false certification set stated instead   |
| How do I authenticate against the web interface? | No             | No documentation links                                  |
| Does the company offer ISP proxies?              | No             | Named in the summary, linked nowhere                    |
| What does it cost per gigabyte?                  | No             | No pricing links or figures                             |
| How much can a kit partner earn?                 | No             | The figure requires 300,000 to 1.2 million devices      |
| Does the kit support Apple mobile?               | No             | The file says Windows, Android, and Fire Stick          |
| How long do sessions persist?                    | No             | Absent, and contradicted across three surfaces          |
| Where do the addresses come from?                | No             | Asserted, with nothing behind it                        |
| What am I not permitted to target?               | No             | The abuse control pages are absent                      |
| Can I use it from a coding assistant?            | Yes            | The protocol server note is one of the few good ones    |
| What geographic coverage exists?                 | Yes            | Stated in the summary                                   |
| Who uses it, and with what result?               | Yes            | One case study carries a before and an after figure     |

The review marked three of twelve answerable from the published material. Re-score the questions after editing the files.

**How to measure it**

Take the twelve questions above, add eighteen covering comparisons, use cases, and integration, and put all thirty to the major assistants. Score each answer on three binaries: correct, complete, and cites a source the company controls. Record that baseline before editing the file. Run it again at fourteen days and at forty-five.

Parse the server logs for requests to the file by user agent, and record which crawlers then request the addresses it lists. That establishes whether the file is read at all, which is worth knowing before investing further in it.

Filter analytics for referrers from assistant hosts. This is directional only. It catches the citation click and misses the typed domain entirely, so it is a floor and never a total.

Re-fetch both files and diff them to confirm the corrections landed.

## Appendix E: Proposed File Structure

The skeleton below carries every correction in this review. Notes are abbreviated for length. The shape is the point.

```markdown
# Massive

> Massive is a consent-based web access network. Real-time residential and ISP
> access, search, rendering, and language model calls across 195+ countries, sold
> to teams building agents, models, and data pipelines. SOC 2 Type 1 audited,
> AppEsteem certified, AMTSO member, GDPR and CCPA compliant.
> Last updated: YYYY-MM-DD

## Products
[nine entries: web access, ISP proxies, search, render, LLM render, protocol
server, playgrounds, pricing, marketplace, each with an entry price]

## Documentation
[the docs file first, then the three interface specifications, the residential
quickstart, the render overview, the reseller interface, the code organisation]

## Trust and Compliance
[blocked destinations, best practices, the consent process, the SOC 2
attestation, the surviving kit privacy policy, the site privacy policy]

## Customers
[case studies, each note carrying a before figure, an after figure, and a name]

## For Startups
[the programme, with the three-month term stated, plus the four routes]

## Solutions
[eleven entries, link text and note reconciled]

## Guides
[the index, plus the five most trafficked integrations]

## Marketplace
[the index, plus providers with published case studies, under a preamble
stating the relationship]

## Blog
[2026 work first, every entry dated]

## Company
[about, brand, press, careers, contact, terms, licence]

## Optional
[glossary, remaining guides, remaining marketplace listings, article long tail]
```

Two notes on the shape.

The summary currently omits the security audit, describes two regulations as certifications, and names a product without linking to it.

The Optional section marks material that a reader can skip when space is limited.