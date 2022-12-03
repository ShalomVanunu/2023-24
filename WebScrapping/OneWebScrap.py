
import requests
from bs4 import BeautifulSoup

URL  = "https://www.sport5.co.il/" # URL that i want to get the data a

html_site = requests.get(URL).content # HTML DATA from site in Bytes

soup = BeautifulSoup(html_site, "html.parser") # transfer Bytes to HTML stracture Parsing


#
result = soup.find_all(class_="img-flag-container")
for i in result:
    print(i.text)