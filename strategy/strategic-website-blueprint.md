# Inner Peace In-Home Nursing & Care — Strategic Website Blueprint

> **Status:** Governing specification for the static **HTML5 / CSS3 / vanilla-JS** rebuild.
> **Authority:** This blueprint is the build spec. It implements the **Strategic Website framework** (https://innerpeace-web.github.io/Strategic-Website/) while preserving the Inner Peace brand.
> **Source of truth:** `strategy/_facts.md` (crawl-derived). Every recommendation below cites **crawl evidence** AND the **framework principle** it implements. Nothing is invented; framework-prescribed additions not yet on the live site are marked **[FRAMEWORK]**.

## How to read this document
- **PURPOSE** = why the page exists in conversion/trust terms.
- **FRAMEWORK PRINCIPLE** = the governing rule from §12 of `_facts.md`.
- **SECTION-BY-SECTION LAYOUT** = exact render order (top → bottom). Build in this order.
- **COPY** = verbatim from the crawl (cited) or *derived* (rewritten to fix a defect; flagged).
- All CTAs, images, trust signals, internal links, and SEO/schema notes are page-specific to Inner Peace, never generic.

### Global build constraints (apply to every template)
- **Tech:** static HTML5 + CSS3 + vanilla JS only; no frameworks/libraries; semantic, WCAG-conscious, mobile-first, progressive enhancement, modular CSS, reusable JS modules (`_facts.md` §12 build-target override).
- **Design tokens:** `--teal #2E8B8B` (primary/CTA), `--teal-600 #246F6F` (hover), `--deep-teal #14454A` (headings), `--sage #A7C4A0`, `--soft-blue #BCD8E6`, `--cream #F4F8F6`, `--sand #EAF1ED`, `--ink #243133`, `--muted #5C6B6D` (`_facts.md` §13). Fonts: **Fraunces** headings, **Hanken Grotesk** body.
- **Persistent header:** logo (`cropped-Logo-270x270.png`), nav (Home · About · Services · Testimonials · Resources · Contact), and a **always-visible click-to-call `tel:+61419853811`** button on mobile (framework: "click-to-call always reachable on mobile"; tap targets ≥44px).
- **Fix locale defect site-wide:** set `<html lang="en-AU">` AND `og:locale=en_AU` (resolves `_facts.md` §10.5 mismatch).
- **Fix naming defect site-wide:** use **"Inner Peace In-Home Nursing & Care"** consistently; eliminate "Inner Peace Vision" / "Inner Peace Services" (`_facts.md` §10.3; dementia page is the offender).
- **Fix URL defect site-wide:** one consistent service path `/services/{slug}/`; never link to dead `/home-care-services/personal-care/` (`_facts.md` §10.1–10.2). Dementia Care moves under `/services/dementia-care/`.

---

# 1. Homepage Strategy

**PURPOSE:** Convert the high-anxiety researcher (framework persona: "an adult child researching on a phone, late at night") into a free consultation booking or a phone call within one scroll. The current home page buries trust copy in long paragraphs and hides testimonials at the bottom (`_facts.md` §10.8, §10.10).

**FRAMEWORK PRINCIPLE:** The **six-section homepage model** + the **5-second clarity rule** ("A visitor understands what you do and how to act within five seconds") + "Every homepage scroll ends with a clear, friendly invitation to act" (`_facts.md` §12).

### Section-by-section layout (exact order)

| # | Section | Render content |
|---|---|---|
| A | **Hero** | Headline + tagline + single primary CTA + quiet trust cue |
| B | **Services overview** | 4 service cards |
| C | **Why Choose Us / Trust** | 4 trust pillars as visual badges |
| D | **Testimonials** | 3 real quotes, given room to breathe |
| E | **Service Area** | Map + town list |
| F | **Closing CTA band** | Book / Call / Join our team |

#### A — Hero
- **H1 (verbatim, home):** "Inner Peace In-Home Nursing & Care"
- **Tagline (verbatim italic, home hero):** *"Personalised Care, in the Comfort of Your Own Home"*
- **Sub-line (verbatim, home):** "we are committed to providing high-quality, personalised care that promotes well-being and health"
- **Primary CTA (single, framework-mandated):** **"Book a free care consultation"** → `/contact/#book` (framework rewrites the existing weak "Book Now"; free-consultation framing per §12 conversion).
- **Quiet trust cue (framework-mandated micro-copy):** **"Caring for East Gippsland since 2022"** (derived from verbatim "Ever since 2022… East Gippsland", home).
- **Image:** **[FRAMEWORK]** Replace the current text-only hero (defect: no emotional hero, `_facts.md` §11) with an authentic carer-with-client East Gippsland photograph; descriptive alt e.g. "Inner Peace carer supporting a client at home in East Gippsland."
- **5-second test:** logo + "In-Home Nursing & Care" + "Book a free care consultation" + "since 2022" all above the fold.

#### B — Services overview (4 cards)
Verbatim card copy and links (home crawl). Single "Learn More" CTA per card.

| Card | Image | Verbatim blurb | Link |
|---|---|---|---|
| Personal Care | `Personal-Care.webp` (alt "Personal Care") | "Providing exceptional support in your daily life, ensuring that you can live independently and comfortably in your own home." | `/services/personal-care/` |
| Social Care | `Social-Care.webp` (alt "Social Care") | "Offering personalized in-home support and social activities tailored to bring joy and excitement into your life." | `/services/social-care/` |
| Nursing Care | `Nursing-Care.webp` (alt "Nursing Care") | "Encompasses a wide range of specialized and personalized support to ensure your holistic well-being." | `/services/nursing-care/` |
| Dementia Care | `Dementia_Nurse_Consulting…png` — **fix alt to** "Dementia Care nurse consulting with a client" (`_facts.md` §10.9, §11) | "Compassionate, personalised support for people living with dementia, their families, carers, and care providers across East Gippsland." | `/services/dementia-care/` |

#### C — Why Choose Us / Trust (4 pillars as badges)
**[FRAMEWORK]** New consolidated band — fixes "no consolidated Why-choose-us trust band" (`_facts.md` §10.10). Surface as 4 icon badges, not paragraphs.

| Pillar | Source copy (verbatim/derived) | Crawl source |
|---|---|---|
| **Cert III qualified** | "All our carers hold a minimum Certificate III in Aged/Community Care qualification, as well as essential certifications in CPR and First Aid." | home |
| **Fully insured** | "comprehensive carer insurances, including public liability, professional indemnity, and work cover" | home |
| **Personalised carer matching** | "we meticulously select each carer… a personalized match… personality, required medical attention, and other specific preferences" | home |
| **Locally owned, RN-led since 2022** | Founder is an RN with 30 yrs experience + palliative care grad cert; "Ever since 2022… East Gippsland" | about-us, home |

Use the framework badge labels verbatim where applicable: **"Fully insured" · "Cert III qualified" · "Client-reviewed"** (`_facts.md` §12 trust badges). Team image `team-members.jpg` (alt "Inner Peace Vision Team Members" — **fix alt** to "Inner Peace In-Home Nursing & Care team members") supports this band.

#### D — Testimonials (room to breathe)
Framework: give reviews "room to breathe" (`_facts.md` §10.8). Render as 3 spacious cards, one per viewport on mobile. **Verbatim, from home (§7):**
1. "Very happy with the service and the compassion shown to me. I enjoy the social support outings very much and the home care assistance is wonderful. Thank you"
2. "I don't usually leave feedback but in this case I feel compelled to do so and it's positive. I have been needing extra assistance to be able to stay living in my own home. 'Inner Peace' I know, definitely helped me achieve this goal. The in-home nursing/domestic assistance and social support outings that Inner Peace provide have really helped me escape bouts of depression and improved my physical and emotional well-being"
3. "Very happy with this service"
- Quotes are unattributed in the crawl — keep unattributed; do not invent names. Add a "Read more reviews" link → `/testimonials/`.

#### E — Service Area (map + towns)
- Intro (verbatim, area-served): "Delivering exceptional services to diverse locations, our extensive service network ensures support in every area served, ensuring assistance wherever you are."
- **Towns (verbatim, area-served §6):** Bairnsdale · Bruthen · East Gippsland · Lakes Entrance · Lindenow South · Paynesville · "Towns in between".
- Each town links to its consolidated Resources location page (see §4).
- **[FRAMEWORK]** Embed a static map of East Gippsland (lazy-loaded, accessible static image fallback — no third-party JS blocking render).

#### F — Closing CTA band (3 actions)
Framework closing band (`_facts.md` §12):
1. **"Book a free care consultation"** → `/contact/#book`
2. **"Call 0419 853 811"** → `tel:+61419853811`
3. **"Join our team"** → `/resources/careers/`
- Background `--cream`/`--sand`; deep-teal heading e.g. "Talk to a real local nurse today."

### SEO / Schema notes
- `<title>` "In-Home Nursing & Care in East Gippsland | Inner Peace" (improves the bare "Home -" title).
- **JSON-LD `MedicalBusiness`/`HomeAndConstructionBusiness`→ prefer `MedicalBusiness`** (fixes "no structured data", `_facts.md` §10.14): name, founder (Annette Keat), telephone `+61419853811`, `areaServed` (the 7 towns), `sameAs` (FB/YT/IG), `foundingDate` 2022.
- Embed `Review`/`AggregateRating` schema from the 3 testimonials.

---

# 2. Service Page Strategy (reusable template)

**PURPOSE:** Deep-explain one service, prove competence, and convert to booking. Covers **Personal · Nursing · Social · Dementia** (Dementia uses an extended variant — see §8). Foot Care handled as coming-soon/noindex.

**FRAMEWORK PRINCIPLE:** "one consistent path to every service" (fixes `_facts.md` §10.2); service Learn-More → detail → single primary action; surface qualifications/insurance "where they build trust fastest."

### Reusable section order

| # | Section | Content |
|---|---|---|
| 1 | Service hero | H1 = service name; verbatim one-liner; service hero image |
| 2 | Intro paragraph(s) | Verbatim service intro |
| 3 | "What we offer" list | Verbatim task/clinical/activity list (below) |
| 4 | Per-service CTA | "Book a free care consultation" + click-to-call |
| 5 | Trust strip | Cert III / Fully insured / Client-reviewed badges (shared partial) |
| 6 | "Other services" cross-links | 3 sibling cards (verbatim) |

### Per-service content

**Personal Care** (`/services/personal-care/`) — hero `Personal-Care-1.webp`
- Intro (verbatim): "With personal care, our dedicated team of carers is here to provide you with exceptional support in your daily life, ensuring that you can live independently and comfortably in your own home. From hygiene assistance to food preparation, our caregivers are trained to offer compassionate and respectful support with your activities of daily living."
- **Task list (verbatim, `_facts.md` §4):** Preparation of Simple Meals · Ironing · Grocery Shopping · Laundry Assistance · Floor Sweeping · General Cleaning Tasks · Dusting and Polishing · Vacuuming · Dog Walking Support.

**Nursing Care** (`/services/nursing-care/`) — hero `Nursing-Care-1-1024x683.webp`
- Intro (verbatim): "Our nursing care services encompass a wide range of specialized and personalized support to ensure your holistic well-being. At Inner Peace In-Home Nursing & Care, we believe in providing not only expert medical care but also compassionate and personalised attention to address your unique needs."
- **Clinical services (verbatim):** Wound Management · Palliative Care · Health Monitoring/Medication Management · Pain Management. **Plus health-management activities (verbatim):** Guided Outdoor Activities · Nutritional Support · Assistance with Activities · Coordination of Allied Health Services · Physical Activities · Transportation and Support · Individualized Pain Management Plans.

**Social Care** (`/services/social-care/`) — hero `social-care-1.webp` (**fix empty alt** → "Inner Peace carer enjoying a social outing with a client", `_facts.md` §10.9)
- Intro (verbatim): "Social Care offers personalized in-home support and social activities tailored to bring joy and excitement into your life. From engaging in recreational activities and dining out at local cafes to shopping trips and running errands, the options are limitless and are only driven by your interests and imagination."
- **Activities (verbatim):** Leisurely Walks · Cinema · Events & Gatherings · Creative Poetry Sessions · Explore the Internet Together · Tourist Attractions · Meaningful Conversations · Plan & Go On Holidays · Share Life Stories & Memoirs · Shopping for Essentials · Gardening Together.

**Dementia Care** — extended variant, see **§8**.

### "Other services" cross-links (verbatim sibling cards)
Each service page shows the **other three** as cards with verbatim blurbs (per crawl: personal-care shows Nursing/Social/Dementia; nursing-care shows Personal/Social/Dementia; social-care shows Personal/Nursing/Dementia). Reuse the §1-B card partial.

### Per-service CTA
Single primary: **"Book a free care consultation"** → `/contact/#book` (replaces verbatim "Book an Appointment" button, upgraded to free-consultation framing). Persistent click-to-call available.

### Services hub (`/services/`)
- Intro (verbatim): "Welcome to our In-Home Nursing & Care Services… we are dedicated to enhancing your quality of life through a range of specialized services designed to meet your unique needs."
- **Fix copy defect (`_facts.md` §10.6):** current text says "Explore our three services below" but shows four cards. Change to **"Explore our four services below"** (derived correction).
- Cards: Personal, Social, Nursing, Dementia (4 cards, verbatim blurbs).

### Foot Care — coming-soon / noindex handling
- Current state: thin "Coming Soon!" page, **indexable** (defect `_facts.md` §10.7); uses stale 2023/11 PNG cards.
- **Spec:** Keep `/services/foot-care/` but render a proper "coming soon" panel; set **`<meta name="robots" content="noindex, follow">`** so it is not an indexable thin page; **exclude from sitemap and from the main Services nav/grid** until launched. Replace stale PNG cards with current `.webp` siblings. CTA: "Register your interest" → `/contact/`.

### SEO / Schema (service pages)
- `<title>` pattern: "{Service} in East Gippsland | Inner Peace In-Home Nursing & Care".
- JSON-LD `Service` with `provider` = the `MedicalBusiness`, `areaServed` = East Gippsland; `MedicalProcedure`/itemList for nursing-care clinical items.
- Image `alt` fixed on `social-care-1.webp` (and dementia hero — §8).

---

# 3. About Page Strategy (`/about/`)

**PURPOSE:** Win trust through the founder's authority and the anti-institutional brand story. This is the emotional credibility anchor for the late-night researcher.

**FRAMEWORK PRINCIPLE:** Surface founder credentials and brand story "where they build trust fastest"; warm, "gentle & human," anti-clinical tone (`_facts.md` §12).

### Section order

| # | Section | Copy (verbatim, about-us / home) |
|---|---|---|
| 1 | Brand story | "Ever since 2022, Inner Peace In-Home Nursing & Care has been dedicated to enhancing the lives of our happy clients in the tranquil East Gippsland area." + "Our approach goes beyond the confines of traditional residential care, empowering individuals and their families to embrace a fulfilling life within the comfort of their home." + "We believe in the significance of cherishing life's simple pleasures, whether it's a refreshing day at the local pool, hosting a social gathering, or exploring hidden treasures at the op shop." |
| 2 | Annette's story | Photo `annette…webp` (**fix weak alt "annette"** → "Annette Keat, Founder, Director and Registered Nurse"). Verbatim: "Hi! I'm **Annette Keat**, Founder and Director of Inner Peace In-Home Nursing & Care. I am dedicated registered nurse with three decades of experience, the last 12 years of which have been devoted to home-based nursing within my community… In 2020, I achieved a graduate certificate in palliative care from the Australian College of Nursing…" |
| 3 | Mission / promise | Verbatim: "My mission is simple: I want to ensure that people always remain at the heart of care." + "the promise of more care, more respect, more options, and the opportunity to live life to the fullest." |
| 4 | Team & qualifications | Reuse §1-C trust pillars: Cert III + CPR + First Aid; carer matching; insurances. |
| 5 | CTA | "Book a free care consultation" + click-to-call. |

- **Fix broken link (`_facts.md` §10.1):** the verbatim "personalised care" link points to dead `/home-care-services/personal-care/`. Repoint to `/services/personal-care/`.
- Internal links: → Services, → Dementia Care, → Contact, → Testimonials.

### SEO / Schema
- `<title>` "About Annette Keat & Inner Peace | In-Home Nursing East Gippsland".
- JSON-LD `Person` (Annette Keat: jobTitle "Founder & Director / Registered Nurse", `alumniOf` Australian College of Nursing, credential "Graduate Certificate in Palliative Care, 2020") linked as `founder` of the business.

---

# 4. Location / Area Page Strategy (consolidate under Resources)

**PURPOSE:** Capture local SEO ("in-home care in Bairnsdale" etc.) without duplicate-content penalties. The six town pages are currently near-identical templates with the town name swapped and the **same hero `image-09`** on all six (defect `_facts.md` §10.12).

**FRAMEWORK PRINCIPLE:** Predictable URLs; "Resources (consolidates area-served + helpful content + careers entry)" (`_facts.md` §12 sitemap). De-duplicate to protect indexability.

### Fix plan
- **Move** all location pages under **`/resources/areas/{town}/`** (consolidated). Keep `/resources/areas/` as the hub (replaces `/area-served/`).
- **6 towns:** Bairnsdale, Bruthen, East Gippsland, Lakes Entrance, Lindenow South, Paynesville (+ "towns in between" mentioned, not its own page).

### Per-town section order (de-duplicated template)

| # | Section | Requirement |
|---|---|---|
| 1 | Local hero | **Unique** local intro per town (rewrite the boilerplate); **distinct image per town** — not the shared `image-09` (fixes §10.12). |
| 2 | Local context | Local landmarks / nearby towns / travel note specific to that town (derived, factual, town-specific). |
| 3 | Services available locally | Link to the 4 service pages (verbatim sibling cards). |
| 4 | Local trust line | "Caring for {town} and East Gippsland since 2022" (derived). |
| 5 | CTA | "Book a free care consultation" + click-to-call. |

- **Base verbatim retained for Bairnsdale** (rewrite others to be unique): "Inner Peace is your foremost choice for unparalleled and compassionate In-Home Nursing & Care in Bairnsdale… safeguarding your well-being and preserving independence within the secure confines of your home environment." Each town page must have ≥150 unique words to avoid the duplicate-content risk.
- Internal links: → each service, → Contact, → home Service-Area section.

### SEO / Schema
- `<title>` "In-Home Nursing & Care in {Town}, East Gippsland | Inner Peace".
- **Per-page local schema:** JSON-LD `MedicalBusiness` with `areaServed` = the specific town + `geo` coordinates per town (fixes §10.14 and gives each page a unique structured signal).
- Unique meta description per town. Canonical self-referencing per town.

---

# 5. Trust Page Strategy (`/about/trust/` or section within About + standalone)

**PURPOSE:** One destination that consolidates every proof point so the researcher can verify legitimacy fast. Today trust copy is scattered in long home-page paragraphs (`_facts.md` §10.10).

**FRAMEWORK PRINCIPLE:** Surface insurance, qualifications, reviews "where they build trust fastest"; badge set "Fully insured / Cert III qualified / Client-reviewed."

### Section order

| # | Section | Verbatim / derived copy |
|---|---|---|
| 1 | Badge row | **"Fully insured" · "Cert III qualified" · "Client-reviewed"** (framework badges, `_facts.md` §12). |
| 2 | Qualifications | "All our carers hold a minimum Certificate III in Aged/Community Care qualification, as well as essential certifications in CPR and First Aid." (home) |
| 3 | Carer character | Verbatim traits list: "capable, resilient, motivated, determined, joyful, empathetic, enthusiastic, compassionate, open-minded, professional, experienced, contemporary, and knowledgeable." (home) |
| 4 | Insurances | "comprehensive carer insurances, including public liability, professional indemnity, and work cover." (home) |
| 5 | Carer matching | "we meticulously select each carer… personality, required medical attention, and other specific preferences." (home) — image `team-members.jpg`. |
| 6 | Founder credentials | RN, 30 yrs, 12 yrs home-based nursing, Graduate Certificate in Palliative Care (2020, Australian College of Nursing). Link → About. |
| 7 | Testimonials | The 3 verbatim quotes (§7); link → `/testimonials/`. |
| 8 | CTA | "Book a free care consultation" + click-to-call. |

### SEO / Schema
- JSON-LD `AggregateRating` + `Review`; reuse business `Person`/`MedicalBusiness` references. Title: "Qualified, Insured & Locally Trusted | Inner Peace".

---

# 6. Contact Page Strategy (`/contact/`)

**PURPOSE:** Route four distinct intents quickly; make the phone the hero on mobile; collect enquiries via form.

**FRAMEWORK PRINCIPLE:** "click-to-call 0419 853 811 always reachable"; single clear action per block; separate internal/external nav.

### Section order — the four intents (verbatim, contact-us)

| # | Block | Verbatim copy | Action |
|---|---|---|---|
| 0 | Intro | "Have questions, suggestions, or just want to say hello? We'd love to hear from you! Our team is here to assist you in any way we can." | — |
| 1 | **Urgent Assistance** | "When time is of the essence, we're here to lend a helping hand. Feel free to reach out to us anytime, even outside regular business hours, at 0419 853 811 for instant support." | `tel:+61419853811` |
| 2 | **Care Inquiry** | "Our friendly and qualified team members are available to discuss the ideal home care options for you. Call us at 0419 853 811 to explore the personalized care solutions we can offer." | `tel:+61419853811` + book |
| 3 | **Brokerage Services** | "We offer brokered services in partnership with accredited home care providers in Bairnsdale. Contact us at 0419 853 811… We also provide guidance on Self-Management options for care packages." | `tel:+61419853811` |
| 4 | **Employment Opportunities** | "If you hold a Certificate III in Aged Care or you're a registered nurse and have a passion for providing top-quality care in the community, we're interested in talking to you about joining our dedicated and innovative team. Reach out to us at 0419 853 811 to learn how." | → `/resources/careers/` |
| 5 | Contact form | Verbatim fields: First Name · Last Name · Phone Number · Email Address · Message · Submit. (Add honeypot/anti-spam; reCAPTCHA per existing.) | submit |
| 6 | Map | Static East Gippsland map (accessible). | — |
| 7 | Social | Facebook (facebook.com/innerpeace.vision) · YouTube (youtube.com/@innerpeace.vision7778) · Instagram (instagram.com/innerpeace.vision). | external `rel="noopener"` |

- Booking anchor `#book` lives here (see §7). Availability note (verbatim, book page): "By appointment only" + urgent help "even outside regular business hours."

### SEO / Schema
- JSON-LD `MedicalBusiness` with `contactPoint` (telephone, contactType "customer service"), `sameAs` socials. Title "Contact Inner Peace | In-Home Nursing & Care, East Gippsland".

---

# 7. Booking Flow Strategy (`/contact/#book`)

**PURPOSE:** Convert intent to a booked **free consultation** with minimum friction. Current booking is a multi-step Bookly-style widget ("Services → Date & Time → Your Information") with weak affordance and no fallback (`_facts.md` §10.13).

**FRAMEWORK PRINCIPLE:** Primary CTA "Book a free care consultation"; reduce friction; mobile-first; click-to-call fallback always present.

### Flow / section order

| # | Step | Spec |
|---|---|---|
| 1 | Framing | Headline "Book a free care consultation" + reassurance "No obligation — a friendly chat with a local nurse." (derived from §12 free-consultation framing). |
| 2 | **Click-to-call fallback (above the widget)** | "Prefer to talk now? Call 0419 853 811" → `tel:+61419853811`. Direct contact: `annette@innerpeace.vision` (verbatim, book page). |
| 3 | Minimal form | Service (Home Care Services / Phone Consultation — verbatim widget categories) → preferred Date & Time → Name, Phone, Email. Keep to one screen on mobile; ≥44px tap targets. |
| 4 | Confirmation / expectations | On submit: "Thank you — we'll be in touch to confirm your free consultation." Set expectation re "by appointment only" and out-of-hours urgent line. |

- **Friction reductions:** progressive enhancement — the form posts and works without JS; date picker is an enhancement only. No account/login required. Single primary button per step.
- **Mobile:** sticky click-to-call bar persists during the flow.

### SEO / Schema
- Booking page itself can be `noindex` (utility) but the `/contact/` parent is indexable. `ReserveAction`/`ContactPoint` schema on the booking CTA optional.

---

# 8. Dementia Care & Referral Page (`/services/dementia-care/`)

**PURPOSE:** The newest, most-evolved page (modified 2026-05-18). Preserve its modern structure, the **full online referral form**, and the **Lisa Tyter** contact. Serves families AND professional referrers (providers, GPs).

**FRAMEWORK PRINCIPLE:** Most modern build on the site — treat as the design reference; "one consistent path" (move under `/services/`); fix the "Inner Peace Vision/Services" naming defect in the privacy/consent copy.

### Section order (verbatim, dementia-care)

| # | Section | Copy |
|---|---|---|
| 1 | Hero | Eyebrow "DEMENTIA CARE"; H1 "Dementia Nurse Consulting"; sub "Specialist Support for Dementia Care"; lead "Compassionate, personalised support for people living with dementia, their families, carers, and care providers across East Gippsland." Image `Dementia_Nurse_Consulting-819x1024.png` (**fix empty alt** → "Dementia nurse consulting with a client", §10.9). CTAs: **"Complete Online Referral"** (`#online-referral`) + **"Contact Dementia Care"** (`#ips-contact`). |
| 2 | Overview | "Clear, practical dementia support with a human centre." + "Working alongside individuals, families, carers, and providers, we deliver person-centred dementia support that promotes dignity, safety, wellbeing, and meaningful connection to home and community." Value chips: **Person-centred · Compassionate · Practical · Aligned with aged care standards.** |
| 3 | Who We Support | People living with dementia at all stages · Support at Home (SaH) recipients · Families and carers · Home care recipients · Aged care and community providers. |
| 4 | How We Help | Personalised care planning · Family and carer guidance · Changed behaviour support and dementia strategies · Support for home care and aged care providers · Improving wellbeing, independence and quality of life. |
| 5 | Specialist Clinical Services | Behaviour Assessment & Support · Individualised Care Planning · Family & Carer Support · Provider & Workforce Consultation · Quality of Life Strategies · Assessment & Ongoing Support (initial cognitive assessment, geriatric assessment, diagnosis support, ongoing support). |
| 6 | **Online Referral Form** | Preserve all field groups (verbatim): **Referral Details** (Provider name, SAH level, Referrer name/phone/email) · **Client/Patient Details** (Title, Gender, DOB, Given names, Surname, Phone, Email, Address, ATSI background Yes/No/Prefer not to say, Medicare number/expiry, Pension/DVA) · **Reason for Referral** · **Contacts & Care Team** (NOK, emergency contact, decision maker, GP, other professionals) · **Home Visit Risk Assessment** (home visit agreeable, parking, pets, smoking, infectious diseases, firearms/weapons, notes) · **Privacy notice** · **3 consent checkboxes** (verbatim). Build as accessible static form, progressive enhancement, anti-spam. |
| 7 | Contact | **Annette Keat** 0419 853 811 (`tel:0419853811`) · **Lisa Tyter** 0477 051 130 (`tel:0477051130`) · `dementiacare@innerpeace.vision` · www.innerpeace.vision. |

- **Fix naming defect (`_facts.md` §10.3):** the privacy/consent copy says "designated Inner Peace Vision email addresses" and "Inner Peace Services contacting…". Rewrite to "Inner Peace In-Home Nursing & Care" for brand consistency (note this as a copy edit; keep legal intent intact).

### SEO / Schema
- `<title>` "Dementia Care & Nurse Consulting in East Gippsland | Inner Peace".
- JSON-LD `MedicalBusiness`/`Service` (Dementia Nurse Consulting), `areaServed` East Gippsland, secondary contact (Lisa Tyter). This is the strongest page for indexable depth — keep indexable.

---

# 9. Careers / Join-the-Team Page (`/resources/careers/`)

**PURPOSE:** Give recruitment a real landing page. Today there is **no /careers/ page** and the DISC + Interview forms are orphaned (not in nav/sitemap) (`_facts.md` §8, §10.11).

**FRAMEWORK PRINCIPLE:** "Join our team" recruitment path surfaced from the homepage closing band; Resources consolidates the careers entry.

### Section order

| # | Section | Copy (verbatim, contact-us / interview-form) |
|---|---|---|
| 1 | Hero | "Join our dedicated and innovative team." (derived from contact-us Employment block). CTA: "Start your application". |
| 2 | Who we're looking for | Verbatim requirement: "If you hold a Certificate III in Aged Care or you're a registered nurse and have a passion for providing top-quality care in the community, we're interested in talking to you about joining our dedicated and innovative team." |
| 3 | Why work here | Reuse brand/values (carer traits list from §5). |
| 4 | **Two-form application** | Surface both forms with explanation (verbatim contact-us): "You need to fill in the DISC Personal Profile System and Interview Form, which are required forms during our application process." Links: **DISC Personal Profile System** → `/resources/careers/disc/` (24-question MOST/LEAST behavioural assessment + DISC PDF), **Interview Form** → `/resources/careers/interview/` (20-question screening, "In-Home & Community Support Services Sector"). |
| 5 | **5-business-day promise** | Verbatim (interview-form): "If your application is successful, we will contact you within 5 business days to discuss the next steps." |
| 6 | CTA | Phone 0419 853 811 + "Start your application". |

- Interview Form is already `noindex, follow` in crawl — keep both forms `noindex, follow` (utility), but **link them from the careers page and add careers to nav/sitemap** (fixes orphaning).
- DISC page: fix empty alt on `Screenshot.png` (§10.9).

### SEO / Schema
- Careers landing indexable; JSON-LD `JobPosting` optional. Title "Careers — Join Our In-Home Care Team | Inner Peace, East Gippsland".

---

# 10. Staff Portal (separate, login-protected)

**PURPOSE:** Internal hub for staff; **must be separated from public nav** (current `/login/` + `/password-reset/` sit in the public surface — defect `_facts.md` §10.4).

**FRAMEWORK PRINCIPLE:** "Staff Portal (separate, login-protected)" with seven prescribed sections (`_facts.md` §12 sitemap). Separate internal/external nav.

### The 7 framework sections (build as portal nav)
1. **Dashboard**
2. **Policies & Procedures**
3. **Training Materials**
4. **Employee Documents**
5. **Forms & Templates**
6. **Staff Announcements**
7. **Useful Links**

- **Access:** login-protected; **not linked from public header/footer nav** (a discreet footer "Staff login" link only). Move `/login/` and `/password-reset/` behind `/portal/`.
- **SEO:** entire portal `noindex, nofollow`, excluded from sitemap.
- **Note:** as a static build, real auth requires a back-end or gated host; spec the portal shell and access pattern, flag auth as an integration dependency.

---

# 11. Implementation Priority Matrix (page → priority → effort)

| Page / Work item | Priority | Effort | Rationale (crawl + framework) |
|---|---|---|---|
| **Homepage (6-section model)** | P0 | High | Primary conversion surface; 5-sec rule; fixes §10.8/§10.10. |
| **Global fixes** (locale, naming, dead `/home-care-services/` links, header click-to-call) | P0 | Med | Live defects §10.1/§10.3/§10.5; quick credibility + SEO wins. |
| **Contact + Booking flow** | P0 | Med | Four intents + free-consult framing; fixes §10.13. |
| **Service pages ×3 (Personal/Nursing/Social)** | P0 | Med | Core demand pages; verbatim lists ready. |
| **Dementia Care page** | P1 | Med | Newest/most-evolved; preserve referral form + Lisa Tyter; move under /services/. |
| **About page** | P1 | Low | Founder authority; fix broken link + alt. |
| **Trust page + badges** | P1 | Low | Consolidates §10.10; high trust ROI, low effort. |
| **Testimonials page** | P1 | Low | "Room to breathe" §10.8; reuse 3 quotes. |
| **Location pages (de-dup, consolidate to Resources)** | P2 | High | Fixes §10.12 duplicate content; per-town rewrite + unique imagery/schema. |
| **Careers landing + surface DISC/Interview** | P2 | Med | Fixes §10.11 orphaning; 5-day promise. |
| **Services hub fix ("four", not "three")** | P2 | Low | Fixes §10.6 copy defect. |
| **Foot Care → noindex / out of nav** | P2 | Low | Fixes thin-content §10.7. |
| **Structured data (JSON-LD) site-wide** | P2 | Med | Fixes §10.14; local + medical + review schema. |
| **Staff Portal shell + auth separation** | P3 | High | Separates §10.4; needs back-end/host integration. |

---

# 12. Page → Template → Primary-CTA Matrix

| Page (new URL) | Template | Primary CTA | Secondary action |
|---|---|---|---|
| `/` Home | Homepage (6-section) | Book a free care consultation | Call 0419 853 811 / Join our team |
| `/about/` | About | Book a free care consultation | Explore services |
| `/services/` | Services hub | Book a free care consultation | Learn More (per card) |
| `/services/personal-care/` | Service | Book a free care consultation | Call / other services |
| `/services/nursing-care/` | Service | Book a free care consultation | Call / other services |
| `/services/social-care/` | Service | Book a free care consultation | Call / other services |
| `/services/dementia-care/` | Service (extended + referral) | Complete Online Referral | Contact Dementia Care (Annette / Lisa) |
| `/services/foot-care/` | Service (coming-soon, noindex) | Register your interest | — |
| `/testimonials/` | Trust/Reviews | Book a free care consultation | Call |
| `/about/trust/` | Trust | Book a free care consultation | Call |
| `/resources/` | Resources hub | Explore areas / careers | — |
| `/resources/areas/{town}/` ×6 | Location | Book a free care consultation | Call |
| `/resources/careers/` | Careers | Start your application | Call 0419 853 811 |
| `/resources/careers/disc/` | Form (noindex) | Submit DISC | — |
| `/resources/careers/interview/` | Form (noindex) | Send | — |
| `/contact/` | Contact | Call 0419 853 811 | Book / form / brokerage |
| `/contact/#book` | Booking flow | Book a free care consultation | Call fallback |
| `/portal/*` | Staff Portal (login, noindex) | Log in | — |

---

*End of blueprint. All copy is verbatim from `innerpeace-crawl/*.json` or explicitly marked derived/[FRAMEWORK]; all recommendations cite both crawl evidence and the Strategic Website framework per `strategy/_facts.md`.*
