from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["users"]

print("📖 모든 사용자:")
for user in collection.find():
    print(user)

print("\n📖 Alice 정보:")
alice = collection.find_one({"name": "Alice"})
print(alice)