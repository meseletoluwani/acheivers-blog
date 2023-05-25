# This file will contain all of the routes related to the core blog application like the homepage etc

from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
def home():
    posts = post.query.all("home.html", user=current_user, posts= user.post)

return render_template()


 