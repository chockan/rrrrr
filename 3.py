from bs4 import BeautifulSoup   # pip install beautifulsoup4
import requests     # pip install requests

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}


URL='https://www.amazon.in/s?k=drone&crid=93CDZKE7Y7NN&sprefix=drone%2Caps%2C286&ref=nb_sb_noss_1'


# HTTP Request
webpage = requests.get(URL, headers=HEADERS)

#print(webpage)
#print(webpage.content)

soup = BeautifulSoup(webpage.content, "html.parser")

#print(soup)


links = soup.find_all("a", attrs={"class": "a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})

#print(links)

a=links[1].get('href')
# #print(a)
product_list="https://www.amazon.in/" + a
#print(product_list)



new_webpage=requests.get(product_list,headers=HEADERS)

##print(new_webpage)

new_soup = BeautifulSoup(new_webpage.content, "html.parser")
# print(new_soup)

c=new_soup.find('span',attrs={'id':'productTitle'})
d=new_soup.find('span',attrs={'id':'productTitle'}).text
e=new_soup.find('span',attrs={'id':'productTitle'}).text.strip()
#print(c)
#print(d)
print(e)

f=new_soup.find('span',attrs={'class':'a-price-whole"'})
#print(f)
g=new_soup.find('span',attrs={'class':'a-price-whole'}).text
print(g)




