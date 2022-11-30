import requests

URL = "https://keithgalli.github.io/web-scraping/webpage.html"

http_get = requests.get(URL) #
print(http_get.content) # show the HTML

file = open("HTML.html", "wb")
file.write(http_get.content)
