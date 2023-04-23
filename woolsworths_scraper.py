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
excel_path = path + '\reference_scraped_data.xlsx'
df = pd.read_excel(excel_path)

#Initialize the Chrome web driver
driver = webdriver.Chrome()

with open('new_scraped_data_42323.csv', 'w') as f:
    #Loop through item_urls and scrape relevant information
    for items in df['item_url']:
        url = items
        item_url.append(url)
        f.write(f'{url},')

        #Navigate to the URL and get the source
        driver.get(url)
        time.sleep(2) #wait for 2 seconds
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        ##Code processing for soup here
        ##Code available upon request

    #Close the driver
    driver.close()

