# main.py
from utils.fetch_news import get_translated_articles
from utils.generate_summary import summarize_article
from utils.post_to_slack import post_to_slack

print("🔧 スクリプトが起動いたしました！")

articles = get_translated_articles()

if not articles:
    print("⚠️ 記事が見つかりませんでした。")
else:
    print("📚 取得した記事一覧:")
    for article in articles:
        print(f"- {article['title']}\n  {article['link']}")

    first_article = articles[0]
    full_text = summarize_article(url=first_article["link"])  # URLを明示的に渡す

    text = (
        f"営業マン必見の📣 生成AIで業務効率化⚡\n"
        f"📰 {first_article['title']}\n"
        f"🔗 {first_article['link']}\n\n"
        f"{full_text}\n"
        f"\n#営業女子 #AI営業 #生成AI活用"
    )

    print("📤 Slack投稿処理に入ります")
    post_to_slack(text)
    print("✅ Slack投稿成功！")
