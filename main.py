# # # import requests
# # # from bs4 import BeautifulSoup
# # # import time

# # # headers = {
# # #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
# # #                   " Chrome/90.0.4430.93 Safari/537.36"
# # # }

# # # def get_products_from_page(url):
# # #     res = requests.get(url, headers=headers)
# # #     soup = BeautifulSoup(res.text, 'html.parser')

# # #     products = []

# # #     # Flipkart uses dynamic classes, so inspect current class names for product blocks.
# # #     # This selector might change over time. For example:
# # #     product_containers = soup.find_all('div', {'class': '_1AtVbE'})  # container for each product block
    
# # #     for container in product_containers:
# # #         # Product name
# # #         name_tag = container.find('a', {'class': 's1Q9rs'})
# # #         if not name_tag:
# # #             name_tag = container.find('div', {'class': '_4rR01T'})  # sometimes product name is here

# # #         if name_tag:
# # #             product_name = name_tag.text.strip()
# # #         else:
# # #             continue

# # #         # Product price
# # #         price_tag = container.find('div', {'class': '_30jeq3'})
# # #         product_price = price_tag.text.strip() if price_tag else 'N/A'

# # #         products.append({
# # #             'name': product_name,
# # #             'price': product_price
# # #         })

# # #     return products

# # # # Example usage:
# # # base_url = 'https://www.flipkart.com/search?q=laptop&page='

# # # all_products = []

# # # for page_num in range(1, 3):  # just scrape first 2 pages to test
# # #     print(f"Scraping page {page_num}")
# # #     url = base_url + str(page_num)
# # #     products = get_products_from_page(url)
# # #     all_products.extend(products)
# # #     time.sleep(2)  # polite delay

# # # for product in all_products:
# # #     print(product)

# # import requests
# # from bs4 import BeautifulSoup
# # import time
# # import csv
# # import os

# # headers = {
# #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
# #                   "Chrome/90.0.4430.93 Safari/537.36"
# # }

# # def get_products_from_page(url):
# #     res = requests.get(url, headers=headers)
# #     soup = BeautifulSoup(res.text, 'html.parser')

# #     products = []

# #     # Find product containers
# #     product_containers = soup.find_all('div', {'class': '_1AtVbE'})

# #     for container in product_containers:
# #         # Product name (two possible classes)
# #         name_tag = container.find('a', {'class': 's1Q9rs'})
# #         if not name_tag:
# #             name_tag = container.find('div', {'class': '_4rR01T'})

# #         if not name_tag:
# #             continue

# #         product_name = name_tag.text.strip()

# #         # Price
# #         price_tag = container.find('div', {'class': '_30jeq3'})
# #         product_price = price_tag.text.strip() if price_tag else 'N/A'

# #         # Image URL - sometimes in 'img' tag src or data-src attribute
# #         image_tag = container.find('img')
# #         image_url = None
# #         if image_tag:
# #             image_url = image_tag.get('src') or image_tag.get('data-src')

# #         products.append({
# #             'name': product_name,
# #             'price': product_price,
# #             'image_url': image_url
# #         })

# #     return products

# # def download_image(url, folder, filename):
# #     if not url:
# #         print(f"No image URL for {filename}")
# #         return
# #     try:
# #         response = requests.get(url, headers=headers)
# #         if response.status_code == 200:
# #             with open(os.path.join(folder, filename), 'wb') as f:
# #                 f.write(response.content)
# #             print(f"Downloaded image: {filename}")
# #         else:
# #             print(f"Failed to download image from {url}")
# #     except Exception as e:
# #         print(f"Error downloading {url}: {e}")

# # def main():
# #     search_query = "laptop"
# #     base_url = f"https://www.flipkart.com/search?q={search_query}&page="

# #     all_products = []
# #     images_folder = "flipkart_images"
# #     os.makedirs(images_folder, exist_ok=True)

# #     pages_to_scrape = 3  # number of pages to scrape

# #     for page_num in range(1, pages_to_scrape + 1):
# #         print(f"Scraping page {page_num}")
# #         url = base_url + str(page_num)
# #         products = get_products_from_page(url)
# #         all_products.extend(products)
# #         time.sleep(2)  # polite delay

# #     # Save to CSV
# #     csv_file = f'flipkart_{search_query}_products.csv'
# #     keys = ['name', 'price', 'image_url']
# #     with open(csv_file, 'w', newline='', encoding='utf-8') as f:
# #         writer = csv.DictWriter(f, fieldnames=keys)
# #         writer.writeheader()
# #         writer.writerows(all_products)

# #     print(f"\nSaved product data to {csv_file}")

# #     # Download images
# #     for idx, product in enumerate(all_products, start=1):
# #         img_url = product['image_url']
# #         # Use a safe filename
# #         filename = f"product_{idx}.jpg"
# #         download_image(img_url, images_folder, filename)
# #         time.sleep(1)  # polite delay for images

# # if __name__ == "__main__":
# #     main()

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import time
# import csv
# import os

# # Setup headless Chrome browser (won't open a window)
# options = Options()
# options.headless = True

# driver = webdriver.Chrome(options=options)  # or specify path: webdriver.Chrome(executable_path='path/to/chromedriver', options=options)

# search_query = "laptop"
# pages_to_scrape = 3

# base_url = f"https://www.flipkart.com/search?q={search_query}&page="

# all_products = []

# images_folder = "flipkart_images"
# os.makedirs(images_folder, exist_ok=True)

# def download_image(url, folder, filename):
#     import requests
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             with open(os.path.join(folder, filename), 'wb') as f:
#                 f.write(response.content)
#             print(f"Downloaded image: {filename}")
#         else:
#             print(f"Failed to download image from {url}")
#     except Exception as e:
#         print(f"Error downloading {url}: {e}")

# for page_num in range(1, pages_to_scrape + 1):
#     print(f"Scraping page {page_num}")
#     driver.get(base_url + str(page_num))
#     time.sleep(3)  # wait for JS to load content

#     products = driver.find_elements(By.CSS_SELECTOR, 'div._1AtVbE')

#     for container in products:
#         try:
#             name_elem = container.find_element(By.CSS_SELECTOR, 'div._4rR01T, a.s1Q9rs')
#             product_name = name_elem.text

#             price_elem = container.find_element(By.CSS_SELECTOR, 'div._30jeq3')
#             product_price = price_elem.text

#             img_elem = container.find_element(By.CSS_SELECTOR, 'img')
#             img_url = img_elem.get_attribute('src')

#             all_products.append({
#                 'name': product_name,
#                 'price': product_price,
#                 'image_url': img_url
#             })
#         except Exception:
#             # Skip containers that do not have product info
#             continue

# driver.quit()

# # Save to CSV
# csv_file = f'flipkart_{search_query}_products.csv'
# keys = ['name', 'price', 'image_url']
# with open(csv_file, 'w', newline='', encoding='utf-8') as f:
#     writer = csv.DictWriter(f, fieldnames=keys)
#     writer.writeheader()
#     writer.writerows(all_products)

# print(f"\nSaved product data to {csv_file}")

# # Download images
# for idx, product in enumerate(all_products, start=1):
#     img_url = product['image_url']
#     filename = f"product_{idx}.jpg"
#     download_image(img_url, images_folder, filename)
#     time.sleep(1)  # polite delay

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import os
import requests

# Setup Chrome options
options = Options()
options.headless = True  # Set False if you want to see browser window

# IMPORTANT: put your chromedriver path here if it's not in PATH
driver = webdriver.Chrome(options=options)  # or webdriver.Chrome(executable_path='path/to/chromedriver', options=options)

search_query = "laptop"
pages_to_scrape = 2
base_url = f"https://www.flipkart.com/search?q={search_query}&page="

all_products = []

images_folder = "flipkart_images"
os.makedirs(images_folder, exist_ok=True)

def download_image(url, folder, filename):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(folder, filename), 'wb') as f:
                f.write(response.content)
            print(f"Downloaded image: {filename}")
        else:
            print(f"Failed to download image from {url}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

for page_num in range(1, pages_to_scrape + 1):
    print(f"\nScraping page {page_num}")
    url = base_url + str(page_num)
    driver.get(url)

    try:
        # Wait for product containers to be visible (max 10 seconds)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div._1AtVbE')))
    except:
        print("Timed out waiting for products to load")
        continue

    product_containers = driver.find_elements(By.CSS_SELECTOR, 'div._1AtVbE')

    count = 0
    for container in product_containers:
        try:
            # Product name selector (two possible types)
            name_elem = container.find_element(By.CSS_SELECTOR, 'div._4rR01T, a.s1Q9rs')
            product_name = name_elem.text.strip()

            price_elem = container.find_element(By.CSS_SELECTOR, 'div._30jeq3')
            product_price = price_elem.text.strip()

            img_elem = container.find_element(By.CSS_SELECTOR, 'img')
            img_url = img_elem.get_attribute('src')

            # Skip entries without product name or price
            if not product_name or not product_price:
                continue

            all_products.append({
                'name': product_name,
                'price': product_price,
                'image_url': img_url
            })

            count += 1
            print(f"Scraped: {product_name} | {product_price}")
        except Exception as e:
            # Skip if any data not found in container
            continue

    print(f"Found {count} products on page {page_num}")
    time.sleep(2)  # polite delay

driver.quit()

if not all_products:
    print("No products scraped. Exiting.")
    exit()

# Save to CSV
csv_file = f'flipkart_{search_query}_products.csv'
keys = ['name', 'price', 'image_url']
with open(csv_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=keys)
    writer.writeheader()
    writer.writerows(all_products)

print(f"\nSaved {len(all_products)} products to {csv_file}")

# Download images
for idx, product in enumerate(all_products, start=1):
    img_url = product['image_url']
    filename = f"product_{idx}.jpg"
    download_image(img_url, images_folder, filename)
    time.sleep(1)

# request html package