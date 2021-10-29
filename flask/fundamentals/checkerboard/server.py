from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<int:x>")
def num_chart_x(x):
    return render_template("index.html", x=x)

@app.route("/<int:x>/<int:y>")
def num_chart_y(x, y):
    return render_template("index.html", x=x, y=y)

@app.route("/<int:x>/<int:y>/<string:color1>")
def num_chart_color(x, y, color1):
    return render_template("index.html", x=x, y=y, color1=color1)

@app.route("/<int:x>/<int:y>/<string:color1>/<string:color2>")
def num_chart_double_color(x, y, color1, color2):
    return render_template("index.html", x=x, y=y, color1=color1, color2=color2)

if __name__ == "__main__":
    app.run(debug=True)