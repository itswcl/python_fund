from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User

@app.route('/')
def index():
    all_users = User.get_all()
    return render_template('users.html', all_users=all_users)

@app.route('/users')
def display():
    # run User function get all to have all data to render on users.html
    all_users = User.get_all()
    return render_template('users.html', all_users=all_users)

# a page to adding the info - adding part 1
@app.route("/users/add_page")
def add_user_page():
    return render_template("add_user.html")

# post request thur server and redirect back to home page adding part 2
@app.route("/users/add", methods=["POST"])
def add_user():
    print(request.form)
    User.create(request.form)
    return redirect("/")

# to link the user detail with user ID and User function to get specific one with id
@app.route("/users/<int:user_id>")
def display_one(user_id):
    return render_template("user.html", user = User.get_one({'id': user_id}))


# let user update the data in the front
@app.route("/users/<int:user_id>/update_user")
def update_one(user_id):
    return render_template("update_user.html", user = User.get_one({'id': user_id}))


# SENT update request to backend
@app.route("/users/<int:user_id>/update_user_sent", methods=["POST"])
def sent_update_one(user_id):
    data = {
        **request.form,
        'id': user_id
    }
    User.update_value(data)

    return redirect(f"/users/{user_id}")


# DELETE the USER with specific user with userID
@app.route("/users/<int:user_id>/remove")
def remove_user(user_id):
    User.remove_user({'id': user_id})
    return redirect('/')