from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["users"]

print("예제 1: 나이 30세 이상 사용자 (나이 내림차순)")
for user in collection.find({"age": {"$gte": 30}}).sort("age", -1):
    print(user)