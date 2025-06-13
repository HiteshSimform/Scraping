import requests
from bs4 import BeautifulSoup
import os
import re


root = "https://subslikescript.com"
website = f"{root}/movies"

result = requests.get(website)
content = result.text


soup = BeautifulSoup(content, "lxml")

box = soup.find("article", class_="main-article")

links = [link["href"] for link in box.find_all("a", href=True)]

os.makedirs("./ScrappedData", exist_ok=True)

for link in links:
    movie_url = f"{root}/{link}"
    result = requests.get(movie_url)
    content = result.text
    soup = BeautifulSoup(content, "lxml")

    box = soup.find("article", class_="main-article")

    title = box.find("h1").get_text() if box.find("h1") else None
    transcript = (
        box.find("div", class_="full-script").get_text(strip=True, separator=" ")
        if box.find("div", class_="full-script")
        else None
    )

    if title and transcript:
        safe_title = re.sub(r'[<>:"/\\|?*]', "_", title)
        file_path = f"./ScrappedData/{safe_title}.txt"

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(transcript)
        print(f"Saved: {file_path}")
    else:
        print(f"Skipping {movie_url}, title or transcript not found.")
