# Inner Peace — Extracted Fact Base (Single Source of Truth)

> This file distils **only what is present in the crawl** (`./innerpeace-crawl/*.json`, `innerpeace-mapping.json`, sitemaps) plus the **Strategic Website framework** (https://innerpeace-web.github.io/Strategic-Website/). Every strategy document and the website build trace back to these facts. Nothing here is invented; where the framework prescribes something not yet on the site, it is labelled **[FRAMEWORK]**.

---

## 1. Brand Identity (crawl-verified)

| Field | Value | Source |
|---|---|---|
| Legal/brand name | **Inner Peace In-Home Nursing & Care** | All pages `og:site_name` |
| Alt name in use (inconsistency) | "Inner Peace Vision", "Inner Peace Services" | `/dementia-care/` body ("designated Inner Peace Vision email addresses", "Inner Peace Services") |
| Domain | innerpeace.vision | sitemap |
| Tagline | *Personalised Care, in the Comfort of Your Own Home* | `/` (home hero, italic) |
| Mission line | "we are committed to providing high-quality, personalised care that promotes well-being and health" | `/`, `/about-us/` |
| Brand promise | "more care, more respect, more options, and the opportunity to live life to the fullest" | `/about-us/` (Annette) |
| Founded | 2022 ("Ever since 2022…") | `/`, `/about-us/` |
| Region | East Gippsland, Victoria, Australia | multiple |
| Language | `en-AU` (but `og:locale = en_US` — inconsistency) | metadata all pages |
| Platform | WordPress 7.0 + Elementor 4.0.8 | `generator` meta |
| Logo | /wp-content/uploads/2023/12/cropped-Logo-270x270.png (favicon 32x32) | `msapplication-TileImage`, `favicon` |

### Brand voice (verbatim cues)
- "cherishing life's simple pleasures, whether it's a refreshing day at the local pool, hosting a social gathering, or exploring hidden treasures at the op shop" (`/`, `/about-us/`)
- "we make sure that we create opportunities that enrich lives" (`/`)
- "empowering individuals and their families to embrace a fulfilling life within the comfort of their home" (`/`)
- Tone: warm, local, dignity-centred, anti-institutional ("goes beyond the confines of traditional residential care").

---

## 2. People

| Person | Role | Credentials | Contact | Source |
|---|---|---|---|---|
| **Annette Keat** | Founder & Director, Registered Nurse | 30 yrs nursing experience; 12 yrs home-based nursing; **Graduate Certificate in Palliative Care (2020, Australian College of Nursing)** | 0419 853 811 / annette@innerpeace.vision | `/about-us/`, `/dementia-care/` |
| **Lisa Tyter** | Dementia Care contact | — | 0477 051 130 | `/dementia-care/` |

Annette's mission (verbatim): *"I want to ensure that people always remain at the heart of care."* and "I envision creating an **award-winning** In-Home Nursing & Care service…" (`/about-us/`).

---

## 3. Contact & Social (crawl-verified)

| Channel | Value | Source |
|---|---|---|
| Primary phone | **0419 853 811** (intl `+61419853811`) | `/contact-us/`, `/book-an-appointment/`, `/dementia-care/` |
| Dementia phone (Lisa) | 0477 051 130 | `/dementia-care/` |
| General email | admin@innerpeace.vision | mapping.json |
| Bookings email | annette@innerpeace.vision | `/book-an-appointment/` |
| Dementia email | dementiacare@innerpeace.vision | `/dementia-care/` |
| Facebook | facebook.com/innerpeace.vision | `article:publisher`, `/contact-us/` |
| YouTube | youtube.com/@innerpeace.vision7778 | `/contact-us/` |
| Instagram | instagram.com/innerpeace.vision | `/contact-us/` |
| Availability | "By appointment only"; urgent help "even outside regular business hours" | `/book-an-appointment/`, `/contact-us/` |

---

## 4. Services (crawl-verified)

| Service | URL | Hero image | One-liner | Source |
|---|---|---|---|---|
| **Personal Care** | /in-home-nursing-care-services/personal-care/ | Personal-Care-1.webp (940×788) | "exceptional support in your daily life… live independently and comfortably in your own home" | service page |
| **Social Care** | /in-home-nursing-care-services/social-care/ | social-care-1.webp (940×788) | "personalized in-home support and social activities tailored to bring joy and excitement into your life" | service page |
| **Nursing Care** | /in-home-nursing-care-services/nursing-care/ | Nursing-Care-1-1024x683.webp (1512×1008) | "specialized and personalized support to ensure your holistic well-being" | service page |
| **Dementia Care** | /dementia-care/ *(NOTE: not under /services/ — different pattern)* | Dementia_Nurse_Consulting-819x1024.png | "Compassionate, personalised support for people living with dementia, their families, carers, and care providers across East Gippsland" | `/dementia-care/` |
| **Foot Care** | /in-home-nursing-care-services/foot-care/ | (none) | "Coming Soon!" — **empty/thin page** | service page |

### Personal Care — task list (verbatim)
Preparation of Simple Meals · Ironing · Grocery Shopping · Laundry Assistance · Floor Sweeping · General Cleaning Tasks · Dusting and Polishing · Vacuuming · Dog Walking Support.

### Nursing Care — clinical services (verbatim)
Wound Management · Palliative Care · Health Monitoring/Medication Management · Pain Management · plus: Guided Outdoor Activities, Nutritional Support, Assistance with Activities, Coordination of Allied Health Services, Physical Activities, Transportation and Support, Individualized Pain Management Plans.

### Social Care — activities (verbatim)
Leisurely Walks · Cinema · Events & Gatherings · Creative Poetry Sessions · Explore the Internet Together · Tourist Attractions · Meaningful Conversations · Plan & Go On Holidays · Share Life Stories & Memoirs · Shopping for Essentials · Gardening Together.

### Dementia Care (newest page, modified 2026-05-18; most modern build)
- Sub-brand: "Dementia Nurse Consulting"; "Specialist Support for Dementia Care".
- **Who we support:** people living with dementia (all stages); **Support at Home (SaH)** recipients; families & carers; home care recipients; aged care & community providers.
- **How we help:** personalised care planning; family/carer guidance; changed-behaviour support & dementia strategies; provider support; wellbeing/independence/quality of life.
- **Specialist clinical services:** Behaviour Assessment & Support; Individualised Care Planning; Family & Carer Support; Provider & Workforce Consultation; Quality of Life Strategies; Assessment & Ongoing Support (cognitive assessment, geriatric assessment, diagnosis support).
- Has a full **online referral form** (provider details, SaH level, client details, ATSI background, Medicare/DVA, reason for referral, care team, home-visit risk assessment, privacy notice, 3 consent checkboxes).
- CTAs: "Complete Online Referral", "Contact Dementia Care".
- Values chips: Person-centred · Compassionate · Practical · Aligned with aged care standards.

---

## 5. Trust Signals (crawl-verified — the conversion gold)

- **All carers hold minimum Certificate III in Aged/Community Care** + **CPR** + **First Aid** (`/`).
- Carer character traits list: capable, resilient, motivated, determined, joyful, empathetic, enthusiastic, compassionate, open-minded, professional, experienced, contemporary, knowledgeable (`/`).
- **Insurances:** public liability, professional indemnity, work cover (`/`).
- **Personalised carer matching** — selection by "personality, required medical attention, and other specific preferences" (`/`).
- **Founder is an RN with 30 yrs experience + palliative care grad cert** (`/about-us/`).
- **Since 2022**, "happy clients" in East Gippsland.
- **3 client testimonials** (verbatim, unattributed) on home page — see §7.
- Brokerage: "brokered services in partnership with accredited home care providers in Bairnsdale"; self-management guidance (`/contact-us/`).

---

## 6. Service Area (crawl-verified)

Bairnsdale · Bruthen · East Gippsland · Lakes Entrance · Lindenow South · Paynesville · "Towns in between" (`/area-served/`). Each town has its own page (identical template, town name swapped, hero `image-09`).

---

## 7. Testimonials (verbatim, from home page — unattributed)

1. "Very happy with the service and the compassion shown to me. I enjoy the social support outings very much and the home care assistance is wonderful. Thank you"
2. "I don't usually leave feedback but in this case I feel compelled to do so and it's positive. I have been needing extra assistance to be able to stay living in my own home. 'Inner Peace' I know, definitely helped me achieve this goal. The in-home nursing/domestic assistance and social support outings that Inner Peace provide have really helped me escape bouts of depression and improved my physical and emotional well-being"
3. "Very happy with this service"

---

## 8. Recruitment / Careers (crawl-verified)

- Requirement: "Certificate III in Aged Care **or** registered nurse" (`/contact-us/`).
- Two-form application: **DISC Personal Profile System** (/disc-personal-profile-system/, 24-question MOST/LEAST behavioural assessment + linked DISC PDF) and **Interview Form** (/interview-form/, 20-question screening questionnaire — "In-Home & Community Support Services Sector").
- "If your application is successful, we will contact you within 5 business days."
- No dedicated /careers/ landing page exists — forms are orphaned (not in sitemap nav).

---

## 9. Full Page Inventory (25 URLs from sitemap + crawl)

**Public, in sitemap (18):** `/` · `/book-an-appointment/` · `/terms-conditions/` · `/area-served/` · `/about-us/` · `/in-home-nursing-care-benefits/` · `/in-home-nursing-care-services/foot-care/` · `/contact-us/` · `/dementia-care/` · `/in-home-nursing-care-services/` · `/in-home-nursing-care-services/nursing-care/` · `/in-home-nursing-care-services/personal-care/` · `/in-home-nursing-care-services/social-care/` · 6× `/area-served/inner-peace-in-home-nursing-care-in-{town}/` · `/privacy-policy/`.

**Crawled but NOT in sitemap (unlisted/utility):** `/disc-personal-profile-system/` · `/interview-form/` · `/login/` · `/password-reset/`.

**Broken / 404:** `/home-care-services/` → "This page could not be found!" — **yet home & about-us link "personalised care" to `/home-care-services/personal-care/`** (dead internal links). This is a live defect.

---

## 10. Defects & Gaps Found in Crawl (evidence-based)

1. **Broken links:** home + about-us → `/home-care-services/personal-care/` (404 parent). (`/`, `/about-us/`, `/home-care-services/`)
2. **URL inconsistency:** services live at `/in-home-nursing-care-services/…` but Dementia Care sits at `/dementia-care/` (off-pattern), and dead `/home-care-services/` pattern referenced. [FRAMEWORK flags "one consistent path to every service"]
3. **Naming inconsistency:** "Inner Peace In-Home Nursing & Care" vs "Inner Peace Vision" vs "Inner Peace Services" (`/dementia-care/`). [FRAMEWORK flags this]
4. **Login in public surface:** `/login/` + `/password-reset/` are public utility pages; framework says separate staff portal from public nav.
5. **Locale mismatch:** `language=en-AU` but `og:locale=en_US` everywhere.
6. **Services hub says "Explore our three services below" but shows four cards** (`/in-home-nursing-care-services/`).
7. **Thin content:** `/in-home-nursing-care-services/foot-care/` = "Coming Soon!" only — indexable thin page.
8. **Testimonials unattributed and bottom-buried** on home; no testimonials page. [FRAMEWORK: give reviews "room to breathe"]
9. **Missing alt text:** `social-care-1.webp`, `Inner-Peace-1024x577.webp` (home Contact image), `Dementia_Nurse_Consulting-819x1024.png`, `Screenshot.png` have empty alts.
10. **No consolidated "Why choose us" trust band** with visual badges (trust copy is buried in long paragraphs on home).
11. **No careers/join-the-team landing page**; recruitment forms orphaned.
12. **Area pages are duplicate/near-identical** (thin, templated, only town name changes) — duplicate-content risk; same hero image (`image-09`) on all six.
13. **Booking "by appointment only"** with a multi-step widget but no fallback/clarity; weak conversion affordance.
14. **No structured data** (no JSON-LD LocalBusiness / MedicalBusiness / Review schema present in crawl metadata).
15. **No blog/resources/insights hub** for SEO topic authority.

---

## 11. Complete Image Inventory (21 content images in crawl)

| File | Used on | Category | Alt present? |
|---|---|---|---|
| Personal-Care.webp | home, services, service pages, area pages | Service card | ✅ "Personal Care" |
| Social-Care.webp | home, services, etc. | Service card | ✅ "Social Care" |
| Nursing-Care.webp | home, services, etc. | Service card | ✅ "Nursing Care" |
| Dementia_Nurse_Consulting…png (elementor thumb) | home, services, etc. | Service card | ✅ "Dementia_Nurse_Consulting" (poor alt) |
| team-members.jpg | home ("Selecting your carers") | Team/trust | ✅ "Inner Peace Vision Team Members" |
| Inner-Peace-1024x577.webp | home (Contact section) | Brand/lifestyle | ❌ empty |
| Personal-Care-1.webp | personal-care | Service hero | ✅ |
| Nursing-Care-1-1024x683.webp | nursing-care, benefits | Service hero | ✅ |
| social-care-1.webp | social-care | Service hero | ❌ empty |
| social-care-2-1024x683.webp | benefits | Lifestyle | ✅ "social care" |
| image-07.webp / image-08… / image-09… / image-10… | benefits, area pages | Lifestyle/care | partial ("In-Home Nursing & Care(Benefits)") |
| annette…webp (elementor thumb) | about-us | Team/founder | ✅ "annette" (weak) |
| Dementia_Nurse_Consulting-819x1024.png | dementia-care hero | Service hero | ❌ empty |
| Personal/Social/Nursing-Care.png (2023/11) | foot-care | Service card (old PNG) | ✅ |
| Screenshot.png | disc page | UI example | ❌ empty |
| cropped-Logo-270x270.png / -32x32 | global | Logo/favicon | n/a |

Image themes observed: real care scenarios, candid; webp adopted 2023/12 onward; older PNGs (2023/11) still referenced on foot-care (inconsistent format). No East-Gippsland location/landscape photography in evidence. No carer-with-client emotional hero on home page (home hero is text-only).

---

## 12. Strategic Website Framework — governing standard (summary)

**Philosophy:** Build on existing strengths; close the gap between service quality and online presentation. "Choosing in-home care is an emotional, high-trust decision — often made by an adult child researching on a phone, late at night." Modern, mobile-first, accessibility-conscious.

**Prescribed sitemap:**
```
Home
├── About Us
├── Services ── Personal · Nursing · Social · Dementia
├── Testimonials
├── Resources (consolidates area-served + helpful content + careers entry)
└── Contact
Staff Portal (separate, login-protected: Dashboard, Policies & Procedures,
  Training Materials, Employee Documents, Forms & Templates,
  Staff Announcements, Useful Links)
```

**Homepage six-section model:** (A) Hero — confident headline + single primary button "Book a free care consultation" + quiet trust cue "Caring for East Gippsland since 2022"; (B) Services overview — 4 cards; (C) Why Choose Us / Trust — 4 pillars (Cert III/CPR/First Aid, fully insured, personalised matching, locally owned); (D) Testimonials given room to breathe; (E) Service Area — map + town list; (F) Closing CTA band — book / call 0419 853 811 / Join our team. Rule: "A visitor understands what you do and how to act within five seconds"; "Every homepage scroll ends with a clear, friendly invitation to act."

**Design system:**
- Colours: White (bg), Sage Green (secondary accent), Soft Blue (supporting accent), **Teal (primary/CTA)**, **Deep Teal (headings/emphasis)**. "Light and airy by default… deeper teal reserved for headings and CTAs — confident, never clinical-cold."
- Type: **Fraunces** (serif headings, warm/editorial); **Hanken Grotesk** (sans body/UI, humanist). Generous, readable-at-any-age scale.
- Imagery: "Authentic, natural photography of carers, clients and East Gippsland… real warmth, never generic stock."
- Visual tone: soft, spacious, professional; generous whitespace; "gentle & human."

**Conversion:** primary CTA "Book a free care consultation"; click-to-call 0419 853 811 always reachable on mobile; service Learn-More links; "Join our team" recruitment path. Surface insurance, qualifications, reviews "where they build trust fastest." Targets (illustrative): +40% enquiries, 2× mobile engagement.

**UX:** mobile-first; single primary action per section; tap targets ≥44px; predictable URLs; separate internal/external nav.

**Trust badges:** "Fully insured", "Cert III qualified", "Client-reviewed".

**Tech (framework's own):** WordPress + ACF PRO. **OUR build target overrides this:** static **HTML5 + CSS3 + vanilla JS**, semantic, accessible (WCAG), mobile-first, performance- & SEO-optimised, progressive enhancement, modular CSS, reusable JS modules, no frameworks/libraries.

---

## 13. Brand Design Tokens (derived for build — framework-aligned)

```
--white:       #FFFFFF
--sage:        #A7C4A0   (sage green, secondary accent)
--soft-blue:   #BcD8E6   (supporting accent — soft, airy)
--teal:        #2E8B8B   (primary accent / CTAs)
--teal-600:    #246F6F   (CTA hover)
--deep-teal:   #14454A   (headings, strong emphasis)
--ink:         #243133   (body text)
--muted:       #5C6B6D   (secondary text)
--cream:       #F4F8F6   (light section bg)
--sand:        #EAF1ED   (alt section bg)
font headings: 'Fraunces', Georgia, serif
font body:     'Hanken Grotesk', system-ui, sans-serif
```
(Hex values are reasonable interpretations of the framework's named palette — confirm against any brand kit before launch.)
