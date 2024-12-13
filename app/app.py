import sys
import os

# プロジェクトのルートディレクトリをインポートパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.models import OnegaiContent
from flask import Flask, request, render_template
from models.database import db_session
from datetime import datetime

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    name = request.args.get("name")
    all_onegai = OnegaiContent.query.all()
    return render_template("index.html", name=name, all_onegai=all_onegai)

@app.route("/index", methods=["post"])
def post():
    name = request.form["name"]
    all_onegai = OnegaiContent.query.all()
    return render_template("index.html", name=name, all_onegai=all_onegai)

@app.route("/add",methods=["post"])
def add():
    title = request.form["title"]
    body = request.form["body"]
    content = OnegaiContent(title,body,datetime.now())
    db_session.add(content)
    db_session.commit()
    return index()

@app.route("/update",methods=["post"])
def update():
    content = OnegaiContent.query.filter_by(id=request.form["update"]).first()
    content.title = request.form["title"]
    content.body = request.form["body"]
    db_session.commit()
    return index()

@app.route("/delete",methods=["post"])
def delete():
    id_list = request.form.getlist("delete")
    for id in id_list:
        content = OnegaiContent.query.filter_by(id=id).first()
        db_session.delete(content)
    db_session.commit()
    return index()

if __name__ == "__main__":
    app.run(debug=True)
