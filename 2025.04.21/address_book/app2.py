from pymongo import MongoClient
from pprint import pprint

# 1. MongoDB 연결
client = MongoClient("mongodb://localhost:27017/")
db = client["addressbook_db"]                # DB 생성
collection = db["contacts"]                  # 주소록 컬렉션

# 2. 주소록 문서 삽입
    contact = [{
        "name": request.form["name"],
        "phone": request.form["phone"],
        "email": request.form["email"],
        "address": request.form["address"],
        "tags": request.form.getlist("tags")
	},
	{
	"name" : "김수철",
	"age" : "57",
	"salary" : "7000",
	"address" : "서울특별시 강남구 역삼동",
	"tags" : ["친구", "회사"],
	"friend" : "홍길동"
    }]

result = collection.insert_many(contact)
print(f"✅ 주소록 문서 삽입 완료. ID: {result.inserted_id}")

# 3. 전체 문서 조회
print("\n📄 현재 주소록 목록:")
for doc in collection.find():
    pprint(doc)