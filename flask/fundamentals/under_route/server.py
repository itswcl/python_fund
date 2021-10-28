from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<string:name>")
def voice(name):
    return f"Hi {name}!"

@app.route("/repeat/<int:number>/<string:name>")
def calling(number, name):
    line = "\t"
    return f"{name}{line}" * number

# @app.route("/<random>")
# def end(random):
#     return f"Sorry! No response. Try again."

@app.errorhandler(404)
def end(e):
    return f"Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)