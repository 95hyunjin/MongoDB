from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["students"]
users = db["users"]

# 사용자 1: 기본 정보만
users.insert_one({
    "name": "Alice",
    "age" : 21,
    "email": "alice@example.com"
})

print("✅ 사용자 삽입 완료")