import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

def summarize_article(url: str) -> str:
    prompt = (
        f"以下のURLの記事内容を要約してください。\n"
        f"記事URL: {url}\n"
        f"\n140文字以内でSNS投稿に使える形でまとめてください。日本語で、営業女子にもわかりやすくお願いします。"
    )
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"⚠️ Geminiでの要約エラー: {e}")
        return "（要約できませんでした）"
