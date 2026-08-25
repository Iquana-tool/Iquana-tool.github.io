"""Render the geometry-metric explainer for the documentation.

Draws one contour and points at the four geometry-tier metrics on it. The
geometry is computed rather than eyeballed: the max-diameter chord really is the
farthest pair of points on the sampled outline, and the circularity figure is the
real 4*pi*A/P^2 of the shape drawn. An explainer that illustrated a metric with a
chord that was not actually the maximum would be teaching the wrong thing.

Only circularity carries a number. Area, perimeter and diameter are reported in
whatever unit the image is calibrated to, so a concrete value on a schematic
would be meaningless; circularity is dimensionless, so its value is the same
everywhere and is worth showing.

    python tools/make_metric_explainer.py

Writes docs/assets/img/metric-explainer.svg. The file is included into pages with
pymdownx.snippets so the SVG inherits the page's CSS variables and follows the
light/dark toggle.
"""
from __future__ import annotations

import math
import pathlib

# One closed contour, as cubic bezier segments: (p0, c1, c2, p1).
# Deliberately elongated and a little lumpy, so "the two farthest points" is
# visually obvious rather than an arbitrary-looking chord.
SEGMENTS = [
    ((62, 225), (70, 168), (128, 132), (196, 142)),
    ((196, 142), (252, 150), (280, 186), (332, 178)),
    ((332, 178), (392, 169), (438, 198), (440, 245)),
    ((440, 245), (442, 292), (392, 318), (332, 310)),
    ((332, 310), (280, 303), (254, 276), (198, 286)),
    ((198, 286), (132, 297), (54, 282), (62, 225)),
]

SAMPLES_PER_SEGMENT = 90
ROOT = pathlib.Path(__file__).resolve().parent.parent


def bezier(p0, c1, c2, p1, t):
    u = 1 - t
    x = u**3 * p0[0] + 3 * u**2 * t * c1[0] + 3 * u * t**2 * c2[0] + t**3 * p1[0]
    y = u**3 * p0[1] + 3 * u**2 * t * c1[1] + 3 * u * t**2 * c2[1] + t**3 * p1[1]
    return x, y


def sample() -> list[tuple[float, float]]:
    pts: list[tuple[float, float]] = []
    for seg in SEGMENTS:
        for i in range(SAMPLES_PER_SEGMENT):
            pts.append(bezier(*seg, i / SAMPLES_PER_SEGMENT))
    return pts


def polygon_area(pts) -> float:
    s = 0.0
    for i in range(len(pts)):
        x0, y0 = pts[i]
        x1, y1 = pts[(i + 1) % len(pts)]
        s += x0 * y1 - x1 * y0
    return abs(s) / 2


def polygon_perimeter(pts) -> float:
    s = 0.0
    for i in range(len(pts)):
        x0, y0 = pts[i]
        x1, y1 = pts[(i + 1) % len(pts)]
        s += math.hypot(x1 - x0, y1 - y0)
    return s


def centroid(pts) -> tuple[float, float]:
    cx = cy = a = 0.0
    for i in range(len(pts)):
        x0, y0 = pts[i]
        x1, y1 = pts[(i + 1) % len(pts)]
        cross = x0 * y1 - x1 * y0
        a += cross
        cx += (x0 + x1) * cross
        cy += (y0 + y1) * cross
    a /= 2
    return cx / (6 * a), cy / (6 * a)


def max_diameter(pts):
    """Farthest pair of sampled points — what `max_diameter` actually measures."""
    best = (0.0, pts[0], pts[0])
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            d = math.hypot(pts[i][0] - pts[j][0], pts[i][1] - pts[j][1])
            if d > best[0]:
                best = (d, pts[i], pts[j])
    return best


def path_d() -> str:
    d = f"M {SEGMENTS[0][0][0]} {SEGMENTS[0][0][1]}"
    for _p0, c1, c2, p1 in SEGMENTS:
        d += f" C {c1[0]} {c1[1]}, {c2[0]} {c2[1]}, {p1[0]} {p1[1]}"
    return d + " Z"


def main() -> None:
    pts = sample()
    area = polygon_area(pts)
    perim = polygon_perimeter(pts)
    circ = 4 * math.pi * area / (perim**2)
    diam, a_pt, b_pt = max_diameter(pts)
    cx, cy = centroid(pts)

    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    bb = (min(xs), min(ys), max(xs), max(ys))

    mx = (a_pt[0] + b_pt[0]) / 2

    # The perimeter leader has to touch the outline it names, so take the real
    # topmost sampled point rather than a hand-placed coordinate.
    top_pt = min(pts, key=lambda q: q[1])
    ty = top_pt[1] - 46

    # The diameter label goes below the whole shape: pushed only perpendicular to
    # the chord it would land on the bottom edge of the contour.
    dlx, dly = mx, bb[3] + 36

    # Glyph for the circularity panel: the same contour, shrunk.
    gs = 34 / (bb[2] - bb[0])
    gx, gy = 545 - (bb[0] + bb[2]) / 2 * gs, 300 - (bb[1] + bb[3]) / 2 * gs

    d = path_d()

    svg = f"""<svg class="iq-metric-explainer" viewBox="0 0 780 392" role="img"
     xmlns="http://www.w3.org/2000/svg"
     aria-label="One annotated contour, labelled with the four geometry metrics:
     area is the enclosed surface, perimeter is the closed outline, max diameter is
     the distance between the two farthest points, and circularity is
     4 pi area over perimeter squared - {circ:.2f} for this shape against 1.00 for a circle.">
  <style>
    .iq-metric-explainer text {{
      font-family: var(--md-text-font, system-ui), system-ui, sans-serif;
    }}
    .iq-me-name {{ font-size: 17px; font-weight: 700; fill: var(--md-default-fg-color); }}
    .iq-me-desc {{ font-size: 13.5px; fill: var(--md-default-fg-color--light); }}
    .iq-me-mono {{
      font-family: var(--md-code-font, monospace), monospace;
      font-size: 13px; fill: var(--md-default-fg-color--light);
    }}
    .iq-me-fill   {{ fill: var(--iq-accent); fill-opacity: .15; }}
    .iq-me-stroke {{ fill: none; stroke: var(--iq-accent); stroke-width: 2.5; }}
    .iq-me-lead   {{ stroke: var(--iq-border-strong); stroke-width: 1.2; fill: none; }}
    .iq-me-chord  {{
      stroke: var(--md-default-fg-color); stroke-width: 1.8;
      stroke-dasharray: 7 5; fill: none;
    }}
    .iq-me-cap    {{ fill: var(--md-default-fg-color); }}
    .iq-me-panel  {{ fill: none; stroke: var(--iq-border); stroke-width: 1; }}
    .iq-me-value  {{ font-size: 21px; font-weight: 700; fill: var(--iq-accent); }}
  </style>

  <!-- ---- the contour ------------------------------------------------- -->
  <path d="{d}" class="iq-me-fill"/>
  <path d="{d}" class="iq-me-stroke"/>

  <!-- area: named inside the region it refers to -->
  <text x="{cx:.0f}" y="{cy - 34:.0f}" class="iq-me-name" text-anchor="middle">area</text>
  <text x="{cx:.0f}" y="{cy - 16:.0f}" class="iq-me-desc" text-anchor="middle">the enclosed surface</text>

  <!-- perimeter: leader out to the top edge -->
  <path d="M {top_pt[0]:.1f} {top_pt[1]:.1f} L {top_pt[0]:.1f} {ty:.1f} L {top_pt[0] + 42:.1f} {ty:.1f}" class="iq-me-lead"/>
  <circle cx="{top_pt[0]:.1f}" cy="{top_pt[1]:.1f}" r="3.5" class="iq-me-cap"/>
  <text x="{top_pt[0] + 52:.1f}" y="{ty - 4:.1f}" class="iq-me-name">perimeter</text>
  <text x="{top_pt[0] + 52:.1f}" y="{ty + 14:.1f}" class="iq-me-desc">the closed outline</text>

  <!-- max diameter: the genuinely farthest pair of points -->
  <path d="M {a_pt[0]:.1f} {a_pt[1]:.1f} L {b_pt[0]:.1f} {b_pt[1]:.1f}" class="iq-me-chord"/>
  <circle cx="{a_pt[0]:.1f}" cy="{a_pt[1]:.1f}" r="4.5" class="iq-me-cap"/>
  <circle cx="{b_pt[0]:.1f}" cy="{b_pt[1]:.1f}" r="4.5" class="iq-me-cap"/>
  <text x="{dlx:.0f}" y="{dly:.0f}" class="iq-me-name" text-anchor="middle">max_diameter</text>
  <text x="{dlx:.0f}" y="{dly + 18:.0f}" class="iq-me-desc" text-anchor="middle">the two farthest points</text>

  <!-- ---- circularity panel ------------------------------------------- -->
  <rect x="497" y="86" width="252" height="240" rx="12" class="iq-me-panel"/>
  <text x="521" y="122" class="iq-me-name">circularity</text>
  <text x="521" y="146" class="iq-me-mono">4&#960; &#183; area / perimeter&#178;</text>
  <text x="521" y="170" class="iq-me-desc">dimensionless, so calibration</text>
  <text x="521" y="188" class="iq-me-desc">never changes it</text>

  <line x1="521" y1="212" x2="725" y2="212" class="iq-me-panel"/>

  <!-- a perfect circle scores exactly 1 -->
  <circle cx="545" cy="248" r="17" class="iq-me-fill"/>
  <circle cx="545" cy="248" r="17" class="iq-me-stroke"/>
  <text x="580" y="245" class="iq-me-value">1.00</text>
  <text x="580" y="263" class="iq-me-desc">a perfect circle</text>

  <!-- the same contour drawn above, shrunk -->
  <g transform="translate({gx:.1f} {gy:.1f}) scale({gs:.4f})">
    <path d="{d}" class="iq-me-fill"/>
    <path d="{d}" class="iq-me-stroke" style="stroke-width:{2.5 / gs:.1f}"/>
  </g>
  <text x="580" y="297" class="iq-me-value">{circ:.2f}</text>
  <text x="580" y="315" class="iq-me-desc">this contour</text>
</svg>
"""

    # No blank lines: Python-Markdown terminates a raw-HTML block at the first
    # one, which would split the SVG into paragraphs and drop its <text> nodes.
    svg = chr(10).join(line for line in svg.splitlines() if line.strip())

    out = ROOT / "docs" / "assets" / "img" / "metric-explainer.svg"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(svg + chr(10), encoding="ascii")

    print(f"wrote {out}")
    print(f"  area        {area:10.1f}")
    print(f"  perimeter   {perim:10.1f}")
    print(f"  circularity {circ:10.3f}")
    print(f"  diameter    {diam:10.1f}  {a_pt[0]:.0f},{a_pt[1]:.0f} -> {b_pt[0]:.0f},{b_pt[1]:.0f}")
    print(f"  centroid    {cx:.0f},{cy:.0f}")


if __name__ == "__main__":
    main()
