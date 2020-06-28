from bs4 import BeautifulSoup
import requests

#Connection Setup !
ProthomAloWebsiteURL = "https://www.prothomalo.com/"
source_link = requests.get(ProthomAloWebsiteURL).text
soup = BeautifulSoup(source_link, "lxml")
# cat = soup.find('div',class_="info")
# print(cat.find('span').text)

for data in soup.findAll('div',class_="info"):
    print(data.find('span').text)
    print()
