# save this as app.py
from flask import Flask
from modules.hello import Hello

app = Flask(__name__)

@app.route("/")
def foo():
    return Hello().call()
