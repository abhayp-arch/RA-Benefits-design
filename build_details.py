import json, os, re

# Read data
with open(r'C:\Users\Itam\.gemini\antigravity\scratch\restaurant-association\img_data.json', 'r') as f:
    imgs = json.load(f)

with open(r'C:\Users\Itam\.gemini\antigravity\scratch\restaurant-association\build_html.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract shared parts
head_css = re.search(r'(<!DOCTYPE html>.*?</style>\n</head>\n<body>)', text, re.DOTALL).group(1)
navbar = re.search(r'(<!-- NAVBAR -->.*?</nav>)', text, re.DOTALL).group(1)
cta_footer = re.search(r'(<!-- CTA BANNER: floats over the footer -->.*?</footer>)', text, re.DOTALL).group(1)
member_widget_clean = re.search(r'(<div class="member-card-widget".*?Upgrade To Gold</a>\n      </div>)', text, re.DOTALL).group(1)

DETAILS_CSS = """
<style>
/* DETAILS PAGE SPECIFIC CSS */
.details-wrapper { background: linear-gradient(131deg, rgba(255,185,162,0.18) 0%, rgba(48,74,219,0.10) 100%); min-height: 100vh; padding-top: 40px; padding-bottom: 80px; }
.details-layout { max-width: 1280px; margin: 0 auto; padding: 0 40px; display: flex; gap: 60px; }
.details-main { flex: 1; max-width: 800px; border-right: 1px solid rgba(0,0,0,0.08); padding-right: 60px; }
.details-sidebar { width: 340px; flex-shrink: 0; position: sticky; top: 100px; height: max-content; }

/* Left Content */
.details-title { font-size: 38px; font-weight: 800; color: #181D2D; margin-bottom: 24px; line-height: 1.2; }
.details-subtitle { font-size: 16px; color: #555; line-height: 1.6; margin-bottom: 32px; }
.details-hero-img { width: 100%; height: auto; max-height: 380px; border-radius: 16px; margin-bottom: 24px; object-fit: cover; box-shadow: 0 4px 20px rgba(0,0,0,0.08); }
.details-tags { display: flex; align-items: center; gap: 12px; margin-bottom: 60px; }

.benefit-alert { background: rgba(239,92,42,0.06); border: 1px solid rgba(239,92,42,0.2); border-radius: 8px; padding: 20px 24px; margin-bottom: 40px; }
.benefit-alert p { font-weight: 700; color: #181D2D; font-size: 15px; margin: 0; line-height: 1.5; }

.content-section h2 { font-size: 24px; font-weight: 800; color: #181D2D; margin-bottom: 20px; margin-top: 36px; }
.content-section h2:first-child { margin-top: 0; }
.bullet-list { list-style: none; margin-bottom: 32px; padding: 0; }
.bullet-list li { position: relative; padding-left: 20px; font-size: 15px; color: #333; line-height: 1.6; margin-bottom: 14px; }
.bullet-list li::before { content: ''; position: absolute; left: 0; top: 9px; width: 6px; height: 6px; background: #EF5C2A; border-radius: 50%; }
.bullet-list li strong { color: #181D2D; }

.number-list { list-style: none; margin-bottom: 40px; padding: 0; counter-reset: item; }
.number-list li { counter-increment: item; position: relative; padding-left: 28px; font-size: 15px; color: #333; line-height: 1.6; margin-bottom: 14px; }
.number-list li::before { content: counter(item); position: absolute; left: 0; top: 0; font-weight: 700; color: #EF5C2A; background: rgba(239,92,42,0.10); width: 20px; height: 20px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 11px; line-height: 20px; text-align: center; }

.sub-bullet-list { list-style: none; padding-left: 20px; margin-top: 6px; }
.sub-bullet-list li { position: relative; padding-left: 16px; font-size: 14px; color: #555; line-height: 1.6; margin-bottom: 8px; }
.sub-bullet-list li::before { content: '\\2013'; position: absolute; left: 0; top: 0; background: transparent; width: auto; height: auto; color: #aaa; font-weight: normal; }

/* Template blocks */
.template-block { background: #F8F9FB; border: 1px solid #E8EAF0; border-radius: 12px; padding: 20px 24px; margin-bottom: 20px; }
.template-block h4 { font-size: 13px; font-weight: 700; color: #EF5C2A; text-transform: uppercase; letter-spacing: 0.04em; margin-bottom: 10px; }
.template-block p { font-size: 14px; color: #444; line-height: 1.65; margin: 0; font-style: italic; }

/* Quick wins row */
.quick-wins { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 40px; }
.quick-win-item { background: #FFF; border: 1px solid #EBEBEB; border-radius: 12px; padding: 16px 18px; display: flex; align-items: flex-start; gap: 12px; }
.quick-win-icon { width: 32px; height: 32px; background: rgba(239,92,42,0.10); border-radius: 8px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.quick-win-icon svg { width: 16px; height: 16px; stroke: #EF5C2A; stroke-width: 2; fill: none; }
.quick-win-item p { font-size: 14px; color: #333; line-height: 1.5; margin: 0; }

/* FAQ */
.faq-block { margin-bottom: 40px; }
.faq-item { border-bottom: 1px solid #EBEBEB; padding: 18px 0; }
.faq-item:last-child { border-bottom: none; }
.faq-q { font-size: 15px; font-weight: 700; color: #181D2D; cursor: pointer; display: flex; justify-content: space-between; align-items: center; list-style: none; margin: 0; outline: none; }
.faq-q::-webkit-details-marker { display: none; }
.faq-icon { flex-shrink: 0; width: 24px; height: 24px; background: url('data:image/svg+xml;utf8,<svg viewBox="0 0 24 24" fill="none" stroke="%23181D2D" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><polyline points="6 9 12 15 18 9"></polyline></svg>') no-repeat center; transition: transform 0.3s ease; }
details[open] .faq-icon { transform: rotate(180deg); }
.faq-a { font-size: 14px; color: #555; line-height: 1.6; margin: 12px 0 0 0; padding-right: 32px; }

/* Sections grid */
.sections-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 40px; }
.section-item { background: #FFF; border: 1px solid #EBEBEB; border-radius: 12px; padding: 16px 18px; }
.section-item .num { font-size: 11px; font-weight: 700; color: #EF5C2A; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 6px; }
.section-item .sec-title { font-size: 14px; font-weight: 700; color: #181D2D; margin-bottom: 4px; }
.section-item .sec-desc { font-size: 13px; color: #666; line-height: 1.5; }
.section-item .bullet-list { margin-bottom: 0; margin-top: 8px; }
.section-item .bullet-list li { font-size: 13px; color: #666; margin-bottom: 8px; line-height: 1.5; }
.section-item .bullet-list li:last-child { margin-bottom: 0; }
/* Claim box */
.claim-box { background: linear-gradient(135deg, #FFF9F5 0%, #FFFDFB 100%); border-radius: 20px; border: 1px solid rgba(239,92,42,0.1); display: flex; align-items: center; justify-content: space-between; overflow: hidden; position: relative; box-shadow: 0 10px 40px rgba(239,92,42,0.04); padding: 40px; margin-bottom: 80px; }
.claim-text { max-width: 380px; position: relative; z-index: 2; }
.claim-title { font-size: 32px; font-weight: 800; color: #181D2D; margin-bottom: 12px; }
.claim-title span { color: #EF5C2A; }
.claim-text p { font-size: 14px; color: #555; line-height: 1.5; margin-bottom: 24px; }
.claim-btn { background: #EF5C2A; color: #FFF; font-size: 16px; font-weight: 700; padding: 14px 32px; border-radius: 8px; border: none; cursor: pointer; display: inline-flex; align-items: center; gap: 8px; transition: background 0.2s; }
.claim-btn:hover { background: #D44D22; }
.claim-tip { display: flex; align-items: flex-start; gap: 10px; background: rgba(239,92,42,0.06); border-radius: 8px; padding: 12px 16px; margin-top: 24px; }
.claim-tip p { font-size: 12px; color: #666; line-height: 1.4; margin: 0; }
.claim-img-wrap { position: absolute; right: 0; top: 0; bottom: 0; width: 45%; max-width: 420px; z-index: 1; pointer-events: none; }
.claim-img-wrap img { width: 100%; height: 100%; object-fit: cover; -webkit-mask-image: linear-gradient(to right, transparent, black 25%); mask-image: linear-gradient(to right, transparent, black 25%); }

@media (min-width: 1440px) {
  .details-layout { max-width: 1440px; padding: 0 60px; }
  .details-main { max-width: 900px; }
}
@media (min-width: 1920px) {
  .details-layout { max-width: 1700px; gap: 80px; padding: 0 80px; }
  .details-main { max-width: 1100px; }
}
</style>
"""

CLAIM_BOX = """
      <div class="claim-box">
        <div class="claim-text">
          <h3 class="claim-title">Ready to <span>Claim?</span></h3>
          <p>Claiming takes less than a minute.<br/>We'll confirm eligibility and send next steps.</p>
          <button class="claim-btn">
            <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M9 12l2 2 4-4"/></svg>
            Claim This Benefit &rarr;
          </button>
          <div class="claim-tip">
            <p>&#128161; Vendor-neutral benefit. Fulfilled by a RA-vetted provider after claim approval.</p>
          </div>
        </div>
        <div class="claim-img-wrap">
          <img src="CLAIM_IMG" alt="Benefit visual" />
        </div>
      </div>
"""

def sidebar():
    return """
    <div class="details-sidebar">
      """ + member_widget_clean + """
    </div>"""

# ─────────────────────────────────────────────
# PAGE DEFINITIONS
# ─────────────────────────────────────────────

pages = {}

# ─── 1. JOB POSTINGS ───────────────────────────────────────────
pages['job_postings'] = {
    'filename': 'details_job_postings.html',
    'img_hero': 'IMG_JOB_POSTINGS',
    'img_claim': 'IMG_JOB_POSTINGS',
    'tag_label': 'Free Access',
    'tag_cat': 'Hiring &bull; Monthly Benefit',
    'content': """
      <a href="index.html" style="color:#EF5C2A;font-weight:800;font-size:18px;line-height:1.2;padding-top:8px;margin-bottom:8px;display:block;text-decoration:none;">Benefits</a>
      <h1 class="details-title">Complimentary Access to Two(2) Job Postings Every Month</h1>
      <p class="details-subtitle">Post up to two jobs each month at no cost and reach candidates actively looking for restaurant work.</p>

      <img src="IMG_JOB_POSTINGS" alt="Restaurant hiring" class="details-hero-img" />

      <div class="details-tags">
        <span class="tag-free" style="padding:6px 14px;font-size:13px;">Free Access</span>
        <span class="tag-cat" style="font-size:15px;">Hiring &bull; Monthly Benefit</span>
      </div>

      <div class="benefit-alert">
        <p>Restaurant Association Benefit &mdash; Vendor-Neutral. Fulfilled By A RA Vetted Provider When Needed.</p>
      </div>

      <div class="content-section">
        <h2>What You Get</h2>
        <ul class="bullet-list">
          <li><strong>2 free job postings every month</strong> (renews monthly)</li>
          <li>Listings visible to candidates browsing restaurant roles</li>
          <li>A simple posting flow: role, pay range, location, schedule, requirements</li>
          <li>Ability to edit postings (hours, pay, description) after publishing</li>
        </ul>

        <h2>Best For</h2>
        <ul class="bullet-list">
          <li>Operators hiring for hourly roles (line cook, cashier, server, dishwasher)</li>
          <li>Restaurants with frequent turnover or seasonal staffing needs</li>
          <li>Multi-location teams that need consistent hiring visibility</li>
        </ul>

        <h2>How It Works</h2>
        <ol class="number-list">
          <li>Sign in to your Restaurant Association account</li>
          <li>Go to Jobs &rarr; Post a Job</li>
          <li>Choose &ldquo;Use monthly free credits&rdquo; (2 credits available each month)</li>
          <li>Publish and start receiving applications</li>
        </ol>

        <h2>Tips to Get More Applicants</h2>
        <ul class="bullet-list">
          <li><strong>Include pay range</strong> (even a band) &mdash; increases apply rate</li>
          <li><strong>Add schedule clarity</strong> (days/hours, weekend needs, shift length)</li>
          <li>Use a short &ldquo;why work here&rdquo; section (meal perks, growth, stable hours, tips)</li>
          <li>Keep requirements realistic and concise</li>
        </ul>

        <h2>FAQs</h2>
        <div class="faq-block">
          <details class="faq-item" open>
            <summary class="faq-q">Do unused job credits roll over?<span class="faq-icon"></span></summary>
            <p class="faq-a">Typically credits reset monthly (recommended: use them each month).</p>
          </details>
          <details class="faq-item">
            <summary class="faq-q">Can I post two jobs at once?<span class="faq-icon"></span></summary>
            <p class="faq-a">Yes, use both monthly credits anytime during the month.</p>
          </details>
          <details class="faq-item">
            <summary class="faq-q">Can I edit a job after posting?<span class="faq-icon"></span></summary>
            <p class="faq-a">Yes, update pay, schedule, and description as needed.</p>
          </details>
          <details class="faq-item">
            <summary class="faq-q">What if I need more than two postings?<span class="faq-icon"></span></summary>
            <p class="faq-a">You can add paid postings (optional) after the free monthly credits are used.</p>
          </details>
        </div>
      </div>
"""
}

# ─── 2. FREE WEBSITE ───────────────────────────────────────────
pages['free_website'] = {
    'filename': 'details_free_website.html',
    'img_hero': 'IMG_LAPTOP',
    'img_claim': 'IMG_LAPTOP',
    'tag_label': 'Free Templates',
    'tag_cat': 'Reputation &bull; Reviews',
    'content': """
      <a href="index.html" style="color:#EF5C2A;font-weight:800;font-size:18px;line-height:1.2;padding-top:8px;margin-bottom:8px;display:block;text-decoration:none;">Benefits</a>
      <h1 class="details-title">Free Website With Restaurant Templates</h1>
      <p class="details-subtitle">Launch a clean, modern restaurant website using proven templates designed to convert visitors into calls, directions, reservations, and online orders.</p>

      <img src="IMG_LAPTOP" alt="Restaurant website on laptop" class="details-hero-img" />

      <div class="details-tags">
        <span class="tag-free" style="padding:6px 14px;font-size:13px;">Free Templates</span>
        <span class="tag-cat" style="font-size:15px;">Reputation &bull; Reviews</span>
      </div>

      <div class="benefit-alert">
        <p>Restaurant Association Benefit &mdash; Vendor-Neutral. Fulfilled By A RA Vetted Provider When Needed.</p>
      </div>

      <div class="content-section">
        <h2>What You Get</h2>
        <ul class="bullet-list">
          <li>A set of restaurant-ready website templates (layout + copy structure)</li>
          <li><strong>Core pages included:</strong>
            <ul class="sub-bullet-list">
              <li>Home</li>
              <li>Menu (or &ldquo;Order&rdquo; page)</li>
              <li>Location / Hours</li>
              <li>About (optional but recommended)</li>
              <li>Contact</li>
            </ul>
          </li>
          <li><strong>Conversion sections already built in:</strong>
            <ul class="sub-bullet-list">
              <li>&ldquo;Call Now&rdquo; + &ldquo;Get Directions&rdquo;</li>
              <li>Reservations / Waitlist link</li>
              <li>Online ordering link</li>
              <li>Catering inquiry CTA (optional)</li>
            </ul>
          </li>
          <li>Mobile-first layout guidance (so it looks great on phones)</li>
          <li>Basic SEO essentials checklist (titles, headings, local keywords, speed basics)</li>
        </ul>

        <h2>Best For</h2>
        <ul class="bullet-list">
          <li>Restaurants that don&rsquo;t have a website yet</li>
          <li>Operators whose current site is outdated or slow</li>
          <li>Restaurants relying too heavily on third-party marketplaces for visibility</li>
        </ul>

        <h2>Template Structure (What Pages Include)</h2>
        <div class="sections-grid">
          <div class="section-item">
            <div class="num">Page 1</div>
            <div class="sec-title">Home Page</div>
            <ul class="bullet-list">
              <li>Hero: headline + 2 primary CTAs (Directions / Order / Call)</li>
              <li>&ldquo;Top sellers&rdquo; / signature items section</li>
              <li>Social proof: review snippets or &ldquo;Featured in&rdquo; (optional)</li>
              <li>Hours + location map block</li>
              <li>Catering or events CTA (optional)</li>
              <li>Footer with contact, socials, and links</li>
            </ul>
          </div>
          <div class="section-item">
            <div class="num">Page 2</div>
            <div class="sec-title">Menu Page</div>
            <ul class="bullet-list">
              <li>Categories + short descriptions (easy scanning)</li>
              <li>Pricing layout guidance (readable, clean)</li>
              <li>&ldquo;Order online&rdquo; and &ldquo;Call to order&rdquo; buttons</li>
            </ul>
          </div>
          <div class="section-item">
            <div class="num">Page 3</div>
            <div class="sec-title">Location / Hours</div>
            <ul class="bullet-list">
              <li>Map embed + parking tips (optional)</li>
              <li>Hours (including holiday messaging)</li>
              <li>Neighborhood keywords (helps &ldquo;near me&rdquo; searches)</li>
            </ul>
          </div>
          <div class="section-item">
            <div class="num">Page 4</div>
            <div class="sec-title">Contact Page</div>
            <ul class="bullet-list">
              <li>Tap-to-call phone</li>
              <li>Contact form (optional)</li>
              <li>Email + social links</li>
              <li>Private events/catering inquiry section (optional)</li>
            </ul>
          </div>
        </div>

        <h2>Example Copy You Can Use</h2>
        <div class="template-block">
          <h4>Homepage Headlines</h4>
          <ul class="bullet-list" style="margin-bottom:0;">
            <li>&ldquo;Your neighborhood spot for [Cuisine] in [City].&rdquo;</li>
            <li>&ldquo;Fresh, fast, and made to order &mdash; right here in [Neighborhood].&rdquo;</li>
            <li>&ldquo;Comfort food done right. Dine in, take out, or order online.&rdquo;</li>
          </ul>
        </div>
        <div class="template-block">
          <h4>CTA Labels</h4>
          <ul class="bullet-list" style="margin-bottom:0;">
            <li>&ldquo;Get Directions&rdquo;</li>
            <li>&ldquo;Order Online&rdquo;</li>
            <li>&ldquo;Call Now&rdquo;</li>
            <li>&ldquo;View Menu&rdquo;</li>
            <li>&ldquo;Request Catering Quote&rdquo;</li>
          </ul>
        </div>

        <h2>How It Works</h2>
        <ol class="number-list">
          <li>Claim the benefit</li>
          <li>Choose a template style (simple, modern, bold, etc.)</li>
          <li>Plug in your details (logo, menu, hours, photos, links)</li>
          <li>Publish and update anytime</li>
        </ol>

        <h2>What to Prepare Before Launch</h2>
        <ul class="bullet-list">
          <li>Logo (or restaurant name text)</li>
          <li>6&ndash;12 photos (food + interior + team)</li>
          <li>Menu PDF or menu list</li>
          <li>Hours, address, phone</li>
          <li>Links: reservations, ordering, catering (if applicable)</li>
        </ul>

        <h2>FAQs</h2>
        <div class="faq-block">
          <details class="faq-item" open>
            <summary class="faq-q">Is this a full custom website build?<span class="faq-icon"></span></summary>
            <p class="faq-a">This benefit provides a high-quality template structure you can launch quickly. Optional upgrades can be offered later but are not required.</p>
          </details>
          <details class="faq-item">
            <summary class="faq-q">Can I use my own domain?<span class="faq-icon"></span></summary>
            <p class="faq-a">Yes, most restaurants can connect their domain to the site.</p>
          </details>
          <details class="faq-item">
            <summary class="faq-q">Will this help with local search?<span class="faq-icon"></span></summary>
            <p class="faq-a">Yes, the templates include SEO basics and local-friendly structure, but results depend on consistency and content (photos, updates, reviews).</p>
          </details>
          <details class="faq-item">
            <summary class="faq-q">How long does it take to launch?<span class="faq-icon"></span></summary>
            <p class="faq-a">Most restaurants can launch a first version in 1&ndash;2 hours once content is ready.</p>
          </details>
        </div>
      </div>
"""
}

# ─── 3. FACEBOOK MASTERCLASS ───────────────────────────────────
pages['facebook_masterclass'] = {
    'filename': 'details_facebook.html',
    'img_hero': 'IMG_WAITER',
    'img_claim': 'IMG_WAITER',
    'tag_label': 'Master Class',
    'tag_cat': 'Free &bull; Reputation',
    'content': """
      <a href="index.html" style="color:#EF5C2A;font-weight:800;font-size:18px;line-height:1.2;padding-top:8px;margin-bottom:8px;display:block;text-decoration:none;">Benefits</a>
      <h1 class="details-title">Facebook Restaurant Marketing Master Class</h1>
      <p class="details-subtitle">A step-by-step masterclass built for restaurant operators to run Facebook marketing that drives reservations, orders, and repeat visits &mdash; without wasting money.</p>

      <img src="IMG_WAITER" alt="Facebook Marketing" class="details-hero-img" />

      <div class="details-tags">
        <span class="tag-free" style="padding:6px 14px;font-size:13px;">Master Class</span>
        <span class="tag-cat" style="font-size:15px;">Free &bull; Reputation</span>
      </div>

      <div class="benefit-alert">
        <p>Restaurant Association Benefit &mdash; Vendor-Neutral. Fulfilled By A RA Vetted Provider When Needed.</p>
      </div>

      <div class="content-section">
        <h2>What You&rsquo;ll Learn</h2>
        <ul class="bullet-list">
          <li>How to set up a high-converting Facebook Page (profile, CTA button, hours, menu links)</li>
          <li>The 3 ad types restaurants should focus on (and when to use each)</li>
          <li>Local targeting that actually works (radius, zip codes, neighborhoods, time-of-day)</li>
          <li>How to promote slow nights, new menu items, and catering</li>
          <li>Simple &ldquo;weekly playbook&rdquo; to stay consistent without a full-time marketer</li>
        </ul>

        <h2>What You Get</h2>
        <ul class="bullet-list">
          <li>Video lessons (bite-sized)</li>
          <li><strong>Downloadable templates:</strong>
            <ul class="sub-bullet-list">
              <li>Promo calendar (30 days)</li>
              <li>Ad copy + creative prompts</li>
              <li>Offer scripts (BOGO, &ldquo;Tonight Only&rdquo;, family bundles)</li>
            </ul>
          </li>
          <li>Budget guide: &ldquo;$10&ndash;$30/day playbook&rdquo; for local restaurants</li>
        </ul>

        <h2>Best For</h2>
        <ul class="bullet-list">
          <li>Restaurants with slow nights</li>
          <li>New openings and re-openings</li>
          <li>Operators who want more direct orders / reservations</li>
        </ul>

        <h2>How It Works</h2>
        <ol class="number-list">
          <li>Claim the masterclass</li>
          <li>Access is unlocked for members (or emailed)</li>
          <li>Follow the weekly playbook and track results</li>
        </ol>
      </div>
"""
}

# ─── 4. INSTAGRAM MASTERCLASS ──────────────────────────────────
pages['instagram_masterclass'] = {
    'filename': 'details_instagram.html',
    'img_hero': 'IMG_CHALKBOARD',
    'img_claim': 'IMG_CHALKBOARD',
    'tag_label': 'Master Class',
    'tag_cat': 'Free &bull; Reputation',
    'content': """
      <a href="index.html" style="color:#EF5C2A;font-weight:800;font-size:18px;line-height:1.2;padding-top:8px;margin-bottom:8px;display:block;text-decoration:none;">Benefits</a>
      <h1 class="details-title">Instagram Restaurant Marketing Master Class</h1>
      <p class="details-subtitle">A practical Instagram masterclass built for restaurants &mdash; how to create content that gets discovered locally, drives visits, and turns followers into customers.</p>

      <img src="IMG_CHALKBOARD" alt="Instagram Marketing" class="details-hero-img" />

      <div class="details-tags">
        <span class="tag-free" style="padding:6px 14px;font-size:13px;">Master Class</span>
        <span class="tag-cat" style="font-size:15px;">Free &bull; Reputation</span>
      </div>

      <div class="benefit-alert">
        <p>Restaurant Association Benefit &mdash; Vendor-Neutral. Fulfilled By A RA Vetted Provider When Needed.</p>
      </div>

      <div class="content-section">
        <h2>What You&rsquo;ll Learn</h2>
        <ul class="bullet-list">
          <li>Reels strategy for restaurants (what to film, how long, and what hooks work)</li>
          <li>Local discovery: how to show up on Explore + &ldquo;near me&rdquo; behavior</li>
          <li>Captions + hashtags that match cuisine + city (without keyword stuffing)</li>
          <li>Content pillars: food, people, process, promos, and community</li>
          <li>The &ldquo;3 posts + 5 stories per week&rdquo; plan operators can actually maintain</li>
        </ul>

        <h2>What You Get</h2>
        <ul class="bullet-list">
          <li>Reel scripts + shot lists (so staff can film quickly)</li>
          <li>Caption templates (grand opening, LTO, lunch special, slow night)</li>
          <li>Hashtag packs by cuisine + city format</li>
          <li>Weekly content calendar template</li>
        </ul>

        <h2>Best For</h2>
        <ul class="bullet-list">
          <li>Restaurants that want more foot traffic</li>
          <li>Operators trying to grow catering/events</li>
          <li>Brands building community + loyalty</li>
        </ul>

        <h2>How It Works</h2>
        <ol class="number-list">
          <li>Claim the masterclass</li>
          <li>Access is unlocked for members (or emailed)</li>
          <li>Follow the weekly playbook and track results</li>
        </ol>
      </div>
"""
}

# ─── 5. YELP GROWTH ────────────────────────────────────────────
pages['yelp_growth'] = {
    'filename': 'details_yelp.html',
    'img_hero': 'IMG_REELS',
    'img_claim': 'IMG_REELS',
    'tag_label': 'Master Class',
    'tag_cat': 'Free &bull; Reputation',
    'content': """
      <a href="index.html" style="color:#EF5C2A;font-weight:800;font-size:18px;line-height:1.2;padding-top:8px;margin-bottom:8px;display:block;text-decoration:none;">Benefits</a>
      <h1 class="details-title">How to Grow Your Business on Yelp</h1>
      <p class="details-subtitle">A Yelp growth guide for restaurants &mdash; how to increase visibility, improve ranking, and turn views into visits while handling reviews professionally.</p>

      <img src="IMG_REELS" alt="Yelp Growth Guide" class="details-hero-img" />

      <div class="details-tags">
        <span class="tag-free" style="padding:6px 14px;font-size:13px;">Master Class</span>
        <span class="tag-cat" style="font-size:15px;">Free &bull; Reputation</span>
      </div>

      <div class="benefit-alert">
        <p>Restaurant Association Benefit &mdash; Vendor-Neutral. Fulfilled By A RA Vetted Provider When Needed.</p>
      </div>

      <div class="content-section">
        <h2>What You&rsquo;ll Learn</h2>
        <ul class="bullet-list">
          <li>Yelp profile optimization checklist (categories, photos, menu, hours, attributes)</li>
          <li>What impacts ranking locally (relevance + activity + quality signals)</li>
          <li>How to respond to 1-star reviews without making it worse</li>
          <li>Review request system (post-visit text/email + table tents)</li>
          <li>Reputation score tracker across Yelp + Google + TripAdvisor</li>
        </ul>

        <h2>What You Get</h2>
        <ul class="bullet-list">
          <li>Yelp profile setup + optimization checklist (PDF)</li>
          <li>Review response templates (1&ndash;5 stars)</li>
          <li>&ldquo;Review request&rdquo; message templates (SMS + email)</li>
          <li>Weekly checklist: 15 minutes per week to keep Yelp fresh</li>
        </ul>

        <h2>Yelp Growth &ldquo;Quick Wins&rdquo;</h2>
        <div class="quick-wins">
          <div class="quick-win-item">
            <div class="quick-win-icon"><svg viewBox="0 0 24 24"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg></div>
            <p>Respond to every review within 48 hours</p>
          </div>
          <div class="quick-win-item">
            <div class="quick-win-icon"><svg viewBox="0 0 24 24"><path d="M23 19a2 2 0 01-2 2H3a2 2 0 01-2-2V8a2 2 0 012-2h4l2-3h6l2 3h4a2 2 0 012 2z"/><circle cx="12" cy="13" r="4"/></svg></div>
            <p>Add 8&ndash;12 new photos monthly (food + interior + staff)</p>
          </div>
          <div class="quick-win-item">
            <div class="quick-win-icon"><svg viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg></div>
            <p>Update menu items seasonally (don&rsquo;t let it look stale)</p>
          </div>
          <div class="quick-win-item">
            <div class="quick-win-icon"><svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg></div>
            <p>Use &ldquo;From the Business&rdquo; updates weekly (1 photo + 1 sentence)</p>
          </div>
        </div>

        <h2>How It Works</h2>
        <ol class="number-list">
          <li>Claim the Yelp guide</li>
          <li>Get the templates + checklist</li>
          <li>Follow the weekly plan and track progress</li>
        </ol>
      </div>
"""
}

# ─── 6. VENDOR NEGOTIATION ─────────────────────────────────────
pages['vendor_negotiation'] = {
    'filename': 'details_vendor.html',
    'img_hero': 'IMG_NEARME',
    'img_claim': 'IMG_NEARME',
    'tag_label': 'Guides',
    'tag_cat': 'Free &bull; Negotiation',
    'content': """
      <a href="index.html" style="color:#EF5C2A;font-weight:800;font-size:18px;line-height:1.2;padding-top:8px;margin-bottom:8px;display:block;text-decoration:none;">Benefits</a>
      <h1 class="details-title">Get Free Vendor Negotiation Guide</h1>
      <p class="details-subtitle">A practical negotiation guide for restaurant operators &mdash; scripts, checklists, and a simple process to lower costs and improve terms with vendors.</p>

      <img src="IMG_NEARME" alt="Vendor Negotiation Guide" class="details-hero-img" />

      <div class="details-tags">
        <span class="tag-free" style="padding:6px 14px;font-size:13px;">Guides</span>
        <span class="tag-cat" style="font-size:15px;">Free &bull; Negotiation</span>
      </div>

      <div class="benefit-alert">
        <p>Restaurant Association Benefit &mdash; Vendor-Neutral. Fulfilled By A RA Vetted Provider When Needed.</p>
      </div>

      <div class="content-section">
        <h2>What&rsquo;s Inside</h2>
        <ul class="bullet-list">
          <li>Vendor negotiation checklist (before the call)</li>
          <li><strong>Scripts for common vendor categories:</strong>
            <ul class="sub-bullet-list">
              <li>Food distributors</li>
              <li>Cleaning + paper goods</li>
              <li>Equipment maintenance</li>
              <li>Delivery packaging</li>
              <li>Merchant processing</li>
            </ul>
          </li>
          <li>&ldquo;3 leverage points&rdquo; operators forget (volume, timing, competitor quotes)</li>
          <li>Renewal timeline + what to ask for (rebates, free delivery, better payment terms)</li>
        </ul>

        <h2>What You&rsquo;ll Get (Downloadables)</h2>
        <ul class="bullet-list">
          <li>Negotiation call script (one-page)</li>
          <li>Vendor comparison table (price + service + terms)</li>
          <li>Renewal calendar (so you don&rsquo;t renegotiate too late)</li>
          <li><strong>Email templates:</strong>
            <ul class="sub-bullet-list">
              <li>&ldquo;We&rsquo;re reviewing vendors&rdquo;</li>
              <li>&ldquo;Match this quote&rdquo;</li>
              <li>&ldquo;Improve terms or we switch&rdquo;</li>
            </ul>
          </li>
        </ul>

        <h2>How It Works</h2>
        <ol class="number-list">
          <li>Claim the guide</li>
          <li>Download templates + scripts</li>
          <li>Use the renewal calendar to negotiate systematically</li>
        </ol>
      </div>
"""
}

# ─── 7. AI CONTENT ─────────────────────────────────────────────
pages['ai_content'] = {
    'filename': 'details_ai_content.html',
    'img_hero': 'IMG_WOMAN',
    'img_claim': 'IMG_WOMAN',
    'tag_label': 'Free',
    'tag_cat': 'AI &bull; Content Kit',
    'content': """
      <a href="index.html" style="color:#EF5C2A;font-weight:800;font-size:18px;line-height:1.2;padding-top:8px;margin-bottom:8px;display:block;text-decoration:none;">Benefits</a>
      <h1 class="details-title">Create Restaurant Marketing Content FAST with AI</h1>
      <p class="details-subtitle">A practical kit that helps restaurant operators generate high-quality posts, promos, emails, and review responses in minutes &mdash; without sounding generic.</p>

      <img src="IMG_WOMAN" alt="AI Content Creation" class="details-hero-img" />

      <div class="details-tags">
        <span class="tag-free" style="padding:6px 14px;font-size:13px;">Free</span>
        <span class="tag-cat" style="font-size:15px;">AI &bull; Content Kit</span>
      </div>

      <div class="benefit-alert">
        <p>Restaurant Association Benefit &mdash; Vendor-Neutral. Fulfilled By A RA Vetted Provider When Needed.</p>
      </div>

      <div class="content-section">
        <h2>What You Get</h2>
        <ul class="bullet-list">
          <li>A library of copy/paste ChatGPT prompts built for restaurants</li>
          <li><strong>Ready-made templates for:</strong>
            <ul class="sub-bullet-list">
              <li>Facebook posts + ads</li>
              <li>Instagram captions + Reels hooks</li>
              <li>SMS promos for slow nights</li>
              <li>Email campaigns (events, catering, specials)</li>
              <li>Yelp/Google review responses (1&ndash;5 stars)</li>
            </ul>
          </li>
          <li>A simple &ldquo;brand voice setup&rdquo; so outputs sound like your restaurant</li>
        </ul>

        <h2>Best For</h2>
        <ul class="bullet-list">
          <li>Owners/managers who need content fast</li>
          <li>Teams without a dedicated marketer</li>
          <li>Restaurants running weekly specials, catering, or events</li>
        </ul>

        <h2>How It Works</h2>
        <ol class="number-list">
          <li>Pick the content type you need (post, promo, email, ad, review response)</li>
          <li>Paste the prompt and fill in 5 quick details (restaurant name, offer, timing, location, tone)</li>
          <li>Generate 3&ndash;5 variations and choose the best</li>
          <li>Post/send immediately (or save to your library)</li>
        </ol>
      </div>
"""
}

# ─── 8. BUSINESS PLAN ──────────────────────────────────────────
pages['business_plan'] = {
    'filename': 'details_business_plan.html',
    'img_hero': 'IMG_BAR',
    'img_claim': 'IMG_BAR',
    'tag_label': 'Free',
    'tag_cat': 'Business Plan &bull; Content Kit',
    'content': """
      <a href="index.html" style="color:#EF5C2A;font-weight:800;font-size:18px;line-height:1.2;padding-top:8px;margin-bottom:8px;display:block;text-decoration:none;">Benefits</a>
      <h1 class="details-title">How To Easily Write A Restaurant Business Plan</h1>
      <p class="details-subtitle">A simple, step-by-step kit to build a professional restaurant business plan &mdash; clear enough for lenders and structured enough for execution.</p>

      <img src="IMG_BAR" alt="Restaurant Business Plan" class="details-hero-img" />

      <div class="details-tags">
        <span class="tag-free" style="padding:6px 14px;font-size:13px;">Free</span>
        <span class="tag-cat" style="font-size:15px;">Business Plan &bull; Content Kit</span>
      </div>

      <div class="benefit-alert">
        <p>Restaurant Association Benefit &mdash; Vendor-Neutral. Fulfilled By A RA Vetted Provider When Needed.</p>
      </div>

      <div class="content-section">
        <h2>What You Get</h2>
        <ul class="bullet-list">
          <li>A restaurant business plan outline (copy/paste structure)</li>
          <li>Fill-in-the-blank prompts for every section</li>
          <li>Financial planning checklist (what numbers to include)</li>
          <li>Sample language + examples (so it doesn&rsquo;t sound generic)</li>
        </ul>

        <h2>Best For</h2>
        <ul class="bullet-list">
          <li>New restaurant openings or first-time owners</li>
          <li>Existing restaurants seeking funding or expanding</li>
          <li>Operators opening a second location, kiosk, or food truck</li>
        </ul>

        <h2>What&rsquo;s Inside (Sections Included)</h2>
        <div class="sections-grid">
          <div class="section-item">
            <div class="num">Section 1</div>
            <div class="sec-title">Executive Summary</div>
            <div class="sec-desc">1 page, lender-friendly</div>
          </div>
          <div class="section-item">
            <div class="num">Section 2</div>
            <div class="sec-title">Concept &amp; Brand</div>
            <div class="sec-desc">What makes you different</div>
          </div>
          <div class="section-item">
            <div class="num">Section 3</div>
            <div class="sec-title">Market &amp; Location</div>
            <div class="sec-desc">Your customers + competition</div>
          </div>
          <div class="section-item">
            <div class="num">Section 4</div>
            <div class="sec-title">Menu &amp; Pricing Strategy</div>
            <div class="sec-desc">Profit focus</div>
          </div>
          <div class="section-item">
            <div class="num">Section 5</div>
            <div class="sec-title">Operations Plan</div>
            <div class="sec-desc">Hours, staffing, suppliers, systems</div>
          </div>
          <div class="section-item">
            <div class="num">Section 6</div>
            <div class="sec-title">Marketing Plan</div>
            <div class="sec-desc">Launch + ongoing growth</div>
          </div>
          <div class="section-item">
            <div class="num">Section 7</div>
            <div class="sec-title">Financial Plan</div>
            <div class="sec-desc">Sales forecast, costs, break-even</div>
          </div>
          <div class="section-item">
            <div class="num">Section 8</div>
            <div class="sec-title">Milestones &amp; Timeline</div>
            <div class="sec-desc">Opening checklist + dates</div>
          </div>
        </div>

        <h2>Competitive Advantage Examples</h2>
        <div class="template-block">
          <h4>Example Statements</h4>
          <ul class="bullet-list" style="margin-bottom:0;">
            <li>&ldquo;Fast, consistent lunch service in under 20 minutes.&rdquo;</li>
            <li>&ldquo;High-margin menu engineered around a short, repeatable prep line.&rdquo;</li>
            <li>&ldquo;Strong local presence with community partnerships + catering focus.&rdquo;</li>
          </ul>
        </div>

        <h2>How It Works</h2>
        <ol class="number-list">
          <li>Download the kit + outline</li>
          <li>Fill in the prompts (most operators finish the first draft in 1&ndash;2 sessions)</li>
          <li>Use the financial checklist to add credibility</li>
          <li>Export as a PDF and share with partners/lenders/investors</li>
        </ol>

        <h2>FAQs</h2>
        <div class="faq-block">
          <details class="faq-item" open>
            <summary class="faq-q">Do I need complicated financial models?<span class="faq-icon"></span></summary>
            <p class="faq-a">No, this kit focuses on the key numbers lenders care about (forecast, costs, break-even, cash needs).</p>
          </details>
          <details class="faq-item">
            <summary class="faq-q">Can I use this for an existing restaurant?<span class="faq-icon"></span></summary>
            <p class="faq-a">Yes, use it for refinancing, expansion, or operational reset.</p>
          </details>
          <details class="faq-item">
            <summary class="faq-q">Is it okay if I don&rsquo;t know all numbers yet?<span class="faq-icon"></span></summary>
            <p class="faq-a">Yes, you can start with assumptions and refine later.</p>
          </details>
        </div>
      </div>
"""
}

# ─── 9. CHOMP SHOW ─────────────────────────────────────────────
pages['chomp_show'] = {
    'filename': 'details_chomp.html',
    'img_hero': 'IMG_CHOMP',
    'img_claim': 'IMG_CHOMP',
    'tag_label': 'Free',
    'tag_cat': 'Opportunity &bull; Chomp',
    'content': """
      <a href="index.html" style="color:#EF5C2A;font-weight:800;font-size:18px;line-height:1.2;padding-top:8px;margin-bottom:8px;display:block;text-decoration:none;">Benefits</a>
      <h1 class="details-title">Get Featured on The Chomp Show (Free of Cost)</h1>
      <p class="details-subtitle">Share your restaurant&rsquo;s story and signature food on a professionally produced feature, built to drive awareness, community support, and new guests.</p>

      <img src="IMG_CHOMP" alt="Chomp Show Feature" class="details-hero-img" />

      <div class="details-tags">
        <span class="tag-free" style="padding:6px 14px;font-size:13px;">Free</span>
        <span class="tag-cat" style="font-size:15px;">Opportunity &bull; Chomp</span>
      </div>

      <div class="benefit-alert">
        <p>Restaurant Association Benefit &mdash; A Complimentary Member Perk. No cost, no catch.</p>
      </div>

      <div class="content-section">
        <h2>What You Get</h2>
        <ul class="bullet-list">
          <li>A chance to be featured on The Chomp Show <strong>at no cost</strong></li>
          <li>A structured, easy process (so it&rsquo;s not awkward or time-consuming)</li>
          <li><strong>A highlight segment designed to be repurposed:</strong>
            <ul class="sub-bullet-list">
              <li>Full episode (YouTube)</li>
              <li>Short clips for Instagram / TikTok / Facebook</li>
              <li>Still frames for posts and press</li>
            </ul>
          </li>
        </ul>

        <h2>Best For</h2>
        <ul class="bullet-list">
          <li>Restaurants with a great story (family-owned, local favorite, unique concept)</li>
          <li>New openings or re-launches</li>
          <li>Operators who want community visibility and credible exposure</li>
        </ul>

        <h2>What the Feature Typically Includes</h2>
        <ul class="bullet-list">
          <li>Your origin story (why you started, what makes you different)</li>
          <li>Signature dish walkthrough (prep &rarr; plating &rarr; first bite)</li>
          <li>Behind-the-scenes moments (kitchen, team, atmosphere)</li>
          <li>A short &ldquo;operator tip&rdquo; segment (optional)</li>
          <li>Clear mention of your location + how guests can visit/order</li>
        </ul>

        <h2>How It Works</h2>
        <ol class="number-list">
          <li>Apply (2&ndash;3 minutes)</li>
          <li>We review your submission and confirm fit + schedule</li>
          <li>We send a prep checklist (what to have ready, what to expect)</li>
          <li>We film the feature and share clips you can post</li>
        </ol>

        <h2>What We Need From You (Simple)</h2>
        <ul class="bullet-list">
          <li>Your best time window for filming</li>
          <li>1&ndash;2 signature dishes you want to highlight</li>
          <li>A team member who can speak on camera (owner/GM/chef)</li>
          <li>Permission to film on-site during the agreed time</li>
        </ul>

        <h2>Example Story Angles That Work Well</h2>
        <div class="template-block">
          <h4>Story Angle Ideas</h4>
          <ul class="bullet-list" style="margin-bottom:0;">
            <li>&ldquo;From family recipe to local favorite&rdquo;</li>
            <li>&ldquo;How we built a loyal community in [City]&rdquo;</li>
            <li>&ldquo;The signature dish everyone orders&rdquo;</li>
            <li>&ldquo;The comeback story: rebuilding after a tough year&rdquo;</li>
          </ul>
        </div>

        <h2>FAQs</h2>
        <div class="faq-block">
          <details class="faq-item" open>
            <summary class="faq-q">Is this really free?<span class="faq-icon"></span></summary>
            <p class="faq-a">Yes, this is a Restaurant Association member benefit.</p>
          </details>
          <details class="faq-item">
            <summary class="faq-q">Do I need professional media experience?<span class="faq-icon"></span></summary>
            <p class="faq-a">No. We guide you through it. The prep checklist makes it easy.</p>
          </details>
          <details class="faq-item">
            <summary class="faq-q">Will I get clips for social media?<span class="faq-icon"></span></summary>
            <p class="faq-a">Yes, short clips are designed for Reels/TikTok/Shorts.</p>
          </details>
          <details class="faq-item">
            <summary class="faq-q">How do you choose restaurants?<span class="faq-icon"></span></summary>
            <p class="faq-a">We prioritize strong stories, signature food, and variety across cuisines and cities.</p>
          </details>
        </div>
      </div>
"""
}

# ─── 10. GOOGLE REVIEWS TEMPLATES ──────────────────────────────
pages['google_reviews'] = {
    'filename': 'details_google_reviews.html',
    'img_hero': 'IMG_GOOGLE_REVIEWS',
    'img_claim': 'IMG_GOOGLE_REVIEWS',
    'tag_label': 'Free',
    'tag_cat': 'Templates &bull; Scripts',
    'content': """
      <a href="index.html" style="color:#EF5C2A;font-weight:800;font-size:18px;line-height:1.2;padding-top:8px;margin-bottom:8px;display:block;text-decoration:none;">Benefits</a>
      <h1 class="details-title">Google Reviews Response Templates (Including 1-Star Responses)</h1>
      <p class="details-subtitle">Professional, ready-to-use responses for 1&ndash;5 star reviews. Protect your reputation, stay consistent, and respond faster without sounding defensive.</p>

      <img src="IMG_GOOGLE_REVIEWS" alt="Google Reviews Templates" class="details-hero-img" />

      <div class="details-tags">
        <span class="tag-free" style="padding:6px 14px;font-size:13px;">Free</span>
        <span class="tag-cat" style="font-size:15px;">Templates &bull; Scripts</span>
      </div>

      <div class="benefit-alert">
        <p>Restaurant Association Benefit &mdash; Vendor-Neutral. Fulfilled By A RA Vetted Provider When Needed.</p>
      </div>

      <div class="content-section">
        <h2>What You Get</h2>
        <ul class="bullet-list">
          <li><strong>Copy/paste templates for:</strong>
            <ul class="sub-bullet-list">
              <li>1-star (calm, professional, de-escalation)</li>
              <li>2&ndash;3 star (acknowledge + improve)</li>
              <li>4&ndash;5 star (grateful + invite back)</li>
            </ul>
          </li>
          <li>&ldquo;Do/Don&rsquo;t&rdquo; checklist for handling negative reviews</li>
          <li>Quick internal process: who responds, when, and how to follow up</li>
        </ul>

        <h2>Best For</h2>
        <ul class="bullet-list">
          <li>Restaurants getting inconsistent reviews</li>
          <li>Operators who want to protect brand perception</li>
          <li>Multi-location teams that need consistent voice</li>
        </ul>

        <h2>1-Star Review Response Templates</h2>
        <div class="template-block">
          <h4>Template A &mdash; Calm + Take Offline</h4>
          <p>&ldquo;Hi [Name], thank you for the feedback. I&rsquo;m sorry your experience didn&rsquo;t meet expectations &mdash; this isn&rsquo;t the standard we aim for. If you&rsquo;re willing, please contact me at [email/phone] with the date/time of your visit so I can look into what happened and make it right. &mdash; [Manager Name], [Title]&rdquo;</p>
        </div>
        <div class="template-block">
          <h4>Template B &mdash; Service Delay / Wait Time</h4>
          <p>&ldquo;Hi [Name], I&rsquo;m sorry about the wait and the experience you had. We&rsquo;re addressing timing and staffing so this doesn&rsquo;t happen again. If you can share the date/time of your visit at [email/phone], I&rsquo;d like to review it with the team and make it right. &mdash; [Manager Name]&rdquo;</p>
        </div>
        <div class="template-block">
          <h4>Template C &mdash; Wrong Order / Missing Items</h4>
          <p>&ldquo;Hi [Name], I&rsquo;m sorry we missed the mark and your order wasn&rsquo;t correct. That&rsquo;s frustrating, and we take it seriously. Please reach us at [email/phone] with your visit details so we can fix this and improve our process. &mdash; [Manager Name]&rdquo;</p>
        </div>
        <div class="template-block">
          <h4>Template D &mdash; Quality Issue (Food Not Fresh / Cold)</h4>
          <p>&ldquo;Hi [Name], thank you for letting us know. I&rsquo;m sorry the food quality wasn&rsquo;t what it should have been. If you can contact us at [email/phone] with the date/time, I&rsquo;d like to look into it and make it right. &mdash; [Manager Name]&rdquo;</p>
        </div>
        <div class="template-block">
          <h4>Template E &mdash; Suspected Fake/Unfair Review (Careful + Professional)</h4>
          <p>&ldquo;Hi [Name], we take feedback seriously and want to look into this. We&rsquo;re not able to locate this experience based on the details provided. Please contact us at [email/phone] with the date/time of your visit so we can investigate and address it. &mdash; [Manager Name]&rdquo;</p>
        </div>

        <h2>5-Star Response Templates</h2>
        <div class="template-block">
          <h4>Template A &mdash; Short + Warm</h4>
          <p>&ldquo;Thank you, [Name]! We really appreciate you taking the time to share this. Hope to see you again soon!&rdquo;</p>
        </div>
        <div class="template-block">
          <h4>Template B &mdash; Mention Signature Item</h4>
          <p>&ldquo;Thanks so much, [Name]! We&rsquo;re glad you enjoyed the [menu item]. Can&rsquo;t wait to have you back.&rdquo;</p>
        </div>

        <h2>Simple Rules for Responding</h2>
        <ul class="bullet-list">
          <li>Respond within 24&ndash;48 hours</li>
          <li>Don&rsquo;t argue or blame the guest publicly</li>
          <li>Apologize once, then move to resolution offline</li>
          <li>Sign with a real name/title to build trust</li>
          <li>If it&rsquo;s a serious issue, invite a direct conversation</li>
        </ul>

        <h2>How It Works</h2>
        <ol class="number-list">
          <li>Claim the benefit</li>
          <li>Download templates + checklist</li>
          <li>Share internally so your team responds consistently</li>
        </ol>
      </div>
"""
}

# ─────────────────────────────────────────────
# BUILD ALL PAGES
# ─────────────────────────────────────────────

for key, page in pages.items():
    content_body = f"""
<div class="details-wrapper">
  <div class="details-layout">
    <div class="details-main">
{page['content']}
{CLAIM_BOX.replace('CLAIM_IMG', page['img_claim'])}
    </div>
{sidebar()}
  </div>
</div>
"""

    full_html = (head_css + DETAILS_CSS + navbar + content_body + '\n<div style="height: 80px;"></div>\n' + cta_footer +
                 "\n</body>\n</html>")

    # Replace all image keys
    for img_key, img_val in imgs.items():
        token = img_key.upper()   # e.g. img_waiter -> IMG_WAITER
        full_html = full_html.replace(token, img_val)

    out_path = rf'C:\Users\Itam\.gemini\antigravity\scratch\restaurant-association\{page["filename"]}'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
    size = os.path.getsize(out_path)
    print(f"Written: {page['filename']} ({size/1024/1024:.2f} MB)")

print("\nAll detail pages generated successfully!")
