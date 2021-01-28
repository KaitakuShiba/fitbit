# save this as app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def render_register_html():
    return render_template( 'index.html')
