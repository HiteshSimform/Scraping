import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

class FlipkartScraper:
    def __init__(self):
        self.url = 'https://www.flipkart.com/search?q=mobiles'
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def page_load(self):
        self.driver.get(self.url)
        time.sleep(3)  # Allow time for results to load
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')

    def create_csv_file(self):
        row_headers = ["Name", "Storage_details", "Screen_size", "Camera_details", "Battery_details", "Processor", "Warranty", "Price in Rupees"]
        self.file_csv = open('Flipkart_output.csv', 'w', newline='', encoding='utf-8')
        self.mycsv = csv.DictWriter(self.file_csv, fieldnames=row_headers)
        self.mycsv.writeheader()

    def data_scrap(self):
        first_page_mobiles = self.soup.find_all('div', class_='tUxRFH')  # Updated class name

        if not first_page_mobiles:
            print("No product data found. Check class names or page structure.")

        for i in first_page_mobiles:
            try:
                name = i.find('div', class_='KzDlHZ')  # Product name
                price = i.find('div', class_='Nx9bqj')  # Price
                details = i.find_all("li", class_='J+igdf')  # Specifications

                if name and price:
                    name = name.text.strip()
                    price = price.text.strip()[1:]  # Remove ₹ symbol
                else:
                    continue  # Skip if name or price is missing

                storage = details[0].text if len(details) > 0 else "No data"
                screen_size = details[1].text if len(details) > 1 else "No data"
                camera_details = details[2].text if len(details) > 2 else "No data"
                battery_details = details[3].text if len(details) > 3 else "No data"
                processor = details[4].text if len(details) > 4 else "No data"
                warranty_details = details[5].text if len(details) > 5 else "No data"

                print(f"Scraped: {name}, Price: {price}")  # Debugging output

                self.mycsv.writerow({
                    "Name": name,
                    "Storage_details": storage,
                    "Screen_size": screen_size,
                    "Camera_details": camera_details,
                    "Battery_details": battery_details,
                    "Processor": processor,
                    "Warranty": warranty_details,
                    "Price in Rupees": price
                })
            except Exception as e:
                print(f"Error scraping data: {e}")

    def tear_down(self):
        self.driver.quit()
        self.file_csv.close()

if __name__ == "__main__":
    flipkart = FlipkartScraper()
    flipkart.page_load()
    flipkart.create_csv_file()
    flipkart.data_scrap()
    flipkart.tear_down()
    print("Task completed")
