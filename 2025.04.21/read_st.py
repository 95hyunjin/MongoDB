from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["student"]
collection = db["student_score"]

print("📖 모든 사용자:")
for user in collection.find():
    print(user)