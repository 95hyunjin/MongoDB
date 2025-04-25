from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["users"]

collection.delete_one({"name": "Charlie"})
print("🗑️ Charlie 삭제 완료")

print("\n📖 삭제 후 사용자 목록:")
for user in collection.find():
    print(user)