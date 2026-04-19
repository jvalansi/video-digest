# Trend Digest

A system that discovers trending topics across the web, curates them against a personal interest profile, and delivers them in configurable formats.

---

## What It Does

- **Discover** — pull trending content from high-signal sources (social platforms, RSS feeds, APIs)
- **Curate** — deduplicate, score against interest profile, select top N topics per day
- **Deliver** — serve as Slack digest, newsletter, video, audio, or web page (video is one option, not the primary goal)

---

## Source Research

### Where developers actually get their news
From the Stack Overflow 2025 Developer Survey (65k+ respondents):

| Platform | Usage |
|---|---|
| Stack Overflow | 84% |
| GitHub | 67% |
| YouTube | 61% |
| Reddit | 54% |
| Stack Exchange | 47% |
| Discord | 39% |
| LinkedIn | 37% |
| Medium | 29% |
| Hacker News | 20% |
| X / Twitter | 17% |
| Slack (public) | 16% |
| Dev.to | 11% |
| Bluesky | 11% |
| Twitch | 9% |
| Substack | 7% |

Key insight: YouTube and Reddit both significantly outrank Hacker News among developers. HN is high-quality but niche (~20%).

### API availability

| Source | Status | Notes |
|---|---|---|
| Hacker News | ✅ Ready | Free, no auth — Firebase REST API |
| YouTube | ✅ Ready | API key configured |
| GitHub | ✅ Ready | No auth needed for public data |
| Stack Overflow | ✅ Ready | Public API, no key needed for read |
| Stack Exchange | ✅ Ready | Same API as Stack Overflow |
| Dev.to | ✅ Ready | Free public API, no auth needed |
| Bluesky | ✅ Ready | AT Protocol API, no auth for public feeds |
| Discord | ⚠️ Limited | API is for bot/server interaction, not public content feeds |
| Reddit | ⚠️ Blocked | AWS IPs blocked; needs proxy or approved credentials |
| Substack | ⚠️ Limited | No official API; RSS feeds available per publication |
| Twitch | ⚠️ Limited | API exists but not relevant for tech news content |
| Medium | ❌ | No useful public API |
| LinkedIn | ❌ | Very restricted |
| X / Twitter | ❌ | Paid API only |
| Slack (public) | ❌ | No public content API |

### Reddit notes
Reddit blocks requests from cloud/AWS IPs regardless of auth method.
The `.env` includes a `REDDIT_PROXY_URL` (webshare.io residential proxy) that may bypass this.
PRAW-based tool at `/home/ubuntu/reddit-tool/` — needs `REDDIT_CLIENT_ID` + `REDDIT_CLIENT_SECRET` once approved.

---

## Interest Profile

Topics to score against (to be refined over time):

- AI / ML research and tools
- Geopolitics and global news
- Science (longevity, physics, biology)
- Startups and tech products
- Self-improvement / productivity
- Finance and markets

---

## Delivery Options

- Slack post (to `#proj-trend-digest`)
- Newsletter / email
- Video (ElevenLabs TTS + Pexels b-roll + moviepy)
- Audio / podcast
- Web page

---

## See Also

- `PLAN.md` — detailed pipeline and implementation plan
- `sources.md` — full source list with RSS feeds and API endpoints
