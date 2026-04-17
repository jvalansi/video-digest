# Video Digest — Sources

Generated: 2026-04-17. Refresh quarterly.

Sources are organized by category. Each entry includes the domain, fetch method, and feed URL where applicable.

---

## Social Signals (APIs)

These platforms surface trending/viral content via dedicated APIs — highest signal for "what people are talking about right now."

| Source | Method | Notes |
|--------|--------|-------|
| reddit.com | Reddit API | Top posts from subreddits below |
| news.ycombinator.com | HN Algolia API | `https://hn.algolia.com/api/v1/search?tags=front_page` |
| youtube.com | YouTube Data API | Trending videos by category |
| x.com / twitter | X API | Trending topics (rate-limited) |
| google.com | Google Trends API | Trending searches (`pytrends`) |
| wikipedia.org | Wikimedia API | Trending pages (`https://wikimedia.org/api/rest_v1/metrics/pageviews/top/...`) |
| github.com | GitHub Trending | `https://github.com/trending` (scrape) or `gh api` |
| producthunt.com | Product Hunt API | Featured products of the day |

### Reddit Subreddits

| Category | Subreddits |
|----------|-----------|
| AI / ML | r/MachineLearning, r/artificial, r/ChatGPT, r/ClaudeAI, r/LocalLLaMA |
| Tech | r/technology, r/programming, r/webdev, r/compsci |
| Science | r/science, r/Futurology, r/biology, r/Physics, r/longevity |
| News | r/worldnews, r/news, r/geopolitics |
| Finance | r/investing, r/wallstreetbets, r/Economics, r/stocks |
| Startups | r/startups, r/Entrepreneur, r/SideProject |
| Self-improvement | r/productivity, r/selfimprovement, r/LifeProTips |

---

## General News (RSS)

Top general news publishers by global traffic.

| Source | Domain | RSS Feed |
|--------|--------|----------|
| BBC News | bbc.com | `https://feeds.bbci.co.uk/news/rss.xml` |
| Reuters | reuters.com | `https://feeds.reuters.com/reuters/topNews` |
| Associated Press | apnews.com | `https://rsshub.app/apnews/topics/apf-topnews` |
| The Guardian | theguardian.com | `https://www.theguardian.com/world/rss` |
| New York Times | nytimes.com | `https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml` |
| Washington Post | washingtonpost.com | `https://feeds.washingtonpost.com/rss/world` |
| Yahoo News | yahoo.com | `https://news.yahoo.com/rss/` |
| MSN News | msn.com | `https://www.msn.com/en-us/news/rss` |
| Al Jazeera | aljazeera.com | `https://www.aljazeera.com/xml/rss/all.xml` |
| CNN | cnn.com | `http://rss.cnn.com/rss/edition.rss` |

---

## Tech News (RSS)

| Source | Domain | RSS Feed |
|--------|--------|----------|
| The Verge | theverge.com | `https://www.theverge.com/rss/index.xml` |
| TechCrunch | techcrunch.com | `https://techcrunch.com/feed/` |
| Ars Technica | arstechnica.com | `https://feeds.arstechnica.com/arstechnica/index` |
| Wired | wired.com | `https://www.wired.com/feed/rss` |
| MIT Tech Review | technologyreview.com | `https://www.technologyreview.com/feed/` |
| VentureBeat | venturebeat.com | `https://venturebeat.com/feed/` |
| Engadget | engadget.com | `https://www.engadget.com/rss.xml` |
| ZDNet | zdnet.com | `https://www.zdnet.com/news/rss.xml` |
| 9to5Mac | 9to5mac.com | `https://9to5mac.com/feed/` |
| The Information | theinformation.com | (paywalled — headlines only via scrape) |

---

## AI / ML (RSS + Blogs)

| Source | Domain | RSS Feed |
|--------|--------|----------|
| Anthropic Blog | anthropic.com | `https://www.anthropic.com/blog/rss` |
| OpenAI Blog | openai.com | `https://openai.com/blog/rss` |
| Google DeepMind | deepmind.google | `https://deepmind.google/blog/rss.xml` |
| Hugging Face Blog | huggingface.co | `https://huggingface.co/blog/feed.xml` |
| AI News | artificialintelligence-news.com | `https://www.artificialintelligence-news.com/feed/` |
| Papers With Code | paperswithcode.com | `https://paperswithcode.com/rss` |
| Import AI (newsletter) | jack-clark.net | `https://jack-clark.net/feed/` |
| The Batch (DeepLearning.AI) | deeplearning.ai | `https://www.deeplearning.ai/the-batch/feed/` |

---

## Science (RSS)

| Source | Domain | RSS Feed |
|--------|--------|----------|
| Nature | nature.com | `https://www.nature.com/nature.rss` |
| Science | science.org | `https://www.science.org/rss/news_current.xml` |
| Scientific American | scientificamerican.com | `https://www.scientificamerican.com/feed/rss/` |
| New Scientist | newscientist.com | `https://www.newscientist.com/feed/home/` |
| Phys.org | phys.org | `https://phys.org/rss-feed/` |
| ScienceDaily | sciencedaily.com | `https://www.sciencedaily.com/rss/all.xml` |

---

## Finance (RSS)

| Source | Domain | RSS Feed |
|--------|--------|----------|
| Bloomberg | bloomberg.com | `https://feeds.bloomberg.com/markets/news.rss` |
| Financial Times | ft.com | (paywalled — limited free feed) |
| Wall Street Journal | wsj.com | (paywalled) |
| CNBC | cnbc.com | `https://www.cnbc.com/id/100003114/device/rss/rss.html` |
| MarketWatch | marketwatch.com | `https://feeds.content.dowjones.io/public/rss/mw_topstories` |
| Seeking Alpha | seekingalpha.com | `https://seekingalpha.com/feed.xml` |
| Investopedia | investopedia.com | `https://www.investopedia.com/feedbuilder/feed/getfeed/?feedName=rss_headline` |

---

## Fetch Strategy

1. **Social signals first** — Reddit, HN, YouTube trending, and Google Trends give real-time signal.
2. **RSS feeds for depth** — Pull headlines from RSS; use LLM to score against interest profile.
3. **Skip paywalled sources** in automated pipeline unless headline-only feeds are available.
4. **Fallback** — If RSS fails, try common paths: `/feed`, `/rss`, `/atom.xml`, `/feed.xml`.

---

## Refresh Policy

- **Source list:** Refresh quarterly (re-run Cloudflare Radar top sites query).
- **Feed URLs:** Validate annually — feeds move/die.
- **Subreddits:** Review quarterly for relevance and new active communities.
