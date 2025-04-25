from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["users"]

print("📊 예제 7: 사용자 수가 2명 이하일 경우 기본 사용자 삽입")

if collection.count_documents({}) <= 2:
    collection.insert_many([
        {"name": "Daisy", "age": 22, "email": "daisy@example.com"},
        {"name": "Ethan", "age": 40, "email": "ethan@example.com"}
    ])
    print("→ 기본 사용자 추가 완료")
else:
    print("→ 사용자 수 충분, 추가 생략")