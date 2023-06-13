# This file will contain all of the routes related to the core blog application like the homepage etc

from flask import Blueprint, render_template, request, flash, redirect, url_for, abort
from flask_login import login_required, current_user
from .models import Post, User, Comment
from . import db

views = Blueprint("views", __name__)

@views.route("/")
def home():
    posts = Post.query.all()
    return render_template("home.html", user=current_user, posts=posts, length=len(posts))

@views.route("/posts/post/<number>")
def paginated_post(number:int):
    posts = Post.query.all()
    
    length = len(posts)
    print(length)
    to_end = int(number) * 2
    to_start = int(to_end) - 2
    posts = posts[to_start:to_end]
    return render_template("home.html", user=current_user, posts=posts, length=length)



@views.route("/dashboard")
@login_required
def dashboard():
    
    post = Post.query.join(User).filter(User.username == current_user.username).all()
    return render_template("dashboard.html", user=current_user, posts=post)

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
    post = Post.query.filter_by(id=id).first()

    if not post:
        flash("Post does not exist.", category= 'error')
    elif current_user.id != post.id:
        flash('You do not have permission to delete this post.', category= 'error')
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted', category='success')
        
    return redirect(url_for('views.home'))

@views.route("/post/<post_title>", methods = ["GET", "POST"])
@login_required
def view_post(post_title):
    post = Post.query.filter(Post.title == post_title).first()
    return render_template("view_post.html", user=current_user, post=post)


@views.route("/posts/<username>", methods = ["GET", "POST"])
@login_required
def view__user_posts(username):
    post = Post.query.join(User).filter(User.username == username).all()
    return render_template("view_user_posts.html", user=current_user, posts=post)

@views.route("/update-post/<post_id>", methods = ["GET", "POST"])
@login_required
def update_post(post_id):
    if request.method == "GET":
          post = Post.query.filter(Post.id == post_id).first() 
          return render_template("update_post.html", post=post, user=current_user)
    
    
    if request.method == "POST":
        title = request.form.get("title")
        image = request.form.get("image")
        content = request.form.get("content")
        post = Post.query.filter(Post.id == post_id).first() 
        post.title = title
        post.image = image
        post.content = content
        db.session.commit()
        flash("Post updated successfully", category="success")
        return redirect(url_for('views.dashboard'))
    
@views.route("/comment/<post_id>", methods=["POST"])
@login_required
def comment(post_id):
    content = request.form.get("content")

    if not content:
        flash("Comment field cannot be empty!", category="error")
    
    else:
        post = Post.query.filter_by(id=post_id)
        if post:
            comment = Comment(content=content, author=current_user.id, post_id=post_id)
            db.session.add(comment)
            db.session.commit()
            flash("Comment posted!", category="success")
        else:
            flash("Post does not exist", category="error")

    return redirect(url_for("views.home"))

