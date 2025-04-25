from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["users"]

collection.update_one({"name": "Bob"}, {"$set": {"age": 32}})
print("✏️ Bob의 나이를 32로 수정 완료")

bob = collection.find_one({"name": "Bob"})
print("업데이트된 Bob 정보:", bob)