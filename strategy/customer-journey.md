# Inner Peace — Customer Journey, Personas & Conversion Map

> Source of truth: `./strategy/_facts.md` + `./innerpeace-crawl/*.json`. Framework = Strategic Website (https://innerpeace-web.github.io/Strategic-Website/). Nothing invented; framework recommendations not yet on site are tagged **[FRAMEWORK]**. Pages are cited by live URL.

**Governing insight (framework):** *"Choosing in-home care is an emotional, high-trust decision — often made by an adult child researching on a phone, late at night."* Every recommendation below is filtered through: mobile-first, one primary action per section, surface trust where it converts fastest, and *"every section ends in an invitation to act."*

---

## 1. Personas (derived only from crawl evidence)

### Persona A — The Adult-Child Decision-Maker (primary buyer)
*Researching care for an ageing parent; often on a phone, late at night, under emotional load. The framework's named primary audience.*

| Dimension | Detail (crawl-grounded) |
|---|---|
| **Goals** | Find a trustworthy local provider so Mum/Dad can stay home; understand what's actually offered (personal, social, nursing, dementia); reach a real person fast; confirm they cover the parent's town. |
| **Anxieties** | "Is this provider real and safe? Are the carers qualified and insured? Will my parent be treated with dignity, not institutionalised? What will it cost? Can I trust a small 2022 startup?" |
| **Crawl pages that serve them** | `/` (mission, services, "Selecting your carers", reviews), `/about-us/` (Annette RN, 30 yrs, palliative cert), `/in-home-nursing-care-services/` (hub), the 3 service pages (`/personal-care/`, `/social-care/`, `/nursing-care/`), `/dementia-care/`, `/area-served/` + town pages, `/contact-us/`, `/book-an-appointment/`. |
| **Trust signals that matter** | Cert III + CPR + First Aid for all carers (`/`); public liability / professional indemnity / work cover insurance (`/`); personalised carer matching by personality + needs (`/`); founder is an RN with 30 yrs + palliative grad cert (`/about-us/`); since-2022 + 3 testimonials (`/`); "even outside regular business hours" reachability (`/contact-us/`). |

### Persona B — The Older Person Who Wants to Stay at Home (care recipient)
*May self-research or sit beside the adult child. The testimonials on `/` are written in this voice ("I have been needing extra assistance to be able to stay living in my own home").*

| Dimension | Detail (crawl-grounded) |
|---|---|
| **Goals** | Keep independence and routine at home; help with daily tasks (meals, laundry, cleaning, dog walking — `/personal-care/`); social connection and outings (`/social-care/`); clinical support without going into residential care (`/nursing-care/`). |
| **Anxieties** | "Will strangers in my home respect me? Will I lose control of my routine? Is this 'aged care' that takes my independence?" The brand voice directly answers this — anti-institutional, dignity-centred ("goes beyond the confines of traditional residential care", `/`). |
| **Crawl pages that serve them** | `/social-care/` (cinema, gardening, share life stories, leisurely walks), `/personal-care/` (everyday-living tasks), `/in-home-nursing-care-benefits/`, the testimonials block on `/` (written in their voice). |
| **Trust signals that matter** | Same-personality carer matching (`/`); warm, simple-pleasures brand voice (op shop, local pool — `/`); peer testimonials about escaping depression and staying home (`/`); local East Gippsland presence (`/area-served/`). |

### Persona C — The Dementia Referrer (GP / aged-care provider / SaH coordinator / family)
*Derived directly from the `/dementia-care/` online referral form fields — the form proves this persona exists and is professional/clinical.*

| Dimension | Detail (crawl-grounded) |
|---|---|
| **Goals** | Make a clean clinical referral without printing/scanning ("complete the referral without needing to download, print, or scan paperwork", `/dementia-care/`); get behaviour assessment, individualised care planning, cognitive/geriatric assessment, diagnosis support; arrange a safe home visit. |
| **Anxieties** | Privacy/consent of health information; whether the provider is clinically credible; whether the home visit is safe (the form asks about parking, pets, smoking, infectious disease, firearms). |
| **Crawl pages that serve them** | `/dementia-care/` — the only page; contains the full referral form (Referral Details + SaH level; Client/Patient Details incl. ATSI, Medicare/DVA; Reason for Referral; Contacts & Care Team incl. GP + decision-maker; Home Visit Risk Assessment; Privacy notice + 3 consent checkboxes). Linked from `/` and `/in-home-nursing-care-services/` service cards. |
| **Trust signals that matter** | "Aligned with aged care standards" values chip (`/dementia-care/`); Annette's palliative-care grad cert + RN status (`/about-us/`); named dementia contacts Annette **0419 853 811** and Lisa Tyter **0477 051 130**, dementiacare@innerpeace.vision (`/dementia-care/`); explicit privacy notice + consent (`/dementia-care/`). |

### Persona D — The Prospective Carer / RN Applicant (recruitment)
*Two real forms in the crawl confirm an active recruitment funnel.*

| Dimension | Detail (crawl-grounded) |
|---|---|
| **Goals** | Find values-aligned local care work; understand requirements; apply. Requirement: "Certificate III in Aged Care **or** registered nurse" (`/contact-us/`). |
| **Anxieties** | "Is this a real, stable employer? Is the process fair? Will I hear back?" (the Interview Form answers the last: *"If your application is successful, we will contact you within 5 business days"*). |
| **Crawl pages that serve them** | `/contact-us/` "Employment Opportunities" + "Join Our Team" (links to both forms); `/disc-personal-profile-system/` (24-item MOST/LEAST behavioural assessment + DISC PDF); `/interview-form/` (20-question screening for the "In-Home & Community Support Services Sector"). **No `/careers/` landing page exists — forms are orphaned, not in nav/sitemap.** |
| **Trust signals that matter** | Carer character traits + Cert III/CPR/First Aid standard (`/`); founder credibility (`/about-us/`); the structured DISC + interview process signals a professional employer; the "5 business days" promise sets expectations. |

---

## 2. Journey Map — 6 Stages

| Stage | Customer goal | Emotional state | Current Inner Peace touchpoints (actual pages) | Gaps / friction | Recommended improvement (framework-aligned) |
|---|---|---|---|---|---|
| **1. Awareness** | Discover a local in-home option for a parent | Worried, overwhelmed, time-poor (late-night phone) | Organic local search → `/area-served/` + 6 town pages; `/` hero ("Personalised Care, in the Comfort of Your Own Home"); FB/YouTube/IG linked from `/contact-us/` | Town pages are near-identical templated thin content (duplicate-content + same `image-09` hero); no JSON-LD LocalBusiness schema; no blog/resources for topic authority; home hero is text-only (no carer-with-client emotional image) | **[FRAMEWORK]** Add LocalBusiness/MedicalBusiness schema; give each town page genuinely local copy; add authentic carer+client hero photography ("real warmth, never generic stock"); 5-second clarity rule on `/` |
| **2. Consideration** | Understand what's offered + whether it fits | Comparing, cautious, seeking proof | `/in-home-nursing-care-services/` hub + `/personal-care/`, `/social-care/`, `/nursing-care/`, `/dementia-care/`; `/in-home-nursing-care-benefits/`; `/about-us/` (Annette's story) | **Broken links:** `/` + `/about-us/` link "personalised care" to dead `/home-care-services/personal-care/` (404); hub says "three services" but shows four cards; `/foot-care/` is "Coming Soon!" thin page; trust copy buried in long paragraphs; testimonials unattributed + bottom-buried | Fix the 404 to `/in-home-nursing-care-services/personal-care/`; correct "three"→"four"; hide or finish `/foot-care/`; **[FRAMEWORK]** add a 4-pillar "Why Choose Us" trust band (Cert III/CPR/First Aid · fully insured · personalised matching · locally owned) and a dedicated Testimonials page "given room to breathe" |
| **3. Decision** | Decide to make contact | Hopeful but hesitant, needs reassurance + funding clarity | `/contact-us/` (Urgent / Care Inquiry / Brokerage / Self-Management); phone **0419 853 811** repeated; `/book-an-appointment/` | **No pricing or funding/SaH/HCP guidance** anywhere except a one-line brokerage mention; no FAQ; "By appointment only" with no clear next-step affordance | **[FRAMEWORK]** Add a funding/"How to pay" + FAQ section (SaH, Home Care Packages, self-management, brokerage in Bairnsdale already referenced on `/contact-us/`); make the single primary CTA "Book a free care consultation" |
| **4. Conversion** | Book the consult / call / refer | Relief, or frustration if blocked | `/book-an-appointment/` multi-step widget (Services → Date & Time → Your Information); click-to-call `tel:+61419853811`; `/contact-us/` form; `/dementia-care/` referral form | Booking widget crawl shows only "Home Care Services(3)" + "Phone Consultation(1)" then **"No matching data"** — likely no bookable slots, a dead end; "by appointment only" with no fallback; primary CTA on `/` is "Book Now" not the framework's "Book a free care consultation" | Guarantee live slots or replace with a simple request-a-callback fallback; rename CTA to **"Book a free care consultation"**; keep click-to-call persistent + ≥44px on mobile; every section ends in an invitation to act |
| **5. Retention** | Feel cared-for; continue service | Reassured, loyal | Care relationship offline; testimonials suggest satisfaction; "even outside regular business hours" support (`/contact-us/`) | No client-facing portal, resources, or post-onboarding content; `/login/` + `/password-reset/` are public utility pages but staff-only | **[FRAMEWORK]** Move staff/client login behind a separate Staff Portal (off public nav); add a Resources hub (consolidating area-served + helpful content + careers entry) for ongoing value |
| **6. Referral / Advocacy** | Recommend to peers / refer professionally | Grateful, willing to advocate | 3 testimonials on `/`; dementia referral pathway on `/dementia-care/`; brokerage partnerships in Bairnsdale (`/contact-us/`) | Testimonials unattributed + buried; no easy "share / leave a review" path; no Google/"Client-reviewed" badge; referral form is the only structured advocacy loop | **[FRAMEWORK]** Add a "Client-reviewed" trust badge + review-collection CTA; surface the dementia referral path prominently for professional referrers; attribute testimonials (first name + town, with consent) |

---

## 3. Entry Points & Exit / Drop-off Points

### Entry points (how people arrive)
| Entry | Evidence | Lands on |
|---|---|---|
| Organic local search ("home care Bairnsdale/Lakes Entrance/Paynesville…") | 6 town pages + `/area-served/` exist for this intent | Town page → ideally service/contact |
| Organic service search ("dementia care East Gippsland", "in-home nursing") | `/dementia-care/`, `/in-home-nursing-care-services/` + service pages | Service hub / dementia page |
| Dementia professional referral | `/dementia-care/` online referral form ("doctors, referrers, families, and providers") | Referral form |
| Social | Facebook, YouTube `@innerpeace.vision7778`, Instagram — all linked from `/contact-us/` | Home / contact |
| Direct / word-of-mouth | Brand name, brokerage partners in Bairnsdale (`/contact-us/`) | Home |
| Recruitment search | `/contact-us/` "Join Our Team" → DISC + Interview forms | Orphaned forms |

### Exit points / drop-off risks
| Risk | Evidence | Why it loses the visitor |
|---|---|---|
| **Broken "personalised care" link → 404** | `/` + `/about-us/` link to `/home-care-services/personal-care/`; parent `/home-care-services/` returns "This page could not be found!" | Dead end at the consideration stage; erodes trust in a small unknown provider |
| **Booking widget dead end** | `/book-an-appointment/` shows "No matching data" under the service/consultation options | Visitor ready to convert hits an apparent no-availability wall |
| **"By appointment only"** with no fallback | `/book-an-appointment/`, `/contact-us/` | No clear single next step; high-anxiety buyer bounces |
| **Thin / "Coming Soon!" foot-care page** | `/in-home-nursing-care-services/foot-care/` | Indexable empty page; looks unfinished |
| **No pricing / funding info** | Absent across crawl (only brokerage line on `/contact-us/`) | A top decision-stage question is unanswered → off-site comparison |
| **Orphaned careers forms** | `/disc-…/` + `/interview-form/` not in sitemap/nav | Candidates can't find the path without the `/contact-us/` text link |
| **Duplicate town pages** | 6 near-identical templated pages, same hero image | Possible SEO suppression → lost awareness entries |
| **Naming inconsistency** | "Inner Peace In-Home Nursing & Care" vs "Inner Peace Vision" vs "Inner Peace Services" (`/dementia-care/`) | Subtle trust friction for an already-anxious buyer |

---

## 4. Conversion Opportunities & Friction Points — Prioritised (Impact × Effort)

| # | Item | Type | Impact | Effort | Priority | Framework tie |
|---|---|---|---|---|---|---|
| 1 | Fix `/home-care-services/personal-care/` 404 → `/in-home-nursing-care-services/personal-care/` | Friction | High | Low | **DO FIRST** | "One consistent path to every service" |
| 2 | Fix booking widget "No matching data" / add request-a-callback fallback | Friction | High | Low–Med | **DO FIRST** | Primary CTA must succeed |
| 3 | Rename primary CTA to "Book a free care consultation" sitewide | Opportunity | High | Low | **DO FIRST** | Named primary conversion |
| 4 | Persistent click-to-call 0419 853 811 (≥44px) on mobile | Opportunity | High | Low | **DO FIRST** | Mobile-first; late-night phone buyer |
| 5 | Add 4-pillar "Why Choose Us" trust band (Cert III/CPR/First Aid · insured · matching · local) | Opportunity | High | Med | **HIGH** | Surface trust where it converts fastest |
| 6 | Add funding / "How to pay" + FAQ (SaH, HCP, self-management, brokerage) | Opportunity | High | Med | **HIGH** | Answers decision-stage blocker |
| 7 | Dedicated Testimonials page, attributed, "room to breathe" | Opportunity | Med–High | Med | **HIGH** | Reviews where they build trust |
| 8 | Create a `/careers/` (Join our team) landing page; link DISC + Interview | Opportunity | Med | Low–Med | **HIGH** | Recruitment path in nav |
| 9 | Finish or unpublish `/foot-care/` "Coming Soon!" page | Friction | Med | Low | **MED** | No thin indexable pages |
| 10 | Add LocalBusiness/MedicalBusiness + Review JSON-LD schema | Opportunity | Med–High | Med | **MED** | SEO awareness entries |
| 11 | Rewrite 6 town pages with genuinely local copy + distinct imagery | Friction | Med | Med–High | **MED** | Predictable URLs + local SEO |
| 12 | Move `/login/` + `/password-reset/` behind separate Staff Portal | Friction | Low–Med | Med | **MED** | Separate internal/external nav |
| 13 | Unify brand name; fix `og:locale` en_US→en_AU | Friction | Low | Low | **MED** | Consistency = trust |
| 14 | Authentic carer+client hero photography on `/` | Opportunity | Med | Med–High | **LATER** | "Real warmth, never generic stock" |

---

## 5. Conversion Funnel (entry → consultation booked)

```
                        ENTRY POINTS
  Local search        Service/dementia       Social (FB/YT/IG)      Referral
  (town pages)         search                 from /contact-us/      (GP/provider)
      |                    |                       |                     |
      v                    v                       v                     v
 /area-served/   /in-home-nursing-care-     /  (home)            /dementia-care/
 + 6 town pages   services/ + service pgs        |                referral form
      |                    |                      |                     |
      +---------+----------+----------+-----------+                     |
                           v                                            |
                  ============================                         |
                  | HOME  /  — 5-sec clarity |  <-- [FRAMEWORK] every  |
                  | hero + 4 service cards   |      section ends in an  |
                  ============================      invitation to act   |
                           |                                            |
            (each section's CTA / "Learn More")                        |
                           v                                            |
                  ----------------------------                         |
                  | CONSIDERATION             |                        |
                  | service pages + /about-us/|                        |
                  | + Why-Choose-Us trust band|  [FRAMEWORK add]       |
                  | + Testimonials page       |  [FRAMEWORK add]       |
                  ----------------------------                         |
                     |                  X  <-- DROP: 404 personalised   |
                     |                       link; no pricing/FAQ       |
                     v                                                  |
                  ----------------------------                         |
                  | DECISION / CONTACT        |                        |
                  | /contact-us/  (call/form) |                        |
                  | funding + FAQ [FRAMEWORK] |                        |
                  ----------------------------                         |
                     |                  \                               |
        click-to-call|                   \  /book-an-appointment/       |
        0419 853 811 |                    \  (widget)                   |
        (always-on,  |                     \    X <-- DROP: "No         |
         mobile)     |                      \      matching data" /     |
                     |                       \     by-appt-only         |
                     v                        v                         v
              ===================================================================
              |     PRIMARY CONVERSION: "Book a free care consultation"          |
              |     OR call 0419 853 811   OR submit dementia referral           |
              ===================================================================
                                            |
                                            v
                                 RETENTION  ->  REFERRAL / ADVOCACY
                              (care delivered)   (reviews, brokerage,
                                                  professional referrals)
```

*Framework rule honoured: a visitor "understands what you do and how to act within five seconds," and "every homepage scroll ends with a clear, friendly invitation to act." Each X marks a current drop-off the build must close.*

---

## 6a. Dementia Referral Journey (provider / GP / family)

**Audience:** Persona C. **Single touchpoint today:** `/dementia-care/` (most modern page, modified 2026-05-18).

```
 Referrer becomes aware ──> /dementia-care/ (Overview + values chips:
 (GP, SaH coordinator,        Person-centred · Compassionate · Practical ·
  provider, or family)        Aligned with aged care standards)
        |
        v
 Reads "Who We Support" / "How We Help" / Specialist Clinical Services
 (Behaviour Assessment · Individualised Care Planning · Family & Carer
  Support · Provider & Workforce Consultation · Quality of Life ·
  Assessment & Ongoing Support)
        |
        v
 TWO paths (framework: clear invitation to act):
   (a) "Complete Online Referral" -> on-page form
   (b) "Contact Dementia Care"   -> Annette 0419 853 811 /
                                     Lisa Tyter 0477 051 130 /
                                     dementiacare@innerpeace.vision
        |
        v
 ONLINE REFERRAL FORM (sections, verbatim from crawl):
   1. Referral Details   — provider name, SaH level, referrer name/phone/email
   2. Client/Patient     — title, gender, DOB, names, contact, address,
                           ATSI background, Medicare #, Pension/DVA
   3. Reason for Referral— goals of assessment + current concerns
   4. Contacts & Care Team— next of kin, emergency contact,
                           medical decision-maker, GP, other professionals
   5. Home Visit Risk    — home-visit agreement, parking, pets, smoking,
                           infectious disease, firearms, access notes
   6. Privacy notice + 3 consent checkboxes (collect/use info · contact
      professionals · accuracy)
        |
        v
 SUBMIT (reCAPTCHA) -> sent to "designated Inner Peace Vision email addresses"
        |
        v
 Inner Peace triages -> home visit / assessment -> care planning
```
**Friction / improvements:**
- The form references "Inner Peace Vision" / "Inner Peace Services" — unify to the legal brand to reassure clinical referrers. **[FRAMEWORK]**
- No stated turnaround time for referrals (recruitment has "5 business days"; referrals have none) — add an expected-response line to reduce referrer anxiety. **[FRAMEWORK]**
- This is the *only* dementia entry point — surface it in main nav under Services → Dementia and as a CTA for professional referrers.

## 6b. Carer Recruitment Journey (DISC + Interview Form)

**Audience:** Persona D. **Requirement:** Cert III in Aged Care **or** RN (`/contact-us/`).

```
 Candidate aware (social / search / word-of-mouth)
        |
        v
 /contact-us/ "Employment Opportunities" + "Join Our Team"
   ("you need to fill in the DISC Personal Profile System and Interview Form")
        |
        +-----------------------------+
        v                             v
 /disc-personal-profile-system/   /interview-form/
   - 24 groups, pick MOST + LEAST    - "Screening Questionnaire" (20 Qs)
     (▲ ■ ★ N/Z symbols)             - sector intro + identity/address fields
   - linked DISC-WORD-EXPLANATION    - Q1-16 qualities/experience/strengths
     PDF                              - Q17-19 physical capacity / H&S
   - reCAPTCHA, Submit                - Q20 what you seek next; Send
        |                             |
        +-------------+---------------+
                      v
        Submission -> Inner Peace review
                      |
                      v
        "If your application is successful, we will contact you
         within 5 business days to discuss the next steps."
                      |
                      v
              Next steps / interview / onboarding -> becomes a matched carer
```
**Friction / improvements:**
- **Forms are orphaned** — not in sitemap or nav; only reachable via a text link on `/contact-us/`. Build a `/careers/` ("Join our team") landing page that explains the role, values, requirements (Cert III or RN), and the 2-step process, then links both forms in order. **[FRAMEWORK]** ("Join our team" is a named conversion path.)
- Two separate forms with no progress indicator between them — state up front it's a 2-part application so candidates don't abandon after DISC.
- DISC page has an empty-alt `Screenshot.png` example and typos in option words ("Agressive", "Diciplined", "Questionairre") — polish for employer credibility.
- The "5 business days" promise is good expectation-setting — keep and surface it on the new careers page.

---

### Cross-cutting principles applied throughout
1. **Mobile-first, late-night, anxious buyer** → persistent click-to-call, single primary CTA, 5-second clarity.
2. **Surface trust fastest** → Cert III/CPR/First Aid, full insurance, RN founder, reviews moved up and made into a band/page.
3. **Every section ends in an invitation to act** → reflected in the funnel and each journey stage.
4. **One consistent path to every service** → fix the 404, unify URL patterns, put Dementia + Careers in nav.
5. **Separate internal from external** → Staff Portal off public nav (`/login/`, `/password-reset/`).
