# Trend Digest

A system that discovers trending topics across the web, curates them against a personal interest profile, and delivers them in configurable formats.

---

## What It Does

- **Discover** — pull trending content from high-signal sources (social platforms, RSS feeds, APIs)
- **Curate** — deduplicate, score against interest profile, select top N topics per day
- **Deliver** — serve as Slack digest, newsletter, video, audio, or web page (video is one option, not the primary goal)

---

## Sources

From the Stack Overflow 2025 Developer Survey (65k+ respondents), with API availability:

| Platform | Developer Usage | API |
|---|---|---|
| Stack Overflow | 84% | ✅ Public API, no auth |
| GitHub | 67% | ✅ Public API, no auth |
| YouTube | 61% | ✅ API key configured |
| Reddit | 54% | ⚠️ AWS IPs blocked; needs proxy or credentials |
| Stack Exchange | 47% | ✅ Same API as Stack Overflow |
| Discord | 39% | ⚠️ API is for server bots, not public content feeds |
| LinkedIn | 37% | ❌ Very restricted |
| Medium | 29% | ❌ No public API |
| Hacker News | 20% | ✅ Free, no auth — Firebase REST API |
| X / Twitter | 17% | ⚠️ API available but expensive |
| Slack (public) | 16% | ❌ No public content API |
| Dev.to | 11% | ✅ Free public API, no auth |
| Bluesky | 11% | ✅ AT Protocol, no auth for public feeds |
| Twitch | 9% | ⚠️ API exists but not relevant for tech news |
| Substack | 7% | ⚠️ No official API; RSS feeds available per publication |

Key insight: YouTube and Reddit both significantly outrank Hacker News among developers. HN is high-quality but niche (~20%).

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
