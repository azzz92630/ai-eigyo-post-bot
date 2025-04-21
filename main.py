# main.py
from utils.fetch_news import get_translated_articles
from utils.generate_summary import summarize_article
from utils.post_to_slack import post_to_slack
from utils.posted_log import load_posted_links, save_posted_link


print("🔧 スクリプトが起動いたしました！")

articles = get_translated_articles()
posted_links = load_posted_links()
articles = [a for a in articles if a["link"] not in posted_links]


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
    save_posted_link(first_article["link"])

