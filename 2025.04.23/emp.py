from pymongo import MongoClient
from pprint import pprint

# MongoDB 연결 및 컬렉션 준비
client = MongoClient("mongodb://localhost:27017/")
db = client["department"]
collection = db["employees"]
collection.delete_many({})

# 샘플 데이터 삽입
employees = [
	{ "name": "Kim", "department": "Welding" },
	{ "name": "Lee", "department": "Welding" },
	{ "name": "Park", "department": "Welding" },
	{ "name": "Choi", "department": "Design" },
	{ "name": "Jung", "department": "Design" },
	{ "name": "Yoon", "department": "Design" },
	{ "name": "Han", "department": "QA" },
	{ "name": "Shin", "department": "QA" },
	{ "name": "Seo", "department": "QA" },
	{ "name": "Kang", "department": "HR" },
	{ "name": "Baek", "department": "HR" },
	{ "name": "Jin", "department": "Sales" },
	{ "name": "Nam", "department": "Sales" }
]
collection.insert_many(employees)

# Aggregation 파이프라인 구성
pipeline = [
	{ "$group": { "_id": "$department", "employee_count": { "$sum": 1 } } }
]

# 결과 출력
result = collection.aggregate(pipeline)
for doc in result:
    print(doc)