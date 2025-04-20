# utils/fetch_news.py
import requests
from bs4 import BeautifulSoup

def get_latest_articles(limit=3):
    url = "https://news.google.com/rss/search?q=生成AI&hl=ja&gl=JP&ceid=JP:ja"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    items = soup.find_all("item")[:limit]
    articles = []

    for item in items:
        title_tag = item.find("title")
        link_tag = item.find("link")
    
        if title_tag and link_tag:
            articles.append({
                "title": title_tag.text,
                "link": link_tag.text
            })


    return articles
# updated for GitHub Actions fix
