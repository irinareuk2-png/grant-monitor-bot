import requests
from bs4 import BeautifulSoup

def get_isar():

    url = "https://ednannia.ua/tryvaiut-hrantovi-konkursy"
    
    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30
    )
    
    print(response.status_code)
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    for a in soup.find_all("a", href=True):
    
        title = a.get_text(" ", strip=True)
        href = a["href"]
    
        if len(title) < 15:
            continue
    
        if "конкурс" not in title.lower() and "грант" not in title.lower():
            continue
    
        grants.append({
            "title": title,
            "url": "https://ednannia.ua" + href,
            "category": "NGO",
            "deadline": "Невідомо"
        })

     print(f"ISAR знайдено: {len(grants)}")
    
    return []

