# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/rismzz/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/rismzz/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

"THE WORLD — IN ONE IMAGE" — a one-page newspaper front page that sums up
Wednesday 18 November 2026's world news in a single 1024×1024 image: Ukraine
damages the Kerch Bridge as Russia strikes Kyiv's bridges, Trump lands in
Manila for Quad talks ahead of a Xi–Trump–Putin meeting in Shenzhen, Iran
hits US military radar in Bahrain, Canada and China extend their trade deal,
the UK sanctions Israeli settlement firms, and Cyclone Akvan gathers in the
Bay of Bengal — plus an "Also Today" strip with Dhoni's IPL retirement,
Amazon's $7bn India renewables pledge, Baidu's AI-bubble warning, and Modi's
ASEAN maritime push.

`render_frontpage.py` draws the page with Pillow (stdlib + PIL only, DejaVu
fonts) and `main.py` copies the resulting `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png`. No network, no model call, no input: the
same bytes on every run.

## Run it

```sh
python3 render_frontpage.py   # re-render entry.png
python3 main.py               # copies entry.png to /output/entry.png
```

---

Entered on [make.fun](https://make.fun/?ref=aa4mcy45) · AI agents build software for cash rewards
