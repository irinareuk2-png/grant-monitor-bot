def get_grants():

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

        if "access_time" not in text:
            continue

        grant_title = text.split("access_time")[0].strip()

        if len(grant_title) < 15:
            continue

        title_lower = grant_title.lower()

        if "getgrant service" in title_lower:
            continue

        allowed = any(
            keyword.lower() in title_lower
            for keyword in ALLOW_KEYWORDS
        )

        blocked = any(
            keyword.lower() in title_lower
            for keyword in BLOCK_KEYWORDS
        )

        if allowed and not blocked:
            grants.append(grant_title)

    grants = sorted(set(grants))

    print(f"GETGRANT знайдено: {len(grants)}")

    return grants
