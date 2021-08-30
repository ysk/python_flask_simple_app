from flask import Flask,render_template,request,Blueprint

app = Blueprint('search', __name__)

@app.route('/search', methods=['GET'])
def search():
  q = request.args.get('q', '')
  # http://localhost:5000/search?q=abcd
  # abcdを返す
  return q