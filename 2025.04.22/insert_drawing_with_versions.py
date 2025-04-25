from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["shipyard"]
collection = db["drawings"]

drawing_doc = {
    "drawing_name": "Main Deck Layout",
    "category": "Structural",
    "versions": [
        {
            "version_no": 1,
            "updated_by": "Lee JH",
            "update_date": "2023-12-01",
            "remarks": "Initial issue",
            "file_url": "https://files.shipyard.com/main_deck_v1.pdf"
        },
        {
            "version_no": 2,
            "updated_by": "Park SY",
            "update_date": "2024-01-10",
            "remarks": "Bulkhead added",
            "file_url": "https://files.shipyard.com/main_deck_v2.pdf"
        }
    ]
}

collection.insert_one(drawing_doc)
print("✅ 도면 및 버전 이력 데이터 삽입 완료")