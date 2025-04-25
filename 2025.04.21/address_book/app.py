from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB 연결
client = MongoClient("mongodb://localhost:27017/")
db = client["addressbook_db"]
collection = db["contacts"]

# 홈 페이지 - 입력 폼
@app.route('/')
def index():
    return render_template("index.html")

# 주소록 저장 처리
@app.route('/save', methods=["POST"])
def save_contact():
    contact = {
        "name": request.form["name"],
        "phone": request.form["phone"],
        "email": request.form["email"],
        "address": request.form["address"],
        "tags": request.form.getlist("tags")
    }
    collection.insert_one(contact)
    return redirect("/list")

# 저장된 주소록 리스트 출력
@app.route('/list')
def contact_list():
    contacts = list(collection.find())
    return render_template("result.html", contacts=contacts)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)