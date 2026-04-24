import json, os, re

# Read data
with open(r'C:\Users\Itam\.gemini\antigravity\scratch\restaurant-association\img_data.json', 'r') as f:
    imgs = json.load(f)

with open(r'C:\Users\Itam\.gemini\antigravity\scratch\restaurant-association\build_html.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract parts
head_css = re.search(r'(<!DOCTYPE html>.*?</style>\n</head>\n<body>)', text, re.DOTALL).group(1)
navbar = re.search(r'(<!-- NAVBAR -->.*?</nav>)', text, re.DOTALL).group(1)
cta_footer = re.search(r'(<!-- CTA BANNER: floats over the footer -->.*?</footer>)', text, re.DOTALL).group(1)
member_widget_clean = re.search(r'(<div class="member-card-widget".*?Upgrade To Gold</a>\n      </div>)', text, re.DOTALL).group(1)

HTML_START = head_css

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
.details-hero-img { width: 100%; height: auto; border-radius: 16px; margin-bottom: 24px; object-fit: cover; box-shadow: 0 4px 20px rgba(0,0,0,0.08); }
.details-tags { display: flex; align-items: center; gap: 12px; margin-bottom: 60px; }

.benefit-alert { background: rgba(239,92,42,0.06); border: 1px solid rgba(239,92,42,0.2); border-radius: 8px; padding: 20px 24px; margin-bottom: 40px; }
.benefit-alert p { font-weight: 700; color: #181D2D; font-size: 15px; margin: 0; line-height: 1.5; }

.content-section h2 { font-size: 24px; font-weight: 800; color: #181D2D; margin-bottom: 24px; }
.bullet-list { list-style: none; margin-bottom: 40px; padding: 0; }
.bullet-list li { position: relative; padding-left: 20px; font-size: 15px; color: #333; line-height: 1.6; margin-bottom: 16px; }
.bullet-list li::before { content: ''; position: absolute; left: 0; top: 8px; width: 6px; height: 6px; background: #EF5C2A; border-radius: 50%; }

.number-list { list-style: none; margin-bottom: 60px; padding: 0; counter-reset: item; }
.number-list li { counter-increment: item; font-size: 15px; color: #333; line-height: 1.6; margin-bottom: 16px; }
.number-list li::before { content: counter(item) ". "; font-weight: 600; color: #555; margin-right: 4px; }

/* Claim box */
.claim-box { background: linear-gradient(135deg, #FFF9F5 0%, #FFFDFB 100%); border-radius: 20px; border: 1px solid rgba(239,92,42,0.1); display: flex; align-items: center; justify-content: space-between; overflow: hidden; position: relative; box-shadow: 0 10px 40px rgba(239,92,42,0.04); padding: 40px; margin-bottom: 80px; }
.claim-text { max-width: 380px; position: relative; z-index: 2; }
.claim-title { font-size: 32px; font-weight: 800; color: #181D2D; margin-bottom: 12px; }
.claim-title span { color: #EF5C2A; }
.claim-text p { font-size: 14px; color: #555; line-height: 1.5; margin-bottom: 24px; }
.claim-btn { background: #EF5C2A; color: #FFF; font-size: 16px; font-weight: 700; padding: 14px 32px; border-radius: 8px; border: none; cursor: pointer; display: inline-flex; align-items: center; gap: 8px; transition: background 0.2s; }
.claim-btn:hover { background: #D44D22; }
.claim-btn svg { width: 18px; height: 18px; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }

.claim-tip { display: flex; align-items: flex-start; gap: 10px; background: rgba(239,92,42,0.06); border-radius: 8px; padding: 12px 16px; margin-top: 24px; }
.claim-tip svg { width: 16px; height: 16px; fill: #EF5C2A; flex-shrink: 0; margin-top: 2px; }
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

DETAILS_CONTENT = """
<div class="details-wrapper">
  <div class="details-layout">
    <div class="details-main">
      <h1 class="details-title">Google Reviews Response Templates</h1>
      <p class="details-subtitle">Professional, Ready-To-Use Responses For 1-5 Star Reviews&mdash;Save Time And Stay Consistent. This Member Benefit Is Designed To Be Simple, Practical, And Fast To Implement.</p>
      
      <img src="IMG_WOMAN" alt="Waitress with tablet" class="details-hero-img" />
      
      <div class="details-tags">
        <span class="tag-free" style="padding: 6px 14px; font-size: 13px;">Free Templates</span>
        <span class="tag-cat" style="font-size: 15px;">Reputation &bull; Reviews</span>
      </div>
      
      <div class="benefit-alert">
        <p>Restaurant Association Benefit &mdash; Vendor-Neutral. Fulfilled By An Ra Vetted Provider When Needed.</p>
      </div>
      
      <div class="content-section">
        <h2>What You Get</h2>
        <ul class="bullet-list">
          <li>Copy/Paste Templates You Can Customize For Your Brand Voice.</li>
          <li>Guidance For When To Use Each Template And What To Avoid.</li>
          <li>A Quick Checklist To Keep Messaging Consistent Across Managers.</li>
        </ul>
        
        <h2>How It Works</h2>
        <ul class="number-list">
          <li>Copy/Paste Templates You Can Customize For Your Brand Voice.</li>
          <li>Guidance For When To Use Each Template And What To Avoid.</li>
          <li>A Quick Checklist To Keep Messaging Consistent Across Managers.</li>
        </ul>
      </div>
      
      <div class="claim-box">
        <div class="claim-text">
          <h3 class="claim-title">Ready to <span>Claim?</span></h3>
          <p>Claiming takes less than a minute.<br/>We'll confirm eligibility and send next steps.</p>
          <button class="claim-btn">
            <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M9 12l2 2 4-4"/></svg>
            Claim This Benefit &rarr;
          </button>
          
          <div class="claim-tip">
            <svg viewBox="0 0 24 24"><path d="M12 2a7 7 0 00-7 7c0 2 1.5 4 2 5.5V17a2 2 0 002 2h6a2 2 0 002-2v-2.5c.5-1.5 2-3.5 2-5.5a7 7 0 00-7-7z" style="stroke:currentColor;stroke-width:2;fill:none;"/><line x1="12" y1="21" x2="12" y2="21.01" style="stroke:currentColor;stroke-width:3;stroke-linecap:round;"/></svg>
            <p>Tip: You can keep this page re-branded and add provider details only after claim approval.</p>
          </div>
        </div>
        <div class="claim-img-wrap">
          <img src="IMG_GIFTS" alt="Gifts" />
        </div>
      </div>
    </div>
    
    <div class="details-sidebar">
      """ + member_widget_clean + """
    </div>
  </div>
</div>
"""

FOOTER_CTA = cta_footer

html = HTML_START + DETAILS_CSS + navbar + DETAILS_CONTENT + FOOTER_CTA + "\n</body>\n</html>"

html = html.replace("IMG_WOMAN", imgs['img_woman'])
html = html.replace("IMG_LOGO", imgs['img_logo'])
html = html.replace("IMG_FAVICON", imgs['img_favicon'])
html = html.replace("IMG_GIFTS", imgs['img_gifts'])

# Ensure "View Details" buttons link to this page
with open(r'C:\Users\Itam\.gemini\antigravity\scratch\restaurant-association\build_html.py', 'r', encoding='utf-8') as f:
    index_script = f.read()

index_script = index_script.replace('class="view-btn"', 'class="view-btn" onclick="window.location.href=\'details.html\'"')

with open(r'C:\Users\Itam\.gemini\antigravity\scratch\restaurant-association\build_html.py', 'w', encoding='utf-8') as f:
    f.write(index_script)

with open(r'C:\Users\Itam\.gemini\antigravity\scratch\restaurant-association\details.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("details.html written successfully!")
