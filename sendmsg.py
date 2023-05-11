import requests
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN_TEL")
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

def send_text(telegram_id, text):
    params = {
        "chat_id": telegram_id,
        "text": text
    }
    response = requests.post(URL, params=params)
    if response.status_code != 200:
        print(f"Error sending message: {response.status_code} {response.reason}")

