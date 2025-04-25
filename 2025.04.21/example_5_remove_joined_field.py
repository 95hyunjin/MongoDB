from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["users"]

collection.update_many({}, {"$unset": {"joined": ""}})
print("예제 5: 'joined' 필드 삭제 완료")