## 📄 scrapers/books_toscrape.
import requests
from bs4 import BeautifulSoup
import json
import os

BASE_URL = "http://books.toscrape.com/"
HEADERS = {'User-Agent': 'Mozilla/5.0'}

def scrape_books():
    page = 1
    all_books = []

    while True:
        url = f"{BASE_URL}catalogue/page-{page}.html"
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            break  # No more pages

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

    return all_books
