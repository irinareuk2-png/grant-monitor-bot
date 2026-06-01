import requests
from bs4 import BeautifulSoup
import re


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

            grant_title = text.split("access_time")[0].strip()

            if len(grant_title) > 15:
                grants.append(grant_title)

    grants = sorted(set(grants))

    print("Гранти:")
    for grant in grants[:20]:
        print(grant)

    print(f"GETGRANT знайдено: {len(grants)}")

    return grants
