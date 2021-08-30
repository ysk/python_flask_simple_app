from flask import Flask, render_template
from flask import Blueprint

app = Flask(__name__)

@app.route('/')
def index():
  title = 'メンバー一覧'
  members = [
      {'name':'山田太郎', 'age':35},
      {'name':'佐藤太郎', 'age':20},
      {'name':'鈴木太郎', 'age':50},
      ]
  return render_template('index.html', title=title, members=members)

if __name__ == '__main__':
  app.run()