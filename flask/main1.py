from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>星期五,Jonas您好!</h1>"