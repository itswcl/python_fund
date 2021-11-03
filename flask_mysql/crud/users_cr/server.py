from flask import Flask, render_template, redirect, request
from user import User

app = Flask(__name__)
app.secret_key = "TEST"

@app.route('/')
def index():
    all_users = User.get_all()

    return render_template('index.html', all_users=all_users)

if __name__ == '__main__':
    app.run(debug=True)