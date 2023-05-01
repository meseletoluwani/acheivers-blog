# This file will contain all of the routes related to the core blog application like the homepage etc

from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return "Hello"

@views.route("/signup")
def signup():
    return render_template("signup.html")
