import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
}

url = 'https://www.ambitionbox.com/'

response = requests.get(url, headers=headers)
webpage = response.text

soup = BeautifulSoup(webpage, 'lxml')

print(soup.find_all('h1')[0].text.strip())

for h2 in soup.find_all('h2'):
    print(h2.text.strip())
