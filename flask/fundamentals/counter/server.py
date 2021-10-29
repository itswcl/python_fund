from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "this is the WCL"

# @app.route("/")
# def index():
#     return render_template("index.html")

@app.route("/", methods=["GET"])
def form_submit():

    if session["click"]:
        session["click"] += 1
    else:
        session["click"] = 1

    return render_template("index.html", number=session["click"])

# @app.route("/")
# def clear():
#     session.clear()
#     return render_template(
#         "index.html",
#         number = session["number"]
#     )

if __name__ == "__main__":
    app.run(debug=True)
