import requests
from bs4 import BeautifulSoup
url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# Empty list to hold the data
products = []

# Find all product wrapper divs
for card in soup.find_all('div', class_='product-wrapper'):
    # Extract title, description, price, rating, and number of reviews
    title = card.find('a', class_='title').text.strip()
    description = card.find('p', class_='description').text.strip()
    price = card.find('h4', class_='price').text.strip()
    rating = len(card.find('div', class_='ratings').find_all('span', class_='ws-icon-star'))
    reviews = card.find('p', class_='review-count').text.strip().split(' ')[0]  # Assuming "X reviews"
    
    # Append the data to the products list
    products.append({
        'title': title,
        'description': description,
        'price': price,
        'rating': rating,
        'reviews': reviews
    })

# Display the extracted data
for product in products:
    print(product)