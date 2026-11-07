from flask import Flask, render_template, request, redirect

app = Flask(__name__)

if __name__ == "_main_":
    app.run(debug=True)

@app.route("/")
def index():
  return render_template("intro.html")

@app.route("/layout")
def layout():
  return render_template("layout.html")


@app.route("/menu.html")
def menu():
  return render_template("menu.html")