# save this as app.py
from flask import Flask, render_template
from modules.fitbit import Fitbit
from modules.fitbir_api_registration import FitbirApiRegistration

app = Flask(__name__)

@app.route("/", methods=["GET"])
def render_register_html():
    return render_template( 'index.html')

@app.route("/registration", methods=["POST"])
def register():
    return FitbirApiRegistration().call()

@app.route("/fitbit")
def fitbit():
    return Fitbit().call()
