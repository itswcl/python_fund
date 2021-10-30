from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "this is the WCL"

# @app.route("/")
# def index():
#     return render_template("index.html")

@app.route("/")
def form_submit():
    if session["click"]:
        session["click"] += 1
    else:
        session["click"] = 1

    return render_template("index.html", number=session["click"])

@app.route("/clear")
def clear_out():
    session["click"] = 0
    render_template("index.html", number=session["click"])
    return redirect("/")

@app.route("/", methods=["POST"])
def form_click():
    if request.form["click"] == "click":
        session["click"] += 1
    elif request.form["click"] == "reset":
        session["click"] = 0
    elif request.form["click"] == "custom view":
        session["click"] += int(request.form["user_input"])

    render_template("index.html", number=session["click"])
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)