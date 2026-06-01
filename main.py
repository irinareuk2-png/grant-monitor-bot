import os
import requests

from grant_parser import get_grants

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

current_grants = get_grants()

try:
    with open("seen.txt", "r", encoding="utf-8") as f:
        seen = set(line.strip() for line in f if line.strip())
except FileNotFoundError:
    seen = set()

new_grants = []

for grant in current_grants:
    if grant not in seen:
        new_grants.append(grant)

if new_grants:

    message = "🆕 Нові грантові можливості (GetGrant)\n\n"

    for grant in new_grants:
        message += f"• {grant}\n"

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": message
        }
    )

    with open("seen.txt", "a", encoding="utf-8") as f:
        for grant in new_grants:
            f.write(grant + "\n")

else:

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": "✅ Сьогодні нових можливостей не знайдено"
        }
    )
