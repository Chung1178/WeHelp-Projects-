from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session
from flask import jsonify
import mysql.connector
import json

app=Flask(__name__, static_folder="static", static_url_path="/")
#靜態資料路徑設定為"/"
app.secret_key="chung@wehelp3"

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="website"
)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods=["POST"])
def signup():
    name=request.form["name"]
    username=request.form["user"]
    password=request.form["pw"]
    mycursor = mydb.cursor()
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
    mycursor = mydb.cursor()
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
    mycursor = mydb.cursor()
    if 'username' in session:
        mycursor.execute('SELECT \
            member.name, message.content \
            FROM member \
            INNER JOIN message ON member.id=message.member_id')
        content=mycursor.fetchall()
        name=session['name']
        return render_template("member.html", name=name, content=content)
    message='尚未登入'
    return render_template("error.html", message=message)

@app.route("/message", methods=["POST"])
def message():
    message=request.form["message"]
    mycursor = mydb.cursor()
    if 'username' in session:
        sql='INSERT INTO message (member_id, content) VALUES (%s, %s)'
        val=(session['id'], message)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect ("/member")

@app.route("/error")
def error():
    message=request.args.get("message",None)
    return render_template("error.html", message=message)

@app.route("/logout")
def logout():
    # 移除 id, name, username
    session.pop("id", None)
    session.pop("name", None)
    session.pop("username", None)
    return redirect("/")

@app.route("/api/member", methods=["GET"])
def search_member():
    err_json_message={"data": None}
    if 'username' in session:
        username=request.args.get("username",None)
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM member WHERE username = %s', (username,))
        account=mycursor.fetchone()
        if account:
            sql='SELECT id, name, username FROM member WHERE username = %s'
            val=(username,)
            mycursor.execute(sql, val)
            user_info=mycursor.fetchone()
            id=user_info[0]
            name=user_info[1]
            username=user_info[2]
            data={"data":{"id":id, "name":name, "username":username}}
            return jsonify(data)
        else:
            return jsonify(err_json_message)
    return jsonify(err_json_message)

@app.route("/api/member", methods=["PATCH"])
def update_member_name():
    err_json_message={"error": True}
    if 'username' in session:
        username=session["username"]
        newname=request.json["name"]
        mycursor = mydb.cursor()
        mycursor.execute('UPDATE member SET name = %s WHERE username = %s', (newname, username))
        mydb.commit()
        result={"ok":True}
        return jsonify(result)
    return jsonify(err_json_message)                

app.run(port=3000)