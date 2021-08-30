from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    title = 'メンバー一覧'
    members = [
      {'id':1, 'name':'山田太郎', 'age':35},
      {'id':2, 'name':'佐藤太郎', 'age':20},
      {'id':3, 'name':'鈴木太郎', 'age':50},
      ]
    return render_template('index.html', title=title, members=members)


@app.route('/<int:user_id>', methods=['GET'])
def detail(user_id):

    ##この辺の値はDBに格納
    user_name = '山田太郎'
    message   = 'はじめまして山田太郎です。'
    return render_template('detail.html', user_id=user_id, user_name=user_name, message=message)


@app.route('/search', methods=['GET'])
def search():
  q = request.args.get('q', '')
  # http://localhost:5000/search?q=abcd
  # abcdを返す
  return q

##実行
if __name__ == '__main__':
  app.run()

