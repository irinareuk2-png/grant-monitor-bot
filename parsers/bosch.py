import requests
from bs4 import BeautifulSoup

def get_bosch():

    url = "https://www.bosch-stiftung.de/en/news/open-calls"

    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30
    )

    soup = BeautifulSoup(response.text, "html.parser")

    text = soup.get_text(" ", strip=True)

    if "There are currently no open calls" in text:
        print("BOSCH: відкритих конкурсів немає")
        return []

    print("BOSCH: знайдено відкритий конкурс")

    return [{
        "title": "Bosch Foundation Open Call",
        "url": url,
        "category": "NGO",
        "deadline": "Невідомо"
    }]
