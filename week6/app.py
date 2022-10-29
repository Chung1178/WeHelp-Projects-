from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
import mysql.connector

app=Flask(__name__, static_folder="static", static_url_path="/")
#靜態資料路徑設定為"/"
app.secret_key="chung@wehelp3"

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="website"
)

mycursor = mydb.cursor()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods=["POST"])
def signup():
    name=request.form["name"]
    username=request.form["user"]
    password=request.form["pw"]
    mycursor.execute('SELECT * FROM member WHERE username = %s', (username,))
    account = mycursor.fetchone()
    if account:
        return redirect("/error?message=帳號已經被註冊")
    elif not name or not username or not password:
        return redirect("/error?message=請輸入註冊資料再註冊")
    else:
        sql='INSERT INTO member (name, username, password) VALUES (%s, %s, %s)'
        val=(name, username, password)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect ("/")
        

@app.route("/signin", methods=["POST"])
def signin():
    username=request.form["user"]
    password=request.form["pw"]
    mycursor.execute('SELECT * FROM member WHERE username = %s AND password = %s', (username, password,))
    account=mycursor.fetchone()
    if account:
        session['id'] = account[0]
        session['name'] = account[1]
        session['username'] = account[2]
        return redirect("/member")
    else:
        return redirect("/error?message=帳號或密碼輸入錯誤")

@app.route("/member")
def member():
    if 'username' in session:
        name=session['name']
        return render_template("member.html", name=name)
    message='尚未登入'
    return render_template("error.html", message=message)

@app.route("/error")
def error():
    message=request.args.get("message",None)
    return render_template("error.html", message=message)

@app.route('/logout')
def logout():
    # 移除 id, name, username
    session.pop('id', None)
    session.pop('name', None)
    session.pop('username', None)
    return redirect("/")


app.run(port=3000)