from flask import Flask, render_template, redirect, request
from user import User

app = Flask(__name__)
app.secret_key = "TEST"


@app.route('/')
def index():
    all_users = User.get_all()
    print(all_users)
    return render_template('users.html', all_users=all_users)

@app.route("/users/add_page")
def add_user_page():
    return render_template("add_user.html")


@app.route("/users/add", methods=["POST"])
def add_user():
    print(request.form)
    User.create(request.form)

    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)