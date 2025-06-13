import requests
from bs4 import BeautifulSoup

# website = "https://subslikescript.com/movie/Titanic-120338"
# website = "https://subslikescript.com/movies"
root = "https://subslikescript.com"
website = f"{root}/movies"
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, "lxml")
# print(soup.prettify())

box = soup.find("article", class_="main-article")

links = []
for link in box.find_all("a", href=True):
    links.append(link["href"])


print(links)

for link in links:
    website = f"{root}/{link}"
    result = requests.get(website)
    content = result.text
    soup = BeautifulSoup(content, "lxml")

    box = soup.find("article", class_="main-article")
    title = box.find("h1").get_text()
    transcript = box.find("div", class_="full-script").get_text(
        strip=True, separator=" "
    )

    with open(f"{title}.txt", "w") as file:
        file.write(transcript)

# title = box.find('h1').get_text()

# transcript = box.find('div',class_='full-script').get_text(strip=True, separator=' ')

# with open('titanic.txt','w') as file:
#     file.write(transcript)

# with open(f'{title}.txt','w') as file:
#     file.write(transcript)
# print(title)
# print(transcript)
