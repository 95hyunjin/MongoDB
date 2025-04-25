from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from pymongo import MongoClient
from werkzeug.utils import secure_filename
import os
import pandas as pd

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/images'

client = MongoClient("mongodb://localhost:27017/")
db = client["part_db"]
collection = db["parts"]

# 초기 데이터 삽입 (엑셀 로딩)
def insert_excel_data():
    df = pd.read_excel("부품_기본정보.xlsx")
    collection.delete_many({})
    collection.insert_many(df.to_dict(orient="records"))

@app.route('/', methods=['GET', 'POST'])
def index():
    parts = list(collection.find())
    return render_template('index2.html', parts=parts)

@app.route('/add', methods=['POST'])
def add_part():
    data = {
        "부품ID": request.form['part_id'],
        "부품명": request.form['name'],
        "카테고리": request.form['category'],
        "제조사": request.form['manufacturer'],
        "재고": int(request.form['stock']),
        "설명": request.form['description'],
    }

    # 이미지 업로드
    image = request.files['image']
    if image and image.filename != '':
        filename = secure_filename(image.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(image_path)
        data["이미지"] = filename
    else:
        data["이미지"] = ""

    collection.insert_one(data)
    return redirect(url_for('index'))

@app.route('/delete/<part_id>')
def delete_part(part_id):
    collection.delete_one({"부품ID": part_id})
    return redirect(url_for('index'))

if __name__ == '__main__':
    if not os.path.exists('static/images'):
        os.makedirs('static/images')
    insert_excel_data()
    app.run(debug=True, host='0.0.0.0', port=5002)