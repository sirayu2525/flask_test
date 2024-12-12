# #Flaskとrender_template（HTMLを表示させるための関数）をインポート
# from flask import Flask,render_template

# #Flaskオブジェクトの生成
# app = Flask(__name__)


# #「/」へアクセスがあった場合に、"Hello World"の文字列を返す
# @app.route("/")
# def hello():
#     return "Hello World"


# #「/index」へアクセスがあった場合に、「index.html」を返す
# @app.route("/index")
# def index():
#     return render_template("index.html")


# #おまじない
# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask,render_template,request

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    name = request.args.get("name")
    okyo = ["色不異空","空不異色","色即是空","空即是色"]
    return render_template("index.html",name=name,okyo=okyo)

@app.route("/index",methods=["post"])
def post():
    name = request.form["name"]
    #request.form は、POSTリクエストの本文に含まれるフォームデータを取得するためのオブジェクト
    okyo = ["色不異空", "空不異色", "色即是空", "空即是色"]
    return render_template("index.html", name=name, okyo=okyo)

if __name__ == "__main__":
    app.run(debug=True)
