from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["users"]

collection.update_many({}, {"$set": {"joined": datetime.utcnow()}})
print(" 예제 2: 모든 사용자에 'joined' 필드 추가 완료")