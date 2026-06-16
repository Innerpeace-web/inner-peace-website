import os

# Content definitions for the 8 pages
pages = [
    {
        "filename": "dashboard.html",
        "title": "Welcome back, team",
        "active_nav": "dashboard",
        "content": """
      <div class="app-grid">
        <a href="policies.html" class="app-card">
          <div class="app-card-icon icon-teal">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
          </div>
          <h3>Policies & Procedures</h3>
          <p>Care standards, safety, codes of conduct and compliance documents.</p>
          <span class="app-card-action">View Library</span>
        </a>
        
        <a href="training.html" class="app-card">
          <div class="app-card-icon icon-blue">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>
          </div>
          <h3>Training Materials</h3>
          <p>Modules, guides and refreshers — CPR, First Aid, manual handling and more.</p>
          <span class="app-card-action">Start Learning</span>
        </a>
        
        <a href="documents.html" class="app-card">
          <div class="app-card-icon icon-sage">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>
          </div>
          <h3>Employee Documents</h3>
          <p>Contracts, rosters, payslips and personal records in one secure place.</p>
          <span class="app-card-action">Open Files</span>
        </a>
        
        <a href="forms.html" class="app-card">
          <div class="app-card-icon icon-teal">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
          </div>
          <h3>Forms & Templates</h3>
          <p>Incident reports, care notes, leave requests and reusable templates.</p>
          <span class="app-card-action">Download</span>
        </a>
        
        <a href="announcements.html" class="app-card">
          <div class="app-card-icon icon-blue">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path></svg>
          </div>
          <h3>Staff Announcements</h3>
          <p>Company updates, shift news and important notices for the whole team.</p>
          <span class="app-card-action">Read Latest</span>
        </a>
        
        <a href="resources.html" class="app-card">
          <div class="app-card-icon icon-sage">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg>
          </div>
          <h3>Useful Links</h3>
          <p>Quick access to booking, the DISC profile tool and external resources.</p>
          <span class="app-card-action">Go To Links</span>
        </a>
      </div>
"""
    },
    {
        "filename": "policies.html",
        "title": "Policies & Procedures",
        "active_nav": "policies",
        "content": "<p>Content for Policies & Procedures goes here.</p>"
    },
    {
        "filename": "training.html",
        "title": "Training Materials",
        "active_nav": "training",
        "content": "<p>Content for Training Materials goes here.</p>"
    },
    {
        "filename": "documents.html",
        "title": "Employee Documents",
        "active_nav": "documents",
        "content": "<p>Content for Employee Documents goes here.</p>"
    },
    {
        "filename": "forms.html",
        "title": "Forms & Templates",
        "active_nav": "forms",
        "content": "<p>Content for Forms & Templates goes here.</p>"
    },
    {
        "filename": "announcements.html",
        "title": "Staff Announcements",
        "active_nav": "announcements",
        "content": "<p>Content for Staff Announcements goes here.</p>"
    },
    {
        "filename": "resources.html",
        "title": "Useful Links",
        "active_nav": "resources",
        "content": "<p>Content for Useful Links goes here.</p>"
    },
    {
        "filename": "support.html",
        "title": "Help & Support",
        "active_nav": "support",
        "content": "<p>Content for Help & Support goes here.</p>"
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
<title>{{title}} | Staff Portal</title>
<link rel="icon" href="../assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Hanken+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/css/styles.css">
<link rel="stylesheet" href="../assets/css/staff.css">
</head>
<body class="app-body">
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-XXXXXXX" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

<div class="app-shell">
  
  <aside class="app-sidebar">
    <a href="dashboard.html" class="app-brand">
      <div class="app-brand-icon">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l8 4v6c0 5-3.5 8-8 10-4.5-2-8-5-8-10V6z"/><path d="M9 12l2 2 4-4"/></svg>
      </div>
      Staff Portal
    </a>
    
    <nav>
      <ul class="app-nav">
        <li>
          <a href="dashboard.html" class="{{nav_dashboard}}">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
            Dashboard
          </a>
        </li>
        <li>
          <a href="policies.html" class="{{nav_policies}}">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
            Policies
          </a>
        </li>
        <li>
          <a href="training.html" class="{{nav_training}}">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>
            Training
          </a>
        </li>
        <li>
          <a href="documents.html" class="{{nav_documents}}">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>
            Documents
          </a>
        </li>
        <li>
          <a href="forms.html" class="{{nav_forms}}">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
            Forms
          </a>
        </li>
        <li>
          <a href="announcements.html" class="{{nav_announcements}}">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path></svg>
            Announcements
          </a>
        </li>
      </ul>
    </nav>
    <div style="margin-top: auto;">
      <a href="../index.html" style="color: rgba(255,255,255,0.6); text-decoration: none; font-size: 0.85rem; display: flex; align-items: center; gap: 8px;">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line></svg>
        Sign out
      </a>
    </div>
  </aside>

  <main class="app-workspace">
    <header class="app-header">
      <h1>{{title}}</h1>
      <div class="app-user">
        Carer view
        <div class="app-avatar">A</div>
      </div>
    </header>
    
    {{content}}
    
  </main>

</div>

</body>
</html>
"""

for page in pages:
    path = os.path.join("/Users/devan/Inner Peace/website/staff", page["filename"])
    
    # Generate nav active states
    html = template
    for nav_item in ["dashboard", "policies", "training", "documents", "forms", "announcements", "resources", "support"]:
        class_str = "active" if page["active_nav"] == nav_item else ""
        html = html.replace(f"{{{{nav_{nav_item}}}}}", class_str)
        
    html = html.replace("{{title}}", page["title"]).replace("{{content}}", page["content"])
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created {path}")
