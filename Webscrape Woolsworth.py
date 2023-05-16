#This web scraper goes to each of the woolsworth products in the given excel, goes to the website and scrapes product information: item_url, item_name, item_price1, price_unit1, is_organic 
import time
import os
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import re
from itertools import zip_longest

# Create empty lists to store item url and item name
item_url = []
item_name = []
item_price_doll = []
item_price_cents = []
item_unit = []
organic = []

#Set path and read the excel file
path = os.getcwd()
excel_path = path + '\Ron Wood_ scraping of prices 4 supermarkets Hardik.xlsx'
df = pd.read_excel(excel_path, sheet_name='woolworths.com.au')

#Initialize the Chrome web driver
driver = webdriver.Chrome()

with open('Output.txt', 'w') as f:
    #Loop through 3 item_urls and scrape relevant information
    for items in df['item_url'].iloc[:1]:
        url = items
        item_url.append(url)
        f.write(f'{url},')

        #Navigate to the URL and get the source
        driver.get(url)
        time.sleep(2) #wait for 2 seconds
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Convert the response content into a string
        html_str = str(soup)
        
        name_match = re.search(r'}\' class="shelfProductTile-title heading3">(.*)</h1>', html_str)
        price_match = re.search(r'<!-- PRODUCT PRICE -->.*class="price-dollars">(.+?)</span>', html_str,flags=re.DOTALL)
        cents_match = re.search(r'<!-- PRODUCT PRICE -->.*class="price-cents">(.+?)</span>', html_str,flags=re.DOTALL)
        unit_match = re.search(r'<!-- PRODUCT PRICE -->.*class="shelfProductTile-cupPrice ng-star-inserted">.+?/ (.+?) </div>', html_str,flags=re.DOTALL)
        is_organic = re.search(r'Organic', html_str, re.IGNORECASE)

        if name_match:
            name = name_match.group(1)
            f.write(f'{name},')

            if price_match:
                price = price_match.group(1)          
                if cents_match:
                    cents = cents_match.group(1)
                else: cents = ''
                f.write(f'{price}')
                f.write(f'.{cents},')
            else: 
                price = ''
                f.write(f'{price},')

            if unit_match:
                unit = unit_match.group(1)
            else: unit = ''
            f.write(f'{unit},')

            if is_organic:
                organics = 'organic'
            else: organics = 'inorganic'
            f.write(f'{organics}\n')
        else: continue

    #Close the driver
    driver.close()