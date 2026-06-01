import requests
from bs4 import BeautifulSoup

URL = "https://getgrant.ua/grants-and-funding/"

def get_grants():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(URL, headers=headers, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    grants = []

    for title in soup.find_all(["h2", "h3"]):
        text = title.get_text(strip=True)

        if len(text) > 20:
            grants.append(text)

    return list(set(grants))
