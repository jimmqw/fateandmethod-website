#!/usr/bin/env python3
import re

path = r'C:\Users\Administrator\github\fateandmethod-site\feng-shui-fundamentals.html'
# Try different encodings
for enc in ['utf-8', 'latin-1', 'cp1252']:
    try:
        with open(path, encoding=enc) as f:
            content = f.read()
        print(f"Read with {enc}, length={len(content)}")
        break
    except Exception as e:
        print(f"{enc} failed: {e}")

# Search for the pattern
idx = content.find('Zi Wei Dou Shu')
if idx >= 0:
    snippet = content[idx-30:idx+100]
    print(f"Found at index {idx}")
    # The em dash is a 3-byte sequence in UTF-8: \xe2\x80\x94
    # Let's check the actual bytes
    snippet_bytes = snippet.encode('latin-1')
    print(f"Snippet (latin-1): {snippet_bytes}")
