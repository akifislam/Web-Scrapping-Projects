#Update on : June 24, 2021

from bs4 import BeautifulSoup
import requests


ProthomAloWebsiteURL = "https://www.prothomalo.com/"
source_link = requests.get(ProthomAloWebsiteURL).text
soup = BeautifulSoup(source_link, "lxml")
soup2 = soup.find('div',class_="row2leftcolumn-m__big_box_row_2__19IML")


counter = 1
headlines = []
unique_headlines = []
for link in soup2.findAll('a',href=True):
    headlines = (str(link['href']).split('/'))
    unique_headlines.append(headlines[-1])
    headlines.clear()

unique_headlines = set(unique_headlines)

for data in unique_headlines:
    print(data)



# for data in soup.findAll('div',class_="newsHeadline-m__title-link__1puEG"):
#     print(data.find('span').text)
#     print()
