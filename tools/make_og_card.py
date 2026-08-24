"""Render the Open Graph card for the landing page.

The site declares `twitter:card = summary_large_image` but shipped no image, so
every link preview of iquana-tool.github.io rendered blank. This draws the card
from the same palette the landing page and the application use.

Dark only, deliberately: every screenshot and clip in the docs is recorded
against the app's dark theme, and an OG card is a fixed image with no way to
follow the reader's preference.

    python tools/make_og_card.py

Writes assets/og.png (1200x630, the size both Open Graph and Twitter want).
"""
from __future__ import annotations

import pathlib

from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1200, 630

# Straight from the landing page's dark tokens.
BG = (13, 17, 23)
SURFACE = (21, 27, 35)
BORDER = (39, 47, 58)
TEXT = (232, 237, 243)
MUTED = (170, 182, 195)
DIM = (139, 152, 166)
ACCENT = (20, 184, 166)
ACCENT_BRIGHT = (61, 219, 199)
ON_ACCENT = (4, 35, 31)

FONTS = pathlib.Path("C:/Windows/Fonts")
ROOT = pathlib.Path(__file__).resolve().parent.parent


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONTS / name), size)


def main() -> None:
    img = Image.new("RGB", (W, H), BG)

    # Soft teal glow behind the mark, mirroring the hero's accent gradient.
    glow = Image.new("RGB", (W, H), BG)
    gd = ImageDraw.Draw(glow)
    gd.ellipse((-260, -400, 900, 420), fill=(16, 62, 60))
    img = Image.blend(img, glow.filter(ImageFilter.GaussianBlur(180)), 0.85)

    d = ImageDraw.Draw(img)

    # --- the mark: same rounded teal badge as the favicon -------------------
    badge = 96
    bx, by = 84, 74
    d.rounded_rectangle((bx, by, bx + badge, by + badge), radius=21, fill=ACCENT)
    iq = font("georgiab.ttf", 52)
    _, _, iw, ih = d.textbbox((0, 0), "IQ", font=iq)
    d.text((bx + (badge - iw) / 2, by + (badge - ih) / 2 - 8), "IQ", font=iq, fill=ON_ACCENT)

    wordmark = font("segoeuib.ttf", 40)
    d.text((bx + badge + 26, by + 26), "IQUANA", font=wordmark, fill=TEXT)

    # --- headline ----------------------------------------------------------
    head = font("segoeuib.ttf", 62)
    lines = ["Annotate, quantify and evaluate", "scientific image data."]
    y = 208
    for line in lines:
        d.text((84, y), line, font=head, fill=TEXT)
        y += 76

    # --- accent rule -------------------------------------------------------
    d.rounded_rectangle((84, y + 22, 84 + 92, y + 28), radius=3, fill=ACCENT)

    # --- subline -----------------------------------------------------------
    sub = font("segoeui.ttf", 27)
    d.text(
        (84, y + 62),
        "AI-assisted segmentation, a human correction loop,",
        font=sub,
        fill=MUTED,
    )
    d.text((84, y + 100), "and measurements in real units.", font=sub, fill=MUTED)

    # --- footer ------------------------------------------------------------
    d.line((84, H - 108, W - 84, H - 108), fill=BORDER, width=1)
    foot = font("segoeui.ttf", 23)
    d.text((84, H - 76), "Built at DFKI  ·  in partnership with HIFMB", font=foot, fill=DIM)

    url = font("segoeuib.ttf", 23)
    _, _, uw, _ = d.textbbox((0, 0), "iquana-tool.github.io", font=url)
    d.text((W - 84 - uw, H - 76), "iquana-tool.github.io", font=url, fill=ACCENT_BRIGHT)

    out = ROOT / "assets" / "og.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, "PNG", optimize=True)
    print(f"wrote {out} ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
