import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

with open("sources.txt", "r", encoding="utf-8") as f:
sources = [line.strip() for line in f if line.strip()]

message = "📢 Щоденний моніторинг грантів, конкурсів та стипендій\n\n"

for url in sources:
message += f"🔹 {url}\n"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(
url,
data={
"chat_id": CHAT_ID,
"text": message
}
)
