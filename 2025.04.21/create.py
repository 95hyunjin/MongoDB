from pymongo import MongoClient  # PyMongo에서 MongoDB 클라이언트 불러오기

# MongoDB 서버에 연결 (기본 포트: 27017, 로컬호스트 기준)
client = MongoClient("mongodb://localhost:27017/")

# 사용할 데이터베이스 선택 (없으면 자동으로 생성됨)
db = client["mydatabase"]

# 사용할 컬렉션 선택 (테이블과 유사한 개념, 없으면 자동 생성됨)
collection = db["users"]

# 삽입할 샘플 사용자 데이터 목록 정의 (리스트 형태)
sample_users = [
    {"name": "Alice", "age": 25, "email": "alice@example.com", "active": True, "joined": "2023-01-01"},
    {"name": "Bob", "age": 30, "email": "bob@example.com", "active": True, "joined": "2022-06-15"},
    {"name": "Charlie", "age": 35, "email": "charlie@example.com", "active": False, "joined": "2021-03-10"},
    {"name": "Diana", "age": 28, "email": "diana@example.com", "active": True, "joined": "2023-02-20"},
    {"name": "Evan", "age": 32, "email": "evan@example.com", "active": False, "joined": "2020-11-05"},
    {"name": "Fiona", "age": 27, "email": "fiona@example.com", "active": True, "joined": "2022-09-01"},
    {"name": "George", "age": 29, "email": "george@example.com", "active": False, "joined": "2021-12-25"},
    {"name": "Hannah", "age": 26, "email": "hannah@example.com", "active": True, "joined": "2023-04-10"},
    {"name": "Ian", "age": 31, "email": "ian@example.com", "active": False, "joined": "2020-02-28"},
    {"name": "Jane", "age": 33, "email": "jane@example.com", "active": True, "joined": "2022-08-08"}
]

# 다수의 문서를 한 번에 컬렉션에 삽입
collection.insert_many(sample_users)

# 완료 메시지 출력
print("✅ 샘플 데이터 삽입 완료")