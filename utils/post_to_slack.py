import os
import requests
from dotenv import load_dotenv
from utils.generate_summary import summarize_article  # ✅正しいモジュールに修正

load_dotenv()

WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def post_to_slack(text):
    payload = {"text": text}
    response = requests.post(WEBHOOK_URL, json=payload)
    if response.status_code == 200:
        print("✅ Slack投稿成功！")
    else:
        print(f"⚠️ Slack投稿失敗: {response.status_code} - {response.text}")
