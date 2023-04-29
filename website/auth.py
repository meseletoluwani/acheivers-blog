# This file will contain all of the routes related to authentication like the sign up, sign in and sign out

from flask import Blueprint

auth = Blueprint("auth", __name__)

@auth.route("/sign-in")
def sign_in():
    return "Sign In"

@auth.route("/sign-up")
def sign_up():
    return "Sign Up"

@auth.route("/sign-out")
def sign_out():
    return "Sign Out"