import requests
from bs4 import BeautifulSoup
import sys

# url = 'https://seattle.craigslist.org/d/electronics/search/ela'
url = sys.argv[1]
page = requests.get(url)

class Merchandise:
    name = '',
    price = 0
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
    
    def get_listing(content):
        soup = BeautifulSoup(content, 'html.parser')

        # results = soup.find(id="search-results")
        elements = soup.find_all("li", class_="result-row")
        items = [Merchandise]
        for element in elements:
            title = element.find("h3", class_="result-heading")
            price = element.find("span", class_="result-price")
            items.append(Merchandise(title.text, int(price.text.strip('$').replace(',', ''))))
        return items
    
    def filter_listing(listing, condition):
        for item in listing:
            if condition(item):
                print(f'{item.name} price: ${item.price}')

def isPriceLess(item: Merchandise):
    if item.price < 30:
        return True
    return False

listing = Merchandise.get_listing(page.content)
Merchandise.filter_listing(listing, isPriceLess)