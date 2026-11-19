#!/usr/bin/env python3
"""Round-4 renderer: a dense one-page broadsheet of Wednesday 18 November 2026.

Renders at 2x supersampling and downscales to a 1024x1024 PNG so the small
type stays crisp. Every story below was verified as reported on 18 Nov 2026
(see STATUS.md for the source list). Deterministic: fixed fonts, fixed data,
no randomness, no network.
"""
from PIL import Image, ImageDraw, ImageFont

S = 2  # supersampling factor
W = 1024 * S
H = 1024 * S

PAPER = (250, 248, 243)
INK = (18, 18, 18)
RED = (178, 26, 26)
GREY = (92, 90, 86)
HAIR = (203, 198, 188)
WHITE = (255, 255, 255)

FD = "/usr/share/fonts/truetype"
SANS = f"{FD}/liberation/LiberationSans-Regular.ttf"
SANSB = f"{FD}/liberation/LiberationSans-Bold.ttf"
SERIFB = f"{FD}/liberation/LiberationSerif-Bold.ttf"


def F(path, size):
    return ImageFont.truetype(path, int(size * S))


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)


def text_w(txt, font):
    return d.textlength(txt, font=font)


def wrap(txt, font, maxw):
    """Greedy word wrap; returns list of lines. Asserts no word overflows."""
    words = txt.split()
    lines, cur = [], ""
    for w_ in words:
        assert text_w(w_, font) <= maxw, f"word too wide: {w_!r}"
        t = (cur + " " + w_).strip()
        if text_w(t, font) <= maxw:
            cur = t
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def tracked(x, y, txt, font, fill, tracking):
    """Draw letter-spaced text starting at x; returns end x."""
    cx = x
    for ch in txt:
        d.text((cx, y), ch, font=font, fill=fill)
        cx += text_w(ch, font) + tracking
    return cx - tracking


def tracked_w(txt, font, tracking):
    return sum(text_w(c, font) for c in txt) + tracking * (len(txt) - 1)


def centered_tracked(y, txt, font, fill, tracking):
    x = (W - tracked_w(txt, font, tracking)) / 2
    tracked(x, y, txt, font, fill, tracking)


# ---------------------------------------------------------------- data
TIMELINE = [
    ("02:00", "BAHRAIN", "Iranian drones intercepted before dawn"),
    ("06:00", "KYIV", "141 drones overnight; 126 downed, six hurt in Dnipro"),
    ("08:00", "SHENZHEN", "Xi and Putin open talks at APEC"),
    ("11:00", "ODESA", "Russian strikes kill four, injure nine"),
    ("13:00", "SHENZHEN", "Trump lands; Xi greets him at the aircraft"),
    ("17:00", "WASHINGTON", "Crude stocks +3.4M barrels; oil slides"),
    ("19:00", "WASHINGTON", "Fed minutes back further rate hikes"),
    ("21:00", "NEW YORK", "Dow -1.11%, S&P -0.23%, Nasdaq +0.42%"),
    ("22:00", "NEW YORK", "Anthropic prices record $81.3B IPO"),
]

LEADS = [
    ("SHENZHEN SUMMIT",
     "Three presidents, one summit table",
     "Xi and Putin meet in Shenzhen; Trump flies in from the Quad in "
     "Manila for Thursday's first US-China-Russia trilateral \u2014 Ukraine, "
     "Iran and trade on the table."),
    ("GULF ESCALATION",
     "Iran and US trade blows across the Gulf",
     "US jets strike an IRGC missile site on Qeshm Island; Iran fires "
     "drones at US bases in Kuwait and Bahrain. Bahrain intercepts; "
     "Kuwait calls the blasts interceptions."),
    ("UKRAINE WAR",
     "Ukraine blows a span of the Crimean Bridge",
     "A road section of Russia's Kerch Bridge collapses after overnight "
     "strikes; the road stays shut, rail resumes. Russia hits Kyiv's "
     "Dnipro bridges in reply."),
]

COLS = [
    [("EUROPE & THE UKRAINE WAR", [
        ("Strikes kill four in Odesa",
         "Russia hits the port city repeatedly Wednesday morning; nine injured."),
        ("141 drones over Ukraine in a night",
         "Kyiv: 126 downed or suppressed by 08:00; six wounded in Dnipro."),
        ("Kyiv asks Ramstein for jets",
         "Ukraine seeks 12 fighters incl. French Mirages; Canada adds air defence."),
        ("Drones hit Russian refineries",
         "Ukraine renews strikes on oil plants in the south that fund the war."),
        ("EU floats \u20ac45bn Ukraine loan",
         "Brussels proposes up to \u20ac45 billion for 2027 as allies meet in Berlin."),
        ("Slovaks protest Fico's Russia line",
         "Thousands rally against the government's Moscow and Ukraine stance."),
        ("Italy passes antisemitism law",
         "Backers: overdue protection. Critics: it may chill criticism of Israel."),
        ("EU moves on Temu",
         "Enforcement action over illegal products sold on the marketplace."),
    ])],
    [("MIDDLE EAST", [
        ("Tanker hit in Strait of Hormuz",
         "ADNOC vessel struck by a projectile: one crew missing, 11 injured."),
        ("Saudis intercept Houthi missile",
         "Cruise missile aimed at the Riyadh region destroyed; no damage."),
        ("Tanks cross Gaza's Yellow Line",
         "Israeli forces push into central Gaza, a major move since the truce."),
        ("Peace board faults both sides",
         "Trump's board tells UN Israel and Hamas are failing the ceasefire."),
        ("950,000 Gazans on flood-prone land",
         "WHO: the displaced face a fourth winter in tents as aid lags."),
        ("UK, Australia sanction settlers",
         "London designates 8 firms; Canberra targets 3 people, 4 groups."),
     ]),
     ("ASIA-PACIFIC", [
        ("Quad meets in Manila",
         "First leader-level Quad in 2+ years; Trump unveils Philippines trade deal."),
        ("Canada and China cut tariffs",
         "Carney and Xi agree reductions as Ottawa diversifies from the US."),
        ("Bombers brush Japan and Taiwan",
         "Russian aircraft off Taiwan; Tokyo reports airspace violation off Fukuoka."),
     ])],
    [("AMERICAS", [
        ("Peltola flips Alaska: Senate 56-44",
         "AP calls it for the Democrat over Sullivan; first Alaska Native senator."),
        ("US loses measles-free status",
         "Elimination ends after 26 years as cases surge; Kennedy vows to regain it."),
        ("Outages probed, attack ruled out",
         "Microsoft 365, FAA, NSA failures probed; Rubio sees no cyberattack."),
        ("27 years for Trump plotter",
         "Pakistani man sentenced over an Iran-linked plot to kill Trump."),
        ("Haiti signs El Salvador pact",
         "Anti-gang security deal formalised; UN counts 4,595 killed this year."),
        ("Rare contact in the Amazon",
         "An isolated Indigenous group emerges in Brazil, raising health alarms."),
     ]),
     ("AFRICA", [
        ("Ebola passes 11,000 cases in Congo",
         "DRC outbreak more than doubles; deaths top 5,400, response lags."),
        ("Ebola vaccines head to trials",
         "Two strain-specific candidates set for Phase 2 trials in the east."),
        ("Sudan army gains in West Kordofan",
         "Khartoum's forces advance on the RSF; civilians pay the toll."),
     ])],
]

STRIP = [
    ("SCIENCE \u00b7 CLIMATE \u00b7 TECH", [
        ("Anthropic prices biggest IPO ever",
         "$83/share, $81.3B raised \u2014 past SpaceX; trades Thu as ANT."),
        ("Nvidia's record $115.8B quarter",
         "Revenue doubles; shares fall 2.9% to $150.96 on AI jitters."),
        ("COP31 deadlocked in Antalya",
         "Phase-out draft stalls; EU attacks text, poor nations want finance."),
        ("Cat-5 Xavier batters Cook Islands",
         "Pukapuka, Nassau under gale warnings; winds 220 km/h."),
        ("NZ tsunami warning lifted",
         "Alert withdrawn after offshore activity off North Island."),
        ("Criminal case in An-12 crash",
         "Russia opens case over Siberia crash; all 19 aboard died."),
    ]),
    ("SPORT", [
        ("England end Spain's 43-match run",
         "3-2 Nations League win in Madrid; Germany rout Dutch 5-0."),
        ("Duckett's 133 seals ODI series",
         "England beat Australia by 97 runs in Hobart decider, 2-1."),
        ("Alcaraz into ATP Finals semis",
         "Beats Medvedev 6-2, 6-4 in Turin despite knee concern."),
        ("Andreeva wins WTA Finals on debut",
         "Teenager beats Svitolina 7-5, 6-3 for first title."),
        ("Littler dumped out of Grand Slam",
         "Defending champion loses 10-8 to Wattimena."),
        ("Dhoni calls time on CSK career",
         "Chennai icon retires from playing for Super Kings."),
    ]),
]

TICKER_LINES = [
    ("MARKETS \u2014 WED CLOSE:  DOW 50,198 -1.11%  \u00b7  S&P 500 7,324 -0.23% "
     "(5TH LOSS IN A ROW)  \u00b7  NASDAQ 24,430 +0.42%  \u00b7  FTSE 100 -1.30%  \u00b7  DAX -1.19%"),
    ("BRENT $91.95  \u00b7  WTI $83.26  \u00b7  GOLD $3,742  \u00b7  US 10-YR 5.07%  \u00b7  VIX 24.56  \u00b7  "
     "ANTHROPIC IPO: $83 A SHARE, $81.3B RAISED \u2014 BIGGEST EVER"),
]

DATECHECK = ("DATE CHECK \u2014 every story on this page was reported on Wednesday "
             "18 November 2026. Sources: Reuters \u00b7 AP \u00b7 AFP \u00b7 BBC \u00b7 Yonhap \u00b7 "
             "Anadolu \u00b7 UN agencies \u00b7 national wires.")

# ---------------------------------------------------------------- layout
M = 20 * S
CW = W - 2 * M
y = 10 * S


def lh(font, factor=1.22):
    a, dd = font.getmetrics()
    return (a + dd) * factor


# kicker
f_kick = F(SANSB, 11)
centered_tracked(y, "50 STORIES \u00b7 SIX REGIONS \u00b7 ONE DAY \u2014 AS REPORTED ON THE DAY",
                 f_kick, RED, 2.2 * S)
y += lh(f_kick) + 2 * S

# title
f_title = F(SERIFB, 47)
tw = text_w("THE WORLD IN ONE DAY", f_title)
d.text(((W - tw) / 2, y), "THE WORLD IN ONE DAY", font=f_title, fill=INK)
y += lh(f_title, 1.05) + 4 * S

# date bar
f_date = F(SANSB, 22)
bar_h = 38 * S
d.rectangle([M, y, M + CW, y + bar_h], fill=INK)
dtxt = "WEDNESDAY \u00b7 18 NOVEMBER 2026"
dtw = text_w(dtxt, f_date)
d.text(((W - dtw) / 2, y + (bar_h - lh(f_date, 1.0)) / 2 - 2 * S), dtxt,
       font=f_date, fill=WHITE)
y += bar_h
d.rectangle([M, y, M + CW, y + 3 * S], fill=RED)
y += 3 * S + 6 * S

# timeline
f_tl_lab = F(SANSB, 12)
d.text((M, y), "THE DAY IN UTC", font=f_tl_lab, fill=INK)
lab_w = text_w("THE DAY IN UTC", f_tl_lab)
d.line([M + lab_w + 10 * S, y + lh(f_tl_lab) / 2, M + CW, y + lh(f_tl_lab) / 2],
       fill=HAIR, width=S)
y += lh(f_tl_lab) + 3 * S
f_time = F(SANSB, 14)
f_place = F(SANSB, 9)
f_tl = F(SANS, 10)
cell_w = CW / 9
tl_top = y
tl_max = 0
for i, (tm, pl, tx) in enumerate(TIMELINE):
    cx = M + i * cell_w + 5 * S
    cwid = cell_w - 9 * S
    yy = tl_top
    d.text((cx, yy), tm, font=f_time, fill=RED)
    yy += lh(f_time, 1.08)
    d.text((cx, yy), pl, font=f_place, fill=GREY)
    yy += lh(f_place, 1.12)
    for ln in wrap(tx, f_tl, cwid):
        d.text((cx, yy), ln, font=f_tl, fill=INK)
        yy += lh(f_tl, 1.14)
    tl_max = max(tl_max, yy - tl_top)
    if i:
        d.line([M + i * cell_w, tl_top + 2 * S, M + i * cell_w, tl_top + 58 * S],
               fill=HAIR, width=S)
y = tl_top + tl_max + 6 * S

# leads
d.rectangle([M, y, M + CW, y + 2.5 * S], fill=INK)
y += 7 * S
f_lead_k = F(SANSB, 10.5)
f_lead_h = F(SERIFB, 20)
f_lead_s = F(SANS, 11.9)
gut = 16 * S
colw = (CW - 2 * gut) / 3
lead_max = 0
for i, (kick, head, summ) in enumerate(LEADS):
    cx = M + i * (colw + gut)
    yy = y
    tracked(cx, yy, kick, f_lead_k, RED, 1.4 * S)
    yy += lh(f_lead_k) + 2 * S
    for ln in wrap(head, f_lead_h, colw):
        d.text((cx, yy), ln, font=f_lead_h, fill=INK)
        yy += lh(f_lead_h, 1.06)
    yy += 2 * S
    for ln in wrap(summ, f_lead_s, colw):
        d.text((cx, yy), ln, font=f_lead_s, fill=(40, 40, 40))
        yy += lh(f_lead_s, 1.12)
    lead_max = max(lead_max, yy - y)
    if i:
        vx = cx - gut / 2
        d.line([vx, y, vx, y + 104 * S], fill=HAIR, width=S)
y += lead_max + 7 * S

# main grid
f_sec = F(SANSB, 13.5)
f_h = F(SANSB, 13.2)
f_s = F(SANS, 11.0)
gut2 = 14 * S
gcolw = (CW - 2 * gut2) / 3
grid_top = y
grid_max = 0
for ci, sections in enumerate(COLS):
    cx = M + ci * (gcolw + gut2)
    yy = grid_top
    for si, (sec, items) in enumerate(sections):
        if si:
            yy += 6 * S
        d.rectangle([cx, yy, cx + gcolw, yy + 22 * S], fill=INK)
        d.text((cx + 7 * S, yy + 3.6 * S), sec, font=f_sec, fill=WHITE)
        yy += 22 * S + 5 * S
        for ii, (head, summ) in enumerate(items):
            for ln in wrap(head, f_h, gcolw):
                d.text((cx, yy), ln, font=f_h, fill=INK)
                yy += lh(f_h, 1.08)
            for ln in wrap(summ, f_s, gcolw):
                d.text((cx, yy), ln, font=f_s, fill=(52, 52, 52))
                yy += lh(f_s, 1.10)
            yy += 2.2 * S
            if ii < len(items) - 1:
                d.line([cx, yy - 1.6 * S, cx + gcolw, yy - 1.6 * S], fill=HAIR, width=S)
    grid_max = max(grid_max, yy - grid_top)
y = grid_top + grid_max + 5 * S

# bottom strip
f_sh = F(SANSB, 12.2)
f_ss = F(SANS, 10.6)
half = (CW - gut2) / 2
strip_top = y
strip_max = 0
for pi, (sec, items) in enumerate(STRIP):
    cx = M + pi * (half + gut2)
    yy = strip_top
    d.rectangle([cx, yy, cx + half, yy + 20 * S], fill=INK)
    d.text((cx + 7 * S, yy + 2.8 * S), sec, font=f_sh, fill=WHITE)
    yy += 20 * S + 4 * S
    sub = (half - 12 * S) / 2
    for r in range(3):
        ry = yy
        row_max = 0
        for c in range(2):
            head, summ = items[r * 2 + c]
            ix = cx + c * (sub + 12 * S)
            iy = ry
            for ln in wrap(head, f_sh, sub):
                d.text((ix, iy), ln, font=f_sh, fill=INK)
                iy += lh(f_sh, 1.08)
            for ln in wrap(summ, f_ss, sub):
                d.text((ix, iy), ln, font=f_ss, fill=(52, 52, 52))
                iy += lh(f_ss, 1.10)
            row_max = max(row_max, iy - ry)
        yy = ry + row_max + 3 * S
    strip_max = max(strip_max, yy - strip_top)
y = strip_top + strip_max + 4 * S

# ticker (two-line markets band)
f_tick = F(SANSB, 11.6)
tick_h = 42 * S
d.rectangle([M, y, M + CW, y + tick_h], fill=INK)
for li, line in enumerate(TICKER_LINES):
    assert text_w(line, f_tick) <= CW - 16 * S, f"ticker line {li} too wide"
    d.text((M + 8 * S, y + 5.5 * S + li * lh(f_tick, 1.22)), line,
           font=f_tick, fill=WHITE)
y += tick_h + 5 * S

# date check
f_dc = F(SANSB, 11)
dcw = text_w(DATECHECK, f_dc)
assert dcw <= CW, "datecheck too wide"
d.text(((W - dcw) / 2, y), DATECHECK, font=f_dc, fill=RED)
y += lh(f_dc, 1.05)

print(f"content bottom: {y / S:.1f}px of 1024")
assert y <= H - 6 * S, "OVERFLOW: content exceeds canvas"

img = img.resize((1024, 1024), Image.LANCZOS)
img.save("/tmp/broadsheet.png")
print("saved /tmp/broadsheet.png")
