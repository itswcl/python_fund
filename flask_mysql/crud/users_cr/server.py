from flask import Flask, render_template, redirect, request
from werkzeug.utils import get_content_type
from user import User

app = Flask(__name__)
app.secret_key = "TEST"


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


@app.route("/users/<int:user_id>")
def display_one(user_id):
    return render_template("user.html", user = User.get_one({'id': user_id}))


if __name__ == '__main__':
    app.run(debug=True)