import requests
from bs4 import BeautifulSoup


ALLOW_KEYWORDS = {
    "МЕДІА": [
        "медіа",
        "журналіст",
        "EED",
        "IREX",
        "редакц",
        "newsroom",
        "media",
        "journalism",
        "eed",
        "irex",
        "internews",
        "інституційн",
        "спроможн",
        "організаційн",
        "media sustainability",
        "media viability",
        "independent media",
        "capacity building",
        "capacity development",
        "organizational development",
        "institutional support",
        "core support",
        "operating support",
        "operational support"
    ],

    "NGO": [
        "ГО",
        "ОГС",
        "громадянськ",
        "Єднання",
        "організаці",
        "інституційн",
        "ГО",
        "ОГС",
        "громадянськ",
        "Єднання",
        "організаці",
        "інституційн",
        "спроможн",
        "організаційний розвиток",
        "організаційного розвитку",
        "capacity building",
        "capacity development",
        "institutional support",
        "institutional strengthening",
        "core support",
        "operating support",
        "operational support"
    ],

    "ГРОМАДИ": [
        "громад",
        "відновлення",
        "SECO"
    ]
}


BLOCK_KEYWORDS = [
    "бізнес",
    "startup",
    "стартап",
    "агро",
    "фермер",
    "Horizon",
    "Erasmus",
    "COST",
    "лазер",
    "robot",
    "AI",
    "дрон",
    "водень",
    "ветеран",
    "стипендія",
    "науков",
    "дослід",
    "culture helps solidarity",
    "тисячовесна",
    "life 2026"
    "угода",
    "конфіденційність",
    "користувача",
    "некомерційні організації",
    "горизонт європа",
    "seeds of bravery",
    "зміцнення демократії",
    "стійкість демократії",
    "стипендії",
    "компаній",
    "компанії"
]


def get_category(title):

    title_lower = title.lower()

    for category, keywords in ALLOW_KEYWORDS.items():

        for keyword in keywords:

            if keyword.lower() in title_lower:
                return category

    return None


def get_grants():

    url = "https://getgrant.ua/grants-and-funding/"

    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30
    )

    soup = BeautifulSoup(response.text, "html.parser")

    grants = []

    seen_titles = set()

    for link in soup.find_all("a", href=True):

        title = link.get_text(" ", strip=True)

        if len(title) < 15:
            continue

        title_lower = title.lower()

        if any(word.lower() in title_lower for word in BLOCK_KEYWORDS):
            continue

        category = get_category(title)

        if not category:
            continue

        if title in seen_titles:
            continue

        seen_titles.add(title)

        grants.append({
            "title": title,
            "url": link["href"],
            "category": category
        })

    print(f"GETGRANT знайдено: {len(grants)}")

    return grants
