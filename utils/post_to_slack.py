import os
import requests

# GitHub Actions環境ではdotenv不要ですが、ローカル動作も考慮して記述
from dotenv import load_dotenv
load_dotenv()

WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def post_to_slack(text):
    if not WEBHOOK_URL:
        print("❌ Slack Webhook URL が設定されていません。SLACK_WEBHOOK_URL を確認してください。")
        return

    payload = {"text": text}

    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.status_code == 200:
            print("✅ Slack投稿成功！")
        else:
            print(f"⚠️ Slack投稿失敗: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"🚨 Slack送信中にエラーが発生しました: {e}")
