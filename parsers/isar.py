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

    text = a.get_text(" ", strip=True)

    if len(text) > 20:

        print(text[:150])
        print(a["href"])
        print("-----")

return []

