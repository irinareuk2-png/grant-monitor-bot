import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re


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
    "life 2026",
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
    "компанії",
    "аналіз грантодавця",
    "аналіз донора",
    "як отримати грант",
    "грантовий гід",
    "огляд програм",
    "підбірка",
    "можливостей",
    "дайджест"
    ]


def get_category(title):

    title_lower = title.lower()

    for category, keywords in ALLOW_KEYWORDS.items():

        for keyword in keywords:

            if keyword.lower() in title_lower:
                return category

    return None

MONTHS = {
    "січня": 1,
    "лютого": 2,
    "березня": 3,
    "квітня": 4,
    "травня": 5,
    "червня": 6,
    "липня": 7,
    "серпня": 8,
    "вересня": 9,
    "жовтня": 10,
    "листопада": 11,
    "грудня": 12
}


def parse_deadline(text):

    match = re.search(
        r"(\d{1,2})\s+(січня|лютого|березня|квітня|травня|червня|липня|серпня|вересня|жовтня|листопада|грудня)\s+(\d{4})",
        text.lower()
    )

    if not match:
        return None

    day = int(match.group(1))
    month = MONTHS[match.group(2)]
    year = int(match.group(3))

    return datetime(year, month, day)
    
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

        url = link["href"]

        deadline = None

        try:
        
            page = requests.get(
                url,
                headers={"User-Agent": "Mozilla/5.0"},
                timeout=30
            )
        
            page_soup = BeautifulSoup(
                page.text,
                "html.parser"
            )
        
            deadline = parse_deadline(
                page_soup.get_text(" ", strip=True)
            )
        
        except Exception:
            pass
        
        if deadline and deadline < datetime.today():
            continue
        
        if title in seen_titles:
            continue

        if "/grants-and-funding-tag/" in url:
            continue

        if "/grants-and-funding-category/" in url:
            continue
       
        seen_titles.add(title)
       
        grants.append({
            "title": title,
            "url": link["href"],
            "category": category,
            "deadline": (
            deadline.strftime("%d.%m.%Y")
            if deadline
            else "Невідомо"
            )
        })

    print(f"GETGRANT знайдено: {len(grants)}")

    return grants
