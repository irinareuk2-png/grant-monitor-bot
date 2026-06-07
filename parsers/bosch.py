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

    print(text[:10000])

    return []
