import sys
import os

# プロジェクトのルートディレクトリをインポートパスに追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.models import OnegaiContent
from flask import Flask, request, render_template

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

if __name__ == "__main__":
    app.run(debug=True)
