## 📄 scrapers/books_toscrape.
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
import time


BASE_URL = "http://books.toscrape.com/"
#HEADERS = {'User-Agent': 'Mozilla/5.0'}

def get_random_headers():
    ua = UserAgent()
    return {
        "User-Agent": ua.random
    }

def get_page(url, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=get_random_headers(), timeout=10)
            if response.status_code == 200:
                return response
            else:
                print(f"⚠️ Status code {response.status_code}, retrying...")
        except Exception as e:
            print(f"❌ Request error: {e}, retrying...")
        time.sleep(random.uniform(2, 5))  # Delay before retry
    return None
'''
def get_page(url, max_retries=3):
    proxies = [
        "http://89.58.45.94:43476",
        
    ]
    for attempt in range(max_retries):
        try:
            proxy = {"http": random.choice(proxies), "https": random.choice(proxies)}
            response = requests.get(url, headers=get_random_headers(), proxies=proxy, timeout=10)
            if response.status_code == 200:
                return response
        except:
            pass
        time.sleep(random.uniform(2, 5))
    return None
'''

def scrape_books():
    page = 1
    all_books = []

    while True:
        url = f"{BASE_URL}catalogue/page-{page}.html"
        response = get_page(url)

        if response is None:
            print(f"❌ Failed to load page {page}, stopping.")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.select("article.product_pod")

        if not books:
            break

        for book in books:
            title = book.h3.a["title"]
            price = book.select_one(".price_color").text
            availability = book.select_one(".availability").text.strip()

            all_books.append({
                "title": title,
                "price": price,
                "availability": availability
            })

        page += 1
        time.sleep(random.uniform(1, 3))  # Random delay between pages

    return all_books