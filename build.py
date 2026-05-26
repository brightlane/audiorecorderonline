from pathlib import Path
from textwrap import dedent
from datetime import date, timedelta
import shutil
import html as html_lib
from xml.sax.saxutils import escape as xml_escape

BASE_URL = "https://brightlane.github.io/1password"
OUT = Path("dist")
SITE = Path("site")
POSTS = SITE / "blog"
ASSETS = Path("assets")
TODAY = str(date.today())
AFFILIATE_URL = "https://1password.partnerlinks.io/px79kbeq78s4?utm_source=brightlane&utm_medium=affiliate&utm_campaign=1password"

if OUT.exists():
    shutil.rmtree(OUT)
if SITE.exists():
    shutil.rmtree(SITE)

OUT.mkdir(exist_ok=True)
SITE.mkdir(exist_ok=True)
POSTS.mkdir(parents=True, exist_ok=True)

def slugify(s):
    s = s.lower().strip()
    out = []
    last_dash = False
    for ch in s:
        if ch.isalnum():
            out.append(ch)
            last_dash = False
        elif not last_dash:
            out.append("-")
            last_dash = True
    slug = "".join(out).strip("-")
    return slug or "post"

blog_topics = [
    ("1Password Free Trial Guide 2026", "How to start with 1Password, test the free trial, and decide if it fits your workflow."),
    ("1Password vs LastPass in 2026", "A security-focused comparison for users leaving LastPass or choosing a premium manager."),
    ("1Password vs Bitwarden for Teams", "A practical comparison of pricing, usability, and team workflows."),
    ("How 1Password Helps Remote Teams", "Why remote teams use 1Password for secure sharing and access control."),
    ("Why Passkeys Matter in 2026", "How 1Password supports passkeys and why that matters for modern account security."),
    ("1Password for Agencies and Marketers", "A workflow guide for affiliate marketers, SEO teams, and agencies."),
    ("1Password Family Plan Review", "A simple breakdown of whether the family plan is the best value."),
]

for i, (title, desc) in enumerate(blog_topics):
    d = date.today() - timedelta(days=i + 1)
    slug = f"{d.isoformat()}-{slugify(title)}"
    content = dedent(f"""
    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>{html_lib.escape(title)} | 1Password</title>
      <meta name="description" content="{html_lib.escape(desc)}">
      <link rel="canonical" href="{BASE_URL}/blog/{slug}.html">
      <meta name="robots" content="index,follow">
      <link rel="stylesheet" href="../assets/css/style.css">
    </head>
    <body>
      <main class="wrap">
        <p><a href="{BASE_URL}/">← Back to 1Password</a></p>
        <article class="card">
          <h1>{html_lib.escape(title)}</h1>
          <p>{html_lib.escape(desc)}</p>
          <p>Add 800–1500 words here with buyer intent, use cases, internal links, and a CTA.</p>
          <a class="cta" href="{AFFILIATE_URL}" target="_blank" rel="nofollow sponsored noopener">Start Free Trial</a>
        </article>
      </main>
    </body>
    </html>
    """).strip()
    (POSTS / f"{slug}.html").write_text(content, encoding="utf-8")

posts_sorted = sorted(POSTS.glob("*.html"))
post_cards = [
    f'<div class="card"><strong><a href="{BASE_URL}/blog/{p.name}">{html_lib.escape(p.stem.replace("-", " ").title())}</a></strong><p>Support article for 1Password search intent.</p></div>'
    for p in posts_sorted
]

index_html = dedent(f"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>1Password Review 2026 | Secure Password Manager for Teams and Families</title>
  <meta name="description" content="1Password review 2026 for solopreneurs, agencies, and families. Secure vault, Watchtower, passkeys, and fast cross-device access.">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <meta name="theme-color" content="#07111f">
  <link rel="canonical" href="{BASE_URL}/">
  <meta property="og:type" content="website">
  <meta property="og:title" content="1Password Review 2026">
  <meta property="og:description" content="Secure password manager with Watchtower, passkeys, and sharing.">
  <meta property="og:url" content="{BASE_URL}/">
  <link rel="stylesheet" href="assets/css/style.css">
  <script defer src="assets/js/main.js"></script>
  <script type="application/ld+json">
  {{
    "@context":"https://schema.org",
    "@type":"WebPage",
    "name":"1Password Review 2026",
    "url":"{BASE_URL}/",
    "dateModified":"{TODAY}"
  }}
  </script>
</head>
<body>
  <main class="wrap">
    <section class="hero">
      <div class="topbar">
        <div class="brand">
          <img src="assets/img/brand-mark.svg" alt="1Password mark">
          <span>Brightlane / 1Password</span>
        </div>
        <div class="badge">Affiliate landing page</div>
      </div>

      <h1 data-rotate-headline>Stay Secure Without the Hassle</h1>
      <p class="sub" data-rotate-intro>1Password helps individuals, teams, and families manage passwords, passkeys, and secure sharing with less friction.</p>
      <a class="cta" href="{AFFILIATE_URL}" rel="sponsored nofollow" target="_blank">Start Free Trial</a>
      <br><a class="cta2" href="#compare">See how it compares</a>

      <div class="grid">
        <div class="card"><strong>Watchtower</strong><p>Security alerts and password health checks.</p></div>
        <div class="card"><strong>Passkeys</strong><p>Modern login support across devices.</p></div>
        <div class="card"><strong>Sharing</strong><p>Secure access for teams and families.</p></div>
      </div>
    </section>

    <section class="section">
      <h2>Why it works</h2>
      <div class="grid">
        <div class="card"><strong>Security-first</strong><p>Built for people who care about account safety.</p></div>
        <div class="card"><strong>Simple UX</strong><p>Easy to use daily, which helps retention.</p></div>
        <div class="card"><strong>Cross-device</strong><p>Use it wherever you work.</p></div>
      </div>
    </section>

    <section id="compare" class="section">
      <h2>How it compares</h2>
      <table>
        <tr><th>Feature</th><th>1Password</th><th>Generic tool</th></tr>
        <tr><td>Password vault</td><td>Yes</td><td>Maybe</td></tr>
        <tr><td>Passkey support</td><td>Yes</td><td>Limited</td></tr>
        <tr><td>Secure sharing</td><td>Yes</td><td>Weak</td></tr>
        <tr><td>Best for teams</td><td>Yes</td><td>Sometimes</td></tr>
      </table>
    </section>

    <section class="section">
      <h2>Who it fits</h2>
      <ul>
        <li>Affiliate marketers managing lots of logins.</li>
        <li>Agencies with shared client access.</li>
        <li>Remote teams needing secure credential sharing.</li>
        <li>Families who want a simple shared vault.</li>
      </ul>
    </section>

    <section class="section">
      <h2>Daily blog posts</h2>
      <div class="posts">
        {"".join(post_cards)}
      </div>
    </section>

    <section class="faq section">
      <h2>FAQ</h2>
      <details><summary>Who is this for?</summary><p>People who want secure password and passkey management.</p></details>
      <details><summary>Should I keep the page simple?</summary><p>Yes. One page, one goal, one primary CTA.</p></details>
      <details><summary>Can I add more pages?</summary><p>Yes, and that is where SEO scale comes from.</p></details>
    </section>

    <div class="disclosure">Disclosure: This page contains affiliate links. Replace the tracking URL with your approved destination before publishing.</div>

    <footer class="footer">
      <p><a href="{BASE_URL}/">brightlane.github.io/1password</a></p>
    </footer>
  </main>
</body>
</html>
""").strip()

(SITE / "index.html").write_text(index_html, encoding="utf-8")
(SITE / "review.html").write_text(dedent(f"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>1Password Review | Features, Pros, and Trial</title>
  <meta name="description" content="Full 1Password review covering features, use cases, pros, cons, and trial details.">
  <link rel="canonical" href="{BASE_URL}/review.html">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body><main class="wrap"><article class="card"><h1>1Password Review</h1><p>Write a deeper review page here.</p></article></main></body>
</html>
""").strip(), encoding="utf-8")
(SITE / "compare.html").write_text(dedent(f"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>1Password vs Bitwarden | Best Password Manager</title>
  <meta name="description" content="Compare 1Password vs Bitwarden, LastPass, and other password managers.">
  <link rel="canonical" href="{BASE_URL}/compare.html">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body><main class="wrap"><article class="card"><h1>1Password vs Bitwarden</h1><p>Write a comparison page here.</p></article></main></body>
</html>
""").strip(), encoding="utf-8")

(OUT / "index.html").write_text((SITE / "index.html").read_text(encoding="utf-8"), encoding="utf-8")
for extra in ["review.html", "compare.html"]:
    (OUT / extra).write_text((SITE / extra).read_text(encoding="utf-8"), encoding="utf-8")

if ASSETS.exists():
    dst = OUT / "assets"
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(ASSETS, dst)

llms = dedent(f"""
# 1Password
{BASE_URL}

## Pages
- [Home]({BASE_URL}/)
- [Review]({BASE_URL}/review.html)
- [Compare]({BASE_URL}/compare.html)

## Focus
- 1Password free trial
- 1Password review
- 1Password vs Bitwarden
- password manager security

## Notes
- Static affiliate site
- Daily content publishing
- Fast navigation for search engines and AI systems
""").strip()
(OUT / "llms.txt").write_text(llms, encoding="utf-8")

robots = dedent(f"""
User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
""").strip()
(OUT / "robots.txt").write_text(robots, encoding="utf-8")

urls = [f"{BASE_URL}/", f"{BASE_URL}/review.html", f"{BASE_URL}/compare.html", f"{BASE_URL}/llms.txt", f"{BASE_URL}/robots.txt"] + [f"{BASE_URL}/blog/{p.name}" for p in posts_sorted]
sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in urls:
    sitemap.append("  <url>")
    sitemap.append(f"    <loc>{xml_escape(u)}</loc>")
    sitemap.append(f"    <lastmod>{TODAY}</lastmod>")
    sitemap.append("  </url>")
sitemap.append("</urlset>")
(OUT / "sitemap.xml").write_text("\n".join(sitemap), encoding="utf-8")

(OUT / "404.html").write_text(dedent(f"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Page Not Found | 1Password</title>
  <meta name="robots" content="noindex,nofollow">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
  <main class="wrap">
    <section class="card">
      <h1>404</h1>
      <p>This page could not be found.</p>
      <p><a href="{BASE_URL}/">Go back to the homepage</a></p>
    </section>
  </main>
</body>
</html>
""").strip(), encoding="utf-8")

print("built")
