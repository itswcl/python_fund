from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/play")
def play_default():
    return render_template("play.html")

@app.route("/play/<int:num>")
def play_number(num):
    return render_template("play.html",num=num)

@app.route("/play/<int:num>/<string:color>")
def play_number_color(num, color):
    return render_template("play.html",num=num, color=color)

if __name__ == "__main__":
    app.run(debug=True)