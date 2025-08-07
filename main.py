from scrapers.books_toscrape import scrape_books
import json
import os

def save_json(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    print("Scraping books.toscrape.com...")
    books = scrape_books()
    save_json(books, "data/books.json")
    print(f"Saved {len(books)} books to data/books.json ✅")
