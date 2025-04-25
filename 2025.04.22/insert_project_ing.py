from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["project"]
collection = db["project_ing"]

project = [
	{"프로젝트명" : "ERP 고도화",
	"담당자": "김민수",
	"시작일": "2025-04-01",
	"종료일": "2025-06-30",
	"진행률(%)": "45%"},
	{"프로젝트명" : "웹 리뉴얼",
	"담당자": "이지은",
	"시작일": "2025-03-10",
	"종료일": "2025-05-15",
	"진행률(%)": "80%"},
	{"프로젝트명" : "모바일 웹",
	"담당자": "박정우",
	"시작일": "2025-02-01",
	"종료일": "2025-04-30",
	"진행률(%)": "95%"}]

collection.insert_many(project)
print("✅ 데이터 삽입 완료")