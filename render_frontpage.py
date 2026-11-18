#!/usr/bin/env python3
"""Render the round-2 poster for news-image-20261118.

Draws a 1024x1024 high-contrast infographic poster summing up
Wednesday 18 November 2026's world news, using only Pillow and
DejaVu fonts. Every story was cross-checked against multiple
news reports of 18 November 2026:

- Ukraine's drone/missile strikes of 16-17 Nov collapsed the road
  arch of the Kerch Bridge into the Kerch Strait (road shut, rail
  restored on the 18th, two killed); Russia hit Kyiv's Dnipro
  bridges in reply. The Shenzhen APEC summit: Xi met Putin on the
  18th, Trump flew in from Quad talks in Manila for the first
  Xi-Trump-Putin trilateral.
- The US struck an IRGC missile site on Qeshm Island; Iran
  answered with drones on US bases in Bahrain and Kuwait.
- Democrat Mary Peltola won Alaska's Senate seat, giving
  Democrats a 56-44 Senate majority.
- The Ebola outbreak in DR Congo more than doubled (UN: over
  11,000 cases, 5,400 deaths); the US lost its measles-free
  status after 26 years.
- A Russian military plane crashed in Siberia (Kemerovo),
  killing 19; Category 5 Cyclone Xavier hit the Cook Islands.
- Markets slid (S&P 500 -1.0%, DAX -2.1%, gold $3,775, Brent
  $91.55); the EU proposed a loan of up to 45 billion euros for
  Ukraine in 2027.

Run:  python3 render_frontpage.py [output-path]
Default output: entry.png next to this script.
"""
import math
import os
import sys

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (13, 22, 38)          # deep navy
PANEL = (23, 38, 62)       # panel navy
PANEL2 = (19, 32, 54)
PAPER = (246, 241, 231)    # headline off-white
BODY = (203, 211, 224)     # body light grey-blue
RED = (226, 54, 48)
ORANGE = (246, 148, 32)
GOLD = (246, 198, 66)
TEAL = (52, 186, 172)
GREY = (148, 161, 180)
SKY = (44, 74, 116)
SEA = (26, 84, 138)
WHITE = (255, 255, 255)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)


def wrap(draw, text, fnt, max_width):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def centered(draw, text, y, fnt, fill):
    draw.text(((W - draw.textlength(text, font=fnt)) / 2, y), text,
              font=fnt, fill=fill)


def chip(draw, x, y, text, fnt, fill_bg, fill_tx):
    w = draw.textlength(text, font=fnt) + 22
    draw.rounded_rectangle([x, y, x + w, y + 30], radius=8, fill=fill_bg)
    draw.text((x + 11, y + 6), text, font=fnt, fill=fill_tx)
    return x + w + 10


def draw_bridge_scene(draw, x0, y0, x1, y1):
    """Kerch Bridge: two towers, a gap where the arch fell, the
    fallen span tilted into the sea, blast and smoke."""
    draw.rectangle([x0, y0, x1, y1], fill=SKY)
    sea_y = y0 + int((y1 - y0) * 0.68)
    deck_y = y0 + int((y1 - y0) * 0.52)
    # drones in the sky, kept clear of the towers
    for dx, dy in ((x0 + 150, y0 + 18), (x1 - 150, y0 + 14)):
        draw.line([(dx - 11, dy), (dx + 11, dy)], fill=(170, 190, 215),
                  width=3)
        draw.line([(dx - 11, dy - 5), (dx - 11, dy + 5)],
                  fill=(170, 190, 215), width=2)
        draw.line([(dx + 11, dy - 5), (dx + 11, dy + 5)],
                  fill=(170, 190, 215), width=2)
    # towers
    for tx in (x0 + 52, x1 - 68):
        draw.rectangle([tx, y0 + 34, tx + 16, deck_y], fill=PAPER)
    # standing deck segments (gap in the middle)
    gap0, gap1 = (x0 + x1) // 2 - 52, (x0 + x1) // 2 + 52
    draw.rectangle([x0 + 6, deck_y, gap0, deck_y + 9], fill=PAPER)
    draw.rectangle([gap1, deck_y, x1 - 6, deck_y + 9], fill=PAPER)
    # cables from tower tops to the standing deck
    for tx, sgn in ((x0 + 60, 1), (x1 - 60, -1)):
        for k in range(1, 5):
            px = tx + sgn * k * 26
            if x0 + 10 < px < gap0 - 4 or gap1 + 4 < px < x1 - 10:
                draw.line([(tx, y0 + 36), (px, deck_y)], fill=PAPER,
                          width=2)
    # blast at the gap
    bx, by = (x0 + x1) // 2, deck_y - 2
    pts = []
    for i in range(16):
        ang = math.pi * i / 8
        r = 40 if i % 2 == 0 else 18
        pts.append((bx + r * math.cos(ang), by + r * math.sin(ang)))
    draw.polygon(pts, fill=ORANGE)
    draw.ellipse([bx - 13, by - 13, bx + 13, by + 13], fill=RED)
    draw.ellipse([bx - 52, by - 62, bx - 16, by - 28], fill=(120, 128, 142))
    draw.ellipse([bx + 10, by - 74, bx + 52, by - 34], fill=(140, 148, 160))
    # fallen span, tilted into the sea
    draw.polygon([(gap0 - 6, deck_y + 4), (gap1 + 16, sea_y + 26),
                  (gap1 + 2, sea_y + 44), (gap0 - 18, deck_y + 20)],
                 fill=(196, 60, 44))
    # sea
    draw.rectangle([x0, sea_y, x1, y1], fill=SEA)
    for wx in range(x0 + 12, x1 - 30, 40):
        draw.arc([wx, sea_y + 16, wx + 28, sea_y + 30], 0, 180,
                 fill=(170, 205, 235), width=2)
    # shore labels
    f_lab = SANS_B(15)
    draw.text((x0 + 10, deck_y + 16), "CRIMEA", font=f_lab, fill=WHITE)
    draw.text((x1 - 10 - draw.textlength("RUSSIA", font=f_lab),
               deck_y + 16), "RUSSIA", font=f_lab, fill=WHITE)


def draw_missile(draw, cx, cy):
    draw.ellipse([cx - 27, cy - 27, cx + 27, cy + 27], fill=(64, 34, 40))
    # rocket body, diagonal
    draw.polygon([(cx - 14, cy + 16), (cx + 4, cy - 20),
                  (cx + 16, cy - 8), (cx - 2, cy + 24)], fill=PAPER)
    draw.polygon([(cx + 4, cy - 20), (cx + 12, cy - 30),
                  (cx + 16, cy - 8)], fill=RED)
    draw.polygon([(cx - 14, cy + 16), (cx - 24, cy + 26),
                  (cx - 8, cy + 26)], fill=ORANGE)
    draw.polygon([(cx - 4, cy + 30), (cx - 14, cy + 40),
                  (cx + 2, cy + 38)], fill=GOLD)


def draw_table(draw, cx, cy):
    draw.ellipse([cx - 27, cy - 27, cx + 27, cy + 27], fill=(30, 62, 54))
    # three leader dots around a table
    for ang, col in ((90, RED), (210, GOLD), (330, TEAL)):
        px = cx + 15 * math.cos(math.radians(ang))
        py = cy + 15 * math.sin(math.radians(ang))
        draw.ellipse([px - 7, py - 7, px + 7, py + 7], fill=col)
    draw.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=PAPER)


def draw_dome(draw, cx, cy):
    draw.ellipse([cx - 27, cy - 27, cx + 27, cy + 27], fill=(52, 44, 84))
    draw.arc([cx - 16, cy - 6, cx + 16, cy + 22], 180, 360, fill=PAPER,
             width=3)
    draw.line([(cx - 20, cy + 8), (cx + 20, cy + 8)], fill=PAPER, width=3)
    draw.line([(cx, cy - 14), (cx, cy - 6)], fill=GOLD, width=3)
    for px in (-12, 0, 12):
        draw.line([(cx + px, cy + 8), (cx + px, cy + 16)], fill=PAPER,
                  width=2)
    draw.line([(cx - 20, cy + 17), (cx + 20, cy + 17)], fill=PAPER,
              width=3)


def draw_virus(draw, cx, cy):
    draw.ellipse([cx - 27, cy - 27, cx + 27, cy + 27], fill=(66, 40, 30))
    for i in range(8):
        ang = math.pi * i / 4
        px = cx + 13 * math.cos(ang)
        py = cy + 13 * math.sin(ang)
        draw.line([(cx, cy), (px, py)], fill=ORANGE, width=3)
        draw.ellipse([px - 4, py - 4, px + 4, py + 4], fill=ORANGE)
    draw.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], fill=RED)


def draw_storm(draw, cx, cy):
    draw.ellipse([cx - 27, cy - 27, cx + 27, cy + 27], fill=(28, 56, 84))
    for r, a0 in ((17, 20), (11, 200), (6, 90)):
        draw.arc([cx - r, cy - r, cx + r, cy + r], a0, a0 + 260,
                 fill=TEAL, width=3)
    draw.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=PAPER)


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    M = 36
    CW = W - 2 * M

    # ---- Masthead ----
    y = 16
    centered(d, "THE WORLD IN ONE DAY", y, SERIF_B(47), PAPER)
    y += 58
    d.rectangle([M, y, W - M, y + 34], fill=RED)
    centered(d, "WEDNESDAY · 18 NOVEMBER 2026", y + 4, SANS_B(25), WHITE)
    y += 48

    # ---- Lead: Kerch Bridge ----
    lead_y0 = y
    lead_y1 = y + 340
    d.rectangle([M, lead_y0, W - M, lead_y1], fill=PANEL)
    tx = M + 22
    ty = lead_y0 + 12
    d.text((tx, ty), "UKRAINE WAR — THE DAY'S BIG STORY", font=SANS_B(19),
           fill=GOLD)
    ty += 30
    f_lead = SERIF_B(54)
    ty = draw_lines(d, ["UKRAINE", "DROPS THE", "KERCH BRIDGE"],
                    tx, ty, f_lead, PAPER, 62)
    ty += 6
    sub = ("Two nights of strikes topple the road arch into the "
           "strait — Russia answers on Kyiv's bridges.")
    ty = draw_lines(d, wrap(d, sub, SANS(20), 545), tx, ty, SANS(20),
                    BODY, 27)
    # illustration, right side of the lead panel
    draw_bridge_scene(d, 622, lead_y0 + 18, W - M - 18, lead_y0 + 252)
    f_cap = SANS(14)
    d.text((622, lead_y0 + 258),
           "The 19-km Kerch Bridge: the fallen road arch.",
           font=f_cap, fill=GREY)
    # chips along the bottom of the lead panel
    cy = lead_y1 - 42
    assert ty <= cy - 6, f"lead text overflows into chips: ty={ty} cy={cy}"
    cx = M + 22
    f_chip = SANS_B(16)
    cx = chip(d, cx, cy, "ARCH DOWN 200+ M", f_chip, RED, WHITE)
    cx = chip(d, cx, cy, "2 KILLED", f_chip, (64, 74, 92), WHITE)
    cx = chip(d, cx, cy, "ROAD SHUT · RAIL BACK", f_chip,
              (64, 74, 92), WHITE)
    cx = chip(d, cx, cy, "PUTIN'S LINK TO CRIMEA", f_chip,
              (64, 74, 92), WHITE)
    y = lead_y1 + 12

    # ---- Middle band: Gulf + Shenzhen ----
    band_y1 = y + 232
    half = (CW - 16) // 2
    panels = [
        (M, "MIDDLE EAST — ESCALATION", RED,
         "US bombs Qeshm — Iran strikes US bases",
         "US jets hit an IRGC missile site on Qeshm Island, in the "
         "Strait of Hormuz. Iran answers with drones on US bases in "
         "Bahrain & Kuwait.", draw_missile),
        (M + half + 16, "SHENZHEN — APEC SUMMIT", TEAL,
         "Xi, Trump & Putin: one table, three powers",
         "Xi hosts Putin in Shenzhen as Trump flies in from Quad "
         "talks in Manila — Thursday brings their first-ever "
         "trilateral.", draw_table),
    ]
    for px, kick, accent, head, body, icon in panels:
        d.rectangle([px, y, px + half, band_y1], fill=PANEL)
        icon(d, px + 44, y + 44)
        d.text((px + 82, y + 18), kick, font=SANS_B(16), fill=accent)
        d.text((px + 82, y + 42), "18 NOV 2026", font=SANS(14), fill=GREY)
        hy = y + 76
        hy = draw_lines(d, wrap(d, head, SERIF_B(28), half - 36),
                        px + 18, hy, SERIF_B(28), PAPER, 34)
        draw_lines(d, wrap(d, body, SANS(18), half - 36),
                   px + 18, hy + 4, SANS(18), BODY, 24)
    y = band_y1 + 12

    # ---- Third band: Senate / Health / Disaster ----
    band2_y1 = y + 186
    col_w = (CW - 32) // 3
    cols = [
        ("UNITED STATES", GOLD, "Peltola flips Alaska",
         "Democrat beats the Republican incumbent — a 56–44 "
         "Democratic Senate majority.", draw_dome),
        ("HEALTH", ORANGE, "Ebola doubles in Congo",
         "UN counts 11,000 cases & 5,400 dead. The US loses its "
         "measles-free status.", draw_virus),
        ("DISASTER", RED, "19 die in Siberia crash",
         "Military plane down in Kemerovo. Cyclone Xavier, Cat 5, "
         "slams the Cook Islands.", draw_storm),
    ]
    for i, (kick, accent, head, body, icon) in enumerate(cols):
        px = M + i * (col_w + 16)
        d.rectangle([px, y, px + col_w, band2_y1], fill=PANEL2)
        icon(d, px + 40, y + 40)
        d.text((px + 74, y + 20), kick, font=SANS_B(15), fill=accent)
        d.text((px + 74, y + 42), "18 NOV", font=SANS(13), fill=GREY)
        hy = y + 70
        hy = draw_lines(d, wrap(d, head, SERIF_B(24), col_w - 30),
                        px + 15, hy, SERIF_B(24), PAPER, 29)
        draw_lines(d, wrap(d, body, SANS(16), col_w - 30),
                   px + 15, hy + 3, SANS(16), BODY, 21)
    y = band2_y1 + 12

    # ---- Markets ticker ----
    d.rectangle([M, y, W - M, y + 42], fill=(120, 26, 22))
    ticker = ("MARKETS SLIDE — S&P 500 −1.0% · DAX −2.1% · "
              "GOLD $3,775 · BRENT $91.55")
    centered(d, ticker, y + 9, SANS_B(20), WHITE)
    y += 54
    extra = ("EU PROPOSES €45BN LOAN FOR UKRAINE · ISRAEL ELECTS "
             "KAHANA SPEAKER · HOUTHIS TARGET SAUDI PIPELINE")
    centered(d, extra, y, SANS_B(15), GREY)
    y += 26
    foot = "Every story first reported on Wednesday, 18 November 2026"
    centered(d, foot, y, SANS(14), GREY)
    y += 20
    assert y <= H - 6, f"layout overflow: final y={y}"

    img.save(out, "PNG", optimize=True)
    print(f"wrote {out} ({os.path.getsize(out)} bytes)")


if __name__ == "__main__":
    main()
