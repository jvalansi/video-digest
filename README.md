# Trend Digest

A system that discovers trending topics across the web, curates them against a personal interest profile, and delivers them in configurable formats.

---

## Pipeline

```
Source Discovery → Curation & Scoring → Delivery
```

### Phase 1 — Source Discovery

Rather than hardcoding sources heuristically, we use traffic data to discover the most popular content publishers per category.

**Step 1 — Discover top sites per category**

Use **Cloudflare Radar API** to get the top-ranked domains per category:
- `GET /radar/ranking/top?rankingType=popular&limit=50`
- Categories: News & Media, Technology, Science, Finance, Politics
- Run periodically (weekly or monthly) to keep source list fresh

Also use `trending_rise` to catch domains with sudden traffic spikes — a leading indicator.

**Step 2 — Route each domain to the right fetcher**

Known platforms → dedicated API/feed (see source files below).
Unknown publishers → auto-discover RSS (`/feed`, `/rss`, `/atom.xml`, etc.).

**Step 3 — Normalize to common format**
```json
{ "title": "...", "summary": "...", "url": "...", "source": "...", "category": "...", "fetched_at": "..." }
```

### Phase 2 — Curation & Scoring

Use Claude to:
1. Deduplicate overlapping stories across sources
2. Score each topic against the interest profile below
3. Select top N topics per day (e.g. 5–10)

### Phase 3 — Delivery

Options (not mutually exclusive):
- Slack post (to `#proj-trend-digest`)
- Newsletter / email
- Video (ElevenLabs TTS + Pexels b-roll + moviepy)
- Audio / podcast
- Web page

---

## Interest Profile & Sources

Each interest area has its own source file:

| Interest | Sources |
|---|---|
| Tech | [sources/tech.md](sources/tech.md) |
| AI / ML | [sources/ai-ml.md](sources/ai-ml.md) |
| Science | [sources/science.md](sources/science.md) |
| Finance | [sources/finance.md](sources/finance.md) |
| Geopolitics | [sources/geopolitics.md](sources/geopolitics.md) |
| Startups | [sources/startups.md](sources/startups.md) |
| Self-improvement | [sources/self-improvement.md](sources/self-improvement.md) |

---

## Implementation Order

1. Source discovery — Cloudflare Radar top sites per category → filter publishers → find RSS feeds
2. Headline fetcher — pull latest headlines from discovered RSS feeds, output ranked list
3. Curation layer — Claude scoring against interest profile
4. Script generator — Claude writes narration
5. TTS — ElevenLabs API
6. Video assembly — moviepy + Pexels b-roll
7. Scheduler — daily cron job
8. Slack delivery — post to channel

---

## Notes

- Cloudflare Radar API token available (free tier)
- Reddit tool at `/home/ubuntu/reddit-tool/`
- Validation tool (HN, Google Trends, Product Hunt, Reddit) at `/home/ubuntu/validation-tool/`
