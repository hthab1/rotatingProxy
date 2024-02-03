import requests

with open("valid_proxies.txt", "r") as f:
    proxies = f.read().split("\n")

sites_to_check = [
    "http://books.toscrape.com/",
    "http://books.toscrape.com/catalogue/category/books/travel_2/index.html",
    "http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html",
    "http://books.toscrape.com/catalogue/category/books/philosophy_7/index.html",
    "http://books.toscrape.com/catalogue/category/books/fiction_10/index.html"
]

counter = 0

for site in sites_to_check:
    try:
       print(f"Using the proxy: {proxies[counter]}")
       res = requests.get(site, proxies={
           "http":proxies[counter],
           "https":proxies[counter],
       })
       print(res.text)
    except:
        print("Failed")
    finally:
        counter += 1
        counter % len(proxies)