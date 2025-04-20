from utils.fetch_news import get_latest_articles
from utils.generate_summary import summarize_article
from utils.post_to_slack import post_to_slack

print("スクリプトが起動しました！")

articles = get_latest_articles(limit=1)
hashtags = "#営業女子 #AI営業 #生成AI活用"

for article in articles:
    title = article["title"]
    link = article["link"]
    post_text = summarize_article(title, link)
    full_text = f"{post_text}\n\n{hashtags}"
    post_to_slack(full_text)

# main.py に以下を追加して確認

print("🔍 Slack投稿処理に入ります")

# Slackへ送信（テキスト確認）
print(f"📦 投稿するテキスト: {full_text}")

post_to_slack(full_text)

print("✅ Slack投稿処理が完了しました")
