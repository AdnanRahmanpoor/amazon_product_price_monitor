import requests
from . import db
from bs4 import BeautifulSoup
from lxml import html
from app.models import Product
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Function to scrape data using BS4
def scrape_product_data(url):
    # try:
    #     response = requests.get(url)
    #     soup = BeautifulSoup(response.text, 'html.parser')
    #     tree = html.fromstring(response.content)

    
    #     # Extract data from html elements
    #     product_name = tree.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]/text()')[0]
    #     print(product_name)
    #     price = tree.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]/text()')[0]
    #     print(price)
    #     # availability_div = soup.find('div', class_='availability')
    #     availability = tree.xpath('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]/text()')[0]
    #     print(availability)

    #     product_link = url
        
    #     print(f"Scraped: Name: {product_name}, Price: {price}, Availability: {availability}, Link: {product_link}")

    #     # save to a database
    #     save_to_db(product_name, price, availability, product_link)
    # except Exception as e:
        # print(f'Error: Unable to scrape product data : {e}')
    try:
        # Setup Selenium with ChromeDriver
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        service = Service('C:\Mods\chromedriver\chromedriver.exe')

        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(url)

        time.sleep(10)

        # Defensive checks using Selenium
        try:
            product_title = driver.find_element(By.XPATH, '//*[@id="productTitle"]').text.strip()
            print(product_title)
        except:
            product_title = "N/A"
            print("Product title not found!")

        try:
            price = driver.find_element(By.XPATH, '//*[@id="corePrice_feature_div"]/div/div/span[1]/span[2]/span[2]').text.strip()
        except:
            price = "N/A"
            print("Price not found!")

        try:
            availability = driver.find_element(By.XPATH, '//*[@id="availability"]/span').text.strip()
        except:
            availability = "N/A"
            print("Availability not found!")

        product_link = url

        print(f"Scraped: Title: {product_title}, Price: {price}, Availability: {availability}")

        # Save the data to the database
        save_to_db(product_title, price, availability, product_link)

        driver.quit()

    except Exception as e:
        print(f"Error scraping product data: {e}")

def save_to_db(name, price, availability, link):
    try:
        product = Product(name=name, price=price, availability=availability, link=link)
        db.session.add(product)
        db.session.commit()
        print(f"Product {name} saved successfully")
    except Exception as e:
        print(f"Error saving product: {e}")