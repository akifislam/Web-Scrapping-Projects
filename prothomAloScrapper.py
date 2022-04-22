from bs4 import BeautifulSoup
import requests
import json

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

responses= {}

count = 0
for data in unique_headlines:
    count=count+1
    responses[count] = data;

print( responses);