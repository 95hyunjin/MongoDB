from pymongo import MongoClient

# 1. MongoDB 연결
client = MongoClient("mongodb://localhost:27017/")

# 2. 데이터베이스 및 컬렉션 선택
db = client["company"]
collection = db["employees"]

# 3. 기존 데이터 초기화 (중복 방지용)
collection.delete_many({})  # 컬렉션 비우기 (선택 사항)

# 4. 삽입할 직원 데이터
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

# 5. 데이터 삽입
collection.insert_many(employees)

# 6. 부서별 평균 급여 계산 (평균 5000 초과만 필터링)
pipeline = [
    { "$group": { "_id": "$department", "avg_salary": { "$avg": "$salary" }, "max_salary" : {"$max": "$salary" }, "min_salary":{"$min": "$salary"}, "employee_count" : {"$sum": 1}}},
    { "$project": {"department" : "$_id", "avg_salary": 1, "max_salary": 1, "min_salary": 1, "employee_count": 1}}
]

# 7. 결과 출력
result = collection.aggregate(pipeline)
for doc in result:
    print(f"부서: {doc['department']}, 평균 급여: {doc['avg_salary']:.2f} 원, "
	  f"최고 급여: {doc['max_salary']} 원, 최저 급여: {doc['min_salary']} 원, "
	  f"직원 수: {doc['employee_count']}명")