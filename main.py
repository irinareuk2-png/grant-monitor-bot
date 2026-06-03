import os
import requests

from parsers.getgrant import get_grants

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def load_seen():

try:
    with open("seen.txt", "r", encoding="utf-8") as f:
        return set(
            line.strip()
            for line in f
            if line.strip()
        )

except FileNotFoundError:
    return set()

def save_seen(data):

with open("seen.txt", "w", encoding="utf-8") as f:
    for item in sorted(data):
        f.write(item + "\n")

grants = get_grants()

seen = load_seen()

current = set()

for item in grants:
current.add(item["url"])

new_urls = current - seen

new_grants = [
item
for item in grants
if item["url"] in new_urls
]

if new_grants:

message = "🆕 Нові можливості\n\n"

categories = {
    "МЕДІА": [],
    "NGO": [],
    "ГРОМАДИ": []
}

for item in new_grants:
    categories[item["category"]].append(item)

for category, items in categories.items():

    if not items:
        continue

    message += f"📌 {category}\n\n"

    for item in items:

        message += (
            f"• {item['title']}\n"
            f"🔗 {item['url']}\n\n"
        )

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": message[:4000]
    }
)


save_seen(current)
