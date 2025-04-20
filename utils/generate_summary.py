from utils.fetch_news import get_latest_articles
from utils.generate_post import summarize_article
from utils.post_to_slack import post_to_slack  # 👈 TwitterではなくSlack用

print("スクリプトが起動しました！")

# 最新記事を取得（1件）
articles = get_latest_articles(limit=1)

# 固定のハッシュタグ
hashtags = "#営業女子 #AI営業 #生成AI活用"

# 投稿ループ
for article in articles:
    title = article["title"]
    link = article["link"]

    # Gemini等で生成した投稿文
    post_text = summarize_article(title, link)

    # ハッシュタグ付きで整形
    full_text = f"{post_text}\n\n{hashtags}"

    # Slackに投稿
    post_to_slack(full_text)
