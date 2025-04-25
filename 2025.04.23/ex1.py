from pymongo import MongoClient
from pprint import pprint
from datetime import datetime

# MongoDB 연결 및 초기화
client = MongoClient("mongodb://localhost:27017/")
db = client["company"]
employees = db["employees"]
departments = db["departments"]
employees.delete_many({})
departments.delete_many({})

# employees 컬렉션 샘플 데이터
employees.insert_many([
    { "name": "Kim", "age": 35, "salary": 6000, "department": "HR", "birthday": datetime(1989, 4, 10), "tags": ["team", "remote"] },
    { "name": "Lee", "age": 28, "salary": 4800, "department": "HR", "birthday": datetime(1996, 1, 22), "tags": ["solo"] },
    { "name": "Choi", "age": 42, "salary": 7200, "department": "Dev", "birthday": datetime(1982, 12, 5), "tags": ["lead", "on-site"] },
    { "name": "Park", "age": 31, "salary": 5300, "department": "Dev", "birthday": datetime(1993, 7, 8), "tags": ["remote"] },
    { "name": "Yoon", "age": 26, "salary": 3900, "department": "Marketing", "birthday": datetime(1998, 9, 18), "tags": ["event", "remote"] }
])

# departments 컬렉션 샘플 데이터
departments.insert_many([
    { "_id": "HR", "manager": "Director A" },
    { "_id": "Dev", "manager": "Director B" },
    { "_id": "Marketing", "manager": "Director C" }
])

# 파이프라인 실행 예시
pipeline = [
    { "$match": { "age": { "$gt": 30 } } }, #나이가 30 초과
    { "$group": { "_id": "$department", "avg_salary": { "$avg": "$salary" } } }, #department그룹화 salary평균으로
    { "$project": { "department": "$_id", "avg_salary": 1, "_id": 0 } }, #
    { "$sort": { "avg_salary": -1 } }, #salary 평균값을 내림차순 정렬
    { "$limit": 5 }, #상위 5개 제한
    { "$skip": 0 }, #문서 건너뛰기
    { "$addFields": { "retrieved_at": datetime.now() } }, #새로운 필드 추가
    { "$unwind": "$tags" }, #배열분해
    { "$count": "total_docs" } #문서 수 카운트
]

# 하나씩 단계적으로 실행 (예시로 일부 단계 선택적 실행)
# $lookup과 $replaceRoot는 별도 실행
lookup_pipeline = [
    {
        "$lookup": {
            "from": "departments", #조인할 컬렉션 이름
            "localField": "department", #현재 컬렉션(employees)의 조인 기준 필드
            "foreignField": "_id", #조인 대상 컬렉션(departments)의 기준 필드
            "as": "dept_info" #조인 결과가 저장될 배열 이름
        }
    },
    { "$unwind": "$dept_info" }, #하나의 객체로 풀어주기
    { "$replaceRoot": { "newRoot": "$dept_info" } } #원래의 문서를 dept_info 객체로 완전히 바꿈 / employees의 기본 정보는 사라지고 departments의 정보만 남는다
]

# 결과 출력 (예시로 lookup 사용)
print("\n📌 $lookup + $replaceRoot 결과:")
for doc in employees.aggregate(lookup_pipeline):
    pprint(doc)
