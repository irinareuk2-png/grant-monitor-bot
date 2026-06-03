import os
import requests

from parsers.getgrant import get_grants


BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


grants = get_grants()

if grants:

    message = "🆕 Нові можливості\n\n"

    categories = {
        "МЕДІА": [],
        "NGO": [],
        "ГРОМАДИ": []
    }

    for item in grants:
        categories[item["category"]].append(item)

    for category, items in categories.items():

        if not items:
            continue

        message += f"📌 {category}\n\n"

        for item in items[:10]:

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
