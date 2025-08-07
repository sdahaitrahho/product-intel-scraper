from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_quotes_js():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # comment out for debugging
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    quotes = []
    page = 1

    while True:
        url = f"https://quotes.toscrape.com/js/page/{page}/"
        driver.get(url)
        time.sleep(2)  # wait for JS to load; later we'll improve this with WebDriverWait

        quote_elements = driver.find_elements(By.CLASS_NAME, "quote")
        if not quote_elements:
            break  # no more quotes

        for quote_el in quote_elements:
            text = quote_el.find_element(By.CLASS_NAME, "text").text
            author = quote_el.find_element(By.CLASS_NAME, "author").text
            tags = [tag.text for tag in quote_el.find_elements(By.CLASS_NAME, "tag")]
            
            quotes.append({
                "text": text,
                "author": author,
                "tags": tags
            })

        page += 1

    driver.quit()
    return quotes
