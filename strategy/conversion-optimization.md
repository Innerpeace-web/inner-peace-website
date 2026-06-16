# Inner Peace In-Home Nursing & Care — Conversion Rate Optimisation (CRO)

> Source of truth: `strategy/_facts.md` + `innerpeace-crawl/*.json`. Governing standard: the Strategic Website Framework (homepage six-section model, primary CTA "Book a free care consultation", click-to-call 0419 853 811 always reachable, trust surfaced "where they build trust fastest", targets +40% enquiries / 2× mobile engagement). Nothing invented; every observation cites a crawled page.

Audience reality (framework): *"Choosing in-home care is an emotional, high-trust decision — often made by an adult child researching on a phone, late at night."* Every recommendation below is judged against that moment.

---

## 1. Conversion Goals

| Tier | Goal | Action / mechanism | Current state in crawl |
|---|---|---|---|
| **Primary** | **Book a free care consultation** | Single primary button → `/book-an-appointment/` widget | Exists, but labelled "Book Now" / "Book an Appointment" (not "free consultation"); buried multi-step widget (`/book-an-appointment/`) |
| **Primary** | **Click-to-call 0419 853 811** | `tel:+61419853811` from any page, esp. mobile | `tel:` link exists **only** inside the booking widget and dementia page (`/book-an-appointment/`, `/dementia-care/`). Contact page lists the number as **plain text, not tappable** (`/contact-us/`) |
| **Secondary** | **Dementia online referral** | `#online-referral` form on `/dementia-care/` ("Complete Online Referral") | Strong form exists; isolated to one off-pattern page |
| **Secondary** | **General contact form** | "Let's connect!" form (`/contact-us/`) | Exists; only on contact page; reCAPTCHA friction |
| **Secondary** | **Join our team** | DISC Personal Profile System + Interview Form | Both forms exist but **orphaned** — not in sitemap nav, only linked from a paragraph on `/contact-us/` |

**Availability constraint (must be designed around, not hidden):** service is **"by appointment only"**, with urgent help available *"even outside regular business hours"* (`/book-an-appointment/`, `/contact-us/`). CRO implication: the call path must be framed as the fast lane ("Call now — we answer outside business hours for urgent care"), and booking framed as the considered lane.

---

## 2. Existing CTA Audit (per page, verbatim)

| Page (crawl) | CTA(s) present — verbatim | Type | Placement | Problems |
|---|---|---|---|---|
| `/` Home | "Learn more" → `/#learn-more`; "Book Now" → `/book-an-appointment/` | learn-more + book | Hero (text-only hero, no image) | Hero offers **two competing buttons**; "Learn more" is a vague anchor jump; framework wants a **single** primary "Book a free care consultation" + quiet trust cue |
| `/` Home | "Learn More" ×4 (Personal/Social/Nursing/Dementia cards) | learn-more | Services grid | Four identical "Learn More" labels — no differentiation, weak verbs |
| `/` Home | "Book an appointment" → `/book-an-appointment/` | book | Mid-page after trust copy | Only one mid-page conversion; reviews + Contact section below it end with… |
| `/` Home | "Scroll to the top of the page" → `/#` | scroll-to-top | Page foot (the final "CTA") | The page's **last call to action is to scroll up** — the closing CTA band (book / call / careers) the framework prescribes is absent |
| `/about-us/` | "Book an Appointment" → `/book-an-appointment/`; "Scroll to the top of the page" | book + scroll-to-top | After Annette bio / foot | Founder-RN trust story (30 yrs, palliative grad cert) is the strongest asset on the site yet ends in a scroll-to-top, not a "Book a free consultation with Annette" |
| `/in-home-nursing-care-services/` (hub) | "Learn More" ×4; "Scroll to the top of the page" | learn-more + scroll-to-top | Cards + foot | Says *"Explore our three services below"* but shows **four** cards (`/in-home-nursing-care-services/`); **no booking/call CTA at all** on the hub |
| `/…/personal-care/` | "Book an Appointment"; 3× "Learn More" (other services); "Scroll to the top" | book + learn-more + scroll-to-top | After task list + foot | Good single "Book an Appointment" but no click-to-call; ends scroll-to-top |
| `/…/social-care/` | same pattern as personal-care | book + learn-more + scroll-to-top | same | same |
| `/…/nursing-care/` | same pattern | book + learn-more + scroll-to-top | same | same; clinical credibility not paired with a call option |
| `/…/foot-care/` | "Coming Soon!"; 3× "Learn More"; "Scroll to the top" | learn-more + scroll-to-top | Thin page | **No primary CTA**; indexable dead-end (`/…/foot-care/`); old 2023/11 PNG cards |
| `/in-home-nursing-care-benefits/` | "Book an Appointment"; "Scroll to the top" | book + scroll-to-top | After 16-bullet benefits wall | One generic book CTA after a long unbroken benefits list; no call, no inline CTAs |
| `/area-served/` (hub) | town links only; "Scroll to the top" | (navigation) + scroll-to-top | List + foot | **No conversion CTA** on the area hub — pure link list |
| `/area-served/…-{town}/` (×6) | "Book an appointment"; 4× "Learn More"; "Scroll to the top" | book + learn-more + scroll-to-top | After town copy + foot | Six near-identical templated pages, same hero `image-09`; one generic book CTA, **no local phone CTA** ("call us about care in Bairnsdale") |
| `/dementia-care/` | "Complete Online Referral" → `#online-referral`; "Contact Dementia Care" → `#ips-contact`; `tel:0419853811`; `tel:0477051130`; "Scroll to the top" | referral + call + scroll-to-top | Hero + contact block | **Best-converting page** — clear dual CTA + tappable phones. Off-pattern URL though; uses "Inner Peace Vision/Services" naming |
| `/book-an-appointment/` | "Continue"; `tel:+61419853811`; `mailto:annette@…`; "Scroll to the top" | book(step) + call | Widget | See §6 — multi-step, "No matching data" empty state |
| `/contact-us/` | "Submit" (form); "0419 853 811" ×5 (**plain text, not `tel:` links**); DISC + Interview Form links; "Scroll to the top" | form + (call-as-text) + careers | Sections + foot | Phone repeated 5× but **none are click-to-call**; careers buried in prose |
| `/disc-personal-profile-system/`, `/interview-form/` | form submit only | careers form | Orphaned | Not in nav/sitemap; no "Join our team" entry surfaces them |

**Dominant anti-patterns (framework-flagged):**
1. **"Scroll to the top of the page"** appears as the terminal element on *every* page — the site's most consistent "CTA" is a no-op. Framework: *"Every homepage scroll ends with a clear, friendly invitation to act."*
2. **"Learn More" repeated 4× per page** with identical labels — weak, undifferentiated.
3. **"Book Now" / "Book an Appointment"** everywhere vs the framework's emotionally-de-risked **"Book a free care consultation."**
4. **Home hero = "Learn more" + "Book Now"** (two buttons, no image, no trust cue) vs framework's single-button confident hero + *"Caring for East Gippsland since 2022."*

---

## 3. Missing CTAs

| Missing element | Framework expectation | Evidence of absence | Impact |
|---|---|---|---|
| **Persistent click-to-call in header** | "click-to-call 0419 853 811 always reachable on mobile" | No header CTA anywhere in crawl; number is plain text on `/contact-us/` | Highest-intent mobile users (adult child, late night) cannot tap to call |
| **Sticky mobile call/book bar** | mobile-first, single primary action | None present | Lost mobile conversions on long pages (benefits, services) |
| **Consultation CTA on benefits & area pages beyond generic "Book an Appointment"** | each scroll ends with an invitation to act | Benefits page = one button after 16 bullets; area pages = one generic button (`/in-home-nursing-care-benefits/`, area pages) | Local + benefit-aware intent not captured |
| **Careers CTA surfaced ("Join our team")** | "Join our team" recruitment path | DISC + Interview forms orphaned; only a prose link on `/contact-us/` | Recruitment pipeline invisible |
| **Email / lead-magnet capture** | surface trust & capture considering visitors | No newsletter/guide/email capture on any page | No way to nurture "researching, not ready" visitors |
| **Click-to-call on service & area pages** | call always reachable | service/area pages have book button but no `tel:` | Phone-preferring users dead-end |
| **Closing CTA band on home** | section (F): book / call 0419 853 811 / Join our team | Home ends with reviews → Contact image → scroll-to-top | No final conversion moment |

---

## 4. Conversion Paths (with friction per step)

Mapped against real intent. Friction cited to crawled pages.

**Path A — Home → Service → Book (primary buyer journey)**
```
/ (hero: "Learn more"/"Book Now")
  → /in-home-nursing-care-services/ (hub, 4 cards, NO book/call CTA)
    → /…/personal-care/ ("Book an Appointment")
      → /book-an-appointment/ (3-step widget)
```
- Friction 1: Hero splits attention between "Learn more" and "Book Now"; no trust cue; no image (`/`).
- Friction 2: Hub page has **zero** conversion CTA — pure "Learn More" cards; momentum dies (`/in-home-nursing-care-services/`).
- Friction 3: "Book an Appointment" ≠ low-commitment "free consultation"; word "Appointment" implies obligation.
- Friction 4: Widget multi-step + "No matching data" (§6).
- **Leak:** Home & About link the phrase "personalised care" to **`/home-care-services/personal-care/`** whose parent **`/home-care-services/` is a 404** (`/`, `/about-us/`, `/home-care-services/` = *"This page could not be found!"*). High-intent click → dead end → bounce.

**Path B — Area → Book (local intent)**
```
/area-served/ (link list, NO CTA)
  → /area-served/…-bairnsdale/ ("Book an appointment")
    → /book-an-appointment/
```
- Friction: area hub has no CTA; town pages are thin duplicates (same hero `image-09`, town name swapped) with one generic book button and **no local phone CTA** (area pages).

**Path C — Dementia → Referral (specialist intent) — strongest path**
```
/dementia-care/ ("Complete Online Referral" + "Contact Dementia Care" + tappable phones)
  → #online-referral form (provider/client/risk/consent)
```
- Low friction at entry (dual CTA, click-to-call present). Friction inside: long clinical form (SaH level, Medicare/DVA, risk assessment, 3 consents) — appropriate for referrers but heavy for a family member; no "not a referrer? call us" shortcut. Off-pattern URL hurts discoverability from main nav.

**Path D — Contact → Call (urgent intent)**
```
/contact-us/ ("Call us at 0419 853 811" ×5, plain text) OR "Submit" form
```
- Friction: the number a panicked mobile user most needs to tap is **not a `tel:` link** anywhere on `/contact-us/`; they must memorise/copy it. Form adds reCAPTCHA friction. Careers content dilutes the page's conversion focus.

---

## 5. Trust-Building Opportunities (framework: surface trust "where they build trust fastest")

Inner Peace has unusually strong, **crawl-verified** trust assets that are currently buried in prose. Surface them as scannable, repeatable components.

| Trust asset (verbatim source) | Where it currently lives | Recommended surfacing |
|---|---|---|
| **Cert III in Aged/Community Care + CPR + First Aid** (all carers) | Buried in "Team of Qualified Carers" paragraph (`/`) | Badge in a **trust band** on every page + footer: "Cert III qualified" |
| **Fully insured** — public liability, professional indemnity, work cover (`/`) | "Safety is Our Priority" paragraph | Badge: "Fully insured" (framework-named badge) |
| **Personalised carer matching** — by "personality, required medical attention, and other specific preferences" (`/`) | "Selecting your carers" / "Personalised Care" paragraphs | Pillar card: "Matched to you, not a roster" |
| **RN founder, 30 yrs + 12 yrs home nursing + Palliative Care Grad Cert 2020** (`/about-us/`) | About page bio only | Founder trust block on home + a face-and-name credibility cue near primary CTA ("Talk to Annette, RN") |
| **"Since 2022", happy clients in East Gippsland** (`/`) | One sentence on home | Quiet hero trust cue per framework: *"Caring for East Gippsland since 2022"* |
| **3 client testimonials** (verbatim, `/`) | Bottom-buried, unattributed, numbered 1-2-3 | Dedicated **Testimonials** section/page "given room to breathe" (framework §D); pull the strongest line ("helped me escape bouts of depression and improved my … well-being") near booking CTA |
| **Brokerage with accredited Bairnsdale providers + self-management guidance** (`/contact-us/`) | Contact page prose | Reassurance line near funding/eligibility content (§7) |

**Recommended component — "Why choose us" trust band** (framework section C, 4 pillars): `Cert III + CPR + First Aid` · `Fully insured` · `Personalised carer matching` · `Locally owned, RN-founded, since 2022`. Render as 4 badge-cards with generous whitespace ("light and airy"), placed (a) on home between services and testimonials, and (b) as a compact strip above every page's footer CTA. Add `LocalBusiness`/`MedicalBusiness` + `Review` JSON-LD (currently absent — defect #14) so trust signals also surface in search.

---

## 6. Appointment Booking Flow

**Current state (`/book-an-appointment/`, verbatim crawl):**
- Heading: "Book an Appointment" → *"Welcome! Let's get you set up with a convenient time by booking an appointment that fits your agenda."*
- Multi-step tabs: **Services → Date & Time → Your Information**.
- Step 1 service options: **"Home Care Services(3)"** and **"Phone Consultation(1)"**, then a "Continue" button.
- Empty state shows **"No matching data"** (no service preselected → dead screen).
- "Get in Touch" sidebar with `tel:+61419853811` + `mailto:annette@…`.
- reCAPTCHA on the step. Page **last modified 2023-12-04** (stalest page on the site).

**Problems:**
1. Three steps before any human contact; high abandonment for an emotional decision.
2. **"No matching data"** is a broken-feeling empty state — the worst possible first impression at the conversion moment.
3. "Book an Appointment" framing implies commitment; framework wants **free consultation**.
4. Opaque labels ("Home Care Services(3)", "Phone Consultation(1)") — counts, not benefits.
5. Click-to-call is demoted to a sidebar, not offered as the easy alternative.
6. reCAPTCHA + small widget controls = poor mobile tap targets.

**Recommended friction-reduced flow:**

| Step | Now | Recommended |
|---|---|---|
| Entry | "Book an Appointment" + 3 tabs | **One screen, one primary action:** "Book a free care consultation" with a clear value line ("A no-obligation chat about your needs — by phone or at home"). |
| Choice | Services → Date → Info | Collapse to **name + phone + "best time to call"** (3 fields). Service/date handled in the consult, not the form. |
| Fallback | Phone in sidebar | **Prominent click-to-call** `tel:+61419853811`: "Prefer to talk now? Call 0419 853 811 — we answer outside business hours for urgent care." (honours "by appointment only" + urgent-care promise). |
| Empty state | "No matching data" | Eliminate; never show a dead screen. Default a sensible option. |
| Trust at point of action | none | Inline mini trust band (Fully insured · Cert III · RN-founded) + one testimonial line. |
| Mobile | small controls + reCAPTCHA | Tap targets **≥44px**; replace/relegate reCAPTCHA (honeypot + server check for static build); large tappable phone button. |
| Confirmation | unknown | Expectation-setting confirmation: *"Thanks — Annette or the team will call you within 1 business day. For urgent help, call 0419 853 811 now."* Set the "5 business days" expectation only where it applies (careers, per `/contact-us/`). |

---

## 7. Lead-Generation Opportunities

| Opportunity | Rationale (cited) | Mechanism | Captures |
|---|---|---|---|
| **Funding & eligibility guide (lead magnet)** | No funding/eligibility content exists; brokerage + self-management mentioned only in prose (`/contact-us/`); cost a top concern for families. | "Understanding Home Care Funding in East Gippsland" PDF/page → email capture | Researching-but-not-ready visitors (the late-night adult child) |
| **Callback request ("We'll call you")** | Phone is the de-facto primary action but only the dementia/booking pages expose `tel:`; "by appointment only" suits a callback model. | 2-field micro-form (name + phone + best time) on every page footer | Phone-preferring, low-friction leads |
| **Dementia referral as a tracked conversion** | Full referral form already exists (`/dementia-care/`), arguably the highest-value lead, but is isolated and untracked. | Surface in main nav (Services → Dementia); add "not a referrer? call us" branch; fire a conversion event on submit | Provider + family referrals |
| **Careers pipeline ("Join our team")** | DISC + Interview forms orphaned; requirement "Cert III in Aged Care or RN" stated only on `/contact-us/`. | Real `/careers/` (or Resources entry) landing → DISC + Interview forms; "successful applicants contacted within 5 business days" expectation already on site | Carer recruitment (capacity = future client capacity) |
| **Testimonials/social proof page** | 3 verbatim reviews buried (`/`). | Dedicated page + review schema + "Client-reviewed" badge | Trust-stage assist conversions |

---

## 8. Prioritised CRO Backlog (Impact × Effort)

Tied to framework targets: **+40% enquiries, 2× mobile engagement.**

| Priority | Action | Impact | Effort | Expected effect |
|---|---|---|---|---|
| **NOW** | Persistent **header click-to-call** + **sticky mobile call/book bar** (`tel:+61419853811`) on every page | High | Low | Direct lift to call volume; primary driver of **2× mobile engagement** |
| **NOW** | Make all `/contact-us/` phone instances real `tel:` links (currently plain text ×5) | High | Low | Recovers high-intent urgent-care taps |
| **NOW** | Fix the **`/home-care-services/` 404 leak** — repoint home + about "personalised care" links to `/…/personal-care/` | High | Low | Stops bounce of high-intent clicks (Path A leak) |
| **NOW** | Rename CTAs site-wide → **"Book a free care consultation"**; remove every "Scroll to the top of the page" terminal CTA | High | Low | De-risks the ask; replaces no-op CTAs with real ones |
| **NOW** | Kill the **"No matching data"** empty state; preselect a default in the booking widget | High | Low | Removes a conversion-killer at the decision point |
| **NEXT** | Add **closing CTA band** (book / call / Join our team) to home + every page footer (framework §F) | High | Med | Every scroll ends with an invitation to act → enquiry lift toward **+40%** |
| **NEXT** | Build **"Why choose us" trust band** + badges (Fully insured · Cert III · Personalised matching · RN-founded since 2022) | High | Med | Trust lift at the moment of decision; improves all-path conversion |
| **NEXT** | Simplify booking to **single screen + click-to-call fallback + confirmation** (§6) | High | Med | Cuts abandonment in the primary funnel |
| **NEXT** | **Dementia referral** into main nav + tracked conversion + "call us" branch | Med | Low | Converts the highest-value lead path |
| **NEXT** | **Testimonials** section "with room to breathe" + review schema | Med | Med | Social-proof assist across funnel |
| **LATER** | **Funding & eligibility guide** lead magnet + email capture | Med | Med | Nurtures not-ready researchers |
| **LATER** | **Callback request** micro-form on all footers | Med | Med | New low-friction lead type |
| **LATER** | Real **`/careers/`** landing surfacing DISC + Interview forms | Med | Med | Unblocks recruitment pipeline |
| **LATER** | **LocalBusiness/MedicalBusiness + Review JSON-LD** (defect #14) | Med | Low | Trust signals in SERP; rich results |
| **LATER** | Consolidate thin area pages; add local phone CTA per town; complete or de-index `/…/foot-care/` | Low | Med | Reduces duplicate-content drag; local conversion |

---

## 9. Measurement Plan (static HTML5 + vanilla JS)

Build target is static (no WordPress analytics plugin), so instrument with a small reusable JS module posting to an analytics endpoint (e.g. `/api/track` or a privacy-light analytics service). Progressive enhancement: tracking never blocks the action.

**Events to capture (vanilla JS):**

| Event | Trigger | How |
|---|---|---|
| `call_click` | Tap on any `tel:+61419853811` (header, sticky bar, page body) | Delegated listener on `a[href^="tel:"]`; send `{location, page}` |
| `book_cta_click` | "Book a free care consultation" button | `data-cta="book"` + click listener |
| `booking_step_complete` | Each step / final submit of booking form | Fire on step advance + on confirmation page view |
| `consult_form_submit` | Callback / consultation form submit | `submit` handler + success state |
| `dementia_referral_submit` | `#online-referral` submit | dedicated event (high-value) |
| `contact_form_submit` | `/contact-us/` "Let's connect!" submit | `submit` handler |
| `careers_form_submit` | DISC / Interview Form submit | dedicated event |
| `lead_magnet_download` | Funding guide email capture | `submit` handler |
| `scroll_depth` | 25/50/75/100% page reach | `IntersectionObserver` sentinels (cheap, passive) |
| `outbound_click` | Facebook/YouTube/Instagram, map | `a[target=_blank]` / `a[href*=...]` |
| `error_404` | Landing on a not-found page | fire on 404 template (track residual `/home-care-services/` hits) |

**Pattern (illustrative):**
```js
function track(event, props={}) {
  navigator.sendBeacon('/api/track',
    JSON.stringify({ event, ...props, path: location.pathname, ts: Date.now() }));
}
document.addEventListener('click', e => {
  const tel = e.target.closest('a[href^="tel:"]');
  if (tel) track('call_click', { location: tel.dataset.loc || 'body' });
  const book = e.target.closest('[data-cta="book"]');
  if (book) track('book_cta_click', { location: book.dataset.loc || 'body' });
});
```

**KPIs:**

| Tier | KPI | Definition | Framework target |
|---|---|---|---|
| **Primary** | Total enquiries | `call_click` + `consult_form_submit` + `dementia_referral_submit` + `contact_form_submit` | **+40%** vs baseline |
| **Primary** | Mobile engagement | mobile sessions reaching scroll 50% + tapping a CTA (`call_click`/`book_cta_click`) | **2×** |
| **Primary** | Booking completion rate | `booking_step_complete(final)` ÷ `book_cta_click` | trend up after §6 simplification |
| **Secondary** | Click-to-call rate | `call_click` ÷ sessions (segment mobile vs desktop) | establish + grow |
| **Secondary** | Form abandonment | starts ÷ submits per form | reduce, esp. booking + dementia referral |
| **Secondary** | Lead-magnet capture | `lead_magnet_download` ÷ guide page views | establish |
| **Secondary** | Careers conversions | `careers_form_submit` | establish pipeline |
| **Guardrail** | 404 hits on `/home-care-services/` | `error_404` count | → 0 after fix |
| **Guardrail** | Avg scroll depth / page | from `scroll_depth` | confirm closing-CTA bands are reached |

Baseline first (2–4 weeks of current site or launch week), then evaluate NOW items, then NEXT, against the +40% / 2× targets.
