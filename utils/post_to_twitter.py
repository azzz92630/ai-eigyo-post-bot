# utils/post_to_twitter.py
import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

auth = tweepy.OAuth1UserHandler(
    os.getenv("TWITTER_API_KEY"),
    os.getenv("TWITTER_API_SECRET"),
    os.getenv("TWITTER_ACCESS_TOKEN"),
    os.getenv("TWITTER_ACCESS_SECRET")
)

api = tweepy.API(auth)

def post_tweet(text):
    try:
        api.update_status(text)
        print("✅ 投稿完了！")
    except Exception as e:
        print("⚠️ 投稿に失敗しました:", e)
