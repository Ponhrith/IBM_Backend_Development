from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "<b> Flask Application </b>"