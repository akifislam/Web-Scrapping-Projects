from bs4 import BeautifulSoup
import requests

#Connection Setup !
source_link = requests.get("https://www.rokomari.com/list/42757/rokomari-bestseller?ref=sm_p8").text
soup = BeautifulSoup(source_link, "lxml")


print("ROKOMARI BEST SELLER 2020 : ")
for data in soup.findAll('div',class_="book-text-area"):
    print("Book Name : ")
    print(data.find('p', class_="book-title").text)
    print("Author Name : ")
    print(data.find('p', class_="book-author").text)
    # print("Old Price : ")
    # print(data.find('p', class_="book-price").find('strike').text)
    print("Current Price : ")
    print(data.find('p', class_="book-price").find('span').text)
    print("-----------------")

