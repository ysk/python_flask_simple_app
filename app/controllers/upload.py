from flask import render_template,Blueprint,request
from werkzeug.utils import secure_filename

app = Blueprint('upload', __name__)


@app.route('/upload', methods=['GET'])
def upload():
  title = 'アップロード画面'
  return render_template('upload.html', title=title)


@app.route('/upload', methods=['POST'])
def upload_file():
  title = 'アップロードされた画像'
  if request.form['name'] and request.files['image']:
    f = request.files['image']
    filepath = 'static/' + secure_filename(f.filename)
    f.save(filepath)
  return render_template('result.html', name=request.form['name'], image_url=filepath, title=title)

