# main.py

from utils.fetch_news import get_latest_articles
from utils.generate_summary import summarize_article
from utils.post_to_slack import post_to_slack

print("🛎️ スクリプトが起動いたしました！")

# 最新記事を取得
articles = get_latest_articles()

if not articles:
    print("⚠️ 記事が見つかりませんでした。")
else:
    # 最初の記事を対象にする
    first_article = articles[0]
    title_list = [first_article["title"]]
    url = first_article["link"]

    print("📚 取得した記事一覧:")
    for article in articles:
        print(f"- {article['title']}")

    # 要約を生成
    full_text = summarize_article(title_list, url)
    print(f"📝 投稿するテキスト:\n{full_text}")

    # Slackへ投稿
    print("🚀 Slack投稿処理に入ります")
    post_to_slack(full_text)
