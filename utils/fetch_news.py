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
        articles.append({
            "title": item.title.text,
            "link": item.link.text
        })

    return articles
