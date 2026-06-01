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

        for item in data:

            f.write(item + "\n")


current = set(get_grants())

seen = load_seen()

new_items = current - seen

if new_items:

    message = "🆕 Нові грантові можливості\n\n"

    for item in sorted(new_items):

        message += f"• {item}\n"

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": message[:4000]
        }
    )

save_seen(current)
