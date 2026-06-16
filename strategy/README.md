# Inner Peace — Strategic Website Analysis & Implementation Plan

A complete, evidence-based strategy for **Inner Peace In-Home Nursing & Care** (innerpeace.vision), built entirely from the site crawl and governed by the [Strategic Website framework](https://innerpeace-web.github.io/Strategic-Website/).

> **Two sources of authority**
> 1. **Business & content source of truth** — the crawl in `../innerpeace-crawl/` + `../innerpeace-mapping.json` (25 URLs, every page, image, alt, heading, CTA, meta field).
> 2. **Implementation standard** — the Strategic Website framework.
>
> Every recommendation cites both. Nothing is generic; everything is specific to Inner Peace and traceable to crawl evidence. Where the framework prescribes something not yet on the site, it is tagged **[FRAMEWORK]**.

## How to read this folder

| # | Document | What it answers |
|---|---|---|
| 0 | **[_facts.md](_facts.md)** | The grounded fact base every other doc traces back to (brand, people, contact, services, trust signals, defects, image inventory, design tokens, framework summary). **Start here.** |
| 1 | **[website-inventory.md](website-inventory.md)** | Every URL: purpose, content type, conversion intent, funnel stage, CTAs, SEO value + missing pages. |
| 2 | **[content-audit.md](content-audit.md)** | Per-page content extraction, quality audit, gaps, consolidation opportunities. |
| 3 | **[information-architecture.md](information-architecture.md)** | Current vs recommended sitemap, navigation, 301 redirect map, service & conversion architecture. |
| 4 | **[customer-journey.md](customer-journey.md)** | Personas, 6-stage journey map, entry/exit points, friction, dementia & carer journeys. |
| 5 | **[brand-analysis.md](brand-analysis.md)** | Positioning, messaging & visual consistency, voice guide, brand gaps. |
| 6 | **[visual-system.md](visual-system.md)** | Design tokens, type scale, components + image inventory, imagery guide, consistency report, optimisation. |
| 7 | **[seo-strategy.md](seo-strategy.md)** | Audit, keyword & topic clusters, internal linking, missing pages, schema, local SEO, roadmap. |
| 8 | **[conversion-optimization.md](conversion-optimization.md)** | CTA audit, conversion paths, trust-building, booking flow, CRO backlog, measurement plan. |
| 9 | **[strategic-website-blueprint.md](strategic-website-blueprint.md)** | The capstone build spec — page-by-page strategy for the new site. |

## The headline findings (all crawl-verified)

1. **Broken internal links** — the home page and About page both link "personalised care" to `/home-care-services/personal-care/`, whose parent `/home-care-services/` returns a 404.
2. **Inconsistent service URLs** — services sit at `/in-home-nursing-care-services/…` but Dementia Care is off-pattern at `/dementia-care/`.
3. **Brand-name drift** — "Inner Peace In-Home Nursing & Care" vs "Inner Peace Vision" vs "Inner Peace Services"; `en-AU` content tagged `og:locale = en_US`; "personalised" and "personalized" both appear.
4. **Buried trust & reviews** — Cert III / CPR / First Aid, full insurance, RN founder and 3 real testimonials exist but are buried; no consolidated trust section.
5. **Duplicate area pages** — six near-identical town pages sharing one hero image (duplicate-content risk).
6. **Orphaned recruitment & thin pages** — DISC + Interview forms have no Careers home; Foot Care is an indexable "Coming Soon!" stub.
7. **No structured data** anywhere in the crawl.

## What was built from this strategy

The static, framework-aligned rebuild lives in **[`../website/`](../website/)** (HTML5 + CSS3 + vanilla JS, no frameworks). See `../website/README.md` for the build's structure, mapping to the framework, and how each defect above is fixed.
