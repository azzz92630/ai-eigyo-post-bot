import feedparser
from langdetect import detect
from googletrans import Translator

rss_feeds = [
    "https://www.artificialintelligence-news.com/feed/",
    "https://venturebeat.com/category/ai/feed/",
    "https://xtech.nikkei.com/rss/ai.rdf",
    "https://rss.itmedia.co.jp/rss/2.0/news_bursts.xml"
]

translator = Translator()

def get_translated_articles(limit_per_feed=1):
    articles = []

    for url in rss_feeds:
        try:
            feed = feedparser.parse(url)
            entries = feed.entries[:limit_per_feed]

            for entry in entries:
                title = entry.title
                link = entry.link

                lang = detect(title)
                if lang == "en":
                    title = translator.translate(title, src="en", dest="ja").text

                articles.append({
                    "title": title.strip(),
                    "link": link.strip()
                })
        except Exception as e:
            print(f"❌ フィード取得エラー: {url} / {e}")

    return articles
