# SEO Strategy — Inner Peace In-Home Nursing & Care (innerpeace.vision)

> Prepared for the team at Inner Peace In-Home Nursing & Care, East Gippsland VIC.
> Grounded entirely in the crawl (`/innerpeace-crawl/*.json`), the fact base (`strategy/_facts.md`), and the Strategic Website framework. Meta titles/descriptions are quoted **verbatim** from the crawl. Where a recommendation comes from the framework rather than the live site, it is labelled **[FRAMEWORK]**.
> Date: 2026-06-16.

The strategic situation in one paragraph: Inner Peace is a high-trust, founder-led RN business (Annette Keat, 30 yrs nursing, palliative care grad cert) with genuine differentiation — Cert III/CPR/First Aid carers, full insurance, personalised carer matching, real testimonials, and a modern Dementia Care/SaH offering. The website undersells all of this. The biggest SEO problems are not content quality but **technical hygiene and structure**: a live broken link from the two most important pages, six near-duplicate town pages that cannibalise each other, a thin "Coming Soon" page that is indexable, an off-pattern Dementia URL, a locale mismatch, zero structured data, and no funding/FAQ/testimonials/blog pages to win informational and funding-related searches. This strategy fixes the hygiene first, then builds topical authority around services, dementia, funding, and place.

---

## 1. Current SEO Audit

Meta titles and descriptions below are **verbatim** from the crawl. Title-length rule of thumb: the visible SERP title truncates around ~60 characters. Every page uses the pattern `{Page} - Inner Peace In-Home Nursing & Care`, and "Inner Peace In-Home Nursing & Care" alone is 34 characters, so almost every title overruns. H1 presence is inferred from the rendered markdown (`# …` / page hero). All public pages carry `robots: index, follow` and `statusCode: 200` unless noted.

| URL | Meta title (verbatim) | Meta description (verbatim) | Title length issue? | H1 present | Indexability | Issues |
|---|---|---|---|---|---|---|
| `/` | `Home - Inner Peace In-Home Nursing & Care` | `At Inner Peace In-Home Nursing & Care, we are committed to providing high-quality, personalised care that promotes well-being and health.` | Borderline (~41 ch) — "Home -" prefix wastes space | Yes — `Inner Peace In-Home Nursing & Care` | Indexable (200) | **Broken internal link**: "personalised care" → `/home-care-services/personal-care/` (404 parent). Testimonials buried & unattributed. No JSON-LD. `og:locale en_US` vs `language en-AU`. |
| `/about-us/` | `About us - Inner Peace In-Home Nursing & Care` | `I envision creating an award-winning In-Home Nursing & Care service that embodies the promise of more care, more respect, more options, and the opportunity to live life to the fullest.` | Yes (~45 ch); "About us" lowercase | Yes | Indexable (200) | **Broken internal link** to `/home-care-services/personal-care/`. Desc is a mission quote, not a search-led summary. Stale (`modified 2023-12-22`). No Person schema for Annette. |
| `/in-home-nursing-care-services/` | `In-Home Nursing & Care Services - Inner Peace In-Home Nursing & Care` | `Welcome to our In-Home Nursing & Care Services, where we provide personalised care, in comfort of home. At Inner Peace In-Home Nursing & Care` | **Yes** (~67 ch, truncates) — brand duplicated | Yes | Indexable (200) | **"Explore our three services" mismatch** — copy says three, four cards shown (Personal, Social, Nursing, Dementia). Dementia card links off-pattern. No ItemList schema. |
| `/in-home-nursing-care-services/personal-care/` | `Personal Care - Inner Peace In-Home Nursing & Care` | `With personal care, our dedicated team of carers is here to provide you with exceptional support in your daily life` | Yes (~50 ch) | Yes | Indexable (200) | No `Service`/`MedicalBusiness` schema. No internal links to relevant town pages. Description has no town/region keyword. |
| `/in-home-nursing-care-services/social-care/` | `Social Care - Inner Peace In-Home Nursing & Care` | `Social Care offers personalized in-home support and social activities tailored to bring joy and excitement into your life.` | Yes (~48 ch) | Yes | Indexable (200) | US spelling "personalized" (en-AU should be "personalised"). No Service schema. Hero image `social-care-1.webp` has empty alt. |
| `/in-home-nursing-care-services/nursing-care/` | `Nursing Care - Inner Peace In-Home Nursing & Care` | `Our nursing care services encompass a wide range of specialized and personalized support to ensure your holistic well-being.` | Yes (~49 ch) | Yes | Indexable (200) | Page hosts wound/palliative/medication content but desc is generic; no "palliative care at home" keyword. US spelling. No Service schema. Not linked to Dementia. |
| `/in-home-nursing-care-services/foot-care/` | `Foot Care - Inner Peace In-Home Nursing & Care` | *(no meta description; og:description auto-generated: "Foot Care Coming Soon! OUR SERVICES Personal Care…")* | Yes (~46 ch) | Yes (but "Coming Soon!") | **Indexable thin page (200)** | **Thin "Coming Soon" content** indexable — quality/thin-content risk. Uses old 2023/11 PNG service cards (format inconsistency). Should be `noindex` or unpublished until built. |
| `/dementia-care/` | `Dementia Care - Inner Peace In-Home Nursing & Care` | *(no meta description; og:description auto-generated from body: "DEMENTIA CARE Dementia Nurse Consulting Specialist Support for Dementia Care…")* | Yes (~50 ch) | Yes | Indexable (200) | **Off-pattern URL** — sits at `/dementia-care/` not under `/in-home-nursing-care-services/`. Missing hand-written meta description. Hero `Dementia_Nurse_Consulting-819x1024.png` empty alt. Best/newest content (modified 2026-05-18) but no FAQ/Service/MedicalBusiness schema. Naming drift: body says "Inner Peace Vision" / "Inner Peace Services". |
| `/in-home-nursing-care-benefits/` | `In-Home Nursing & Care Benefits - Inner Peace In-Home Nursing & Care` | `In-Home Nursing & Care offers numerous benefits, especially for individuals who require assistance with daily activities` | **Yes** (~67 ch, truncates) — brand duplicated | Yes | Indexable (200) | Strongest informational asset; orphaned-ish (few inbound links). No links out to service/town pages. Stale (`2023-12-23`). |
| `/area-served/` | `Area Served - Inner Peace In-Home Nursing & Care` | `Delivering exceptional services to diverse locations, our extensive service network ensures support in every area served, ensuring assistance wherever you are.` | Yes (~48 ch) | Yes | Indexable (200) | Generic, no town keywords in title/desc. Acts as hub for six near-duplicate town pages. |
| `/area-served/…-in-bairnsdale/` | `Inner Peace In-Home Nursing & Care in Bairnsdale - Inner Peace In-Home Nursing & Care` | `Inner Peace is your foremost choice for unparalleled and compassionate In-Home Nursing & Care in Bairnsdale.` | **Yes** (~83 ch) — brand name appears twice | Yes | Indexable (200) | **Duplicate/near-duplicate template** — see note below. |
| `/area-served/…-in-bruthen/` | `Inner Peace In-Home Nursing & Care in Bruthen - Inner Peace In-Home Nursing & Care` | *(template: "…compassionate In-Home Nursing & Care in Bruthen.")* | **Yes** (~80 ch) — brand twice | Yes | Indexable (200) | Duplicate template. |
| `/area-served/…-in-east-gippsland/` | `Inner Peace In-Home Nursing & Care in East Gippsland - Inner Peace In-Home Nursing & Care` | *(template: "…in East Gippsland.")* | **Yes** (~88 ch) — brand twice | Yes | Indexable (200) | Duplicate template; also competes with `/area-served/` for the regional term. |
| `/area-served/…-in-lakes-entrance/` | `Inner Peace In-Home Nursing & Care in Lakes Entrance - Inner Peace In-Home Nursing & Care` | `Inner Peace is your foremost choice for unparalleled and compassionate In-Home Nursing & Care in Lakes Entrance.` | **Yes** (~87 ch) — brand twice | Yes | Indexable (200) | Duplicate template. |
| `/area-served/…-in-lindenow-south/` | `Inner Peace In-Home Nursing & Care in Lindenow South - Inner Peace In-Home Nursing & Care` | *(template: "…in Lindenow South.")* | **Yes** (~88 ch) — brand twice | Yes | Indexable (200) | Duplicate template. |
| `/area-served/…-in-paynesville/` | `Inner Peace In-Home Nursing & Care in Paynesville - Inner Peace In-Home Nursing & Care` | `Inner Peace is your foremost choice for unparalleled and compassionate In-Home Nursing & Care in Paynesville.` | **Yes** (~84 ch) — brand twice | Yes | Indexable (200) | Duplicate template. |
| `/contact-us/` | `Contact Us - Inner Peace In-Home Nursing & Care` | *(no meta description; og:description auto-generated)* | Yes (~47 ch) | Yes | Indexable (200) | Holds funding/brokerage/self-management & careers content but it is buried, not its own page. Missing meta description. |
| `/book-an-appointment/` | `Book an Appointment - Inner Peace In-Home Nursing & Care` | *(no meta description; og:description: "Book an Appointment Welcome! Let's get you set up…")* | Yes (~55 ch) | Yes | Indexable (200) | Conversion page; missing meta description; "by appointment only" widget with weak fallback. |
| `/home-care-services/` | `Page not found - Inner Peace In-Home Nursing & Care` | n/a | n/a | n/a | **404 — NOT indexable** | **Live defect.** Home & About-Us link "personalised care" to its child `/home-care-services/personal-care/`. Dead internal links bleed link equity and harm UX/crawl. |
| `/disc-personal-profile-system/` | *(recruitment form)* | — | — | Yes | Indexable, **not in sitemap** | Orphaned recruitment form; should sit under a Careers page. `Screenshot.png` empty alt. |
| `/interview-form/` | *(recruitment form)* | — | — | Yes | Indexable, **not in sitemap** | Orphaned recruitment form; should sit under a Careers page. |
| `/login/`, `/password-reset/` | *(WP utility)* | — | — | — | Public utility, **not in sitemap** | **[FRAMEWORK]** Separate staff portal from public surface; `noindex` these. |
| `/privacy-policy/`, `/terms-conditions/` | *(legal)* | — | — | Yes | Indexable (200) | Fine; keep, link from footer. |

**Cross-cutting findings (apply to all pages):**

| Finding | Evidence (crawl) | SEO impact |
|---|---|---|
| **No structured data anywhere** | Zero `application/ld+json` / `@type` / `schema.org` matches across `/`, `/dementia-care/`, `/contact-us/` and all crawled pages | No rich results, no entity clarity for Google; missing LocalBusiness, Review, FAQ eligibility |
| **Locale mismatch (en-AU vs en_US)** | Every page: `language: en-AU` but `og:locale: en_US` | Geo/locale signal confusion; trivial to fix |
| **US spelling in en-AU site** | "personalized"/"specialized" on social-care & nursing-care meta | Minor relevance/consistency issue for AU queries |
| **Title pattern wastes pixels** | Brand string duplicated on services-hub, benefits, and all town titles | Truncation; weakens keyword prominence |
| **Brand-name inconsistency (NAP)** | `/dementia-care/` body: "Inner Peace Vision", "Inner Peace Services" vs canonical "Inner Peace In-Home Nursing & Care" | NAP inconsistency hurts local ranking & entity trust |
| **Empty alt text** | `social-care-1.webp`, `Inner-Peace-1024x577.webp`, `Dementia_Nurse_Consulting-819x1024.png`, `Screenshot.png` | Image SEO + accessibility (WCAG) loss |
| **"Three services" mismatch** | `/in-home-nursing-care-services/` copy "Explore our three services" but 4 cards | Content/accuracy signal; confusing |

> **Cannibalisation / duplicate-content note:** The six `/area-served/…` town pages share one template with only the town name swapped — identical structure, same hero image (`image-09`), and a single-sentence description that changes only the place name (verbatim pattern: *"Inner Peace is your foremost choice for unparalleled and compassionate In-Home Nursing & Care in {Town}."*). This is classic doorway-style near-duplication: thin pages competing with each other and with `/area-served/`, diluting local relevance instead of concentrating it. The remedy is the per-town de-duplication strategy in §7.

---

## 2. Keyword Clusters

Clusters are built only from services that actually exist (Personal, Social, Nursing incl. palliative/wound/medication, Dementia, plus funding/SaH/HCP and brokerage referenced on `/contact-us/` and `/dementia-care/`) and the real towns (Bairnsdale, Bruthen, Lakes Entrance, Lindenow South, Paynesville, East Gippsland). Intent: I = informational, C = commercial, T = transactional.

### Cluster A — In-home nursing (head + local)
| Keyword | Intent | Target page |
|---|---|---|
| in-home nursing care | C | `/in-home-nursing-care-services/nursing-care/` |
| in-home nursing care Bairnsdale | C/T | New town page: Bairnsdale (de-duplicated) |
| in-home nursing care East Gippsland | C | `/in-home-nursing-care-services/` (hub) |
| home nursing services Lakes Entrance | C/T | Town page: Lakes Entrance |
| registered nurse home visits Gippsland | C | `/about-us/` + `/in-home-nursing-care-services/nursing-care/` |
| wound care at home / wound management nurse | I/C | `/in-home-nursing-care-services/nursing-care/` |

### Cluster B — Palliative care
| Keyword | Intent | Target page |
|---|---|---|
| palliative care at home Gippsland | C/T | `/in-home-nursing-care-services/nursing-care/` (palliative section → consider dedicated sub-page) |
| in-home palliative care East Gippsland | C | nursing-care page |
| palliative care nurse Bairnsdale | C/T | nursing-care + Bairnsdale town page |
| what is in-home palliative care | I | New resource article |

### Cluster C — Dementia care
| Keyword | Intent | Target page |
|---|---|---|
| dementia care East Gippsland | C/T | `/dementia-care/` |
| in-home dementia care Bairnsdale | C/T | `/dementia-care/` + Bairnsdale page |
| dementia nurse consultant / dementia consulting | C | `/dementia-care/` |
| dementia behaviour support / changed behaviours | I/C | `/dementia-care/` + resource article |
| dementia care for Support at Home recipients | C | `/dementia-care/` (SaH section) |
| how to support someone living with dementia at home | I | New resource article (links to dementia-care) |
| dementia care referral / make a dementia referral | T | `/dementia-care/` (online referral form) |

### Cluster D — Personal care & domestic assistance
| Keyword | Intent | Target page |
|---|---|---|
| personal care at home Lakes Entrance | C/T | `/in-home-nursing-care-services/personal-care/` + town page |
| domestic assistance / home help Bairnsdale | C/T | personal-care page |
| meal preparation, laundry, cleaning home help East Gippsland | C | personal-care page |
| help to stay living at home | I/C | personal-care + benefits page |

### Cluster E — Social support & respite
| Keyword | Intent | Target page |
|---|---|---|
| social support outings East Gippsland | C | `/in-home-nursing-care-services/social-care/` |
| companionship / social care for elderly Paynesville | C/T | social-care + town page |
| respite care at home Gippsland | C/T | social-care (add respite framing) + new resource |
| transport and social activities for seniors | I/C | social-care page |

### Cluster F — Aged care at home (local)
| Keyword | Intent | Target page |
|---|---|---|
| aged care at home Paynesville | C/T | Town page: Paynesville |
| home care for elderly Bruthen / Lindenow South | C/T | Town pages |
| in-home aged care East Gippsland | C | `/in-home-nursing-care-services/` hub |

### Cluster G — Funding (Support at Home / Home Care Packages) — biggest informational gap
| Keyword | Intent | Target page |
|---|---|---|
| Support at Home provider Victoria | C/T | **New** Funding page |
| Support at Home program explained | I | **New** Funding/Resources article |
| Home Care Package provider East Gippsland | C/T | **New** Funding page |
| self-managed home care package Gippsland | I/C | **New** Funding page (self-management referenced on `/contact-us/`) |
| brokerage home care provider Bairnsdale | C | **New** Funding page (brokerage referenced on `/contact-us/`) |
| how much does in-home care cost | I | **New** Pricing/Funding article |

### Cluster H — Brand & conversion
| Keyword | Intent | Target page |
|---|---|---|
| Inner Peace In-Home Nursing & Care | Navigational | `/` |
| book a care consultation East Gippsland | T | `/book-an-appointment/` |
| in-home care jobs / aged care jobs Bairnsdale | C/T | **New** Careers page |

---

## 3. Topic Clusters / Content Hubs (Pillar → Cluster)

Hub-and-spoke model. Each pillar is a strong page that links down to specific spokes; spokes link back up to the pillar and laterally to siblings. This concentrates topical authority and fixes the current "flat, orphaned" structure.

```
PILLAR 1 — Services hub  (/in-home-nursing-care-services/)   [exists]
  ├─ Personal Care      (/…/personal-care/)        [exists]
  ├─ Social Care        (/…/social-care/)          [exists]
  ├─ Nursing Care       (/…/nursing-care/)         [exists]
  │     └─ Palliative care at home (spoke)         [NEW sub-page/section]
  ├─ Foot Care          (/…/foot-care/)            [thin — build or noindex]
  └─ → links across to Dementia pillar

PILLAR 2 — Dementia hub  (/dementia-care/)   [exists, strongest content]
  ├─ Dementia behaviour support                    [NEW article]
  ├─ Supporting someone with dementia at home      [NEW article]
  ├─ Dementia care for Support at Home recipients  [section → links to Funding pillar]
  └─ Online referral (conversion)                  [exists]

PILLAR 3 — Funding hub  (/funding/ or /home-care-funding/)   [NEW]
  (referenced today only inside /contact-us/ & /dementia-care/)
  ├─ Support at Home (SaH) explained               [NEW]
  ├─ Home Care Packages (HCP)                       [NEW]
  ├─ Self-managing your package                     [NEW]
  └─ Brokerage with accredited Bairnsdale providers [NEW]

PILLAR 4 — Local / Area hub  (/area-served/)   [exists]
  ├─ Bairnsdale   ├─ Bruthen   ├─ Lakes Entrance
  ├─ Lindenow South   ├─ Paynesville   └─ East Gippsland
  (each de-duplicated — see §7; each links to relevant Service pillar pages)

PILLAR 5 — Caregiving-at-home advice / Resources  (/resources/ or /blog/)   [NEW]
  (seed from existing /in-home-nursing-care-benefits/)
  ├─ Benefits of in-home care vs residential care   [exists → move under hub]
  ├─ How to choose an in-home care provider         [NEW]
  ├─ Staying independent at home (daily living)     [NEW]
  └─ Funding & dementia explainers (cross-link to Pillars 2 & 3)
```

**[FRAMEWORK]** The Strategic Website framework prescribes a `Resources` hub consolidating area-served + helpful content + careers entry. Pillar 5 is that hub; Pillar 4 nests under it for users while keeping crawlable `/area-served/` URLs.

---

## 4. Internal Linking Opportunities

Current crawl shows a flat, sparse link graph: the benefits page links out to almost nothing, service pages don't link to towns, dementia is isolated, and two key pages point at a 404. Recommended links:

| From | To | Anchor (suggested) | Why / crawl evidence |
|---|---|---|---|
| `/` ("personalised care") | `/in-home-nursing-care-services/personal-care/` | "personalised care" | **Fixes broken link** — currently points to 404 `/home-care-services/personal-care/` (confirmed on `/`) |
| `/about-us/` ("personalised care") | `/in-home-nursing-care-services/personal-care/` | "personalised care" | **Fixes broken link** — same 404 confirmed on `/about-us/` |
| `/in-home-nursing-care-benefits/` | Personal / Social / Nursing / Dementia pages | service names | Benefits page is the best informational asset but links out to nothing; route its authority into commercial pages |
| `/in-home-nursing-care-benefits/` | `/funding/` (new) | "how in-home care is funded" | Connect advice → funding intent |
| `/dementia-care/` | `/in-home-nursing-care-services/nursing-care/` | "nursing care" / "palliative care" | Dementia clients often need clinical/palliative nursing; currently isolated |
| `/dementia-care/` | `/funding/` (new) SaH section | "Support at Home (SaH)" | Dementia page already names SaH recipients; link to funding hub |
| `/in-home-nursing-care-services/nursing-care/` | `/dementia-care/` | "specialist dementia support" | Reciprocal link; nursing ↔ dementia |
| Each Service page | Relevant town pages | e.g. "nursing care in Bairnsdale" | No service→town links exist today; build local relevance |
| Each town page | Relevant Service pages + `/book-an-appointment/` | service names + "book a consultation" | Town pages currently dead-end; give them outbound equity & a CTA |
| `/in-home-nursing-care-services/` (hub) | `/dementia-care/` | "Dementia Care" | Hub already shows a Dementia card; ensure crawlable contextual link and fix "three services" copy |
| `/contact-us/` (careers/brokerage copy) | `/careers/` (new), `/funding/` (new) | "Join our team" / "funding options" | Surfaces orphaned recruitment forms (`/disc-personal-profile-system/`, `/interview-form/`) and funding content |
| Footer (global) | Services, Dementia, Funding, Resources, Testimonials, Contact | nav labels | Sitewide link distribution; **[FRAMEWORK]** predictable nav |
| `/in-home-nursing-care-services/foot-care/` | (until built) self-canonical + remove from internal nav | — | Stop passing equity into a "Coming Soon" page |

---

## 5. Missing Pages

| Page | Target keywords | Rationale / framework |
|---|---|---|
| **FAQ** (`/faq/`) | "how much does in-home care cost", "what is Support at Home", "do you cover {town}", "are your carers qualified" | Captures long-tail informational intent; powers `FAQPage` schema (§6). **[FRAMEWORK]** trust-building. |
| **Funding / Pricing** (`/funding/`) | "Support at Home provider Victoria", "Home Care Package provider East Gippsland", "self-managed package", "brokerage Bairnsdale", "cost of in-home care" | **Pillar 3.** Funding is currently buried in `/contact-us/` & `/dementia-care/`; highest-value commercial-informational gap. |
| **Testimonials** (`/testimonials/`) | "Inner Peace reviews", "in-home care reviews East Gippsland" | The 3 home-page testimonials are buried & unattributed; a page powers `Review`/`AggregateRating` schema. **[FRAMEWORK]** "give reviews room to breathe." |
| **Careers / Join Our Team** (`/careers/`) | "aged care jobs Bairnsdale", "in-home carer jobs East Gippsland", "RN jobs Gippsland" | Recruitment forms (`/disc-personal-profile-system/`, `/interview-form/`) are orphaned & not in sitemap; framework's "Join our team" path. |
| **Richer per-town pages** (rebuild 6 existing) | "in-home nursing care {town}", "aged care at home {town}" | De-duplicate the near-identical templates (§7); unique local content per town. **Pillar 4.** |
| **Resources / Blog** (`/resources/`) | dementia/funding/independence explainers; "benefits of in-home care vs residential" | **Pillar 5** topical authority hub; seed with existing `/in-home-nursing-care-benefits/`. **[FRAMEWORK]** Resources hub. |
| **Palliative care** (sub-page or strong section) | "palliative care at home Gippsland", "in-home palliative care" | Annette holds a Palliative Care grad cert — a genuine, ownable differentiator currently invisible in URLs/meta. |
| **Foot Care** (finish the thin page) | "foot care at home", "nurse foot care Bairnsdale" | Replace "Coming Soon!"; until then `noindex`. |

---

## 6. Schema Opportunities (JSON-LD)

The crawl contains **no structured data at all** (zero `ld+json`). Note: the production build target is **static HTML5/CSS/JS**, so schema is **hand-embedded** in each page's `<head>` (not plugin-generated) — keep one source-of-truth snippet per type and template it during build.

| Type | Where | Key fields (from facts) |
|---|---|---|
| `MedicalBusiness` / `LocalBusiness` (use `@type: ["MedicalBusiness","LocalBusiness"]`) | Home + sitewide | name "Inner Peace In-Home Nursing & Care", telephone +61419853811, email admin@innerpeace.vision, `areaServed` [Bairnsdale, Bruthen, Lakes Entrance, Lindenow South, Paynesville, East Gippsland], `priceRange`, `medicalSpecialty: Nursing`, `foundingDate 2022`, logo URL |
| `Organization` + `sameAs` | Home | sameAs → facebook.com/innerpeace.vision, youtube.com/@innerpeace.vision7778, instagram.com/innerpeace.vision; legalName canonical (fixes naming drift) |
| `Person` | `/about-us/` | Annette Keat — Registered Nurse, "Graduate Certificate in Palliative Care (2020, Australian College of Nursing)", `jobTitle` Founder & Director, `worksFor` Org |
| `Service` (one per service) | Personal/Social/Nursing/Dementia pages | `serviceType`, `provider` (Org), `areaServed`, description; link Dementia `Service` to MedicalBusiness |
| `Review` + `AggregateRating` | `/testimonials/` (new) | The 3 verbatim home-page testimonials; mark `reviewBody`; aggregate cautiously (testimonials are unattributed/unrated — attribute first names + ratings before publishing ratings) |
| `FAQPage` | `/faq/` (new) | Q&As on cost, SaH, coverage, qualifications |
| `BreadcrumbList` | All deep pages | Home › Services › {Service}; Home › Area › {Town} — reinforces hierarchy and the consistent URL pattern |
| `WebSite` + `SearchAction` (optional) | Home | sitelinks search box eligibility |

> Caution on `AggregateRating`: Google requires reviews to be genuine and ideally attributed. Add at least first names/initials and a rating value before emitting rating schema, to stay within guidelines.

---

## 7. Local SEO

| Area | Current state (crawl) | Action |
|---|---|---|
| **NAP consistency** | Canonical "Inner Peace In-Home Nursing & Care" but `/dementia-care/` body uses "Inner Peace Vision" and "Inner Peace Services" | Standardise to one legal/brand name everywhere (site, GBP, schema, footer). Fix dementia-care copy. |
| **Google Business Profile** | Not in crawl scope, but essential for a local service-area business | Create/claim GBP as a **service-area business** (no public address) covering the six towns; categories: Home health care service, Nursing agency; add services, photos (real East Gippsland imagery), phone 0419 853 811, hours "By appointment", and push the 3 testimonials toward Google reviews. |
| **Per-town landing strategy (de-dup)** | 6 near-identical templated pages (only town name + one-sentence desc change), same hero `image-09` — cannibalisation/doorway risk | Rebuild each town page with **unique** content: local travel/coverage notes, which services are offered there, a local testimonial if available, distinct hero image, town-specific title (drop the duplicated brand suffix), and links to relevant service pages + Book CTA. Keep East Gippsland as the **regional** page and the six towns as **sub-locality** pages so they stop competing. |
| **Locale / hreflang** | `language: en-AU` but `og:locale: en_US` on every page | Set `og:locale = en_AU`, `<html lang="en-AU">`, and (single-locale site) a self-referencing `hreflang="en-au"`. Convert "personalized/specialized" → "personalised/specialised". |
| **Local content depth** | Town pages are thin | Add genuinely local signals (towns "in between", travel willingness, brokerage with accredited Bairnsdale providers per `/contact-us/`). |

---

## 8. Technical SEO

| Item | Current state (crawl) | Action |
|---|---|---|
| **Broken link / 404** | `/home-care-services/` is 404 yet linked from `/` and `/about-us/` | Fix the two links to `/in-home-nursing-care-services/personal-care/`; 301 `/home-care-services/*` → correct service URLs. |
| **URL consistency** | Services under `/in-home-nursing-care-services/…` but Dementia at `/dementia-care/`; dead `/home-care-services/` pattern referenced | **[FRAMEWORK]** "one consistent path to every service." On the new static build, place Dementia under the services path and 301 the old `/dementia-care/` URL (preserve equity — it's the most-modified page). |
| **Sitemap** | `sitemap_index.xml` + `page-sitemap.xml` exist; recruitment forms & utility pages excluded | On migration, regenerate XML sitemap for the new static site; include Services, Dementia, Funding, Testimonials, FAQ, Resources, Careers, town pages; exclude `/login/`, `/password-reset/`, thin `/foot-care/` until built. |
| **Canonicals** | Not confirmed present in crawl | Add self-referencing canonicals on every page; canonical the six town pages to themselves (not to `/area-served/`) once de-duplicated. |
| **Redirects (migration)** | WordPress → static HTML migration planned | Build a 301 map: every current indexable URL → new equivalent; consolidate `/home-care-services/*` and (optionally) `/dementia-care/`. Preserve `/in-home-nursing-care-benefits/` under the Resources hub. |
| **Thin/indexable page** | `/foot-care/` "Coming Soon!" is `index,follow` | `noindex` or unpublish until real content exists. |
| **Robots / indexation** | Public `/login/`, `/password-reset/` indexable | `noindex` utility pages; **[FRAMEWORK]** separate staff portal from public surface. |
| **Core Web Vitals** | Currently WordPress 7.0 + Elementor 4.0.8 | The static HTML/CSS/vanilla-JS build is a **major CWV advantage** — no Elementor bloat, inline critical CSS, lazy-load images, serve WebP (already adopted 2023/12), preconnect to Google Fonts (Fraunces/Hanken Grotesk), target green LCP/CLS/INP. |
| **Mobile-first** | **[FRAMEWORK]** decision often made on a phone, late at night | Mobile-first layout, ≥44px tap targets, persistent click-to-call 0419 853 811, single primary CTA "Book a free care consultation". |
| **Structured data** | None present | Hand-embed JSON-LD per §6 in the static build. |
| **Image SEO/alt** | Empty alts on `social-care-1.webp`, `Inner-Peace-1024x577.webp`, `Dementia_Nurse_Consulting-819x1024.png`, `Screenshot.png`; weak alts ("annette", "Dementia_Nurse_Consulting") | Write descriptive, keyword-aware alt text during rebuild. |

---

## Prioritised Roadmap (Now / Next / Later)

| Priority | Action | Cluster/§ | Effort | Impact |
|---|---|---|---|---|
| **NOW** | Fix broken `/home-care-services/personal-care/` links on `/` & `/about-us/`; 301 `/home-care-services/*` | §4, §8 | Low | High (live defect, equity loss) |
| **NOW** | `noindex` or unpublish thin `/foot-care/` "Coming Soon" page | §1, §8 | Low | Med (thin-content risk) |
| **NOW** | Fix locale: `og:locale=en_AU`, `<html lang=en-AU>`, AU spelling | §7, §8 | Low | Med |
| **NOW** | Fix "three services" copy → four; standardise brand name (remove "Inner Peace Vision/Services") | §1, §7 | Low | Med (NAP/accuracy) |
| **NOW** | Create / claim Google Business Profile (service-area, 6 towns) | §7 | Low–Med | High (local) |
| **NEXT** | Add JSON-LD: MedicalBusiness/LocalBusiness, Organization+sameAs, Person (Annette), Service ×4, BreadcrumbList | §6 | Med | High |
| **NEXT** | Write proper meta descriptions for foot-care, dementia-care, contact, book; shorten title pattern | §1 | Low | Med |
| **NEXT** | Build internal links: benefits→services, service↔town, dementia↔nursing, contact→careers/funding | §4 | Med | High |
| **NEXT** | De-duplicate 6 town pages with unique local content + distinct heroes; shorten titles | §1, §7 | Med–High | High (cannibalisation) |
| **NEXT** | Add descriptive alt text to images during rebuild | §8 | Low | Low–Med |
| **NEXT** | Build Funding page (SaH/HCP/self-management/brokerage) + FAQPage schema | §3, §5, §6 | Med | High (commercial gap) |
| **LATER** | Build Testimonials page + Review/AggregateRating schema (attribute first) | §5, §6 | Med | Med–High (conversion) |
| **LATER** | Build Careers page; surface DISC & Interview forms | §5 | Med | Med |
| **LATER** | Launch Resources/blog hub seeded from benefits page; palliative-care page | §3, §5 | High | High (long-term authority) |
| **LATER** | Static-site migration: regenerate sitemap, self-canonicals, 301 map (incl. `/dementia-care/` if path changes), CWV optimisation | §8 | High | High (foundation) |
