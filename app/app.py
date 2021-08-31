from flask import Flask
from controllers import index,action,detail,search,login,upload

app = Flask(__name__)

app.register_blueprint(action.app)
app.register_blueprint(index.app)
app.register_blueprint(detail.app)
app.register_blueprint(search.app)
app.register_blueprint(login.app)
app.register_blueprint(upload.app)

if __name__ == '__main__':
  app.run()

