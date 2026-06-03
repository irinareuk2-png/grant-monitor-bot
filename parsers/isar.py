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

    grants = []

    seen_urls = set()

    for a in soup.find_all("a", href=True):
    
        title = a.get_text(" ", strip=True)
        href = a["href"]
           
        if href in seen_urls:
           continue
        
        seen_urls.add(href)
        
        if not href.startswith("/tryvaiut-hrantovi-konkursy/"):
           continue

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
        
        print(title)
        print(href)
        print("-----")

        grants.append({
            "title": title,
            "url": "https://ednannia.ua" + href,
            "category": "NGO",
            "deadline": "Невідомо"
        })
        
    print(f"ISAR знайдено: {len(grants)}")
    
    return grants

