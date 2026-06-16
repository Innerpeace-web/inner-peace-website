# Inner Peace — Static Website Build

A production-ready static rebuild of **Inner Peace In-Home Nursing & Care**, implementing the [Strategic Website framework](https://innerpeace-web.github.io/Strategic-Website/) while preserving the existing brand, voice, services, trust signals and content captured in the crawl.

**Stack:** HTML5 · CSS3 · Vanilla JavaScript. **No** React/Vue/Angular/Svelte, **no** Bootstrap/Tailwind, **no** jQuery, **no** build step. Semantic, accessible, mobile-first, progressively enhanced, SEO-optimised. Deployable to any static host (Netlify, GitHub Pages, S3, Apache/Nginx).

## Run it
It's a static site — just open `index.html`, or serve the folder:
```bash
cd website && python3 -m http.server 8080   # then visit http://localhost:8080
```

## Structure
```
website/
├── index.html                  # Home — framework's 6-section model (A–F)
├── about.html                  # Annette's story + brand story
├── trust.html                  # [NEW] consolidated "Why choose us" / trust hub
├── testimonials.html           # [NEW] real reviews given room to breathe
├── book.html                   # "Book a free care consultation" — multi-step widget
├── contact.html                # 4 contact intents + tappable phone + form
├── careers.html                # [NEW] Join our team — surfaces DISC + Interview forms
├── 404.html                    # Friendly not-found
├── services/
│   ├── index.html              # Services hub (fixes "three services" → four)
│   ├── personal-care.html      # 9 tasks (verbatim)
│   ├── nursing-care.html       # clinical services (verbatim)
│   ├── social-care.html        # 11 activities (verbatim)
│   └── dementia-care.html      # most-evolved page + online referral form (canonical fix)
├── resources/
│   ├── index.html              # Resources hub
│   ├── area-served.html        # consolidates 6 duplicate town pages
│   └── benefits.html           # benefits of home care (verbatim list)
├── legal/{privacy.html, terms.html}
├── staff/index.html            # Staff Portal login (separate, noindex)
├── assets/
│   ├── css/styles.css          # design system: tokens + components
│   ├── js/main.js              # nav, booking widget, reveal, forms, analytics hooks
│   └── img/                    # local asset slot (live build references crawl image URLs)
├── sitemap.xml · robots.txt
└── _redirects · .htaccess      # 301 migration map (old WordPress URLs → new)
```

## How the build implements the framework

| Framework principle | Implementation |
|---|---|
| Homepage 6-section model (A Hero → F CTA) | `index.html` sections A–F, "Book a free care consultation" hero CTA, "Caring for East Gippsland since 2022" trust cue |
| Single consistent service path | All services under `/services/`; `/dementia-care/` → `/services/dementia-care.html` (301 in `_redirects`/`.htaccess`) |
| Separate staff portal | `/staff/` is `noindex`, kept out of primary nav, in footer only |
| Surface trust fastest | Hero trust row, trust pillars + badges section, dedicated `trust.html`, testimonials given room |
| Mobile-first + click-to-call always reachable | Sticky `.callbar` (call / book) on mobile; `tel:` links throughout; ≥48px tap targets |
| Warm palette, never clinical-cold | Teal/deep-teal + sage/soft-blue tokens; Fraunces + Hanken Grotesk fonts |
| Every section ends in an invitation to act | Closing `.cta-band` on every page |
| Predictable URLs, accessibility | Semantic landmarks, skip link, breadcrumbs, labelled forms, focus styles, reduced-motion support |

## Crawl defects fixed in this build

| Defect (from crawl) | Fix |
|---|---|
| Broken `/home-care-services/personal-care/` links on home & about | Links repointed to `/services/personal-care.html`; legacy path 301'd |
| Off-pattern `/dementia-care/` URL | Moved under `/services/`, 301 from old URL |
| "Inner Peace Vision/Services" name drift | Single canonical name throughout |
| `og:locale = en_US` on en-AU site | `lang="en-AU"` + `og:locale="en_AU"` |
| "Explore our three services" but four shown | Copy corrected to four |
| Foot Care thin "Coming Soon!" indexable page | Omitted from nav/sitemap (reinstate when ready) |
| Testimonials buried & unattributed | Dedicated page + home section, framed as real client reviews |
| 6 duplicate town pages, shared hero | Consolidated into `resources/area-served.html` with distinct local blurbs |
| Orphaned DISC + Interview forms | Surfaced via `careers.html` |
| No structured data | JSON-LD (LocalBusiness/MedicalBusiness, Person, Service, Review/AggregateRating) embedded |
| Phone numbers as plain text on contact | All numbers are `tel:` links |
| Missing/weak image alts | Descriptive alt text on all content images |

## Notes for go-live
- **Images** reference the live `innerpeace.vision` upload URLs (real brand assets from the crawl). For a self-contained deploy, download them into `assets/img/` and update `src` paths; add `srcset`/AVIF per `strategy/visual-system.md`.
- **Forms** are front-end demos (progressive enhancement via `main.js`). Wire `action`/`fetch` to an email service or form endpoint before launch.
- **Colours** are framework-named hues interpreted as hex tokens in `styles.css` — confirm against any official brand kit.
- **Analytics**: `main.js` emits events (`call_click`, `cta_click`, `booking_step`, `form_submit`, `scroll_depth`) to `dataLayer`/console — connect your analytics tool.
- See **`../strategy/`** for the full reasoning behind every decision.
