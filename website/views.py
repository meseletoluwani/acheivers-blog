# This file will contain all of the routes related to the core blog application like the homepage etc

from flask import Blueprint

views = Blueprint("views", __name__)

@views.route("/")
def home():
    return "Hello"