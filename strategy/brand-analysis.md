# Brand Analysis — Inner Peace In-Home Nursing & Care

> Source of truth: `strategy/_facts.md` + `innerpeace-crawl/*.json`. Every claim below is traced to crawl evidence (cited by page) or to the Strategic Website framework (cited as **[FRAMEWORK]**). Nothing is invented. Visual-system detail is deferred to `visual-system.md`.

---

## 1. Brand Essence & Positioning

**Brand essence (one line):** *Personalised nursing-led care that lets East Gippsland locals keep living their own life, in their own home.*

This is distilled directly from verbatim crawl copy, not imposed:

| Essence pillar | Verbatim evidence | Source |
|---|---|---|
| Care that comes to you | Tagline: *"Personalised Care, in the Comfort of Your Own Home"* (italic hero line) | `/` |
| Not an institution | *"Our approach goes beyond the confines of traditional residential care"* | `/`, `/about-us/` |
| Life worth living, not just kept safe | *"cherishing life's simple pleasures, whether it's a refreshing day at the local pool, hosting a social gathering, or exploring hidden treasures at the op shop"* | `/`, `/about-us/` |
| People before process | *"I want to ensure that people always remain at the heart of care"* (Annette) | `/about-us/` |
| Dignity + independence | *"empowering individuals and their families to embrace a fulfilling life within the comfort of their home"* | `/` |
| Enrichment, not maintenance | *"We don't just deliver exceptional in-home care; we make sure that we create opportunities that enrich lives"* | `/` |

**Positioning statement (derived):** For older people and their families in East Gippsland who want care without leaving home, Inner Peace is the **warm, locally-owned, founder/RN-led** in-home nursing and care service that protects **dignity and independence** — the human, anti-institutional alternative to "traditional residential care." It competes not on scale but on **closeness**: a 30-year Registered Nurse founder, locally based since 2022, who matches each carer to the person.

Positioning axes that the copy already owns: **warm** (not clinical), **local** ("the tranquil East Gippsland area"), **founder/RN-led** (Annette front-and-centre), **dignity-and-independence** ("live independently and comfortably in your own home" — `/in-home-nursing-care-services/personal-care/`). The framework reinforces this: *"warm professionalism… confident, never clinical-cold"* **[FRAMEWORK]**.

---

## 2. Messaging Consistency Audit

### 2a. Brand-name usage — the core inconsistency

| Name variant | Where it appears | Source |
|---|---|---|
| **Inner Peace In-Home Nursing & Care** | `og:site_name` and `og:title` on every page; all body headings | All pages (e.g. `/`, `/about-us/`) |
| **Inner Peace Vision** | Privacy notice: *"Submissions are sent to the designated **Inner Peace Vision** email addresses"*; also home image alt *"Inner Peace Vision Team Members"* | `/dementia-care/`, `/` (team-members.jpg alt) |
| **Inner Peace Services** | Contact block heading *"**Inner Peace Services** — Specialist support for dementia care"*; consent line *"I consent to **Inner Peace Services** contacting relevant health/community professionals"* | `/dementia-care/` |
| **Dementia Nurse Consulting** (sub-brand) | H1 of dementia page; reads as a separate practice | `/dementia-care/` |
| **innerpeace.vision** (domain) | URL / "www.innerpeace.vision" CTA | sitemap, `/dementia-care/` |

Four names for one organisation across the site — three of them on a single page (`/dementia-care/`). For a high-trust care decision, this reads as either disorganised or as multiple legal entities. **[FRAMEWORK]** explicitly flags naming inconsistency (`_facts.md` §10.3).

### 2b. Locale + spelling inconsistency

| Issue | Evidence | Source |
|---|---|---|
| Locale tag mismatch | Page `language = en-AU` but `og:locale = en_US` on **every** page | metadata, all pages |
| US spelling on home page | `personalized` ×3, `specialized` ×1, `recognize` ×1, `prioritize` ×1 — in the service cards and trust copy | `/` |
| AU spelling on home page | `personalised` ×6 — in the hero tagline and "About" prose | `/` |
| Service pages skew US | Nursing Care: `personalized` ×5, `specialized` ×4, `prioritize` ×1. Social Care: `personalized` ×5, `specialized` ×1 | `/in-home-nursing-care-services/nursing-care/`, `/social-care/` |
| Founder + dementia pages skew AU | `personalised` ×2 (about), `personalised` ×3 + `centre` ×7 (dementia) | `/about-us/`, `/dementia-care/` |

**The same word is spelled both ways within the home page** ("personalised" in the tagline, "personalized" in the Social Care card directly below it). The newest, most polished page (`/dementia-care/`, modified 2026-05) is consistently Australian; the older 2023 service pages are American — suggesting the US spelling is a legacy template artefact.

### 2c. Recommendation — canonical standard

| Standard | Decision |
|---|---|
| Canonical brand name | **Inner Peace In-Home Nursing & Care** (matches `og:site_name`, the legal-feeling full name). Retire "Inner Peace Vision" and "Inner Peace Services" from public copy; keep `innerpeace.vision` only as the domain. |
| Short form (second reference) | **Inner Peace** (already used naturally in testimonial #2: *"'Inner Peace' I know, definitely helped me…"`) |
| Dementia sub-brand | Demote "Dementia Nurse Consulting" to a service descriptor under the parent name (e.g. "Dementia Care — by Inner Peace In-Home Nursing & Care"), not a standalone brand. |
| Spelling | **Australian English throughout** (personalised, specialised, recognise, prioritise, centre). Matches `en-AU`, the region, and the strongest pages. |
| Locale tag | Set `og:locale = en_AU` to match `language = en-AU`. |

---

## 3. Visual Consistency (high level — see `visual-system.md` for detail)

| Observation | Evidence | Source |
|---|---|---|
| Logo is low-res raster | Only `cropped-Logo-270x270.png` (+ 32×32 favicon) exists; no SVG, no wordmark lock-up | `msapplication-TileImage`, favicon (all pages) |
| Mixed image formats | `.webp` adopted from 2023/12 (most service/lifestyle imagery), but **older 2023/11 PNGs still served on `/foot-care/`** (Personal/Social/Nursing-Care.png) — two generations of the same assets live side by side | `_facts.md` §11; `/foot-care/` |
| Single hero reused across all 6 area pages | Every `/area-served/…{town}/` page uses the **same** `image-09` hero with only the town name swapped | `_facts.md` §6, §10.12 |
| No place-specific or emotional hero | No East-Gippsland landscape/location photography; home page hero is **text-only** (no carer-with-client image) | `_facts.md` §11 |
| Empty alt text on key brand images | `Inner-Peace-1024x577.webp` (home Contact), `social-care-1.webp`, `Dementia_Nurse_Consulting-819x1024.png` all have empty `alt` | `_facts.md` §11 |

Net: visuals are functional but generic and inconsistent in format/resolution — at odds with the framework's *"authentic, natural photography… real warmth, never generic stock"* **[FRAMEWORK]**. Full token/typography/photography direction belongs in `visual-system.md`.

---

## 4. Emotional Positioning & Brand Personality

**Primary archetype: The Caregiver.** The entire copy system is oriented to protect, nurture and serve — *"people always remain at the heart of care"* (`/about-us/`), *"compassion shown to me"* (testimonial 1, `/`), *"comprehensive carer insurances… maintaining a secure environment"* (`/`).

**Secondary archetypes (evidence-backed):**
- **The Everyman / "regular folks"** — life's-simple-pleasures language (op shop, local pool, social gathering) is deliberately ordinary and unpretentious (`/`, `/about-us/`).
- **A touch of Sage / Expert** — the RN founder credentials, palliative grad cert, and clinical service lists (Wound Management, Behaviour Assessment) lend authority without coldness (`/about-us/`, `/dementia-care/`).

**The 13 carer character traits (home page, verbatim):**
> capable · resilient · motivated · determined · joyful · empathetic · enthusiastic · compassionate · open-minded · professional · experienced · contemporary · knowledgeable (`/`)

These map cleanly onto the Caregiver core (empathetic, compassionate, joyful) plus competence signals (capable, professional, experienced, knowledgeable). This list is a brand-personality asset that is currently buried mid-paragraph; it should become a visible "what we look for in a carer" feature.

**Emotional register to own:** reassurance + warmth + quiet competence. The framework names the buyer precisely: *"an adult child researching on a phone, late at night"* **[FRAMEWORK]** — the emotional job is to make that person feel they have found someone who will treat their parent as a person.

---

## 5. Brand Authority & Trust

### 5a. Trust assets that exist (the conversion gold)

| Trust signal | Verbatim / detail | Source |
|---|---|---|
| Founder credentials | RN, *"three decades of experience"*, 12 yrs home-based nursing, **Graduate Certificate in Palliative Care (2020, Australian College of Nursing)** | `/about-us/` |
| Carer qualifications | *"All our carers hold a minimum Certificate III in Aged/Community Care… CPR and First Aid"* | `/` |
| Insurances | *"public liability, professional indemnity, and work cover"* | `/` |
| Personalised matching | carer selected by *"personality, required medical attention, and other specific preferences"* | `/` |
| Tenure / local | *"Ever since 2022… happy clients in the tranquil East Gippsland area"* | `/`, `/about-us/` |
| Testimonials | 3 client reviews (one detailed: staying home, escaping depression, improved wellbeing) | `/` |
| Standards alignment | dementia service *"aligned with aged care standards"*; brokerage with *"accredited home care providers in Bairnsdale"* | `/dementia-care/`, `/contact-us/` |

### 5b. How well is authority *surfaced* today? (vs framework's "surface trust where it builds fastest")

| Asset | Current surfacing | Gap vs **[FRAMEWORK]** |
|---|---|---|
| Insurances / Cert III / CPR | Buried in long body paragraphs near the bottom of home page | Framework wants a **"Why Choose Us" 4-pillar trust band** with visual badges ("Fully insured", "Cert III qualified", "Client-reviewed"). Not present. (`_facts.md` §10.10) |
| Founder authority | Lives only on `/about-us/`; absent from home hero | Framework: surface qualifications "where they build trust fastest" — i.e. on the homepage, not one click deep |
| Testimonials | 3 reviews, **unattributed**, bottom-buried; no testimonials page | Framework: *"give reviews room to breathe"* + dedicated Testimonials page. Not present. (`_facts.md` §10.8) |
| Tenure cue | Stated as prose, not as a quiet hero trust-cue | Framework prescribes hero cue *"Caring for East Gippsland since 2022"*. Not used as a cue. |
| Structured proof | No JSON-LD LocalBusiness / Review schema in crawl | Framework + SEO want machine-readable trust. Absent. (`_facts.md` §10.14) |

**Verdict:** The brand has *strong* authority assets and *weak* presentation of them. Trust copy exists but is paragraph-buried and back-page; the highest-converting signals (insured, qualified, reviewed, RN-founded, since-2022) never appear at the decision moment (home hero / above the fold). This is the single biggest brand-to-web gap.

---

## 6. Brand Voice Guide

**Tone principles (drawn from the copy that already works):**
1. **Dignity first** — speak to the person, not the condition ("people always remain at the heart of care").
2. **Independence, not dependence** — frame care as enabling ("live independently and comfortably in your own home").
3. **Life's simple pleasures** — concrete, local, ordinary joys (op shop, local pool), never abstract.
4. **Plain, warm Australian** — short sentences, no jargon, no corporate hedging.
5. **Quietly competent** — state credentials plainly, let them reassure; don't boast.

### DO / DON'T

| DO (real or aligned with crawl) | DON'T (anti-patterns, some present today) |
|---|---|
| *"Personalised Care, in the Comfort of Your Own Home"* — warm, concrete, benefit-led (`/`) | Don't slip into US spelling — "personalized in-home support" (`/social-care/`) breaks the AU voice |
| *"cherishing life's simple pleasures… exploring hidden treasures at the op shop"* — specific, local, human (`/`) | Don't go abstract/clinical — "encompasses a wide range of specialized… support to ensure your holistic well-being" (`/nursing-care/`) is cold and vague |
| *"goes beyond the confines of traditional residential care"* — positions warmly against institutions (`/`) | Don't sound like a facility or use institutional register ("residential care", "facility", "patient management") |
| *"I want to ensure that people always remain at the heart of care"* — first-person, founder warmth (`/about-us/`) | Don't hide the founder behind passive corporate "we"-only voice |
| *"All our carers hold a minimum Certificate III… CPR and First Aid"* — plain, factual reassurance (`/`) | Don't bury proof in dense paragraphs where it can't be scanned |
| Australian English throughout (personalised, specialised, centre) — as on `/dementia-care/` | Don't mix "Inner Peace Vision / Inner Peace Services / Inner Peace In-Home Nursing & Care" — one name only |
| Speak to the adult-child researcher with reassurance **[FRAMEWORK]** | Don't use generic stock-photo tone in words or imagery — *"authentic, never generic stock"* **[FRAMEWORK]** |

---

## 7. Brand Gap Analysis vs Strategic Website Framework

| # | Gap (current state) | Evidence | Framework principle | Fix |
|---|---|---|---|---|
| 1 | Four brand names in use | `/dementia-care/`, `/` | Consistent identity | Adopt **Inner Peace In-Home Nursing & Care** as canonical; retire Vision/Services from copy (see §2c) |
| 2 | Mixed US/AU spelling, even within one page | `/`, `/nursing-care/`, `/social-care/` | Authentic, consistent voice | Australian English everywhere; fix `og:locale` to `en_AU` |
| 3 | Trust signals buried, no badge band | `_facts.md` §10.10 | *"Surface trust where it builds fastest"*; 4 trust pillars + badges | Add "Why Choose Us" band: Cert III/CPR/First Aid · Fully insured · Personalised matching · Locally owned since 2022 |
| 4 | Testimonials unattributed, bottom-buried, no page | `/`, `_facts.md` §10.8 | *"Give reviews room to breathe"* | Dedicated Testimonials page; attribute (first name + town) with consent; pull one to home |
| 5 | Founder authority one click deep | only `/about-us/` | Surface authority where it converts | Bring RN + 30 yrs + palliative cert into home hero/about-strip |
| 6 | Text-only hero, no human image; generic/reused imagery | `_facts.md` §11; 6 area pages share `image-09` | *"Authentic, natural photography of carers, clients and East Gippsland… real warmth, never generic stock"* | Commission real carer-with-client + local photography; unique image per area page (detail → `visual-system.md`) |
| 7 | Clinical-cold copy on service pages | `/nursing-care/`, `/social-care/` | *"Warm professionalism… confident, never clinical-cold"* | Rewrite service intros in plain, warm AU voice; lead with benefit not "encompasses a wide range of…" |
| 8 | Visual identity undefined / inconsistent assets | low-res PNG logo; webp+PNG mix; `_facts.md` §11 | Fraunces (headings) + Hanken Grotesk (body); teal/deep-teal + sage + soft-blue palette | Build the design system in `visual-system.md`; produce SVG logo; standardise on webp |
| 9 | Dementia sub-brand reads as separate company | `/dementia-care/` H1 "Dementia Nurse Consulting" | One coherent brand | Frame as a *service* of the parent brand, shared visual identity |
| 10 | No structured-data trust (no Review/LocalBusiness schema) | `_facts.md` §10.14 | Surface trust + SEO | Add LocalBusiness/MedicalBusiness + Review JSON-LD at build |

---

### Summary of the brand position to carry into the build
Inner Peace already *says* the right things — warm, local, RN-led, dignity-and-independence, anti-institutional, life's-simple-pleasures. The brand problem is not voice invention but **discipline and surfacing**: one name, one spelling standard (AU), trust assets moved to the decision moment, authentic local imagery, and a defined visual identity. Fix those and the existing copy carries the brand.
