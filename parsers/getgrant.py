def get_grants():

```
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

        if (
            len(grant_title) > 15
            and "GetGrant Service" not in grant_title
        ):

            title_lower = grant_title.lower()

            allowed = any(
                word.lower() in title_lower
                for word in ALLOW_KEYWORDS
            )

            blocked = any(
                word.lower() in title_lower
                for word in BLOCK_KEYWORDS
            )

            if allowed and not blocked:
                grants.append(grant_title)

grants = sorted(set(grants))

print(f"GETGRANT знайдено: {len(grants)}")

return grants
```
import requests
from bs4 import BeautifulSoup

ALLOW_KEYWORDS = [
"ГО",
"ОГС",
"громад",
"громади",
"громадянськ",
"демократ",
"медіа",
"журналіст",
"IREX",
"EED",
"Єднання",
"Bosch",
"Documenting Ukraine",
"відновлення"
]

BLOCK_KEYWORDS = [
"бізнес",
"підприєм",
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
"культура",
"резиденц",
"стипендія",
"науков",
"дослід"
]

def get_grants():

    url = "https://getgrant.ua/grants-and-funding/"
    
    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=30
    )
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    grants = []
    
   for link in soup.find_all("a", href=True):

    text = link.get_text(" ", strip=True)

    if len(text) > 30:
        print(text)
        print(link["href"])
        print("-----")
    
        text = title.get_text(" ", strip=True)
    
        if "access_time" in text:
    
            grant_title = text.split("access_time")[0].strip()
    
            if (
                len(grant_title) > 15
                and "GetGrant Service" not in grant_title
            ):
    
                title_lower = grant_title.lower()
    
                allowed = any(
                    word.lower() in title_lower
                    for word in ALLOW_KEYWORDS
                )
    
                blocked = any(
                    word.lower() in title_lower
                    for word in BLOCK_KEYWORDS
                )
    
                if allowed and not blocked:
                    grants.append(grant_title)
    
    grants = sorted(set(grants))
    
    print(f"GETGRANT знайдено: {len(grants)}")
    
    return grants
