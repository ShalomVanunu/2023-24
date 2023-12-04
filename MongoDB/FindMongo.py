from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://MongoUser:Password1@clusterdb.ekaau.mongodb.net/?retryWrites=true&w=majority")
db = cluster["CyberClass"]
collection = db["Users"]

result = collection.find()
for i in result:
    print(i)

result = collection.find_one({"_id":2})
print(result)
