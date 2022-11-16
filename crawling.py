from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.nike.com/kr/w/new-releases-tops-tshirts-3n82yz9om13")

bsObject = BeautifulSoup(html, "html.parser")

#for link in bsObject.find_all('a'):
#    print(link.text.strip(), link.get('href'))

for link in bsObject.find_all('img'):
    print(link.text.strip(), link.get('src'))