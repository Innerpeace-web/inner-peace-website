# Inner Peace In-Home Nursing & Care — Information Architecture

> **Source of truth:** `strategy/_facts.md` + `innerpeace-crawl/*.json` (25 crawled URLs, `page-sitemap.xml`). Governing standard: **Strategic Website framework** (`_facts.md §12`). Nothing invented; every recommendation cites BOTH crawl evidence AND the framework.
> **Scope of the live site:** 18 public/sitemap URLs + 4 crawled-but-unlisted utility pages + 1 broken 404 = the 25 URLs reconciled below.

---

## 1. Current Sitemap (ACTUAL crawled structure)

ASCII tree of the live site exactly as crawled. Problems annotated inline with `← [P#]` markers (keyed to §2).

```
innerpeace.vision/                                         [Home]
│
├── /about-us/                                             [About Us]
│       └─→ links "personalised care" to
│           /home-care-services/personal-care/  ← [P1] DEAD LINK (404 parent)
│
├── /in-home-nursing-care-services/                        [Services hub]
│   │     "Explore our three services below" but shows 4 cards  ← [P7]
│   ├── /in-home-nursing-care-services/personal-care/      [Personal Care]
│   ├── /in-home-nursing-care-services/social-care/        [Social Care]
│   ├── /in-home-nursing-care-services/nursing-care/       [Nursing Care]
│   └── /in-home-nursing-care-services/foot-care/          [Foot Care = "Coming Soon!" thin page] ← [P8]
│
├── /dementia-care/                  ← [P2] OFF-PATTERN: 4th service NOT under /services/ hub
│       (Dementia Care card on hub links here, breaking the URL pattern)
│
├── /in-home-nursing-care-benefits/                        [Benefits — content page, no nav home]
│
├── /area-served/                                          [Area Served hub]
│   ├── …/inner-peace-in-home-nursing-care-in-bairnsdale/      ⎫
│   ├── …/inner-peace-in-home-nursing-care-in-bruthen/         ⎪
│   ├── …/inner-peace-in-home-nursing-care-in-east-gippsland/  ⎬ [P3] 6× near-identical
│   ├── …/inner-peace-in-home-nursing-care-in-lakes-entrance/  ⎪  templated pages,
│   ├── …/inner-peace-in-home-nursing-care-in-lindenow-south/  ⎪  same hero image-09,
│   └── …/inner-peace-in-home-nursing-care-in-paynesville/     ⎭  duplicate-content risk
│
├── /contact-us/                                           [Contact]
├── /book-an-appointment/                                  [Booking widget — "by appointment only"]
│
├── /terms-conditions/                                     [Legal]
├── /privacy-policy/                                       [Legal]
│
│   ─── CRAWLED BUT NOT IN SITEMAP (orphaned / utility) ───
├── /disc-personal-profile-system/   ← [P4] orphaned recruitment form (24-Q DISC, no /careers/ parent)
├── /interview-form/                 ← [P4] orphaned recruitment form (20-Q screening, no /careers/ parent)
├── /login/                          ← [P5] WP staff login exposed on PUBLIC surface
└── /password-reset/                 ← [P5] WP password reset exposed on PUBLIC surface

    ─── REFERENCED BUT BROKEN (404, noindex) ───
    /home-care-services/             ← [P1] "This page could not be found!" — yet linked from / and /about-us/
```

**Counts reconcile to 25:** Home (1) + About (1) + Services hub + 4 service pages (5) + Dementia (1) + Benefits (1) + Area hub + 6 towns (7) + Contact (1) + Booking (1) + 2 legal (2) + 2 recruitment forms (2) + login + password-reset (2) + 1 broken 404 (1) = **25**.

---

## 2. Current IA Problems (evidence + framework rule)

Every problem cites the crawl page where it is observable and the **framework IA rule (`_facts.md §12`)** it violates.

| # | Problem | Crawl evidence (source page) | Framework rule violated (§12) |
|---|---|---|---|
| **P1** | **Broken `/home-care-services/` links.** Home and About both link "personalised care" → `/home-care-services/personal-care/`; the parent `/home-care-services/` returns **404** ("This page could not be found!"). | `/` and `/about-us/` both contain `home-care-services/personal-care` (grep-confirmed); `/home-care-services/` `statusCode: 404`, `robots: noindex` | "predictable URLs"; framework prescribes "one consistent path to every service" — a dead path is the worst failure of predictability |
| **P2** | **Dementia Care off-pattern.** Three services live at `/in-home-nursing-care-services/{service}/` but Dementia sits at root-level `/dementia-care/`. The hub's Dementia card links out of the pattern. | `/in-home-nursing-care-services/` Dementia card → `/dementia-care/`; `_facts.md §4` flags "(not under /services/ — different pattern)" | Prescribed sitemap nests all four under **Services**; "one consistent path to every service" |
| **P3** | **6 duplicate area pages.** Six town pages share one template (only town name swapped) and the **same hero `image-09`**, creating duplicate-content / thin-content risk. | `area-served/…-in-{bairnsdale,bruthen,east-gippsland,lakes-entrance,lindenow-south,paynesville}/`; all reference `image-09-…webp` in `page-sitemap.xml`; `_facts.md §6, §10.12` | Framework consolidates area-served into a single **Resources** entry (map + town list), not six indexable near-duplicates |
| **P4** | **Orphaned DISC / Interview forms.** Two recruitment forms exist but are **not in the sitemap** and have **no `/careers/` parent** — unreachable except by direct link. | `/disc-personal-profile-system/`, `/interview-form/` crawled but absent from `page-sitemap.xml`; `_facts.md §8` "No dedicated /careers/ landing page exists — forms are orphaned" | Framework prescribes a **careers entry under Resources** and a "Join our team" recruitment path |
| **P5** | **Login in public surface.** WordPress `/login/` (Username/Password) and `/password-reset/` are reachable utility pages mixed into the public site. | `/login/` (grep: "Username", "Password", "login" ×6), `/password-reset/`; `_facts.md §9` | "separate internal/external nav"; framework prescribes a **separate, login-protected Staff Portal** |
| **P6** | **Benefits page floating.** `/in-home-nursing-care-benefits/` has rich lifestyle content but no clear parent or nav home. | `/in-home-nursing-care-benefits/` in sitemap; not in any service/hub hierarchy | Prescribed sitemap has no standalone "benefits" node — content belongs in Services / Resources |
| **P7** | **"Three services" vs four.** Hub copy reads "Explore our **three** services below" yet renders **four** cards (Personal, Social, Nursing, Dementia). | `/in-home-nursing-care-services/` body: "Explore our three services below" + 4 cards; `_facts.md §10.6` | "A visitor understands what you do … within five seconds" — a miscount erodes that instant clarity; prescribed Services = 4 (Personal, Nursing, Social, Dementia) |
| **P8** | **Thin Foot Care page indexed.** `/in-home-nursing-care-services/foot-care/` is just "Coming Soon!" with no body, yet `index,follow`. | `/in-home-nursing-care-services/foot-care/` "Coming Soon!"; `_facts.md §4, §10.7` | Mobile-first quality bar; framework wants each service page to build trust, not leak crawl budget to an empty page |
| **P9** | **Booking is a bare widget.** `/book-an-appointment/` is "by appointment only" with a multi-step widget and weak fallback/affordance. | `/book-an-appointment/`; `_facts.md §10.13` | Conversion rule: primary CTA "Book a free care consultation" + click-to-call always reachable |
| **P10** | **No Testimonials home.** 3 unattributed reviews are bottom-buried on the home page; no dedicated page. | `_facts.md §7, §10.8` (home page) | Prescribed sitemap includes top-level **Testimonials**; "give reviews room to breathe" |

---

## 3. Recommended Sitemap (framework-prescribed structure)

Implements `_facts.md §12` prescribed sitemap. Dementia moves **under** `/services/dementia-care/` to fix the pattern (301 from `/dementia-care/`). Public site and Staff Portal are separated.

```
/                                                  Home
│
├── /about/                                        About Us
│
├── /services/                                     Services (hub — 4 cards, copy says "four")
│   ├── /services/personal-care/                   Personal Care
│   ├── /services/nursing-care/                    Nursing Care
│   ├── /services/social-care/                     Social Care
│   └── /services/dementia-care/                   Dementia Care   ← 301 from /dementia-care/
│       (Foot Care = noindex + hidden until ready — see §7)
│
├── /testimonials/                                 Testimonials (reviews given room to breathe)
│
├── /resources/                                    Resources (hub)
│   ├── /resources/areas-served/                   Areas Served (map + single town list, 6 dupes folded in)
│   ├── /resources/funding/                        Funding & Support at Home (SaH) guidance
│   └── /resources/careers/                         Careers — "Join our team" entry
│       ├── /resources/careers/disc-profile/       DISC Personal Profile (re-parented)
│       └── /resources/careers/interview/          Interview Form (re-parented)
│
├── /contact/                                       Contact (phone, email, social, booking entry)
│   └── /contact/book/                              Book a free care consultation
│
└── (footer-only)
    ├── /privacy-policy/
    └── /terms-conditions/

════════════════════════════════════════════════════════════════
STAFF PORTAL  —  separate, login-protected, NOT in public nav (§12)
════════════════════════════════════════════════════════════════
/portal/                                            Staff Portal (login gate)
├── /portal/dashboard/                              Dashboard
├── /portal/policies/                               Policies & Procedures
├── /portal/training/                               Training Materials
├── /portal/documents/                              Employee Documents
├── /portal/forms/                                  Forms & Templates
├── /portal/announcements/                          Staff Announcements
└── /portal/links/                                  Useful Links
        (login / password-reset live inside the portal gate, not public)
```

---

## 4. URL Migration / Redirect Map

Covers **every** current URL including the 404 and all six area pages. Type = **301** throughout (permanent; preserves any link equity, signals canonical move).

| # | Old URL | New URL | Type | Rationale |
|---|---|---|---|---|
| 1 | `/` | `/` | — | Keep. Home unchanged (re-templated per framework six-section model). |
| 2 | `/about-us/` | `/about/` | 301 | Shorter, predictable noun (framework "predictable URLs"). |
| 3 | `/in-home-nursing-care-services/` | `/services/` | 301 | Collapse verbose path to framework's `Services` hub. |
| 4 | `/in-home-nursing-care-services/personal-care/` | `/services/personal-care/` | 301 | Consistent service path. |
| 5 | `/in-home-nursing-care-services/nursing-care/` | `/services/nursing-care/` | 301 | Consistent service path. |
| 6 | `/in-home-nursing-care-services/social-care/` | `/services/social-care/` | 301 | Consistent service path. |
| 7 | `/dementia-care/` | `/services/dementia-care/` | 301 | **Fixes the off-pattern (P2):** 4th service nested under Services hub. |
| 8 | `/in-home-nursing-care-services/foot-care/` | `/services/foot-care/` (noindex, hidden) | 301 | Keep slug consistent but de-list & noindex thin "Coming Soon" (P8, §7). |
| 9 | `/home-care-services/` (**404**) | `/services/` | 301 | **Repoints the dead 404 (P1)** to the real Services hub. |
| 10 | `/home-care-services/personal-care/` (broken link target) | `/services/personal-care/` | 301 | Catch the dead internal links from `/` and `/about-us/` (P1). |
| 11 | `/in-home-nursing-care-benefits/` | `/services/` (or merge into service bodies) | 301 | Benefits content folds into Services; no standalone node (P6). |
| 12 | `/area-served/` | `/resources/areas-served/` | 301 | Areas served becomes one Resources entry (map + list). |
| 13 | `/area-served/…-in-bairnsdale/` | `/resources/areas-served/#bairnsdale` | 301 | Fold duplicate town page into a single anchor (P3). |
| 14 | `/area-served/…-in-bruthen/` | `/resources/areas-served/#bruthen` | 301 | Fold duplicate town page (P3). |
| 15 | `/area-served/…-in-east-gippsland/` | `/resources/areas-served/#east-gippsland` | 301 | Fold duplicate town page (P3). |
| 16 | `/area-served/…-in-lakes-entrance/` | `/resources/areas-served/#lakes-entrance` | 301 | Fold duplicate town page (P3). |
| 17 | `/area-served/…-in-lindenow-south/` | `/resources/areas-served/#lindenow-south` | 301 | Fold duplicate town page (P3). |
| 18 | `/area-served/…-in-paynesville/` | `/resources/areas-served/#paynesville` | 301 | Fold duplicate town page (P3). |
| 19 | `/contact-us/` | `/contact/` | 301 | Predictable noun. |
| 20 | `/book-an-appointment/` | `/contact/book/` | 301 | Booking nested under Contact; aligns CTA "Book a free care consultation" (P9). |
| 21 | `/disc-personal-profile-system/` | `/resources/careers/disc-profile/` | 301 | Re-parent orphaned recruitment form under Careers (P4). |
| 22 | `/interview-form/` | `/resources/careers/interview/` | 301 | Re-parent orphaned recruitment form under Careers (P4). |
| 23 | `/login/` | `/portal/` (login gate) | 301 | Move staff login off public surface into Staff Portal (P5). |
| 24 | `/password-reset/` | `/portal/` (gate handles reset) | 301 | Move reset behind portal gate (P5). |
| 25 | `/privacy-policy/` | `/privacy-policy/` | — | Keep (footer-only). |
| 26 | `/terms-conditions/` | `/terms-conditions/` | — | Keep (footer-only). |

> All 25 crawled URLs accounted for (rows 1–9, 11–24, 25–26; plus the broken-link target row 10). New nodes created by the framework but absent on the live site (`/testimonials/`, `/resources/`, `/resources/funding/`, `/resources/careers/`) have no "old" URL and are net-new.

---

## 5. Navigation Structure

### 5a. Primary navigation (desktop header)
Single primary action present at all times: **Book a free care consultation** (CTA button) + click-to-call. (Framework: "single primary action per section"; CTA "Book a free care consultation"; call 0419 853 811 always reachable.)

| Order | Label | Target | Notes |
|---|---|---|---|
| 1 | Home | `/` | Logo also links home |
| 2 | About | `/about/` | |
| 3 | Services ▾ | `/services/` | Dropdown: Personal · Nursing · Social · Dementia |
| 4 | Testimonials | `/testimonials/` | Net-new (P10) |
| 5 | Resources ▾ | `/resources/` | Dropdown: Areas Served · Funding & SaH · Careers |
| 6 | Contact | `/contact/` | |
| — | **Book a free care consultation** | `/contact/book/` | Teal CTA button, persistent |
| — | **Call 0419 853 811** | `tel:+61419853811` | Click-to-call, persistent (mobile-critical) |

### 5b. Footer navigation
| Column | Items |
|---|---|
| **Services** | Personal Care · Nursing Care · Social Care · Dementia Care |
| **Company** | About · Testimonials · Contact · Careers (`/resources/careers/`) |
| **Resources** | Areas Served · Funding & Support at Home (SaH) |
| **Connect** | Phone 0419 853 811 · admin@innerpeace.vision · Facebook · YouTube · Instagram (`_facts.md §3`) |
| **Legal + utility** | Privacy Policy · Terms & Conditions · **Staff Login → `/portal/`** (single quiet link, segregated) |

### 5c. Mobile navigation (hamburger drawer; mobile-first per §12)
| Order | Label | Target |
|---|---|---|
| Sticky top | **Call 0419 853 811** (tap-to-call, ≥44px) | `tel:+61419853811` |
| Sticky top | **Book consultation** (teal button) | `/contact/book/` |
| 1 | Home | `/` |
| 2 | About | `/about/` |
| 3 | Services (accordion) | Personal · Nursing · Social · Dementia |
| 4 | Testimonials | `/testimonials/` |
| 5 | Resources (accordion) | Areas Served · Funding & SaH · Careers |
| 6 | Contact | `/contact/` |
| Footer of drawer | Staff Login | `/portal/` |

### 5d. Staff Portal navigation (SEPARATE — login-protected, not in public nav)
The 7 portal sections from the framework (`_facts.md §12`):

| Order | Section | Target |
|---|---|---|
| 1 | Dashboard | `/portal/dashboard/` |
| 2 | Policies & Procedures | `/portal/policies/` |
| 3 | Training Materials | `/portal/training/` |
| 4 | Employee Documents | `/portal/documents/` |
| 5 | Forms & Templates | `/portal/forms/` |
| 6 | Staff Announcements | `/portal/announcements/` |
| 7 | Useful Links | `/portal/links/` |

---

## 6. Parent–Child Hierarchy + Breadcrumb Scheme

### 6a. Parent–child hierarchy
| Level 0 | Level 1 | Level 2 |
|---|---|---|
| Home | — | — |
| Home | About | — |
| Home | Services | Personal Care · Nursing Care · Social Care · Dementia Care · (Foot Care – hidden) |
| Home | Testimonials | — |
| Home | Resources | Areas Served · Funding & SaH · Careers |
| Home | Resources › Careers | DISC Profile · Interview Form |
| Home | Contact | Book a consultation |
| Home | (footer) | Privacy Policy · Terms & Conditions |
| **Staff Portal (separate root)** | Dashboard · Policies · Training · Documents · Forms · Announcements · Links | — |

### 6b. Breadcrumb scheme
Format: `Home / [Section] / [Page]` — left-aligned, below header, last crumb non-link. Emit `BreadcrumbList` JSON-LD (closes `_facts.md §10.14` "no structured data"). Examples:

| Page | Breadcrumb |
|---|---|
| Dementia Care | `Home / Services / Dementia Care` |
| Nursing Care | `Home / Services / Nursing Care` |
| Areas Served | `Home / Resources / Areas Served` |
| DISC Profile | `Home / Resources / Careers / DISC Personal Profile` |
| Book consultation | `Home / Contact / Book a free care consultation` |

Staff Portal pages use a separate, in-portal breadcrumb (`Portal / [Section]`) and never expose the public trail.

---

## 7. Service Architecture (5 services, incl. Foot Care)

All services unify under `/services/` to fix the split pattern (P2). The hub renders **four** cards and the copy must say "four" (fixes P7: "Explore our three services below" + 4 cards on `/in-home-nursing-care-services/`).

| Service | New URL | State | IA treatment |
|---|---|---|---|
| Personal Care | `/services/personal-care/` | Live | Full page; verbatim task list (`_facts.md §4`: meals, ironing, grocery, laundry, cleaning, dog walking). |
| Nursing Care | `/services/nursing-care/` | Live | Full page; clinical list (wound mgmt, palliative, medication, pain mgmt). RN founder credential surfaced (`_facts.md §2,§4`). |
| Social Care | `/services/social-care/` | Live | Full page; activities list (walks, cinema, holidays, gardening). |
| Dementia Care | `/services/dementia-care/` | Live (richest page, mod. 2026-05-18) | 4th hub card. **301 from `/dementia-care/`.** Carries its own referral form + SaH content + Lisa Tyter contact 0477 051 130 (`_facts.md §2,§4`). |
| **Foot Care** | `/services/foot-care/` | **"Coming Soon!" — thin (`_facts.md §4,§10.7`)** | **Recommend: HIDE from nav + cards, add `robots: noindex`** until real content exists. Keep slug reserved for a 301 from the old foot-care URL. **Do not show a 4th-and-a-half empty card.** |

**Foot Care rationale:** the live page is "Coming Soon!" only and currently `index,follow` (P8). Framework's mobile-first quality bar and "understand within five seconds" mean an empty page dilutes trust and wastes crawl budget. Noindex + hide now; promote to a live 5th card when content lands.

**Cross-sell pattern:** every service page footer carries the other three service cards (already the live pattern — `page-sitemap.xml` shows Personal/Social/Nursing/Dementia thumbs referenced on each service page) plus the conversion spine (§8).

---

## 8. Conversion Architecture (the conversion spine)

Framework conversion rules (`_facts.md §12`): primary CTA **"Book a free care consultation"**; **click-to-call 0419 853 811 always reachable on mobile**; service Learn-More links; **"Join our team"** recruitment path; surface insurance/qualifications/reviews where they build trust fastest. The spine places four CTA types across the IA:

| CTA | Type | Where it lives across the IA | Evidence / framework anchor |
|---|---|---|---|
| **Book a free care consultation** | Primary booking | Persistent header button (all pages); Home Hero (section A) + Home closing band (section F); end of every Services page; Contact | Framework Homepage six-section model A & F; routes to `/contact/book/` (was `/book-an-appointment/`, P9) |
| **Call 0419 853 811** | Click-to-call | Sticky mobile header (≥44px tap target); header on desktop; Contact; Dementia page also exposes Lisa 0477 051 130 | `_facts.md §3`; framework "click-to-call always reachable on mobile" |
| **Complete Online Referral / Contact Dementia Care** | Referral | Dementia Care page (`/services/dementia-care/`) — provider/SaH referral form retained | `/dementia-care/` CTAs (`_facts.md §4`) |
| **Join our team** | Careers | Home closing CTA band (section F); footer; Resources › Careers landing → DISC + Interview forms | Framework "Join our team" path; fixes orphaned forms (P4, `_facts.md §8`) |

**Trust band feeding conversion (framework section C — "Why Choose Us"):** 4 pillars surfaced near CTAs site-wide — *Cert III + CPR + First Aid · Fully insured (public liability, professional indemnity, work cover) · Personalised carer matching · Locally owned since 2022* (`_facts.md §5, §12`). Render as the framework trust badges ("Fully insured", "Cert III qualified", "Client-reviewed"). This closes `_facts.md §10.10` (trust copy buried in paragraphs).

**Conversion spine summary (every scroll ends with an invitation to act — framework rule):**
```
Home Hero ──► Book consult ┐
Services hub/pages ────────┤
Dementia ──► Referral ─────┼─► /contact/book/  +  tel:+61419853811  (persistent)
Testimonials ──────────────┤
Areas Served ──────────────┘
Careers ──► Join our team ──► DISC + Interview forms
```
