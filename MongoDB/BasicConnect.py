#
from pymongo import MongoClient


cluster = MongoClient("mongodb+srv://1002872382:Password1@cluster0.gmeyduy.mongodb.net/?retryWrites=true&w=majority")
db = cluster["Users"]
collection = db["Users_Table"]

data = {"lastname":"vanunu"}
collection.insert_one(data)
