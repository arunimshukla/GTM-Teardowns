# Methodology

This document describes how reports in GTM Teardowns are scoped, tested, prioritised, and corrected.

## Purpose

The reviews examine what a prospective buyer, developer, procurement team, candidate, or automated system can learn from a company's public surface.

They answer four questions:

1. What does the company claim?
2. What public evidence supports that claim?
3. Where does the evidence fail to reach the decision path?
4. What is the smallest defensible change that would close the gap?

The reviews do not attempt to infer confidential strategy or internal performance from public material.

## Review process

### 1. Declare the scope

Each report records:

- the company and surfaces reviewed;
- the date of checking;
- the access available;
- any comparators used;
- material deliberately excluded from the review.

A bounded scope is more useful than an implied claim of completeness.

### 2. Capture the public position

The review records how the company describes its product, audience, evidence, services, and differentiation across the relevant public surfaces.

Sources may include:

- homepages and product pages;
- documentation and public repositories;
- research and content libraries;
- recruitment material;
- public interviews;
- social profiles;
- machine-readable files.

Claims published by the company are treated as company claims. Third-party measurements are attributed to the party that produced them.

### 3. Separate observation from inference

A finding begins with a condition that can be checked on a public surface. The commercial consequence and recommended response are reasoned interpretations of that condition.

This distinction matters. A public review can establish that evidence is missing from a page. It cannot establish the conversion effect of that omission without analytics or buyer research.

### 4. Select comparators for a specific question

A comparator is chosen because it demonstrates a relevant practice, not because the two companies are identical.

For example, one firm may be a useful benchmark for evidence presentation while being the wrong benchmark for market position, pricing, or category strategy.

### 5. Retest before publication

Each proposed finding is checked again against the declared scope. Findings are removed when:

- the evidence cannot be reproduced;
- the page has changed;
- the conclusion requires unavailable internal data;
- the comparator does not support the intended comparison;
- the recommendation exceeds what the evidence justifies.

### 6. Prioritise by buyer consequence

Impact is assigned according to the consequence for the intended reader, not the size of the implementation.

| Impact | Definition |
|:--|:--|
| 🔴 **High** | The issue blocks an enquiry or evaluation path, contradicts a material public claim, or prevents a buyer from verifying evidence central to the purchase. |
| 🟠 **Medium** | Nothing is technically broken, but a meaningful differentiator, proof point, or audience path is absent or materially weakened. |
| 🟢 **Low** | The issue concerns structure, attribution, accessibility, or editorial consistency. Its cost accumulates rather than appearing in one decisive failure. |
| 🔵 **Informational** | A relevant observation that is not, by itself, a defect. |

Effort is estimated independently:

| Effort | Definition |
|:--|:--|
| 🟢 **Low** | Copy, links, metadata, or configuration. Normally measured in hours. |
| 🟠 **Medium** | A new page, programme, or reusable component built largely from existing material. Normally measured in days. |
| 🔴 **High** | New content, data collection, organisational process, or substantial structural work. Normally measured in weeks. |

Impact and effort are not substitutes. A one-character error can have high impact, while a large new content programme can have low urgency.

## Evidence standard

A defensible finding should identify:

- the public surface or address;
- the observed condition;
- the date of checking;
- the source of any numerical claim;
- whether a statement is an observation, a company claim, a third-party result, or an inference.

Short quotations may be used when wording is central to the finding. The reports do not reproduce entire third-party pages.

## Limitations

Unless a report states otherwise, the review has no access to:

- website or product analytics;
- customer interviews;
- win and loss data;
- paid acquisition performance;
- internal roadmaps;
- sales pipeline data;
- private repositories or documentation.

A page can be weakly constructed and still perform. These reports evaluate the quality and consistency of the public evidence, not the private effectiveness of the business.

## Independence and publication

The reviews are independent and were not commissioned. Each company was given the report before it was published in this repository.

Company names, product names, and trademarks remain the property of their owners. They are used for identification and commentary.

## Corrections and revalidation

Public surfaces change. A finding is a claim about the page and date recorded in its report, not a permanent claim about the company.

To propose a correction, open a [GitHub Issue](https://github.com/arunimshukla/GTM-Teardowns/issues) and include:

1. the report and finding;
2. the current public source;
3. the date checked;
4. the specific statement that should change.

Corrections should preserve the historical record while making the current state clear.
