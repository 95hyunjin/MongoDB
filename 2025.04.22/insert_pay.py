from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["project"]
collection = db["pay"]

project = [
	{"지출일자" : "2025-04-15",
	"지출 항목": "회의용 다과비",
	"금액(원)": "58,000",
	"사용 목적": "팀 미팅 다과 구입",
	"결재자 서명": "홍길동"},
	{"지출일자" : "2025-04-14",
	"지출 항목": "외부 출장 교통비",
	"금액(원)": "32,000",
	"사용 목적": "고객사 방문 KTX 이용",
	"결재자 서명": "김부장"},
	{"지출일자" : "2025-04-13",
	"지출 항목": "노트북 구매",
	"금액(원)": "1,250,000",
	"사용 목적": "신입사원 업무 장비 지급",
	"결재자 서명": "이이사"}]

collection.insert_many(project)
print("✅ 데이터 삽입 완료")