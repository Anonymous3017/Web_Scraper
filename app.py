import requests
from bs4 import BeautifulSoup
import json

response = requests.get("https://books.toscrape.com/", headers={'Accept-Encoding': 'utf-8'})
soup = BeautifulSoup(response.content, 'html.parser', from_encoding='utf-8')

data = []
for article in soup.find_all('article'):
    book = {}
    link = article.find('h3').find('a')['href']
    title = article.find('h3').find('a')['title']
    price = article.select('.price_color')[0].get_text()
    rating = article.select('.star-rating')[0]['class'][1]
    availability = article.select('.availability')[0].get_text().strip()
    image_link = article.find('img')['src']
    book["link"] = link
    book["title"] = title
    book["price"] = price
    book["rating"] = rating
    book["availability"] = availability
    book["image_link"] = image_link
    data.append(book)

with open('books.json', 'w') as outfile:
    json.dump(data, outfile)
