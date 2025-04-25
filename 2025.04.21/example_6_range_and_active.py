from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["users"]

print("🔍 예제 6: 나이 25~35세 & active 사용자")
query = {"age": {"$gte": 25, "$lte": 35}, "active": True}
for user in collection.find(query):
    print(user)