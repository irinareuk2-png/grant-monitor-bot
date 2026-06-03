import requests
from bs4 import BeautifulSoup

def get_bosch():

```
url = "https://www.bosch-stiftung.de/en/news/open-calls"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
)

soup = BeautifulSoup(response.text, "html.parser")

items = []

text = soup.get_text(" ", strip=True)

if "There are currently no open calls" not in text:
    items.append("Новий конкурс на Bosch Foundation")

return items
```
