# Inner Peace In-Home Nursing & Care — Website Inventory

> **Authoritative source.** This inventory is built entirely from the live crawl (`/innerpeace-crawl/*.json`), the URL map (`/innerpeace-mapping.json`), the published sitemaps, and the extracted fact base (`/strategy/_facts.md`). Where a value is quoted, it is **verbatim from the crawl**. Where a page or section is prescribed but does not yet exist on the live site, it is labelled **[FRAMEWORK]** and traced to the Strategic Website framework (`_facts.md §12`). Nothing here is invented.
>
> **Scope:** 25 URLs total — 18 public pages in the sitemap, 4 unlisted utility pages crawled but not in the sitemap, and 1 broken/404 path that is actively linked from production pages. The crawl was run 2026-06-16; the most recently modified page is `/dementia-care/` (2026-05-18), the newest and most modern build on the site.

---

## 1. Master Inventory — All 25 URLs

Columns: **URL · Page Title (verbatim `<title>`) · Page Purpose · Content Type · Conversion Intent · Funnel Stage · Primary CTA (verbatim) · Supporting CTA · SEO Value**. Defect flags reference `_facts.md §10` and are expanded in §3.

### 1a. Public pages — in sitemap (18)

| # | URL | Page Title (verbatim) | Page Purpose | Content Type | Conversion Intent | Funnel Stage | Primary CTA (verbatim) | Supporting CTA | SEO Value |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `/` | Home - Inner Peace In-Home Nursing & Care | Brand front door; introduces service, qualifications, reviews, contact | Marketing / hub | Get visitor to book or learn | **Awareness** | `Book Now` → `/book-an-appointment/` | `Learn more` (#learn-more); per-service `Learn More`; `Book an appointment` | **High** — primary ranking & brand-query landing page; carries the trust copy (Cert III/CPR/First Aid, insurances). **DEFECT D1, D5, D9, D10** |
| 2 | `/about-us/` | About us - Inner Peace In-Home Nursing & Care | Founder story (Annette Keat, RN); trust/credibility | Story / trust | Build trust → book | **Consideration** | `Book an Appointment` → `/book-an-appointment/` | none | **High** — E-E-A-T anchor (RN, 30 yrs, palliative care grad cert). **DEFECT D1** (links "personalised care" to dead `/home-care-services/personal-care/`) |
| 3 | `/in-home-nursing-care-services/` | In-Home Nursing & Care Services - Inner Peace In-Home Nursing & Care | Services hub; routes to 4 service cards | Hub / navigation | Route to a service page | **Consideration** | `Learn More` (per card) | none | **High** — top-of-cluster pillar for service queries. **DEFECT D6** ("Explore our three services" but four cards shown) |
| 4 | `/in-home-nursing-care-services/personal-care/` | Personal Care - Inner Peace In-Home Nursing & Care | Detail Personal Care tasks (meals, laundry, cleaning, dog walking) | Service detail | Book Personal Care | **Decision** | `Book an Appointment` → `/book-an-appointment/` | sibling `Learn More` cards | **High** — rich, specific task list; strong long-tail target |
| 5 | `/in-home-nursing-care-services/social-care/` | Social Care - Inner Peace In-Home Nursing & Care | Detail Social Care activities (walks, cinema, gardening) | Service detail | Book Social Care | **Decision** | `Book an Appointment` → `/book-an-appointment/` | sibling `Learn More` cards | **High** — rich activity list. **DEFECT D9** (hero `social-care-1.webp` empty alt) |
| 6 | `/in-home-nursing-care-services/nursing-care/` | Nursing Care - Inner Peace In-Home Nursing & Care | Detail clinical nursing (wound, palliative, pain, meds) | Service detail | Book Nursing Care | **Decision** | `Book an Appointment` → `/book-an-appointment/` | sibling `Learn More` cards | **High** — clinical depth; highest-value/highest-intent service |
| 7 | `/in-home-nursing-care-services/foot-care/` | Foot Care - Inner Peace In-Home Nursing & Care | Intended foot-care service page | Service detail (stub) | None — no CTA | **Utility** (effectively dead) | none | sibling `Learn More` cards (only 3, no Dementia) | **Low** — body is literally "Coming Soon!"; indexable thin page; uses old 2023/11 PNG cards. **DEFECT D7** |
| 8 | `/dementia-care/` | Dementia Care - Inner Peace In-Home Nursing & Care | Specialist dementia ("Dementia Nurse Consulting") + online referral | Service detail + lead-gen form | Capture referral / call | **Conversion** | `Complete Online Referral` (#online-referral) | `Contact Dementia Care` (#ips-contact); phones 0419 853 811 / 0477 051 130 | **High** — newest, richest, most modern page; only page with a conversion form. **DEFECT D2** (off-pattern URL), **D3** ("Inner Peace Vision"/"Inner Peace Services" naming), **D9** (hero empty alt) |
| 9 | `/in-home-nursing-care-benefits/` | In-Home Nursing & Care Benefits - Inner Peace In-Home Nursing & Care | Educational: 15 benefits of home care | Educational / supporting | Persuade → book | **Awareness** | `Book an Appointment` → `/book-an-appointment/` | none | **Med** — generic, non-localised benefits copy; useful internal-link target but thin on Inner-Peace specificity |
| 10 | `/area-served/` | Area Served - Inner Peace In-Home Nursing & Care | Service-area hub; links 6 towns | Hub / local SEO | Route to town page | **Awareness** | none (link list only) | 6 town links + "Towns in between" | **Med** — local-SEO hub but no CTA; **DEFECT D12** anchor (its 6 children are near-duplicate). Note: 2 of 6 town links omit trailing slash |
| 11 | `/area-served/inner-peace-in-home-nursing-care-in-bairnsdale/` | Inner Peace In-Home Nursing & Care in Bairnsdale - … | Local landing — Bairnsdale | Local landing (templated) | Book in Bairnsdale | **Awareness** | `Book an appointment` → `/book-an-appointment/` | service `Learn More` cards | **Med** — only the strongest town query; near-identical to siblings. **DEFECT D12** |
| 12 | `/area-served/inner-peace-in-home-nursing-care-in-bruthen/` | Inner Peace In-Home Nursing & Care in Bruthen - … | Local landing — Bruthen | Local landing (templated) | Book in Bruthen | **Awareness** | `Book an appointment` | service cards | **Low** — duplicate template, town swap only. **DEFECT D12** |
| 13 | `/area-served/inner-peace-in-home-nursing-care-in-east-gippsland/` | Inner Peace In-Home Nursing & Care in East Gippsland - … | Local landing — East Gippsland | Local landing (templated) | Book in region | **Awareness** | `Book an appointment` | service cards | **Med** — broad regional term; otherwise duplicate. **DEFECT D12** |
| 14 | `/area-served/inner-peace-in-home-nursing-care-in-lakes-entrance/` | Inner Peace In-Home Nursing & Care in Lakes Entrance - … | Local landing — Lakes Entrance | Local landing (templated) | Book in Lakes Entrance | **Awareness** | `Book an appointment` | service cards | **Low** — duplicate template. **DEFECT D12** |
| 15 | `/area-served/inner-peace-in-home-nursing-care-in-lindenow-south/` | Inner Peace In-Home Nursing & Care in Lindenow South - … | Local landing — Lindenow South | Local landing (templated) | Book in Lindenow South | **Awareness** | `Book an appointment` | service cards | **Low** — duplicate template; low search volume. **DEFECT D12** |
| 16 | `/area-served/inner-peace-in-home-nursing-care-in-paynesville/` | Inner Peace In-Home Nursing & Care in Paynesville - … | Local landing — Paynesville | Local landing (templated) | Book in Paynesville | **Awareness** | `Book an appointment` | service cards | **Low** — duplicate template. **DEFECT D12** |
| 17 | `/book-an-appointment/` | Book an Appointment - Inner Peace In-Home Nursing & Care | The conversion endpoint — multi-step booking widget | Conversion / form | Complete a booking | **Conversion** | `Continue` (booking widget step) | `+61419853811` (tel), `annette@innerpeace.vision` | **Low** (intentionally — convert, not rank) — but **DEFECT D13** (widget shows "No matching data"; "By appointment only" with weak fallback) |
| 18 | `/contact-us/` | Contact Us - Inner Peace In-Home Nursing & Care | Contact, urgent help, brokerage, **employment**, social links | Contact / multi-purpose | Call / message / apply | **Conversion** | `Submit` (contact form) | phone 0419 853 811; `DISC Personal Profile System` & `Interview Form` links; FB/YouTube/IG | **Med** — converts and carries hidden careers + brokerage content that belongs on dedicated pages. **DEFECT D4-adjacent** (careers buried here) |

### 1b. Legal pages — in sitemap (subset of the 18 above, grouped here for clarity)

| # | URL | Page Title (verbatim) | Page Purpose | Content Type | Conversion Intent | Funnel Stage | Primary CTA | Supporting CTA | SEO Value |
|---|---|---|---|---|---|---|---|---|---|
| 19 | `/privacy-policy/` | Privacy Policy - Inner Peace In-Home Nursing & Care | Privacy/health-info handling | Legal | None | **Utility** | none | email/phone in body | **Low** — but content note: page stacks a **legacy** policy (mentions "vehicle"/automotive boilerplate, copy/paste error) above a **new 2026-05-22 policy** citing the Privacy Act 1988, APPs, **Aged Care Act 2024**, Health Records Act 2001, and naming **Inner Peace Services Pty Ltd**. Authoritative funding/legal facts live here, not on commercial pages |
| 20 | `/terms-conditions/` | Terms & Conditions - Inner Peace In-Home Nursing & Care | Website terms of use | Legal | None | **Utility** | none | none | **Low** — generic boilerplate ("Australia Securities and Investments Commision" typo; references vehicle-style boilerplate elsewhere on legal stack) |

> Note: items 19–20 are part of the 18 sitemap URLs; they are split out only for template-family clarity. Sitemap count remains 18 (items 1–20 minus the 2 here would double-count — see §2 for the authoritative grouping).

### 1c. Unlisted utility / recruitment pages — crawled, NOT in sitemap (4)

| # | URL | Page Title (verbatim) | Page Purpose | Content Type | Conversion Intent | Funnel Stage | Primary CTA (verbatim) | Supporting CTA | SEO Value |
|---|---|---|---|---|---|---|---|---|---|
| 21 | `/disc-personal-profile-system/` | DISC Personal Profile System - Inner Peace In-Home Nursing & Care | Carer applicant behavioural assessment (24-item MOST/LEAST) | Recruitment form | Submit DISC profile | **Utility** (recruitment) | `Submit` | `Click here to read the Disc Word Explanation` (PDF) | **Low** — `noindex, follow`; orphaned (only linked from `/contact-us/`). **DEFECT D11** |
| 22 | `/interview-form/` | Interview Form - Inner Peace In-Home Nursing & Care | Carer screening questionnaire (20 questions) | Recruitment form | Submit application | **Utility** (recruitment) | `Send` | none | **Low** — `noindex, follow`; orphaned. Header typo "SCREENING QUESTIONAIRRE". **DEFECT D11** |
| 23 | `/login/` | Login - Inner Peace In-Home Nursing & Care | Staff "Team Login Form" | Auth / utility | Authenticate staff | **Utility** | (login submit) | `Forgot your password?` → `/password-reset/` | **Low** — `noindex, follow` but **publicly reachable in the live surface**. **DEFECT D4** |
| 24 | `/password-reset/` | Password Reset - Inner Peace In-Home Nursing & Care | Staff password reset | Auth / utility | Reset password | **Utility** | (reset submit) | none | **Low** — `noindex, follow`; public surface. **DEFECT D4** |

### 1d. Broken / 404 — actively linked from production (1)

| # | URL | Page Title (verbatim) | Page Purpose | Content Type | Conversion Intent | Funnel Stage | Primary CTA (verbatim) | Supporting CTA | SEO Value |
|---|---|---|---|---|---|---|---|---|---|
| 25 | `/home-care-services/` | Page not found - Inner Peace In-Home Nursing & Care | (intended unknown) — returns 404 | Error (404) | None | **Utility** (error) | `Back To Homepage` → `/` | none | **None / negative** — `statusCode 404`, `noindex, follow`. Yet `/` and `/about-us/` link "personalised care" to its child `/home-care-services/personal-care/`. Live broken-link defect. **DEFECT D1** |

---

## 2. Grouping by Template Family

The crawl reveals **six distinct template families**. The site is built on WordPress 7.0 + Elementor 4.0.8 (`generator` meta, all pages).

| Template family | Pages | Shared signature (from crawl) |
|---|---|---|
| **Service hub + service detail** | `/in-home-nursing-care-services/` (hub); `/personal-care/`, `/social-care/`, `/nursing-care/`, `/foot-care/` (details) | Intro paragraph → itemised task/activity list → service hero image → `Book an Appointment` → "OTHER/OUR SERVICES" 3–4 card grid. `foot-care` is a broken member (stub body, old 2023/11 PNG cards, only 3 sibling cards). |
| **Off-pattern service page** | `/dementia-care/` | Does NOT share the service template or URL path. Section-based modern build (Overview → Support & Services → Specialist Clinical Services → Online Referral Form → Contact). Two CTAs, embedded referral form. Newest mod date (2026-05-18). **DEFECT D2.** |
| **Area hub + area landing** | `/area-served/` (hub); 6× `/area-served/inner-peace-in-home-nursing-care-in-{town}/` | Town pages are byte-for-byte template clones: identical 3-paragraph body with the town name string-swapped, identical hero `image-09-1536x1024-1`, identical `Book an appointment` + identical 4-card service grid. **DEFECT D12.** |
| **Marketing / story / educational** | `/` (home), `/about-us/`, `/in-home-nursing-care-benefits/` | Long-form prose; brand voice; `Book an Appointment` CTA. Home is the only page carrying trust copy + reviews. |
| **Conversion / contact** | `/book-an-appointment/`, `/contact-us/` | Form-centric. Booking = multi-step Elementor widget ("Services / Date & Time / Your Information"); Contact = name/email/message form + tel/social. |
| **Legal** | `/privacy-policy/`, `/terms-conditions/` | Static legal prose, no CTA. Privacy page contains the only references to Aged Care Act 2024 / APP / My Aged Care funding. |
| **Utility / auth / recruitment (unlisted)** | `/login/`, `/password-reset/`, `/disc-personal-profile-system/`, `/interview-form/` | `noindex, follow`; orphaned from public nav; form-only. **DEFECT D4 (auth in public surface), D11 (orphaned careers forms).** |
| **Error** | `/home-care-services/` (404) | `statusCode 404`, `noindex`. **DEFECT D1.** |

---

## 3. Defect Register (from `_facts.md §10`) — Mapped to Inventory Rows

| ID | Defect (evidence) | Affected rows | Framework principle violated (`_facts.md §12`) |
|---|---|---|---|
| **D1** | Broken `/home-care-services/` path: `/` and `/about-us/` both link the words "personalised care" to `/home-care-services/personal-care/`, whose parent returns **404** (`statusCode 404`, "This page could not be found!"). | #1, #2, #25 | "Predictable URLs"; "one consistent path to every service." A dead internal link from the two highest-authority pages bleeds trust and crawl equity. |
| **D2** | URL inconsistency: services live at `/in-home-nursing-care-services/…` but Dementia Care sits at `/dementia-care/`, and the dead `/home-care-services/` pattern is still referenced. | #3–#8, #25 | Prescribed sitemap nests all four services under `Services` with one consistent path. |
| **D3** | Naming inconsistency: "Inner Peace In-Home Nursing & Care" vs **"Inner Peace Vision"** (`team-members` alt, `/dementia-care/` privacy notice: "designated Inner Peace Vision email addresses") vs **"Inner Peace Services"** (`/dementia-care/` consent line; "Inner Peace Services Pty Ltd" in `/privacy-policy/`). | #1, #8, #19 | Brand consistency; trust is built on a single confident identity. |
| **D4** | Auth pages in public surface: `/login/` ("Team Login Form") and `/password-reset/` are reachable, and `/login/` is linked from `/password-reset/`. | #23, #24 | Framework prescribes a **separate, login-protected Staff Portal** distinct from public nav. |
| **D5** | Locale mismatch: `language=en-AU` but `og:locale=en_US` on every page. | all 25 | Mobile-first, AU-audience correctness; clean technical SEO. |
| **D6** | Copy/count mismatch: services hub says "Explore our **three** services below" but renders **four** cards (Personal, Social, Nursing, Dementia). | #3 | "A visitor understands what you do … in five seconds" — internal contradiction undermines clarity. |
| **D7** | Thin content: `/foot-care/` body is "Coming Soon!" only, yet is `index, follow`. Uses stale 2023/11 PNG service cards and shows only 3 sibling cards (omits Dementia). | #7 | Quality bar for indexable pages; avoid thin/placeholder pages competing for crawl budget. |
| **D8** | Testimonials unattributed and bottom-buried on `/` ("OUR CLIENT'S REVIEWS", three quotes, numbered 1–3, no names); no Testimonials page exists. | #1 | "Give reviews room to breathe"; dedicated Testimonials page in prescribed sitemap. |
| **D9** | Missing alt text: `social-care-1.webp` (#5 hero), `Inner-Peace-1024x577.webp` (#1 contact image), `Dementia_Nurse_Consulting-819x1024.png` (#8 hero). | #1, #5, #8 | Accessibility-conscious, WCAG; mobile-first. |
| **D10** | No consolidated "Why Choose Us" trust band: Cert III/CPR/First Aid, insurances, and carer-matching copy are buried inside long home-page paragraphs, not surfaced as badges/pillars. | #1 | Homepage section (C) = 4 trust pillars; trust badges "Fully insured / Cert III qualified / Client-reviewed." |
| **D11** | No careers landing page; DISC + Interview forms are orphaned (`noindex`, linked only from `/contact-us/`). | #21, #22, #18 | "Join our team" recruitment path; Resources consolidates careers entry. |
| **D12** | Area pages are near-identical templated duplicates (town-name swap, same `image-09` hero) — duplicate-content risk. | #10–#16 | Resources hub "consolidates area-served"; quality over quantity. |
| **D13** | Booking "by appointment only" with a multi-step widget but weak affordance; crawl shows the widget rendering "No matching data". | #17 | "Every homepage scroll ends with a clear, friendly invitation to act"; single primary action; click-to-call always reachable. |
| **D14** | No structured data (no JSON-LD LocalBusiness / MedicalBusiness / Review schema in any page's metadata). | all 25 | Performance- & SEO-optimised build target. |
| **D15** | No blog/resources/insights hub for topic authority. | (absent) | Resources hub in prescribed sitemap. |

---

## 4. Pages the Framework Requires That DO NOT Yet Exist

The Strategic Website framework (`_facts.md §12`) prescribes a sitemap and homepage model that the current site only partially satisfies. The following are **required but absent** in the crawl.

| Required page / surface | Framework citation (`_facts.md §12`) | What currently exists instead (crawl evidence) | Why it is required (Inner-Peace-specific) |
|---|---|---|---|
| **Testimonials page** | Prescribed sitemap lists `Testimonials` as a top-level item; homepage model section (D) = "Testimonials given room to breathe"; trust badge "Client-reviewed." | Only 3 unattributed quotes buried at the bottom of `/` under "OUR CLIENT'S REVIEWS" (verbatim incl. the depression-recovery story). No standalone page. | Choosing in-home care is "an emotional, high-trust decision" — the existing reviews are genuine and powerful (e.g., review #2) but invisible. A dedicated page converts them into a ranking, shareable trust asset. Resolves **D8**. |
| **Resources hub** | Prescribed sitemap: `Resources (consolidates area-served + helpful content + careers entry)`. | `/area-served/` exists as a bare link list; `/in-home-nursing-care-benefits/` exists in isolation; no insights/blog; careers forms are orphaned. | Consolidates the 6 duplicate town pages (**D12**), the benefits article, and a careers entry into one authoritative hub — fixing duplicate-content risk and the missing topic-authority hub (**D15**). |
| **Careers / Join-the-team page** | Conversion model: "'Join our team' recruitment path"; homepage closing CTA band (F) includes "Join our team"; Resources consolidates "careers entry." | Recruitment requirement + DISC + Interview forms live only inside `/contact-us/` body and as two orphaned `noindex` pages (`/disc-personal-profile-system/`, `/interview-form/`). | A real careers landing page gives the recruitment funnel a front door, surfaces the "Cert III in Aged Care **or** registered nurse" requirement and the "contact within 5 business days" promise, and de-orphans the two forms. Resolves **D11**. |
| **Consolidated Trust / "Why Choose Us" section** | Homepage section (C): 4 pillars — Cert III/CPR/First Aid, fully insured, personalised matching, locally owned; trust badges "Fully insured / Cert III qualified / Client-reviewed." | Trust facts exist but are buried in long prose on `/` ("Team of Qualified Carers", "Safety is Our Priority", "Personalised Care" paragraphs). No badge band. | The conversion gold (`_facts.md §5`) is real but presentationally weak. Surfacing it as four scannable pillars/badges is the single highest-leverage trust fix. Resolves **D10**. |
| **Staff Portal (separate, login-protected)** | Prescribed: `Staff Portal (separate, login-protected: Dashboard, Policies & Procedures, Training Materials, Employee Documents, Forms & Templates, Staff Announcements, Useful Links)`. | Only a bare `/login/` ("Team Login Form") + `/password-reset/` exist in the public surface, with no portal behind them in the crawl. | Staff/internal surface must be separated from the public site. The portal is the destination the existing login implies but the crawl shows no protected content — only the door. Resolves **D4**. |

---

## 5. Inventory Summary

- **25 URLs total:** 18 in sitemap (16 commercial/marketing + 2 legal) · 4 unlisted utility/recruitment (`noindex`) · 1 broken 404 that is actively linked.
- **Conversion endpoints today:** `/book-an-appointment/` (multi-step widget, currently rendering "No matching data"), `/contact-us/` (form + click-to-call), and `/dementia-care/` (the only page with a purpose-built lead form — the online referral).
- **Highest-value SEO assets:** `/`, `/about-us/`, the services hub + 3 real service pages, and `/dementia-care/`. **Lowest:** 5 of 6 area pages, `/foot-care/`, all utility pages, and the 404.
- **15 defects** carried from `_facts.md §10` are mapped to specific rows in §3; **5 framework-required surfaces** are entirely missing (§4).
- **Most modern reference build:** `/dementia-care/` (mod. 2026-05-18) — the template/quality target the rest of the site should be lifted to.
