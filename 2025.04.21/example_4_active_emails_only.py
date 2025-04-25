from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["users"]

print("📧 예제 4: active 사용자 이메일 목록")
for user in collection.find({"active": True}, {"_id": 0, "email": 1}):
    print(user)