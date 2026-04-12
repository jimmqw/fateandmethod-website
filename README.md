# Fate & Method &mdash; fateandmethod.com

Ancient Chinese Metaphysics in English. A premium English-language resource covering Zi Wei Dou Shu, Liu Yao, Mei Hua Yi Shu, Da Liu Ren, Xuan Kong, and Tai Yi.

Site: https://fateandmethod.com

## The Six Systems

| # | System | Chinese | Description |
|---|--------|---------|-------------|
| 01 | Zi Wei Dou Shu | 紫微斗数 | The most sophisticated Chinese astrological system — 12 palaces, 14 main stars, 100+ auxiliary stars |
| 02 | Liu Yao | 六爻 | I Ching coin divination — three coins, six lines, one specific question |
| 03 | Mei Hua Yi Shu | 梅花易数 | Plum Blossom Numerology — spontaneous divination using any observable phenomenon |
| 04 | Da Liu Ren | 大六壬 | The oldest of the three greats — day-based celestial stem & earthly branch system |
| 05 | Xuan Kong | 奇门遁甲 | Secret Gate Numerology — optimal timing and directional energy for tactical decisions |
| 06 | Tai Yi Shen Shu | 太乙神数 | The most esoteric — cosmic-scale cycle divination for predicting empire-wide events |

## Technical Notes

- All pages use the same header/footer/nav from `index.html`
- Article pages use a 2-column layout (content + sticky TOC sidebar at 240px)
- All internal links use relative paths (`./ziwei.html`, etc.)
- Each page has proper SEO meta tags (title, description, canonical)
- Design: deep black (#0a0a0f) + gold (#c9a84c) + cream (#f0ece0)
- Fonts: Cormorant Garamond (headings) + Inter (body) from Google Fonts
- CSS is embedded in each HTML file (no external stylesheet)
- All emoji/decorative symbols are decorative only (not meaningful content)

## File Structure

```
fateandmethod-site/
├── index.html       — Homepage
├── ziwei.html       — Zi Wei Dou Shu article
├── liuyao.html      — Liu Yao article
├── meihua.html      — Mei Hua Yi Shu article
├── daliuren.html    — Da Liu Ren article
├── xuankong.html    — Xuan Kong article
├── taiyi.html       — Tai Yi article
├── sitemap.xml      — XML sitemap
├── CNAME            — GitHub Pages custom domain
└── README.md        — This file
```

## Development

The site is a static HTML site suitable for hosting on GitHub Pages, Netlify, Vercel, or any static host.

To preview locally:
```bash
# Python simple server
python -m http.server 8000

# Or any static file server
npx serve .
```

## License

&copy; 2026 FateAndMethod.com. All rights reserved.
