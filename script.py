import base64
import urllib.request
import re

with open(r'C:\Users\adity\.gemini\antigravity\brain\646d578b-4f52-4600-8fbd-16154262d9d0\media__1775847836092.jpg', 'rb') as f:
    img_b64 = base64.b64encode(f.read()).decode('utf-8')
    prefix = 'data:image/jpeg;base64,'
    aditya_img = prefix + img_b64

url = 'https://hero-section-gules.vercel.app/api/hero?name=ADITYA'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
svg_content = urllib.request.urlopen(req).read().decode('utf-8')

pattern = r'href=\"data:image/[^;]+;base64,[A-Za-z0-9+/=]+\"'
svg_content = re.sub(pattern, f'href=\"{aditya_img}\"', svg_content)

view_pattern = r'(>PROFILE VIEWS</text>\s*<text[^>]*>)[0-9,]+(</text>)'
svg_content = re.sub(view_pattern, r'\g<1>123\g<2>', svg_content)

with open('hero.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)
print('Done!')
