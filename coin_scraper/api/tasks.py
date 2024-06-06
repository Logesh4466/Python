from celery import shared_task
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@shared_task
def scrape_coin_data(coin_acronyms):
    options = Options()
    options.headless = True
    service = Service('/path/to/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)
    
    coin_data = {}
    for acronym in coin_acronyms:
        url = f"https://coinmarketcap.com/currencies/{acronym}/"
        driver.get(url)
        
        # Scrape necessary details here
        try:
            name = driver.find_element(By.CSS_SELECTOR, 'h1 .name').text
            price = driver.find_element(By.CSS_SELECTOR, '.priceValue').text
        
            coin_data[acronym] = {
                'name': name,
                'price': price
             }
        except Exception as e:
            coin_data[acronym] = {'error':str(e)}
        
    driver.quit()
    return coin_data
