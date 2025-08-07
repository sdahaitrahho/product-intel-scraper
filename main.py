from scrapers.books_toscrape import scrape_books
from scrapers.quotes_js import scrape_quotes_js
import json
import os

def save_json(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    # books.toscrape.com
    print("Scraping books.toscrape.com...")
    books = scrape_books()
    save_json(books, "data/books.json")
    print(f"Saved {len(books)} books to data/books.json ✅")

    '''# quotes.toscrape.com/js
    print("Scraping quotes.toscrape.com (JavaScript)...")
    quotes = scrape_quotes_js()
    save_json(quotes, "data/quotes.json")
    print(f"Saved {len(quotes)} quotes ✅")'''
