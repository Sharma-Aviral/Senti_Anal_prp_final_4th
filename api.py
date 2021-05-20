from flask import Flask
from flask import render_template
import senti

# app = Flask(__name__ ,static_url_path="/static",static_folder="/static")

# @app.route("/")
# def index(): 
#  return render_template("index.html")

senti.twitter_anal("BeerBicepsGuy" , 10000)
