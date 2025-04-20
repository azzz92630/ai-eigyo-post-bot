import os
import requests
from dotenv import load_dotenv

load_dotenv()
WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def post_to_slack(text: str):
    if not WEBHOOK_URL:
        print("❌ Slack Webhook URL が設定されていません。")
        return

    payload = {"text": text}
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.status_code != 200:
            print(f"⚠️ Slack投稿失敗: {response.status_code} - {response.text}")
        else:
            print("✅ Slack投稿成功！")
    except Exception as e:
        print(f"⚠️ Slack送信中にエラーが発生しました: {e}")
