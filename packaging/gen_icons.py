#!/usr/bin/env python3
"""PhotoSweet identity: generate the aperture logo (SVG) and every raster app icon."""
import math, pathlib
from PIL import Image, ImageDraw

DIR = pathlib.Path(__file__).resolve().parent.parent
ICONS = DIR / "assets" / "app-icon"
VIO = (139, 92, 246)   # #8B5CF6
ROSE = (244, 63, 94)   # #F43F5E
CX = CY = 256.0
RO = 168.0
RI = 92.0
INSET = 1.7
RADIUS = 112.0


def blade_points():
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
    pts = []
    for i in range(8):
        a = math.radians(i * 45 - 90)
        rad = R if i % 2 == 0 else r
        pts.append((cx + rad * math.cos(a), cy + rad * math.sin(a)))
    return pts


def svg_text():
    quads = blade_points()
    blades = "\n".join(
        "    <polygon points=\"%s\"/>" % " ".join(f"{x:.1f},{y:.1f}" for x, y in q)
        for q in quads
    )
    pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in sparkle(392, 122, 34, 9))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" role="img" aria-label="PhotoSweet">
  <defs>
    <linearGradient id="tile" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#8B5CF6"/>
      <stop offset="1" stop-color="#F43F5E"/>
    </linearGradient>
  </defs>
  <rect width="512" height="512" rx="112" fill="url(#tile)"/>
  <g fill="#FFFFFF" fill-opacity="0.95">
{blades}
    <polygon points="{pts}"/>
  </g>
</svg>
'''


def lerp(a, b, t):
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


def render(view, size, ss=3):
    x, y, w, h = view
    big = size * ss
    img = Image.new("RGBA", (big, big), (0, 0, 0, 0))

    grad = Image.new("RGB", (512, 512))
    px = grad.load()
    for j in range(512):
        for i in range(512):
            px[i, j] = lerp(VIO, ROSE, (i + j) / 1022.0)

    s = big / w
    tile = grad.resize((big, big), Image.LANCZOS)

    mask = Image.new("L", (big, big), 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle(
        [(-x) * s, (-y) * s, (-x + 512) * s, (-y + 512) * s],
        radius=RADIUS * s, fill=255)
    img.paste(tile, (0, 0), mask)

    d = ImageDraw.Draw(img, "RGBA")
    fg = (255, 255, 255, 242)
    for q in blade_points():
        d.polygon([((qx - x) * s, (qy - y) * s) for qx, qy in q], fill=fg)
    d.polygon([((px2 - x) * s, (py2 - y) * s) for px2, py2 in sparkle(392, 122, 34, 9)], fill=fg)

    return img.resize((size, size), Image.LANCZOS)


def main():
    ICONS.mkdir(parents=True, exist_ok=True)
    (ICONS / "photosweet.svg").write_text(svg_text(), encoding="utf-8")
    (ICONS / "photosweet-small.svg").write_text(svg_text(), encoding="utf-8")

    FULL = (0, 0, 512, 512)
    TIGHT = (22, 22, 468, 468)
    MAC = (-62, -62, 636, 636)

    render(MAC, 1024).save(ICONS / "photosweet-1024.png")

    for s in (16, 24, 32, 48, 64, 128, 256, 512):
        out = ICONS / "hicolor" / f"{s}x{s}" / "apps"
        out.mkdir(parents=True, exist_ok=True)
        render(TIGHT, s, ss=6 if s <= 64 else 3).save(out / "studio.salim.photosweet.png")

    scal = ICONS / "hicolor" / "scalable" / "apps"
    scal.mkdir(parents=True, exist_ok=True)
    (scal / "studio.salim.photosweet.svg").write_text(svg_text(), encoding="utf-8")

    ico_sizes = [16, 20, 24, 32, 40, 48, 64, 128, 256]
    base = render(TIGHT, 256)
    base.save(ICONS / "photosweet.ico", format="ICO", sizes=[(s, s) for s in ico_sizes])

    icns = render(MAC, 1024)
    icns.save(ICONS / "photosweet.icns", format="ICNS")

    print("icons written to", ICONS)


if __name__ == "__main__":
    main()
