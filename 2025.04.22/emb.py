from pymongo import MongoClient  # PyMongo에서 MongoDB 클라이언트 불러오기

# MongoDB 서버에 연결 (기본 포트: 27017, 로컬호스트 기준)
client = MongoClient("mongodb://localhost:27017/")

# 사용할 데이터베이스 선택 (없으면 자동으로 생성됨)
db = client["embedding"]

# 사용할 컬렉션 선택 (테이블과 유사한 개념, 없으면 자동 생성됨)
collection = db["users"]

# 삽입할 샘플 사용자 데이터 목록 정의 (리스트 형태)
sample_users = [
{
  "drawing_name": "Hull Plan",
  "category": "Structure",
  "versions": [
    {
      "version_no": 1,
      "updated_by": "Kim",
      "update_date": "2024-01-01"
    },
    {
      "version_no": 2,
      "updated_by": "Lee",
      "update_date": "2024-02-15"
    }
  ]
}
]

# 다수의 문서를 한 번에 컬렉션에 삽입
collection.insert_many(sample_users)

# 완료 메시지 출력
print("✅ 샘플 데이터 삽입 완료")
