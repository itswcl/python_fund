from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = "testtest and test"

@app.route("/")
def index():
    session["random_number"] = random.randint(1, 100)
    # print(session["random_number"])
    # print(session.clear)
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit_number():
    session["user_input"] = request.form['number']
    return redirect("/result")

@app.route("/result")
def result():
    user_input = int(session["user_input"])
    random_number = int(session["random_number"])
    # print(random_number)
    if user_input > random_number:
        message = " INPUT - LESSER"
        bg_color = "red"
        hit_number = "<div></div>"
    elif user_input < random_number:
        message = "INPUT - HIGHER"
        bg_color = "red"
        hit_number = "<div></div>"
    else:
        message = "RIGHT ON"
        bg_color = "green"
        hit_number = "<input type='submit' name='reset' value='reset'>"

    return render_template("index.html",
                            message=message,
                            color_name=bg_color,
                            hit_number=hit_number)

@app.route("/reset", methods=["GET"])
def reset():
    return index() # either redirect/rendertemp

if __name__ == "__main__":
    app.run(debug=True)