import requests
from bs4 import BeautifulSoup

URL = "https://getgrant.ua/grants-and-funding/"

headers = {
"User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers, timeout=30)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

print("=== GETGRANT ===")

titles = soup.find_all(["h2", "h3"])

found = set()

for title in titles:
text = title.get_text(strip=True)

```
if len(text) > 15 and text not in found:
    found.add(text)
    print(text)
```

print(f"\nЗнайдено: {len(found)} записів")

