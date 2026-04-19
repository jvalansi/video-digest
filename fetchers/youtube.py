#!/usr/bin/env python3
"""
YouTube fetcher — pulls trending or channel videos via YouTube Data API v3.

Usage:
  python fetchers/youtube.py [--mode trending|channels] [--category CATEGORY_ID] [--limit N]

Category IDs (for trending):
  28 = Science & Technology  26 = Howto & Style  25 = News & Politics
  24 = Entertainment         22 = People & Blogs

Output: JSON array of normalized items to stdout.
"""

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone

BASE = "https://www.googleapis.com/youtube/v3"

# Tech-focused channels to pull from in channels mode
DEFAULT_CHANNELS = [
    {"id": "UCsBjURrPoezykLs9EqgamOA", "name": "Fireship"},
    {"id": "UCXuqSBlHAE6Xw-yeJA0Tunw",  "name": "Linus Tech Tips"},
    {"id": "UCnUYZLuoy1rq1aVMwx4aTzw",  "name": "Theo (t3.gg)"},
    {"id": "UC8butISFwT-Wl7EV0hUK0BQ",  "name": "freeCodeCamp"},
    {"id": "UCVls1GmFKf6WlTraIb_IaJg",  "name": "Distro Tube"},
    {"id": "UCddiUEpeqJcYeBxX1IVBKvQ",  "name": "ThePrimeagen"},
]


def api_get(endpoint: str, params: dict) -> dict:
    api_key = os.environ.get("YOUTUBE_API_KEY")
    if not api_key:
        print("ERROR: YOUTUBE_API_KEY not set", file=sys.stderr)
        sys.exit(1)
    params["key"] = api_key
    url = f"{BASE}/{endpoint}?{urllib.parse.urlencode(params)}"
    with urllib.request.urlopen(url, timeout=10) as resp:
        return json.loads(resp.read())


def normalize(item: dict, source: str) -> dict:
    snippet = item.get("snippet", {})
    published = snippet.get("publishedAt")
    return {
        "title": snippet.get("title", "").strip(),
        "summary": snippet.get("description", "")[:500],
        "url": f"https://www.youtube.com/watch?v={item['id']['videoId'] if isinstance(item['id'], dict) else item['id']}",
        "source": f"YouTube / {source}",
        "category": "tech",
        "thumbnail": snippet.get("thumbnails", {}).get("medium", {}).get("url"),
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "published_at": published,
    }


def fetch_trending(category_id: str, limit: int) -> list[dict]:
    data = api_get("videos", {
        "part": "snippet",
        "chart": "mostPopular",
        "regionCode": "US",
        "videoCategoryId": category_id,
        "maxResults": min(limit, 50),
    })
    return [normalize({"id": item["id"], "snippet": item["snippet"]}, "Trending") for item in data.get("items", [])]


def fetch_channel(channel: dict, limit: int) -> list[dict]:
    data = api_get("search", {
        "part": "snippet",
        "channelId": channel["id"],
        "order": "date",
        "type": "video",
        "maxResults": min(limit, 50),
    })
    return [normalize(item, channel["name"]) for item in data.get("items", []) if item.get("id", {}).get("videoId")]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="trending", choices=["trending", "channels"])
    parser.add_argument("--category", default="28", help="YouTube category ID for trending mode (default: 28 = Science & Tech)")
    parser.add_argument("--limit", type=int, default=10, help="Max items per source (default: 10)")
    args = parser.parse_args()

    results = []

    if args.mode == "trending":
        print(f"  Fetching YouTube trending (category {args.category})...", file=sys.stderr)
        items = fetch_trending(args.category, args.limit)
        results.extend(items)
        print(f"  Got {len(items)} videos", file=sys.stderr)
    else:
        for channel in DEFAULT_CHANNELS:
            try:
                items = fetch_channel(channel, args.limit)
                results.extend(items)
                print(f"  {channel['name']}: {len(items)} videos", file=sys.stderr)
            except Exception as e:
                print(f"  {channel['name']}: ERROR — {e}", file=sys.stderr)

    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
