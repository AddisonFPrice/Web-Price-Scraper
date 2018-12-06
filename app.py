import requests
from bs4 import BeautifulSoup


request = requests.get("https://www.filson.com/small-rugged-twill-duffle-bag.html#sku=11070220-fco-000971914")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find ("span", {"class": "price"})
string_price = element.text
integer_price = float(string_price[1:])

if integer_price < 375:
    print("Buy the bag! The current price is {}".format(string_price))
else:
    print("This shit is too expensive")


# Website we're scraping from
# https://www.filson.com/small-rugged-twill-duffle-bag.html#sku=11070220-fco-000971914

# HTML target for the data we're scraping
# <span class="price">$350.00</span>

