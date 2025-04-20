import os
import requests
from dotenv import load_dotenv

load_dotenv()

def post_to_slack(text):
    url = os.getenv("SLACK_WEBHOOK_URL")
    payload = {"text": text}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("✅ Slack投稿成功")
    else:
        print("⚠️ Slack投稿失敗:", response.status_code, response.text)
