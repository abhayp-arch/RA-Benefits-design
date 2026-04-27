import re

with open('build_details.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update CSS
old_css = """/* FAQ */
.faq-block { margin-bottom: 40px; }
.faq-item { border-bottom: 1px solid #EBEBEB; padding: 18px 0; }
.faq-item:last-child { border-bottom: none; }
.faq-q { font-size: 15px; font-weight: 700; color: #181D2D; margin-bottom: 8px; }
.faq-a { font-size: 14px; color: #555; line-height: 1.6; margin: 0; }"""

new_css = """/* FAQ */
.faq-block { margin-bottom: 40px; }
.faq-item { border-bottom: 1px solid #EBEBEB; padding: 18px 0; }
.faq-item:last-child { border-bottom: none; }
.faq-q { font-size: 15px; font-weight: 700; color: #181D2D; cursor: pointer; display: flex; justify-content: space-between; align-items: center; list-style: none; margin: 0; outline: none; }
.faq-q::-webkit-details-marker { display: none; }
.faq-icon { flex-shrink: 0; width: 24px; height: 24px; background: url('data:image/svg+xml;utf8,<svg viewBox="0 0 24 24" fill="none" stroke="%23181D2D" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><polyline points="6 9 12 15 18 9"></polyline></svg>') no-repeat center; transition: transform 0.3s ease; }
details[open] .faq-icon { transform: rotate(180deg); }
.faq-a { font-size: 14px; color: #555; line-height: 1.6; margin: 12px 0 0 0; padding-right: 32px; }"""

if old_css in text:
    text = text.replace(old_css, new_css)
    print("Updated CSS.")

# The blocks start with <div class="faq-block"> and end when we see a closing div before </div>\n      </div>
# We can just split by `<div class="faq-block">`
parts = text.split('<div class="faq-block">')

new_text = parts[0]
for i in range(1, len(parts)):
    part = parts[i]
    # part contains the faq-items and then the rest of the string for that page.
    # we can find all faq-items until another div closes the faq-block.
    # Actually, we can just split by `</div>\n      </div>\n"""\n}` or similar.
    # Or just use regex to find `<div class="faq-item">` and replace them until there's no more.
    # Since we know the exact HTML structure, let's parse items sequentially.
    
    # We'll extract all items from the start of `part` until we hit the end of the block.
    # Since each `<div class="faq-item">` contains exactly `<p class="faq-q">` and `<p class="faq-a">` and one `</div>`, 
    # the end of the block is simply the `</div>` that appears right after the last faq-item's `</div>`.
    
    items_html = ""
    item_pattern = r'^\s*<div class="faq-item">\s*<p class="faq-q">(.*?)</p>\s*<p class="faq-a">(.*?)</p>\s*</div>(.*)$'
    
    index = 0
    rest = part
    while True:
        match = re.match(item_pattern, rest, re.DOTALL)
        if not match:
            break
        q = match.group(1).strip()
        a = match.group(2).strip()
        rest = match.group(3)
        
        attr = " open" if index == 0 else ""
        items_html += f'''
          <details class="faq-item"{attr}>
            <summary class="faq-q">{q}<span class="faq-icon"></span></summary>
            <p class="faq-a">{a}</p>
          </details>'''
        index += 1
    
    new_text += '<div class="faq-block">' + items_html + rest

if new_text != text:
    with open('build_details.py', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Updated FAQs.")
else:
    print("No changes made to HTML (already updated or regex failed).")
