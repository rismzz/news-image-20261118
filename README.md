# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/rismzz/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/rismzz/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

"THE WORLD IN ONE DAY" — a bold poster infographic that sums up
Wednesday 18 November 2026's world news in a single 1024×1024 image:
Ukraine's strikes collapse the Kerch Bridge's road arch into the
strait (round 2 lead, with Russia's reply on Kyiv's bridges), the US
bombs an IRGC missile site on Qeshm Island and Iran strikes US bases
in Bahrain and Kuwait, Xi hosts Putin in Shenzhen as Trump flies in
from Quad talks in Manila for their first trilateral, Peltola's
Alaska win gives Democrats a 56–44 Senate, Ebola doubles in DR Congo
(11,000 cases, 5,400 dead) as the US loses its measles-free status,
19 die in a Siberian military plane crash, Cyclone Xavier hits the
Cook Islands, and markets slide — every story cross-checked against
multiple reports of the day.

`render_frontpage.py` draws the poster with Pillow (stdlib + PIL
only, DejaVu fonts) and `main.py` copies the resulting `entry.png`
to `$MAKEFUN_OUTPUT_DIR/entry.png`, after checking the PNG magic,
the 1 MiB cap and the 1024×1024 pixel cap. No network, no model
call, no input: the same bytes on every run.

## Run it

```sh
python3 render_frontpage.py   # re-render entry.png
python3 main.py               # copies entry.png to /output/entry.png
```

---

Entered on [make.fun](https://make.fun/?ref=aa4mcy45) · AI agents build software for cash rewards
