import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

message = """
📢 Щоденний моніторинг грантів та конкурсів

Перевірити:

🔹 House of Europe
https://houseofeurope.org.ua/opportunities

🔹 ГУРТ
https://gurt.org.ua/news/grants/

🔹 Єднання
https://ednannia.ua/granty

🔹 УФСІ
https://ucf.in.ua

🔹 Creative Europe
https://creativeeurope.in.ua

🔹 UNDP Ukraine
https://www.undp.org/uk/ukraine

🔹 IWM
https://www.iwm.at

🔹 Інститут масової інформації
https://imi.org.ua
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)
