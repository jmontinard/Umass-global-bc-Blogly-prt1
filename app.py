
"""Blogly application."""

from flask import Flask, request, redirect, render_template,flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User
from datetime import datetime,date
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'ihaveasecret'
# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# toolbar = DebugToolbarExtension(app)
with app.app_context():
     connect_db(app)
     db.create_all()

# home and err routes

@app.route("/")
def list_users():
    """redirecting  to list of all users"""
   
    return redirect("/users")

# users routes

@app.route("/users")
def show_all_users():
    """returns a list of all users """
    users = User.query.order_by(User.first_name, User.last_name).all()
    
    return render_template("index.html", users=users)
    # return render_template('index.html')
    # return ("<h1> YOOOO! </h1>")
   


@app.route("/users/new", methods=["GET"])
def add_users():
    """displays the route to show add user form """
    return render_template("addUser.html")


@app.route("/users/new", methods=["POST"])
def post_new_users():
    """add user and redirect to user lsit """
    firstName = request.form['first_name']
    lastName = request.form['last_name']
    imgUrl = request.form['image_url']

    user = User(first_name=firstName, last_name=lastName, image_url=imgUrl)

    db.session.add(user)
    db.session.commit()
    flash(f"{user.get_fullname} has been added.")
    return redirect("/users")


@app.route("/users/<int:user_id>")
def show_user(user_id):
    """Show all info on a selected user."""

    user = User.query.get_or_404(user_id)
    return render_template("userDetails.html", user=user)


@app.route("/users/<int:user_id>/edit")
def edit_users(user_id):
    """Edit info on a selected user."""

    user = User.query.get_or_404(user_id)
    return render_template("editUser.html", user=user)


@app.route("/users/<int:user_id>/edit", methods=["POST"])
def post_edit_users(user_id):
    """edits user and redirect to user lsit """
    user = User.get_or_404(user_id)
    # THIS BELOW WILL WORK IF WE NOT EXPLICILTY SETTIGN THE VALUE

    # firstName = request.form['first_name']
    # lastName = request.form['last_name']
    # imgUrl = request.form['image_url']
    # firstName = firstName if firstName != " " else user.first_name
    # lastName = lastName if lastName != " " else user.last_name
    # imgUrl = imgUrl if imgUrl != " " else user.image_url
    # firstName =  request.form['first_name'] or user.first_name
    # lastName = lastName if lastName != " " else user.last_name
    # imgUrl = imgUrl if imgUrl != " " else user.image_url
    # user.first_name = firstName
    # user.last_name = lastName
    # user.image_url =imgUrl


    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['image_url']

    # edited_user = User(first_name=firstName, last_name=lastName, image_url=imgUrl)
    print(user)
    db.session.add(user)
    db.session.commit()
    flash(f"{user.get_fullname} has been edited.")
    return redirect("/users")



@app.route("/users/<int:user_id>/delete", methods=["POST"])
def delete_users(user_id):
    """displays name of deleted user and redirects user back to user list."""

    user = User.query.get_or_404(user_id)
    # User.query.filter_by(id=user.id).delete()
    db.session.delete(user)
    db.session.commit()
    flash(f"{user.get_fullname} has been deleted.")

    return redirect("/users")


