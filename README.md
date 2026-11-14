# Fab Rides website

Static site for [fab-rides.co.uk](https://fab-rides.co.uk), published by Cloudflare Pages.

- Content: `tools/build.py` → run `python3 tools/build.py` → output in `site/`
- Style: `site/assets/site.css`
- Health check: `python3 tools/check.py`
- Rules for Claude: `CLAUDE.md`

**Cloudflare Pages settings:** framework preset *None*, build command *(empty)*, build output directory `site`.
