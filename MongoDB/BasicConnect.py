#
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://MongoUser:Password1@clusterdb.ekaau.mongodb.net/?retryWrites=true&w=majority")
db = cluster["CyberClass"]
collection = db["Users"]

data = {"lastname":"vanunu"}
collection.insert_one(data)
