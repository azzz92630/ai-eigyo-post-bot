import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

def summarize_article(title, url):
    prompt = (
        f"↓以下は生成AIに関する記事のタイトルです。\n"
        f"『{title}』\n"
        f"これをもとに、営業職向けのX（旧Twitter）投稿を140文字以内で作成してください。\n"
        f"カジュアルで親しみやすく、記事URL（{url}）も最後に含めてください。"
    )
    response = model.generate_content(prompt)
    return response.text.strip()
