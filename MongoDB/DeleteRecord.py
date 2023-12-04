
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://MongoUser:Password1@clusterdb.ekaau.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["mongoDB"]
collection = db["PhoneAddress"]

result = collection.find()  # Query all DB
for i in result:
    print(i)
    print(i["name"])

print("____________________________")
result = collection.delete_one({"_id":2})  # Delete by item
print(result)

print("____________________________")

result = collection.find()  # Query all DB
for i in result:
    print(i)
    print(i["name"])
