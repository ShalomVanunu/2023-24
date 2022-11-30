import requests

URL = "https://keithgalli.github.io/web-scraping/webpage.html"

http_get = requests.get(URL)
print(http_get.content) # show the HTML Code

file = open("HTML.html", "wb")
file.write(http_get.content)

# codec of symbols
# "dssdfdsffd" utf-8,16
# byte(s) - 8 bits - 0-255 -HEX