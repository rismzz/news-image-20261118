#!/usr/bin/env python3
"""Render the front page for news-image-20261118.

Draws a 1024x1024 newspaper front page summing up Wednesday
18 November 2026's world news, using only Pillow and DejaVu fonts.
Run:  python3 render_frontpage.py [output-path]
Default output: entry.png next to this script.
"""
import os
import sys
import textwrap

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)      # off-white
INK = (20, 20, 20)           # near-black
RED = (185, 28, 28)          # accent red
NAVY = (30, 58, 95)          # dark blue
GREY = (90, 90, 85)
LIGHT_BLUE = (214, 226, 238)
SEA = (52, 96, 138)
ORANGE = (234, 120, 30)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)


def wrap(draw, text, fnt, max_width):
    """Greedy word-wrap of text to fit max_width pixels."""
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


def rule(draw, x0, x1, y, width=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def draw_bridge(draw, x0, y0, x1, y1):
    """Simple geometric Kerch Bridge illustration with a blast."""
    draw.rectangle([x0, y0, x1, y1], fill=LIGHT_BLUE)
    # sea
    sea_y = y0 + int((y1 - y0) * 0.72)
    draw.rectangle([x0, sea_y, x1, y1], fill=SEA)
    # sun
    draw.ellipse([x1 - 62, y0 + 10, x1 - 22, y0 + 50], fill=(240, 200, 90))
    # towers
    deck_y = y0 + int((y1 - y0) * 0.55)
    for tx in (x0 + 70, x1 - 90):
        draw.rectangle([tx, y0 + 28, tx + 16, deck_y], fill=NAVY)
        draw.rectangle([tx - 4, y0 + 22, tx + 20, y0 + 30], fill=NAVY)
    # deck
    draw.rectangle([x0 + 8, deck_y, x1 - 8, deck_y + 8], fill=INK)
    # suspension cables: diagonals from each tower top down to the deck
    for tx in (x0 + 70, x1 - 90):
        top_x, top_y = tx + 8, y0 + 24
        for k in range(1, 6):
            px = tx + 8 + (k - 3) * 22 if tx < (x0 + x1) // 2 else tx + 8 - (k - 3) * 22
            draw.line([(top_x, top_y), (px, deck_y)], fill=NAVY, width=2)
    # blast starburst on the deck
    bx, by = (x0 + x1) // 2, deck_y - 6
    pts = []
    import math
    for i in range(16):
        ang = math.pi * i / 8
        r = 34 if i % 2 == 0 else 15
        pts.append((bx + r * math.cos(ang), by + r * math.sin(ang)))
    draw.polygon(pts, fill=ORANGE)
    draw.ellipse([bx - 12, by - 12, bx + 12, by + 12], fill=RED)
    # smoke puffs
    draw.ellipse([bx - 46, by - 52, bx - 14, by - 22], fill=(120, 120, 118))
    draw.ellipse([bx + 8, by - 60, bx + 44, by - 26], fill=(140, 140, 136))
    # waves
    for wx in range(x0 + 12, x1 - 12, 34):
        draw.arc([wx, sea_y + 12, wx + 26, sea_y + 26], 0, 180, fill=(255, 255, 255), width=2)


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 36                      # margin
    CW = W - 2 * M              # content width
    y = 22

    # ---- Masthead ----
    mast = "THE WORLD — IN ONE IMAGE"
    f_mast = SERIF_B(50)
    d.text(((W - d.textlength(mast, font=f_mast)) / 2, y), mast,
           font=f_mast, fill=INK)
    y += 66
    rule(d, M, W - M, y, 3)
    y += 8
    date = "WEDNESDAY, 18 NOVEMBER 2026"
    f_date = SANS_B(24)
    d.text(((W - d.textlength(date, font=f_date)) / 2, y), date,
           font=f_date, fill=RED)
    y += 38
    rule(d, M, W - M, y, 1)
    y += 6
    rule(d, M, W - M, y, 3)
    y += 16

    # ---- Lead story ----
    f_kick = SANS_B(19)
    d.text((M, y), "UKRAINE · RUSSIA — WAR OF THE BRIDGES", font=f_kick, fill=RED)
    y += 28
    f_head = SERIF_B(42)
    head = "Ukraine hits Kerch Bridge as Russia strikes Kyiv's bridges"
    lines = wrap(d, head, f_head, CW)
    y = draw_lines(d, lines, M, y, f_head, INK, 50)
    y += 6
    # deck (left) + bridge illustration (right)
    deck_w = 560
    ill_x0, ill_y0 = M + deck_w + 16, y
    ill_x1, ill_y1 = W - M, y + 148
    f_deck = SANS(20)
    deck = ("On the second day of a war of the bridges, Ukraine damaged "
            "the Kerch Bridge to Crimea while Russian missiles hit bridges "
            "in Kyiv — each side striking the other's strategic crossings.")
    dlines = wrap(d, deck, f_deck, deck_w)
    y2 = draw_lines(d, dlines, M, y, f_deck, INK, 27)
    draw_bridge(d, ill_x0, ill_y0, ill_x1, ill_y1)
    cap = "The Kerch Bridge, linking Crimea to Russia."
    f_cap = SERIF(14)
    d.text((ill_x0, ill_y1 + 6), cap, font=f_cap, fill=GREY)
    y = max(y2, ill_y1 + 26) + 10
    rule(d, M, W - M, y, 2)
    y += 14

    # ---- Supporting stories, 2x2 grid ----
    col_w = (CW - 24) // 2
    stories = [
        ("ASIA-PACIFIC · DIPLOMACY",
         "Trump lands in Manila for Quad talks ahead of China trip",
         "Xi, Trump and Putin are set to meet in Shenzhen on Thursday "
         "on the sidelines of the APEC summit."),
        ("MIDDLE EAST",
         "Iran hits US military radar in Bahrain with drones",
         "An IRGC drone strike on Sheikh Isa base was intercepted, "
         "Bahrain says; no casualties or damage reported."),
        ("TRADE · APEC",
         "Canada and China extend trade deal as Xi meets Carney",
         "The two leaders agreed to keep trade flowing ahead of "
         "the APEC summit in Shenzhen."),
        ("BRITAIN · MIDDLE EAST",
         "UK sanctions Israeli settlement firms to protect two-state solution",
         "London targets companies in the occupied territories in "
         "defence of a two-state future."),
    ]
    f_sk = SANS_B(15)
    f_sh = SERIF_B(23)
    f_sd = SANS(16)
    row_top = y
    for i, (kick, headline, summary) in enumerate(stories):
        col = i % 2
        row = i // 2
        x = M + col * (col_w + 24)
        yy = row_top + row * 128
        d.text((x, yy), kick, font=f_sk, fill=RED)
        yy += 20
        hlines = wrap(d, headline, f_sh, col_w)
        yy = draw_lines(d, hlines, x, yy, f_sh, INK, 27)
        slines = wrap(d, summary, f_sd, col_w)
        draw_lines(d, slines, x, yy, f_sd, INK, 21)
        if col == 0:
            d.line([(M + col_w + 12, row_top + row * 128),
                    (M + col_w + 12, row_top + row * 128 + 112)],
                   fill=(200, 196, 186), width=1)
    y = row_top + 2 * 128 + 2
    rule(d, M, W - M, y, 2)
    y += 12

    # ---- Cyclone strip ----
    f_ck = SANS_B(15)
    d.text((M, y), "WEATHER · BAY OF BENGAL", font=f_ck, fill=RED)
    y += 20
    f_ch = SERIF_B(22)
    d.text((M, y), "Cyclone Akvan may strengthen into a severe cyclonic storm",
           font=f_ch, fill=INK)
    y += 30
    f_cd = SANS(16)
    d.text((M, y), "The storm over the Bay of Bengal is forecast to intensify "
                    "as it tracks towards the coast.", font=f_cd, fill=INK)
    y += 28
    rule(d, M, W - M, y, 2)
    y += 12

    # ---- ALSO TODAY footer ----
    f_ft = SANS_B(17)
    bar_h = 30
    d.rectangle([M, y, W - M, y + bar_h], fill=RED)
    d.text((M + 10, y + 5), "ALSO TODAY", font=f_ft, fill=(255, 255, 255))
    y += bar_h + 10
    also = [
        ("CRICKET", "MS Dhoni retires from the IPL and will mentor "
                     "Chennai Super Kings."),
        ("INDIA", "Amazon pledges $7bn for renewable energy in India."),
        ("TECH", "Baidu chief warns of an AI bubble ahead of APEC talks."),
        ("ASEAN", "Modi pushes India–ASEAN maritime cooperation at the "
                  "East Asia Summit."),
    ]
    f_ak = SANS_B(15)
    f_at = SANS(15)
    a_col_w = (CW - 24) // 2
    for i, (kick, text) in enumerate(also):
        col = i % 2
        row = i // 2
        x = M + col * (a_col_w + 24)
        yy = y + row * 44
        d.text((x, yy), kick + " — ", font=f_ak, fill=NAVY)
        kw = d.textlength(kick + " — ", font=f_ak)
        tlines = wrap(d, text, f_at, a_col_w - kw)
        # first line continues after kicker, rest on next lines
        if tlines:
            d.text((x + kw, yy), tlines[0], font=f_at, fill=INK)
            yy2 = yy + 19
            for extra in tlines[1:]:
                d.text((x, yy2), extra, font=f_at, fill=INK)
                yy2 += 19
    y += 2 * 44

    # ---- Footer line ----
    y += 6
    rule(d, M, W - M, y, 1)
    y += 8
    f_foot = SANS(13)
    foot = "THE WORLD — IN ONE IMAGE · All stories first reported on Wednesday, 18 November 2026"
    d.text(((W - d.textlength(foot, font=f_foot)) / 2, y), foot,
           font=f_foot, fill=GREY)
    y += 22
    assert y <= H - 8, f"layout overflow: final y={y}"

    img.save(out, "PNG", optimize=True)
    print(f"wrote {out} ({os.path.getsize(out)} bytes)")


if __name__ == "__main__":
    main()
