from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# MongoDB 연결
client = MongoClient("mongodb://localhost:27017/")
db = client["board_db"]
collection = db["posts"]

# 홈: 글 목록
@app.route('/')
def index():
    posts = list(collection.find().sort("created_at", -1))
    return render_template('index.html', posts=posts)

# 글쓰기
@app.route('/write', methods=['GET', 'POST'])
def write():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        file = request.files['image']

        filename = ""
        if file and file.filename != '':
            filename = datetime.now().strftime("%Y%m%d%H%M%S_") + file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

        post = {
            "title": title,
            "content": content,
            "author": author,
            "image": filename,
            "created_at": datetime.now()
        }
        collection.insert_one(post)
        return redirect(url_for('index'))

    return render_template('write.html')

# 글 상세
@app.route('/post/<post_id>')
def post_detail(post_id):
    post = collection.find_one({"_id": ObjectId(post_id)})
    return render_template('detail.html', post=post)

# 글 삭제
@app.route('/delete/<post_id>')
def delete_post(post_id):
    collection.delete_one({"_id": ObjectId(post_id)})
    return redirect(url_for('index'))

if __name__ == '__main__':
    if not os.path.exists('static/uploads'):
        os.makedirs('static/uploads')
    app.run(debug=True, host='0.0.0.0', port=5001)