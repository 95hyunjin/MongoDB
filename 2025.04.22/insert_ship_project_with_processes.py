from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["shipyard"]
collection = db["project_processes"]

doc = {
    "project_name": "LNGC-Alpha",
    "client": "SK Gas",
    "processes": [
        {
            "name": "Block Assembly",
            "description": "Welding and assembling hull blocks",
            "start_date": "2024-01-01",
            "end_date": "2024-01-10",
            "status": "Completed"
        },
        {
            "name": "Painting",
            "description": "Surface treatment and painting",
            "start_date": "2024-01-11",
            "end_date": "2024-01-20",
            "status": "In Progress"
        }
    ]
}

collection.insert_one(doc)
print("✅ 프로젝트 + 공정 데이터 삽입 완료")