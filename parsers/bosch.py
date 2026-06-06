import requests
from bs4 import BeautifulSoup

def get_bosch():

url = "https://www.bosch-stiftung.de/en/news/open-calls"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
)

soup = BeautifulSoup(response.text, "html.parser")

for a in soup.find_all("a", href=True):

    text = a.get_text(" ", strip=True)

    if len(text) > 15:

        print(text)
        print(a["href"])
        print("-----")

return []

}
