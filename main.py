from utils.fetch_news import get_latest_articles
from utils.generate_post import summarize_article
from utils.post_to_twitter import post_tweet

if __name__ == "__main__":
    print("✅ スクリプトが起動しました！")

    articles = get_latest_articles(limit=1)  # 1件だけ取得（朝・夕用）
    for article in articles:
        print(f"📰 {article['title']}")
        print(article["link"])
        tweet = summarize_article(article["title"], article["link"])
        print("💬 投稿文：")
        print(tweet)
        post_tweet(tweet)
