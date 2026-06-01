import os
import requests
from bs4 import BeautifulSoup

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

URL = "https://getgrant.ua/grants-and-funding/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers, timeout=30)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all(["h2", "h3"])

message = "📢 Нові грантові можливості (GetGrant)\n\n"

found = set()

for title in titles:
    text = title.get_text(strip=True)

    if len(text) > 20 and text not in found:
        found.add(text)
        message += f"🔹 {text}\n"

        if len(found) >= 15:
            break

telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(
    telegram_url,
    data={
        "chat_id": CHAT_ID,
        "text": message[:4000]
    }
)
