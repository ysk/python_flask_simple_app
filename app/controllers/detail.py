from flask import render_template,Blueprint

app = Blueprint('detail', __name__)

@app.route('/<int:user_id>', methods=['GET'])
def detail(user_id):

    ##この辺の値はDBに格納
    user_name = '山田太郎'
    message   = 'はじめまして山田太郎です。'
    title     = '詳細情報'
    return render_template('detail.html', user_id=user_id, user_name=user_name, message=message, title=title)