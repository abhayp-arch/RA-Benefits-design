import json, os

# Load base64 encoded images
with open(r'C:\Users\Itam\.gemini\antigravity\scratch\restaurant-association\img_data.json', 'r') as f:
    imgs = json.load(f)

html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Member Benefits | Restaurant Association</title>
  <meta name="description" content="Practical perks for real restaurant operators. Vendor-neutral resources focused on outcomes: more guests, stronger operations, and better margins." />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: "Inter", "Segoe UI", sans-serif; background-color: #F4F5F7; color: #0A0A0A; min-width: 320px; }
    a { text-decoration: none; color: inherit; }

    /* ── NAVBAR ── */
    .navbar { background: #FFFFFF; border-bottom: 1px solid #EBEBEB; height: 64px; display: flex; align-items: center; padding: 0 40px; position: sticky; top: 0; z-index: 100; box-shadow: 0 1px 4px rgba(0,0,0,0.04); }
    .navbar-inner { max-width: 1280px; width: 100%; margin: 0 auto; display: flex; align-items: center; }
    .logo { display: flex; align-items: center; flex-shrink: 0; margin-right: 48px; }
    .logo-img { height: 32px; width: auto; display: block; }
    .nav-links { display: flex; align-items: center; justify-content: center; gap: 32px; list-style: none; flex: 1; }
    .nav-links a { font-size: 14px; font-weight: 500; color: #181D2D; transition: color 0.2s; }
    .nav-links a:hover { color: #EF5C2A; }
    .nav-right { display: flex; align-items: center; gap: 12px; margin-left: 32px; }
    .search-bar { display: flex; align-items: center; gap: 8px; background: #F4F5F7; border: 1px solid #E0E0E0; border-radius: 100px; padding: 8px 16px; min-width: 185px; }
    .search-bar input { border: none; background: transparent; outline: none; font-size: 13px; font-family: inherit; color: #9E9E9E; width: 100%; }
    .profile-btn { width: 36px; height: 36px; background: #EF5C2A; border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; flex-shrink: 0; }

    /* ── HERO ── */
    .hero-wrapper { background: linear-gradient(131deg, rgba(255,185,162,0.18) 0%, rgba(48,74,219,0.10) 100%); }
    .hero-section { max-width: 1280px; margin: 0 auto; padding: 80px 40px 140px; display: flex; align-items: center; justify-content: flex-start; gap: clamp(60px, 10vw, 180px); }
    .hero-left { max-width: 650px; flex-shrink: 0; }
    .member-badge { display: inline-block; border: 1px solid #EF5C2A; border-radius: 100px; padding: 4px 14px; font-size: 12px; font-weight: 500; color: #EF5C2A; margin-bottom: 24px; background: rgba(239,92,42,0.08); }
    .hero-heading { font-size: 52px; font-weight: 800; line-height: 1.12; margin-bottom: 24px; color: #0A0A0A; }
    .hero-heading .highlight { color: #EF5C2A; }
    .hero-subtext { font-size: 16px; font-weight: 400; color: #333; line-height: 1.7; max-width: 420px; }

    /* ── MEMBER CARD WIDGET ── */
    .member-card-widget { background: #FFFFFF; border-radius: 20px; box-shadow: 0 8px 40px rgba(0,0,0,0.10); padding: 32px; min-width: 380px; max-width: 440px; flex-shrink: 0; }
    .member-card-widget h3 { font-size: 18px; font-weight: 700; color: #181D2D; margin-bottom: 4px; }
    .widget-subtitle { font-size: 13px; color: #777; margin-bottom: 20px; }
    .id-card { background: linear-gradient(135deg, #FFB9A2 0%, #F97C50 40%, #EF5C2A 100%); border-radius: 14px; padding: 22px 22px 20px; position: relative; overflow: hidden; margin-bottom: 16px; }
    .id-card::before { content: ""; position: absolute; width: 180px; height: 180px; background: rgba(255,255,255,0.08); border-radius: 50%; top: -60px; right: -40px; }
    .id-card::after { content: ""; position: absolute; width: 120px; height: 120px; background: rgba(255,255,255,0.06); border-radius: 50%; bottom: -40px; left: 20px; }
    .id-card-top { display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 32px; position: relative; z-index: 1; }
    .id-card-name { font-size: 26px; font-weight: 700; color: #FFF; line-height: 1.1; }
    .id-card-members { font-size: 12px; color: rgba(255,255,255,0.82); margin-top: 4px; }
    .active-badge { background: #03DE81; color: #FFF; font-size: 11px; font-weight: 600; padding: 4px 10px; border-radius: 100px; display: flex; align-items: center; gap: 5px; flex-shrink: 0; }
    .active-dot { width: 6px; height: 6px; background: #FFF; border-radius: 50%; display: inline-block; }
    .id-card-bottom { display: flex; align-items: flex-end; justify-content: space-between; position: relative; z-index: 1; }
    .id-field { background: rgba(255,255,255,0.22); border-radius: 8px; padding: 8px 14px; }
    .id-field-label { font-size: 10px; color: rgba(255,255,255,0.75); margin-bottom: 2px; }
    .id-field-value { font-size: 14px; font-weight: 700; color: #FFF; letter-spacing: 0.5px; }
    .id-member-since { text-align: right; }
    .id-member-since .ms-label { font-size: 10px; color: rgba(255,255,255,0.75); margin-bottom: 2px; }
    .id-member-since .ms-value { font-size: 13px; font-weight: 700; color: #FFF; }
    .upgrade-btn { display: block; width: 100%; text-align: center; border: 1.5px solid #EF5C2A; border-radius: 8px; padding: 11px; font-size: 14px; font-weight: 600; color: #EF5C2A; background: #FFF; cursor: pointer; transition: background 0.2s, color 0.2s; }
    .upgrade-btn:hover { background: #EF5C2A; color: #FFF; }

    /* ── RESOURCE CARDS ── */
    .cards-section { max-width: 1400px; margin: -70px auto 0; padding: 0 60px 80px; position: relative; z-index: 10; }
    .cards-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 28px; }

    /* Card: white rounded box, image sits INSIDE on the left */
    .resource-card {
      background: #FFFFFF;
      border-radius: 20px;
      box-shadow: 0 4px 18px rgba(0,0,0,0.07);
      border: 1px solid #EBEBEB;
      display: flex;
      align-items: stretch;
      overflow: hidden;
      transition: box-shadow 0.25s;
    }
    .resource-card:hover { box-shadow: 0 8px 32px rgba(0,0,0,0.12); }

    /* Image wrapper: inner padding creates the inset look */
    .card-img-wrap {
      flex-shrink: 0;
      padding: 16px 0 16px 16px;
      display: flex;
      align-items: stretch;
    }
    .card-img {
      width: 270px;
      min-width: 270px;
      object-fit: cover;
      border-radius: 16px;
      display: block;
      align-self: stretch;
    }

    /* Content side */
    .card-box {
      flex: 1;
      display: flex;
      flex-direction: column;
      padding: 20px 22px 22px 20px;
    }
    .card-content { display: flex; flex-direction: column; }
    .card-tags { display: flex; align-items: center; gap: 8px; margin-bottom: 10px; flex-wrap: wrap; }
    .tag-free { background: rgba(28,117,187,0.10); border: 1px solid rgba(28,117,187,0.20); color: #1C75BB; font-size: 11px; font-weight: 600; padding: 3px 10px; border-radius: 100px; }
    .tag-cat { font-size: 12px; color: #777; font-weight: 400; }
    .card-title { font-size: 18px; font-weight: 700; color: #181D2D; line-height: 1.3; margin-bottom: 8px; }
    .card-desc { font-size: 13px; color: #555; line-height: 1.6; margin-bottom: 24px; }
    .view-btn { display: inline-block; background: #EF5C2A; color: #FFF; font-size: 13px; font-weight: 600; padding: 9px 22px; border-radius: 8px; border: none; cursor: pointer; transition: background 0.2s, transform 0.15s; align-self: flex-start; }
    .view-btn:hover { background: #D44D22; transform: translateY(-1px); }

    /* ── LARGE SCREEN RESPONSIVE ── */
    @media (min-width: 1440px) {
      .navbar { padding: 0 60px; }
      .navbar-inner { max-width: 1440px; }
      .hero-section { max-width: 1440px; padding: 90px 60px 150px; }
      .cards-section { max-width: 1440px; padding: 0 60px 80px; }
      .cards-grid { gap: 32px; }
      .card-img { width: 280px; min-width: 280px; }
      .card-box { padding: 22px 24px 24px 20px; }
      .card-title { font-size: 19px; }
      .cta-banner-wrap { max-width: 1440px; padding: 0 60px; }
      footer { padding: 70px 60px 0; }
      .footer-inner { max-width: 1440px; }
    }
    @media (min-width: 1920px) {
      .navbar-inner { max-width: 1700px; }
      .hero-section { max-width: 1700px; padding: 100px 80px 170px; gap: 240px; }
      .hero-left { max-width: 800px; }
      .hero-heading { font-size: 64px; }
      .member-card-widget { min-width: 440px; max-width: 480px; padding: 40px; }
      .cards-section { max-width: 1700px; padding: 0 80px 100px; }
      .cards-grid { gap: 40px; }
      .card-img { width: 300px; min-width: 300px; }
      .card-box { padding: 24px 26px 26px 22px; }
      .card-title { font-size: 20px; }
      .card-desc { font-size: 14px; }
      .cta-banner-wrap { max-width: 1700px; padding: 0 80px; }
      footer { padding: 80px 80px 0; }
      .footer-inner { max-width: 1700px; }
    }

    /* ── CTA BANNER ── */
    /* CTA banner floats on top of the footer */
    .cta-outer-wrap { position: relative; z-index: 10; }
    .cta-banner-wrap { padding: 0 60px; max-width: 1400px; margin: 0 auto; margin-bottom: -60px; }
    .cta-banner { background: linear-gradient(135deg, #FFFFFF 0%, #F0F2F8 100%); border-radius: 20px; display: flex; align-items: center; justify-content: space-between; padding: 28px 40px; box-shadow: 0 8px 40px rgba(0,0,0,0.12); border: 1px solid rgba(255,255,255,0.8); gap: 24px; }
    .cta-banner-left { display: flex; align-items: center; gap: 20px; }
    .cta-logo-box { width: 72px; height: 72px; background: #FFFFFF; border-radius: 14px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-shadow: 0 4px 16px rgba(0,0,0,0.08); }
    .cta-logo-img { height: 40px; width: 40px; display: block; object-fit: contain; }
    .cta-text h4 { font-size: 22px; font-weight: 800; color: #181D2D; margin-bottom: 6px; }
    .cta-text p { font-size: 16px; color: #555; font-weight: 400; }
    .cta-sign-up-btn { background: #EF5C2A; color: #FFF; font-size: 17px; font-weight: 700; padding: 15px 40px; border-radius: 12px; border: none; cursor: pointer; transition: background 0.2s, transform 0.15s; white-space: nowrap; flex-shrink: 0; }
    .cta-sign-up-btn:hover { background: #D44D22; transform: translateY(-1px); }

    /* ── FOOTER ── */
    footer { background: #181D2D; color: #FFF; padding: 110px 40px 0; margin-top: 0; }
    .footer-inner { max-width: 1280px; margin: 0 auto; }
    .footer-main { display: grid; grid-template-columns: 1.3fr 1fr 1fr 1fr; gap: 40px; padding-bottom: 48px; }
    .footer-logo-row { display: flex; align-items: center; margin-bottom: 12px; }
    .footer-logo-img { height: 44px; width: 44px; display: block; object-fit: contain; }
    .footer-brand h3 { font-size: 24px; font-weight: 800; color: #FFF; margin-bottom: 12px; letter-spacing: -0.3px; }
    .footer-brand p { font-size: 13px; color: #9EA5B4; line-height: 1.7; margin-bottom: 24px; max-width: 260px; }
    .footer-signup-btn { background: #EF5C2A; color: #FFF; font-size: 13px; font-weight: 600; padding: 10px 22px; border-radius: 8px; border: none; cursor: pointer; transition: background 0.2s; }
    .footer-signup-btn:hover { background: #D44D22; }
    .footer-col h4 { font-size: 14px; font-weight: 700; color: #FFF; margin-bottom: 20px; }
    .footer-col ul { list-style: none; }
    .footer-col ul li { margin-bottom: 12px; }
    .footer-col ul li a { font-size: 13px; color: #9EA5B4; transition: color 0.2s; }
    .footer-col ul li a:hover { color: #FFF; }
    .footer-connect { padding-bottom: 40px; }
    .footer-connect h4 { font-size: 16px; font-weight: 700; color: #FFF; margin-bottom: 16px; }
    .social-icons { display: flex; align-items: center; gap: 14px; }
    .social-icon { width: 36px; height: 36px; background: rgba(255,255,255,0.10); border-radius: 8px; display: flex; align-items: center; justify-content: center; transition: background 0.2s; cursor: pointer; }
    .social-icon:hover { background: rgba(255,255,255,0.20); }
    .social-icon svg { width: 18px; height: 18px; fill: #FFF; }
    .footer-bottom { border-top: 1px solid rgba(255,255,255,0.10); padding: 20px 0; display: flex; flex-direction: column; align-items: center; gap: 10px; }
    .footer-legal { display: flex; align-items: center; gap: 24px; flex-wrap: wrap; justify-content: center; }
    .footer-legal a { font-size: 12px; color: #9EA5B4; transition: color 0.2s; }
    .footer-legal a:hover { color: #FFF; }
    .footer-copyright { font-size: 12px; color: #9EA5B4; }
  </style>
</head>
<body>

  <!-- NAVBAR -->
  <nav class="navbar" id="navbar">
    <div class="navbar-inner">
      <a href="index.html" class="logo" id="logo-link">
        <img src="IMG_LOGO" alt="Restaurant Association" class="logo-img" />
      </a>
      <ul class="nav-links" id="nav-links">
        <li><a href="#" id="nav-news">News</a></li>
        <li><a href="#" id="nav-topics">Topics</a></li>
        <li><a href="#" id="nav-shows">Shows</a></li>
        <li><a href="#" id="nav-academy">Academy</a></li>
        <li><a href="#" id="nav-events">Events</a></li>
        <li><a href="#" id="nav-jobs">Jobs</a></li>
        <li><a href="#" id="nav-resources">Resources</a></li>
      </ul>
      <div class="nav-right">
        <div class="search-bar" id="search-bar">
          <svg width="15" height="15" viewBox="0 0 15 15" fill="none">
            <circle cx="6.5" cy="6.5" r="5" stroke="#9E9E9E" stroke-width="1.5"/>
            <path d="M10.5 10.5L13.5 13.5" stroke="#9E9E9E" stroke-width="1.5" stroke-linecap="round"/>
          </svg>
          <input type="text" placeholder="Search insights..." id="search-input" />
        </div>
        <div class="profile-btn" id="profile-btn">
          <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
            <circle cx="9" cy="6" r="3.5" stroke="#FFFFFF" stroke-width="1.5"/>
            <path d="M2 16c0-3.314 3.134-6 7-6s7 2.686 7 6" stroke="#FFFFFF" stroke-width="1.5" stroke-linecap="round"/>
          </svg>
        </div>
      </div>
    </div>
  </nav>

  <!-- HERO SECTION -->
  <div class="hero-wrapper">
    <section class="hero-section" id="hero">
      <div class="hero-left">
        <span class="member-badge">Member benefits</span>
        <h1 class="hero-heading">
          <span class="highlight">Practical Perks</span> For Real Operators.
        </h1>
        <p class="hero-subtext">
          Everything Here Is Vendor-Neutral And Focused On Outcomes: More
          Guests, Stronger Operations, And Better Margins.
        </p>
      </div>
      <div class="member-card-widget" id="member-card-widget">
        <h3>Your Member Card</h3>
        <p class="widget-subtitle">For the local demo, this is pulled from your Login</p>
        <div class="id-card" id="id-card">
          <div class="id-card-top">
            <div>
              <div class="id-card-name">John Doe</div>
              <div class="id-card-members">Members Only</div>
            </div>
            <div class="active-badge">
              <span class="active-dot"></span>Active
            </div>
          </div>
          <div class="id-card-bottom">
            <div class="id-field">
              <div class="id-field-label">Membership ID:</div>
              <div class="id-field-value">373839393</div>
            </div>
            <div class="id-member-since">
              <div class="ms-label">Member Since</div>
              <div class="ms-value">9 JUN 2023</div>
            </div>
          </div>
        </div>
        <a href="#" class="upgrade-btn" id="upgrade-btn">Upgrade To Gold</a>
      </div>
    </section>
  </div>

  <!-- RESOURCE CARDS -->
  <section class="cards-section" id="cards-section">
    <div class="cards-grid">

      <div class="resource-card" id="card-job-postings">
        <div class="card-img-wrap"><img class="card-img" src="IMG_JOB_POSTINGS" alt="Restaurant manager reviewing job applications" /></div>
        <div class="card-box">
          <div class="card-content">
            <div>
              <div class="card-tags"><span class="tag-free">Free Access</span><span class="tag-cat">Hiring &bull; Monthly Benefit</span></div>
              <h2 class="card-title">Complimentary Access to Two(2) Job Postings Every Month</h2>
              <p class="card-desc">Quickly fill open restaurant roles with premium visibility to top local hospitality talent. Post jobs easily and hire faster.</p>
            </div>
            <a href="details_job_postings.html" class="view-btn" id="btn-job-postings">View Details</a>
          </div>
        </div>
      </div>

      <div class="resource-card" id="card-free-website">
        <div class="card-img-wrap"><img class="card-img" src="IMG_LAPTOP" alt="Laptop with food delivery website" /></div>
        <div class="card-box">
          <div class="card-content">
            <div>
              <div class="card-tags"><span class="tag-free">Free Templates</span><span class="tag-cat">Reputation &bull; Reviews</span></div>
              <h2 class="card-title">Free Website With Restaurant Templates</h2>
              <p class="card-desc">A Modern Website Starter With Restaurant-Specific Structure And Conversion Sections.</p>
            </div>
            <a href="details_free_website.html" class="view-btn" id="btn-free-website">View Details</a>
          </div>
        </div>
      </div>

      <div class="resource-card" id="card-facebook-masterclass">
        <div class="card-img-wrap"><img class="card-img" src="IMG_WAITER" alt="Restaurant waiter serving food" /></div>
        <div class="card-box">
          <div class="card-content">
            <div>
              <div class="card-tags"><span class="tag-free">Master Class</span><span class="tag-cat">Free &bull; Reputation</span></div>
              <h2 class="card-title">Facebook Restaurant Marketing Master Class</h2>
              <p class="card-desc">A step-by-step masterclass built for restaurant operators to run Facebook marketing that drives reservations, orders, and repeat visits without wasting money.</p>
            </div>
            <a href="details_facebook.html" class="view-btn" id="btn-facebook-masterclass">View Details</a>
          </div>
        </div>
      </div>

      <div class="resource-card" id="card-instagram-masterclass">
        <div class="card-img-wrap"><img class="card-img" src="IMG_CHALKBOARD" alt="Restaurant menu chalkboard" /></div>
        <div class="card-box">
          <div class="card-content">
            <div>
              <div class="card-tags"><span class="tag-free">Master Class</span><span class="tag-cat">Free &bull; Reputation</span></div>
              <h2 class="card-title">Instagram Restaurant Marketing Master Class</h2>
              <p class="card-desc">A practical Instagram masterclass built for restaurants sharing how to create content that gets discovered locally, drives visits, and turns followers into customers.</p>
            </div>
            <a href="details_instagram.html" class="view-btn" id="btn-instagram-masterclass">View Details</a>
          </div>
        </div>
      </div>

      <div class="resource-card" id="card-yelp-growth">
        <div class="card-img-wrap"><img class="card-img" src="IMG_REELS" alt="Overhead view of diner holding wine" /></div>
        <div class="card-box">
          <div class="card-content">
            <div>
              <div class="card-tags"><span class="tag-free">Master Class</span><span class="tag-cat">Free &bull; Reputation</span></div>
              <h2 class="card-title">How to Grow Your Business on Yelp</h2>
              <p class="card-desc">A Yelp growth guide for restaurants - how to increase visibility, improve ranking, and turn views into visits while handling reviews professionally?</p>
            </div>
            <a href="details_yelp.html" class="view-btn" id="btn-yelp-growth">View Details</a>
          </div>
        </div>
      </div>

      <div class="resource-card" id="card-vendor-negotiation">
        <div class="card-img-wrap"><img class="card-img" src="IMG_NEARME" alt="Overhead restaurant food spread" /></div>
        <div class="card-box">
          <div class="card-content">
            <div>
              <div class="card-tags"><span class="tag-free">Guides</span><span class="tag-cat">Free &bull; Negotiation</span></div>
              <h2 class="card-title">Get Free Vendor Negotiation Guide</h2>
              <p class="card-desc">A practical negotiation guide for restaurant operators - scripts, checklists, and a simple process to lower costs and improve terms with vendors.</p>
            </div>
            <a href="details_vendor.html" class="view-btn" id="btn-vendor-negotiation">View Details</a>
          </div>
        </div>
      </div>

      <div class="resource-card" id="card-ai-content">
        <div class="card-img-wrap"><img class="card-img" src="IMG_WOMAN" alt="Woman enjoying restaurant meal" /></div>
        <div class="card-box">
          <div class="card-content">
            <div>
              <div class="card-tags"><span class="tag-free">Free</span><span class="tag-cat">AI &bull; Content Kit</span></div>
              <h2 class="card-title">Create Restaurant Marketing Content FAST with AI</h2>
              <p class="card-desc">A practical kit that helps restaurant operators generate high-quality posts, promos, emails, and review responses in minutes without sounding generic.</p>
            </div>
            <a href="details_ai_content.html" class="view-btn" id="btn-ai-content">View Details</a>
          </div>
        </div>
      </div>

      <div class="resource-card" id="card-business-plan">
        <div class="card-img-wrap"><img class="card-img" src="IMG_BAR" alt="Upscale bar interior" /></div>
        <div class="card-box">
          <div class="card-content">
            <div>
              <div class="card-tags"><span class="tag-free">Free</span><span class="tag-cat">Business Plan &bull; Content Kit</span></div>
              <h2 class="card-title">How To Easily Write A Restaurant Business Plan</h2>
              <p class="card-desc">A simple, step-by-step kit to build a professional restaurant business plan - clear enough for lenders and structured enough for execution.</p>
            </div>
            <a href="details_business_plan.html" class="view-btn" id="btn-business-plan">View Details</a>
          </div>
        </div>
      </div>

      <div class="resource-card" id="card-chomp-show">
        <div class="card-img-wrap"><img class="card-img" src="IMG_CHOMP" alt="Woman dining at restaurant" /></div>
        <div class="card-box">
          <div class="card-content">
            <div>
              <div class="card-tags"><span class="tag-free">Free</span><span class="tag-cat">Opportunity &bull; Chomp</span></div>
              <h2 class="card-title">Get Featured on The Chomp Show - Complimentary Restaurant Spotlight</h2>
              <p class="card-desc">Share your restaurant's story and signature food on a professionally produced feature, built to drive awareness, community support, and new guests.</p>
            </div>
            <a href="details_chomp.html" class="view-btn" id="btn-chomp-show">View Details</a>
          </div>
        </div>
      </div>

      <div class="resource-card" id="card-google-reviews">
        <div class="card-img-wrap"><img class="card-img" src="IMG_GOOGLE_REVIEWS" alt="Google Reviews Templates" /></div>
        <div class="card-box">
          <div class="card-content">
            <div>
              <div class="card-tags"><span class="tag-free">Free</span><span class="tag-cat">Templates &bull; Scripts</span></div>
              <h2 class="card-title">Google Reviews Response Templates (Including 1-Star Responses)</h2>
              <p class="card-desc">Professional, ready-to-use responses for 1–5 star reviews. Protect your reputation, stay consistent, and respond faster without sounding defensive.</p>
            </div>
            <a href="details_google_reviews.html" class="view-btn" id="btn-google-reviews">View Details</a>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- CTA BANNER: floats over the footer -->
  <div class="cta-outer-wrap">
    <div class="cta-banner-wrap" id="cta-wrap">
      <div class="cta-banner">
        <div class="cta-banner-left">
          <div class="cta-logo-box">
            <img src="IMG_FAVICON" alt="Icon" class="cta-logo-img" />
          </div>
          <div class="cta-text">
            <h4>Become A Member Of The Restaurant Association!</h4>
            <p>Unlock Exclusive Access To Webinars, Events, And The Latest News For Free!</p>
          </div>
        </div>
        <button class="cta-sign-up-btn" id="cta-signup-btn">Sign Up</button>
      </div>
    </div>
  </div>

  <!-- FOOTER -->
  <footer id="footer">
    <div class="footer-inner">
      <div class="footer-main">
        <div class="footer-brand">
          <div class="footer-logo-row">
            <img src="IMG_FAVICON" alt="Restaurant Association Icon" class="footer-logo-img" />
          </div>
          <h3>Restaurant Association</h3>
          <p>Empowering restaurant professionals with free resources, training, and networking opportunities to build successful businesses.</p>
          <button class="footer-signup-btn" id="footer-signup-btn">Sign Up Free</button>
        </div>
        <div class="footer-col">
          <h4>Pages</h4>
          <ul>
            <li><a href="#" id="footer-articles">Articles</a></li>
            <li><a href="#" id="footer-news">News</a></li>
            <li><a href="#" id="footer-topics">Topics</a></li>
            <li><a href="#" id="footer-shows">Shows</a></li>
            <li><a href="#" id="footer-academy">Academy</a></li>
            <li><a href="#" id="footer-events">Events</a></li>
            <li><a href="#" id="footer-jobs">Jobs</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>About</h4>
          <ul>
            <li><a href="#" id="footer-about">About Us</a></li>
            <li><a href="#" id="footer-team">Our Team</a></li>
            <li><a href="#" id="footer-contact">Contact Us</a></li>
            <li><a href="#" id="footer-sitemap">Sitemap</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Resources</h4>
          <ul>
            <li><a href="#" id="footer-library">Library</a></li>
            <li><a href="#" id="footer-templates">Templates</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-connect">
        <h4>Connect</h4>
        <div class="social-icons">
          <a href="#" class="social-icon" id="social-linkedin" aria-label="LinkedIn">
            <svg viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
          </a>
          <a href="#" class="social-icon" id="social-instagram" aria-label="Instagram">
            <svg viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
          </a>
          <a href="#" class="social-icon" id="social-tiktok" aria-label="TikTok">
            <svg viewBox="0 0 24 24"><path d="M19.59 6.69a4.83 4.83 0 01-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 01-2.88 2.5 2.89 2.89 0 01-2.89-2.89 2.89 2.89 0 012.89-2.89c.28 0 .54.04.79.1V9.01a6.31 6.31 0 00-.79-.05 6.34 6.34 0 00-6.34 6.34 6.34 6.34 0 006.34 6.34 6.34 6.34 0 006.33-6.34V8.69a8.22 8.22 0 004.83 1.56V6.79a4.85 4.85 0 01-1.06-.1z"/></svg>
          </a>
          <a href="#" class="social-icon" id="social-youtube" aria-label="YouTube">
            <svg viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 00-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 00.502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 002.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 002.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
          </a>
          <a href="#" class="social-icon" id="social-x" aria-label="X (Twitter)">
            <svg viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.747l7.73-8.835L1.254 2.25H8.08l4.253 5.622L18.244 2.25zm-1.161 17.52h1.833L7.084 4.126H5.117L17.083 19.77z"/></svg>
          </a>
        </div>
      </div>

      <div class="footer-bottom">
        <div class="footer-legal">
          <a href="#" id="footer-ethics">Editorial Ethics Policy</a>
          <a href="#" id="footer-guidelines">Review Guidelines</a>
          <a href="#" id="footer-disclosure">Disclosure Policy</a>
          <a href="#" id="footer-privacy">Privacy Policy</a>
          <a href="#" id="footer-terms">Terms of Service</a>
        </div>
        <p class="footer-copyright">&copy; 2026 Restaurant Association. All rights reserved.</p>
      </div>
    </div>
  </footer>

</body>
</html>"""

# Replace image placeholders with actual base64 data
for img_key, img_val in imgs.items():
    token = img_key.upper()   # e.g. img_waiter -> IMG_WAITER
    html = html.replace(token, img_val)

output_path = r'C:\Users\Itam\.gemini\antigravity\scratch\restaurant-association\index.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

size = os.path.getsize(output_path)
print(f'HTML written successfully!')
print(f'File: {output_path}')
print(f'Size: {size:,} bytes ({size/1024/1024:.2f} MB)')
