# utils/posted_log.py
import json
import os

POSTED_LOG_PATH = "posted_articles.json"

def load_posted_links():
    if not os.path.exists(POSTED_LOG_PATH):
        return set()
    with open(POSTED_LOG_PATH, "r") as f:
        return set(json.load(f))

def save_posted_link(link):
    posted = load_posted_links()
    posted.add(link)
    with open(POSTED_LOG_PATH, "w") as f:
        json.dump(list(posted), f, ensure_ascii=False, indent=2)
