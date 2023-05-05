from flask import Flask
import felix


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/vanfelix")
def hello_world2():
    return felix.ditisvanfelix()