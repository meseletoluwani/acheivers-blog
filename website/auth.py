# This file will contain all of the routes related to authentication like the sign up, sign in and sign out

from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__)

@auth.route("/signin", methods = ["GET", "POST"])
def sign_in():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect password!", category="error")
        else:
            flash("Account does not exist", category="error")
    return render_template("signin.html")

@auth.route("/signup", methods = ["GET", "POST"])
def signup():
    if request.method == "POST":
        fullname = request.form.get("fullname")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        username_exists = User.query.filter_by(username=username).first()

        if username_exists:
            flash("Username is already in use", category="error")
        elif password1 != password2:
            flash("Passwords don't match", category="error")
        elif len(password1) < 7:
            flash("Password must be at least 7 characters!", category="error")
        elif len(fullname) < 7:
            flash("Name must be at least 7 characters!", category="error")
        elif len(username) < 4:
            flash("Username is too short", category="error")
        else:
            new_user = User(fullname=fullname, username=username, password=generate_password_hash(password1, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Account created successfully", category="success")
            return redirect(url_for("views.home"))
    return render_template("signup.html")

@auth.route("/sign-out")
@login_required
def sign_out():
    logout_user()
    return redirect(url_for("auth.sign_in"))