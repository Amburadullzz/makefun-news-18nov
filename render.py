#!/usr/bin/env python3
"""Draw the one-image summary of Wednesday 18 November 2026."""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (11, 18, 32)
CARD = (18, 28, 46)
EDGE = (38, 54, 80)
WHITE = (245, 248, 252)
MUTED = (168, 184, 208)
ACCENT = (96, 165, 250)
RED = (239, 68, 68)
GOLD = (245, 196, 81)
ORANGE = (249, 115, 22)
CYAN = (56, 189, 248)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def rrect(d, box, r, fill, outline=None, width=1):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)


def text_fit(d, xy, s, f, fill, maxw):
    """Draw s, shrinking the font until it fits maxw."""
    size = f.size
    while size > 10:
        f2 = font(BOLD if "Bold" in str(f.path) else REG, size)
        if d.textlength(s, font=f2) <= maxw:
            break
        size -= 1
    d.text(xy, s, font=f2, fill=fill)
    return f2


def icon_summit(d, x, y):
    """Three flagpoles: US, China, Russia."""
    flags = [
        ("us", x + 14),
        ("cn", x + 50),
        ("ru", x + 86),
    ]
    for kind, px in flags:
        d.rectangle([px, y + 14, px + 3, y + 104], fill=(120, 134, 158))
        if kind == "us":
            d.rectangle([px + 3, y + 18, px + 33, y + 46], fill=(255, 255, 255))
            for i in range(4):
                d.rectangle([px + 3, y + 18 + i * 7, px + 33, y + 21 + i * 7], fill=RED)
            d.rectangle([px + 3, y + 18, px + 15, y + 32], fill=(37, 64, 143))
        elif kind == "cn":
            d.rectangle([px + 3, y + 18, px + 33, y + 46], fill=(206, 17, 38))
            d.ellipse([px + 7, y + 22, px + 15, y + 30], fill=(255, 214, 0))
        else:
            d.rectangle([px + 3, y + 18, px + 33, y + 46], fill=(255, 255, 255))
            d.rectangle([px + 3, y + 27, px + 33, y + 36], fill=(0, 57, 166))
            d.rectangle([px + 3, y + 36, px + 33, y + 46], fill=(213, 43, 30))


def icon_hormuz(d, x, y):
    """Tanker on the strait with an incoming missile."""
    d.rectangle([x + 6, y + 78, x + 112, y + 92], fill=(30, 64, 108))
    d.polygon([(x + 6, y + 92), (x + 112, y + 92), (x + 100, y + 104), (x + 18, y + 104)],
              fill=(148, 163, 184))
    d.rectangle([x + 30, y + 62, x + 90, y + 78], fill=(203, 213, 225))
    d.rectangle([x + 66, y + 48, x + 84, y + 62], fill=(226, 232, 240))
    d.line([(x + 10, y + 22), (x + 62, y + 56)], fill=ORANGE, width=6)
    d.polygon([(x + 6, y + 20), (x + 26, y + 22), (x + 12, y + 34)], fill=ORANGE)
    for i in range(3):
        d.arc([x + 20 + i * 4, y + 40, x + 60 + i * 4, y + 70], 200, 260, fill=(251, 146, 60), width=3)


def icon_bridge(d, x, y):
    """Truss bridge over water with a blast at its centre."""
    d.rectangle([x + 8, y + 96, x + 112, y + 104], fill=(30, 64, 108))
    d.line([(x + 6, y + 78), (x + 114, y + 78)], fill=(203, 213, 225), width=6)
    for tx in (x + 26, x + 86):
        d.rectangle([tx, y + 40, tx + 8, y + 96], fill=(148, 163, 184))
        d.line([(tx + 4, y + 42), (x + 58, y + 78)], fill=(148, 163, 184), width=3)
        d.line([(tx + 4, y + 42), (x + 58, y + 40)], fill=(148, 163, 184), width=3)
    d.polygon([(x + 58, y + 18), (x + 74, y + 44), (x + 66, y + 62), (x + 48, y + 60),
               (x + 42, y + 40)], fill=ORANGE)
    d.polygon([(x + 58, y + 30), (x + 66, y + 48), (x + 54, y + 52)], fill=(253, 224, 71))


def icon_voyager(d, x, y):
    """The probe, its trail and a far star."""
    d.ellipse([x + 26, y + 34, x + 96, y + 96], outline=(203, 213, 225), width=4)
    d.line([(x + 61, y + 30), (x + 61, y + 100)], fill=(203, 213, 225), width=3)
    d.ellipse([x + 40, y + 48, x + 82, y + 82], outline=(148, 163, 184), width=3)
    d.line([(x + 61, y + 66), (x + 96, y + 78)], fill=(148, 163, 184), width=4)
    for i in range(6):
        d.ellipse([x + 4 + i * 8, y + 100 - i * 3, x + 7 + i * 8, y + 103 - i * 3], fill=CYAN)
    d.ellipse([x + 4, y + 12, x + 14, y + 22], fill=(253, 224, 71))


def icon_cyclone(d, x, y):
    """A spiral storm over a coastline."""
    cx, cy = x + 60, y + 58
    for i, r in enumerate((46, 36, 26, 16, 7)):
        d.arc([cx - r, cy - r, cx + r, cy + r], 200 + i * 40, 340 + i * 40,
              fill=(226, 232, 240) if i % 2 == 0 else CYAN, width=5)
    d.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=(226, 232, 240))
    d.rectangle([x + 4, y + 100, x + 116, y + 106], fill=(30, 64, 108))


def icon_gold(d, x, y):
    """Two gold bars and a falling arrow."""
    for i, by in enumerate((y + 62, y + 84)):
        d.polygon([(x + 18, by), (x + 62, by), (x + 74, by + 14), (x + 30, by + 14)],
                  fill=GOLD if i == 0 else (214, 168, 60))
        d.polygon([(x + 18, by), (x + 30, by + 14), (x + 30, by + 18), (x + 18, by + 4)],
                  fill=(255, 226, 130))
    d.line([(x + 92, y + 22), (x + 92, y + 74)], fill=RED, width=6)
    d.polygon([(x + 80, y + 60), (x + 104, y + 60), (x + 92, y + 80)], fill=RED)


CARDS = [
    ("SHENZHEN SUMMIT", ["Xi welcomes Trump; Putin", "joins for Thursday's first", "three-way summit"], icon_summit),
    ("US STRIKES IRAN", ["Qeshm missile site struck;", "drones over Bahrain and", "Kuwait; Hormuz tense"], icon_hormuz),
    ("KERCH BRIDGE HIT", ["Ukraine hits the Crimea", "bridge; 72 killed in a", "double-tap strike"], icon_bridge),
    ("VOYAGER 1: LIGHT-DAY", ["Probe passes 16 billion", "miles out, the first a", "light-day from Earth"], icon_voyager),
    ("CYCLONE AKVAN", ["Storm aims at Andhra and", "Odisha; two lakh people", "moved from the coast"], icon_cyclone),
    ("GOLD BELOW $3,800", ["Lowest in over a year as", "the Fed signals more rate", "rises; silver slides too"], icon_gold),
]


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # header
    d.rectangle([0, 0, W, 8], fill=ACCENT)
    d.text((36, 40), "WEDNESDAY", font=font(BOLD, 26), fill=ACCENT)
    d.text((34, 74), "18 NOVEMBER 2026", font=font(BOLD, 76), fill=WHITE)
    d.text((36, 162), "THE WORLD IN ONE DAY", font=font(BOLD, 22), fill=MUTED)
    d.line([(36, 200), (W - 36, 200)], fill=EDGE, width=2)

    # cards
    cw, ch, gap = 470, 216, 18
    left = 32
    top = 214
    for i, (title, lines, icon) in enumerate(CARDS):
        col = i % 2
        row = i // 2
        x = left + col * (cw + gap)
        y = top + row * (ch + gap)
        rrect(d, [x, y, x + cw, y + ch], 18, CARD, EDGE, 2)
        icon(d, x + 26, y + 52)
        tf = font(BOLD, 30)
        tf = text_fit(d, (x + 152, y + 34), title, tf, WHITE, cw - 176)
        ty = y + 34 + tf.size + 12
        for line in lines:
            bf = text_fit(d, (x + 152, ty), line, font(REG, 21), MUTED, cw - 172)
            ty += 28

    # footer strip
    fy = top + 3 * (ch + gap) + 12
    rrect(d, [left, fy, W - left, fy + 66], 14, (16, 26, 42), EDGE, 2)
    d.text((left + 20, fy + 20), "Also today: Quad leaders meet in Manila, UK sanctions",
           font=font(REG, 20), fill=MUTED)
    d.text((left + 20, fy + 42), "settler firms, Israel's parliament turns on Netanyahu",
           font=font(REG, 20), fill=MUTED)

    img.save("entry.png", format="PNG", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
