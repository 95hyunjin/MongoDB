from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["users"]

print("예제 3: 이름에 'a'가 포함된 사용자 (대소문자 무시)")
for user in collection.find({"name": {"$regex": "a", "$options": "i"}}):
    print(user)