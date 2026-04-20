import re

fpath = r'C:\Users\Administrator\github\fateandmethod-site\bazi-ten-gods-guide.html'
with open(fpath, 'rb') as f:
    c = f.read()

# Add SEO meta tags after <meta name="viewport"
viewport_end = c.find(b'<meta name="viewport"')
if viewport_end >= 0:
    end_tag = c.find(b'>', viewport_end)
    canonical = b'https://fateandmethod.com/bazi-ten-gods-guide.html'
    meta_tags = (
        b'    <meta name="description" content="Complete guide to BaZi Ten Gods - the fundamental framework for analyzing energy interactions in Chinese metaphysics. Learn how the ten celestial stems manifest as productive or destructive relationships in your Ba Zi chart.">\n'
        b'    <link rel="canonical" href="https://fateandmethod.com/bazi-ten-gods-guide.html">\n'
        b'    <meta property="og:title" content="BaZi Ten Gods Complete Guide | Fate & Method">\n'
        b'    <meta property="og:description" content="Complete guide to BaZi Ten Gods - the fundamental framework for analyzing energy interactions in Chinese metaphysics.">\n'
        b'    <meta property="og:type" content="article">\n'
        b'    <meta property="og:url" content="https://fateandmethod.com/bazi-ten-gods-guide.html">\n'
        b'    <meta property="og:site_name" content="Fate & Method">\n'
        b'    <meta name="twitter:card" content="summary_large_image">\n'
        b'    <meta name="twitter:title" content="BaZi Ten Gods Complete Guide | Fate & Method">\n'
        b'    <meta name="twitter:description" content="Complete guide to BaZi Ten Gods - the fundamental framework for analyzing energy interactions in Chinese metaphysics.">\n'
    )
    c = c[:end_tag+1] + b'\n' + meta_tags + c[end_tag+1:]

with open(fpath, 'wb') as f:
    f.write(c)

# Verify
c2 = open(fpath, 'rb').read()
for tag in [b'og:type', b'og:url', b'og:title', b'twitter:title', b'canonical']:
    i = c2.find(tag)
    if i >= 0:
        snippet = c2[i:i+60].decode('utf-8', errors='replace')
        print(tag.decode(), ':', snippet[:60])
    else:
        print(tag.decode(), ': MISSING')
