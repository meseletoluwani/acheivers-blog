# This file will contain all of the routes related to the core blog application like the homepage etc

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Post
from . import db

views = Blueprint("views", __name__)

@views.route("/")
def home():
    posts = post.query.all("home.html", user=current_user, posts= user.post)

return render_template()


 

@views.route("/getstarted")
def getStarted():
    return render_template("getstarted.html", user=current_user)

@views.route("/post", methods = ["GET", "POST"])
@login_required
def create_post():
    if request.method == "POST":
        title = request.form.get("title")
        image = request.form.get("image")
        content = request.form.get("content")

        if not title:
            flash("Tile must not be empty", category="error")
        elif not image:
            flash("Please input a url link to your preferred email!", category="error")
        elif not content:
            flash("Content cannot be empty", category="error")
        else:
            post = Post(title=title, image=image, content=content, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash("Post created successfully!", category="success")
            return redirect(url_for("views.home"))
    return render_template("post.html", user=current_user)


@views.route("/delete-post/<id>")
@login_required
def delete_post(id):
    post = post.query.filter_by(id=id).first()

    if not post:
        flash("post does not exist.", category= 'error')
    elif current_user.id != post.id:
        flash('you do not have permission to delete this post.', category= 'error')
    else:
        db.session.delete(post)
        db.session.commit()
        flash('post deleted', category='success')
        
    return redirect(url_for('views.home'))

