from flask import render_template,Blueprint

app = Blueprint('index', __name__)

@app.route('/', methods=['GET'])
def index():
    title = 'メンバー一覧'
    members = [
      {'id':1, 'name':'山田太郎', 'age':35},
      {'id':2, 'name':'佐藤太郎', 'age':20},
      {'id':3, 'name':'鈴木太郎', 'age':50},
      ]
    return render_template('index.html', title=title, members=members)