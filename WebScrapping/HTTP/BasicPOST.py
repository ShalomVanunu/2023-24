
import requests

URL = "https://hack-yourself-first.com/Account/Login"

data = {  "Email":"mekifh@rishon.il", "Password":"1q2w3e1" }
http_post = requests.post(URL,data)
print(http_post.content)

if b"Hello" in http_post.content:
    print("Succes")
else:
    print("Not Success")

