import os
from utils.fetch_news import get_latest_articles
from utils.generate_summary import summarize_article
from utils.post_to_slack import post_to_slack
from dotenv import load_dotenv

# .envの読み込み（ローカル実行用、GitHub Actionsでは不要）
load_dotenv()

print("📦 スクリプトが起動しました！")

# 1. ニュースを取得
articles = get_latest_articles()

# ログに記事を出力（デバッグ用）
print("📰 取得した記事一覧:")
for a in articles:
    print(f"- {a['title']} / {a['link']}")

# 2. 要約生成
full_text = summarize_article(articles)

# 3. 投稿内容を表示して確認
print(f"📨 投稿するテキスト: {full_text}")
print("🔔 Slack投稿処理に入ります")

# 4. Slackへ投稿
post_to_slack(full_text)
