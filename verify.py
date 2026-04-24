with open(r'C:\Users\Itam\.gemini\antigravity\scratch\restaurant-association\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

checks = [
    ('DOCTYPE html', '<!DOCTYPE html>' in content),
    ('Navbar class', 'class="navbar"' in content),
    ('Logo SVG', 'class="logo-svg"' in content),
    ('Nav links', 'id="nav-news"' in content and 'id="nav-topics"' in content),
    ('Search bar', 'class="search-bar"' in content),
    ('Profile btn', 'class="profile-btn"' in content),
    ('Hero section', 'class="hero-section"' in content),
    ('Member badge', 'class="member-badge"' in content),
    ('Practical Perks heading', 'Practical Perks' in content),
    ('Orange highlight', 'class="highlight"' in content),
    ('Member card widget', 'class="member-card-widget"' in content),
    ('ID card', 'class="id-card"' in content),
    ('John Doe', 'John Doe' in content),
    ('Active badge', 'class="active-badge"' in content),
    ('Membership ID 373839393', '373839393' in content),
    ('9 JUN 2023', '9 JUN 2023' in content),
    ('Upgrade To Gold', 'Upgrade To Gold' in content),
    ('Cards grid', 'class="cards-grid"' in content),
    ('8 resource cards', content.count('class="resource-card"') == 8),
    ('Google Reviews card', 'Google Reviews Response Templates' in content),
    ('Delivery Menu card', 'Delivery Menu Optimization Guide' in content),
    ('Reels card', 'Reels' in content),
    ('Near Me card', 'Near Me' in content),
    ('Email List card', 'Email List Builder' in content),
    ('SMS card', 'Sms Templates For Slow Nights' in content),
    ('Chomp Show card', 'Chomp Show' in content),
    ('Free Website card', 'Free Website With Restaurant Templates' in content),
    ('Base64 images present', 'data:image/png;base64' in content),
    ('All 8 images embedded', content.count('data:image/png;base64') == 8),
    ('CTA banner', 'class="cta-banner"' in content),
    ('Signup CTA text', 'Become A Member Of The Restaurant Association' in content),
    ('CTA Sign Up btn', 'cta-sign-up-btn' in content),
    ('Dark footer', '#181D2D' in content),
    ('Pages column', 'footer-articles' in content),
    ('About column', 'footer-about' in content),
    ('Resources column', 'footer-library' in content),
    ('Social icons', 'social-linkedin' in content),
    ('Connect section', 'footer-connect' in content),
    ('LinkedIn', 'social-linkedin' in content),
    ('Instagram', 'social-instagram' in content),
    ('TikTok', 'social-tiktok' in content),
    ('YouTube', 'social-youtube' in content),
    ('X Twitter', 'social-x' in content),
    ('Legal links', 'footer-ethics' in content),
    ('Copyright 2026', '2026 Restaurant Association' in content),
    ('Inter font', 'Inter' in content),
    ('Orange brand #EF5C2A', '#EF5C2A' in content),
    ('tag-free label', 'tag-free' in content),
    ('View Details button', 'View Details' in content),
]

passed = 0
failed = 0
for name, result in checks:
    status = 'PASS' if result else 'FAIL'
    if not result:
        failed += 1
    print(f'[{status}] {name}')
    if result:
        passed += 1

print(f'\nResults: {passed} passed, {failed} failed out of {len(checks)} checks')
print(f'File size: {len(content):,} bytes ({len(content)/1024/1024:.2f} MB)')
