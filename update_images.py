import base64
import json
import os

IMG_DIR = r'C:\Users\Itam\.gemini\antigravity\scratch\restaurant-association\benefits page Restaurant Association image'
JSON_PATH = r'C:\Users\Itam\.gemini\antigravity\scratch\restaurant-association\img_data.json'

mapping = {
    'Complimentary Access to 2 Job Postings Every Month.png': 'img_job_postings',
    'Free Website With Restaurant Templates.png': 'img_laptop',
    'Facebook Restaurant Marketing Master Class.png': 'img_waiter',
    'Instagram Restaurant Marketing Master Class.png': 'img_chalkboard',
    'How to Grow Your Business on Yelp.png': 'img_reels',
    'Get Free Vendor Negotiation Guide.png': 'img_nearme',
    'Create Restaurant Marketing Content FAST with AI.png': 'img_woman',
    'How To Easily Write A Restaurant Business Plan.png': 'img_bar',
    'Get Featured on The Chomp Show - Complimentary Restaurant Spotlight.png': 'img_chomp',
    'Google Reviews Response Templates (Including 1-Star Responses).png': 'img_google_reviews'
}

def get_base64(path):
    with open(path, 'rb') as f:
        data = f.read()
        return f"data:image/png;base64,{base64.b64encode(data).decode('utf-8')}"

with open(JSON_PATH, 'r') as f:
    data = json.load(f)

for filename, key in mapping.items():
    full_path = os.path.join(IMG_DIR, filename)
    if os.path.exists(full_path):
        print(f"Processing {filename} -> {key}")
        data[key] = get_base64(full_path)
    else:
        print(f"Warning: {filename} not found!")

with open(JSON_PATH, 'w') as f:
    json.dump(data, f)

print("img_data.json updated successfully.")
