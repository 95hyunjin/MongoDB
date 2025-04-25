from flask import Flask, render_template, request, redirect, url_for, session
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta, datetime

app = Flask(__name__, static_folder='static')
app.secret_key = 'vision'
app.config["MONGO_URI"] = "mongodb://localhost:27017/user_db"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

mongo = PyMongo(app)
users = mongo.db.users

@app.route('/')
def home():
    return redirect(url_for('login_page'))

@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        gender = request.form['gender']

        if users.find_one({'username': username}):
            return "이미 존재하는 사용자입니다."

        hashed_pw = generate_password_hash(password)
        users.insert_one({
            'username': username,
            'password': hashed_pw,
            'name': name,
            'email': email,
            'age': int(age),
            'gender': gender,
            'created_at': datetime.utcnow()
        })

        return redirect(url_for('login_page'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = users.find_one({'username': username})
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            session.permanent = True
            return redirect(url_for('success_page'))
        return "로그인 실패. 아이디 또는 비밀번호를 확인하세요."

    return render_template('login.html')

@app.route('/success')
def success_page():
	if 'username' in session:
        #return render_template('success.html', user=session['username'])
		return redirect('http://34.64.141.174:5010/')
   #return redirect(url_for('login_page'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login_page'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
