# makefun-news-image

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Amburadullzz/makefun-news-18nov/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Amburadullzz/makefun-news-18nov/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

Sum up 18 November's world news in one image

## The entry

`entry.png` is a 1024×1024 dark editorial poster for 18 November 2026. A large
`18 NOVEMBER 2026` header sits over the tagline `WORLD NEWS · ONE DAY`, and
below it seven stories are laid out as a 2×3 grid plus one full-width card.
Each card carries a coloured accent bar, a flat drawn icon, a region tag, a
bold headline and one line of detail: Middle East (US strikes Iran in the
Gulf), Diplomacy (Putin and Xi meet in Shenzhen), Asia-Pacific (Quad leaders
meet in Manila), United States (outages across US systems), Mongolia (President
Khurelsukh resigns), Europe (UK sanctions West Bank firms) and South Asia
(Cyclone Akvan and smog over Delhi). The copy is limited to what the day's wire
briefings reported.

    entry.png   the entry — 1024×1024 PNG, under 1 MiB
    main.ts     copies entry.png to $MAKEFUN_OUTPUT_DIR, or /output

`main.ts` runs on Node 22 with the standard library only (`node:fs`,
`node:path`), makes no network calls, and copies the bytes verbatim:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

<sub>Entered on [make.fun](https://make.fun/?ref=k2b4xjp7&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
