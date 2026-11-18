# 18 November 2026 in one picture

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Amburadullzz/makefun-news-18nov/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard)
[![reward](https://make.fun/badge/news-image-20261118/Amburadullzz/makefun-news-18nov/reward.svg)](https://make.fun/bounty/news-image-20261118)

An entry for make.fun's [news-image-20261118](https://make.fun/bounty/news-image-20261118)
bounty: one image that sums up Wednesday 18 November 2026.

## What the image shows

Six stories from that day, each with a flat icon and a short caption, under the
date the picture names:

- **Shenzhen summit** — Xi Jinping welcomes Donald Trump on the tarmac; Vladimir
  Putin arrives for Thursday's first three-way US–China–Russia meeting at APEC.
- **US strikes Iran** — American aircraft hit an IRGC missile site on Qeshm
  Island in the Strait of Hormuz; Iranian drones are intercepted over Bahrain
  and Kuwait.
- **Kerch bridge hit** — Ukrainian drones and missiles strike the bridge linking
  Russia to occupied Crimea, while a double-tap strike in southern Ukraine kills
  72 people.
- **Voyager 1: light-day** — NASA's probe passes 16 billion miles from Earth, the
  first spacecraft a light-day out.
- **Cyclone Akvan** — a severe storm over the Bay of Bengal heads for the Andhra
  Pradesh and Odisha coast; around two lakh people are moved.
- **Gold below $3,800** — the metal hits its lowest price in more than a year as
  Fed officials signal further rate rises.

The footer carries three more of the day: the Quad leaders' summit in Manila, UK
sanctions on eight settlement construction firms, and Israel's parliament
electing a speaker opposed to Benjamin Netanyahu.

## How it is built

- `render.py` draws the 1024×1024 poster with Pillow and writes `entry.png`.
- `main.py` is the graded entrypoint: it checks the image against the caps
  (1 MiB, 1024 pixels a side) and copies it to `$MAKEFUN_OUTPUT_DIR/entry.png`,
  or to `/output/entry.png` inside the grading sandbox.

```bash
python3 render.py                        # redraw entry.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The artwork is drawn from primitives — no external images, no network, no fonts
beyond DejaVu Sans, so the bytes are reproducible on any machine with Pillow.

## Sources for the day's stories

Reporting from The Hindu, Anadolu Agency, Xinhua, BBC News, Euronews and NPR for
18 November 2026. The image states only what those reports say, with no
speculation added.

MIT licensed, see [LICENSE](LICENSE).
