# Shared Partials — paste VERBATIM into every page

Two variants. **ROOT** = files directly in `website/` (index.html, about.html, etc.). **NESTED** = files one level deep (`services/`, `resources/`, `legal/`, `staff/`). The ONLY difference is path prefix (`` vs `../`). Set `aria-current="page"` on the active top-level nav item; remove it elsewhere.

The site uses: fonts (Fraunces + Hanken Grotesk), `styles.css`, `main.js`. Lang is `en-AU`. Phone `+61419853811` displayed as `0419 853 811`. Brand: **Inner Peace In-Home Nursing & Care**.

---

## A. `<head>` boilerplate

### ROOT
```html
<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>PAGE_TITLE</title>
<meta name="description" content="PAGE_DESCRIPTION">
<link rel="canonical" href="https://innerpeace.vision/CANONICAL_PATH">
<meta property="og:locale" content="en_AU">
<meta property="og:site_name" content="Inner Peace In-Home Nursing & Care">
<meta property="og:title" content="PAGE_TITLE">
<meta property="og:description" content="PAGE_DESCRIPTION">
<link rel="icon" href="https://innerpeace.vision/wp-content/uploads/2023/12/cropped-Logo-32x32.png" sizes="32x32">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Hanken+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/styles.css">
</head>
```
### NESTED — change last 2 asset lines + canonical to `../`:
`<link rel="stylesheet" href="../assets/css/styles.css">`, script `../assets/js/main.js`, all nav/footer links prefixed `../`.

---

## B. Header (ROOT)
```html
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container nav">
    <a class="brand" href="index.html" aria-label="Inner Peace In-Home Nursing & Care — home">
      <img src="https://innerpeace.vision/wp-content/uploads/2023/12/cropped-Logo-270x270.png" alt="" width="40" height="40">
      <span>Inner Peace<small>In-Home Nursing &amp; Care</small></span>
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav-menu" aria-label="Open menu">
      <span></span><span></span><span></span>
    </button>
    <div class="nav-menu" id="nav-menu">
      <ul class="nav-list">
        <li><a href="index.html">Home</a></li>
        <li><a href="about.html">About</a></li>
        <li class="has-sub">
          <a href="services/index.html">Services</a>
          <ul class="submenu">
            <li><a href="services/personal-care.html">Personal Care</a></li>
            <li><a href="services/nursing-care.html">Nursing Care</a></li>
            <li><a href="services/social-care.html">Social Care</a></li>
            <li><a href="services/dementia-care.html">Dementia Care</a></li>
          </ul>
        </li>
        <li><a href="testimonials.html">Testimonials</a></li>
        <li class="has-sub">
          <a href="resources/index.html">Resources</a>
          <ul class="submenu">
            <li><a href="resources/area-served.html">Areas We Serve</a></li>
            <li><a href="resources/benefits.html">Benefits of Home Care</a></li>
            <li><a href="careers.html">Join Our Team</a></li>
          </ul>
        </li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
      <div class="nav-cta">
        <a class="btn btn--ghost" href="tel:+61419853811" data-cta="nav-call">0419 853 811</a>
        <a class="btn btn--primary" href="book.html" data-cta="nav-book">Book a free consultation</a>
      </div>
    </div>
  </div>
</header>
```
**NESTED header:** identical but every `href="X"` → `href="../X"` (e.g. `../index.html`, `../services/personal-care.html`, `../about.html`, `../book.html`). Same-dir links in `services/` can stay relative but using `../services/...` is safest and uniform.

---

## C. Footer (ROOT) — paste before `</body>` region
```html
<footer class="site-footer">
  <div class="container footer-grid">
    <div>
      <a class="brand" href="index.html" style="color:#fff">
        <img src="https://innerpeace.vision/wp-content/uploads/2023/12/cropped-Logo-270x270.png" alt="" width="40" height="40">
        <span style="color:#fff">Inner Peace<small style="color:var(--sage)">In-Home Nursing &amp; Care</small></span>
      </a>
      <p style="margin-top:var(--sp-3);color:#bcd6d2;max-width:34ch">Personalised care, in the comfort of your own home. Caring for East Gippsland since 2022.</p>
      <div class="footer-social">
        <a href="https://www.facebook.com/innerpeace.vision" aria-label="Facebook"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M14 9h3V6h-3c-2 0-3.5 1.5-3.5 3.5V11H8v3h2.5v7h3v-7H16l.5-3h-3V9.5C13.5 9.2 13.7 9 14 9z"/></svg></a>
        <a href="https://www.youtube.com/@innerpeace.vision7778" aria-label="YouTube"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M22 8.2a3 3 0 0 0-2.1-2.1C18 5.5 12 5.5 12 5.5s-6 0-7.9.6A3 3 0 0 0 2 8.2 31 31 0 0 0 1.6 12 31 31 0 0 0 2 15.8a3 3 0 0 0 2.1 2.1c1.9.6 7.9.6 7.9.6s6 0 7.9-.6a3 3 0 0 0 2.1-2.1c.3-1.3.4-2.5.4-3.8s-.1-2.5-.4-3.8zM10 15V9l5 3z"/></svg></a>
        <a href="https://www.instagram.com/innerpeace.vision/" aria-label="Instagram"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r="1.2" fill="currentColor" stroke="none"/></svg></a>
      </div>
    </div>
    <div>
      <h3>Services</h3>
      <ul class="footer-list">
        <li><a href="services/personal-care.html">Personal Care</a></li>
        <li><a href="services/nursing-care.html">Nursing Care</a></li>
        <li><a href="services/social-care.html">Social Care</a></li>
        <li><a href="services/dementia-care.html">Dementia Care</a></li>
      </ul>
    </div>
    <div>
      <h3>Explore</h3>
      <ul class="footer-list">
        <li><a href="about.html">About us</a></li>
        <li><a href="testimonials.html">Testimonials</a></li>
        <li><a href="resources/area-served.html">Areas we serve</a></li>
        <li><a href="resources/benefits.html">Benefits of home care</a></li>
        <li><a href="careers.html">Join our team</a></li>
      </ul>
    </div>
    <div>
      <h3>Get in touch</h3>
      <ul class="footer-list">
        <li><a href="tel:+61419853811">0419 853 811</a> (Annette)</li>
        <li><a href="mailto:admin@innerpeace.vision">admin@innerpeace.vision</a></li>
        <li><a href="book.html">Book a consultation</a></li>
        <li><a href="staff/index.html">Staff portal login</a></li>
      </ul>
      <p style="margin-top:var(--sp-3);font-size:var(--fs-200);color:#a9c6c3">By appointment only. For urgent help, call any time.</p>
    </div>
  </div>
  <div class="container footer-bottom">
    <span>© <span data-year>2026</span> Inner Peace In-Home Nursing &amp; Care. All rights reserved.</span>
    <span><a href="legal/privacy.html">Privacy Policy</a> · <a href="legal/terms.html">Terms &amp; Conditions</a></span>
  </div>
</footer>

<nav class="callbar" aria-label="Quick contact">
  <a class="call" href="tel:+61419853811" data-cta="callbar-call">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3 19.5 19.5 0 0 1-6-6 19.8 19.8 0 0 1-3-8.6A2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.2-1.3a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>
    Call us
  </a>
  <a class="book" href="book.html" data-cta="callbar-book">Book free consult</a>
</nav>

<script src="assets/js/main.js" defer></script>
</body>
</html>
```
**NESTED footer/callbar/script:** every internal `href`/`src` → `../` prefixed (`../services/...`, `../about.html`, `../book.html`, `../legal/privacy.html`, `../staff/index.html`, `../assets/js/main.js`). External `tel:`/`mailto:`/`https://` links unchanged.

---

## D. Interior page banner pattern (use under header on non-home pages)
```html
<section class="page-banner">
  <div class="container stack">
    <p class="eyebrow" style="color:var(--sage)">EYEBROW</p>
    <h1>PAGE H1</h1>
    <p>SUPPORTING SENTENCE.</p>
  </div>
</section>
<nav class="breadcrumbs container" aria-label="Breadcrumb">
  <ol>
    <li><a href="index.html">Home</a></li>   <!-- ../ if nested -->
    <li>CURRENT</li>
  </ol>
</nav>
```

## E. Verbatim content building blocks (from crawl — use exactly)
- Phone Annette: 0419 853 811 / tel:+61419853811. Lisa (dementia): 0477 051 130 / tel:0477051130.
- Emails: admin@innerpeace.vision (general), annette@innerpeace.vision (bookings), dementiacare@innerpeace.vision (dementia).
- Tagline: *Personalised Care, in the Comfort of Your Own Home*.
- Trust: "All our carers hold a minimum Certificate III in Aged/Community Care… CPR and First Aid." Insurances: public liability, professional indemnity, work cover. Carer matching by personality/medical need/preferences.
- 3 testimonials: see /Users/devan/Inner Peace/strategy/_facts.md §7 (use verbatim).
- Reuse the closing CTA band + trust badges patterns from index.html where useful.
