from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["project"]
collection = db["project_ing"]

project = {"_id": "ObjectId('68073a8e945e8bc0b5903d8d')"}

collection.delete_One(project)
print("✅ 데이터 삭제 완료")