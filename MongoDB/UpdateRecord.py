
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://MongoUser:Password1@clusterdb.ekaau.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["mongoDB"]
collection = db["PhoneAddress"]

result = collection.find()  # Query all DB
for i in result:
    print(i)

print("____________________________")
result = collection.update_one({"_id":3},{"$set":{"name":"Tim"}})  # Delete by item
print(result)

print("____________________________")

result = collection.find()  # Query all DB
for i in result:
    print(i)

count = collection.count_documents({})
print(count)