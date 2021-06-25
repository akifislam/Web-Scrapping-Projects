from bs4 import BeautifulSoup
import requests

#Connection Setup !
page_no = 1
book_no = 1
while (page_no<=5):

    source_link = requests.get(f"https://www.rokomari.com/list/42757/%25E0%25A6%25B6%25E0%25A7%2587%25E0%25A6%25B7+%25E0%25A7%25A7+%25E0%25A6%25AC%25E0%25A6%259B%25E0%25A6%25B0%25E0%25A7%2587%25E0%25A6%25B0+%25E0%25A6%25B0%25E0%25A6%2595%25E0%25A6%25AE%25E0%25A6%25BE%25E0%25A6%25B0%25E0%25A6%25BF%25E0%25A6%25B0+%25E0%25A6%25AC%25E0%25A7%2587%25E0%25A6%25B8%25E0%25A7%258D%25E0%25A6%259F%25E0%25A6%25B8%25E0%25A7%2587%25E0%25A6%25B2%25E0%25A6%25BE%25E0%25A6%25B0+%25E0%25A6%25AC%25E0%25A6%2587%25E0%25A6%25B8%25E0%25A6%25AE%25E0%25A7%2582%25E0%25A6%25B9?ref=sm_p8&page2&page={page_no}").text
    soup = BeautifulSoup(source_link, "lxml")


    print("ROKOMARI BEST SELLER 2020 : ")
    for data in soup.findAll('div',class_="book-text-area"):
        print(f"{book_no}. Book Name : ")
        book_no+=1

        print(data.find('p', class_="book-title").text)
        print("Author Name : ")
        print(data.find('p', class_="book-author").text)
        # print("Old Price : ")
        # print(data.find('p', class_="book-price").find('strike').text)
        print("Current Price : ")
        print(data.find('p', class_="book-price").find('span').text)
        print("-----------------")
    page_no+=1
