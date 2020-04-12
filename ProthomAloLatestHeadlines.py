from bs4 import BeautifulSoup
import requests

#Connection Setup !
source_link = requests.get("https://www.prothomalo.com/").text
soup = BeautifulSoup(source_link, "lxml")
# cat = soup.find('div',class_="info")
# print(cat.find('span').text)

for data in soup.findAll('div',class_="info"):
    print(data.find('span').text)
    print()
