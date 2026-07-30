import requests
from bs4 import BeautifulSoup
import pandas as pd

print("=" * 60)
print("       CODEALPHA DATA ANALYTICS TASK 1")
print("              WEB SCRAPING PROJECT")
print("=" * 60)

url = "https://books.toscrape.com/"

print("\nConnecting to Website...")

response = requests.get(url)

if response.status_code == 200:
    print("Website Connected Successfully")
else:
    print("Connection Failed")
    exit()

print("\nCollecting Book Details...")

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

book_names = []
prices = []
ratings = []

for book in books:

    title = book.h3.a["title"]

    price = book.find("p", class_="price_color").text

    rating = book.find("p")["class"][1]

    book_names.append(title)

    prices.append(price)

    ratings.append(rating)

df = pd.DataFrame({
    "Book Name": book_names,
    "Price": prices,
    "Rating": ratings
})

print("\nData Collected Successfully")

print("\nFirst 10 Books\n")

print(df.head(10))

df.to_csv("scraped_data.csv", index=False)

print("\nCSV File Saved Successfully")

print("\nTotal Books Collected :", len(df))

print("\nProject Completed Successfully")

print("=" * 60)