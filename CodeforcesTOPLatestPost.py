from bs4 import BeautifulSoup
import requests

#Connection Setup
source = requests.get('https://codeforces.com/top').text
soup = BeautifulSoup(source,'lxml')


headline = soup.find('div',class_='title').a.text

print(headline)
print("\n")

summary =  soup.find('div',class_='ttypography').text
print(summary)
