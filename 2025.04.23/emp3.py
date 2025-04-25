from pymongo import MongoClient
from pprint import pprint

# MongoDB 연결 및 컬렉션 준비
client = MongoClient("mongodb://localhost:27017/")
db = client["department"]
collection = db["employees"]
collection.delete_many({})

# 샘플 데이터 삽입
employees = [
    { "name": "Kim", "department": "Welding", "salary": 6000 },
    { "name": "Lee", "department": "Welding", "salary": 5800 },
    { "name": "Park", "department": "Welding", "salary": 4900 },
    
    { "name": "Choi", "department": "Design", "salary": 5200 },
    { "name": "Jung", "department": "Design", "salary": 5100 },
    { "name": "Yoon", "department": "Design", "salary": 5000 },

    { "name": "Han", "department": "QA", "salary": 4500 },
    { "name": "Shin", "department": "QA", "salary": 4700 },
    { "name": "Seo", "department": "QA", "salary": 4600 }
]

collection.insert_many(employees)

pipeline = [
    {
        "$group": {
            "_id": "$department",
            "max_salary": { "$max": "$salary" },
            "min_salary": { "$min": "$salary" },
            "avg_salary": { "$avg": "$salary" }
        }
    }
]

result = db["employees"].aggregate(pipeline)
for doc in result:
    print(doc)