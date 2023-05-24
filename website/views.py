# This file will contain all of the routes related to the core blog application like the homepage etc

from flask import Blueprint, render_template
from flask_login import login_required
views = Blueprint("views", __name__)

@views.route("/")
def home():
    return "Hello"
@views.route("/getstarted")
def getStarted():
    return render_template("getstarted.html")

