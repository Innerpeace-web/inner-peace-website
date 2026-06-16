import os

pages = [
    {
        "filename": "dashboard.html",
        "title": "Staff Dashboard",
        "h1": "Welcome back, team",
        "content": """
      <div class="grid grid--3">
        <div class="card reveal">
          <div class="card__content">
            <h3>Recent Announcements</h3>
            <p><strong>May 2026 Update:</strong> New CPR refresher dates have been posted.</p>
            <p><strong>April 2026 Update:</strong> Welcome to our new RN, Sarah!</p>
          </div>
        </div>
        <div class="card reveal">
          <div class="card__content">
            <h3>Upcoming Shifts</h3>
            <p>Your roster is up to date.</p>
            <a href="#" class="btn btn--ghost">View Roster</a>
          </div>
        </div>
        <div class="card reveal">
          <div class="card__content">
            <h3>Quick Actions</h3>
            <ul style="list-style:none;padding:0;display:grid;gap:0.5rem">
              <li><a href="forms.html">Submit Timesheet</a></li>
              <li><a href="forms.html">Request Leave</a></li>
              <li><a href="policies.html">View Policies</a></li>
            </ul>
          </div>
        </div>
      </div>
"""
    },
    {
        "filename": "resources.html",
        "title": "Staff Resources",
        "h1": "Staff Resources",
        "content": """
      <div class="grid grid--2-up">
        <div class="card reveal">
          <div class="card__content">
            <h3>External Portals</h3>
            <ul>
              <li><a href="#">Payroll System Login</a></li>
              <li><a href="#">Rostering App Login</a></li>
              <li><a href="#">Email Webmail</a></li>
            </ul>
          </div>
        </div>
        <div class="card reveal">
          <div class="card__content">
            <h3>Uniform Ordering</h3>
            <p>Order new scrubs, polo shirts, or name badges. Allow 2 weeks for delivery.</p>
            <a href="#" class="btn btn--primary">Order Uniforms</a>
          </div>
        </div>
      </div>
"""
    },
    {
        "filename": "training.html",
        "title": "Training Hub",
        "h1": "Training Hub",
        "content": """
      <div class="grid grid--3">
        <div class="card reveal">
          <div class="card__content">
            <h3>CPR & First Aid</h3>
            <p>Mandatory annual refresher. Due: Dec 2026.</p>
            <span class="badge">Incomplete</span>
            <br><br><a href="#" class="btn btn--ghost">Start Module</a>
          </div>
        </div>
        <div class="card reveal">
          <div class="card__content">
            <h3>Manual Handling</h3>
            <p>Safe lifting and moving techniques.</p>
            <span class="badge" style="background:var(--sage);color:var(--deep-teal)">Completed</span>
            <br><br><a href="#" class="btn btn--ghost">Review Module</a>
          </div>
        </div>
        <div class="card reveal">
          <div class="card__content">
            <h3>Dementia Care</h3>
            <p>Advanced communication and behavioral support.</p>
            <span class="badge" style="background:var(--sage);color:var(--deep-teal)">Completed</span>
            <br><br><a href="#" class="btn btn--ghost">Review Module</a>
          </div>
        </div>
      </div>
"""
    },
    {
        "filename": "policies.html",
        "title": "Policies & Procedures",
        "h1": "Policies & Procedures",
        "content": """
      <ul class="feature-list reveal" style="max-width:800px;margin:auto">
        <li><span><strong>Code of Conduct</strong> — Our expectations for professional behavior.</span> <a href="#">Download PDF</a></li>
        <li><span><strong>Privacy & Confidentiality</strong> — Handling client information securely.</span> <a href="#">Download PDF</a></li>
        <li><span><strong>Incident Reporting Procedure</strong> — Steps to take following a workplace or client incident.</span> <a href="#">Download PDF</a></li>
        <li><span><strong>Infection Control</strong> — PPE usage and hygiene standards.</span> <a href="#">Download PDF</a></li>
      </ul>
"""
    },
    {
        "filename": "forms.html",
        "title": "Forms Library",
        "h1": "Forms Library",
        "content": """
      <div class="grid grid--2-up">
        <div class="card reveal">
          <div class="card__content">
            <h3>HR & Admin</h3>
            <ul>
              <li><a href="#">Leave Request Form (PDF)</a></li>
              <li><a href="#">Timesheet Adjustment Form (PDF)</a></li>
              <li><a href="#">Change of Details Form (PDF)</a></li>
            </ul>
          </div>
        </div>
        <div class="card reveal">
          <div class="card__content">
            <h3>Clinical & Care</h3>
            <ul>
              <li><a href="#">Progress Notes Template (Word)</a></li>
              <li><a href="#">Incident Report Form (PDF)</a></li>
              <li><a href="#">Medication Chart Template (PDF)</a></li>
            </ul>
          </div>
        </div>
      </div>
"""
    },
    {
        "filename": "handbook.html",
        "title": "Employee Handbook",
        "h1": "Employee Handbook",
        "content": """
      <div class="reveal" style="max-width:80ch;margin:auto">
        <p>Welcome to Inner Peace In-Home Nursing & Care. This handbook is your guide to our mission, values, and workplace practices.</p>
        <div style="padding:var(--sp-4);background:var(--white);border:1px solid var(--line);border-radius:4px;margin-top:var(--sp-4)">
          <h3>Table of Contents</h3>
          <ol>
            <li><a href="#">Introduction & History</a></li>
            <li><a href="#">Our Values & Philosophy of Care</a></li>
            <li><a href="#">Employment Conditions</a></li>
            <li><a href="#">Work Health & Safety</a></li>
            <li><a href="#">Professional Development</a></li>
          </ol>
          <hr style="margin:var(--sp-4) 0;border:none;border-top:1px solid var(--line)">
          <a href="#" class="btn btn--primary">Download Full Handbook (PDF)</a>
        </div>
      </div>
"""
    },
    {
        "filename": "onboarding.html",
        "title": "Onboarding Resources",
        "h1": "Onboarding Resources",
        "content": """
      <div class="reveal" style="max-width:80ch;margin:auto">
        <p>Welcome to the team! Please complete the following checklist within your first week.</p>
        <ul class="feature-list" style="margin-top:var(--sp-4)">
          <li><input type="checkbox" checked> <span>Submit signed employment contract</span></li>
          <li><input type="checkbox" checked> <span>Provide Tax File Number and Superannuation details</span></li>
          <li><input type="checkbox"> <span>Provide current Police Check and NDIS Worker Screening Check</span></li>
          <li><input type="checkbox"> <span>Complete mandatory induction modules in the Training Hub</span></li>
          <li><input type="checkbox"> <span>Order your uniform</span></li>
        </ul>
      </div>
"""
    },
    {
        "filename": "support.html",
        "title": "Contact & Support",
        "h1": "Contact & Support",
        "content": """
      <div class="grid grid--2-up">
        <div class="stack reveal">
          <h3>Internal Directory</h3>
          <p><strong>Annette Keat (Director/RN Coordinator)</strong><br>Clinical support, urgent client escalations.<br><a href="tel:+61419853811">0419 853 811</a></p>
          <p><strong>Admin & HR</strong><br>Payroll, rostering, general inquiries.<br><a href="mailto:admin@innerpeace.vision">admin@innerpeace.vision</a></p>
          <p><strong>IT Support</strong><br>Portal access issues, email setup.<br><a href="mailto:support@innerpeace.vision">support@innerpeace.vision</a></p>
        </div>
        <div class="stack reveal">
          <h3>Submit a Request</h3>
          <form class="form" onsubmit="event.preventDefault(); alert('Request submitted successfully.');">
            <div class="field">
              <label>Topic</label>
              <select><option>Rostering</option><option>Payroll</option><option>IT Support</option><option>Other</option></select>
            </div>
            <div class="field">
              <label>Message</label>
              <textarea rows="4"></textarea>
            </div>
            <button type="submit" class="btn btn--primary">Send Request</button>
          </form>
        </div>
      </div>
"""
    }
]

template = """<!DOCTYPE html>
<html lang="en-AU">
<head>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({"gtm.start":new Date().getTime(),event:"gtm.js"});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!="dataLayer"?"&l="+l:"";j.async=true;j.src="https://www.googletagmanager.com/gtm.js?id="+i+dl;f.parentNode.insertBefore(j,f);})(window,document,"script","dataLayer","GTM-XXXXXXX");</script>
<!-- End Google Tag Manager -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{{title}} | Inner Peace Staff Portal</title>
<link rel="icon" href="../assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="../assets/img/apple-touch-icon.png">
<link rel="manifest" href="../site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Hanken+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/css/styles.css">
</head>
<body style="background:var(--cream)">
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-XXXXXXX" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

<a class="skip-link" href="#main">Skip to content</a>

<!-- ===== Staff Header ===== -->
<header class="site-header" style="background:var(--deep-teal);color:var(--white)">
  <div class="container nav">
    <a class="brand" href="dashboard.html" aria-label="Staff Portal Home" style="color:var(--white)">
      <img src="https://innerpeace.vision/wp-content/uploads/2023/12/cropped-Logo-270x270.png" alt="" width="40" height="40">
      <span style="color:var(--white)">Staff Portal<small style="color:var(--sage)">Inner Peace In-Home Care</small></span>
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav-menu" aria-label="Open menu" style="filter:invert(1)">
      <span></span><span></span><span></span>
    </button>
    <div class="nav-menu" id="nav-menu">
      <ul class="nav-list" style="--ink:var(--white);">
        <li><a href="dashboard.html" style="color:var(--white)">Dashboard</a></li>
        <li><a href="policies.html" style="color:var(--white)">Policies</a></li>
        <li><a href="training.html" style="color:var(--white)">Training</a></li>
        <li><a href="resources.html" style="color:var(--white)">Resources</a></li>
        <li class="has-sub">
          <a href="#" style="color:var(--white)">More</a>
          <ul class="submenu" style="background:var(--deep-teal)">
            <li><a href="forms.html" style="color:var(--white)">Forms</a></li>
            <li><a href="handbook.html" style="color:var(--white)">Handbook</a></li>
            <li><a href="onboarding.html" style="color:var(--white)">Onboarding</a></li>
          </ul>
        </li>
        <li><a href="support.html" style="color:var(--white)">Support</a></li>
      </ul>
      <div class="nav-cta">
        <a class="btn btn--primary" href="../index.html" style="background:var(--sage);color:var(--deep-teal)">Sign Out</a>
      </div>
    </div>
  </div>
</header>

<main id="main">

  <section class="page-banner" style="background:var(--teal);padding-block:var(--sp-6)">
    <div class="container center stack reveal">
      <h1 style="color:var(--white)">{{h1}}</h1>
    </div>
  </section>

  <section class="section">
    <div class="container">
{{content}}
    </div>
  </section>

</main>

<footer class="site-footer" style="padding-block:var(--sp-4);background:var(--white);border-top:1px solid var(--line);text-align:center">
  <div class="container">
    <p style="color:var(--muted);font-size:0.875rem">Inner Peace Staff Portal Prototype &copy; 2026. This is a static demonstration.</p>
  </div>
</footer>

<script src="../assets/js/main.js" defer></script>
</body>
</html>
"""

for page in pages:
    path = os.path.join("/Users/devan/Inner Peace/website/staff", page["filename"])
    html = template.replace("{{title}}", page["title"]).replace("{{h1}}", page["h1"]).replace("{{content}}", page["content"])
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created {path}")
