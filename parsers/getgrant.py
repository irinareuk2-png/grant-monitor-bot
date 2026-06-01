import requests
from bs4 import BeautifulSoup


def get_grants():

    url = "https://getgrant.ua/grants-and-funding/"

    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30
    )

    soup = BeautifulSoup(response.text, "html.parser")

    grants = []

    for title in soup.find_all():

        text = title.get_text(" ", strip=True)

        if "access_time" in text:
        print(text[:200])

    grants = sorted(list(set(grants)))

    print(f"GETGRANT знайдено: {len(grants)}")

    return grants
