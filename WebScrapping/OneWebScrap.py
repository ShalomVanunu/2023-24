
import requests
from bs4 import BeautifulSoup

URL  = "https://worldcup.sport5.co.il/TemplatesExternal/Mondial/MondialStage.aspx?folderid=10795" # URL that i want to get the data

html_site = requests.get(URL).content # HTML DATA from site in Bytes

soup = BeautifulSoup(html_site, "html.parser") # transfer Bytes to HTML stracture Parsing


#
result = soup.find_all("h3")
for i in result:
    print(i.get_text())