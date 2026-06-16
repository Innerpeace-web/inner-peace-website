/* =============================================================
   Inner Peace — main.js
   Reusable, dependency-free modules (progressive enhancement).
   Each module no-ops gracefully if its markup is absent.
   ============================================================= */
(function () {
  "use strict";
  document.documentElement.classList.add("js");

  /* ---------- Analytics hook (vendor-agnostic) ----------
     Pushes to dataLayer if present, else logs. Swap for your endpoint. */
  function track(event, detail) {
    var payload = Object.assign({ event: event, ts: Date.now() }, detail || {});
    if (window.dataLayer && typeof window.dataLayer.push === "function") {
      window.dataLayer.push(payload);
    } else if (window.console) {
      console.debug("[track]", payload);
    }
  }
  window.IP = window.IP || {};
  window.IP.track = track;

  /* ---------- Mobile navigation ---------- */
  function initNav() {
    var toggle = document.querySelector(".nav-toggle");
    var menu = document.getElementById("nav-menu");
    if (!toggle || !menu) return;

    function close() { toggle.setAttribute("aria-expanded", "false"); menu.classList.remove("open"); }
    function open() { toggle.setAttribute("aria-expanded", "true"); menu.classList.add("open"); }

    toggle.addEventListener("click", function () {
      var expanded = toggle.getAttribute("aria-expanded") === "true";
      expanded ? close() : open();
    });
    // Close on Escape / outside click / resize to desktop
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") close(); });
    document.addEventListener("click", function (e) {
      if (!menu.contains(e.target) && !toggle.contains(e.target)) close();
    });
    window.addEventListener("resize", function () { if (window.innerWidth >= 980) close(); });
  }

  /* ---------- Click-to-call / book tracking ---------- */
  function initCtaTracking() {
    document.querySelectorAll('a[href^="tel:"]').forEach(function (a) {
      a.addEventListener("click", function () { track("call_click", { number: a.getAttribute("href") }); });
    });
    document.querySelectorAll("[data-cta]").forEach(function (a) {
      a.addEventListener("click", function () { track("cta_click", { cta: a.getAttribute("data-cta") }); });
    });
  }

  /* ---------- Scroll reveal (IntersectionObserver) ---------- */
  function initReveal() {
    var items = document.querySelectorAll(".reveal");
    if (!items.length) return;
    if (!("IntersectionObserver" in window)) {
      items.forEach(function (el) { el.classList.add("is-visible"); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add("is-visible"); io.unobserve(entry.target); }
      });
    }, { rootMargin: "0px 0px -10% 0px", threshold: 0.08 });
    items.forEach(function (el) { io.observe(el); });
  }

  /* ---------- Scroll depth (engagement metric) ---------- */
  function initScrollDepth() {
    var marks = [25, 50, 75, 100], sent = {};
    function onScroll() {
      var h = document.documentElement;
      var pct = Math.round(((h.scrollTop + window.innerHeight) / h.scrollHeight) * 100);
      marks.forEach(function (m) { if (pct >= m && !sent[m]) { sent[m] = true; track("scroll_depth", { percent: m }); } });
    }
    var t;
    window.addEventListener("scroll", function () { clearTimeout(t); t = setTimeout(onScroll, 200); }, { passive: true });
  }

  /* ---------- Booking widget (multi-step, accessible) ---------- */
  function initBooking() {
    var widget = document.querySelector("[data-booking]");
    if (!widget) return;
    var panels = Array.prototype.slice.call(widget.querySelectorAll(".booking__panel"));
    var steps = Array.prototype.slice.call(widget.querySelectorAll(".booking__steps li"));
    var current = 0;

    function show(i) {
      current = Math.max(0, Math.min(i, panels.length - 1));
      panels.forEach(function (p, idx) { p.hidden = idx !== current; });
      steps.forEach(function (s, idx) {
        if (idx === current) { s.setAttribute("aria-current", "step"); } else { s.removeAttribute("aria-current"); }
      });
      var heading = panels[current].querySelector("h2, h3");
      if (heading) { heading.setAttribute("tabindex", "-1"); heading.focus(); }
      track("booking_step", { step: current + 1 });
    }

    widget.addEventListener("click", function (e) {
      var next = e.target.closest("[data-next]");
      var prev = e.target.closest("[data-prev]");
      if (next) {
        // simple required-field guard on current panel
        var required = panels[current].querySelectorAll("[required]");
        var ok = true;
        required.forEach(function (f) {
          if (f.type === "radio") {
            var group = panels[current].querySelectorAll('input[name="' + f.name + '"]');
            if (![].some.call(group, function (g) { return g.checked; })) ok = false;
          } else if (!f.value) { ok = false; }
        });
        if (!ok) { panels[current].setAttribute("data-invalid", "true"); return; }
        show(current + 1);
      }
      if (prev) show(current - 1);
    });

    var form = widget.querySelector("form");
    if (form) {
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        track("booking_submit", {});
        var status = widget.querySelector(".form-status");
        if (status) {
          status.setAttribute("data-state", "success");
          status.hidden = false;
          status.textContent =
            "Thank you — your consultation request has been received. Annette or the team will call you within 1 business day. For anything urgent, call 0419 853 811.";
        }
        panels.forEach(function (p) { p.hidden = true; });
      });
    }
    show(0);
  }

  /* ---------- Generic form (contact / referral / careers) ---------- */
  function initForms() {
    document.querySelectorAll("form[data-ajax]").forEach(function (form) {
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        var status = form.querySelector(".form-status");
        // Native validation first
        if (!form.checkValidity()) { form.reportValidity(); return; }
        track("form_submit", { form: form.getAttribute("name") || "form" });
        if (status) {
          status.setAttribute("data-state", "success");
          status.hidden = false;
          status.textContent = form.getAttribute("data-success") ||
            "Thank you — we’ve received your message and will be in touch shortly.";
        }
        form.reset();
      });
    });
  }

  /* ---------- Footer year ---------- */
  function initYear() {
    var el = document.querySelector("[data-year]");
    if (el) el.textContent = new Date().getFullYear();
  }

  document.addEventListener("DOMContentLoaded", function () {
    initNav();
    initCtaTracking();
    initReveal();
    initScrollDepth();
    initBooking();
    initForms();
    initYear();
  });
})();
