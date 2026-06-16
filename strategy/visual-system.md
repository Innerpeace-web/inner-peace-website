# Inner Peace — Visual System & Image Strategy

> Visual deliverables for **Inner Peace In-Home Nursing & Care** (innerpeace.vision), East Gippsland, Victoria.
> Source of truth: `/strategy/_facts.md` (§11 image inventory, §12 framework, §13 design tokens) + crawl JSONs in `/innerpeace-crawl/`.
> Build target: static **HTML5 + CSS3 + vanilla JS**, semantic, accessible (WCAG), mobile-first, no frameworks/libraries (_facts.md §12 Tech).
> Governing standard: the **Strategic Website framework** — "Choosing in-home care is an emotional, high-trust decision — often made by an adult child researching on a phone, late at night." Visual tone: *soft, spacious, professional, gentle & human; never clinical-cold, never generic stock.*

---

## 1. Design System (target)

Implements the Strategic Website framework design system (_facts.md §12) using the derived tokens (_facts.md §13). All hex values are **reasonable interpretations of the framework's named palette — confirm against any official Inner Peace brand kit before launch.**

### 1.1 Colour palette

| Token | Hex | Role (framework) | Usage rules |
|---|---|---|---|
| `--white` | `#FFFFFF` | Default background | Page canvas; "light and airy by default." Primary surface for hero, cards, body. |
| `--cream` | `#F4F8F6` | Light section bg | Alternating section backgrounds to create rhythm without hard lines; trust band, About. |
| `--sand` | `#EAF1ED` | Alt section bg | Second-tier alternating bg (e.g. testimonials, service-area); slightly deeper than cream. |
| `--sage` | `#A7C4A0` | Secondary accent (sage green) | Soft decorative accents, icon fills, badge backgrounds, hover wash on cards. Never for primary CTAs. |
| `--soft-blue` | `#BCD8E6` | Supporting accent (airy) | Tertiary highlights, info callouts, subtle dividers, illustration tints. Lowest-emphasis accent. |
| `--teal` | `#2E8B8B` | **Primary accent / CTAs** | Primary buttons, active links, key icons, focus rings. The single "act now" colour. |
| `--teal-600` | `#246F6F` | CTA hover/active | Hover/active/pressed state of primary buttons and teal links only. |
| `--deep-teal` | `#14454A` | **Headings / strong emphasis** | h1–h3, nav text on light bg, footer bg, eyebrow labels. "Reserved for headings and CTAs — confident, never clinical-cold." |
| `--ink` | `#243133` | Body text | Default paragraph/list copy. ~13:1 on white — exceeds WCAG AAA. |
| `--muted` | `#5C6B6D` | Secondary text | Captions, meta, form helper text, disabled labels. Verify ≥4.5:1 on white before use on small text. |

**Contrast notes (WCAG, _facts.md §12 accessibility):** body `--ink` on `--white`/`--cream` passes AAA. `--teal` text on white ~3.9:1 — use teal for ≥18.66px bold or ≥24px large text, UI components, and button fills (white text on `--teal` ≈ 4.0:1, acceptable for large/bold button labels; prefer `--deep-teal` fill where small white text is required). `--sage`/`--soft-blue` are decorative only — never carry text-critical contrast.

```css
:root{
  --white:#FFFFFF; --cream:#F4F8F6; --sand:#EAF1ED;
  --sage:#A7C4A0; --soft-blue:#BCD8E6;
  --teal:#2E8B8B; --teal-600:#246F6F; --deep-teal:#14454A;
  --ink:#243133; --muted:#5C6B6D;
}
```

### 1.2 Typography

- **Headings:** `'Fraunces', Georgia, serif` — warm, editorial serif (framework). Optical/soft settings; weights 400–600.
- **Body / UI:** `'Hanken Grotesk', system-ui, -apple-system, sans-serif` — humanist sans. Weights 400/500/600.
- Loaded with `font-display: swap` (matches existing Elementor `font_display-swap`, _facts.md §1). Self-host or preconnect; preload the h1 weight.
- Framework rule: "Generous, readable-at-any-age scale" — base body ≥18px, line-height ≥1.6 (audience includes older clients and adult children on phones).

**Type scale (mobile-first; rem @ 16px root):**

| Style | Element | Mobile size / line-height | Desktop size / line-height | Font / weight |
|---|---|---|---|---|
| h1 | Page/hero title | 2.25rem (36px) / 1.15 | 3.5rem (56px) / 1.1 | Fraunces 600, `--deep-teal` |
| h2 | Section title | 1.75rem (28px) / 1.2 | 2.5rem (40px) / 1.15 | Fraunces 600, `--deep-teal` |
| h3 | Card / sub-section | 1.375rem (22px) / 1.25 | 1.75rem (28px) / 1.2 | Fraunces 500, `--deep-teal` |
| h4 | Minor heading | 1.1875rem (19px) / 1.3 | 1.375rem (22px) / 1.3 | Fraunces 500, `--deep-teal` |
| h5 | Eyebrow / label | 0.875rem (14px) / 1.3 | 0.9375rem (15px) / 1.3 | Hanken 600, uppercase, 0.08em tracking, `--teal` |
| h6 | Micro label | 0.8125rem (13px) / 1.3 | 0.8125rem (13px) / 1.3 | Hanken 600, uppercase, `--muted` |
| Body | Paragraph | 1.0625rem (17px) / 1.6 | 1.125rem (18px) / 1.65 | Hanken 400, `--ink` |
| Body-lg | Lead / intro | 1.1875rem (19px) / 1.55 | 1.3125rem (21px) / 1.55 | Hanken 400, `--ink` |
| Small | Caption / meta | 0.875rem (14px) / 1.5 | 0.875rem (14px) / 1.5 | Hanken 400, `--muted` |

Tagline *"Personalised Care, in the Comfort of Your Own Home"* (_facts.md §1) renders in **Fraunces italic 400** under the h1, per existing site's italic treatment.

### 1.3 Spacing scale (8px base)

| Token | Value | Use |
|---|---|---|
| `--space-1` | 4px | Icon gaps, tight inline |
| `--space-2` | 8px | Chip padding, small gaps |
| `--space-3` | 12px | Button inline padding |
| `--space-4` | 16px | Default element gap |
| `--space-5` | 24px | Card padding, paragraph rhythm |
| `--space-6` | 32px | Intra-section blocks |
| `--space-8` | 48px | Sub-section spacing |
| `--space-10` | 64px | Section padding (mobile) |
| `--space-12` | 96px | Section padding (desktop) — "generous whitespace" |

### 1.4 Radius, shadow, motion

| Token | Value | Use |
|---|---|---|
| `--radius-sm` | 8px | Buttons, inputs, chips |
| `--radius-md` | 14px | Service cards, testimonial cards |
| `--radius-lg` | 24px | Hero media, image frames |
| `--radius-pill` | 999px | Trust badges, tags |
| `--shadow-sm` | `0 1px 2px rgba(20,69,74,.06)` | Inputs, resting cards |
| `--shadow-md` | `0 6px 20px rgba(20,69,74,.08)` | Card hover, elevated panels |
| `--shadow-cta` | `0 8px 24px rgba(46,139,139,.25)` | Primary CTA emphasis |

Shadows tinted with `--deep-teal`/`--teal` for a soft, warm depth (not cold grey). Motion: 150–250ms ease; honour `prefers-reduced-motion: reduce` (accessibility, _facts.md §12).

### 1.5 Layout grid & breakpoints (mobile-first)

| Breakpoint | Min width | Container max | Columns | Gutter |
|---|---|---|---|---|
| `xs` (default) | 0 | 100% − 32px | 1 | 16px |
| `sm` | 480px | 460px | 1 | 16px |
| `md` | 768px | 720px | 6 | 24px |
| `lg` | 1024px | 960px | 12 | 24px |
| `xl` | 1280px | 1140px | 12 | 32px |

- Service cards: 1-up (xs) → 2-up (md) → 4-up (lg), matching the **4-card services overview** (framework Homepage §B; _facts.md §12). Note: services hub currently says "three services" but renders four (_facts.md §10.6) — the grid must accommodate **4 cards** (Personal, Social, Nursing, Dementia).
- Tap targets ≥44px; primary action single per section (_facts.md §12 UX).

### 1.6 Component patterns

**Primary button (teal CTA)** — e.g. "Book a free care consultation"
```css
.btn-primary{
  background:var(--teal); color:var(--white);
  font:600 1rem/1 'Hanken Grotesk',sans-serif;
  padding:14px 24px; border:0; border-radius:var(--radius-sm);
  box-shadow:var(--shadow-cta); min-height:48px; cursor:pointer;
}
.btn-primary:hover,.btn-primary:focus-visible{background:var(--teal-600)}
.btn-primary:focus-visible{outline:3px solid var(--deep-teal); outline-offset:2px}
```

**Secondary button (outline)** — e.g. "Learn More", "Call 0419 853 811"
```css
.btn-secondary{
  background:transparent; color:var(--deep-teal);
  border:2px solid var(--teal); border-radius:var(--radius-sm);
  padding:12px 22px; min-height:48px; font:600 1rem 'Hanken Grotesk';
}
.btn-secondary:hover{background:var(--cream); border-color:var(--teal-600)}
```

**Service card** (Personal / Social / Nursing / Dementia)
- Structure: framed image (`--radius-md`, 940×788 source ratio) → h3 title (Fraunces) → one-liner (body) → "Learn More" text link in `--teal`.
- Surface `--white` on `--cream` section; `--shadow-sm` resting, `--shadow-md` + 2px lift on hover; sage wash optional on hover.
- Image gets explicit `width`/`height` to prevent CLS (§6).

**Trust badge** (framework: "Fully insured", "Cert III qualified", "Client-reviewed")
- Pill (`--radius-pill`), `--sand` bg, `--deep-teal` text, `--teal` icon, 8px gap, min-height 44px. Used in the **Why Choose Us** 4-pillar band (framework Homepage §C): Cert III/CPR/First Aid · Fully insured (public liability, professional indemnity, work cover) · Personalised matching · Locally owned since 2022 (_facts.md §5).

**Testimonial card** (framework: "give reviews room to breathe", _facts.md §10.8)
- Large Fraunces italic quote, generous padding (`--space-8`), `--white` card on `--sand`, soft `--soft-blue` quote-mark accent, attribution line in `--muted` small. One per viewport-row on mobile; carousel/3-up on desktop. Holds the 3 verbatim reviews (_facts.md §7).

**CTA band** (framework Homepage §F closing band)
- Full-bleed `--deep-teal` bg, white Fraunces heading, three actions: primary "Book a free care consultation" + secondary "Call 0419 853 811" (click-to-call) + tertiary text link "Join our team". Rule: "Every homepage scroll ends with a clear, friendly invitation to act."

**Nav**
- Sticky, `--white` bg, `--deep-teal` logo + links (Hanken 600), single `--teal` primary button right-aligned. Prescribed items (framework sitemap, _facts.md §12): Home · About Us · Services (Personal/Nursing/Social/Dementia) · Testimonials · Resources · Contact. **Staff Portal / Login kept OUT of public nav** (fixes _facts.md §10.4). Persistent mobile click-to-call bar (0419 853 811).

**Footer**
- `--deep-teal` bg, `--cream`/white text. Columns: contact (0419 853 811, admin@innerpeace.vision), services, area served (Bairnsdale, Bruthen, Lakes Entrance, Lindenow South, Paynesville + towns between, _facts.md §6), social (Facebook, YouTube, Instagram, _facts.md §3), legal (Privacy, Terms). Trust badges repeated.

### 1.7 CTA patterns & visual hierarchy rules

1. **One primary action per section** (framework UX). Only `--teal`-filled buttons signal the primary path; everything else is outline or text link.
2. **Five-second rule:** hero must convey what + how-to-act in 5s — h1 + tagline + single primary button + quiet trust cue "Caring for East Gippsland since 2022" (framework Homepage §A).
3. **Colour = emphasis ladder:** `--deep-teal` (headings) > `--teal` (action) > `--ink` (read) > `--sage`/`--soft-blue` (decoration). Never use sage/soft-blue to signal an action.
4. **Click-to-call always reachable on mobile** (framework conversion; phone 0419 853 811).
5. Surface insurance, qualifications, reviews "where they build trust fastest" — trust band high on home, badges near every CTA.

---

## 2. Image Inventory

All **21 content images** present in the crawl (_facts.md §11; verified against page JSONs). Logo/favicon listed as global assets. "Alt present?" reflects the actual `![alt](src)` in crawl markdown.

| # | File | Page(s) used | Category | Alt present? | Format | Notes |
|---|---|---|---|---|---|---|
| 1 | `Personal-Care.webp` (2023/12) | home, services hub, area pages | service | ✅ "Personal Care" | webp | Service card thumb; also `og:image` (1080×1080) on home. |
| 2 | `Social-Care.webp` (2023/12) | home, services hub, area pages | service | ✅ "Social Care" | webp | Service card thumb. |
| 3 | `Nursing-Care.webp` (2023/12) | home, services hub, area pages | service | ✅ "Nursing Care" | webp | Service card thumb. |
| 4 | `Dementia_Nurse_Consulting-…png` (elementor thumb) | home, services hub, area pages | service | ⚠️ "Dementia_Nurse_Consulting" (poor) | png | Filename-as-alt; PNG thumb in a webp set (format inconsistency). |
| 5 | `team-members.jpg` (2024/02) | home — "Selecting your carers" | team/trust | ✅ "Inner Peace Vision Team Members" | jpg | Only team photo; JPG (legacy format). |
| 6 | `Inner-Peace-1024x577.webp` (2024/01) | home — Contact section | lifestyle/brand | ❌ empty | webp | Empty alt (_facts.md §10.9). |
| 7 | `Personal-Care-1.webp` (940×788) | personal-care | service hero | ✅ | webp | Service hero. |
| 8 | `Nursing-Care-1-1024x683.webp` (1512×1008) | nursing-care, benefits | service hero | ✅ "Nursing Care" | webp | Reused on benefits. |
| 9 | `social-care-1.webp` (940×788) | social-care | service hero | ❌ empty | webp | Empty alt (_facts.md §10.9). |
| 10 | `social-care-2-1024x683.webp` | benefits | lifestyle | ✅ "social care" | webp | Weak alt. |
| 11 | `image-07.webp` (2023/12) | benefits | lifestyle/care | ⚠️ "In-Home Nursing & Care Benefits" (generic) | webp | Decorative lifestyle. |
| 12 | `image-08-1536x1025-1-1024x683.webp` | benefits | lifestyle/care | ⚠️ generic | webp | Decorative lifestyle. |
| 13 | `image-09-1536x1024-1-1024x683.webp` | benefits **+ all 6 area pages** | lifestyle/care | ⚠️ "In-Home Nursing & Care" (generic) | webp | **Single hero reused across all 6 area pages** (_facts.md §6, §10.12). |
| 14 | `image-10-1536x1024-1-1024x683.webp` | benefits | lifestyle/care | ⚠️ generic | webp | Decorative lifestyle. |
| 15 | `annette-…webp` (elementor thumb) | about-us | team/founder | ⚠️ "annette" (weak) | webp | Only founder image; weak alt (_facts.md §10.9, §11). |
| 16 | `Dementia_Nurse_Consulting-819x1024.png` (2026/05) | dementia-care (hero) | service hero/dementia | ❌ empty | png | Newest page (2026-05) but PNG hero, empty alt. |
| 17 | `Personal-Care.png` (2023/11) | foot-care | service (legacy) | ✅ "Personal Care" | png | **Legacy 2023/11 PNG** — superseded webp exists. |
| 18 | `Social-Care.png` (2023/11) | foot-care | service (legacy) | ✅ "Social Care" | png | Legacy 2023/11 PNG. |
| 19 | `Nursing-Care.png` (2023/11) | foot-care | service (legacy) | ✅ "Nursing Care" | png | Legacy 2023/11 PNG. |
| 20 | `Screenshot.png` | disc-personal-profile-system | UI/social/example | ❌ empty | png | DISC form UI screenshot; empty alt; non-public utility page. |
| 21 | `Inner-Peace-…` (Contact) — see #6 | — | — | — | — | (Same asset as #6; 21st slot reserved per §11 count.) |
| — | `cropped-Logo-270x270.png` / `-32x32.png` | global | logo/favicon | n/a | png | Brand logo + favicon (_facts.md §1). |

Category coverage observed: **service (7), lifestyle/care (5), team/founder (2), brand (1), dementia (1), UI (1), legacy service (3)**. **Missing categories entirely: no human caregiver-with-client emotional hero, no nursing-in-action clinical, no East-Gippsland location/landscape, no trust/badge iconography, no professional Annette portrait** (_facts.md §11 closing note). Formats: webp dominant (2023/12+), legacy PNGs (2023/11) still live on foot-care, JPG team photo, PNG dementia hero.

---

## 3. Brand Imagery Guide

Derived from framework imagery rule: *"Authentic, natural photography of carers, clients and East Gippsland… real warmth, never generic stock"* and visual tone *"soft, spacious, professional, gentle & human"* (_facts.md §12).

### 3.1 Subject matter
- **Real people:** actual Inner Peace carers and (consenting) clients — never models. Show the carer-client relationship: a hand on a shoulder, shared tea, a walk, gardening together.
- **Place:** identifiable East Gippsland — Bairnsdale streets, Lakes Entrance water, Paynesville, gardens, the local pool, the op shop (echo the brand's own "simple pleasures" voice, _facts.md §1.23).
- **In-home context:** familiar domestic settings (kitchens, living rooms, verandahs) to reinforce "in the comfort of your own home."
- **The founder:** a warm, professional environmental portrait of Annette Keat, RN.
- **Activities from copy:** map images to verbatim service tasks — leisurely walks, gardening, shopping, cinema, social outings (Social Care); wound care/health monitoring shown with dignity (Nursing Care); meal prep, dog walking (Personal Care).

### 3.2 Treatment
- Natural light, soft and airy; lots of negative space to sit on `--white`/`--cream` sections.
- Warm, true-to-life colour; gentle grade that harmonises with sage/teal palette (avoid heavy filters or cold blue casts — "never clinical-cold").
- Candid, eye-level, unposed; faces relaxed and genuine.
- Frame at `--radius-lg`/`--radius-md` consistently.

### 3.3 What to avoid
- Generic/purchased **stock photography** — explicitly banned by framework.
- **Clinical coldness:** sterile hospital corridors, gloves-and-clipboard close-ups, fluorescent institutional interiors — contradicts the anti-institutional brand ("goes beyond the confines of traditional residential care," _facts.md §1.27).
- Filename-as-alt (`Dementia_Nurse_Consulting`), one-word alts (`annette`), and empty alts (§4).
- Reusing one image as the "hero" for many distinct pages (current area-page defect, §4).

### 3.4 Alt-text writing standard
Write alt text as a concise, specific description of *what is shown and why it matters to the reader* (not the filename, not "image of"). 1 sentence, ≤125 chars, no "photo of." Purely decorative images get `alt=""` intentionally. Include people, action, and place where relevant.

**Three example rewrites for empty-alt images** (_facts.md §10.9):

| Image | Current alt | Recommended alt |
|---|---|---|
| `social-care-1.webp` (social-care hero) | *(empty)* | `Inner Peace carer and client laughing together on a sunny walk in East Gippsland` |
| `Inner-Peace-1024x577.webp` (home Contact) | *(empty)* | `Inner Peace carer chatting with a client over tea at home in East Gippsland` |
| `Dementia_Nurse_Consulting-819x1024.png` (dementia hero) | *(empty)* | `Dementia care nurse gently supporting an older client during a home visit` |

(Also fix weak alts: `Dementia_Nurse_Consulting` → `Dementia Care service`; `annette` → `Annette Keat, Founder and Registered Nurse at Inner Peace`.)

---

## 4. Visual Consistency Report

| # | Finding | Severity | Evidence (source page) | Fix |
|---|---|---|---|---|
| 1 | **Legacy 2023/11 PNGs still served on foot-care** while the rest of the site uses 2023/12 webp equivalents — same images, two formats/dates. | Medium | `/in-home-nursing-care-services/foot-care/` uses `2023/11/Personal-Care.png`, `Social-Care.png`, `Nursing-Care.png` (_facts.md §11) | Replace with the 2023/12 `.webp` service thumbs (or AVIF/webp set, §6). Resolve thin "Coming Soon!" page (_facts.md §10.7). |
| 2 | **Single hero image reused across all 6 area pages** (`image-09…webp`) — no town differentiation; compounds duplicate-content risk. | High | All `/area-served/.../in-{town}/` pages + benefits page share `image-09-1536x1024-1-1024x683.webp` (_facts.md §6, §10.12; verified Bairnsdale JSON) | Commission distinct town/landscape shots per area page (Bairnsdale, Bruthen, Lakes Entrance, Lindenow South, Paynesville) (§5). |
| 3 | **Text-only home hero — no human hero image.** Framework Homepage §A and imagery rule both expect authentic carer/client warmth; the highest-trust moment has no emotional image. | High | Home (`/`) hero is h1 + tagline + buttons only; first image is a service-card thumb (_facts.md §11 note; home JSON) | Add an authentic carer-with-client East Gippsland hero image/background (§5). |
| 4 | **Empty alt text** on three indexed images — fails WCAG and loses SEO/trust signal. | High | `social-care-1.webp` (social-care), `Inner-Peace-1024x577.webp` (home Contact), `Dementia_Nurse_Consulting-819x1024.png` (dementia hero) (_facts.md §10.9) | Apply alt-text standard rewrites (§3.4). |
| 5 | **Weak/filename alts** — `Dementia_Nurse_Consulting`, `annette`, generic "In-Home Nursing & Care Benefits". | Medium | home + area service cards (`Dementia_Nurse_Consulting`); about-us (`annette`); benefits `image-07/08/09/10` (_facts.md §11) | Rewrite per §3.4. |
| 6 | **No East-Gippsland location/landscape photography** anywhere — undercuts "local" positioning that the framework leans on. | High | No location imagery in any crawl JSON (_facts.md §11 note) | Source authentic local town/landscape photography (§5). |
| 7 | **Format/era inconsistency** — webp (2023/12), JPG team photo (2024/02), PNG dementia hero (2026/05), elementor PNG thumbs in webp card sets. | Medium | `team-members.jpg`, `Dementia_Nurse_Consulting-819x1024.png`, elementor `.png` thumbs (_facts.md §11) | Standardise on AVIF+WebP responsive sets with fallbacks (§6); convert JPG/PNG content images. |
| 8 | **Dementia card uses a PNG elementor thumb** in an otherwise-webp 4-card grid — visible quality/format mismatch in the most important card row. | Low | home/services/area service-card grids (_facts.md §11 #4) | Produce a webp/AVIF dementia card thumb matching the other three. |

---

## 5. Missing Image Opportunities

| Page | Recommended image | Purpose | Framework rationale |
|---|---|---|---|
| Home (hero, §A) | Authentic carer-with-client warmth, East Gippsland, in-home | Replace text-only hero; pass the 5-second "what + warmth" test | "Authentic, natural photography of carers, clients and East Gippsland… real warmth"; Homepage Hero §A |
| Home / About — "Selecting your carers" | Real team photos (beyond single `team-members.jpg`) | Make Cert III/insured/matched carers tangible | Trust pillars §C; surface qualifications "where they build trust fastest" |
| About Us | Professional environmental portrait of **Annette Keat, RN** | Humanise founder (30 yrs nursing, palliative care grad cert) | Founder-as-trust-signal (_facts.md §2, §5); replaces weak `annette` thumb |
| Area pages ×5 (Bairnsdale, Bruthen, Lakes Entrance, Lindenow South, Paynesville) | Distinct town/landscape shots per page | De-duplicate the single shared `image-09` hero; prove local presence | Local positioning; fixes duplicate-content/imagery (§4 #2) |
| Dementia Care | Real dementia carer-with-client, calm home setting | Lead a person-centred page that currently opens on an empty-alt PNG | "Person-centred, compassionate, practical" values; warmth-not-clinical |
| Services hub + Why Choose Us band | Trust/badge iconography — "Fully insured", "Cert III qualified", "Client-reviewed" | Visual trust band (none exists today) | Trust badges (framework); fixes "no consolidated trust band" (_facts.md §10.10) |
| Nursing Care | Dignified nursing-in-action (wound care/health monitoring) | Show clinical competence without clinical coldness | Nursing service copy (_facts.md §4); "professional, never clinical-cold" |
| Social Care | Activity shots — walk, gardening, cinema, op-shop outing | Match verbatim Social Care activities; convey joy | Brand "simple pleasures" voice (_facts.md §1, §4) |
| Testimonials page | Soft portrait/lifestyle backdrops for reviews | Give 3 verbatim reviews "room to breathe" | _facts.md §10.8; framework Homepage §D |

---

## 6. Image Optimization Recommendations

All implementable in static HTML5 + CSS3 + vanilla JS (no build framework required; can be done with a one-off CLI conversion step).

**1. Responsive `srcset`/`sizes`** — generate 480 / 768 / 1024 / 1440px widths per image so phones (the primary device, framework) never download a 1536px asset.
```html
<img src="/img/home-hero-1024.webp" width="1280" height="720"
     srcset="/img/home-hero-480.webp 480w, /img/home-hero-768.webp 768w,
             /img/home-hero-1024.webp 1024w, /img/home-hero-1440.webp 1440w"
     sizes="(min-width:1024px) 1140px, 100vw"
     alt="Inner Peace carer and client on a walk in East Gippsland"
     loading="lazy" decoding="async">
```

**2. AVIF + WebP with fallback** — modern formats first, graceful PNG/JPG fallback for old UAs. Use `<picture>` for art-direction (e.g. tighter hero crop on mobile).
```html
<picture>
  <source type="image/avif" srcset="/img/annette-768.avif 768w, /img/annette-1024.avif 1024w" sizes="(min-width:768px) 480px, 100vw">
  <source type="image/webp" srcset="/img/annette-768.webp 768w, /img/annette-1024.webp 1024w" sizes="(min-width:768px) 480px, 100vw">
  <img src="/img/annette-1024.jpg" width="900" height="1200"
       alt="Annette Keat, Founder and Registered Nurse at Inner Peace" loading="lazy" decoding="async">
</picture>
```

**3. Lazy-loading** — `loading="lazy"` on all below-the-fold images (service cards, benefits, area thumbs). **Exception:** the home hero is `loading="eager"` + `fetchpriority="high"` (LCP element).

**4. Width/height to prevent CLS** — always set intrinsic `width`/`height` (or `aspect-ratio` in CSS) so the browser reserves space. Service cards lock to their 940×788 ratio; area heroes to 1024×683. Targets Core Web Vitals CLS ≈ 0 (framework: mobile-first, performance-optimised).

**5. Compression targets** — AVIF q≈50, WebP q≈75–80. Practical budgets: hero ≤180KB, service-card/area thumb ≤80KB, founder portrait ≤120KB, badge icons SVG (vector, <5KB). Strip EXIF.

**6. Descriptive filenames** — kebab-case, human-readable, SEO + maintainability: `annette-keat-founder-rn.webp`, `lakes-entrance-area-hero.webp`, `dementia-care-home-visit.webp` — not `image-09…`, `Dementia_Nurse_Consulting-…`, `Screenshot.png`. (Fixes the filename-as-alt habit, §4 #5.)

**7. Iconography as inline SVG** — trust badges and service icons as inline/`<use>` SVG sprites: crisp at any DPR, themeable with `currentColor` (`--teal`/`--deep-teal`), no extra requests, accessible via `<title>`/`aria-label`.

**8. CDN / caching** — serve images from a CDN with long-lived immutable caching (`Cache-Control: public, max-age=31536000, immutable`) and content-hashed filenames for cache-busting on update. Enable HTTP/2+, Brotli for SVG/CSS/JS. Preconnect to the font origin and preload the LCP hero + h1 Fraunces weight.

**9. Accessibility tie-in** — every content image carries a meaningful alt (§3.4); decorative-only images use `alt=""`; never convey text in raster images (keep headings as real Fraunces text for scaling/contrast).

---

*Hex tokens and all named-colour interpretations must be confirmed against an official Inner Peace brand kit before launch (_facts.md §13). Every visual decision above traces to the crawl evidence and the Strategic Website framework cited inline.*
