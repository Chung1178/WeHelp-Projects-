from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session

app=Flask(__name__, static_folder="static", static_url_path="/")
#靜態資料路徑設定為"/"
app.secret_key="chung@wehelp3"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin", methods=["POST"])
def signin():
    account=request.form["user"]
    password=request.form["pw"]
    if account=="test" and password=="test":
        session['username'] = account
        return redirect("/member")
    elif account=="" or password=="":
        return redirect("/error?message=請輸入帳號、密碼")
    else:
        return redirect("/error?message=帳號或密碼輸入錯誤")

@app.route("/member")
def member():
    if 'username' in session:
        return render_template("member.html")
    return '尚未登入'

@app.route("/error")
def error():
    message=request.args.get("message",None)
    return render_template("error.html", message=message)

@app.route('/logout')
def logout():
    # 移除 username
    session.pop('username', None)
    return redirect("/")


app.run(port=3000)