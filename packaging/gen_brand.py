#!/usr/bin/env python3
"""Write PhotoSweet brand assets (mark + wordmark) into docs/brand/."""
import math, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "brand"

CX = CY = 256.0
RO, RI, INSET = 168.0, 92.0, 1.7


def blades():
    quads = []
    for k in range(6):
        a0 = math.radians(k * 60 + INSET)
        a1 = math.radians((k + 1) * 60 - INSET)
        quads.append([
            (CX + RO * math.cos(a0), CY + RO * math.sin(a0)),
            (CX + RO * math.cos(a1), CY + RO * math.sin(a1)),
            (CX + RI * math.cos(a1), CY + RI * math.sin(a1)),
            (CX + RI * math.cos(a0), CY + RI * math.sin(a0)),
        ])
    return quads


def sparkle(cx, cy, R, r):
    return [(cx + (R if i % 2 == 0 else r) * math.cos(math.radians(i * 45 - 90)),
             cy + (R if i % 2 == 0 else r) * math.sin(math.radians(i * 45 - 90))) for i in range(8)]


def poly(pts):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)


MARK = f'''  <defs>
    <linearGradient id="tile" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#8B5CF6"/>
      <stop offset="1" stop-color="#F43F5E"/>
    </linearGradient>
  </defs>
  <rect width="512" height="512" rx="112" fill="url(#tile)"/>
  <g fill="#FFFFFF" fill-opacity="0.95">''' + "".join(
    f'\n    <polygon points="{poly(q)}"/>' for q in blades()) + f'''
    <polygon points="{poly(sparkle(392, 122, 34, 9))}"/>
  </g>'''

mark = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" role="img" aria-label="PhotoSweet">{MARK}\n</svg>\n'


def wordmark(fill, tag):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 200" role="img" aria-label="PhotoSweet">
  <g transform="translate(20 20) scale(0.3125)">{MARK}
  </g>
  <text x="205" y="132" font-family="Inter, Segoe UI, Helvetica, Arial, sans-serif" font-weight="800" font-size="94" letter-spacing="-2" fill="{fill}">PhotoSweet</text>
</svg>
'''


OUT.mkdir(parents=True, exist_ok=True)
(OUT / "photosweet-mark.svg").write_text(mark, encoding="utf-8")
(OUT / "photosweet-mark-white.svg").write_text(mark, encoding="utf-8")
(OUT / "photosweet-logo.svg").write_text(wordmark("#0F172A", "dark"), encoding="utf-8")
(OUT / "photosweet-logo-white.svg").write_text(wordmark("#FFFFFF", "light"), encoding="utf-8")
(OUT / "README.md").write_text(
    "# PhotoSweet brand\n\n"
    "The PhotoSweet mark (a six-blade aperture with a sparkle on a violet-to-rose gradient) and\n"
    "wordmark, owned by salim-slimani.\n\n"
    "- `photosweet-mark.svg`: the app mark alone.\n"
    "- `photosweet-logo.svg`: mark + wordmark for light backgrounds.\n"
    "- `photosweet-logo-white.svg`: mark + wordmark for dark backgrounds.\n\n"
    "The app icon in `assets/app-icon/` is the same mark; regenerate both with\n"
    "`packaging/gen_icons.py`. These files are licensed like the rest of PhotoSweet (MIT OR\n"
    "Apache-2.0); see `LICENSE-brand.txt`.\n", encoding="utf-8")
(OUT / "LICENSE-brand.txt").write_text(
    "The PhotoSweet name, mark and wordmark in this directory are the brand of salim-slimani.\n"
    "They may be used to refer to this project. Unlike the upstream project this fork was\n"
    "derived from, these brand assets are covered by the same license as the source code\n"
    "(MIT OR Apache-2.0); see the repository root LICENSE-MIT, LICENSE-APACHE and NOTICE.\n",
    encoding="utf-8")
print("brand written to", OUT)
