from flask import render_template,Blueprint,request

app = Blueprint('login', __name__)


@app.route('/login', methods=['GET'])
def login():
  title = 'ログイン'
  return render_template('login.html', title=title)


@app.route('/login', methods=['POST'])
def login_post():
  title = 'ログイン'
  if request.form['username'] and request.form['email']:
    return render_template('check.html', email=request.form['email'], username=request.form['username'], title=title)
  else:
    return render_template('error.html', title=title)

