import feedparser

FEED_URL = "https://www.espn.com/espn/rss/nba/news"
feed = feedparser.parse(FEED_URL)

print("🏀 今日 NBA 新聞：")
for entry in feed.entries[:5]:
    print(f"【{entry.title}】")
    print(entry.link)
    print()
