from bs4 import BeautifulSoup   # pip install beautifulsoup4
import requests     # pip install requests
from tabulate import tabulate    # pip install tabulate


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}

# The webpage URL
URL = "https://www.amazon.in/s?k=drone&crid=208IBUQWLQPDV&sprefix=drone%2Caps%2C210&ref=nb_sb_noss_1"

# HTTP Request
webpage = requests.get(URL, headers=HEADERS)

# Soup Object containing all data
soup = BeautifulSoup(webpage.content, "html.parser")

# Fetch links as List of Tag Objects
links = soup.find_all("a", attrs={"class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})

# Store the links
links_list = []

# Loop for extracting links from Tag Objects
for link in links:
    links_list.append(link.get('href'))

titles = []
prices = []  # Store prices
reviews = []  # Store reviews
stocks = []  # Store stocks

for link in links_list:
    try:
        # Retry logic for failed requests
        for attempt in range(3):
            new_webpage = requests.get("https://www.amazon.in" + link, headers=HEADERS)
            new_webpage.raise_for_status()  # Raise an exception for HTTP errors
            if new_webpage.status_code == 200:
                break
        else:
            continue  # Skip to the next link if all attempts fail

        new_soup = BeautifulSoup(new_webpage.content, "html.parser")

        # Check if the title is properly displayed
        title_tag = new_soup.find("span", id="productTitle")
        price_tag = new_soup.find("span", class_="a-price-whole")
        review_tag = new_soup.find("span", class_="a-icon-alt")
        stock_tag = new_soup.find("span", class_="a-size-medium a-color-success")

        if title_tag and price_tag and review_tag and stock_tag:
            title = title_tag.get_text().strip()
            titles.append(title)
            price = price_tag.get_text().strip()
            prices.append(price)
            review = review_tag.get_text().strip()  # Corrected variable name here
            reviews.append(review)  # Corrected variable name here
            stock = stock_tag.get_text().strip()
            stocks.append(stock)
        else:
            titles.append(None)
            prices.append(None)
            reviews.append(None)
            stocks.append(None)


    except requests.exceptions.RequestException as e:
        # Skip printing error messages and continue with the next link
        continue

# Ensure the lengths of titles, prices, reviews, and stocks are the same
if len(titles) != len(prices) != len(reviews) != len(stocks):
    raise ValueError("Lengths of titles, prices, reviews, and stocks lists do not match.")

# Combine titles, prices, reviews, and stocks into a list of lists
# Generate table_data
table_data = [[title, price, review, stock] for title, price, review, stock in zip(titles, prices, reviews, stocks)]

# Iterate through table_data and print each item with label
for data in table_data:
    print(" "*20,"\n")
    print("Title:", data[0],"\n")
    print("#"*20)
    print("Price:", data[1],"\n")
    print("#"*20)
    print("Review:", data[2],"\n")
    print("#"*20)
    print("Stock:", data[3],"\n")
    print("#"*20)
    print()  # Print an empty line between each set of data







