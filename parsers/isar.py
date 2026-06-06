import re
from datetime import datetime

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

import requests
from bs4 import BeautifulSoup

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

def get_isar():
    
    url = "https://ednannia.ua/tryvaiut-hrantovi-konkursy"
        
    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30
    )
        
    print(response.status_code)
        
    soup = BeautifulSoup(response.text, "html.parser")
    
    grants = []
    
    seen_titles = set()
    seen_urls = set()

    for a in soup.find_all("a", href=True):
    
        title = a.get_text(" ", strip=True)
        href = a["href"]
           
        if not href.startswith("/tryvaiut-hrantovi-konkursy/"):
           continue
        
        if href in seen_urls:
           continue
        
        seen_urls.add(href)
        
        if len(title) < 15:
           continue

        if title in seen_titles:
           continue

        seen_titles.add(title)

        page = requests.get(
            "https://ednannia.ua" + href,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=30
        )

        page_soup = BeautifulSoup(
            page.text,
            "html.parser"
        )

        page_text = page_soup.get_text(" ", strip=True)
        
        deadline = parse_deadline(page_text)
        
        print("CHECK:", title, deadline)
        
        if deadline and deadline < datetime.today():
           continue
       
        print("ADD:", title, deadline)
        grants.append({
            "title": title,
            "url": "https://ednannia.ua" + href,
            "category": "NGO",
            "deadline": (
                deadline.strftime("%d.%m.%Y")
                if deadline
                else "Невідомо"
            )
        })
        
    print(f"ISAR знайдено: {len(grants)}")
    
    return grants

