from pymongo import MongoClient
from datetime import datetime, timedelta

client = MongoClient("mongodb://localhost:27017/")
db = client["business"]
collection = db["sales"]

# 기존 데이터 초기화
collection.delete_many({})

customer = [
	{ "customer": "Samsung", "amount": 1000 },
	{ "customer": "Samsung", "amount": 1500 },
	{ "customer": "Hyundai", "amount": 800 }
]
collection.insert_many(customer)

pipeline = [
    {
        "$group": {
            "_id": "$customer",
            "order_count": { "$sum": 1 },
            "total_amount": { "$sum": "$amount" }
        }
    }
]

result = collection.aggregate(pipeline)
for doc in result:
    print(doc)