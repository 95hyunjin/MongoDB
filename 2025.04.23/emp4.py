from pymongo import MongoClient
from pprint import pprint

# MongoDB 연결 및 컬렉션 준비
client = MongoClient("mongodb://localhost:27017/")
db = client["department"]
collection = db["employees"]
collection.delete_many({})

# 샘플 데이터 삽입
project_processes = [
{ "project_name": "VLCC-2025", "status": "Completed" },
{ "project_name": "VLCC-2025", "status": "Completed" },
{ "project_name": "VLCC-2025", "status": "Pending" },
{ "project_name": "VLCC-2025", "status": "Begin" },

{ "project_name": "K-Tanker", "status": "Completed" },
{ "project_name": "K-Tanker", "status": "Pending" },
{ "project_name": "K-Tanker", "status": "Pending" },
{ "project_name": "K-Tanker", "status": "Completed" },

{ "project_name": "OilRig-A1", "status": "Begin" },
{ "project_name": "OilRig-A1", "status": "Completed" },
{ "project_name": "OilRig-A1", "status": "Completed" },
{ "project_name": "OilRig-A1", "status": "Completed" },
{ "project_name": "OilRig-A1", "status": "Pending" },

{ "project_name": "FPSO-X99", "status": "Begin" },
{ "project_name": "FPSO-X99", "status": "Begin" },
{ "project_name": "FPSO-X99", "status": "Pending" },

{ "project_name": "SUBSEA-D", "status": "Completed" },
{ "project_name": "SUBSEA-D", "status": "Pending" },
{ "project_name": "SUBSEA-D", "status": "Completed" }
]

collection.insert_many(project_processes)
pipeline = [
    {
        "$group": {
            "_id": "$project_name",
            "completed_steps": {
                "$sum": {
                    "$cond": [ { "$eq": ["$status", "Completed"] }, 1, 0 ]
                }
            }
        }
    }
]

result = collection.aggregate(pipeline)
for doc in result:
    print(doc)
result = db["employees"].aggregate(pipeline)
for doc in result:
    print(doc)