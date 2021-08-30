from flask import Flask,render_template,request,Blueprint

app = Blueprint('action', __name__)

@app.route("/hello")
def hello():
    return "Hello from action.py"

