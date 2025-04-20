import requests
import json

# 発行されたWebhook URLをここに貼り付けてください
WEBHOOK_URL = "https://hooks.slack.com/services/XXXX/YYYY/ZZZZ"

def post_to_slack(message):
    payload = {"text": message}
    headers = {"Content-Type": "application/json"}

    response = requests.post(WEBHOOK_URL, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        print("✅ Slackへの投稿に成功しました。")
    else:
        print(f"⚠️ 投稿失敗: {response.status_code} - {response.text}")
