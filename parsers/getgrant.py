import requests
from bs4 import BeautifulSoup


def get_grants():

    url = "https://getgrant.ua/grants-and-funding/"

    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30
    )

    print(response.status_code)
    print(response.text[:1000])

    soup = BeautifulSoup(response.text, "html.parser")

    grants = []

   for title in soup.find_all():
    text = title.get_text(strip=True)

    if len(text) > 30:
        print(text[:100])

        text = title.get_text(strip=True)

        if len(text) > 20:
            grants.append(text)

    print("GETGRANT:")
    print(grants)
    print(f"Знайдено: {len(grants)}")

    return sorted(set(grants))
